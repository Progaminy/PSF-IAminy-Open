"""Continuidade de função racional num ponto — três condições conferidas de verdade.

Liga `limite de função racional` (ETAPA 1058) e `divisão de polinômios`
(ETAPA 1056): a resposta legada de `nucleo/conceitos_avancados_puros.py`
("uma função é contínua em x=a se está definida em a, tem limite em a, e
esse limite é igual ao valor da função em a") tinha as três condições em
prosa, sem checá-las contra nada. Aqui as três são calculadas de verdade
e comparadas — inclusive o caso do outro exemplo legado, `(x²-1)/(x-1)`
em `x=1`: o limite existe (2, por fatoração), mas a função não está
definida ali (denominador zero na expressão original), então não é
contínua. Ter limite não é o mesmo que ser contínua — a descontinuidade
é removível, não inexistente.
"""
from __future__ import annotations

from dataclasses import dataclass

from .divisao_polinomios import avaliar_polinomio
from .limite_racional_exato import limite_racional_em_ponto
from .reais_intervalos_naturais import RacionalAssinado

_ZERO = RacionalAssinado(0)


@dataclass(frozen=True, slots=True)
class AnaliseContinuidade:
    """As três condições da continuidade, cada uma calculada de verdade."""

    definida_no_ponto: bool
    valor_no_ponto: RacionalAssinado | None
    limite_no_ponto: RacionalAssinado | None
    continua: bool


def analisar_continuidade_racional(
    numerador: tuple[RacionalAssinado, ...],
    denominador: tuple[RacionalAssinado, ...],
    a: RacionalAssinado,
) -> AnaliseContinuidade:
    """f(x)=P(x)/Q(x) é contínua em a quando as três condições valem.

    ``definida_no_ponto``: Q(a) ≠ 0 na expressão original (não no
    quociente reduzido — dividir por zero não define valor, mesmo que o
    limite exista aproximando-se de a).
    ``limite_no_ponto``: o mesmo limite exato de `limite_racional_em_ponto`.
    ``continua``: as três condições comparadas, não assumidas.
    """
    valor_q = avaliar_polinomio(denominador, a)
    definida = valor_q != _ZERO
    valor_no_ponto = avaliar_polinomio(numerador, a).multiplicar(valor_q.reciproco()) if definida else None
    limite = limite_racional_em_ponto(numerador, denominador, a)
    continua = definida and limite is not None and limite == valor_no_ponto
    return AnaliseContinuidade(definida, valor_no_ponto, limite, continua)
