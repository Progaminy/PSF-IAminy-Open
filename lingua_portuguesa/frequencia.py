"""Sinal de frequência de uso -- Fase 4.2 do plano de corretor (técnica 5:
"prefere palavra comum entre empatadas").

A fonte real de frequência ampla (corpus geral de português) continua uma
decisão de dado em aberto, mesmo status da lista de lemas da Fase 3, não
resolvida aqui. O que existe agora é honesto e mais limitado: contagem
real sobre o corpus interno (Fase 4.3, `corpus_interno.py`), pequeno e
enviesado para vocabulário técnico/didático. `frequencia_de` devolve
`None` (nunca `0.0` nem um valor inventado) quando a palavra não aparece
nem nesse corpus limitado -- `None` é o sinal honesto de "sem dado",
distinguível de "frequência real zero".
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache

from .corpus_interno import tokens_do_corpus
from .normalizacao import normalizar_chave


@lru_cache(maxsize=1)
def _contagens() -> tuple[Counter, int]:
    contagem = Counter(tokens_do_corpus())
    total = sum(contagem.values())
    return contagem, total


def frequencia_de(forma: str) -> float | None:
    """Frequência relativa de `forma` no corpus interno, ou `None` se a
    palavra não aparecer nele -- nunca um valor fabricado."""
    contagem, total = _contagens()
    if total == 0:
        return None
    vezes = contagem.get(normalizar_chave(forma), 0)
    if vezes == 0:
        return None
    return vezes / total


def ordenar_por_frequencia(candidatos: tuple[str, ...]) -> tuple[str, ...]:
    """Ordena candidatos da mais para a menos frequente no corpus interno.
    Candidatos sem dado de frequência (`None`) ficam por último, mantendo
    a ordem original entre si -- nunca tratados como empatados com
    frequência real zero."""

    def chave(item: tuple[int, str]) -> tuple[int, float]:
        indice, candidato = item
        freq = frequencia_de(candidato)
        return (0, -freq) if freq is not None else (1, float(indice))

    com_indice = sorted(enumerate(candidatos), key=chave)
    return tuple(candidato for _, candidato in com_indice)
