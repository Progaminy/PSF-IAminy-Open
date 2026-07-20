"""Candidatos ortográficos observados somente no corpus do projeto.

Ocorrência repetida produz evidência para revisão, não entrada automática no
dicionário: exemplos negativos, nomes técnicos e lapsos também podem repetir.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache

from .corpus_interno import tokens_do_corpus, tokens_do_corpus_reconstrucao_local
from .normalizacao import normalizar_chave


_AUTORREFERENCIAS = frozenset({"psf", "psf-iaminy"})


@lru_cache(maxsize=1)
def formas_com_evidencia_canonica() -> tuple[str, ...]:
    """Candidatos repetidos no conhecimento canônico, sem símbolos ou código.

    Duas ocorrências independentes são o piso de evidência. Uma ocorrência
    isolada permanece candidata, pois pode ser exemplo negativo ou lapso do
    próprio texto e não deve entrar silenciosamente no corretor.
    """
    contagem = Counter(tokens_do_corpus())
    formas = {
        normalizar_chave(forma)
        for forma, total in contagem.items()
        if total >= 2
        and len(forma) >= 2
        and forma.replace("-", "").isalpha()
        and forma not in _AUTORREFERENCIAS
    }
    return tuple(sorted(formas))


@lru_cache(maxsize=1)
def formas_com_evidencia_ampla() -> tuple[str, ...]:
    """Candidatos repetidos na prosa autoral ampla, ainda não validados."""
    contagem = Counter(tokens_do_corpus_reconstrucao_local())
    formas = {
        normalizar_chave(forma)
        for forma, total in contagem.items()
        if total >= 2
        and len(forma) >= 2
        and forma.replace("-", "").isalpha()
        and forma not in _AUTORREFERENCIAS
    }
    return tuple(sorted(formas))
