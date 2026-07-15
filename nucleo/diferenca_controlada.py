# ==============================================================================
# DIFERENÇA CONTROLADA — construída SEM divisão, SEM resto, SEM módulo.
# ==============================================================================
# Lei PSF-IAminy:
#   Subtrair em N só é operação total quando aceitamos truncamento.
#   A diferença matemática a-b, como número natural, só está definida se a >= b.
#
# Esta camada torna explícito o que antes poderia ficar escondido:
#   - SUB(a)(b) já existe como subtração truncada de Peano;
#   - DIFERENCA_CONTROLADA(a,b) só é considerada definida se a >= b;
#   - quando não está definida, ZERO é apenas sentinela operacional.
# ==============================================================================
from .primitivas import V, F, ZERO
from .logica import E, IMPLICA, SSE
from .aritmetica import SUB, SOMA, IGUAL, MAIOR, MAIOR_OU_IGUAL
from .divisibilidade_pura import DIVIDE_PURO
from .mdc_puro import DIVISOR_COMUM_PURO


# a-b está definido em N quando a >= b.
DIFERENCA_DEFINIDA = lambda a: lambda b: MAIOR_OU_IGUAL(a)(b)


# Diferença controlada: devolve a-b se definido; senão devolve ZERO como sentinela.
DIFERENCA_CONTROLADA = lambda a: lambda b: DIFERENCA_DEFINIDA(a)(b)(
    lambda _: SUB(a)(b)
)(
    lambda _: ZERO
)(V)


# Diferença positiva: exige a > b.
DIFERENCA_POSITIVA_DEFINIDA = lambda a: lambda b: MAIOR(a)(b)
DIFERENCA_POSITIVA = lambda a: lambda b: DIFERENCA_POSITIVA_DEFINIDA(a)(b)(
    lambda _: SUB(a)(b)
)(
    lambda _: ZERO
)(V)


# Reconstituição: se a>=b, então (a-b)+b = a.
# Isto valida que a diferença controlada não inventa valor.
RECONSTITUI_DIFERENCA = lambda a: lambda b: IMPLICA(
    DIFERENCA_DEFINIDA(a)(b)
)(
    IGUAL(SOMA(DIFERENCA_CONTROLADA(a)(b))(b))(a)
)


# Se d divide a e d divide b, e a>=b, então d divide a-b.
# Este é o passo conceitual que permitirá Euclides por subtração.
DIVISOR_COMUM_PRESERVA_DIFERENCA = lambda d: lambda a: lambda b: IMPLICA(
    E(DIVISOR_COMUM_PURO(d)(a)(b))(DIFERENCA_DEFINIDA(a)(b))
)(
    DIVIDE_PURO(d)(DIFERENCA_CONTROLADA(a)(b))
)


# Se d divide b e d divide a-b, então d divide a, porque a=(a-b)+b.
DIVISOR_COMUM_RECOMPOE_ORIGINAL = lambda d: lambda a: lambda b: IMPLICA(
    E(E(DIVIDE_PURO(d)(b))(DIVIDE_PURO(d)(DIFERENCA_CONTROLADA(a)(b))))(DIFERENCA_DEFINIDA(a)(b))
)(
    DIVIDE_PURO(d)(a)
)


# Para a>=b: d comum(a,b) equivale a d comum(a-b,b).
# Esta equivalência é a raiz do algoritmo de Euclides por subtração.
DIVISOR_COMUM_EQUIVALENTE_APOS_SUBTRACAO = lambda d: lambda a: lambda b: IMPLICA(
    DIFERENCA_DEFINIDA(a)(b)
)(
    SSE(DIVISOR_COMUM_PURO(d)(a)(b))(DIVISOR_COMUM_PURO(d)(DIFERENCA_CONTROLADA(a)(b))(b))
)
