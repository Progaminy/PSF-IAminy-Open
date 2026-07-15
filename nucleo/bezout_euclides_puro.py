# ==============================================================================
# BÉZOUT E EUCLIDES ESTENDIDO — construção pura após divisão euclidiana.
# ==============================================================================
# Lei PSF-IAminy:
#   O lema de Euclides não será fingido nem fechado por circularidade.
#   Antes dele, precisamos de coeficientes inteiros e combinação linear.
#
# Esta etapa constrói:
#   - inteiro relativo puro como par (positivo, negativo), representando p-n;
#   - operações inteiras por pares, sem sinal nativo do Python;
#   - combinação linear ax + by;
#   - Euclides estendido por quociente/resto já construídos;
#   - identidade de Bézout como validação operacional.
#
# Dependências proibidas aqui:
#   operador nativo /, //, %, congruência, aritmética modular, primos.py,
#   aritmética.DIV, aritmética.MOD, aritmética.MDC, aritmética.MMC.
# ==============================================================================
from .primitivas import V, F, ZERO, S, PAR, Y
from .logica import E, OU, IMPLICA
from .aritmetica import IS_ZERO, IGUAL, SOMA, MULT, _UM
from .divisibilidade_pura import DIVIDE_PURO
from .mdc_puro import MDC_DEFINIDO_PURO, COPRIMOS_PURO
from .euclides_resto_puro import MDC_RESTO_PURO
from .divisao_euclidiana_pura import QUOCIENTE_PURO, RESTO_PURO
from .primalidade_pura import PRIMO_PURO


# --------------------------------------------------------------------------
# Inteiro relativo puro
# --------------------------------------------------------------------------
# Um inteiro z é um par:
#   z = (parte_positiva, parte_negativa)
# e representa:
#   parte_positiva - parte_negativa
#
# Isto evita usar negativos nativos do Python dentro do núcleo.
# --------------------------------------------------------------------------
INTEIRO_PURO = lambda positivo: lambda negativo: PAR(positivo)(negativo)
PARTE_POSITIVA_PURA = lambda z: z(V)
PARTE_NEGATIVA_PURA = lambda z: z(F)

ZERO_INTEIRO_PURO = INTEIRO_PURO(ZERO)(ZERO)
UM_INTEIRO_PURO = INTEIRO_PURO(_UM)(ZERO)

NATURAL_COMO_INTEIRO_PURO = lambda n: INTEIRO_PURO(n)(ZERO)


# Igualdade de inteiros por equivalência cruzada:
#   p1 - n1 = p2 - n2
# equivale a:
#   p1 + n2 = p2 + n1
IGUAL_INTEIRO_PURO = lambda z1: lambda z2: IGUAL(
    SOMA(PARTE_POSITIVA_PURA(z1))(PARTE_NEGATIVA_PURA(z2))
)(
    SOMA(PARTE_POSITIVA_PURA(z2))(PARTE_NEGATIVA_PURA(z1))
)

OPOSTO_INTEIRO_PURO = lambda z: INTEIRO_PURO(PARTE_NEGATIVA_PURA(z))(PARTE_POSITIVA_PURA(z))

SOMA_INTEIRO_PURO = lambda z1: lambda z2: INTEIRO_PURO(
    SOMA(PARTE_POSITIVA_PURA(z1))(PARTE_POSITIVA_PURA(z2))
)(
    SOMA(PARTE_NEGATIVA_PURA(z1))(PARTE_NEGATIVA_PURA(z2))
)

SUB_INTEIRO_PURO = lambda z1: lambda z2: SOMA_INTEIRO_PURO(z1)(OPOSTO_INTEIRO_PURO(z2))

MULT_INTEIRO_PURO = lambda z1: lambda z2: INTEIRO_PURO(
    SOMA(
        MULT(PARTE_POSITIVA_PURA(z1))(PARTE_POSITIVA_PURA(z2))
    )(
        MULT(PARTE_NEGATIVA_PURA(z1))(PARTE_NEGATIVA_PURA(z2))
    )
)(
    SOMA(
        MULT(PARTE_POSITIVA_PURA(z1))(PARTE_NEGATIVA_PURA(z2))
    )(
        MULT(PARTE_NEGATIVA_PURA(z1))(PARTE_POSITIVA_PURA(z2))
    )
)

# Multiplicação de inteiro por natural:
#   (p-n) * a = (p*a) - (n*a)
MULT_INTEIRO_NATURAL_PURO = lambda z: lambda a: INTEIRO_PURO(
    MULT(PARTE_POSITIVA_PURA(z))(a)
)(
    MULT(PARTE_NEGATIVA_PURA(z))(a)
)


# --------------------------------------------------------------------------
# Combinação linear
# --------------------------------------------------------------------------
# A expressão ax + by exige inteiros x,y e naturais a,b.
# O resultado é inteiro puro.
# --------------------------------------------------------------------------
COMBINACAO_LINEAR_PURA = lambda a: lambda b: lambda x: lambda y: SOMA_INTEIRO_PURO(
    MULT_INTEIRO_NATURAL_PURO(x)(a)
)(
    MULT_INTEIRO_NATURAL_PURO(y)(b)
)


