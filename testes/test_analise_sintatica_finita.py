import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from nucleo.traducao import para_bool
from nucleo.analise_sintatica_finita import (
    TOKEN_FINITO, LEXER_ARITMETICO_FINITO, PARSE_TEXTO_ARITMETICO_FINITO,
    PARENTESES_BALANCEADOS_FINITO, ANALISE_TIPADA_ARITMETICA_FINITA,
    TABELA_LL1_MINIMA_FINITA, FECHAMENTO_ANALISE_SINTATICA_FINITA,
)
from nucleo.semantica_operacional_finita import ADD, MUL, LIT
falhas=[]
def ok(nome, obtido, esperado):
    print(("[OK]" if obtido==esperado else "[FALHOU]"), nome, obtido, esperado)
    if obtido!=esperado: falhas.append(nome)
def b(x): return para_bool(x)

def main():
    ok("token", TOKEN_FINITO("NUM",3), ("NUM",3))
    toks = LEXER_ARITMETICO_FINITO("2 + 3*4")
    ok("lexer termina com EOF", toks[-1], ("EOF","EOF"))
    ok("parser respeita precedência", PARSE_TEXTO_ARITMETICO_FINITO("2+3*4"), ADD(LIT(2), MUL(LIT(3), LIT(4))))
    ok("parênteses balanceados", b(PARENTESES_BALANCEADOS_FINITO("(())()")), True)
    ok("parênteses rejeitados", b(PARENTESES_BALANCEADOS_FINITO("(()")), False)
    rel = ANALISE_TIPADA_ARITMETICA_FINITA("2+3*4")
    ok("pipeline valor", rel["valor"], 14)
    ok("tabela LL1 contém Expr NUM", TABELA_LL1_MINIMA_FINITA()[("Expr","NUM")], "Term ExprTail")
    ok("fechamento", b(FECHAMENTO_ANALISE_SINTATICA_FINITA()), True)
    if falhas:
        print("FALHAS", falhas); raise SystemExit(1)
    print("Tudo passou.")
if __name__ == "__main__": main()
