# ==============================================================================
# DIVISIBILIDADE PURA — construída SEM divisão, SEM resto e SEM módulo.
# ==============================================================================
# Lei PSF-IAminy:
#   a | b  <=>  a != 0 e existe k natural tal que a * k = b.
#
# Esta camada existe para corrigir a ordem conceitual: divisibilidade nasce de
# multiplicação + existência limitada, antes de qualquer DIV/MOD.
# ==============================================================================
from .primitivas import F, ZERO, S, PAR
from .logica import E, NAO
from .aritmetica import IS_ZERO, IGUAL, MENOR, SUB, SOMA, MULT, _UM
from .predicados import EXISTE
from .combinadores import INTERVALO


# --------------------------------------------------------------------------
# DIVISIBILIDADE BRUTA: aceita 0 | 0 como caso degenerado, pois 0*k = 0.
# Não é a relação estável usada pela teoria usual; fica documentada para
# honestidade fundacional.
# --------------------------------------------------------------------------
DIVIDE_BRUTO = lambda a: lambda b: EXISTE(b)(lambda k: IGUAL(MULT(a)(k))(b))


# --------------------------------------------------------------------------
# DIVISIBILIDADE ESTÁVEL: exclui divisor zero.
# a divide b se a != 0 e existe k em [0,b] tal que a*k = b.
# O limite b é suficiente para naturais positivos: se a>0 e a*k=b, então k<=b.
# --------------------------------------------------------------------------
DIVIDE_PURO = lambda a: lambda b: E(NAO(IS_ZERO(a)))(DIVIDE_BRUTO(a)(b))


# --------------------------------------------------------------------------
# MÚLTIPLO: b é múltiplo de a <=> a divide b.
# --------------------------------------------------------------------------
MULTIPLO_PURO = lambda a: lambda b: DIVIDE_PURO(a)(b)


# --------------------------------------------------------------------------
# DIVISOR PRÓPRIO: d divide n e d < n.
# --------------------------------------------------------------------------
DIVISOR_PROPRIO_PURO = lambda d: lambda n: E(DIVIDE_PURO(d)(n))(MENOR(d)(n))


# --------------------------------------------------------------------------
# LISTA/SOMA/QUANTIDADE de divisores pela definição pura.
# Lista segue a convenção cons/nil do projeto: PAR(cabeça)(cauda), F vazio.
# --------------------------------------------------------------------------
LISTA_DIVISORES_PURO = lambda n: INTERVALO(_UM)(n)(
    lambda d: lambda acc: DIVIDE_PURO(d)(n)(
        lambda _: PAR(d)(acc)
    )(
        lambda _: acc
    )(F)
)(F)

QTD_DIVISORES_PURO = lambda n: INTERVALO(_UM)(n)(
    lambda d: lambda acc: DIVIDE_PURO(d)(n)(lambda _: S(acc))(lambda _: acc)(F)
)(ZERO)

SOMA_DIVISORES_PURO = lambda n: INTERVALO(_UM)(n)(
    lambda d: lambda acc: DIVIDE_PURO(d)(n)(lambda _: SOMA(acc)(d))(lambda _: acc)(F)
)(ZERO)

SOMA_DIVISORES_PROPRIOS_PURO = lambda n: INTERVALO(_UM)(SUB(n)(_UM))(
    lambda d: lambda acc: DIVIDE_PURO(d)(n)(lambda _: SOMA(acc)(d))(lambda _: acc)(F)
)(ZERO)


# --------------------------------------------------------------------------
# Classificação pela soma de divisores próprios.
# --------------------------------------------------------------------------
PERFEITO_PURO = lambda n: IGUAL(SOMA_DIVISORES_PROPRIOS_PURO(n))(n)
DEFICIENTE_PURO = lambda n: MENOR(SOMA_DIVISORES_PROPRIOS_PURO(n))(n)
ABUNDANTE_PURO = lambda n: MENOR(n)(SOMA_DIVISORES_PROPRIOS_PURO(n))
