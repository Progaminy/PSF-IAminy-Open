"""Inequações lineares — isolar x preservando ordem, invertendo com coeficiente negativo.

"Inequações" existia neste projeto só como resposta legada
(`nucleo/conceitos_avancados_puros.py`): explicação e exemplo prontos, sem
prova, código ou teste. Este módulo liga a `ordem total` (ETAPA 69) e
`equação de primeiro grau` (ETAPA 133): resolver `a·x + b ⋈ c` é isolar x
do mesmo jeito que numa equação, exceto que multiplicar ou dividir por
uma quantidade negativa inverte o sentido da comparação.

A regra de inversão não é aceita "porque é conhecida": cada solução é
conferida testando um valor de cada lado do limite na inequação
original, e só o lado esperado deve satisfazê-la.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .reais_intervalos_naturais import RacionalAssinado

_UM = RacionalAssinado(1)


class Comparador(Enum):
    MAIOR = ">"
    MAIOR_OU_IGUAL = ">="
    MENOR = "<"
    MENOR_OU_IGUAL = "<="


_INVERSO = {
    Comparador.MAIOR: Comparador.MENOR,
    Comparador.MENOR: Comparador.MAIOR,
    Comparador.MAIOR_OU_IGUAL: Comparador.MENOR_OU_IGUAL,
    Comparador.MENOR_OU_IGUAL: Comparador.MAIOR_OU_IGUAL,
}


def _satisfaz(comparador: Comparador, esquerda: RacionalAssinado, direita: RacionalAssinado) -> bool:
    iguais = esquerda.menor_ou_igual(direita) and direita.menor_ou_igual(esquerda)
    if comparador is Comparador.MAIOR:
        return direita.menor_ou_igual(esquerda) and not iguais
    if comparador is Comparador.MENOR:
        return esquerda.menor_ou_igual(direita) and not iguais
    if comparador is Comparador.MAIOR_OU_IGUAL:
        return direita.menor_ou_igual(esquerda)
    return esquerda.menor_ou_igual(direita)


@dataclass(frozen=True, slots=True)
class SolucaoInequacao:
    comparador: Comparador
    limite: RacionalAssinado

    def satisfaz(self, x: RacionalAssinado) -> bool:
        return _satisfaz(self.comparador, x, self.limite)

    def texto(self) -> str:
        return f"x {self.comparador.value} {self.limite.numerador}/{self.limite.denominador}"


def resolver_inequacao_linear(
    a: RacionalAssinado, b: RacionalAssinado, comparador: Comparador, c: RacionalAssinado
) -> SolucaoInequacao:
    """Resolve a·x + b ⋈ c para x.

    Isola x subtraindo `b` e dividindo por `a`; inverte o comparador
    quando `a` é negativo. Conferida testando `limite+1` e `limite-1` na
    inequação original: só o lado que a solução aponta deve satisfazê-la.
    """
    if a.numerador == 0:
        raise ValueError("coeficiente de x não pode ser zero nesta etapa")
    lado_direito = c.subtrair(b)
    limite = lado_direito.multiplicar(a.reciproco())
    inverte = a.numerador < 0
    comparador_final = _INVERSO[comparador] if inverte else comparador
    solucao = SolucaoInequacao(comparador_final, limite)

    acima = limite.somar(_UM)
    abaixo = limite.subtrair(_UM)
    lado_de_acima_satisfaz_original = _satisfaz(comparador, a.multiplicar(acima).somar(b), c)
    lado_de_abaixo_satisfaz_original = _satisfaz(comparador, a.multiplicar(abaixo).somar(b), c)
    if solucao.satisfaz(acima) != lado_de_acima_satisfaz_original:
        raise ValueError("solução divergiu ao testar um valor acima do limite")
    if solucao.satisfaz(abaixo) != lado_de_abaixo_satisfaz_original:
        raise ValueError("solução divergiu ao testar um valor abaixo do limite")
    return solucao
