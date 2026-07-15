# -*- coding: utf-8 -*-
"""Base canônica pesquisável do Chat Vivo."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from nucleo.chat_tipos import RegistroCanonico
from nucleo.chat_texto import normalizar, tokens_de

ROOT = Path(__file__).resolve().parents[1]
CAMINHO_BASE_CANONICA = ROOT / "dados" / "base_canonica.jsonl"

def _texto_registro(dados: dict[str, Any]) -> str:
    partes = [
        dados.get("id", ""),
        dados.get("titulo", ""),
        dados.get("pergunta_original", ""),
        " ".join(str(x) for x in dados.get("perguntas_equivalentes", [])),
        " ".join(str(x) for x in dados.get("palavras_chave", [])),
        dados.get("categoria", ""),
        dados.get("tipo", ""),
    ]
    return " ".join(str(p) for p in partes if p)


@lru_cache(maxsize=1)
def carregar_base_canonica() -> tuple[RegistroCanonico, ...]:
    if not CAMINHO_BASE_CANONICA.exists():
        return ()
    registros: list[RegistroCanonico] = []
    for linha in CAMINHO_BASE_CANONICA.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha:
            continue
        dados = json.loads(linha)
        registros.append(RegistroCanonico(dados=dados, tokens=tokens_de(_texto_registro(dados))))
    return tuple(registros)


def obter_registro(id_registro: str) -> RegistroCanonico | None:
    for registro in carregar_base_canonica():
        if registro.id == id_registro:
            return registro
    return None


def buscar_base_canonica(consulta: str) -> tuple[RegistroCanonico | None, int]:
    consulta_norm = normalizar(consulta)
    consulta_tokens = tokens_de(consulta)
    if not consulta_norm:
        return None, 0
    melhor: tuple[int, RegistroCanonico | None] = (0, None)
    for registro in carregar_base_canonica():
        dados = registro.dados
        frases = [dados.get("pergunta_original", ""), *dados.get("perguntas_equivalentes", [])]
        frases_norm = [normalizar(str(f)) for f in frases if str(f).strip()]
        score = 0
        if consulta_norm in frases_norm:
            score = 120
        elif any(len(f) >= 6 and (consulta_norm in f or f in consulta_norm) for f in frases_norm):
            score = 88
        inter = len(consulta_tokens & registro.tokens)
        if inter:
            uniao = len(consulta_tokens | registro.tokens) or 1
            score = max(score, inter * 14 + int((inter / uniao) * 60))
        if score > melhor[0]:
            melhor = (score, registro)
    limite = 18 if len(consulta_tokens) <= 2 else 24
    if melhor[0] >= limite:
        return melhor[1], min(99, melhor[0])
    return None, melhor[0]

