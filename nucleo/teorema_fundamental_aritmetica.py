# ==============================================================================
# TEOREMA FUNDAMENTAL DA ARITMÉTICA — camada construída após fatoração pura.
# ==============================================================================
# Lei PSF-IAminy:
#   não usamos fatoração para definir primo;
#   agora, depois de primo e fatoração terem nascido, podemos estudar a
#   decomposição prima como objeto matemático.
#
# Observação honesta de implementação:
#   a lista antiga do projeto é codificada como PAR(cabeça)(cauda) e termina em F.
#   Essa codificação constrói listas bem, mas para inspecioná-las no Python atual
#   precisamos reconhecer a sentinela F, exatamente como faz traducao.para_lista.
#   Isto não introduz divisão, módulo, primalidade pronta ou fatoração externa.
#
# Dependências proibidas aqui:
#   operador nativo de divisão, operador nativo de resto, módulo pronto,
#   divisão pronta, primos.py, aritmética.DIV, aritmética.MOD, aritmética.MDC,
#   aritmética.MMC.
# ==============================================================================
from .primitivas import V, F, ZERO, S, PAR
from .logica import E, IMPLICA
from .aritmetica import IGUAL, MAIOR, MULT, _UM
from .primalidade_pura import PRIMO_PURO
from .fatoracao_pura import FATORACAO_PURA
from .mdc_puro import MDC_PURO, MDC_DEFINIDO_PURO


# --------------------------------------------------------------------------
# Lista vazia tipo-PSF:
#   lista vazia = F
#   cons(a, resto) = PAR(a)(resto)
# --------------------------------------------------------------------------
def LISTA_VAZIA_PURA(lista):
    return V if lista is F else F


# --------------------------------------------------------------------------
# Produto de fatores:
#   produto([]) = 1
#   produto(cabeça :: cauda) = cabeça × produto(cauda)
# --------------------------------------------------------------------------
def PRODUTO_LISTA_PURO(lista):
    if lista is F:
        return _UM
    return MULT(lista(V))(PRODUTO_LISTA_PURO(lista(F)))


# --------------------------------------------------------------------------
# Todos os elementos de uma lista são primos?
# Lista vazia satisfaz a condição por vacuidade.
# --------------------------------------------------------------------------
def TODOS_PRIMOS_LISTA_PURO(lista):
    if lista is F:
        return V
    return E(PRIMO_PURO(lista(V)))(TODOS_PRIMOS_LISTA_PURO(lista(F)))


# --------------------------------------------------------------------------
# Existência operacional da decomposição prima:
#   fatoracao(n) deve multiplicar de volta para n.
# Para n=1, a fatoração vazia tem produto 1.
# --------------------------------------------------------------------------
FATORACAO_RECONSTROI_NUMERO = lambda n: IGUAL(
    PRODUTO_LISTA_PURO(FATORACAO_PURA(n))
)(n)


# --------------------------------------------------------------------------
# A decomposição produzida deve conter apenas primos.
# --------------------------------------------------------------------------
FATORACAO_CONTEM_APENAS_PRIMOS = lambda n: TODOS_PRIMOS_LISTA_PURO(
    FATORACAO_PURA(n)
)


# --------------------------------------------------------------------------
# Teorema fundamental — parte operacional:
#   se n > 1, então a fatoração encontrada reconstrói n e é feita só de primos.
# A prova conceitual vive em conhecimento/ETAPA_13_TFA_EXISTENCIA.md.
# --------------------------------------------------------------------------
TFA_EXISTENCIA_OPERACIONAL = lambda n: IMPLICA(
    MAIOR(n)(_UM)
)(
    E(FATORACAO_RECONSTROI_NUMERO(n))(FATORACAO_CONTEM_APENAS_PRIMOS(n))
)


# --------------------------------------------------------------------------
# Contagem de ocorrências de um valor dentro de uma lista.
# --------------------------------------------------------------------------
def CONTA_VALOR_LISTA_PURO(valor):
    def contar(lista):
        if lista is F:
            return ZERO
        resto = contar(lista(F))
        return IGUAL(lista(V))(valor)(
            lambda _: S(resto)
        )(
            lambda _: resto
        )(V)
    return contar


# --------------------------------------------------------------------------
# Remover uma única ocorrência de valor em lista.
# Se valor não aparece, a lista volta estruturalmente preservada.
# --------------------------------------------------------------------------
def REMOVER_UMA_OCORRENCIA_PURO(valor):
    def remover(lista):
        if lista is F:
            return F
        cabeca = lista(V)
        cauda = lista(F)
        return IGUAL(cabeca)(valor)(
            lambda _: cauda
        )(
            lambda _: PAR(cabeca)(remover(cauda))
        )(V)
    return remover


