# ==============================================================================
# OPERAÇÕES ALGÉBRICAS NATURAIS — Etapas 81 a 90 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   grupo nasce depois de operação binária, fechamento e associatividade;
#   anel nasce depois de grupo (aditivo) e semigrupo (multiplicativo).
#
# Este módulo continua o padrão de relacoes_funcoes_naturais.py: uma
# "operação binária sobre um domínio finito" é representada exatamente como
# aritmetica.SOMA/MULT já são — uma função curried `lambda a: lambda b: c` —
# não uma estrutura nova. O que É novo aqui são os PREDICADOS sobre essa
# função (fechamento, associatividade, neutro, comutatividade...), testados
# sobre um domínio finito explícito com o mesmo TODO_FINITO_PURO/
# EXISTE_FINITO_PURO já usado nas etapas 61-80.
#
# Conceitos permitidos aqui:
#   V/F, igualdade dos naturais, lógica booleana, domínio finito explícito,
#   tudo o que já nasceu nas etapas 1-80.
# Conceitos proibidos aqui:
#   anéis com divisão, corpos, espaços vetoriais, homomorfismos, categoria,
#   estruturas infinitas, análise, estruturas ainda não construídas.
#
# Observação honesta: GRUPO_PURO e ANEL_INICIAL_PURO precisam localizar um
# elemento neutro concreto para depois testar inversos — isso usa um `for`
# Python sobre o domínio finito explícito (mesmo padrão já usado em
# CLASSE_EQUIVALENCIA_PURA, etapa 67), não uma nova licença para laços sobre
# quantidades não-finitas ou não-declaradas.
# ==============================================================================
from .primitivas import V, F
from .logica import E
from .aritmetica import IGUAL
from .traducao import para_bool
from .relacoes_funcoes_naturais import TODO_FINITO_PURO, EXISTE_FINITO_PURO


# ----------------------------------------------------------------------------
# Etapa 81 — operação binária.
# Não é uma estrutura nova: é o nome próprio para "função de dois argumentos
# que devolve um valor", o mesmo padrão de SOMA/MULT. Existe só para o
# tópico ficar rastreável no índice conceitual.
# ----------------------------------------------------------------------------
OPERACAO_BINARIA_PURA = lambda funcao: funcao


# ----------------------------------------------------------------------------
# Etapa 82 — fechamento: o resultado da operação permanece no domínio.
# ----------------------------------------------------------------------------
FECHADA_PURA = lambda dominio: lambda op: TODO_FINITO_PURO(
    dominio,
    lambda a: TODO_FINITO_PURO(
        dominio,
        lambda b: EXISTE_FINITO_PURO(dominio, lambda c: IGUAL(op(a)(b))(c)),
    ),
)


# ----------------------------------------------------------------------------
# Etapa 83 — associatividade: (a∘b)∘c = a∘(b∘c) para todo a,b,c do domínio.
# ----------------------------------------------------------------------------
ASSOCIATIVA_PURA = lambda dominio: lambda op: TODO_FINITO_PURO(
    dominio,
    lambda a: TODO_FINITO_PURO(
        dominio,
        lambda b: TODO_FINITO_PURO(
            dominio,
            lambda c: IGUAL(op(op(a)(b))(c))(op(a)(op(b)(c))),
        ),
    ),
)


# ----------------------------------------------------------------------------
# Etapa 84 — elemento neutro: e tal que e∘a = a∘e = a para todo a.
# ----------------------------------------------------------------------------
EH_NEUTRO_PURA = lambda dominio: lambda op: lambda e: TODO_FINITO_PURO(
    dominio,
    lambda a: E(IGUAL(op(e)(a))(a))(IGUAL(op(a)(e))(a)),
)

EXISTE_NEUTRO_PURA = lambda dominio: lambda op: EXISTE_FINITO_PURO(
    dominio, lambda e: EH_NEUTRO_PURA(dominio)(op)(e)
)


def NEUTRO_CONCRETO_PURA(dominio, op):
    """Devolve o elemento neutro concreto, se existir, senão None.
    Usa `for` sobre o domínio finito explícito — mesmo padrão de
    CLASSE_EQUIVALENCIA_PURA (etapa 67): busca operacional sobre uma
    coleção finita e já dada, não uma nova licença de iteração."""
    for e in dominio:
        if para_bool(EH_NEUTRO_PURA(dominio)(op)(e)):
            return e
    return None


