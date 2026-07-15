# ==============================================================================
# COMBINATÓRIA NATURAL — Etapas 36 a 60 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   depois de teoria dos números natural, a matemática segue para contagem
#   estruturada. Este módulo não usa combinatoria.py antigo, catalan_stirling.py
#   antigo, DIV/MOD/MMC de aritmetica.py, nem operadores nativos /, //, %.
#
# Conceitos permitidos aqui:
#   ZERO/S/PAR/Y, lógica, ordem, soma, subtração já construída, multiplicação,
#   potência, quociente euclidiano puro, resto puro e INTERVALO.
# ==============================================================================
from .primitivas import V, F, ZERO, S, PAR, Y, ITER
from .logica import E, OU, NAO, IMPLICA
from .aritmetica import IS_ZERO, IGUAL, MENOR, MAIOR, MENOR_OU_IGUAL, SOMA, SUB, MULT, POT, PRED, _UM
from .combinadores import INTERVALO
from .divisao_euclidiana_pura import QUOCIENTE_PURO
from .teoria_numeros_natural import SOMA_MODULAR_PURA, MULT_MODULAR_PURA

_DOIS = S(_UM)
_TRES = S(_DOIS)


# ------------------------------------------------------------------------------
# Etapas 36 a 38 — princípios de contagem finita.
# ------------------------------------------------------------------------------
PRINCIPIO_ADITIVO_PURO = lambda a: lambda b: SOMA(a)(b)
PRINCIPIO_MULTIPLICATIVO_PURO = lambda a: lambda b: MULT(a)(b)
CONTAGEM_FINITA_UNIAO_DISJUNTA_PURA = PRINCIPIO_ADITIVO_PURO
CONTAGEM_FINITA_PRODUTO_CARTESIANO_PURA = PRINCIPIO_MULTIPLICATIVO_PURO


# ------------------------------------------------------------------------------
# Etapa 39 — escolha ordenada com repetição.
# n opções em k posições: n^k.
# ------------------------------------------------------------------------------
ESCOLHAS_ORDENADAS_COM_REPETICAO_PURO = lambda n: lambda k: POT(n)(k)


# ------------------------------------------------------------------------------
# Etapa 40 — fatorial como produtório finito de 1 até n.
# ------------------------------------------------------------------------------
FATORIAL_NATURAL_PURO = lambda n: INTERVALO(_UM)(n)(
    lambda k: lambda acc: MULT(acc)(k)
)(_UM)


# ------------------------------------------------------------------------------
# Etapas 41 a 43 — permutação, arranjo e combinação.
# Para k>n, devolvem ZERO como sentinela natural.
# ------------------------------------------------------------------------------
PERMUTACOES_SIMPLES_PURO = FATORIAL_NATURAL_PURO

ARRANJOS_SIMPLES_PURO = lambda n: lambda k: MENOR_OU_IGUAL(k)(n)(
    lambda _: QUOCIENTE_PURO(FATORIAL_NATURAL_PURO(n))(FATORIAL_NATURAL_PURO(SUB(n)(k)))
)(
    lambda _: ZERO
)(V)

COMBINACOES_SIMPLES_PURO = lambda n: lambda k: MENOR_OU_IGUAL(k)(n)(
    lambda _: QUOCIENTE_PURO(ARRANJOS_SIMPLES_PURO(n)(k))(FATORIAL_NATURAL_PURO(k))
)(
    lambda _: ZERO
)(V)


# ------------------------------------------------------------------------------
# Etapas 44 e 45 — simetria binomial e Pascal por recorrência.
# ------------------------------------------------------------------------------
BINOMIAL_FATORIAL_PURO = COMBINACOES_SIMPLES_PURO

BINOMIAL_PASCAL_PURO = Y(lambda C: lambda n: lambda k: MENOR_OU_IGUAL(k)(n)(
    lambda _: OU(IS_ZERO(k))(IGUAL(k)(n))(
        lambda __: _UM
    )(
        lambda __: SOMA(C(PRED(n))(PRED(k)))(C(PRED(n))(k))
    )(V)
)(
    lambda _: ZERO
)(V))

BINOMIAL_SIMETRIA_CONFERE_PURO = lambda n: lambda k: IMPLICA(
    MENOR_OU_IGUAL(k)(n)
)(
    IGUAL(BINOMIAL_PASCAL_PURO(n)(k))(BINOMIAL_PASCAL_PURO(n)(SUB(n)(k)))
)


# ------------------------------------------------------------------------------
# Etapa 46 — binómio de Newton finito por soma de termos.
# (a+b)^n = soma C(n,k)a^(n-k)b^k.
# ------------------------------------------------------------------------------
BINOMIO_TERMO_PURO = lambda n: lambda k: lambda a: lambda b: MULT(
    BINOMIAL_PASCAL_PURO(n)(k)
)(
    MULT(POT(a)(SUB(n)(k)))(POT(b)(k))
)

BINOMIO_EXPANSAO_SOMA_PURO = lambda n: lambda a: lambda b: INTERVALO(ZERO)(n)(
    lambda k: lambda acc: SOMA(acc)(BINOMIO_TERMO_PURO(n)(k)(a)(b))
)(ZERO)

BINOMIO_CONFERE_PURO = lambda n: lambda a: lambda b: IGUAL(
    POT(SOMA(a)(b))(n)
)(
    BINOMIO_EXPANSAO_SOMA_PURO(n)(a)(b)
)


