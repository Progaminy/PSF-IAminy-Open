# -*- coding: utf-8 -*-
"""Rotas de contexto, cálculo simples, índice total e não encontrado."""
from __future__ import annotations

from typing import Any

from ensino.resolvedor_exercicios import resolver as resolver_exercicio
from nucleo.chat_base_canonica import obter_registro
from nucleo.chat_estilo import resposta_natural
from nucleo.chat_formatacao import _bloco_final, _fonte_publica_registro, _formatar_registro, _limpar_rastro_tecnico
from nucleo.chat_texto import detectar_modo, detectar_tom, normalizar
from nucleo.chat_tipos import RespostaChat
from nucleo.indexador_total import buscar_total

def _responder_contexto(texto: str, contexto: dict[str, Any] | None) -> RespostaChat | None:
    contexto = contexto if isinstance(contexto, dict) else {}
    t = normalizar(texto)
    registro_id = str(contexto.get("ultimo_registro_id") or "")
    if not registro_id:
        return None
    registro = obter_registro(registro_id)
    if registro is None:
        return None
    modo = detectar_modo(texto)
    if modo in {"simples", "passos", "exemplo", "exercicios", "cientista"}:
        return _formatar_registro(registro, modo, 92)
    if any(p in t for p in ("onde esta este conhecimento", "de que etapa veio", "tem teste", "tem aula", "tem lacuna", "contradiz algo anterior", "esta pronto para uso")):
        dados = registro.dados
        linhas = [
            f"Último assunto: {registro.titulo}.",
            f"Fonte viva: {_fonte_publica_registro(registro)}.",
            "O chat não organiza esta resposta por etapas; o rastro antigo fica só para auditoria.",
            f"Tem aula: {'sim' if dados.get('aula_direta') or dados.get('aula_detalhada') else 'não'}.",
            f"Tem teste: {'sim' if dados.get('testes') else 'não'}.",
            f"Tem lacuna: {'sim' if dados.get('tem_lacuna') else 'não'}.",
            "Contradição detectada nesta rota: não.",
        ]
        return RespostaChat(
            "\n".join(linhas),
            "auditoria_contextual",
            "pergunta",
            88,
            origem=f"base_canonica:{registro.id}",
            conhecimento_encontrado=True,
            contexto_chat=contexto,
        )
    return None


def _responder_resolvedor(texto: str) -> RespostaChat | None:
    if not (any(c.isdigit() for c in texto) or any(op in texto for op in ("+", "-", "×", "*", "÷", "/")) or "calcula" in normalizar(texto)):
        return None
    resolucao = resolver_exercicio(texto)
    if resolucao.resolvida:
        resposta = resposta_natural(
            resolucao.raciocinio,
            resolucao.resposta,
            origem="resolvedor_exercicios",
            padrao=resolucao.padrao,
        )
        return RespostaChat(
            resposta,
            "resolvido",
            "pergunta",
            86,
            origem="resolvedor_exercicios",
            conhecimento_encontrado=True,
            contexto_chat={"ultimo_titulo": resolucao.padrao or "exercício", "ultima_origem": "resolvedor_exercicios"},
        )
    if resolucao.padrao:
        return RespostaChat(
            resolucao.raciocinio + "\n\n" + _bloco_final(64, "ensino.resolvedor_exercicios", ["padrão reconhecido sem solução segura"]),
            "lacuna_resolvedor",
            "pergunta",
            64,
            origem="resolvedor_exercicios",
            conhecimento_encontrado=True,
            lacunas=["padrão reconhecido sem solução segura"],
            deve_melhorar=True,
        )
    return None


def _responder_indice_total(texto: str) -> RespostaChat | None:
    resultados = buscar_total(texto, limite=1)
    if not resultados:
        return None
    resultado = resultados[0]
    registro = resultado.registro
    if registro is None or resultado.score < 28:
        return None
    trecho = registro.trecho
    if len(trecho) > 700:
        trecho = trecho[:700].rstrip() + "..."
    trecho_publico = _limpar_rastro_tecnico(trecho)
    titulo_publico = _limpar_rastro_tecnico(registro.titulo)
    corpo = (
        "Encontrei isto no índice total do projeto materializado. Não vou fingir que é resposta final; vou mostrar como registro bruto, sem apresentar o conhecimento como blocos antigos.\n\n"
        "Fonte: índice total do projeto\n"
        f"Tipo: {registro.tipo}; score: {resultado.score}\n"
        f"Título: {titulo_publico}\n\n"
        f"Trecho: {trecho_publico}\n\n"
        "Próximo passo PSF: transformar este trecho em conhecimento puro materializado, com conceito, dependências, teste e lacuna explícita se ele for usado."
    )
    return RespostaChat(
        corpo,
        "indice_total",
        "pergunta",
        min(78, 45 + resultado.score),
        origem=f"indice_total:{registro.caminho}",
        conhecimento_encontrado=True,
        lacunas=["cobertura canônica ainda curta"],
        contexto_chat={"ultimo_titulo": registro.titulo, "ultima_origem": registro.caminho},
    )


def _responder_nao_encontrado(texto: str) -> RespostaChat:
    return RespostaChat(
        "Não encontrei isto materializado na base canônica nem no índice local com confiança suficiente. Posso criar uma entrada nova para investigar, mas não vou fingir que já sei.",
        "nao_materializado",
        detectar_tom(texto),
        35,
        origem="sem_rota_segura",
        conhecimento_encontrado=False,
        lacunas=["conhecimento ou rota não materializados"],
        fallback_usado=True,
        deve_melhorar=True,
    )

