"""Regra de três simples — proporção direta e inversa, por multiplicação cruzada exata.

"Regra de três simples" já era, sem esse nome, `sao_grandezas_proporcionais`
(ETAPA 1036): `a1/b1 = a2/x` é exatamente a mesma multiplicação cruzada
`a1·x = a2·b1`. Este módulo dá a forma de apresentação pedagógica —
resolver para o valor que falta — e acrescenta o caso inverso (quando
aumentar uma grandeza diminui a outra na mesma razão).
"""
from __future__ import annotations

from .reais_intervalos_naturais import RacionalAssinado


def regra_de_tres_direta(
    a1: RacionalAssinado, b1: RacionalAssinado, a2: RacionalAssinado
) -> RacionalAssinado:
    """a1 está para b1 assim como a2 está para x — proporção direta: a1/b1 = a2/x.

    x = a2·b1/a1, conferido por multiplicação cruzada: `a1·x` deve ser
    igual a `a2·b1` — a mesma prova de proporção já usada em ETAPA 1036.
    """
    if a1.numerador == 0:
        raise ValueError("primeiro termo não pode ser zero")
    x = a2.multiplicar(b1).multiplicar(a1.reciproco())
    if a1.multiplicar(x) != a2.multiplicar(b1):
        raise ValueError("solução não confere pela multiplicação cruzada")
    return x


def regra_de_tres_inversa(
    a1: RacionalAssinado, b1: RacionalAssinado, a2: RacionalAssinado
) -> RacionalAssinado:
    """Proporção inversa: a1·b1 = a2·x (aumentar a1 para a2 diminui b1 na mesma razão).

    x = a1·b1/a2, conferido reconstruindo o produto constante.
    """
    if a2.numerador == 0:
        raise ValueError("segundo termo (novo) não pode ser zero")
    x = a1.multiplicar(b1).multiplicar(a2.reciproco())
    if a2.multiplicar(x) != a1.multiplicar(b1):
        raise ValueError("solução não confere pelo produto constante")
    return x