# ------------------------------------------------------------------------------
# Etapa 47 — inclusão-exclusão básica para duas grandezas finitas.
# |A ∪ B| = |A| + |B| - |A ∩ B|, quando a interseção foi contada duas vezes.
# ------------------------------------------------------------------------------
INCLUSAO_EXCLUSAO_DOIS_PURO = lambda tamanho_a: lambda tamanho_b: lambda tamanho_intersecao: SUB(
    SOMA(tamanho_a)(tamanho_b)
)(
    tamanho_intersecao
)


# ------------------------------------------------------------------------------
# Etapas 48 a 51 — sequências finitas e recorrências clássicas.
# ------------------------------------------------------------------------------
SEQUENCIA_ITERADA_PURA = lambda inicial: lambda passo: lambda n: ITER(n)(inicial)(passo)
PA_TERMO_PURO = lambda a0: lambda d: lambda n: SOMA(a0)(MULT(n)(d))
PG_TERMO_PURO = lambda a0: lambda r: lambda n: MULT(a0)(POT(r)(n))

_PASSO_FIB_PURO = lambda p: PAR(p(F))(SOMA(p(V))(p(F)))
FIBONACCI_NATURAL_PURO = lambda n: ITER(n)(PAR(ZERO)(_UM))(_PASSO_FIB_PURO)(V)

_PASSO_LUCAS_PURO = lambda p: PAR(p(F))(SOMA(p(V))(p(F)))
LUCAS_NATURAL_PURO = lambda n: ITER(n)(PAR(_DOIS)(_UM))(_PASSO_LUCAS_PURO)(V)


# ------------------------------------------------------------------------------
# Etapa 52 — números figurados básicos revisitados sem módulo antigo.
# ------------------------------------------------------------------------------
TRIANGULAR_NATURAL_PURO = lambda n: QUOCIENTE_PURO(MULT(n)(S(n)))(_DOIS)
QUADRADO_NATURAL_PURO = lambda n: MULT(n)(n)
PENTAGONAL_NATURAL_PURO = lambda n: QUOCIENTE_PURO(MULT(n)(SUB(MULT(_TRES)(n))(_UM)))(_DOIS)
HEXAGONAL_NATURAL_PURO = lambda n: MULT(n)(SUB(MULT(_DOIS)(n))(_UM))


# ------------------------------------------------------------------------------
# Etapas 53 a 55 — Catalan, Stirling de segunda espécie e Bell.
# ------------------------------------------------------------------------------
CATALAN_NATURAL_PURO = lambda n: QUOCIENTE_PURO(
    BINOMIAL_PASCAL_PURO(SOMA(n)(n))(n)
)(
    S(n)
)

STIRLING2_NATURAL_PURO = Y(lambda st: lambda n: lambda k: IS_ZERO(n)(
    lambda _: IS_ZERO(k)(lambda __: _UM)(lambda __: ZERO)(V)
)(
    lambda _: IS_ZERO(k)(
        lambda __: ZERO
    )(
        lambda __: IGUAL(n)(k)(
            lambda ___: _UM
        )(
            lambda ___: SOMA(MULT(k)(st(PRED(n))(k)))(st(PRED(n))(PRED(k)))
        )(V)
    )(V)
)(V))

BELL_NATURAL_PURO = lambda n: INTERVALO(ZERO)(n)(
    lambda k: lambda acc: SOMA(acc)(STIRLING2_NATURAL_PURO(n)(k))
)(ZERO)


# ------------------------------------------------------------------------------
# Etapa 56 — partições inteiras por recorrência p(n,k).
# p(n,k) = partições de n usando partes até k.
# ------------------------------------------------------------------------------
PARTICOES_RESTRITAS_PURO = Y(lambda part: lambda n: lambda k: IS_ZERO(n)(
    lambda _: _UM
)(
    lambda _: IS_ZERO(k)(
        lambda __: ZERO
    )(
        lambda __: MENOR(n)(k)(
            lambda ___: part(n)(n)
        )(
            lambda ___: SOMA(part(n)(PRED(k)))(part(SUB(n)(k))(k))
        )(V)
    )(V)
)(V))

PARTICOES_INTEIRAS_PURO = lambda n: PARTICOES_RESTRITAS_PURO(n)(n)


# ------------------------------------------------------------------------------
# Etapas 57 a 60 — versão modular de contagens, preservando o fluxo já nascido.
# ------------------------------------------------------------------------------
FATORIAL_MODULAR_PURO = lambda n: lambda m: INTERVALO(_UM)(n)(
    lambda k: lambda acc: MULT_MODULAR_PURA(acc)(k)(m)
)(_UM)

BINOMIAL_MODULAR_PURO = lambda n: lambda k: lambda m: SOMA_MODULAR_PURA(
    BINOMIAL_PASCAL_PURO(n)(k)
)(ZERO)(m)

FIBONACCI_MODULAR_PURO = lambda n: lambda m: SOMA_MODULAR_PURA(
    FIBONACCI_NATURAL_PURO(n)
)(ZERO)(m)

COMBINATORIA_FECHA_BLOCO_PURO = lambda n: E(
    IGUAL(BINOMIAL_PASCAL_PURO(n)(ZERO))(_UM)
)(
    IGUAL(BINOMIAL_PASCAL_PURO(n)(n))(_UM)
)
