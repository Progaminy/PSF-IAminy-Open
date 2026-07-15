# ==============================================================================
# NÚMEROS INTEIROS — pares (parte-positiva, parte-negativa) de naturais.
# ==============================================================================
# LACUNA PREENCHIDA: os numerais de Church/Peano do núcleo (ZERO, S) e a
# SUB derivada deles são truncados — SUB(m)(n) = max(0, m-n) — porque não
# existe "menos que zero" nesse sistema. Isso é invisível na aritmética
# pura (MDC, primos, etc. nunca precisam de negativos), mas quebra
# silenciosamente qualquer coisa que precise de diferenças reais — como
# vetores em geometria (ver PERPENDICULARES, PARALELAS, COEF_ANGULAR).
#
# A solução é o mesmo truque já usado para os RACIONAIS: em vez de negar
# a estrutura, envolvê-la num par. Um inteiro z = (p, n) representa p - n.
# Não há uma "forma canônica" única (3 = (3,0) = (5,2) = ...), exatamente
# como 1/2 = 2/4 nos racionais — e por isso a igualdade é por
# equivalência cruzada, não por comparação estrutural direta.
from .primitivas import V, F, PAR
from .aritmetica import SOMA, MULT, IGUAL, MENOR, ZERO

INTEIRO = lambda pos: lambda neg: PAR(pos)(neg)
PARTE_POS = lambda z: z(V)
PARTE_NEG = lambda z: z(F)

DE_NATURAL = lambda n: INTEIRO(n)(ZERO)   # mergulha um natural como inteiro >= 0

# --------------------------------------------------------------------------
# IGUALDADE — z1 ~ z2  <=>  p1 + n2 == p2 + n1   (equivalente a p1-n1 == p2-n2,
# mas só usa SOMA, que nunca trunca)
# --------------------------------------------------------------------------
EQ_INT = lambda z1: lambda z2: IGUAL(
    SOMA(PARTE_POS(z1))(PARTE_NEG(z2))
)(
    SOMA(PARTE_POS(z2))(PARTE_NEG(z1))
)

IS_ZERO_INT = lambda z: EQ_INT(z)(INTEIRO(ZERO)(ZERO))
EH_NEGATIVO = lambda z: MENOR(PARTE_POS(z))(PARTE_NEG(z))

# --------------------------------------------------------------------------
# Tópico 51 (Área 1): NÚMERO OPOSTO — troca parte positiva com negativa.
# z + OPOSTO_INT(z) ~ 0 (por EQ_INT, não por igualdade estrutural).
# --------------------------------------------------------------------------
OPOSTO_INT = lambda z: INTEIRO(PARTE_NEG(z))(PARTE_POS(z))

# --------------------------------------------------------------------------
# SOMA — (p1-n1) + (p2-n2) = (p1+p2) - (n1+n2)
# --------------------------------------------------------------------------
SOMA_INT = lambda z1: lambda z2: INTEIRO(
    SOMA(PARTE_POS(z1))(PARTE_POS(z2))
)(
    SOMA(PARTE_NEG(z1))(PARTE_NEG(z2))
)

# --------------------------------------------------------------------------
# SUBTRAÇÃO — verdadeira, não-truncada:
# (p1-n1) - (p2-n2) = (p1+n2) - (n1+p2)
# --------------------------------------------------------------------------
SUB_INT = lambda z1: lambda z2: INTEIRO(
    SOMA(PARTE_POS(z1))(PARTE_NEG(z2))
)(
    SOMA(PARTE_NEG(z1))(PARTE_POS(z2))
)

# --------------------------------------------------------------------------
# MULTIPLICAÇÃO — (p1-n1)(p2-n2) = (p1p2+n1n2) - (p1n2+n1p2)
# --------------------------------------------------------------------------
MULT_INT = lambda z1: lambda z2: INTEIRO(
    SOMA(MULT(PARTE_POS(z1))(PARTE_POS(z2)))(MULT(PARTE_NEG(z1))(PARTE_NEG(z2)))
)(
    SOMA(MULT(PARTE_POS(z1))(PARTE_NEG(z2)))(MULT(PARTE_NEG(z1))(PARTE_POS(z2)))
)
