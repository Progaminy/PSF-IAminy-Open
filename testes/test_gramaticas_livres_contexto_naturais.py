import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from nucleo.traducao import para_bool
from nucleo.gramaticas_livres_contexto_naturais import (
    CFG_NATURAL_FINITA, DERIVACAO_ESQUERDA_UM_PASSO_FINITA, DERIVAR_ESQUERDA_ATE_FINITO,
    EH_CNF_FINITA, CYK_RECONHECE_FINITO, ARVORE_SINTATICA_FINITA, RAIZ_ARVORE_SINTATICA,
    FOLHAS_ARVORE_SINTATICA, PROFUNDIDADE_ARVORE_SINTATICA, CFG_E_CYK_CONCORDAM_CATALOGO,
    FECHAMENTO_CFG_NATURAL_FINITA,
)
falhas=[]
def ok(nome, obtido, esperado):
    print(("[OK]" if obtido==esperado else "[FALHOU]"), nome, obtido, esperado)
    if obtido!=esperado: falhas.append(nome)
def b(x): return para_bool(x)

def gramatica_anbn_cnf():
    return CFG_NATURAL_FINITA(("S","A","B","X"),("a","b"),"S",(
        ("S", ("A","B")), ("S", ("A","X")), ("X", ("S","B")), ("A", ("a",)), ("B", ("b",)),
    ))

def main():
    g = gramatica_anbn_cnf()
    ok("CNF válida", b(EH_CNF_FINITA(g)), True)
    ok("derivação esquerda de S", set(DERIVACAO_ESQUERDA_UM_PASSO_FINITA(g,("S",))), {("A","B"),("A","X")})
    ok("deriva formas em limite", ("a","b") in DERIVAR_ESQUERDA_ATE_FINITO(g,3), True)
    ok("CYK aceita ab", b(CYK_RECONHECE_FINITO(g,("a","b"))), True)
    ok("CYK aceita aabb", b(CYK_RECONHECE_FINITO(g,("a","a","b","b"))), True)
    ok("CYK rejeita abb", b(CYK_RECONHECE_FINITO(g,("a","b","b"))), False)
    arv = ARVORE_SINTATICA_FINITA("S", ARVORE_SINTATICA_FINITA("A", ARVORE_SINTATICA_FINITA("a")), ARVORE_SINTATICA_FINITA("B", ARVORE_SINTATICA_FINITA("b")))
    ok("raiz", RAIZ_ARVORE_SINTATICA(arv), "S")
    ok("folhas", FOLHAS_ARVORE_SINTATICA(arv), ("a","b"))
    ok("profundidade", PROFUNDIDADE_ARVORE_SINTATICA(arv), 3)
    ok("geração e CYK concordam no catálogo", b(CFG_E_CYK_CONCORDAM_CATALOGO(g, (("a","b"),("a","a","b","b"),("a","b","b")), 7)), True)
    ok("fechamento", b(FECHAMENTO_CFG_NATURAL_FINITA()), True)
    if falhas:
        print("FALHAS", falhas); raise SystemExit(1)
    print("Tudo passou.")
if __name__ == "__main__": main()
