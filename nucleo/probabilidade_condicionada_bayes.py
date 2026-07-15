"""Teorema de Bayes — conferido contra a probabilidade condicional direta.

"Probabilidade condicionada (Bayes)" existia neste projeto só como
resposta legada (`nucleo/conceitos_avancados_puros.py`), sem prova,
código ou teste. Este módulo não recomeça do zero: liga direto a
`nucleo/medida_probabilidade_finita.py` (ETAPA 921-960), que já constrói
`probabilidade_como_par` e `condicional_como_par` a partir de conjuntos e
pesos — a definição direta de probabilidade condicional.

Bayes não é aceito como fórmula pronta: `P(A|B)` é calculada pela fórmula
`P(B|A)·P(A) / P(B)` e conferida, por produto cruzado exato, contra
`condicional_como_par(a, b, ...)` — a mesma probabilidade condicional
calculada diretamente dos conjuntos, sem passar pela fórmula. Se
divergirem, é erro de construção, não um resultado aceito por confiança.
"""
from __future__ import annotations

from .medida_probabilidade_finita import condicional_como_par, probabilidade_como_par


def bayes_como_par(a, b, universo, pesos=None) -> tuple[int, int]:
    """P(A|B) pela fórmula de Bayes, conferida contra a probabilidade condicional direta.

    Devolve `(numerador, denominador)`, no mesmo formato de
    `condicional_como_par`. Levanta erro se P(B) ou P(A) forem nulos
    (Bayes não está definido condicionando em evento impossível) ou se a
    fórmula divergir da definição direta.
    """
    if pesos is None:
        pesos = {x: 1 for x in universo}
    p_b_dado_a_num, p_b_dado_a_den = condicional_como_par(b, a, universo, pesos)
    p_a_num, p_a_den = probabilidade_como_par(a, universo, pesos)
    p_b_num, p_b_den = probabilidade_como_par(b, universo, pesos)

    if p_b_num == 0:
        raise ValueError("P(B) não pode ser zero para aplicar Bayes")
    if p_b_dado_a_den == 0:
        raise ValueError("P(A) não pode ser zero (condicional em evento impossível)")

    numerador = p_b_dado_a_num * p_a_num * p_b_den
    denominador = p_b_dado_a_den * p_a_den * p_b_num

    direta_num, direta_den = condicional_como_par(a, b, universo, pesos)
    if numerador * direta_den != denominador * direta_num:
        raise ValueError("fórmula de Bayes divergiu da probabilidade condicional direta")
    return (numerador, denominador)