# --------------------------------------------------------------------------
# Resultado do Euclides estendido
# --------------------------------------------------------------------------
# Guardamos um triplo como:
#   PAR(g)(PAR(x)(y))
# onde:
#   g = mdc(a,b)
#   x,y = coeficientes inteiros tais que ax + by = g
# --------------------------------------------------------------------------
RESULTADO_BEZOUT_PURO = lambda g: lambda x: lambda y: PAR(g)(PAR(x)(y))
BEZOUT_G_PURO = lambda r: r(V)
BEZOUT_X_PURO = lambda r: r(F)(V)
BEZOUT_Y_PURO = lambda r: r(F)(F)


# --------------------------------------------------------------------------
# Euclides estendido puro
# --------------------------------------------------------------------------
# Se b=0:
#   mdc(a,0)=a e a*1 + 0*0 = a
# Se b>0:
#   primeiro resolve (b, resto(a,b)); depois recompõe:
#   r = a - q*b
#   g = b*x1 + r*y1
#   g = b*x1 + (a - q*b)*y1
#   g = a*y1 + b*(x1 - q*y1)
# Logo:
#   x = y1
#   y = x1 - q*y1
# --------------------------------------------------------------------------
EUCLIDES_ESTENDIDO_PURO = Y(lambda ext: lambda a: lambda b:
    IS_ZERO(b)(
        lambda _: RESULTADO_BEZOUT_PURO(a)(UM_INTEIRO_PURO)(ZERO_INTEIRO_PURO)
    )(
        lambda _: (lambda r: (lambda anterior: (lambda q:
            RESULTADO_BEZOUT_PURO(
                BEZOUT_G_PURO(anterior)
            )(
                BEZOUT_Y_PURO(anterior)
            )(
                SUB_INTEIRO_PURO(
                    BEZOUT_X_PURO(anterior)
                )(
                    MULT_INTEIRO_NATURAL_PURO(BEZOUT_Y_PURO(anterior))(q)
                )
            )
        )(QUOCIENTE_PURO(a)(b)))(ext(b)(r)))(RESTO_PURO(a)(b))
    )(V)
)


MDC_ESTENDIDO_PURO = lambda a: lambda b: BEZOUT_G_PURO(EUCLIDES_ESTENDIDO_PURO(a)(b))
COEFICIENTE_X_BEZOUT_PURO = lambda a: lambda b: BEZOUT_X_PURO(EUCLIDES_ESTENDIDO_PURO(a)(b))
COEFICIENTE_Y_BEZOUT_PURO = lambda a: lambda b: BEZOUT_Y_PURO(EUCLIDES_ESTENDIDO_PURO(a)(b))


# Validação da identidade:
#   ax + by = mdc(a,b)
# Para (0,0), o MDC conceitual é indefinido; por isso a validação é condicional.
BEZOUT_CONFERE_PURO = lambda a: lambda b: IMPLICA(
    MDC_DEFINIDO_PURO(a)(b)
)(
    IGUAL_INTEIRO_PURO(
        COMBINACAO_LINEAR_PURA(a)(b)(COEFICIENTE_X_BEZOUT_PURO(a)(b))(COEFICIENTE_Y_BEZOUT_PURO(a)(b))
    )(
        NATURAL_COMO_INTEIRO_PURO(MDC_RESTO_PURO(a)(b))
    )
)


MDC_ESTENDIDO_CONFERE_PURO = lambda a: lambda b: IMPLICA(
    MDC_DEFINIDO_PURO(a)(b)
)(
    IGUAL(MDC_ESTENDIDO_PURO(a)(b))(MDC_RESTO_PURO(a)(b))
)


# Coprimalidade revisitada:
# Se mdc(a,b)=1, então a combinação linear encontrada vale 1.
COPRIMOS_BEZOUT_CONFERE_PURO = lambda a: lambda b: IMPLICA(
    COPRIMOS_PURO(a)(b)
)(
    IGUAL_INTEIRO_PURO(
        COMBINACAO_LINEAR_PURA(a)(b)(COEFICIENTE_X_BEZOUT_PURO(a)(b))(COEFICIENTE_Y_BEZOUT_PURO(a)(b))
    )(
        UM_INTEIRO_PURO
    )
)


# --------------------------------------------------------------------------
# Lema de Euclides — forma verificável
# --------------------------------------------------------------------------
# Se p é primo e p divide a*b, então p divide a ou p divide b.
# A prova conceitual usa Bézout e fica registrada em conhecimento/.
# Aqui mantemos um verificador direto da proposição.
# --------------------------------------------------------------------------
LEMA_EUCLIDES_PURO = lambda p: lambda a: lambda b: IMPLICA(
    E(PRIMO_PURO(p))(DIVIDE_PURO(p)(MULT(a)(b)))
)(
    OU(DIVIDE_PURO(p)(a))(DIVIDE_PURO(p)(b))
)
