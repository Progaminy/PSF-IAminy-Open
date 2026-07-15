"""Divisão de polinômios por (x−a) e Teorema do Resto — Briot-Ruffini.

Liga `polinômios anel` e `grau operações polinomiais` (ETAPA 101-102):
dividir um polinômio por `(x−a)` é o algoritmo de Briot-Ruffini, e o
resto dessa divisão é exatamente `P(a)` — o Teorema do Resto não é aceito
como fato citado: os dois caminhos (dividir e avaliar) são calculados de
forma independente e conferidos um contra o outro.

Polinômios são representados como tuplas de coeficientes do maior grau
para o menor, `(c_n, c_{n-1}, ..., c_1, c_0)` para
`c_n·xⁿ + c_{n-1}·xⁿ⁻¹ + ... + c_0` — mesma convenção usada para ler um
número em `digitos()` (ETAPA 1037), do dígito mais significativo primeiro.
"""
from __future__ import annotations

from .reais_intervalos_naturais import RacionalAssinado

_ZERO = RacionalAssinado(0)


def avaliar_polinomio(coeficientes: tuple[RacionalAssinado, ...], x: RacionalAssinado) -> RacionalAssinado:
    """P(x) pelo método de Horner: ((...(c_n·x + c_{n-1})·x + ...) + c_0."""
    if not coeficientes:
        raise ValueError("polinômio precisa de ao menos um coeficiente")
    resultado = _ZERO
    for c in coeficientes:
        resultado = resultado.multiplicar(x).somar(c)
    return resultado


def dividir_por_x_menos_a(
    coeficientes: tuple[RacionalAssinado, ...], a: RacionalAssinado
) -> tuple[tuple[RacionalAssinado, ...], RacionalAssinado]:
    """Divide P(x) por (x−a) por Briot-Ruffini: devolve (quociente, resto).

    O resto é conferido contra o Teorema do Resto (`P(a)`, calculado por
    avaliação direta via Horner) — dois algoritmos independentes que têm
    que concordar, não um aceito por confiança no outro.
    """
    if not coeficientes:
        raise ValueError("polinômio precisa de ao menos um coeficiente")
    parciais = [coeficientes[0]]
    for c in coeficientes[1:]:
        parciais.append(c.somar(a.multiplicar(parciais[-1])))
    quociente = tuple(parciais[:-1])
    resto = parciais[-1]
    valor_direto = avaliar_polinomio(coeficientes, a)
    if resto != valor_direto:
        raise ValueError("resto da divisão diverge do Teorema do Resto (P(a))")
    return quociente, resto


def teorema_do_resto(coeficientes: tuple[RacionalAssinado, ...], a: RacionalAssinado) -> RacionalAssinado:
    """O resto de dividir P(x) por (x−a) é exatamente P(a)."""
    _, resto = dividir_por_x_menos_a(coeficientes, a)
    return resto


def eh_raiz(coeficientes: tuple[RacionalAssinado, ...], a: RacionalAssinado) -> bool:
    """a é raiz de P quando o resto de dividir por (x−a) é zero."""
    return teorema_do_resto(coeficientes, a) == _ZERO
