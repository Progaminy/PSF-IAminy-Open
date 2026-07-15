# ==============================================================================
# NÚMEROS RACIONAIS — como pares ordenados (numerador, denominador)
# ==============================================================================
from .primitivas import V, F, PAR, ITER
from .aritmetica import MULT, IGUAL, SOMA, SUB, MDC, DIV, _UM

RAC = lambda num: lambda den: PAR(num)(den)
NUM = lambda r: r(V)   # numerador
DEN = lambda r: r(F)   # denominador

# --------------------------------------------------------------------------
# IGUALDADE POR MULTIPLICAÇÃO CRUZADA — a/b == c/d  <=>  a*d == c*b
# --------------------------------------------------------------------------
EQ_RAC = lambda r1: lambda r2: IGUAL(
    MULT(NUM(r1))(DEN(r2))
)(
    MULT(NUM(r2))(DEN(r1))
)

# --------------------------------------------------------------------------
# SOMA — a/b + c/d = (a*d + c*b) / (b*d)
# --------------------------------------------------------------------------
SOMA_RAC = lambda r1: lambda r2: RAC(
    SOMA(MULT(NUM(r1))(DEN(r2)))(MULT(NUM(r2))(DEN(r1)))
)(
    MULT(DEN(r1))(DEN(r2))
)

# --------------------------------------------------------------------------
# MULTIPLICAÇÃO — a/b * c/d = (a*c) / (b*d)
# --------------------------------------------------------------------------
MULT_RAC = lambda r1: lambda r2: RAC(
    MULT(NUM(r1))(NUM(r2))
)(
    MULT(DEN(r1))(DEN(r2))
)

# --------------------------------------------------------------------------
# SIMPLIFICAÇÃO — divide numerador e denominador pelo MDC
# --------------------------------------------------------------------------
SIMPLIFICAR = lambda r: RAC(
    DIV(NUM(r))(MDC(NUM(r))(DEN(r)))
)(
    DIV(DEN(r))(MDC(NUM(r))(DEN(r)))
)

# --------------------------------------------------------------------------
# Tópico 24 (Área 1): SUBTRAÇÃO DE FRAÇÕES — a/b − c/d = (ad − cb)/(bd)
# Usa a SUB truncada do núcleo sobre os numeradores cruzados: só é a
# diferença VERDADEIRA quando r1 >= r2 numericamente. Para diferenças
# que podem ser negativas, usar racionais assinados (fora do escopo
# desta versão — mesma lacuna documentada em `inteiros.py`).
# --------------------------------------------------------------------------
SUB_RAC = lambda r1: lambda r2: RAC(
    SUB(MULT(NUM(r1))(DEN(r2)))(MULT(NUM(r2))(DEN(r1)))
)(
    MULT(DEN(r1))(DEN(r2))
)

# --------------------------------------------------------------------------
# Tópico 26 (Área 1): DIVISÃO DE FRAÇÕES — a/b ÷ c/d = a/b × d/c
# --------------------------------------------------------------------------
DIV_RAC = lambda r1: lambda r2: MULT_RAC(r1)(RAC(DEN(r2))(NUM(r2)))

# --------------------------------------------------------------------------
# Tópico 52 (Área 1): NÚMERO INVERSO (recíproco) — 1/r, trocando num/den.
# r × RECIPROCO_RAC(r) == 1 (não simplificado: dá NUM*DEN / DEN*NUM).
# --------------------------------------------------------------------------
RECIPROCO_RAC = lambda r: RAC(DEN(r))(NUM(r))

# --------------------------------------------------------------------------
# POTÊNCIA DE EXPOENTE NATURAL — (a/b)^n, via ITER (mesmo padrão de POT em
# aritmetica.py). Necessário para probabilidade binomial (Área 8).
# --------------------------------------------------------------------------
POT_RAC = lambda r: lambda n: ITER(n)(RAC(_UM)(_UM))(lambda acc: MULT_RAC(acc)(r))
