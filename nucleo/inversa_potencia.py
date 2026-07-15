# ==============================================================================
# OPERAÇÃO UNIFICADA DA POTÊNCIA — implementação da ideia da Aula 18
# ==============================================================================
# Aula 14 -> radiciação (acha a base)
# Aula 16 -> logaritmo   (acha o expoente)
# Aula 17 -> as duas são inversas da MESMA caixa {base, expoente, potência}
# Aula 18 -> proposta: um único símbolo ⟦ ⟧ com um "?" na posição a
#            descobrir, em vez de dois símbolos (√ e log) para a mesma ideia.
#
#   ⟦a, b⟧  = c        (potenciação — dados a e b, acha c)
#   ⟦?, b⟧  = c  ->  a  (radiciação disfarçada:  a = b-ésima raiz de c)
#   ⟦a, ?⟧  = c  ->  b  (logaritmo disfarçado:   b = log_a(c))
#
# Aqui a "caixa" ⟦ ⟧ é UMA função de busca (não duas), que devolve o
# membro que falta, construída inteiramente sobre POT, IGUAL, MAIOR e Y —
# sem nenhuma dependência de math.sqrt, math.log, ou qualquer outra coisa.
# A busca é exaustiva e discreta (compatível com o resto do núcleo, que
# nunca sai dos inteiros — veja DIST_EUCL_QUAD, que por isso mesmo evita
# raiz quadrada).
# ==============================================================================
from .primitivas import V, F, ZERO, S, Y
from .aritmetica import IGUAL, MAIOR, POT, _UM

# --------------------------------------------------------------------------
# Busca a BASE que falta: acha `a` tal que a^b = c   (a "raiz" da Aula 14)
# Percorre a = 0, 1, 2, ... até achar, ou até ultrapassar c (não existe
# raiz exata nesse caso — devolve o candidato onde a busca parou).
# --------------------------------------------------------------------------
_BUSCA_BASE = Y(lambda busca: lambda cand: lambda b: lambda c:
    IGUAL(POT(cand)(b))(c)(
        lambda _: cand
    )(
        lambda _: MAIOR(cand)(c)(
            lambda _: cand
        )(
            lambda _: busca(S(cand))(b)(c)
        )(V)
    )(V)
)
INV_BASE = lambda b: lambda c: _BUSCA_BASE(ZERO)(b)(c)

# --------------------------------------------------------------------------
# Busca o EXPOENTE que falta: acha `b` tal que a^b = c  (o "log" da Aula 16)
# --------------------------------------------------------------------------
_BUSCA_EXPO = Y(lambda busca: lambda cand: lambda a: lambda c:
    IGUAL(POT(a)(cand))(c)(
        lambda _: cand
    )(
        lambda _: MAIOR(cand)(c)(
            lambda _: cand
        )(
            lambda _: busca(S(cand))(a)(c)
        )(V)
    )(V)
)
INV_EXPO = lambda a: lambda c: _BUSCA_EXPO(ZERO)(a)(c)

# --------------------------------------------------------------------------
# EXISTE_RAIZ_EXATA / EXISTE_LOG_EXATO — verificam se a busca acima
# encontrou de fato uma solução exata (em vez de ter parado por
# ultrapassar o limite).
# --------------------------------------------------------------------------
EXISTE_RAIZ_EXATA = lambda b: lambda c: IGUAL(POT(INV_BASE(b)(c))(b))(c)
EXISTE_LOG_EXATO = lambda a: lambda c: IGUAL(POT(a)(INV_EXPO(a)(c)))(c)
