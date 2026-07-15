# ==============================================================================
# TEORIA DOS NÚMEROS NATURAL — Etapas 20 a 35 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   acelerar não significa saltar fundamentos.
#   Este módulo só usa conceitos já nascidos no fluxo:
#     divisibilidade, resto euclidiano puro, MDC puro, fatoração pura,
#     inteiros relativos puros e Bézout.
#
# Proibido aqui:
#   operador nativo de divisão, operador nativo de resto, aritmética modular
#   pronta, funções antigas de primos.py, DIV/MOD/MDC/MMC de aritmetica.py.
# ==============================================================================
from .primitivas import V, F, ZERO, S, PAR
from .logica import E, OU, NAO, IMPLICA
from .aritmetica import IS_ZERO, IGUAL, MENOR, MAIOR, MENOR_OU_IGUAL, SOMA, MULT, SUB, POT, _UM
from .combinadores import INTERVALO
from .divisibilidade_pura import DIVIDE_PURO, SOMA_DIVISORES_PURO, QTD_DIVISORES_PURO, SOMA_DIVISORES_PROPRIOS_PURO, PERFEITO_PURO
from .divisao_euclidiana_pura import RESTO_PURO, QUOCIENTE_PURO
from .mdc_puro import COPRIMOS_PURO, MDC_DEFINIDO_PURO
from .euclides_resto_puro import MDC_RESTO_PURO
from .primalidade_pura import PRIMO_PURO
from .bezout_euclides_puro import (
    INTEIRO_PURO,
    ZERO_INTEIRO_PURO,
    UM_INTEIRO_PURO,
    NATURAL_COMO_INTEIRO_PURO,
    IGUAL_INTEIRO_PURO,
    SOMA_INTEIRO_PURO,
    MULT_INTEIRO_PURO,
    MULT_INTEIRO_NATURAL_PURO,
    COMBINACAO_LINEAR_PURA,
    COEFICIENTE_X_BEZOUT_PURO,
    COEFICIENTE_Y_BEZOUT_PURO,
)

_DOIS = S(_UM)
_TRES = S(_DOIS)


# ------------------------------------------------------------------------------
# Etapas 20 e 21 — propriedades de divisibilidade sobre soma e produto.
# ------------------------------------------------------------------------------
DIVISIBILIDADE_FECHADA_SOMA_PURO = lambda d: lambda a: lambda b: IMPLICA(
    E(DIVIDE_PURO(d)(a))(DIVIDE_PURO(d)(b))
)(
    DIVIDE_PURO(d)(SOMA(a)(b))
)

DIVISIBILIDADE_FECHADA_PRODUTO_DIREITA_PURO = lambda d: lambda a: lambda c: IMPLICA(
    DIVIDE_PURO(d)(a)
)(
    DIVIDE_PURO(d)(MULT(a)(c))
)

DIVISIBILIDADE_FECHADA_PRODUTO_ESQUERDA_PURO = lambda d: lambda a: lambda c: IMPLICA(
    DIVIDE_PURO(d)(a)
)(
    DIVIDE_PURO(d)(MULT(c)(a))
)


# ------------------------------------------------------------------------------
# Etapa 22 — congruência como igualdade de restos.
# a ≡ b mod m nasce só depois do resto euclidiano puro.
# Para m=0, a relação fica indefinida e devolve F como sentinela.
# ------------------------------------------------------------------------------
MODULO_VALIDO_PURO = lambda m: MAIOR(m)(ZERO)

CONGRUENTES_PURO = lambda a: lambda b: lambda m: E(
    MODULO_VALIDO_PURO(m)
)(
    IGUAL(RESTO_PURO(a)(m))(RESTO_PURO(b)(m))
)


# ------------------------------------------------------------------------------
# Etapa 23 — congruência como relação de equivalência.
# ------------------------------------------------------------------------------
CONGRUENCIA_REFLEXIVA_PURO = lambda a: lambda m: IMPLICA(
    MODULO_VALIDO_PURO(m)
)(
    CONGRUENTES_PURO(a)(a)(m)
)

CONGRUENCIA_SIMETRICA_PURO = lambda a: lambda b: lambda m: IMPLICA(
    CONGRUENTES_PURO(a)(b)(m)
)(
    CONGRUENTES_PURO(b)(a)(m)
)

CONGRUENCIA_TRANSITIVA_PURO = lambda a: lambda b: lambda c: lambda m: IMPLICA(
    E(CONGRUENTES_PURO(a)(b)(m))(CONGRUENTES_PURO(b)(c)(m))
)(
    CONGRUENTES_PURO(a)(c)(m)
)


