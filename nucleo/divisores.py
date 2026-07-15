# ==============================================================================
# DIVISORES — construído sobre primos.py e aritmetica.py.
# Cobre da lista original: Tópicos 8-13, 59-61, 70, 72-78 (Área 1).
# ==============================================================================
from .primitivas import V, F, ZERO, S, PAR
from .aritmetica import SOMA, SUB, MULT, IGUAL, MAIOR, _UM
from .logica import E, NAO
from .primos import DIVIDE, EH_PRIMO, _DOIS
from .combinadores import INTERVALO

# --------------------------------------------------------------------------
# Tópico 9: MÚLTIPLO — m é múltiplo de d  <=>  d divide m
# --------------------------------------------------------------------------
MULTIPLO = lambda d: lambda m: DIVIDE(d)(m)

# --------------------------------------------------------------------------
# Tópico 8: COMPOSTO — n > 1 e não é primo
# --------------------------------------------------------------------------
EH_COMPOSTO = lambda n: E(MAIOR(n)(_UM))(NAO(EH_PRIMO(n)))

# --------------------------------------------------------------------------
# Tópico 11: LISTA DE DIVISORES — cons/nil, mesma convenção de CRIVO
# --------------------------------------------------------------------------
LISTA_DIVISORES = lambda n: INTERVALO(_UM)(n)(
    lambda d: lambda acc: DIVIDE(d)(n)(
        lambda _: PAR(d)(acc)
    )(
        lambda _: acc
    )(V)
)(F)

# --------------------------------------------------------------------------
# Tópico 73: QUANTIDADE DE DIVISORES — τ(n) = |{d em [1,n] : d|n}|
# --------------------------------------------------------------------------
QTD_DIVISORES = lambda n: INTERVALO(_UM)(n)(
    lambda d: lambda acc: DIVIDE(d)(n)(lambda _: S(acc))(lambda _: acc)(V)
)(ZERO)

# --------------------------------------------------------------------------
# Tópico 74: SOMA DE DIVISORES — σ(n) = Σ{d em [1,n] : d|n}
# (inclui n; para divisores PRÓPRIOS, ver DIVISORES_PROPRIOS_SOMA abaixo)
# --------------------------------------------------------------------------
SOMA_DIVISORES = lambda n: INTERVALO(_UM)(n)(
    lambda d: lambda acc: DIVIDE(d)(n)(lambda _: SOMA(acc)(d))(lambda _: acc)(V)
)(ZERO)

# --------------------------------------------------------------------------
# Tópico 75: PRODUTO DE DIVISORES
# --------------------------------------------------------------------------
PRODUTO_DIVISORES = lambda n: INTERVALO(_UM)(n)(
    lambda d: lambda acc: DIVIDE(d)(n)(lambda _: MULT(acc)(d))(lambda _: acc)(V)
)(_UM)

# --------------------------------------------------------------------------
# soma dos divisores PRÓPRIOS (excluindo o próprio n) — base de PERFEITO e AMIGOS
# --------------------------------------------------------------------------
DIVISORES_PROPRIOS_SOMA = lambda n: SUB(SOMA_DIVISORES(n))(n)

# --------------------------------------------------------------------------
# Tópico 59: NÚMERO PERFEITO — igual à soma dos seus divisores próprios
# (ex.: 6 = 1+2+3;  28 = 1+2+4+7+14)
# --------------------------------------------------------------------------
PERFEITO = lambda n: IGUAL(DIVISORES_PROPRIOS_SOMA(n))(n)

# --------------------------------------------------------------------------
# Tópico 60: NÚMEROS AMIGOS — a e b onde a soma dos divisores próprios de
# um dá o outro (ex.: 220 e 284)
# ESCOPO TESTADO: correto matematicamente, mas o menor par conhecido
# (220, 284) NÃO completa em tempo razoável neste núcleo — SOMA_DIVISORES
# sobre números > ~150 fica lento pela mesma razão documentada em
# nucleo/reais.py (SUB/MOD custam O(n) por chamada, não O(1)). Testado:
# SOMA_DIVISORES(100) já leva ~3s; (220) não terminou em 20s.
# --------------------------------------------------------------------------
AMIGOS = lambda a: lambda b: E(
    IGUAL(DIVISORES_PROPRIOS_SOMA(a))(b)
)(
    IGUAL(DIVISORES_PROPRIOS_SOMA(b))(a)
)

# --------------------------------------------------------------------------
# Tópico 76: CONGRUÊNCIA — a ≡ b (mod n)  <=>  mesmo resto na divisão por n
# --------------------------------------------------------------------------
from .aritmetica import MOD  # noqa: E402
CONGRUENTE = lambda a: lambda b: lambda n: IGUAL(MOD(a)(n))(MOD(b)(n))

# --------------------------------------------------------------------------
# Tópicos 81/82: MERSENNE (2^p - 1) e FERMAT (2^(2^n) + 1)
# --------------------------------------------------------------------------
from .aritmetica import POT  # noqa: E402
MERSENNE = lambda p: SUB(POT(_DOIS)(p))(_UM)
EH_MERSENNE_PRIMO = lambda p: EH_PRIMO(MERSENNE(p))
FERMAT = lambda n: SOMA(POT(_DOIS)(POT(_DOIS)(n)))(_UM)

# --------------------------------------------------------------------------
# Tópicos 79/80: TERNA PITAGÓRICA — a² + b² = c²  (ex.: 3,4,5)
# Verificador, não busca (buscar ternas por força bruta custaria O(limite³)
# — fora do que este núcleo processa depressa, ver nucleo/reais.py).
# --------------------------------------------------------------------------
EH_TERNA_PITAGORICA = lambda a: lambda b: lambda c: IGUAL(
    SOMA(POT(a)(_DOIS))(POT(b)(_DOIS))
)(
    POT(c)(_DOIS)
)
