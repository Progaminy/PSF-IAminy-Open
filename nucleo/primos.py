# ==============================================================================
# NÚMEROS PRIMOS — construídos inteiramente sobre a aritmética derivada
# ==============================================================================
from .primitivas import V, F, ZERO, S, PAR, Y
from .aritmetica import IS_ZERO, MOD, SUB, MAIOR, DIV, IGUAL, _UM
from .combinadores import INTERVALO

_DOIS = S(_UM)

# --------------------------------------------------------------------------
# LEMA 3.1: DIVISIBILIDADE — d divide n  <=>  n mod d == 0
# --------------------------------------------------------------------------
DIVIDE = lambda d: lambda n: IS_ZERO(MOD(n)(d))

# --------------------------------------------------------------------------
# LEMA 3.3: CONTADOR DE DIVISORES em [2, n-1]
# --------------------------------------------------------------------------
CONTAR_DIVISORES = lambda n: INTERVALO(_DOIS)(SUB(n)(_UM))(
    lambda d: lambda acum: DIVIDE(d)(n)(
        lambda _: S(acum)
    )(
        lambda _: acum
    )(V)
)(ZERO)

# --------------------------------------------------------------------------
# LEMA 3.4: TESTE DE PRIMALIDADE — n > 1 e n tem 0 divisores em [2, n-1]
# --------------------------------------------------------------------------
EH_PRIMO = lambda n: MAIOR(n)(_UM)(
    lambda _: IS_ZERO(CONTAR_DIVISORES(n))
)(
    lambda _: F
)(V)

# --------------------------------------------------------------------------
# LEMA 3.5: CRIVO — lista (cons/nil) dos primos em [2, limite]
# cons(cabeça, cauda) = PAR(cabeça)(cauda); lista vazia = F
# --------------------------------------------------------------------------
CRIVO = lambda limite: INTERVALO(_DOIS)(limite)(
    lambda n: lambda acum: EH_PRIMO(n)(
        lambda _: PAR(n)(acum)
    )(
        lambda _: acum
    )(V)
)(F)

# --------------------------------------------------------------------------
# LEMA 3.6: N-ÉSIMO NÚMERO PRIMO — busca sequencial via Y
# --------------------------------------------------------------------------
_ENESIMO_PRIMO = Y(lambda busca: lambda n: lambda cand:
    EH_PRIMO(cand)(
        lambda _: IS_ZERO(SUB(n)(_UM))(
            lambda _: cand
        )(
            lambda _: busca(SUB(n)(_UM))(S(cand))
        )(V)
    )(
        lambda _: busca(n)(S(cand))
    )(V)
)
PRIMO_N = lambda n: _ENESIMO_PRIMO(n)(_DOIS)

# --------------------------------------------------------------------------
# LEMA 3.7: DECOMPOSIÇÃO EM FATORES PRIMOS — lista (cons/nil)
# Busca o menor fator primo `d` de n, adiciona-o, e recorre sobre n/d.
# --------------------------------------------------------------------------
FATORES = Y(lambda fat: lambda n: lambda d:
    MAIOR(d)(n)(
        lambda _: F
    )(
        lambda _: E_PRIMO_E_DIVIDE(d)(n)(
            lambda _: PAR(d)(fat(DIV(n)(d))(d))
        )(
            lambda _: fat(n)(S(d))
        )(V)
    )(V)
)

# auxiliar: "d é primo E d divide n" (evita reavaliar EH_PRIMO em cada passo
# de forma confusa — mantém FATORES legível)
E_PRIMO_E_DIVIDE = lambda d: lambda n: EH_PRIMO(d)(
    lambda _: DIVIDE(d)(n)
)(
    lambda _: F
)(V)

DECOMPOR = lambda n: FATORES(n)(_DOIS)

# --------------------------------------------------------------------------
# LEMA 3.9: COPRIMOS — a, b coprimos  <=>  MDC(a, b) == 1
# --------------------------------------------------------------------------
from .aritmetica import MDC  # noqa: E402  (evita import circular no topo)

COPRIMOS = lambda a: lambda b: IGUAL(MDC(a)(b))(_UM)

# --------------------------------------------------------------------------
# LEMA 3.10: FUNÇÃO TOTIENTE DE EULER — φ(n) = |{k em [1,n] : mdc(k,n)=1}|
# --------------------------------------------------------------------------
TOTIENTE = lambda n: INTERVALO(_UM)(n)(
    lambda k: lambda acum: COPRIMOS(k)(n)(
        lambda _: S(acum)
    )(
        lambda _: acum
    )(V)
)(ZERO)
