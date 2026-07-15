"""Testes das etapas 441-480: gramáticas formais finitas e pilha finita."""
import ast
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.fluxo import relatorio_fluxo, proxima_etapa_natural
from nucleo.gramaticas_finitas import (
    ACEITA_PILHA_FINITA,
    ALFABETO_GRAMATICAL_FINITO,
    AUTOMATO_PILHA_PARENTESIS_FINITO,
    CONCATENACAO_GRAMATICAS_REGULARES_FINITA,
    DERIVACAO_UM_PASSO_FINITA,
    DERIVAR_ATE_FINITO,
    DERIVAVEL_EM_ATE_FINITO,
    EH_GRAMATICA_REGULAR_DIREITA_FINITA,
    EPSILON_FINITO,
    ESTRELA_LIMITADA_LINGUAGEM_FINITA,
    FECHAMENTO_DERIVACAO_FINITA,
    FECHAMENTO_GRAMATICAS_E_PILHA_FINITA,
    FECHAMENTO_GRAMATICAS_REGULARES_FINITA,
    FOLHAS_ARVORE_DERIVACAO_FINITA,
    FORMA_SENTENCIAL_INICIAL_FINITA,
    GRAMATICA_E_DFA_CONCORDAM_FINITO,
    GRAMATICA_E_PILHA_PARENTESIS_CONCORDAM_FINITA,
    GRAMATICA_FINITA,
    GRAMATICA_PARENTESIS_BALANCEADOS_FINITA,
    GRAMATICA_REGULAR_PARA_DFA_FINITO,
    PALAVRAS_GERADAS_ATE_FINITO,
    PALAVRA_GRAMATICAL_FINITA,
    PRODUCAO_FINITA,
    TERMINAIS_E_NAO_TERMINAIS_FINITOS,
    UNIAO_GRAMATICAS_FINITA,
)
from nucleo.metodos_finitos import ACEITA_DFA_FINITO
from nucleo.traducao import para_bool

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def b(valor):
    return para_bool(valor)


