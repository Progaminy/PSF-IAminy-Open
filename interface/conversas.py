"""Armazém de conversas do PSF-IAminy -- gravação automática em JSON.

Uma conversa é um ficheiro `<id>.json`. Cada mensagem enviada grava o
ficheiro de novo -- não há botão de "guardar": a gravação é automática,
como pedido. O título nasce da primeira mensagem do aluno: as primeiras
palavras, resumidas -- "inteligente" no sentido de nascer do conteúdo
real da conversa, não de um modelo de linguagem; "genérico" porque o
mesmo heurístico serve qualquer assunto, sem regra por área.
"""
from __future__ import annotations

import json
import secrets
from datetime import datetime, timezone
from pathlib import Path

CAMINHO_PADRAO = Path(__file__).resolve().parent / "dados" / "conversas"

TITULO_SEM_MENSAGENS = "Nova conversa"


def _agora() -> str:
    return datetime.now(timezone.utc).isoformat()


def titulo_automatico(primeira_mensagem: str, maximo_palavras: int = 6) -> str:
    palavras = primeira_mensagem.split()
    if not palavras:
        return TITULO_SEM_MENSAGENS
    resumo = " ".join(palavras[:maximo_palavras])
    if len(palavras) > maximo_palavras:
        resumo += "…"
    return resumo[0].upper() + resumo[1:]


class ArmazemConversas:
    """Conversas persistidas em `<pasta>/<id>.json`, uma por ficheiro."""

    def __init__(self, pasta: "Path | str | None" = None) -> None:
        self.pasta = Path(pasta) if pasta is not None else CAMINHO_PADRAO
        self.pasta.mkdir(parents=True, exist_ok=True)

    def _caminho(self, id_conversa: str) -> Path:
        return self.pasta / f"{id_conversa}.json"

    def criar(self) -> dict:
        id_conversa = secrets.token_hex(6)
        conversa = {
            "id": id_conversa,
            "titulo": TITULO_SEM_MENSAGENS,
            "criado_em": _agora(),
            "mensagens": [],
        }
        self._guardar(conversa)
        return conversa

    def carregar(self, id_conversa: str) -> "dict | None":
        caminho = self._caminho(id_conversa)
        if not caminho.exists():
            return None
        return json.loads(caminho.read_text(encoding="utf-8"))

    def _guardar(self, conversa: dict) -> None:
        self._caminho(conversa["id"]).write_text(
            json.dumps(conversa, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    def adicionar_mensagem(self, id_conversa: str, papel: str, texto: str) -> "dict | None":
        conversa = self.carregar(id_conversa)
        if conversa is None:
            return None
        if not conversa["mensagens"] and papel == "aluno":
            conversa["titulo"] = titulo_automatico(texto)
        conversa["mensagens"].append({"papel": papel, "texto": texto, "quando": _agora()})
        self._guardar(conversa)
        return conversa

    def renomear(self, id_conversa: str, novo_titulo: str) -> "dict | None":
        conversa = self.carregar(id_conversa)
        if conversa is None:
            return None
        conversa["titulo"] = novo_titulo
        self._guardar(conversa)
        return conversa

    def definir_estado(self, id_conversa: str, chave: str, valor: object) -> None:
        """Guarda um pedaço pequeno de estado da conversa (ex.: 'estamos à
        espera dos dados do PSF humano?') junto da própria conversa --
        evita um novo ficheiro/registo só para uma bandeira."""
        conversa = self.carregar(id_conversa)
        if conversa is None:
            return
        conversa.setdefault("estado", {})[chave] = valor
        self._guardar(conversa)

    def obter_estado(self, id_conversa: str, chave: str, padrao: object = None) -> object:
        conversa = self.carregar(id_conversa)
        if conversa is None:
            return padrao
        return conversa.get("estado", {}).get(chave, padrao)

    def remover(self, id_conversa: str) -> bool:
        caminho = self._caminho(id_conversa)
        if not caminho.exists():
            return False
        caminho.unlink()
        return True

    def listar(self) -> list[dict]:
        """Resumos (id, título, criado_em), mais recente primeiro."""
        resumos = []
        for caminho in self.pasta.glob("*.json"):
            conversa = json.loads(caminho.read_text(encoding="utf-8"))
            resumos.append(
                {"id": conversa["id"], "titulo": conversa["titulo"], "criado_em": conversa["criado_em"]}
            )
        resumos.sort(key=lambda c: c["criado_em"], reverse=True)
        return resumos
