# ==============================================================================
# EXPRESSÕES SIMBÓLICAS E EQUAÇÕES FINITAS — Etapas 131 a 133 e 135.
# ==============================================================================
# Lei PSF-IAminy:
#   expressão simbólica nasce depois de anel/corpo (soma, subtração,
#   produto, potência já existem); equação de primeiro grau nasce depois
#   de expressão E de inverso multiplicativo (etapa 94).
#
# O bloqueio antigo era a equação de segundo grau por fórmula real, que
# exigiria raiz quadrada geral. A Etapa 135 resolve apenas a versão finita:
# busca exaustiva em domínio explícito, sem fórmula quadrática e sem raízes
# gerais. Correta no domínio declarado, sem prometer o caso real.
#
# Representação: uma expressão é uma tupla aninhada:
#   ('const', valor)      valor é um elemento do domínio
#   ('var',)               a variável (só uma, "x" implícito)
#   ('soma', e1, e2)
#   ('sub', e1, e2)
#   ('mult', e1, e2)
#   ('pot', e, n)           n é um natural Python (expoente), não uma expressão
#
# Conceitos permitidos: tudo o que nasceu nas etapas 1-134.
# Conceitos proibidos: múltiplas variáveis, fórmula quadrática real,
# raízes gerais, estruturas ainda não construídas.
# ==============================================================================
from .traducao import para_bool, de_int
from .aritmetica import IGUAL


# ----------------------------------------------------------------------------
# Etapa 131 — expressão simbólica finita: construtores da gramática.
# ----------------------------------------------------------------------------
CONST = lambda valor: ("const", valor)
VAR = ("var",)
SOMA_EXPR = lambda e1: lambda e2: ("soma", e1, e2)
SUB_EXPR = lambda e1: lambda e2: ("sub", e1, e2)
MULT_EXPR = lambda e1: lambda e2: ("mult", e1, e2)
POT_EXPR = lambda e: lambda n: ("pot", e, n)


# ----------------------------------------------------------------------------
# Etapa 132 — avaliação de expressão sobre um domínio finito: substitui a
# variável por um valor concreto e reduz usando as operações do anel/corpo
# fornecidas (nunca operadores nativos do Python sobre os coeficientes).
# ----------------------------------------------------------------------------
def AVALIAR_EXPRESSAO_PURA(expr, valor_x, soma, sub, mult, pot):
    tag = expr[0]
    if tag == "const":
        return expr[1]
    if tag == "var":
        return valor_x
    if tag == "soma":
        return soma(AVALIAR_EXPRESSAO_PURA(expr[1], valor_x, soma, sub, mult, pot))(
            AVALIAR_EXPRESSAO_PURA(expr[2], valor_x, soma, sub, mult, pot)
        )
    if tag == "sub":
        return sub(AVALIAR_EXPRESSAO_PURA(expr[1], valor_x, soma, sub, mult, pot))(
            AVALIAR_EXPRESSAO_PURA(expr[2], valor_x, soma, sub, mult, pot)
        )
    if tag == "mult":
        return mult(AVALIAR_EXPRESSAO_PURA(expr[1], valor_x, soma, sub, mult, pot))(
            AVALIAR_EXPRESSAO_PURA(expr[2], valor_x, soma, sub, mult, pot)
        )
    if tag == "pot":
        base = AVALIAR_EXPRESSAO_PURA(expr[1], valor_x, soma, sub, mult, pot)
        # expr[2] é um int nativo do Python por desenho (POT_EXPR guarda o
        # expoente assim, para a gramática ficar simples de escrever à
        # mão: POT_EXPR(VAR)(2), não POT_EXPR(VAR)(de_int(2))). A
        # conversão para numeral de Church acontece exatamente aqui —
        # única fronteira, não espalhada pelas funções de corpo (que
        # continuam a esperar Church, como em todo o resto do projeto).
        return pot(base)(de_int(expr[2]))
    raise ValueError(f"construtor de expressão desconhecido: {tag}")


# ----------------------------------------------------------------------------
# Etapa 133 — equação de primeiro grau finita: ax+b=c, sobre um corpo já
# validado. Duas formas independentes, cruzadas uma contra a outra:
#   (a) fórmula fechada — x = (c-b)·a⁻¹, usando o inverso multiplicativo
#       do corpo (etapa 94);
#   (b) busca exaustiva — avalia a EXPRESSÃO ax+b em todo o domínio finito
#       e vê onde bate com c (generaliza para QUALQUER expressão, não só
#       linear, mas só é honesta porque o domínio é pequeno).
# As duas devolvem a mesma resposta sempre que existe solução — é uma
# prova de consistência, não só duas formas de fazer a mesma coisa.
# ----------------------------------------------------------------------------
def RESOLVER_LINEAR_FORMULA_PURA(a, b, c, dominio, soma, sub, mult, unidade):
    """x = (c-b)/a, achando o inverso de `a` por busca no domínio."""
    alvo = sub(c)(b)
    for candidato_inverso in dominio:
        if para_bool(IGUAL(mult(a)(candidato_inverso))(unidade)):
            return mult(alvo)(candidato_inverso)
    return None  # `a` não tem inverso neste domínio (não é corpo, ou a=0)


def RESOLVER_EXPRESSAO_POR_BUSCA_PURA(expr, alvo, dominio, soma, sub, mult, pot):
    """Acha x no domínio tal que AVALIAR_EXPRESSAO_PURA(expr,x,...) == alvo.
    Funciona para QUALQUER expressão desta gramática, não só linear —
    generalização honesta: busca exaustiva, correta porque o domínio é
    finito e pequeno (mesma disciplina de RAIZES_EM_DOMINIO_PURA)."""
    for x in dominio:
        if para_bool(IGUAL(AVALIAR_EXPRESSAO_PURA(expr, x, soma, sub, mult, pot))(alvo)):
            return x
    return None


# ----------------------------------------------------------------------------
# Etapa 135 — equação quadrática finita: ax²+bx+c=0 por busca exaustiva.
# Isto NÃO é a fórmula real de Bhaskara: não usa discriminante, raiz quadrada
# geral nem divisão por 2a. É a versão honesta que já cabe no sistema:
# domínio finito explícito + avaliação de expressão.
# ----------------------------------------------------------------------------
QUADRATICA_EXPR = lambda a: lambda b: lambda c: SOMA_EXPR(
    SOMA_EXPR(MULT_EXPR(CONST(a))(POT_EXPR(VAR)(2)))(
        MULT_EXPR(CONST(b))(VAR)
    )
)(CONST(c))


def RESOLVER_EXPRESSAO_TODAS_SOLUCOES_PURA(expr, alvo, dominio, soma, sub, mult, pot):
    """Todas as soluções x do domínio finito com expr(x) == alvo."""
    return tuple(
        x for x in dominio
        if para_bool(IGUAL(AVALIAR_EXPRESSAO_PURA(expr, x, soma, sub, mult, pot))(alvo))
    )


def RESOLVER_QUADRATICA_FINITA_PURA(a, b, c, dominio, soma, sub, mult, pot, zero):
    """Raízes de ax²+bx+c=0 em um domínio finito explícito.

    Se a=0, a equação deixou de ser quadrática; esta função devolve tupla
    vazia e a etapa 133 continua responsável pelo caso linear.
    """
    if para_bool(IGUAL(a)(zero)):
        return tuple()
    return RESOLVER_EXPRESSAO_TODAS_SOLUCOES_PURA(
        QUADRATICA_EXPR(a)(b)(c), zero, dominio, soma, sub, mult, pot
    )
