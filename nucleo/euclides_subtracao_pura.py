# ==============================================================================
# EUCLIDES POR SUBTRAÇÃO — construído SEM divisão, SEM resto, SEM módulo.
# ==============================================================================
# Ideia:
#   Se a > b, os divisores comuns de (a,b) são os mesmos de (a-b,b).
#   Se b > a, os divisores comuns de (a,b) são os mesmos de (a,b-a).
#   Repetindo diferenças controladas, chegamos ao mesmo número nos dois lados:
#       MDC(a,a)=a
#
# Isto ainda NÃO é o algoritmo eficiente com resto. É o ancestral conceitual.
# ==============================================================================
from .primitivas import V, ZERO, Y
from .logica import E, NAO
from .aritmetica import IS_ZERO, IGUAL, MAIOR, SUB
from .mdc_puro import MDC_DEFINIDO_PURO, MDC_PURO


# O algoritmo só tem significado matemático quando (a,b)!=(0,0).
MDC_SUBTRACAO_DEFINIDO = MDC_DEFINIDO_PURO


MDC_SUBTRACAO_PURO = Y(lambda mdc: lambda a: lambda b:
    IS_ZERO(a)(
        lambda _: b
    )(
        lambda _: IS_ZERO(b)(
            lambda _: a
        )(
            lambda _: IGUAL(a)(b)(
                lambda _: a
            )(
                lambda _: MAIOR(a)(b)(
                    lambda _: mdc(SUB(a)(b))(b)
                )(
                    lambda _: mdc(a)(SUB(b)(a))
                )(V)
            )(V)
        )(V)
    )(V)
)


# Validação interna: o resultado do processo por subtração deve coincidir
# com o MDC por definição de maior divisor comum.
MDC_SUBTRACAO_CONFERE_COM_DEFINICAO = lambda a: lambda b: E(
    MDC_SUBTRACAO_DEFINIDO(a)(b)
)(
    IGUAL(MDC_SUBTRACAO_PURO(a)(b))(MDC_PURO(a)(b))
)
