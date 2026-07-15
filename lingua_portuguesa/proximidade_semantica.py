"""Proximidade semântica por coocorrência contada -- Fase 6.1 do plano de
corretor, substituto honesto da técnica 7 (Word2Vec).

**Isto não é Word2Vec.** Não há treino, não há função objetivo otimizada
por gradiente, não há vetor denso aprendido. É distribuição de
coocorrência CONTADA (vetor esparso clássico, pré-neural -- a mesma
família de ideia por trás de PMI/matrizes de coocorrência) sobre o corpus
interno (Fase 4.3): cada palavra vira um vetor de quantas vezes cada
palavra vizinha aparece ao seu lado dentro de uma janela fixa, e
similaridade é cosseno em Python puro. É deliberadamente mais fraco,
menor e mais explicável que um embedding treinado -- a intenção desta nota
é nunca deixar confundir isto depois com a capacidade que a regra do
projeto proíbe importar pronta.

Quando ambas as palavras em questão são também conceitos PSF modelados
(`ConceitoPortugues`), o caminho real no grafo de dependências
(`ensino/navegacao_pacotes.py`, já existente) é um sinal de proximidade
mais forte e mais barato do que isto -- ver `corretor.py`, que consulta os
dois, nessa ordem.
"""
from __future__ import annotations

import math
from collections import Counter, defaultdict
from functools import lru_cache

from .corpus_interno import tokens_do_corpus

JANELA_PADRAO = 2


def vetores_coocorrencia(tokens: tuple[str, ...], janela: int = JANELA_PADRAO) -> dict[str, Counter]:
    """Um vetor esparso por palavra: contagem de cada vizinho encontrado
    dentro de `janela` posições para os dois lados, ao longo de `tokens`."""
    vetores: dict[str, Counter] = defaultdict(Counter)
    for indice, palavra in enumerate(tokens):
        inicio = max(0, indice - janela)
        fim = min(len(tokens), indice + janela + 1)
        for vizinho_indice in range(inicio, fim):
            if vizinho_indice == indice:
                continue
            vetores[palavra][tokens[vizinho_indice]] += 1
    return vetores


@lru_cache(maxsize=1)
def _vetores_padrao() -> dict[str, Counter]:
    return vetores_coocorrencia(tokens_do_corpus())


def vetor_de(palavra: str, vetores: dict[str, Counter] | None = None) -> Counter:
    """Vetor esparso de coocorrência de `palavra` -- vazio se a palavra
    não aparece na fonte usada."""
    fonte = vetores if vetores is not None else _vetores_padrao()
    return fonte.get(palavra, Counter())


def similaridade_cosseno(a: Counter, b: Counter) -> float:
    """Cosseno entre dois vetores esparsos (contagem palavra->vizinho),
    em aritmética Python pura -- `0.0` se qualquer um dos dois for vazio
    ou não tiver nenhuma dimensão em comum."""
    if not a or not b:
        return 0.0
    chaves_comuns = set(a) & set(b)
    produto_escalar = sum(a[chave] * b[chave] for chave in chaves_comuns)
    if produto_escalar == 0:
        return 0.0
    norma_a = math.sqrt(sum(valor * valor for valor in a.values()))
    norma_b = math.sqrt(sum(valor * valor for valor in b.values()))
    return produto_escalar / (norma_a * norma_b)


def proximidade(palavra_a: str, palavra_b: str, vetores: dict[str, Counter] | None = None) -> float:
    """Similaridade de coocorrência entre duas palavras (0.0 a 1.0),
    sobre a fonte de vetores dada (por omissão, o corpus interno)."""
    fonte = vetores if vetores is not None else _vetores_padrao()
    return similaridade_cosseno(vetor_de(palavra_a, fonte), vetor_de(palavra_b, fonte))
