"""Paridade — par e ímpar, pelo resto da divisão por dois.

"Pares e ímpares" existia neste projeto só como caso implícito dentro de
`divisibilidade pura` (ETAPA 3: "n é par" é exatamente `2 | n`), nunca
nomeado à parte nem testado como propriedade própria. Este módulo liga a
`dividir_com_resto` (Etapa 31, aritmética escolar nativa): resto 0 é par,
resto 1 é ímpar — nenhuma outra construção é necessária, porque o resto
de dividir por dois só pode ser 0 ou 1.
"""
from __future__ import annotations

from .aritmetica_escolar_nativa import dividir_com_resto, somar


def eh_par(n: int) -> bool:
    _, resto = dividir_com_resto(n, 2)
    return resto == 0


def eh_impar(n: int) -> bool:
    return not eh_par(n)


def paridade(n: int) -> str:
    """"par" ou "ímpar", nomeando o resultado."""
    return "par" if eh_par(n) else "ímpar"


def paridade_da_soma(a: int, b: int) -> str:
    """Paridade de a+b, decidida pela regra clássica e conferida contra a soma direta.

    par+par=par, ímpar+ímpar=par, par+ímpar=ímpar (e vice-versa) — a
    regra não é aceita por decoreba: soma `a` e `b` de verdade (Etapa 31)
    e confere que a paridade do resultado bate com o que a regra previu.
    """
    if eh_par(a) and eh_par(b):
        esperado = "par"
    elif eh_impar(a) and eh_impar(b):
        esperado = "par"
    else:
        esperado = "ímpar"
    paridade_real = paridade(somar(a, b))
    if esperado != paridade_real:
        raise ValueError("regra de paridade da soma divergiu do cálculo direto")
    return paridade_real
