# ==============================================================================
# ANÁLISE COMBINATÓRIA — construída sobre FATORIAL (calculo_discreto.py) e
# POT (aritmetica.py). Cobre da lista original: Tópicos 582-589 (Área 8).
# ==============================================================================
# ESCOPO HONESTO: como tudo o que usa DIV/FATORIAL sobre valores que
# crescem depressa, isto herda o mesmo teto de sempre — FATORIAL(n) já
# fica lento por volta de n~8-9 (8! = 40320, ~0.3s; 9! = 362880 ESTOURA
# a pilha — testado, não assumido). Seguro e rápido até n~7-8.
# ==============================================================================
from .aritmetica import MULT, SOMA, SUB, DIV, POT, _UM
from .calculo_discreto import FATORIAL

# --------------------------------------------------------------------------
# Tópico 582: PRINCÍPIO FUNDAMENTAL DA CONTAGEM — se há `a` formas de
# fazer uma coisa e `b` formas de fazer outra, há a×b formas de fazer as
# duas. É literalmente MULT — nome próprio para deixar o tópico explícito.
# --------------------------------------------------------------------------
PRINCIPIO_FUNDAMENTAL_CONTAGEM_2 = lambda a: lambda b: MULT(a)(b)
PRINCIPIO_FUNDAMENTAL_CONTAGEM_3 = lambda a: lambda b: lambda c: MULT(MULT(a)(b))(c)

# --------------------------------------------------------------------------
# Tópico 583: PERMUTAÇÃO SIMPLES — P(n) = n!  (todas as ordens de n itens)
# --------------------------------------------------------------------------
PERMUTACAO_SIMPLES = FATORIAL

# --------------------------------------------------------------------------
# Tópico 584: PERMUTAÇÃO COM REPETIÇÃO (2 grupos) — P(n; n1,n2) = n!/(n1!·n2!)
# (ex.: anagramas de "ARARA": n=5, repetições de A e R)
# --------------------------------------------------------------------------
PERMUTACAO_REPETICAO_2 = lambda n: lambda n1: lambda n2: DIV(
    FATORIAL(n)
)(
    MULT(FATORIAL(n1))(FATORIAL(n2))
)

# --------------------------------------------------------------------------
# Tópico 585: PERMUTAÇÃO CIRCULAR — PC(n) = (n-1)!
# (rotações contam como a mesma disposição)
# --------------------------------------------------------------------------
PERMUTACAO_CIRCULAR = lambda n: FATORIAL(SUB(n)(_UM))

# --------------------------------------------------------------------------
# Tópico 586: ARRANJO SIMPLES — A(n,r) = n!/(n-r)!  (escolhe r de n, ORDEM importa)
# --------------------------------------------------------------------------
ARRANJO_SIMPLES = lambda n: lambda r: DIV(FATORIAL(n))(FATORIAL(SUB(n)(r)))

# --------------------------------------------------------------------------
# Tópico 587: ARRANJO COM REPETIÇÃO — AR(n,r) = n^r
# (r posições, cada uma podendo repetir qualquer uma das n opções)
# --------------------------------------------------------------------------
ARRANJO_REPETICAO = lambda n: lambda r: POT(n)(r)

# --------------------------------------------------------------------------
# Tópico 588: COMBINAÇÃO SIMPLES — C(n,r) = n!/(r!·(n-r)!)  (ORDEM não importa)
# --------------------------------------------------------------------------
COMBINACAO_SIMPLES = lambda n: lambda r: DIV(ARRANJO_SIMPLES(n)(r))(FATORIAL(r))

# --------------------------------------------------------------------------
# Tópico 589: COMBINAÇÃO COM REPETIÇÃO — CR(n,r) = C(n+r-1, r)
# (fórmula de "estrelas e barras")
# --------------------------------------------------------------------------
COMBINACAO_REPETICAO = lambda n: lambda r: COMBINACAO_SIMPLES(SUB(SOMA(n)(r))(_UM))(r)
