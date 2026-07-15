# ==============================================================================
# LÓGICA DE PREDICADOS — quantificadores ∀ e ∃, LIMITADOS a um intervalo.
# ==============================================================================
# Honestidade sobre o escopo: ∀x P(x) e ∃x P(x) "de verdade" quantificam
# sobre um domínio infinito, e isso não é decidível por busca exaustiva.
# Aqui, como em EH_PRIMO/CRIVO, quantificamos sobre [0, limite] — um
# ∀/∃ *limitado*, mas honesto: nunca finge verificar o infinito, só o
# intervalo dado. Construído apenas com V, F e a lógica E/OU já
# derivadas, sobre o combinador partilhado INTERVALO — nenhuma
# dependência nova.
from .primitivas import V, F, ZERO
from .logica import E, OU

from .combinadores import INTERVALO

# --------------------------------------------------------------------------
# PARA_TODO(limite)(P) — verdadeiro sse P(k) vale para todo k em [0, limite]
# --------------------------------------------------------------------------
PARA_TODO = lambda limite: lambda P: INTERVALO(ZERO)(limite)(
    lambda k: lambda acc: E(acc)(P(k))
)(V)

# --------------------------------------------------------------------------
# EXISTE(limite)(P) — verdadeiro sse P(k) vale para AO MENOS UM k em [0,limite]
# --------------------------------------------------------------------------
EXISTE = lambda limite: lambda P: INTERVALO(ZERO)(limite)(
    lambda k: lambda acc: OU(acc)(P(k))
)(F)
