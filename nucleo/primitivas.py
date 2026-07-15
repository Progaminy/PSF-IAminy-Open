# ==============================================================================
# PSF-IAMINY — NÚCLEO: AS 5 PRIMITIVAS FUNDACIONAIS
# ==============================================================================
# Tudo neste sistema — lógica, aritmética, primos, racionais, geometria e a
# operação unificada de potência (Aula 18) — é construído exclusivamente a
# partir destas 5 primitivas. Nenhuma outra função embutida do Python
# (soma, comparação, listas, etc.) é usada no núcleo formal. A única camada
# que "sabe" que existe um Python por baixo é `traducao.py`.
#
#   V, F        -> seleção binária (booleano de Church)
#   0, S        -> aplicação sucessiva (numeral de Church / Peano)
#   PAR         -> pareamento ordenado
#   ITER        -> iteração estrutural (recursão primitiva)
#   Y           -> combinador de ponto fixo (recursão geral)
# ==============================================================================

# --------------------------------------------------------------------------
# PRIMITIVA 0: Seleção Binária
# --------------------------------------------------------------------------
# Não representa "dados": representa um CAMINHO de execução.
V = lambda t: lambda f: t   # Verdade: escolhe o primeiro argumento
F = lambda t: lambda f: f   # Falso:   escolhe o segundo argumento

# --------------------------------------------------------------------------
# PRIMITIVA 1: Aplicação Sucessiva (numeral de Church)
# --------------------------------------------------------------------------
# Um número n é a CAPACIDADE de aplicar uma função f, n vezes, a x.
ZERO = lambda f: lambda x: x
S = lambda n: lambda f: lambda x: f(n(f)(x))

# --------------------------------------------------------------------------
# PRIMITIVA 2: Pareamento Ordenado
# --------------------------------------------------------------------------
# Retém duas expressões e as entrega a um seletor (V ou F).
PAR = lambda a: lambda b: lambda s: s(a)(b)

# --------------------------------------------------------------------------
# PRIMITIVA 3: Iteração Estrutural (Recursão Primitiva)
# --------------------------------------------------------------------------
# ITER(n)(inicial)(passo) aplica `passo` a `inicial`, n vezes.
# Isto é exatamente o que um numeral de Church já faz — ITER só existe
# como nome próprio para deixar explícita a intenção de "iterar".
ITER = lambda n: lambda inicial: lambda passo: n(passo)(inicial)

# --------------------------------------------------------------------------
# PRIMITIVA 4: Combinador de Ponto Fixo (recursão geral / Y de Curry,
# em versão "Z" para avaliação estrita — necessária em Python).
# --------------------------------------------------------------------------
# Permite que uma função anônima (lambda) chame a si mesma, sem precisar
# de um nome. É o que torna possível DIV, MOD, MDC, busca de primos, etc.
Y = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))
