# ==============================================================================
# NÚMEROS FIGURADOS — construídos como fórmulas fechadas, todas seguras
# contra a SUB truncada: nenhuma subtração aqui produz negativo p/ n>=1.
# Cobre da lista original: Tópicos 61-64 (Área 1).
# ==============================================================================
from .primitivas import S
from .aritmetica import SOMA, SUB, MULT, DIV, _UM

_DOIS = S(_UM)
_TRES = S(_DOIS)

# --------------------------------------------------------------------------
# Tópico 61: TRIANGULAR — T(n) = n(n+1)/2  (1, 3, 6, 10, 15, ...)
# --------------------------------------------------------------------------
TRIANGULAR = lambda n: DIV(MULT(n)(SOMA(n)(_UM)))(_DOIS)

# --------------------------------------------------------------------------
# Tópico 62: QUADRADO (figurado) — Q(n) = n²  (1, 4, 9, 16, ...)
# --------------------------------------------------------------------------
QUADRADO_FIGURADO = lambda n: MULT(n)(n)

# --------------------------------------------------------------------------
# Tópico 63: PENTAGONAL — P(n) = n(3n-1)/2  (1, 5, 12, 22, ...)
# 3n-1 é sempre >= 2 para n>=1, então a SUB truncada nunca mente aqui.
# --------------------------------------------------------------------------
PENTAGONAL = lambda n: DIV(MULT(n)(SUB(MULT(_TRES)(n))(_UM)))(_DOIS)

# --------------------------------------------------------------------------
# HEXAGONAL — H(n) = n(2n-1)  (1, 6, 15, 28, ...) — bónus, mesmo padrão
# ("Números poligonais", Tópico 88, é exatamente esta família generalizada)
# --------------------------------------------------------------------------
HEXAGONAL = lambda n: MULT(n)(SUB(MULT(_DOIS)(n))(_UM))
