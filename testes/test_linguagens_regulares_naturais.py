import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from nucleo.traducao import para_bool
from nucleo.linguagens_regulares_naturais import (
    SIMBOLO_REGEX, CONCAT_REGEX, ESTRELA_REGEX, UNIAO_REGEX, EPSILON_REGEX,
    ENUMERAR_REGEX_LIMITADO, LINGUAGEM_REGEX_CONTEM_LIMITADO, ALFABETO_REGEX,
    REGEX_PARA_NFA_NATURAL, REGEX_E_NFA_CONCORDAM_CATALOGO, REGEX_E_DFA_CONCORDAM_CATALOGO,
    FECHAMENTO_LINGUAGENS_REGULARES_NATURAIS,
)
from nucleo.automatos_finitos_naturais import ACEITA_NFA_NATURAL
falhas=[]
def ok(nome, obtido, esperado):
    print(("[OK]" if obtido==esperado else "[FALHOU]"), nome, obtido, esperado)
    if obtido!=esperado: falhas.append(nome)
def b(x): return para_bool(x)

def main():
    r = CONCAT_REGEX(ESTRELA_REGEX(SIMBOLO_REGEX("a")), SIMBOLO_REGEX("b"))
    ok("alfabeto", set(ALFABETO_REGEX(r)), {"a","b"})
    ok("enumera b e aab", {("b",),("a","a","b")} <= set(ENUMERAR_REGEX_LIMITADO(r,3,4)), True)
    ok("contém aaab", b(LINGUAGEM_REGEX_CONTEM_LIMITADO(r,("a","a","a","b"),4)), True)
    ok("não contém aba", b(LINGUAGEM_REGEX_CONTEM_LIMITADO(r,("a","b","a"),4)), False)
    nfa = REGEX_PARA_NFA_NATURAL(UNIAO_REGEX(EPSILON_REGEX(), SIMBOLO_REGEX("c")))
    ok("NFA da regex aceita epsilon", b(ACEITA_NFA_NATURAL(nfa, tuple())), True)
    ok("NFA da regex aceita c", b(ACEITA_NFA_NATURAL(nfa, ("c",))), True)
    catalogo=(tuple(), ("b",), ("a","b"), ("a","b","a"))
    ok("regex e NFA concordam", b(REGEX_E_NFA_CONCORDAM_CATALOGO(r,catalogo,4)), True)
    ok("regex e DFA concordam", b(REGEX_E_DFA_CONCORDAM_CATALOGO(r,catalogo,4)), True)
    ok("fechamento", b(FECHAMENTO_LINGUAGENS_REGULARES_NATURAIS()), True)
    if falhas:
        print("FALHAS", falhas); raise SystemExit(1)
    print("Tudo passou.")
if __name__ == "__main__": main()
