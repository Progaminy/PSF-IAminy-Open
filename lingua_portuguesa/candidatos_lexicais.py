"""Extração de candidatos a lema: tokens distintos do corpus amplo
(`corpus_interno.py::tokens_do_corpus_amplo`) que ainda não estão
indexados no léxico atual (`lexico.py::Dicionario.padrao()`), ordenados
por frequência real nesse mesmo corpus -- prioriza revisão pelas palavras
que o próprio projeto já usa mais, não uma ordem arbitrária ou alfabética
crua.

Fase 3 do plano de léxico (~650 mil palavras, zero fonte externa): este
módulo só GERA a lista de candidatos para revisão humana -- não incorpora
nada sozinho no léxico do motor. Incorporação real (Fase 4) exige atribuir
classe gramatical a cada candidato aprovado antes de virar lema em
`lexico_expansao.py`; um token cru sem classe não é "conhecer uma
palavra" no sentido que o projeto usa.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .corpus_interno import tokens_do_corpus_amplo
from .lexico import Dicionario

# Autorreferências do próprio projeto (nome/sigla), medidas no topo da
# lista de candidatos por aparecerem dezenas de vezes em README/RELATÓRIO/
# PLANO -- não são vocabulário comum do português (nome próprio de marca,
# não substantivo/adjetivo/verbo), por isso não viram candidato a lema
# aqui. Lista pequena e explícita (não heurística de maiúscula/hífen, que
# apagaria composto real como "guarda-chuva") -- só cresce se auditoria
# real achar outra autorreferência inflando a contagem sem ser palavra.
_AUTORREFERENCIAS_PROJETO = frozenset({"psf", "psf-iaminy"})


@dataclass(frozen=True, slots=True)
class CandidatoLexical:
    forma: str
    frequencia: int


def candidatos_lexicais(
    minimo_letras: int = 3, dicionario: Dicionario | None = None
) -> tuple[CandidatoLexical, ...]:
    """Tokens do corpus amplo que ainda não existem no léxico, ordenados
    por frequência decrescente (mais frequente primeiro) e, para desempate
    estável, ordem alfabética. Autorreferências do próprio projeto (nome/
    sigla, ver `_AUTORREFERENCIAS_PROJETO`) ficam de fora -- inflam a
    contagem sem ser vocabulário comum."""
    dicionario = dicionario or Dicionario.padrao()
    contagem = Counter(tokens_do_corpus_amplo(minimo_letras))
    candidatos = [
        CandidatoLexical(forma, frequencia)
        for forma, frequencia in contagem.items()
        if forma not in dicionario and forma not in _AUTORREFERENCIAS_PROJETO
    ]
    candidatos.sort(key=lambda candidato: (-candidato.frequencia, candidato.forma))
    return tuple(candidatos)
