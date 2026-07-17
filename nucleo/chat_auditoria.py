# -*- coding: utf-8 -*-
"""Auditoria JSONL do Chat Vivo."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from psf_iaminy.recursos import caminho_dado_mutavel
from typing import Any

from nucleo.chat_tipos import RespostaChat

CAMINHO_AUDITORIA = caminho_dado_mutavel("dados", "auditoria_chat_vivo.jsonl")
CAMINHO_FALHAS = caminho_dado_mutavel("dados", "falhas_chat_vivo.jsonl")

def _registrar_jsonl(caminho: Path, dados: dict[str, Any]) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("a", encoding="utf-8") as f:
        f.write(json.dumps(dados, ensure_ascii=False, sort_keys=True) + "\n")


def _auditar(mensagem: str, resposta: RespostaChat, duracao_ms: int) -> None:
    registro = {
        "quando": datetime.now(timezone.utc).isoformat(),
        "mensagem_do_usuario": mensagem,
        "tipo_detectado": resposta.intencao,
        "tom_detectado": resposta.tom,
        "conhecimento_encontrado": resposta.conhecimento_encontrado,
        "origem": resposta.origem,
        "confianca": resposta.confianca,
        "lacunas": resposta.lacunas,
        "fallback_usado": resposta.fallback_usado,
        "deve_melhorar": resposta.deve_melhorar,
        "duracao_ms": duracao_ms,
    }
    _registrar_jsonl(CAMINHO_AUDITORIA, registro)
    if resposta.fallback_usado or resposta.deve_melhorar:
        _registrar_jsonl(CAMINHO_FALHAS, registro)