# --------------------------------------------------------------------------
# Igualdade de fatorações como multiconjuntos.
# A ordem não importa; a quantidade de cada fator importa.
# --------------------------------------------------------------------------
def MESMO_MULTICONJUNTO_PURO(xs):
    def comparar(ys):
        if xs is F:
            return LISTA_VAZIA_PURA(ys)
        cabeca = xs(V)
        cauda = xs(F)
        return MAIOR(CONTA_VALOR_LISTA_PURO(cabeca)(ys))(ZERO)(
            lambda _: MESMO_MULTICONJUNTO_PURO(cauda)(REMOVER_UMA_OCORRENCIA_PURO(cabeca)(ys))
        )(
            lambda _: F
        )(V)
    return comparar


# --------------------------------------------------------------------------
# Unicidade operacional:
# uma lista de fatores candidata representa a mesma decomposição canônica de n
# quando contém exatamente os mesmos fatores, com as mesmas repetições.
# A prova matemática de unicidade está no documento teórico da etapa.
# --------------------------------------------------------------------------
FATORACAO_EQUIVALE_A_CANONICA = lambda n: lambda fatores: MESMO_MULTICONJUNTO_PURO(
    FATORACAO_PURA(n)
)(fatores)


# --------------------------------------------------------------------------
# Interseção de multiconjuntos de fatores.
# Cada fator comum entra uma vez e é removido da segunda lista.
# O produto da interseção é o MDC por fatores.
# --------------------------------------------------------------------------
def PRODUTO_INTERSECAO_FATORES_PURO(xs):
    def inter(ys):
        if xs is F:
            return _UM
        cabeca = xs(V)
        cauda = xs(F)
        return MAIOR(CONTA_VALOR_LISTA_PURO(cabeca)(ys))(ZERO)(
            lambda _: MULT(cabeca)(PRODUTO_INTERSECAO_FATORES_PURO(cauda)(REMOVER_UMA_OCORRENCIA_PURO(cabeca)(ys)))
        )(
            lambda _: PRODUTO_INTERSECAO_FATORES_PURO(cauda)(ys)
        )(V)
    return inter


MDC_POR_FATORES_PURO = lambda a: lambda b: PRODUTO_INTERSECAO_FATORES_PURO(
    FATORACAO_PURA(a)
)(FATORACAO_PURA(b))


MDC_POR_FATORES_CONFERE = lambda a: lambda b: IMPLICA(
    MDC_DEFINIDO_PURO(a)(b)
)(
    IGUAL(MDC_POR_FATORES_PURO(a)(b))(MDC_PURO(a)(b))
)


# --------------------------------------------------------------------------
# União de multiconjuntos de fatores.
# Quando um fator da primeira lista também aparece na segunda, ele entra uma
# vez e uma ocorrência é removida da segunda lista. Ao final, os fatores que
# sobraram na segunda lista entram no produto. O resultado é o MMC por fatores.
# --------------------------------------------------------------------------
def PRODUTO_UNIAO_FATORES_PURO(xs):
    def unir(ys):
        if xs is F:
            return PRODUTO_LISTA_PURO(ys)
        cabeca = xs(V)
        cauda = xs(F)
        return MAIOR(CONTA_VALOR_LISTA_PURO(cabeca)(ys))(ZERO)(
            lambda _: MULT(cabeca)(PRODUTO_UNIAO_FATORES_PURO(cauda)(REMOVER_UMA_OCORRENCIA_PURO(cabeca)(ys)))
        )(
            lambda _: MULT(cabeca)(PRODUTO_UNIAO_FATORES_PURO(cauda)(ys))
        )(V)
    return unir


MMC_POR_FATORES_PURO = lambda a: lambda b: PRODUTO_UNIAO_FATORES_PURO(
    FATORACAO_PURA(a)
)(FATORACAO_PURA(b))


# --------------------------------------------------------------------------
# Relação natural entre MDC, MMC e produto.
# Como ainda não usamos divisão como fórmula aqui, validamos pela igualdade:
#   mdc(a,b) × mmc(a,b) = a × b
# para a,b positivos.
# --------------------------------------------------------------------------
MDC_MMC_PRODUTO_CONFERE = lambda a: lambda b: IMPLICA(
    E(MAIOR(a)(ZERO))(MAIOR(b)(ZERO))
)(
    IGUAL(
        MULT(MDC_POR_FATORES_PURO(a)(b))(MMC_POR_FATORES_PURO(a)(b))
    )(
        MULT(a)(b)
    )
)
