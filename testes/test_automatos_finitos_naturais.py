import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.traducao import para_bool
from nucleo.automatos_finitos_naturais import (
    DFA_NATURAL_FINITO, EXECUTAR_DFA_NATURAL, ACEITA_DFA_NATURAL,
    COMPLEMENTO_DFA_NATURAL, UNIAO_DFA_NATURAL, INTERSECAO_DFA_NATURAL,
    NFA_NATURAL_FINITO, FECHO_EPSILON_NATURAL, ACEITA_NFA_NATURAL,
    NFA_PARA_DFA_NATURAL, EQUIVALENTES_EM_CATALOGO_DFA,
    FECHAMENTO_AUTOMATOS_FINITOS_NATURAIS,
)

falhas=[]
def ok(nome, obtido, esperado):
    print(("[OK]" if obtido==esperado else "[FALHOU]"), nome, obtido, esperado)
    if obtido!=esperado: falhas.append(nome)
def b(x): return para_bool(x)

def dfa_par_a():
    estados=("par","impar"); alf=("a","b")
    trans={("par","a"):"impar",("impar","a"):"par",("par","b"):"par",("impar","b"):"impar"}
    return DFA_NATURAL_FINITO(estados, alf, trans, "par", ("par",))

def dfa_termina_b():
    estados=("nao","sim"); alf=("a","b")
    trans={("nao","a"):"nao",("nao","b"):"sim",("sim","a"):"nao",("sim","b"):"sim"}
    return DFA_NATURAL_FINITO(estados, alf, trans, "nao", ("sim",))

def main():
    d1=dfa_par_a(); d2=dfa_termina_b()
    ok("traço DFA", EXECUTAR_DFA_NATURAL(d1, ("a","b","a")), ("par","impar","impar","par"))
    ok("DFA aceita par de a", b(ACEITA_DFA_NATURAL(d1, ("a","b","a"))), True)
    ok("complemento rejeita onde original aceita", b(ACEITA_DFA_NATURAL(COMPLEMENTO_DFA_NATURAL(d1), ("a","b","a"))), False)
    ok("união aceita por segundo", b(ACEITA_DFA_NATURAL(UNIAO_DFA_NATURAL(d1,d2), ("a","b"))), True)
    ok("interseção exige ambos", b(ACEITA_DFA_NATURAL(INTERSECAO_DFA_NATURAL(d1,d2), ("a","b","a"))), False)

    nfa=NFA_NATURAL_FINITO(("s","a","f"),("x",),{("s","ε"):("a",),("a","x"):("f",)},"s",("f",))
    ok("fecho epsilon chega a a", set(FECHO_EPSILON_NATURAL(nfa,("s",))), {"s","a"})
    ok("NFA aceita x", b(ACEITA_NFA_NATURAL(nfa,("x",))), True)
    dfa=NFA_PARA_DFA_NATURAL(nfa)
    ok("DFA determinizado aceita x", b(ACEITA_DFA_NATURAL(dfa,("x",))), True)
    ok("equivalência catálogo", b(EQUIVALENTES_EM_CATALOGO_DFA(dfa, dfa, (tuple(), ("x",)))), True)
    ok("fechamento", b(FECHAMENTO_AUTOMATOS_FINITOS_NATURAIS()), True)
    if falhas:
        print("FALHAS", falhas); raise SystemExit(1)
    print("Tudo passou.")
if __name__ == "__main__": main()
