import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from nucleo.traducao import para_bool
from nucleo.semantica_operacional_finita import LIT, ADD, MUL, VAR, LET
from nucleo.semantica_tipos_finitos import (
    BOOL_EXPR, IF_EXPR, EQ_EXPR, TIPO_EXPRESSAO_FINITA, BEM_TIPADA_FINITA,
    AVALIAR_TIPADA_FINITA, PRESERVACAO_TIPO_POR_AVALIACAO_FINITA,
    EQUIVALENTES_POR_CATALOGO_FINITO, FECHAMENTO_SEMANTICA_TIPOS_FINITOS,
    TIPO_NAT, TIPO_BOOL,
)
falhas=[]
def ok(nome, obtido, esperado):
    print(("[OK]" if obtido==esperado else "[FALHOU]"), nome, obtido, esperado)
    if obtido!=esperado: falhas.append(nome)
def b(x): return para_bool(x)

def main():
    expr = IF_EXPR(EQ_EXPR(ADD(LIT(1),LIT(1)), LIT(2)), MUL(LIT(3),LIT(4)), LIT(0))
    ok("tipo if", TIPO_EXPRESSAO_FINITA(expr), TIPO_NAT)
    ok("avalia if tipado", AVALIAR_TIPADA_FINITA(expr), 12)
    ok("bool tem tipo Bool", TIPO_EXPRESSAO_FINITA(BOOL_EXPR(True)), TIPO_BOOL)
    ok("expressão mal tipada é rejeitada", b(BEM_TIPADA_FINITA(ADD(BOOL_EXPR(True), LIT(1)))), False)
    let = LET("x", LIT(5), ADD(VAR("x"), LIT(1)))
    ok("let preserva tipo", b(PRESERVACAO_TIPO_POR_AVALIACAO_FINITA(let)), True)
    a = ADD(VAR("x"), LIT(1)); c = ADD(LIT(1), VAR("x"))
    ok("equivalência por catálogo", b(EQUIVALENTES_POR_CATALOGO_FINITO(a,c,({"x":0},{"x":2}), {"x":TIPO_NAT})), True)
    ok("fechamento", b(FECHAMENTO_SEMANTICA_TIPOS_FINITOS()), True)
    if falhas:
        print("FALHAS", falhas); raise SystemExit(1)
    print("Tudo passou.")
if __name__ == "__main__": main()
