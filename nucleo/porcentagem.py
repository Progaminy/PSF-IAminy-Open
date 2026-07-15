# ==============================================================================
# PORCENTAGEM — casos particulares de racionais com denominador 100.
# Cobre da lista original: Tópico 34 (Área 1).
# ==============================================================================
from .primitivas import S
from .aritmetica import SOMA, SUB, MULT, _UM
from .racionais import RAC, MULT_RAC

_DOIS = S(_UM)
_DEZ = SOMA(_DOIS)(SOMA(_DOIS)(SOMA(_DOIS)(SOMA(_DOIS)(_DOIS))))
_CEM = MULT(_DEZ)(_DEZ)

# --------------------------------------------------------------------------
# p% de n, como racional exato (ex.: PORCENTAGEM_DE(25)(80) = 25*80/100 = 2000/100)
# --------------------------------------------------------------------------
PORCENTAGEM_DE = lambda p: lambda n: RAC(MULT(p)(n))(_CEM)

# --------------------------------------------------------------------------
# Aumentar n em p% — n*(100+p)/100
# --------------------------------------------------------------------------
AUMENTAR_PERCENTUAL = lambda n: lambda p: RAC(MULT(n)(SOMA(_CEM)(p)))(_CEM)

# --------------------------------------------------------------------------
# Diminuir n em p% — n*(100-p)/100.
# ATENÇÃO: usa SUB truncada — para p > 100 (diminuir mais que 100%) o
# resultado trunca em 0/100 em vez de ficar negativo. Correto para o uso
# comum (p em [0,100]); fora disso, precisaria de racionais assinados.
# --------------------------------------------------------------------------
DIMINUIR_PERCENTUAL = lambda n: lambda p: RAC(MULT(n)(SUB(_CEM)(p)))(_CEM)
