# ==============================================================================
# GEOMETRIA NO PLANO DISCRETO (sobre inteiros) — Derivada da aritmética
# ==============================================================================
# Nota: no material original a função de acesso à coordenada Y tinha o
# mesmo nome do combinador Y (colisão de nomes). Aqui ela chama-se `COY`
# para não sombrear o Y (ponto fixo) importado de `primitivas`.
from .primitivas import V, F, PAR, S
from .aritmetica import SOMA, SUB, MULT, MENOR, IS_ZERO, IGUAL, POT, ZERO, _UM
# NOTA IMPORTANTE (lacuna herdada do material original, corrigida aqui):
# este núcleo só tem SUB truncada (m ∸ n = max(0, m-n)), porque os
# numerais de Church/Peano não representam negativos. Isso é inofensivo
# em ALINHADOS/PERPENDICULARES/PARALELAS *desde que se compare com
# IGUAL (equivalência de verdade) em vez de IS_ZERO(SUB(...)) — usar
# IS_ZERO(SUB(a)(b)) só testa "a <= b", não "a == b", e dá falsos
# positivos sempre que a < b. Resolvido com um tipo INTEIRO assinado
# (ver `inteiros.py`) para os vetores — DX, DY, PERPENDICULARES e
# PARALELAS usam subtração verdadeira, não truncada.
from .racionais import RAC
from .inteiros import DE_NATURAL, SUB_INT, MULT_INT, SOMA_INT, IS_ZERO_INT, EQ_INT

_DOIS = S(_UM)

# --------------------------------------------------------------------------
# PONTO E VETOR
# --------------------------------------------------------------------------
PONTO = lambda x: lambda y: PAR(x)(y)
COX = lambda p: p(V)     # coordenada x
COY = lambda p: p(F)     # coordenada y

# VETOR usa subtração ASSINADA (SUB_INT), não a SUB truncada — um vetor
# precisa poder apontar "para trás" (componente negativa).
VETOR = lambda p1: lambda p2: PAR(
    SUB_INT(DE_NATURAL(COX(p2)))(DE_NATURAL(COX(p1)))
)(
    SUB_INT(DE_NATURAL(COY(p2)))(DE_NATURAL(COY(p1)))
)
DX = lambda v: v(V)   # inteiro assinado
DY = lambda v: v(F)   # inteiro assinado

# --------------------------------------------------------------------------
# VALOR ABSOLUTO — sobre a subtração truncada já definida
# --------------------------------------------------------------------------
ABS = lambda n: MENOR(n)(ZERO)(lambda _: SUB(ZERO)(n))(lambda _: n)(V)

# --------------------------------------------------------------------------
# DISTÂNCIA DE MANHATTAN
# --------------------------------------------------------------------------
DIST_MANHATTAN = lambda p1: lambda p2: SOMA(
    ABS(SUB(COX(p2))(COX(p1)))
)(
    ABS(SUB(COY(p2))(COY(p1)))
)

# --------------------------------------------------------------------------
# DISTÂNCIA EUCLIDIANA AO QUADRADO (evita raiz quadrada)
# --------------------------------------------------------------------------
DIST_EUCL_QUAD = lambda p1: lambda p2: SOMA(
    POT(SUB(COX(p2))(COX(p1)))(_DOIS)
)(
    POT(SUB(COY(p2))(COY(p1)))(_DOIS)
)

# --------------------------------------------------------------------------
# ALINHAMENTO DE TRÊS PONTOS (determinante 3x3 = 0)
# |x1 y1 1|
# |x2 y2 1| = x1*y2 + x3*y1 + x2*y3 - x3*y2 - x1*y3 - x2*y1
# |x3 y3 1|
# Corrigido para usar IGUAL (equivalência real) em vez de
# IS_ZERO(SUB(...)) — a versão original dava falso-positivo sempre que
# o lado direito era maior que o esquerdo (ver nota sobre SUB truncada
# no topo do ficheiro).
# --------------------------------------------------------------------------
ALINHADOS = lambda p1: lambda p2: lambda p3: IGUAL(
    SOMA(SOMA(
        MULT(COX(p1))(COY(p2))
    )(
        MULT(COX(p3))(COY(p1))
    ))(MULT(COX(p2))(COY(p3)))
)(
    SOMA(SOMA(
        MULT(COX(p3))(COY(p2))
    )(
        MULT(COX(p1))(COY(p3))
    ))(MULT(COX(p2))(COY(p1)))
)

# --------------------------------------------------------------------------
# PONTO MÉDIO (coordenadas racionais)
# --------------------------------------------------------------------------
PONTO_MEDIO = lambda p1: lambda p2: PAR(
    RAC(SOMA(COX(p1))(COX(p2)))(_DOIS)
)(
    RAC(SOMA(COY(p1))(COY(p2)))(_DOIS)
)

# --------------------------------------------------------------------------
# COEFICIENTE ANGULAR COMO RACIONAL
# --------------------------------------------------------------------------
COEF_ANGULAR = lambda p1: lambda p2: RAC(
    SUB(COY(p2))(COY(p1))
)(
    SUB(COX(p2))(COX(p1))
)

# --------------------------------------------------------------------------
# PERPENDICULARIDADE — dy1*dy2 + dx1*dx2 = 0  (produto escalar nulo)
# Corrigido para usar o vetor assinado (VETOR/DX/DY) e MULT_INT/SOMA_INT/
# IS_ZERO_INT — a versão original usava SUB truncada e dava falso-positivo
# sempre que um segmento "andava para trás" em algum eixo.
# --------------------------------------------------------------------------
PERPENDICULARES = lambda p1: lambda p2: lambda q1: lambda q2: IS_ZERO_INT(
    SOMA_INT(
        MULT_INT(DY(VETOR(p1)(p2)))(DY(VETOR(q1)(q2)))
    )(
        MULT_INT(DX(VETOR(p1)(p2)))(DX(VETOR(q1)(q2)))
    )
)

# --------------------------------------------------------------------------
# PARALELISMO — mesmo coeficiente angular, por multiplicação cruzada:
# dy1*dx2 == dy2*dx1. Mesma correção: vetores assinados + EQ_INT.
# --------------------------------------------------------------------------
PARALELAS = lambda p1: lambda p2: lambda q1: lambda q2: EQ_INT(
    MULT_INT(DY(VETOR(p1)(p2)))(DX(VETOR(q1)(q2)))
)(
    MULT_INT(DY(VETOR(q1)(q2)))(DX(VETOR(p1)(p2)))
)
