# ==============================================================================
# DIVISÃO EUCLIDIANA PURA — construída por subtrações repetidas.
# ==============================================================================
# Lei PSF-IAminy:
#   antes de existir operador eficiente, a divisão nasce como contagem de
#   quantas vezes um número positivo cabe dentro de outro por retirada sucessiva.
#
# Esta camada NÃO importa DIV, NÃO importa MOD e NÃO usa operadores nativos.
# A definição depende apenas de:
#   ZERO, S, PAR, Y, ordem, soma, multiplicação, subtração controlada.
# ==============================================================================
from .primitivas import V, F, ZERO, S, PAR, Y
from .logica import E, NAO, IMPLICA
from .aritmetica import IS_ZERO, MENOR, IGUAL, SOMA, MULT, SUB


# A divisão euclidiana em naturais só está definida quando o divisor não é zero.
DIVISAO_EUCLIDIANA_DEFINIDA = lambda a: lambda b: NAO(IS_ZERO(b))


# Processo interno:
#   se a < b: quociente é 0 e resto é a;
#   senão: resolve a-b, depois acrescenta 1 ao quociente.
#
# O resultado é um PAR(q)(r), onde:
#   q = quociente
#   r = resto
_DIVISAO_REPETIDA = Y(lambda div: lambda a: lambda b:
    MENOR(a)(b)(
        lambda _: PAR(ZERO)(a)
    )(
        lambda _: (lambda p: PAR(S(p(V)))(p(F)))(div(SUB(a)(b))(b))
    )(V)
)


# Para divisor zero, devolvemos PAR(0)(a) apenas como sentinela operacional.
# A validade deve ser consultada por DIVISAO_EUCLIDIANA_DEFINIDA(a)(b).
DIVISAO_EUCLIDIANA_PURA = lambda a: lambda b: DIVISAO_EUCLIDIANA_DEFINIDA(a)(b)(
    lambda _: _DIVISAO_REPETIDA(a)(b)
)(
    lambda _: PAR(ZERO)(a)
)(V)


# Quociente e resto são projeções do par da divisão euclidiana.
QUOCIENTE_PURO = lambda a: lambda b: DIVISAO_EUCLIDIANA_PURA(a)(b)(V)
RESTO_PURO = lambda a: lambda b: DIVISAO_EUCLIDIANA_PURA(a)(b)(F)


# Validação estrutural:
#   se b != 0, então a = b*q + r e r < b.
# Não é uma definição nova; é a propriedade que confirma que o par produzido
# tem sentido matemático.
DIVISAO_EUCLIDIANA_CONFERE = lambda a: lambda b: IMPLICA(
    DIVISAO_EUCLIDIANA_DEFINIDA(a)(b)
)(
    E(
        IGUAL(
            SOMA(MULT(b)(QUOCIENTE_PURO(a)(b)))(RESTO_PURO(a)(b))
        )(a)
    )(
        MENOR(RESTO_PURO(a)(b))(b)
    )
)
