"""Limite de função racional em ponto finito — fatoração por Briot-Ruffini.

Liga `divisão de polinômios e Teorema do Resto` (ETAPA 1056): a
indeterminação clássica `0/0` de um limite de função racional
`P(x)/Q(x)` quando `x→a` não é "levantada" por regra mágica — quando
`a` é raiz de `P` e de `Q`, os dois se dividem exatamente por `(x−a)`
(Briot-Ruffini), e o limite é reavaliado no quociente reduzido. Se o
grau do quociente ainda tiver `a` como raiz de `Q`, repete; termina
porque cada divisão reduz o grau do denominador em um.

Isto cobre só limite em ponto finito de função racional — não é a
teoria geral de limites (que exigiria reais completos para sequências
arbitrárias) nem limites que envolvem funções não-racionais (seno,
exponencial). Limite no infinito e limites trigonométricos/exponenciais
continuam como próximo alvo.
"""
from __future__ import annotations

from .divisao_polinomios import avaliar_polinomio, dividir_por_x_menos_a
from .reais_intervalos_naturais import RacionalAssinado

_ZERO = RacionalAssinado(0)


def _eh_polinomio_nulo(coeficientes: tuple[RacionalAssinado, ...]) -> bool:
    return all(c == _ZERO for c in coeficientes)


def limite_racional_em_ponto(
    numerador: tuple[RacionalAssinado, ...],
    denominador: tuple[RacionalAssinado, ...],
    a: RacionalAssinado,
) -> RacionalAssinado | None:
    """lim(x→a) P(x)/Q(x), exato, por avaliação direta ou fatoração de (x−a).

    Devolve ``None`` quando o limite não é finito: `Q(a)=0` mas `P(a)≠0`
    é uma divergência genuína (a função cresce sem limite perto de `a`),
    não um caso a fingir com um valor de infinito.
    """
    if not numerador or not denominador:
        raise ValueError("numerador e denominador precisam de ao menos um coeficiente")
    if _eh_polinomio_nulo(denominador):
        raise ValueError("denominador não pode ser o polinômio nulo")

    p, q = numerador, denominador
    while True:
        valor_q = avaliar_polinomio(q, a)
        if valor_q != _ZERO:
            valor_p = avaliar_polinomio(p, a)
            return valor_p.multiplicar(valor_q.reciproco())
        valor_p = avaliar_polinomio(p, a)
        if valor_p != _ZERO:
            return None
        p, _ = dividir_por_x_menos_a(p, a)
        q, _ = dividir_por_x_menos_a(q, a)


def eh_indeterminacao_zero_sobre_zero(
    numerador: tuple[RacionalAssinado, ...], denominador: tuple[RacionalAssinado, ...], a: RacionalAssinado
) -> bool:
    """P(a)=0 e Q(a)=0 ao mesmo tempo — a condição que exige fatoração."""
    return avaliar_polinomio(numerador, a) == _ZERO and avaliar_polinomio(denominador, a) == _ZERO
