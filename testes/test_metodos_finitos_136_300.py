"""PSF-IAminy — Métodos finitos, Etapas 136 a 300.
Roda com: python3 testes/test_metodos_finitos_136_300.py
"""
import ast
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.fluxo import relatorio_fluxo
from nucleo.traducao import para_bool
from nucleo.metodos_finitos import (
    ALFABETO_FINITO,
    ACEITA_DFA_FINITO,
    ANTICADEIA_FINITA,
    AVALIAR_EXPR_MULTIVAR_FINITA,
    AVALIAR_PROP_FINITA,
    CADEIA_FINITA,
    CNF_POR_TABELA_FINITA,
    COMPLEMENTO_DFA_FINITO,
    CONEXO_TOPOLOGICO_FINITO,
    CONJUNTO_FINITO,
    CONSEQUENCIA_FINITA,
    CONTINUA_FINITA,
    CONTRADICAO_FINITA,
    CONTRAEXEMPLOS_FINITO,
    DECIDIR_PROP_FINITA,
    DFA_FINITO,
    DNF_POR_TABELA_FINITA,
    EQUACOES_EQUIVALENTES_FINITO,
    FECHO_FINITO,
    FECHAMENTO_METODO_FINITO,
    FECHAMENTO_METODOS_FINITOS_ATE_300,
    FECHAMENTO_PREFIXOS_LINGUAGEM_FINITO,
    FRONTEIRA_FINITA,
    IGUAL_CONJUNTO_FINITO,
    INTERIOR_FINITO,
    INTERSECAO_FINITA,
    LINGUAGEM_ACEITA_FINITA,
    LINGUAGEM_FINITA,
    MAXIMIZADORES_FINITO,
    MINIMIZADORES_FINITO,
    MODELOS_PROP_FINITO,
    PARTICAO_FINITA,
    PARTES_FINITO,
    PERTENCE_CONJUNTO_FINITO,
    PERTENCE_LINGUAGEM_FINITA,
    PALAVRA_FINITA,
    PREFIXO_FINITO,
    PREFIXOS_FINITO,
    PRODUTO_CARTESIANO_FINITO,
    PRODUTO_DOMINIOS_NOMEADOS_FINITO,
    PROP_E,
    PROP_IMPLICA,
    PROP_NAO,
    PROP_OU,
    PROP_VAR,
    REDE_FINITA,
    SATISFATIVEL_FINITA,
    SISTEMA_SOLUCOES_FINITO,
    SOLUCOES_PREDICADO_FINITO,
    SUFIXO_FINITO,
    SUPREMOS_FINITO,
    TABELA_VERDADE_FINITA,
    TAUTOLOGIA_FINITA,
    TEORIA_CONSISTENTE_FINITA,
    TOPOLOGIA_FINITA,
    TRANSICAO_ESTENDIDA_DFA_FINITA,
    UNIAO_FINITA,
    VALORACOES_PROP_FINITA,
)

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
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "metodos_finitos.py")
    with open(caminho, "r", encoding="utf-8") as f:
        arvore = ast.parse(f.read(), filename=caminho)
    proibidos = {"DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "DECOMPOR"}
    modulos_proibidos = {"primos", "divisores"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em metodos_finitos.py")
        if isinstance(no, ast.Name) and no.id in proibidos:
            falhas.append(f"nome proibido {no.id}")
        if isinstance(no, ast.ImportFrom):
            modulo = (no.module or "").split(".")[-1]
            if modulo in modulos_proibidos:
                falhas.append(f"módulo proibido {no.module}")


def main():
    print("PSF-IAminy — Métodos finitos, Etapas 136 a 300")
    verificar_pureza()

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 300", r["maior_etapa"] >= 300, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    dominio = tuple(range(6))
    pares = SOLUCOES_PREDICADO_FINITO(dominio, lambda x: x in (0, 2, 4))
    verificar("soluções por predicado finito", pares, (0, 2, 4))
    verificar(
        "sistema finito x>1 e x<4",
        SISTEMA_SOLUCOES_FINITO(dominio, lambda x: x > 1, lambda x: x < 4),
        (2, 3),
    )
    verificar(
        "equações equivalentes no domínio",
        b(EQUACOES_EQUIVALENTES_FINITO(dominio, lambda x: x < 3, lambda x: x in (0, 1, 2))),
        True,
    )
    verificar("minimizadores", MINIMIZADORES_FINITO((1, 2, 3), lambda x: abs(x - 2)), (2,))
    verificar("maximizadores", MAXIMIZADORES_FINITO((1, 2, 3), lambda x: x * x), (3,))
    valoracoes = PRODUTO_DOMINIOS_NOMEADOS_FINITO({"x": (0, 1), "y": (2, 3)})
    verificar("produto de domínios nomeados", len(valoracoes), 4)
    expr = ("soma", ("var", "x"), ("mult", ("const", 2), ("var", "y")))
    verificar(
        "expressão multivariável",
        AVALIAR_EXPR_MULTIVAR_FINITA(expr, {"x": 1, "y": 3}, {
            "soma": lambda a, c: a + c,
            "sub": lambda a, c: a - c,
            "mult": lambda a, c: a * c,
        }),
        7,
    )
    verificar("contraexemplos finitos", CONTRAEXEMPLOS_FINITO((0, 1, 2), lambda x: x < 2), (2,))
    verificar("fechamento de método finito", b(FECHAMENTO_METODO_FINITO((0, 1, 2), lambda x: x < 2)), True)

    A = CONJUNTO_FINITO("a", "b", "a")
    B = CONJUNTO_FINITO("b", "c")
    verificar("conjunto finito remove repetição", A, ("a", "b"))
    verificar("pertencimento finito", b(PERTENCE_CONJUNTO_FINITO("a", A)), True)
    verificar("união finita", UNIAO_FINITA(A, B), ("a", "b", "c"))
    verificar("interseção finita", INTERSECAO_FINITA(A, B), ("b",))
    verificar("produto cartesiano finito", PRODUTO_CARTESIANO_FINITO(("a",), (1, 2)), (("a", 1), ("a", 2)))
    verificar("partes finito tamanho", len(PARTES_FINITO(("a", "b", "c"))), 8)
    verificar("partição finita", b(PARTICAO_FINITA(("a", "b", "c"), (("a",), ("b", "c")))), True)
    verificar("igualdade extensional", b(IGUAL_CONJUNTO_FINITO(("b", "a"), ("a", "b"))), True)

    div_leq = lambda a, c: c % a == 0
    ordem = (1, 2, 3, 6)
    verificar("supremo de 2 e 3 por divisibilidade", SUPREMOS_FINITO(ordem, (2, 3), div_leq), (6,))
    verificar("cadeia", b(CADEIA_FINITA((1, 2, 6), div_leq)), True)
    verificar("anticadeia", b(ANTICADEIA_FINITA((2, 3), div_leq)), True)
    verificar("rede finita por divisibilidade de divisores de 6", b(REDE_FINITA(ordem, div_leq)), True)

    universo = ("a", "b")
    abertos = (tuple(), ("a",), universo)
    verificar("topologia finita de Sierpinski", b(TOPOLOGIA_FINITA(universo, abertos)), True)
    verificar("interior finito", INTERIOR_FINITO(("a", "b"), abertos), ("a", "b"))
    verificar("fecho finito de {a}", FECHO_FINITO(universo, ("a",), abertos), ("a", "b"))
    verificar("fronteira finita de {a}", FRONTEIRA_FINITA(universo, ("a",), abertos), ("b",))
    verificar("continuidade identidade", b(CONTINUA_FINITA(universo, abertos, abertos, lambda x: x)), True)
    verificar("conexidade topológica", b(CONEXO_TOPOLOGICO_FINITO(universo, abertos)), True)

    alfabeto = ALFABETO_FINITO("a")
    palavra = PALAVRA_FINITA("a", "a")
    linguagem = LINGUAGEM_FINITA(palavra)
    verificar("alfabeto finito", alfabeto, ("a",))
    verificar("prefixo", b(PREFIXO_FINITO(("a",), palavra)), True)
    verificar("sufixo", b(SUFIXO_FINITO(("a",), palavra)), True)
    verificar("prefixos", PREFIXOS_FINITO(palavra), (tuple(), ("a",), ("a", "a")))
    verificar("linguagem pertence", b(PERTENCE_LINGUAGEM_FINITA(palavra, linguagem)), True)
    verificar("fechamento prefixos linguagem", FECHAMENTO_PREFIXOS_LINGUAGEM_FINITO(linguagem), (tuple(), ("a",), ("a", "a")))

    automato = DFA_FINITO(
        ("par", "impar"),
        alfabeto,
        {
            ("par", "a"): "impar",
            ("impar", "a"): "par",
        },
        "par",
        ("par",),
    )
    amostra = (tuple(), ("a",), ("a", "a"))
    verificar("transição estendida DFA", TRANSICAO_ESTENDIDA_DFA_FINITA(automato, "par", palavra), "par")
    verificar("aceita DFA palavra par", b(ACEITA_DFA_FINITO(automato, palavra)), True)
    verificar("linguagem aceita em amostra", LINGUAGEM_ACEITA_FINITA(automato, amostra), (tuple(), ("a", "a")))
    verificar("complemento DFA aceita ímpar", b(ACEITA_DFA_FINITO(COMPLEMENTO_DFA_FINITO(automato), ("a",))), True)

    p = PROP_VAR("p")
    q = PROP_VAR("q")
    taut = PROP_IMPLICA(p, p)
    conj = PROP_E(p, q)
    contr = PROP_E(p, PROP_NAO(p))
    verificar("avaliar proposição", AVALIAR_PROP_FINITA(PROP_OU(p, q), {"p": False, "q": True}), True)
    verificar("valorações proposicionais", len(VALORACOES_PROP_FINITA(("p", "q"))), 4)
    verificar("tabela verdade", len(TABELA_VERDADE_FINITA(PROP_OU(p, q))), 4)
    verificar("modelos", len(MODELOS_PROP_FINITO(conj)), 1)
    verificar("tautologia", b(TAUTOLOGIA_FINITA(taut)), True)
    verificar("satisfatível", b(SATISFATIVEL_FINITA(conj)), True)
    verificar("contradição", b(CONTRADICAO_FINITA(contr)), True)
    verificar("consequência", b(CONSEQUENCIA_FINITA((conj,), p)), True)
    verificar("DNF por tabela tem termo", DNF_POR_TABELA_FINITA(conj), ((("p", True), ("q", True)),))
    verificar("CNF por tabela não vazia", len(CNF_POR_TABELA_FINITA(PROP_OU(p, q))), 1)
    verificar("teoria consistente", b(TEORIA_CONSISTENTE_FINITA((p, PROP_IMPLICA(p, q)))), True)
    verificar("decidir proposição", DECIDIR_PROP_FINITA(contr), {"tautologia": False, "satisfativel": False, "contradicao": True})
    verificar("fechamento até 300", b(FECHAMENTO_METODOS_FINITOS_ATE_300()), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
