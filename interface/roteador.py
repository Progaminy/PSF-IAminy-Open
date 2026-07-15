"""Roteador HTTP do PSF-IAminy -- lógica pura, sem socket.

Cada método devolve exatamente o que a resposta HTTP precisa (estado +
corpo), para ser testável diretamente (`testes/test_interface_servidor.py`)
sem abrir nenhuma porta de rede. `servidor.py` é só a casca fina que liga
isto a `http.server`.
"""
from __future__ import annotations

import base64
from pathlib import Path
from typing import TYPE_CHECKING

from ensino.leitura_documentos import ler_anexo_bytes
from ensino.navegacao_pacotes import (
    alcancaveis_de,
    caminho_mais_curto,
    caminho_mais_longo,
    componentes_conectados,
    onde_estou,
)
from ensino.pacotes_reais import (
    gerar_corrigidos,
    gerar_exercicios,
    pacotes_matematica,
    pacotes_portugues,
    verificar_resposta,
)
from nucleo.chat_vivo import responder as responder_chat
from nucleo.problemas_abertos import listar_problemas

from .conversas import ArmazemConversas
from .mapa_conhecimento import mapa_completo

_PACOTES_POR_AREA = {"portugues": pacotes_portugues, "matematica": pacotes_matematica}

if TYPE_CHECKING:
    from ensino.dialogo import MotorDialogo

ESTATICO_PADRAO = Path(__file__).resolve().parent / "estatico"

_TIPOS_CONTEUDO = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".svg": "image/svg+xml",
}


