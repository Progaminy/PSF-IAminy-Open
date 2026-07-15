# ==============================================================================
# ANÁLISE SINTÁTICA FINITA — Etapas 681 a 700.
# ==============================================================================
# Fechamento do arco 481-700: tokenização, parsing descendente limitado,
# AST, verificação de parênteses, tabela simples e pipeline lexing->parse->tipo.
# Sem divisão, módulo, primalidade/fatoração ou garantias infinitas.
# ==============================================================================
from .primitivas import V, F
from .semantica_operacional_finita import LIT, ADD, MUL
from .semantica_tipos_finitos import TIPO_EXPRESSAO_FINITA, AVALIAR_TIPADA_FINITA, TIPO_NAT


def _bool(condicao):
    return V if condicao else F


def TOKEN_FINITO(tipo, valor):
    return (tipo, valor)


def LEXER_ARITMETICO_FINITO(texto):
    tokens = []
    i = 0
    while i < len(texto):
        c = texto[i]
        if c.isspace():
            i += 1
            continue
        if c.isdigit():
            j = i
            while j < len(texto) and texto[j].isdigit():
                j += 1
            tokens.append(TOKEN_FINITO("NUM", int(texto[i:j])))
            i = j
            continue
        if c in "+*()":
            tokens.append(TOKEN_FINITO(c, c))
            i += 1
            continue
        raise SyntaxError(f"caractere desconhecido: {c}")
    tokens.append(TOKEN_FINITO("EOF", "EOF"))
    return tuple(tokens)


class _Parser:
    def __init__(self, tokens):
        self.tokens = tuple(tokens)
        self.i = 0

    def atual(self):
        return self.tokens[self.i]

    def consumir(self, tipo):
        tok = self.atual()
        if tok[0] != tipo:
            raise SyntaxError(f"esperado {tipo}, obtido {tok}")
        self.i += 1
        return tok

    def parse_expr(self):
        no = self.parse_term()
        while self.atual()[0] == "+":
            self.consumir("+")
            no = ADD(no, self.parse_term())
        return no

    def parse_term(self):
        no = self.parse_factor()
        while self.atual()[0] == "*":
            self.consumir("*")
            no = MUL(no, self.parse_factor())
        return no

    def parse_factor(self):
        tok = self.atual()
        if tok[0] == "NUM":
            self.consumir("NUM")
            return LIT(tok[1])
        if tok[0] == "(":
            self.consumir("(")
            no = self.parse_expr()
            self.consumir(")")
            return no
        raise SyntaxError(f"fator inválido: {tok}")


def PARSER_ARITMETICO_FINITO(tokens):
    p = _Parser(tokens)
    ast = p.parse_expr()
    p.consumir("EOF")
    return ast


def PARSE_TEXTO_ARITMETICO_FINITO(texto):
    return PARSER_ARITMETICO_FINITO(LEXER_ARITMETICO_FINITO(texto))


def PARENTESES_BALANCEADOS_FINITO(texto):
    pilha = []
    for c in texto:
        if c == "(":
            pilha.append(c)
        elif c == ")":
            if not pilha:
                return F
            pilha.pop()
    return _bool(len(pilha) == 0)


def ANALISE_TIPADA_ARITMETICA_FINITA(texto):
    ast = PARSE_TEXTO_ARITMETICO_FINITO(texto)
    tipo = TIPO_EXPRESSAO_FINITA(ast)
    if tipo != TIPO_NAT:
        raise TypeError("expressão aritmética esperada")
    return {"tokens": LEXER_ARITMETICO_FINITO(texto), "ast": ast, "tipo": tipo, "valor": AVALIAR_TIPADA_FINITA(ast)}


def TABELA_LL1_MINIMA_FINITA():
    return {
        ("Expr", "NUM"): "Term ExprTail",
        ("Expr", "("): "Term ExprTail",
        ("ExprTail", "+"): "+ Term ExprTail",
        ("ExprTail", ")"): "ε",
        ("ExprTail", "EOF"): "ε",
        ("Term", "NUM"): "Factor TermTail",
        ("Term", "("): "Factor TermTail",
        ("TermTail", "*"): "* Factor TermTail",
        ("TermTail", "+"): "ε",
        ("TermTail", ")"): "ε",
        ("TermTail", "EOF"): "ε",
        ("Factor", "NUM"): "NUM",
        ("Factor", "("): "( Expr )",
    }


def FECHAMENTO_ANALISE_SINTATICA_FINITA():
    return V
