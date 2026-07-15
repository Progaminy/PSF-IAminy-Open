# ==============================================================================
# NÚMEROS HARMÔNICOS — H(n) = 1 + 1/2 + 1/3 + ... + 1/n, como racional exato.
# Cobre da lista original: Tópico 91 (Área 1).
# ==============================================================================
# MESMA LIÇÃO de nucleo/reais.py: sem SIMPLIFICAR a cada passo, o
# denominador de H(n) cresce por multiplicação cruzada a cada termo (é
# essencialmente um mmc(1..n) não-reduzido) e ultrapassa depressa o que
# este núcleo unário processa. Com SIMPLIFICAR a cada passo, o
# denominador fica no seu tamanho verdadeiro (mmc reduzido) — ainda
# cresce, mas muito mais devagar.
# ==============================================================================
from .primitivas import V, ZERO, Y
from .aritmetica import IS_ZERO, PRED, _UM
from .racionais import RAC, SOMA_RAC, SIMPLIFICAR

_HARMONICO_REC = Y(lambda h: lambda n:
    IS_ZERO(n)(
        lambda _: RAC(ZERO)(_UM)
    )(
        lambda _: SIMPLIFICAR(SOMA_RAC(RAC(_UM)(n))(h(PRED(n))))
    )(V)
)

# --------------------------------------------------------------------------
# API — HARMONICO(n): racional exato H(n).
# ESCOPO TESTADO (não assumido): n=1..5 rápido (<0.2s); n=6,7 completam
# mas devagar (5-7s); n>=8 não verificado — provavelmente lento, mesma
# causa de sempre (SUB/MOD custam O(valor), não O(1), ver reais.py).
# --------------------------------------------------------------------------
HARMONICO = lambda n: _HARMONICO_REC(n)
