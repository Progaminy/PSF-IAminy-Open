# ==============================================================================
# CÁLCULO DISCRETO — Σ, Π, indução, sequências recursivas.
# ==============================================================================
# Onde este núcleo PARA, honestamente: limite, derivada e integral "de
# verdade" (Tópicos 671-760 da tua lista original) precisam de números
# reais/irracionais — uma noção de "tão perto quanto se queira" que
# numerais de Peano/Church, por construção, não representam (são sempre
# um número finito de aplicações de S). Sem uma camada de reais (fora do
# escopo desta v1 — ver README), LIMITE/DERIVADA/INTEGRAL não podem ser
# construídos de forma honesta aqui.
#
# O que ESTE módulo constrói são as ferramentas discretas que sustentam
# esse andar de cima quando ele existir: somatório e produtório (que
# viram integral/soma de Riemann quando o passo -> 0), fatorial,
# sequências definidas por recorrência (que são a base de indução), e
# um VERIFICADOR de indução limitado (não um provador — ver nota abaixo).
from .primitivas import V, F, ZERO, S, Y
from .aritmetica import SOMA, MULT, _UM
from .logica import E
from .combinadores import INTERVALO

# --------------------------------------------------------------------------
# SOMATÓRIO — Σ_{i=a}^{b} f(i)
# --------------------------------------------------------------------------
SOMATORIO = lambda f: lambda a: lambda b: INTERVALO(a)(b)(
    lambda i: lambda acc: SOMA(acc)(f(i))
)(ZERO)

# --------------------------------------------------------------------------
# PRODUTÓRIO — Π_{i=a}^{b} f(i)
# --------------------------------------------------------------------------
PRODUTORIO = lambda f: lambda a: lambda b: INTERVALO(a)(b)(
    lambda i: lambda acc: MULT(acc)(f(i))
)(_UM)

# --------------------------------------------------------------------------
# FATORIAL — n! = Π_{i=1}^{n} i   (caso particular do produtório, f=identidade)
# --------------------------------------------------------------------------
FATORIAL = lambda n: PRODUTORIO(lambda i: i)(_UM)(n)

# --------------------------------------------------------------------------
# INDUÇÃO — VERIFICADOR limitado, não provador.
# O rascunho original ("INDUCAO = lambda P: lambda n: E(P(0))(...)") tentava
# ser um provador de teoremas — impossível por busca (indução prova para
# TODO n, não para uma amostra). O que se pode honestamente construir por
# busca é um VERIFICADOR: confirma que P(0) vale e que P(k) -> P(S(k))
# vale para todo k em [0, limite) — evidência computacional, não prova.
# --------------------------------------------------------------------------
from .logica import IMPLICA  # noqa: E402

VERIFICAR_INDUCAO = lambda P: lambda limite: E(
    P(ZERO)
)(
    INTERVALO(ZERO)(limite)(
        lambda k: lambda acc: E(acc)(IMPLICA(P(k))(P(S(k))))
    )(V)
)

# --------------------------------------------------------------------------
# SEQUÊNCIA RECORRENTE GERAL — dado o estado inicial e a função de passo,
# devolve o n-ésimo termo. (Isto é literalmente ITER, com outro nome, para
# deixar a intenção explícita quando se está a definir uma sequência.)
# --------------------------------------------------------------------------
from .primitivas import ITER  # noqa: E402

SEQUENCIA = lambda inicial: lambda passo: lambda n: ITER(n)(inicial)(passo)

# --------------------------------------------------------------------------
# FIBONACCI — via par de estado (F(k), F(k+1)), avançado com ITER.
# --------------------------------------------------------------------------
from .primitivas import PAR  # noqa: E402

_PASSO_FIB = lambda p: PAR(p(F))(SOMA(p(V))(p(F)))
FIBONACCI = lambda n: ITER(n)(PAR(ZERO)(_UM))(_PASSO_FIB)(V)
