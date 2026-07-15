# ==============================================================================
# MDC PURO — construído SEM divisão, SEM resto, SEM módulo, SEM Euclides.
# ==============================================================================
# Definição:
#   g = mdc(a,b)  <=>
#   g|a, g|b, e todo divisor comum d de a,b satisfaz d <= g.
#
# Implementação conceitual: busca finita dos divisores comuns e mantém o maior.
# Eficiência não é o objetivo desta camada; pureza conceitual é.
# ==============================================================================
from .primitivas import V, F, ZERO
from .logica import E, NAO
from .aritmetica import IS_ZERO, IGUAL, MIN, _UM
from .combinadores import INTERVALO
from .divisibilidade_pura import DIVIDE_PURO


DIVISOR_COMUM_PURO = lambda d: lambda a: lambda b: E(DIVIDE_PURO(d)(a))(DIVIDE_PURO(d)(b))


# MDC(0,0) não é definido: todos os naturais positivos dividem 0, então não há maior.
MDC_DEFINIDO_PURO = lambda a: lambda b: NAO(E(IS_ZERO(a))(IS_ZERO(b)))


# Para (0,0), esta função devolve ZERO apenas como sentinela operacional.
# A validade deve ser consultada por MDC_DEFINIDO_PURO(a)(b).
MDC_PURO = lambda a: lambda b: IS_ZERO(a)(
    lambda _: b
)(
    lambda _: IS_ZERO(b)(
        lambda _: a
    )(
        lambda _: INTERVALO(_UM)(MIN(a)(b))(
            lambda d: lambda acc: DIVISOR_COMUM_PURO(d)(a)(b)(
                lambda _: d
            )(
                lambda _: acc
            )(F)
        )(_UM)
    )(V)
)(V)


COPRIMOS_PURO = lambda a: lambda b: E(MDC_DEFINIDO_PURO(a)(b))(IGUAL(MDC_PURO(a)(b))(_UM))
