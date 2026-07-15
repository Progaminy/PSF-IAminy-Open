"""PSF-IAminy — Teoria de modelos finita + prova de primeira ordem, Etapas 361 a 380.
Roda com: python3 testes/test_teoria_modelos_prova_finita.py
"""
import ast
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.fluxo import relatorio_fluxo
from nucleo.traducao import para_bool
from nucleo.logica_predicados_finita import (
    ATOMICA,
    DOMINIO_FINITO,
    ESTRUTURA_FINITA,
    EXISTE_QUANTIFICADO,
    IGUALDADE_DIAGONAL_FINITA,
    PARA_TODO_QUANTIFICADO,
    SATISFAZ_FINITA,
    SUBSTITUIR_LIVRE_FINITA,
    TERMO_CONST,
    TERMO_FUNC,
    TERMO_VAR,
)
from nucleo.metodos_finitos import PROP_VAR, PROP_IMPLICA, CONSEQUENCIA_FINITA
from nucleo.teoria_modelos_prova_finita import (
    ASSINATURA_FINITA,
    CONCLUSAO_DE,
    CONCLUSAO_FINAL_DA_DERIVACAO,
    DERIVACAO_VALIDA,
    DOMINIO_DE,
    EH_HOMOMORFISMO_ESTRUTURAS,
    EH_ISOMORFISMO_ESTRUTURAS,
    EH_MERGULHO_ESTRUTURAS,
    EH_SUBESTRUTURA_FECHADA,
    EH_SUBESTRUTURA_FINITA,
    EQUIVALENCIA_ELEMENTAR_FINITA,
    EXPANSAO_FINITA,
    FECHAMENTO_PROVA_FINITA_ATE_380,
    FECHAMENTO_TEORIA_MODELOS_FINITA_ATE_370,
    ISOMORFISMO_ELEMENTAR_FINITO,
    PASSO_DERIVACAO,
    PASSO_VALIDO,
    PREMISSAS_DE,
    REDUCT_FINITO,
    SEQUENTE_FINITO,
    SUBESTRUTURA_FINITA,
    SUBESTRUTURA_GERADA_FINITA,
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
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "teoria_modelos_prova_finita.py")
    with open(caminho, "r", encoding="utf-8") as f:
        arvore = ast.parse(f.read(), filename=caminho)
    proibidos = {"DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "DECOMPOR"}
    modulos_proibidos = {"primos", "divisores"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em teoria_modelos_prova_finita.py")
        if isinstance(no, ast.Name) and no.id in proibidos:
            falhas.append(f"nome proibido {no.id}")
        if isinstance(no, ast.ImportFrom):
            modulo = (no.module or "").split(".")[-1]
            if modulo in modulos_proibidos:
                falhas.append(f"módulo proibido {no.module}")


def estrutura_z3():
    D = (0, 1, 2)
    soma_tab = {
        (0, 0): 0, (0, 1): 1, (0, 2): 2,
        (1, 0): 1, (1, 1): 2, (1, 2): 0,
        (2, 0): 2, (2, 1): 0, (2, 2): 1,
    }
    return ESTRUTURA_FINITA(D, {"=": IGUALDADE_DIAGONAL_FINITA(D)}, {"+": soma_tab})


def estrutura_z3_relabeled():
    D = ("a", "b", "c")
    mapa = {0: "a", 1: "b", 2: "c"}
    soma_tab_z3 = {
        (0, 0): 0, (0, 1): 1, (0, 2): 2,
        (1, 0): 1, (1, 1): 2, (1, 2): 0,
        (2, 0): 2, (2, 1): 0, (2, 2): 1,
    }
    soma_tab = {(mapa[i], mapa[j]): mapa[soma_tab_z3[(i, j)]] for (i, j) in soma_tab_z3}
    return ESTRUTURA_FINITA(D, {"=": IGUALDADE_DIAGONAL_FINITA(D)}, {"+": soma_tab}), mapa


def main():
    print("PSF-IAminy — Teoria de modelos finita + prova de primeira ordem, Etapas 361 a 380")
    verificar_pureza()

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 380", r["maior_etapa"] >= 380, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    # --- Etapas 361-362: subestrutura e subestrutura gerada ---
    Ez3 = estrutura_z3()
    verificar("{0} é subestrutura fechada (0+0=0)", b(EH_SUBESTRUTURA_FECHADA(Ez3, (0,))), True)
    verificar("{0,1} não é fechada (1+1=2 sai fora)", b(EH_SUBESTRUTURA_FECHADA(Ez3, (0, 1))), False)
    sub0 = SUBESTRUTURA_FINITA(Ez3, (0,))
    verificar("subestrutura {0} é subestrutura válida de Z3", b(EH_SUBESTRUTURA_FINITA(Ez3, sub0)), True)
    gerada = SUBESTRUTURA_GERADA_FINITA(Ez3, (1,))
    verificar("1 gera Z3 inteiro (facto: 1 gera grupo cíclico de ordem 3)", tuple(sorted(DOMINIO_DE(gerada))), (0, 1, 2))

    # --- Etapas 363-365: homomorfismo, isomorfismo, mergulho ---
    Ez3b, mapa = estrutura_z3_relabeled()
    verificar("mapa 0->a,1->b,2->c é homomorfismo", b(EH_HOMOMORFISMO_ESTRUTURAS(Ez3, Ez3b, mapa)), True)
    verificar("mapa 0->a,1->b,2->c é isomorfismo", b(EH_ISOMORFISMO_ESTRUTURAS(Ez3, Ez3b, mapa)), True)
    mapa_errado = {0: "a", 1: "a", 2: "b"}
    verificar("mapa não-injetivo não é isomorfismo", b(EH_ISOMORFISMO_ESTRUTURAS(Ez3, Ez3b, mapa_errado)), False)
    verificar("mergulho de Z3 em si mesma relabeled", b(EH_MERGULHO_ESTRUTURAS(Ez3, Ez3b, mapa)), True)

    # --- Etapas 366-367: reduct e expansão ---
    reduzida = REDUCT_FINITO(Ez3, ("=",), tuple())
    verificar("reduct sem '+' não guarda funções", reduzida["funcoes"], {})
    expandida = EXPANSAO_FINITA(reduzida, funcoes_novos={"+": Ez3["funcoes"]["+"]})
    verificar("expansão devolve '+' de volta", expandida["funcoes"]["+"], Ez3["funcoes"]["+"])

    # --- Etapas 368-369: equivalência elementar / isomorfismo elementar (FACTO INDEPENDENTE) ---
    x, y, z = TERMO_VAR("x"), TERMO_VAR("y"), TERMO_VAR("z")
    soma = lambda a1, a2: TERMO_FUNC("+", a1, a2)
    assoc = PARA_TODO_QUANTIFICADO("x", PARA_TODO_QUANTIFICADO("y", PARA_TODO_QUANTIFICADO("z",
        ATOMICA("=", soma(soma(x, y), z), soma(x, soma(y, z))))))
    verificar("Z3 e sua versão relabeled são elementarmente equivalentes (associatividade)", b(EQUIVALENCIA_ELEMENTAR_FINITA(Ez3, Ez3b, (assoc,))), True)
    verificar("isomorfismo implica equivalência elementar (facto padrão)", b(ISOMORFISMO_ELEMENTAR_FINITO(Ez3, Ez3b, mapa, (assoc,))), True)

    # --- Etapa 370 ---
    verificar("fechamento teoria de modelos até 370", b(FECHAMENTO_TEORIA_MODELOS_FINITA_ATE_370()), True)

    # --- Etapa 371: assinatura finita ---
    assinatura = ASSINATURA_FINITA({"=": 2}, {"+": 2})
    verificar("assinatura registra aridade de '+'", assinatura["funcoes"]["+"], 2)

    # --- Etapa 372: sequente ---
    seq = SEQUENTE_FINITO((ATOMICA("P"),), ATOMICA("P"))
    verificar("premissas do sequente", PREMISSAS_DE(seq), (ATOMICA("P"),))
    verificar("conclusão do sequente", CONCLUSAO_DE(seq), ATOMICA("P"))

    # --- Etapas 373-376: regras proposicionais + solidez cruzada (FACTO INDEPENDENTE) ---
    p, q, rr = ATOMICA("p"), ATOMICA("q"), ATOMICA("r")
    gamma = (p, ("implica", p, q), ("implica", q, rr))
    passos = (
        PASSO_DERIVACAO("premissa", (), SEQUENTE_FINITO(gamma, p)),
        PASSO_DERIVACAO("premissa", (), SEQUENTE_FINITO(gamma, ("implica", p, q))),
        PASSO_DERIVACAO("premissa", (), SEQUENTE_FINITO(gamma, ("implica", q, rr))),
        PASSO_DERIVACAO("modus_ponens", (0, 1), SEQUENTE_FINITO(gamma, q)),
        PASSO_DERIVACAO("modus_ponens", (3, 2), SEQUENTE_FINITO(gamma, rr)),
    )
    verificar("derivação {p,p→q,q→r} ⊢ r é válida (dois modus ponens)", b(DERIVACAO_VALIDA(passos)), True)
    verificar("conclusão final da derivação é r", CONCLUSAO_FINAL_DA_DERIVACAO(passos), rr)

    pp, pq, pr = PROP_VAR("p"), PROP_VAR("q"), PROP_VAR("r")
    premissas_prop = (pp, PROP_IMPLICA(pp, pq), PROP_IMPLICA(pq, pr))
    verificar("oráculo proposicional (etapa 275) confirma r é consequência de {p,p→q,q→r}", b(CONSEQUENCIA_FINITA(premissas_prop, pr)), True)

    passos_invalidos = passos[:3] + (PASSO_DERIVACAO("modus_ponens", (0, 2), SEQUENTE_FINITO(gamma, rr)),)
    verificar("derivação com modus ponens malformado é rejeitada", b(DERIVACAO_VALIDA(passos_invalidos)), False)

    conjuncao_seq = SEQUENTE_FINITO(gamma, ("e", p, q))
    passos_e = passos[:4] + (PASSO_DERIVACAO("e_intro", (0, 3), conjuncao_seq),)
    verificar("∧-introdução válida (p e q derivados)", b(DERIVACAO_VALIDA(passos_e)), True)
    passos_e_elim = passos_e + (PASSO_DERIVACAO("e_elim_dir", (4,), SEQUENTE_FINITO(gamma, q)),)
    verificar("∧-eliminação-direita recupera q", b(DERIVACAO_VALIDA(passos_e_elim)), True)

    disj_seq = SEQUENTE_FINITO(gamma, ("ou", p, rr))
    passos_ou = passos[:1] + (PASSO_DERIVACAO("ou_intro", (0,), disj_seq),)
    verificar("∨-introdução válida (p implica p∨r)", b(DERIVACAO_VALIDA(passos_ou)), True)

    # --- Etapas 377-378: quantificadores ---
    Dp = DOMINIO_FINITO(0, 1, 2)
    Ep = ESTRUTURA_FINITA(Dp, {"P": ((0,), (1,), (2,))}, {})
    formula_px = ATOMICA("P", x)
    universal = PARA_TODO_QUANTIFICADO("x", formula_px)
    seq_univ = SEQUENTE_FINITO((universal,), universal)
    seq_inst = SEQUENTE_FINITO((universal,), SUBSTITUIR_LIVRE_FINITA(formula_px, "x", TERMO_CONST(0)))
    passos_forall = (
        PASSO_DERIVACAO("premissa", (), seq_univ),
        PASSO_DERIVACAO("para_todo_elim", (0,), seq_inst, TERMO_CONST(0)),
    )
    verificar("∀-eliminação instancia P(0) a partir de ∀x P(x)", b(DERIVACAO_VALIDA(passos_forall)), True)
    verificar("estrutura Ep satisfaz P(0), confirmando a instanciação", b(SATISFAZ_FINITA(Ep, ATOMICA("P", TERMO_CONST(0)))), True)

    p0 = ATOMICA("P", TERMO_CONST(0))
    existencial = EXISTE_QUANTIFICADO("x", formula_px)
    passos_existe = (
        PASSO_DERIVACAO("premissa", (), SEQUENTE_FINITO((p0,), p0)),
        PASSO_DERIVACAO("existe_intro", (0,), SEQUENTE_FINITO((p0,), existencial), TERMO_CONST(0)),
    )
    verificar("∃-introdução por testemunha 0 é válida", b(DERIVACAO_VALIDA(passos_existe)), True)
    verificar("estrutura satisfaz ∃x P(x) quando P(0) vale (facto semântico correspondente)", b(SATISFAZ_FINITA(Ep, existencial)), True)

    # --- Etapa 380 ---
    verificar("fechamento prova finita até 380", b(FECHAMENTO_PROVA_FINITA_ATE_380()), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