# ------------------------------------------------------------------------------
# Etapa 24 — classe residual finita até um limite dado.
# Lista: PAR(cabeça)(cauda), terminada em F.
# ------------------------------------------------------------------------------
CLASSE_RESIDUAL_ATE_PURO = lambda a: lambda m: lambda limite: INTERVALO(ZERO)(limite)(
    lambda x: lambda acc: CONGRUENTES_PURO(x)(a)(m)(
        lambda _: PAR(x)(acc)
    )(
        lambda _: acc
    )(F)
)(F)

REPRESENTANTE_CANONICO_PURO = lambda a: lambda m: MODULO_VALIDO_PURO(m)(
    lambda _: RESTO_PURO(a)(m)
)(
    lambda _: ZERO
)(V)


# ------------------------------------------------------------------------------
# Etapas 25, 26 e 27 — aritmética modular.
# ------------------------------------------------------------------------------
SOMA_MODULAR_PURA = lambda a: lambda b: lambda m: MODULO_VALIDO_PURO(m)(
    lambda _: RESTO_PURO(SOMA(a)(b))(m)
)(
    lambda _: ZERO
)(V)

MULT_MODULAR_PURA = lambda a: lambda b: lambda m: MODULO_VALIDO_PURO(m)(
    lambda _: RESTO_PURO(MULT(a)(b))(m)
)(
    lambda _: ZERO
)(V)

POT_MODULAR_PURA = lambda a: lambda e: lambda m: MODULO_VALIDO_PURO(m)(
    lambda _: INTERVALO(_UM)(e)(
        lambda _: lambda acc: MULT_MODULAR_PURA(acc)(a)(m)
    )(REPRESENTANTE_CANONICO_PURO(_UM)(m))
)(
    lambda _: ZERO
)(V)


# ------------------------------------------------------------------------------
# Etapa 28 — inverso modular por busca finita.
# O inverso existe quando m>1 e a é coprimo de m.
# ------------------------------------------------------------------------------
INVERSO_MODULAR_EXISTE_PURO = lambda a: lambda m: E(MAIOR(m)(_UM))(COPRIMOS_PURO(a)(m))

_INVERSO_SENTINELA = lambda m: S(m)

INVERSO_MODULAR_PURO = lambda a: lambda m: INVERSO_MODULAR_EXISTE_PURO(a)(m)(
    lambda _: INTERVALO(_UM)(m)(
        lambda x: lambda acc: MENOR_OU_IGUAL(acc)(m)(
            lambda _: acc
        )(
            lambda _: CONGRUENTES_PURO(MULT(a)(x))(_UM)(m)(
                lambda __: x
            )(
                lambda __: acc
            )(F)
        )(V)
    )(_INVERSO_SENTINELA(m))
)(
    lambda _: ZERO
)(V)

INVERSO_MODULAR_CONFERE_PURO = lambda a: lambda m: IMPLICA(
    INVERSO_MODULAR_EXISTE_PURO(a)(m)
)(
    CONGRUENTES_PURO(MULT(a)(INVERSO_MODULAR_PURO(a)(m)))(_UM)(m)
)


# ------------------------------------------------------------------------------
# Etapas 29, 30 e 31 — Fermat, phi de Euler e teorema de Euler.
# ------------------------------------------------------------------------------
PHI_EULER_PURO = lambda n: INTERVALO(_UM)(n)(
    lambda k: lambda acc: COPRIMOS_PURO(k)(n)(
        lambda _: S(acc)
    )(
        lambda _: acc
    )(F)
)(ZERO)

FERMAT_PEQUENO_TEOREMA_PURO = lambda a: lambda p: IMPLICA(
    E(PRIMO_PURO(p))(COPRIMOS_PURO(a)(p))
)(
    CONGRUENTES_PURO(POT_MODULAR_PURA(a)(SUB(p)(_UM))(p))(_UM)(p)
)

TEOREMA_EULER_PURO = lambda a: lambda n: IMPLICA(
    E(MAIOR(n)(_UM))(COPRIMOS_PURO(a)(n))
)(
    CONGRUENTES_PURO(POT_MODULAR_PURA(a)(PHI_EULER_PURO(n))(n))(_UM)(n)
)


# ------------------------------------------------------------------------------
# Etapa 32 — Teorema Chinês dos Restos por construção buscada.
# Para m,n coprimos e positivos, procura x em [0, m*n] que satisfaça as duas
# congruências. A existência conceitual fica no documento da etapa.
# ------------------------------------------------------------------------------
CRT_HIPOTESE_PURA = lambda m: lambda n: E(MODULO_VALIDO_PURO(m))(E(MODULO_VALIDO_PURO(n))(COPRIMOS_PURO(m)(n)))

_CRT_SENTINELA = lambda m: lambda n: S(MULT(m)(n))

