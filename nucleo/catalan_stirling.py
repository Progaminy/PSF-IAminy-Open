# ==============================================================================
# CATALAN E STIRLING — extensão pequena da Área 1/Combinatória.
# ==============================================================================
# Este módulo é núcleo puro: usa apenas funções já derivadas em nucleo/.
# Escopo honesto: rápido para n pequeno (até ~5/6), porque herda o custo de
# FATORIAL/DIV/recursão em numerais de Church.
# ==============================================================================
from .primitivas import V, ZERO, S, Y
from .aritmetica import IS_ZERO, IGUAL, SOMA, SUB, MULT, DIV, PRED, _UM
from .combinatoria import COMBINACAO_SIMPLES

# --------------------------------------------------------------------------
# Tópico 88: NÚMERO DE CATALAN
# C_n = C(2n,n)/(n+1)
# --------------------------------------------------------------------------
CATALAN = lambda n: DIV(
    COMBINACAO_SIMPLES(SOMA(n)(n))(n)
)(
    S(n)
)

# --------------------------------------------------------------------------
# Tópico 90: NÚMERO DE STIRLING DE SEGUNDA ESPÉCIE
# S(0,0)=1; S(n,0)=0 para n>0; S(n,n)=1;
# S(n,k)=k*S(n-1,k)+S(n-1,k-1)
# --------------------------------------------------------------------------
STIRLING2 = Y(lambda st: lambda n: lambda k:
    IS_ZERO(n)(
        lambda _: IS_ZERO(k)(lambda __: _UM)(lambda __: ZERO)(V)
    )(
        lambda _: IS_ZERO(k)(
            lambda __: ZERO
        )(
            lambda __: IGUAL(n)(k)(
                lambda ___: _UM
            )(
                lambda ___: SOMA(
                    MULT(k)(st(PRED(n))(k))
                )(
                    st(PRED(n))(PRED(k))
                )
            )(V)
        )(V)
    )(V)
)
