# ==============================================================================
# PRIMALIDADE PURA — construída depois de divisibilidade.
# ==============================================================================
# Lei PSF-IAminy:
#   primo não nasce de tabela, nem de operador MOD, nem de fatoração pronta.
#   primo nasce da ausência de divisores internos.
#
# Dependências legítimas nesta etapa:
#   número natural, ordem, subtração truncada, resto euclidiano puro, intervalo.
#
# Dependências proibidas aqui:
#   DIV, MOD, MMC, fatoração pronta, módulo nativo, divisão nativa.
# ==============================================================================
from .primitivas import V, F, ZERO, S, PAR, Y
from .logica import E, NAO, OU
from .aritmetica import IS_ZERO, IGUAL, MENOR, MAIOR, SUB, _UM
from .combinadores import INTERVALO
from .divisao_euclidiana_pura import RESTO_PURO

_DOIS = S(_UM)


# --------------------------------------------------------------------------
# Divisor interno: um divisor d de n que está entre 2 e n-1.
# Não usamos divisão. Só perguntamos se d | n pela definição pura:
#   existe k natural tal que d*k = n.
# --------------------------------------------------------------------------
DIVIDE_POR_RESTO_PURO = lambda d: lambda n: E(MAIOR(d)(ZERO))(IS_ZERO(RESTO_PURO(n)(d)))

DIVISOR_INTERNO_PURO = lambda d: lambda n: E(MENOR(_UM)(d))(E(MENOR(d)(n))(DIVIDE_POR_RESTO_PURO(d)(n)))


# --------------------------------------------------------------------------
# Existe divisor interno em n?
# Para n=0,1,2 o intervalo [2,n-1] é vazio quando adequado.
# --------------------------------------------------------------------------
POSSUI_DIVISOR_INTERNO_PURO = lambda n: INTERVALO(_DOIS)(SUB(n)(_UM))(
    lambda d: lambda acc: OU(acc)(DIVIDE_POR_RESTO_PURO(d)(n))
)(F)


# --------------------------------------------------------------------------
# Primalidade pura:
#   n é primo ⇔ n > 1 e não existe divisor interno d com 2 <= d < n.
# --------------------------------------------------------------------------
PRIMO_PURO = lambda n: E(MAIOR(n)(_UM))(NAO(POSSUI_DIVISOR_INTERNO_PURO(n)))


# --------------------------------------------------------------------------
# Composto puro:
#   n é composto ⇔ n > 1 e existe divisor interno.
# --------------------------------------------------------------------------
COMPOSTO_PURO = lambda n: E(MAIOR(n)(_UM))(POSSUI_DIVISOR_INTERNO_PURO(n))


# --------------------------------------------------------------------------
# Menor fator puro:
#   para n >= 2, procura o primeiro d >= 2 tal que d | n.
# Como n sempre divide n, a busca termina sem precisar de fatoração prévia.
# --------------------------------------------------------------------------
_MENOR_FATOR_BUSCA = Y(lambda busca: lambda n: lambda d:
    DIVIDE_POR_RESTO_PURO(d)(n)(
        lambda _: d
    )(
        lambda _: busca(n)(S(d))
    )(V)
)

MENOR_FATOR_PURO = lambda n: _MENOR_FATOR_BUSCA(n)(_DOIS)


# --------------------------------------------------------------------------
# Crivo por enumeração:
#   não é ainda um crivo otimizado; é a enumeração honesta dos números em
#   [2, limite] filtrados por PRIMO_PURO.
# Lista: PAR(cabeça)(cauda), terminada em F.
# --------------------------------------------------------------------------
CRIVO_ENUMERACAO_PURO = lambda limite: INTERVALO(_DOIS)(limite)(
    lambda n: lambda acc: PRIMO_PURO(n)(
        lambda _: PAR(n)(acc)
    )(
        lambda _: acc
    )(V)
)(F)


# --------------------------------------------------------------------------
# Contagem pura de primos até limite.
# --------------------------------------------------------------------------
QTD_PRIMOS_ATE_PURO = lambda limite: INTERVALO(_DOIS)(limite)(
    lambda n: lambda acc: PRIMO_PURO(n)(
        lambda _: S(acc)
    )(
        lambda _: acc
    )(V)
)(ZERO)
