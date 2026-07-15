"""Adjacência física de teclas no teclado (layout ABNT2/QWERTY de PC).

Dado factual sobre um objeto físico (o teclado), não capacidade emprestada
— mesma categoria de "dado, não atalho" que uma lista de lemas. Serve para
saber se um erro de digitação plausível é "tecla vizinha" (ex.: "vabos" em
vez de "vamos", 'b' e 'm' não são vizinhas, mas 'b'/'v' são) — sinal real
para o canal ruidoso (Fase 5) e para gerar candidatos de correção.

Escopo desta primeira versão: só letras base sem acento. Sequências de
tecla morta acentuada (~, ´, `, ^) ficam como extensão documentada e
futura, não escondida.
"""
from __future__ import annotations

import json
from functools import lru_cache
from importlib.resources import files


@lru_cache(maxsize=1)
def _tabela() -> dict[str, frozenset[str]]:
    caminho = files("lingua_portuguesa.dados").joinpath("teclado_pt.json")
    with caminho.open("r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return {
        letra: frozenset(vizinhas)
        for letra, vizinhas in dados["adjacencias"].items()
    }


def teclas_adjacentes(caractere: str) -> frozenset[str]:
    """Teclas fisicamente vizinhas de `caractere` no teclado (vazio se desconhecida)."""
    return _tabela().get(caractere.lower(), frozenset())


def sao_adjacentes(a: str, b: str) -> bool:
    """True se `a` e `b` forem teclas fisicamente vizinhas (ordem não importa)."""
    return b.lower() in teclas_adjacentes(a)
