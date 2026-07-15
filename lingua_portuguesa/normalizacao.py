"""Normalização conservadora de texto português."""
from __future__ import annotations

import re
import unicodedata

_ESPACOS = re.compile(r"\s+")


def normalizar_texto(texto: str) -> str:
    """Aplica Unicode NFC e uniformiza espaços sem remover acentos."""
    if not isinstance(texto, str):
        raise TypeError("texto deve ser uma string")
    return _ESPACOS.sub(" ", unicodedata.normalize("NFC", texto)).strip()


def normalizar_chave(texto: str) -> str:
    """Produz uma chave lexical sem alterar a ortografia portuguesa."""
    return unicodedata.normalize("NFC", texto).casefold()


def sem_acentos(texto: str) -> str:
    """Remove marcas diacríticas; útil apenas para busca aproximada."""
    decomposto = unicodedata.normalize("NFD", normalizar_chave(texto))
    return "".join(c for c in decomposto if unicodedata.category(c) != "Mn")

