# ==============================================================================
# EUCLIDES POR RESTO — nasce depois da divisão euclidiana.
# ==============================================================================
# Lei PSF-IAminy:
#   só agora o algoritmo por resto pode existir, porque quociente e resto já
#   foram construídos por subtrações repetidas.
#
# Esta camada NÃO importa DIV, NÃO importa MOD e NÃO usa operadores nativos.
# ==============================================================================
from .primitivas import V, Y
from .logica import E
from .aritmetica import IS_ZERO, IGUAL
from .mdc_puro import MDC_DEFINIDO_PURO, MDC_PURO
from .euclides_subtracao_pura import MDC_SUBTRACAO_PURO
from .divisao_euclidiana_pura import RESTO_PURO


MDC_RESTO_DEFINIDO = MDC_DEFINIDO_PURO


# Algoritmo:
#   mdc(a,0)=a
#   mdc(a,b)=mdc(b, resto(a,b))
#
# A palavra resto aqui já é legítima, pois RESTO_PURO foi construído antes.
MDC_RESTO_PURO = Y(lambda mdc: lambda a: lambda b:
    IS_ZERO(b)(
        lambda _: a
    )(
        lambda _: mdc(b)(RESTO_PURO(a)(b))
    )(V)
)


# Validação contra o ancestral por subtração.
# O algoritmo por resto é uma compressão do algoritmo por subtração.
MDC_RESTO_CONFERE_COM_SUBTRACAO = lambda a: lambda b: E(
    MDC_RESTO_DEFINIDO(a)(b)
)(
    IGUAL(MDC_RESTO_PURO(a)(b))(MDC_SUBTRACAO_PURO(a)(b))
)


# Validação contra a definição pura de maior divisor comum.
MDC_RESTO_CONFERE_COM_DEFINICAO = lambda a: lambda b: E(
    MDC_RESTO_DEFINIDO(a)(b)
)(
    IGUAL(MDC_RESTO_PURO(a)(b))(MDC_PURO(a)(b))
)