# ----------------------------------------------------------------------------
# Etapa 85 — comutatividade: a∘b = b∘a para todo a,b.
# ----------------------------------------------------------------------------
COMUTATIVA_PURA = lambda dominio: lambda op: TODO_FINITO_PURO(
    dominio,
    lambda a: TODO_FINITO_PURO(dominio, lambda b: IGUAL(op(a)(b))(op(b)(a))),
)


# ----------------------------------------------------------------------------
# Etapa 86 — semigrupo: fechada + associativa.
# ----------------------------------------------------------------------------
SEMIGRUPO_PURO = lambda dominio: lambda op: E(
    FECHADA_PURA(dominio)(op)
)(
    ASSOCIATIVA_PURA(dominio)(op)
)


# ----------------------------------------------------------------------------
# Etapa 87 — monoide: semigrupo + existe elemento neutro.
# ----------------------------------------------------------------------------
MONOIDE_PURO = lambda dominio: lambda op: E(
    SEMIGRUPO_PURO(dominio)(op)
)(
    EXISTE_NEUTRO_PURA(dominio)(op)
)


# ----------------------------------------------------------------------------
# Etapa 88 — inverso algébrico, relativo a um neutro `e` já conhecido.
# ----------------------------------------------------------------------------
EH_INVERSO_PURA = lambda dominio: lambda op: lambda e: lambda a: lambda b: E(
    IGUAL(op(a)(b))(e)
)(
    IGUAL(op(b)(a))(e)
)

TEM_INVERSO_PURA = lambda dominio: lambda op: lambda e: lambda a: EXISTE_FINITO_PURO(
    dominio, lambda b: EH_INVERSO_PURA(dominio)(op)(e)(a)(b)
)

TODOS_TEM_INVERSO_PURA = lambda dominio: lambda op: lambda e: TODO_FINITO_PURO(
    dominio, lambda a: TEM_INVERSO_PURA(dominio)(op)(e)(a)
)


# ----------------------------------------------------------------------------
# Etapa 89 — grupo: monoide onde todo elemento tem inverso.
# Precisa do neutro CONCRETO (não só "existe") para testar os inversos —
# por isso não é uma composição direta de booleanos PSF como as etapas
# anteriores; usa NEUTRO_CONCRETO_PURA (mesma justificação da etapa 84).
# ----------------------------------------------------------------------------
def GRUPO_PURO(dominio, op):
    if not para_bool(MONOIDE_PURO(dominio)(op)):
        return F
    e = NEUTRO_CONCRETO_PURA(dominio, op)
    return TODOS_TEM_INVERSO_PURA(dominio)(op)(e)


def GRUPO_ABELIANO_PURO(dominio, op):
    return E(GRUPO_PURO(dominio, op))(COMUTATIVA_PURA(dominio)(op))


# ----------------------------------------------------------------------------
# Etapa 90 — anel inicial: (D,soma) grupo abeliano; (D,produto) semigrupo;
# produto distribui sobre soma dos dois lados.
# ----------------------------------------------------------------------------
DISTRIBUTIVA_PURA = lambda dominio: lambda soma: lambda produto: TODO_FINITO_PURO(
    dominio,
    lambda a: TODO_FINITO_PURO(
        dominio,
        lambda b: TODO_FINITO_PURO(
            dominio,
            lambda c: E(
                IGUAL(produto(a)(soma(b)(c)))(soma(produto(a)(b))(produto(a)(c)))
            )(
                IGUAL(produto(soma(b)(c))(a))(soma(produto(b)(a))(produto(c)(a)))
            ),
        ),
    ),
)


def ANEL_INICIAL_PURO(dominio, soma, produto):
    grupo_aditivo_abeliano = para_bool(GRUPO_ABELIANO_PURO(dominio, soma))
    semigrupo_multiplicativo = para_bool(SEMIGRUPO_PURO(dominio)(produto))
    distributiva = para_bool(DISTRIBUTIVA_PURA(dominio)(soma)(produto))
    return V if (grupo_aditivo_abeliano and semigrupo_multiplicativo and distributiva) else F
