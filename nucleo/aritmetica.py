# ==============================================================================
# ARITMÉTICA DE PEANO — Derivada exclusivamente de 0, S, PAR, ITER, Y
# ==============================================================================
# Nota sobre os numerais: no material original (DeepSeek) aparecia
# "1 = S(0)", "2 = S(1)", ... — sintaxe inválida em Python (não se pode
# atribuir a um literal). Em vez de nomear numerais individualmente,
# qualquer numeral é construído a partir de um inteiro Python apenas na
# camada periférica (ver `traducao.de_int`). O núcleo abaixo é
# independente de literais numéricos do Python.

from .primitivas import V, F, ZERO, S, PAR, ITER, Y
from .logica import E, NAO

# --------------------------------------------------------------------------
# ADIÇÃO — m + n = ITER(n)(m)(S)   (aplica sucessor n vezes a partir de m)
# --------------------------------------------------------------------------
SOMA = lambda m: lambda n: ITER(n)(m)(S)

# --------------------------------------------------------------------------
# PREDECESSOR — via "deslizamento" de pares (a, b) -> (b, S(b))
# Estado inicial (0, 0); após n iterações o primeiro elemento é n-1.
# --------------------------------------------------------------------------
PRED = lambda n: ITER(n)(PAR(ZERO)(ZERO))(
    lambda p: PAR(p(F))(S(p(F)))
)(V)

# --------------------------------------------------------------------------
# SUBTRAÇÃO TRUNCADA — m ∸ n = ITER(n)(m)(PRED); se n > m, resultado é 0.
# --------------------------------------------------------------------------
SUB = lambda m: lambda n: ITER(n)(m)(PRED)

# --------------------------------------------------------------------------
# COMPARADORES — derivados de SUB
# --------------------------------------------------------------------------
IS_ZERO = lambda n: n(lambda _: F)(V)                      # aplica (_->F) n vezes a V
MENOR_OU_IGUAL = lambda m: lambda n: IS_ZERO(SUB(m)(n))
IGUAL = lambda m: lambda n: E(MENOR_OU_IGUAL(m)(n))(MENOR_OU_IGUAL(n)(m))
MENOR = lambda m: lambda n: E(MENOR_OU_IGUAL(m)(n))(NAO(IGUAL(m)(n)))
MAIOR = lambda m: lambda n: MENOR(n)(m)
MAIOR_OU_IGUAL = lambda m: lambda n: MENOR_OU_IGUAL(n)(m)

# --------------------------------------------------------------------------
# VALOR ABSOLUTO DA DIFERENÇA, MÍNIMO, MÁXIMO
# --------------------------------------------------------------------------
ABS_DIFF = lambda m: lambda n: SOMA(SUB(m)(n))(SUB(n)(m))
MIN = lambda m: lambda n: MENOR_OU_IGUAL(m)(n)(lambda _: m)(lambda _: n)(V)
MAX = lambda m: lambda n: MAIOR_OU_IGUAL(m)(n)(lambda _: m)(lambda _: n)(V)

# --------------------------------------------------------------------------
# MULTIPLICAÇÃO — m * n = ITER(n)(0)(x -> SOMA(m)(x))
# --------------------------------------------------------------------------
MULT = lambda m: lambda n: ITER(n)(ZERO)(lambda x: SOMA(m)(x))

# --------------------------------------------------------------------------
# POTENCIAÇÃO — m^n = ITER(n)(1)(x -> MULT(m)(x))
# (o "1" aqui é S(ZERO), construído localmente para não depender de
#  numerais externos)
# --------------------------------------------------------------------------
_UM = S(ZERO)
POT = lambda m: lambda n: ITER(n)(_UM)(lambda x: MULT(m)(x))

# --------------------------------------------------------------------------
# DIVISÃO INTEIRA — subtrações sucessivas, via Y (recursão geral)
# --------------------------------------------------------------------------
DIV = Y(lambda div: lambda m: lambda n:
    MENOR(m)(n)(
        lambda _: ZERO
    )(
        lambda _: S(div(SUB(m)(n))(n))
    )(V)
)

# --------------------------------------------------------------------------
# MÓDULO (resto da divisão) — mesma estratégia recursiva
# --------------------------------------------------------------------------
MOD = Y(lambda mod: lambda m: lambda n:
    MENOR(m)(n)(
        lambda _: m
    )(
        lambda _: mod(SUB(m)(n))(n)
    )(V)
)

# --------------------------------------------------------------------------
# MDC — Algoritmo de Euclides:  MDC(a,0)=a ;  MDC(a,b)=MDC(b, a mod b)
# --------------------------------------------------------------------------
MDC = Y(lambda mdc: lambda a: lambda b:
    IS_ZERO(b)(
        lambda _: a
    )(
        lambda _: mdc(b)(MOD(a)(b))
    )(V)
)

# --------------------------------------------------------------------------
# MMC —  MMC(a,b) = (a*b) / MDC(a,b)
# --------------------------------------------------------------------------
MMC = lambda a: lambda b: DIV(MULT(a)(b))(MDC(a)(b))
