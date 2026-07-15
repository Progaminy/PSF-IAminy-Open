# ==============================================================================
# COMBINADORES PARTILHADOS — construídos só sobre as 5 primitivas.
# ==============================================================================
# INTERVALO já era usado por primos.py (crivo, totiente, etc). Vive aqui
# porque não é específico de primos: é o "fold sobre [k, limite]" que vai
# sustentar também quantificadores (∀, ∃) e cálculo discreto (Σ, Π).
from .primitivas import V, S, Y
from .aritmetica import MAIOR

INTERVALO = Y(lambda intv: lambda k: lambda limite: lambda passo: lambda inic:
    MAIOR(k)(limite)(
        lambda _: inic
    )(
        lambda _: intv(S(k))(limite)(passo)(passo(k)(inic))
    )(V)
)
