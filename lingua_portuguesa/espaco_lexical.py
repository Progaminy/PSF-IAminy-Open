"""Ponte entre o alfabeto real do português e o espaço combinatório
genérico de `nucleo/espaco_combinatorio_palavras.py`.

Dá resposta direta ao pedido do autor: em vez de gerar palavra por
combinação aleatória infinita (sem parar, sem saber quais combinações já
foram vistas), toda sequência de letras tem uma POSIÇÃO exata e computável
dentro do total de sequências do mesmo comprimento -- dado um comprimento
`r`, existem exatamente 26^r sequências possíveis (Etapa 39, arranjo com
repetição), numeradas de 0 a 26^r - 1. Isso permite:

1. Dado um comprimento, saber quantas sequências existem antes de gerar
   qualquer uma (`total_palavras_possiveis`).
2. Dada uma palavra, saber exatamente que posição ela ocupa nesse total
   (`posicao_da_palavra`) -- localizar uma palavra conhecida no espaço,
   em vez de adivinhar por tentativa aleatória.
3. Dada uma posição, reconstruir a sequência de letras correspondente
   (`palavra_da_posicao`) -- permite percorrer o espaço de forma
   sistemática e retomável (a partir de uma posição dada), nunca "gerar
   para sempre sem controlo".

Decisão de design explícita (a confirmar com o autor, não escondida):
o alfabeto de base usado para a posição é só a-z (26 símbolos), sem
letras acentuadas -- uma letra acentuada é tratada como marca sobre uma
letra-base, não como símbolo adicional na contagem posicional. Isto
mantém o espaço combinatório pequeno e bem definido; acentuação como
dimensão própria (multiplicar por variantes de acento por posição) fica
como extensão futura separada, não confundida com esta camada.
"""
from __future__ import annotations

from nucleo.espaco_combinatorio_palavras import (
    posicao_da_sequencia,
    sequencia_da_posicao,
    total_sequencias,
)

ALFABETO_PT = "abcdefghijklmnopqrstuvwxyz"
TAMANHO_ALFABETO = len(ALFABETO_PT)


def _indice_letra(letra: str) -> int:
    indice = ALFABETO_PT.find(letra)
    if indice < 0:
        raise ValueError(
            f'letra "{letra}" fora do alfabeto-base a-z (acentos e outros símbolos não contam nesta camada)'
        )
    return indice


def total_palavras_possiveis(comprimento: int) -> int:
    """Quantas sequências de `comprimento` letras (a-z) existem no total --
    arranjo com repetição, Etapa 39 (`nucleo/combinatoria_natural.py::
    ESCOLHAS_ORDENADAS_COM_REPETICAO_PURO`)."""
    return total_sequencias(TAMANHO_ALFABETO, comprimento)


def posicao_da_palavra(palavra: str) -> int:
    """Posição (0-based) de `palavra` dentro da ordem lexicográfica de
    todas as sequências do mesmo comprimento sobre a-z."""
    if not palavra:
        raise ValueError("palavra vazia não tem posição definida")
    indices = tuple(_indice_letra(letra) for letra in palavra.casefold())
    return posicao_da_sequencia(indices, TAMANHO_ALFABETO)


def palavra_da_posicao(posicao: int, comprimento: int) -> str:
    """Caminho inverso: a sequência de letras a-z que ocupa `posicao` entre
    as `total_palavras_possiveis(comprimento)` sequências desse comprimento."""
    indices = sequencia_da_posicao(posicao, TAMANHO_ALFABETO, comprimento)
    return "".join(ALFABETO_PT[indice] for indice in indices)
