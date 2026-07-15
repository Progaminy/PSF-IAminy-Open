# ==============================================================================
# SEMÂNTICA E TIPOS FINITOS — Etapas 641 a 680.
# ==============================================================================
# Depois de sintaxe e semântica operacional, nasce a pergunta: uma expressão é
# bem-formada semanticamente antes de executar? Esta camada constrói tipos
# finitos, juízos de tipagem, avaliação segura limitada e equivalência por
# catálogo. Não usa divisão, módulo, primalidade/fatoração nem infinito atual.
# ==============================================================================
from .primitivas import V, F
from .semantica_operacional_finita import LIT, VAR, ADD, MUL, LET, AVALIAR_EXPRESSAO_FINITA


def _bool(condicao):
    return V if condicao else F


def _bool_to_py(valor):
    return valor(True)(False)


TIPO_NAT = "Nat"
TIPO_BOOL = "Bool"


def BOOL_EXPR(valor):
    return ("bool", bool(valor))


def IF_EXPR(condicao, entao, senao):
    return ("if", condicao, entao, senao)


def EQ_EXPR(a, b):
    return ("eq", a, b)


def TIPO_EXPRESSAO_FINITA(expressao, contexto=None):
    contexto = dict(contexto or {})
    tipo = expressao[0]
    if tipo == "lit":
        return TIPO_NAT
    if tipo == "bool":
        return TIPO_BOOL
    if tipo == "var":
        if expressao[1] not in contexto:
            raise TypeError(f"variável sem tipo: {expressao[1]}")
        return contexto[expressao[1]]
    if tipo in {"add", "mul"}:
        t1 = TIPO_EXPRESSAO_FINITA(expressao[1], contexto)
        t2 = TIPO_EXPRESSAO_FINITA(expressao[2], contexto)
        if t1 == TIPO_NAT and t2 == TIPO_NAT:
            return TIPO_NAT
        raise TypeError("adição/multiplicação finita exigem Nat")
    if tipo == "eq":
        t1 = TIPO_EXPRESSAO_FINITA(expressao[1], contexto)
        t2 = TIPO_EXPRESSAO_FINITA(expressao[2], contexto)
        if t1 == t2:
            return TIPO_BOOL
        raise TypeError("igualdade exige tipos iguais")
    if tipo == "if":
        tc = TIPO_EXPRESSAO_FINITA(expressao[1], contexto)
        if tc != TIPO_BOOL:
            raise TypeError("condição do if precisa ser Bool")
        t2 = TIPO_EXPRESSAO_FINITA(expressao[2], contexto)
        t3 = TIPO_EXPRESSAO_FINITA(expressao[3], contexto)
        if t2 == t3:
            return t2
        raise TypeError("ramos do if precisam ter mesmo tipo")
    if tipo == "let":
        nome = expressao[1]
        tipo_valor = TIPO_EXPRESSAO_FINITA(expressao[2], contexto)
        novo = dict(contexto)
        novo[nome] = tipo_valor
        return TIPO_EXPRESSAO_FINITA(expressao[3], novo)
    raise TypeError(f"expressão desconhecida: {tipo}")


def BEM_TIPADA_FINITA(expressao, contexto=None):
    try:
        TIPO_EXPRESSAO_FINITA(expressao, contexto)
        return V
    except TypeError:
        return F


def AVALIAR_TIPADA_FINITA(expressao, ambiente=None, contexto=None, limite_passos=100):
    if not _bool_to_py(BEM_TIPADA_FINITA(expressao, contexto)):
        raise TypeError("expressão não é bem tipada")

    def avaliar(expr, env):
        tipo = expr[0]
        if tipo == "bool":
            return expr[1]
        if tipo == "if":
            return avaliar(expr[2], env) if avaliar(expr[1], env) else avaliar(expr[3], env)
        if tipo == "eq":
            return avaliar(expr[1], env) == avaliar(expr[2], env)
        if tipo in {"lit", "var", "add", "mul", "let"}:
            return AVALIAR_EXPRESSAO_FINITA(expr, env, limite_passos)
        raise ValueError("expressão desconhecida")

    return avaliar(expressao, dict(ambiente or {}))


def PRESERVACAO_TIPO_POR_AVALIACAO_FINITA(expressao, contexto=None, ambiente=None):
    tipo_antes = TIPO_EXPRESSAO_FINITA(expressao, contexto)
    valor = AVALIAR_TIPADA_FINITA(expressao, ambiente, contexto)
    if isinstance(valor, bool):
        tipo_depois = TIPO_BOOL
    else:
        tipo_depois = TIPO_NAT
    return _bool(tipo_antes == tipo_depois)


def EQUIVALENTES_POR_CATALOGO_FINITO(expr_a, expr_b, catalogo_ambientes, contexto=None):
    if TIPO_EXPRESSAO_FINITA(expr_a, contexto) != TIPO_EXPRESSAO_FINITA(expr_b, contexto):
        return F
    for ambiente in catalogo_ambientes:
        if AVALIAR_TIPADA_FINITA(expr_a, ambiente, contexto) != AVALIAR_TIPADA_FINITA(expr_b, ambiente, contexto):
            return F
    return V


def FECHAMENTO_SEMANTICA_TIPOS_FINITOS():
    return V
