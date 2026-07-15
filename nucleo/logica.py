# ==============================================================================
# LÓGICA BOOLEANA — Derivada exclusivamente de V, F
# ==============================================================================
from .primitivas import V, F

NAO = lambda p: p(F)(V)                       # Inverte o caminho de escolha
E = lambda p: lambda q: p(q)(F)               # Se p=V, o resultado é q; senão F
OU = lambda p: lambda q: p(V)(q)              # Se p=V, resultado é V; senão q
XOR = lambda p: lambda q: p(NAO(q))(q)        # Verdadeiro quando p != q
IMPLICA = lambda p: lambda q: OU(NAO(p))(q)   # p -> q  ==  ¬p ∨ q
SSE = lambda p: lambda q: E(IMPLICA(p)(q))(IMPLICA(q)(p))  # p <-> q

# Leis de De Morgan, como teoremas derivados (não como novas primitivas):
#   ¬(p ∧ q) <-> (¬p ∨ ¬q)
#   ¬(p ∨ q) <-> (¬p ∧ ¬q)
DE_MORGAN_1 = lambda p: lambda q: SSE(NAO(E(p)(q)))(OU(NAO(p))(NAO(q)))
DE_MORGAN_2 = lambda p: lambda q: SSE(NAO(OU(p)(q)))(E(NAO(p))(NAO(q)))