class Roteador:
    def __init__(
        self,
        armazem: "ArmazemConversas | None" = None,
        dialogo: "MotorDialogo | None" = None,
        estatico: "Path | str | None" = None,
    ) -> None:
        self.armazem = armazem or ArmazemConversas()
        # `dialogo` fica None por omissão: `ensino.dialogo.MotorDialogo` (entrevista/
        # identidade do criador) ainda não existe nesta árvore -- `nucleo.chat_vivo`
        # já tolera `dialogo=None` para todo o resto do chat (mesmo padrão usado em
        # `nucleo/chat_rotas_basicas._obter_dialogo`).
        self.dialogo = dialogo
        self.estatico = Path(estatico).resolve() if estatico is not None else ESTATICO_PADRAO.resolve()

    # ------------------------------------------------------------------
    # Ficheiros estáticos
    # ------------------------------------------------------------------

    def pagina_inicial(self) -> tuple[int, str, bytes]:
        return self.arquivo_estatico("index.html")

    def arquivo_estatico(self, caminho_relativo: str) -> tuple[int, str, bytes]:
        alvo = (self.estatico / caminho_relativo).resolve()
        dentro_da_pasta = alvo == self.estatico or self.estatico in alvo.parents
        if not dentro_da_pasta:
            return 403, "text/plain; charset=utf-8", b"acesso negado"
        if not alvo.exists() or not alvo.is_file():
            return 404, "text/plain; charset=utf-8", b"nao encontrado"
        tipo = _TIPOS_CONTEUDO.get(alvo.suffix, "application/octet-stream")
        return 200, tipo, alvo.read_bytes()

    # ------------------------------------------------------------------
    # API de conversas
    # ------------------------------------------------------------------

    def listar_conversas(self) -> tuple[int, dict]:
        return 200, {"conversas": self.armazem.listar()}

    def mapa_conhecimento(self) -> tuple[int, dict]:
        return 200, mapa_completo()

    def listar_aulas(self, area: str) -> tuple[int, dict]:
        gerador = _PACOTES_POR_AREA.get(area)
        if gerador is None:
            return 404, {"erro": f"área desconhecida: {area!r}"}
        pacotes = gerador()
        return 200, {
            "area": area,
            "pacotes": [
                {"codigo": p.codigo, "conceitos": [a.conceito for a in p.aulas]}
                for p in pacotes
            ],
        }

    def obter_pacote(self, area: str, codigo: str) -> tuple[int, dict]:
        gerador = _PACOTES_POR_AREA.get(area)
        if gerador is None:
            return 404, {"erro": f"área desconhecida: {area!r}"}
        pacote = next((p for p in gerador() if p.codigo == codigo), None)
        if pacote is None:
            return 404, {"erro": f"pacote não encontrado: {codigo!r}"}
        aulas = []
        for aula in pacote.aulas:
            aulas.append({
                "conceito": aula.conceito,
                "tema": aula.tema,
                "texto": aula.texto(),
                "completa": aula.completa,
                "exercicios": [
                    {"tipo": e.tipo, "pergunta": e.pergunta} for e in gerar_exercicios(aula)
                ],
                "corrigidos": [
                    {"pergunta": c.exercicio.pergunta, "resposta": c.resposta_modelo}
                    for c in gerar_corrigidos(aula)
                ],
            })
        return 200, {"codigo": pacote.codigo, "area": area, "aulas": aulas}

    def verificar_exercicio(self, area: str, conceito: str, tipo: str, resposta: str) -> tuple[int, dict]:
        gerador = _PACOTES_POR_AREA.get(area)
        if gerador is None:
            return 404, {"erro": f"área desconhecida: {area!r}"}
        aula = next(
            (a for p in gerador() for a in p.aulas if a.conceito == conceito), None
        )
        if aula is None:
            return 404, {"erro": f"conceito não encontrado: {conceito!r}"}
        exercicio = next((e for e in gerar_exercicios(aula) if e.tipo == tipo), None)
        if exercicio is None:
            return 404, {"erro": f"exercício {tipo!r} não existe para {conceito!r}"}
        resultado = verificar_resposta(exercicio, resposta)
        return 200, {
            "correto": resultado.correto,
            "semelhanca": resultado.semelhanca,
            "resposta_modelo": resultado.resposta_modelo,
            "metodo": resultado.metodo,
        }

    def onde_estou(self, area: str, conceito: str) -> tuple[int, dict]:
        if area not in _PACOTES_POR_AREA:
            return 404, {"erro": f"área desconhecida: {area!r}"}
        loc = onde_estou(conceito, area)
        if loc is None:
            return 404, {"erro": f"conceito não encontrado: {conceito!r}"}
        return 200, {
            "conceito": loc.conceito, "tema": loc.tema,
            "depende_de": list(loc.depende_de), "dependentes": list(loc.dependentes),
            "e_raiz": loc.e_raiz, "e_folha": loc.e_folha,
            "alcancaveis": list(alcancaveis_de(conceito, area)),
        }

    def navegar(self, area: str, origem: str, destino: str, modo: str) -> tuple[int, dict]:
        if area not in _PACOTES_POR_AREA:
            return 404, {"erro": f"área desconhecida: {area!r}"}
        funcao = caminho_mais_longo if modo == "longo" else caminho_mais_curto
        caminho = funcao(origem, destino, area)
        return 200, {
            "origem": caminho.origem, "destino": caminho.destino, "existe": caminho.existe,
            "conceitos": list(caminho.conceitos), "comprimento": caminho.comprimento, "modo": modo,
        }

    def componentes(self, area: str) -> tuple[int, dict]:
        if area not in _PACOTES_POR_AREA:
            return 404, {"erro": f"área desconhecida: {area!r}"}
        comps = componentes_conectados(area)
        return 200, {
            "area": area,
            "total_componentes": len(comps),
            "componentes": [list(c) for c in comps],
        }

    def problemas_abertos(self) -> tuple[int, dict]:
        problemas = listar_problemas()
        return 200, {
            "total": len(problemas),
            "problemas": [
                {
                    "id": p["id"], "titulo": p["titulo"], "bloco": p["bloco"],
                    "estado": p["estado"], "resposta": p["resposta"],
                    "plano_investigacao": p["plano_investigacao"],
                }
                for p in problemas
            ],
        }

    def criar_conversa(self) -> tuple[int, dict]:
        return 200, self.armazem.criar()

    def obter_conversa(self, id_conversa: str) -> tuple[int, dict]:
        conversa = self.armazem.carregar(id_conversa)
        if conversa is None:
            return 404, {"erro": "conversa não encontrada"}
        return 200, conversa

    def remover_conversa(self, id_conversa: str) -> tuple[int, dict]:
        if not self.armazem.remover(id_conversa):
            return 404, {"erro": "conversa não encontrada"}
        return 200, {"removida": id_conversa}

    def renomear_conversa(self, id_conversa: str, titulo: str) -> tuple[int, dict]:
        titulo_limpo = titulo.strip()
        if not titulo_limpo:
            return 400, {"erro": "título não pode ficar vazio"}
        conversa = self.armazem.renomear(id_conversa, titulo_limpo)
        if conversa is None:
            return 404, {"erro": "conversa não encontrada"}
        return 200, conversa

    def enviar_mensagem(self, id_conversa: str, texto: str) -> tuple[int, dict]:
        estado_psf = self.armazem.obter_estado(id_conversa, "estado_psf", None)
        reconhecido = bool(self.armazem.obter_estado(id_conversa, "psf_reconhecido", False))
        contexto_dialogo = self.armazem.obter_estado(id_conversa, "contexto_dialogo", {})
        contexto_chat = self.armazem.obter_estado(id_conversa, "contexto_chat_vivo", {})
        conversa = self.armazem.adicionar_mensagem(id_conversa, "aluno", texto)
        if conversa is None:
            return 404, {"erro": "conversa não encontrada"}
        resposta = responder_chat(
            estado_psf=estado_psf,
            reconhecido=reconhecido,
            contexto=contexto_chat if isinstance(contexto_chat, dict) else {},
            contexto_dialogo=contexto_dialogo if isinstance(contexto_dialogo, dict) else {},
            dialogo=self.dialogo,
            id_conversa=id_conversa,
            mensagem=texto,
        )
        self.armazem.definir_estado(id_conversa, "estado_psf", resposta.estado_psf)
        if resposta.contexto_dialogo is not None:
            self.armazem.definir_estado(id_conversa, "contexto_dialogo", resposta.contexto_dialogo)
        if resposta.contexto_chat is not None:
            self.armazem.definir_estado(id_conversa, "contexto_chat_vivo", resposta.contexto_chat)
        if resposta.intencao == "entrevista_psf_concluida":
            # a entrevista completa NESTA conversa é o que desbloqueia
            # conhecimento restrito (ver ensino/dialogo.py) -- não é global
            # nem automático só por o facto existir noutra conversa.
            self.armazem.definir_estado(id_conversa, "psf_reconhecido", True)
        conversa = self.armazem.adicionar_mensagem(id_conversa, "assistente", resposta.texto)
        return 200, conversa

    def enviar_anexo(self, id_conversa: str, nome: str, conteudo_base64: str) -> tuple[int, dict]:
        if self.armazem.carregar(id_conversa) is None:
            return 404, {"erro": "conversa não encontrada"}
        try:
            dados = base64.b64decode(conteudo_base64, validate=True)
            extraidos = ler_anexo_bytes(nome, dados)
        except Exception as erro:  # noqa: BLE001 -- qualquer falha de leitura vira resposta 400 honesta.
            return 400, {"erro": f"não consegui ler o anexo {nome!r}: {erro}"}

        self.armazem.adicionar_mensagem(id_conversa, "aluno", f"[anexo: {nome}]")
        resposta = responder_chat(
            f"resolve o anexo {nome}",
            id_conversa=id_conversa,
            anexos=extraidos,
            dialogo=self.dialogo,
        )
        conversa = self.armazem.adicionar_mensagem(id_conversa, "assistente", resposta.texto)
        return 200, conversa