CRT_SOLUCAO_PURA = lambda a: lambda m: lambda b: lambda n: CRT_HIPOTESE_PURA(m)(n)(
    lambda _: INTERVALO(ZERO)(MULT(m)(n))(
        lambda x: lambda acc: MENOR_OU_IGUAL(acc)(MULT(m)(n))(
            lambda __: acc
        )(
            lambda __: E(CONGRUENTES_PURO(x)(a)(m))(CONGRUENTES_PURO(x)(b)(n))(
                lambda ___: x
            )(
                lambda ___: acc
            )(F)
        )(V)
    )(_CRT_SENTINELA(m)(n))
)(
    lambda _: ZERO
)(V)

CRT_CONFERE_PURO = lambda a: lambda m: lambda b: lambda n: IMPLICA(
    CRT_HIPOTESE_PURA(m)(n)
)(
    E(
        CONGRUENTES_PURO(CRT_SOLUCAO_PURA(a)(m)(b)(n))(a)(m)
    )(
        CONGRUENTES_PURO(CRT_SOLUCAO_PURA(a)(m)(b)(n))(b)(n)
    )
)


# ------------------------------------------------------------------------------
# Etapa 33 — equação diofantina linear ax + by = c.
# c é natural nesta camada. x,y são inteiros relativos puros.
# ------------------------------------------------------------------------------
DIOFANTINA_LINEAR_SOLUVEL_PURO = lambda a: lambda b: lambda c: E(
    MDC_DEFINIDO_PURO(a)(b)
)(
    DIVIDE_PURO(MDC_RESTO_PURO(a)(b))(c)
)

SOLUCAO_DIOFANTINA_LINEAR_PURA = lambda a: lambda b: lambda c: DIOFANTINA_LINEAR_SOLUVEL_PURO(a)(b)(c)(
    lambda _: (lambda g: (lambda q: PAR(
        MULT_INTEIRO_NATURAL_PURO(COEFICIENTE_X_BEZOUT_PURO(a)(b))(q)
    )(
        MULT_INTEIRO_NATURAL_PURO(COEFICIENTE_Y_BEZOUT_PURO(a)(b))(q)
    ))(QUOCIENTE_PURO(c)(g)))(MDC_RESTO_PURO(a)(b))
)(
    lambda _: PAR(ZERO_INTEIRO_PURO)(ZERO_INTEIRO_PURO)
)(V)

DIOFANTINA_X_PURO = lambda sol: sol(V)
DIOFANTINA_Y_PURO = lambda sol: sol(F)

DIOFANTINA_CONFERE_PURO = lambda a: lambda b: lambda c: IMPLICA(
    DIOFANTINA_LINEAR_SOLUVEL_PURO(a)(b)(c)
)(
    IGUAL_INTEIRO_PURO(
        COMBINACAO_LINEAR_PURA(a)(b)(
            DIOFANTINA_X_PURO(SOLUCAO_DIOFANTINA_LINEAR_PURA(a)(b)(c))
        )(
            DIOFANTINA_Y_PURO(SOLUCAO_DIOFANTINA_LINEAR_PURA(a)(b)(c))
        )
    )(
        NATURAL_COMO_INTEIRO_PURO(c)
    )
)


# ------------------------------------------------------------------------------
# Etapa 34 — funções aritméticas naturais.
# tau(n), sigma(n) e phi(n) já são suficientes para inaugurar o bloco.
# ------------------------------------------------------------------------------
TAU_DIVISORES_PURO = QTD_DIVISORES_PURO
SIGMA_DIVISORES_PURO = SOMA_DIVISORES_PURO
SOMA_ALIQUOTA_PURO = SOMA_DIVISORES_PROPRIOS_PURO


# ------------------------------------------------------------------------------
# Etapa 35 — números especiais naturais.
# ------------------------------------------------------------------------------
AMIGAVEIS_PURO = lambda a: lambda b: E(
    NAO(IGUAL(a)(b))
)(
    E(IGUAL(SOMA_ALIQUOTA_PURO(a))(b))(IGUAL(SOMA_ALIQUOTA_PURO(b))(a))
)

MERSENNE_NUMERO_PURO = lambda p: SUB(POT(_DOIS)(p))(_UM)
MERSENNE_PRIMO_PURO = lambda p: E(PRIMO_PURO(p))(PRIMO_PURO(MERSENNE_NUMERO_PURO(p)))

FERMAT_NUMERO_PURO = lambda n: S(POT(_DOIS)(POT(_DOIS)(n)))
FERMAT_PRIMO_PURO = lambda n: PRIMO_PURO(FERMAT_NUMERO_PURO(n))

PERFEITO_REVISITADO_PURO = PERFEITO_PURO