def verificar_pureza():
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "gramaticas_finitas.py")
    with open(caminho, "r", encoding="utf-8") as f:
        arvore = ast.parse(f.read(), filename=caminho)
    proibidos = {"DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "DECOMPOR"}
    modulos_proibidos = {"primos", "divisores"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em gramaticas_finitas.py")
        if isinstance(no, ast.Name) and no.id in proibidos:
            falhas.append(f"nome proibido {no.id}")
        if isinstance(no, (ast.Import, ast.ImportFrom)):
            nomes = []
            if isinstance(no, ast.Import):
                nomes = [a.name.split('.')[0] for a in no.names]
            else:
                nomes = [no.module.split('.')[-1] if no.module else a.name for a in no.names]
            for nome in nomes:
                if nome in modulos_proibidos:
                    falhas.append(f"módulo proibido importado: {nome}")


def gramatica_a_estrela_b():
    return GRAMATICA_FINITA(
        nao_terminais=("S",),
        terminais=("a", "b"),
        inicial="S",
        producoes=(
            PRODUCAO_FINITA("S", ("a", "S")),
            PRODUCAO_FINITA("S", ("b",)),
        ),
    )


def main():
    print("PSF-IAminy — Gramáticas formais finitas, Etapas 441 a 480")
    verificar_pureza()

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 480", r["maior_etapa"] >= 480, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])
    verificar("motor já avançou além de 480 sem lacunas", r["maior_etapa"] >= 480 and r["faltando_ate_maior"] == [], True)

    verificar("alfabeto remove repetições preservando ordem", ALFABETO_GRAMATICAL_FINITO(("a", "b", "a")), ("a", "b"))
    verificar("palavra gramatical é tupla finita", PALAVRA_GRAMATICAL_FINITA("a", "b"), ("a", "b"))
    verificar("terminais e não-terminais separados", TERMINAIS_E_NAO_TERMINAIS_FINITOS(("a",), ("S",)), (("a",), ("S",)))

    g = gramatica_a_estrela_b()
    verificar("forma inicial é o símbolo inicial", FORMA_SENTENCIAL_INICIAL_FINITA(g), ("S",))
    verificar("um passo de S gera aS e b", set(DERIVACAO_UM_PASSO_FINITA(g, ("S",))), {("a", "S"), ("b",)})
    geradas = set(PALAVRAS_GERADAS_ATE_FINITO(g, 4))
    verificar("gramática gera b, ab, aab, aaab até 4 passos", {("b",), ("a", "b"), ("a", "a", "b"), ("a", "a", "a", "b")} <= geradas, True)
    verificar("aaab derivável em até 4 passos", b(DERIVAVEL_EM_ATE_FINITO(g, ("a", "a", "a", "b"), 4)), True)
    verificar("epsilon é palavra vazia", EPSILON_FINITO(), tuple())
    verificar("fechamento da derivação finita", b(FECHAMENTO_DERIVACAO_FINITA()), True)

    verificar("gramática a*b é regular à direita", b(EH_GRAMATICA_REGULAR_DIREITA_FINITA(g)), True)
    dfa = GRAMATICA_REGULAR_PARA_DFA_FINITO(g)
    verificar("DFA traduzido aceita aaab", b(ACEITA_DFA_FINITO(dfa, ("a", "a", "a", "b"))), True)
    verificar("DFA traduzido rejeita aba", b(ACEITA_DFA_FINITO(dfa, ("a", "b", "a"))), False)
    verificar("gramática e DFA concordam em catálogo finito", b(GRAMATICA_E_DFA_CONCORDAM_FINITO(g, (("b",), ("a", "b"), ("a", "b", "a")), 5)), True)

    g2 = GRAMATICA_FINITA(("T",), ("c",), "T", (("T", ("c",)),))
    uniao = UNIAO_GRAMATICAS_FINITA(g, g2)
    verificar("união gera palavra de g", b(DERIVAVEL_EM_ATE_FINITO(uniao, ("b",), 4)), True)
    verificar("união gera palavra de g2", b(DERIVAVEL_EM_ATE_FINITO(uniao, ("c",), 3)), True)

    g_eps_a = GRAMATICA_FINITA(("S",), ("a",), "S", (("S", tuple()), ("S", ("a",))))
    concat = CONCATENACAO_GRAMATICAS_REGULARES_FINITA(g_eps_a, g2)
    verificar("concatenação substitui epsilon da primeira pelo inicial da segunda", b(DERIVAVEL_EM_ATE_FINITO(concat, ("c",), 4)), True)
    verificar("estrela limitada de {a,b} até 2 repetições", set(ESTRELA_LIMITADA_LINGUAGEM_FINITA((("a",), ("b",)), 2)), {tuple(), ("a",), ("b",), ("a", "a"), ("a", "b"), ("b", "a"), ("b", "b")})
    verificar("fechamento das gramáticas regulares finitas", b(FECHAMENTO_GRAMATICAS_REGULARES_FINITA()), True)

    gp = GRAMATICA_PARENTESIS_BALANCEADOS_FINITA()
    formas = DERIVAR_ATE_FINITO(gp, 4)
    verificar("gramática de parênteses gera epsilon", tuple() in PALAVRAS_GERADAS_ATE_FINITO(gp, 1), True)
    verificar("gramática de parênteses gera ()", ("(", ")") in PALAVRAS_GERADAS_ATE_FINITO(gp, 3), True)
    arvore = ("S", (("(", ()), ("S", ()), (")", ()), ("S", ())))
    verificar("folhas de árvore de derivação são lidas da esquerda para direita", FOLHAS_ARVORE_DERIVACAO_FINITA(arvore), ("(", "S", ")", "S"))

    pda = AUTOMATO_PILHA_PARENTESIS_FINITO(8)
    verificar("PDA aceita parênteses balanceados simples", b(ACEITA_PILHA_FINITA(pda, ("(", ")"), 10)), True)
    verificar("PDA aceita parênteses balanceados aninhados", b(ACEITA_PILHA_FINITA(pda, ("(", "(", ")", ")"), 20)), True)
    verificar("PDA rejeita parênteses desbalanceados", b(ACEITA_PILHA_FINITA(pda, ("(", ")", ")"), 20)), False)
    catalogo = (tuple(), ("(", ")"), ("(", "(", ")", ")"), ("(", ")", ")"))
    verificar("gramática e PDA de parênteses concordam no catálogo finito", b(GRAMATICA_E_PILHA_PARENTESIS_CONCORDAM_FINITA(catalogo, 6, 8, 20)), True)
    verificar("fechamento gramáticas livres de contexto e pilha finita", b(FECHAMENTO_GRAMATICAS_E_PILHA_FINITA()), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
