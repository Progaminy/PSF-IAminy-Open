"""PSF-IAminy — Lógica de predicados finita, Etapas 341 a 360.
Roda com: python3 testes/test_logica_predicados_finita.py
"""
import ast
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.fluxo import relatorio_fluxo
from nucleo.traducao import para_bool
from nucleo.logica_predicados_finita import (
    ATOMICA,
    ATRIBUICAO_FINITA,
    ATUALIZAR_ATRIBUICAO,
    AVALIAR_TERMO,
    DOMINIO_DE,
    DOMINIO_FINITO,
    EH_ESTRUTURA_FINITA_VALIDA,
    EH_EXTENSAO_VALIDA_PREDICADO,
    EH_MODELO_FINITO,
    EH_SENTENCA_FINITA,
    ESTRUTURA_FINITA,
    E_FORMULA,
    EXISTE_QUANTIFICADO,
    FECHAMENTO_LOGICA_PREDICADOS_ATE_360,
    IGUALDADE_DIAGONAL_FINITA,
    IMPLICA_FORMULA,
    NAO,
    OU_FORMULA,
    PARA_TODO_QUANTIFICADO,
    SATISFAZ_ATOMICA_FINITA,
    SATISFAZ_FINITA,
    SUBSTITUIR_LIVRE_FINITA,
    SUBSTITUIR_TERMO,
    TERMO_CONST,
    TERMO_FUNC,
    TERMO_VAR,
    VALIDA_SOBRE_ESTRUTURAS_FINITA,
    VARIAVEIS_DO_TERMO,
    VARIAVEIS_LIGADAS_FINITA,
    VARIAVEIS_LIVRES_FINITA,
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
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "logica_predicados_finita.py")
    with open(caminho, "r", encoding="utf-8") as f:
        arvore = ast.parse(f.read(), filename=caminho)
    proibidos = {"DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "DECOMPOR"}
    modulos_proibidos = {"primos", "divisores"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em logica_predicados_finita.py")
        if isinstance(no, ast.Name) and no.id in proibidos:
            falhas.append(f"nome proibido {no.id}")
        if isinstance(no, ast.ImportFrom):
            modulo = (no.module or "").split(".")[-1]
            if modulo in modulos_proibidos:
                falhas.append(f"módulo proibido {no.module}")


def estrutura_sucessor_ciclico():
    """Domínio {0,1,2} com sucessor cíclico 0->1->2->0.

    Usado para o facto independente: ∀x∃y suc(x,y) não implica
    ∃y∀x suc(x,y) — padrão de qualquer livro-texto de lógica de primeira
    ordem (ex.: Enderton).
    """
    D = DOMINIO_FINITO(0, 1, 2)
    suc = ((0, 1), (1, 2), (2, 0))
    return ESTRUTURA_FINITA(D, {"suc": suc, "=": IGUALDADE_DIAGONAL_FINITA(D)}, {})


def estrutura_z3_aditivo():
    """Z_3 sob adição — grupo cíclico de ordem 3, facto publicado de álgebra.

    Tabela dada por extensão (enumeração explícita), não calculada por
    operador nativo de módulo dentro do núcleo.
    """
    D = (0, 1, 2)
    soma_tab = {
        (0, 0): 0, (0, 1): 1, (0, 2): 2,
        (1, 0): 1, (1, 1): 2, (1, 2): 0,
        (2, 0): 2, (2, 1): 0, (2, 2): 1,
    }
    return ESTRUTURA_FINITA(D, {"=": IGUALDADE_DIAGONAL_FINITA(D)}, {"+": soma_tab})


def main():
    print("PSF-IAminy — Lógica de predicados finita, Etapas 341 a 360")
    verificar_pureza()

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 360", r["maior_etapa"] >= 360, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    # --- Etapas 341-344: domínio, estrutura, predicado, função ---
    D = DOMINIO_FINITO("a", "b", "c")
    verificar("domínio finito", D, ("a", "b", "c"))

    E = ESTRUTURA_FINITA(D, {"P": (("a",), ("b",))}, {})
    verificar("domínio da estrutura", DOMINIO_DE(E), ("a", "b", "c"))
    verificar("extensão de P válida (aridade 1)", b(EH_EXTENSAO_VALIDA_PREDICADO(E, "P", 1)), True)
    verificar("extensão de P inválida como aridade 2", b(EH_EXTENSAO_VALIDA_PREDICADO(E, "P", 2)), False)
    verificar("igualdade diagonal sobre {0,1}", IGUALDADE_DIAGONAL_FINITA((0, 1)), ((0, 0), (1, 1)))

    # --- Etapa 345/346: termo e avaliação ---
    Ez3 = estrutura_z3_aditivo()
    verificar("estrutura Z3 válida (=, +)", b(EH_ESTRUTURA_FINITA_VALIDA(Ez3, {"=": 2}, {"+": 2})), True)
    x, y, z = TERMO_VAR("x"), TERMO_VAR("y"), TERMO_VAR("z")
    soma = lambda a1, a2: TERMO_FUNC("+", a1, a2)
    atrib = ATRIBUICAO_FINITA({"x": 1, "y": 2})
    verificar("avaliação de termo x+y em Z3 (1+2=0)", AVALIAR_TERMO(Ez3, soma(x, y), atrib), 0)
    verificar("variáveis do termo x+y", VARIAVEIS_DO_TERMO(soma(x, y)), ("x", "y"))
    verificar("variáveis do termo (x+y)+0", VARIAVEIS_DO_TERMO(soma(soma(x, y), TERMO_CONST(0))), ("x", "y"))

    # --- Etapa 347/348: fórmula atômica e conectivos reaproveitados ---
    atomica_xy = ATOMICA("=", soma(x, y), z)
    verificar("fórmula atômica é uma tupla marcada", atomica_xy[0], "atomica")
    formula_e = E_FORMULA(atomica_xy, NAO(atomica_xy))
    verificar("conectivo E reaproveitado de metodos_finitos", formula_e[0], "e")
    verificar("conectivo OU existe", OU_FORMULA(atomica_xy, atomica_xy)[0], "ou")
    verificar("conectivo IMPLICA existe", IMPLICA_FORMULA(atomica_xy, atomica_xy)[0], "implica")

    # --- Etapa 349/350: variáveis livres e ligadas ---
    formula_livre = ATOMICA("suc", x, y)
    verificar("variáveis livres de suc(x,y)", VARIAVEIS_LIVRES_FINITA(formula_livre), ("x", "y"))
    formula_quant = PARA_TODO_QUANTIFICADO("x", EXISTE_QUANTIFICADO("y", formula_livre))
    verificar("variáveis livres de ∀x∃y suc(x,y)", VARIAVEIS_LIVRES_FINITA(formula_quant), tuple())
    verificar("variáveis ligadas de ∀x∃y suc(x,y)", VARIAVEIS_LIGADAS_FINITA(formula_quant), ("x", "y"))
    verificar("∀x∃y suc(x,y) é sentença", b(EH_SENTENCA_FINITA(formula_quant)), True)
    verificar("suc(x,y) sozinha não é sentença", b(EH_SENTENCA_FINITA(formula_livre)), False)

    # --- Etapa 351/352/357/358: quantificadores, ordem importa (FACTO INDEPENDENTE) ---
    Esuc = estrutura_sucessor_ciclico()
    para_todo_existe = PARA_TODO_QUANTIFICADO("x", EXISTE_QUANTIFICADO("y", ATOMICA("suc", TERMO_VAR("x"), TERMO_VAR("y"))))
    existe_para_todo = EXISTE_QUANTIFICADO("y", PARA_TODO_QUANTIFICADO("x", ATOMICA("suc", TERMO_VAR("x"), TERMO_VAR("y"))))
    verificar("∀x∃y suc(x,y) — verdadeiro (facto: todo elemento tem sucessor)", b(SATISFAZ_FINITA(Esuc, para_todo_existe)), True)
    verificar("∃y∀x suc(x,y) — falso (facto: nenhum é sucessor de todos)", b(SATISFAZ_FINITA(Esuc, existe_para_todo)), False)

    # --- Etapa 353: substituição de termo por variável ---
    phi = ATOMICA("=", TERMO_VAR("x"), TERMO_CONST(1))
    phi_sub = SUBSTITUIR_LIVRE_FINITA(phi, "x", TERMO_CONST(1))
    verificar("substituição livre produz termo constante 1=1", phi_sub, ATOMICA("=", TERMO_CONST(1), TERMO_CONST(1)))
    verificar("substituição em termo simples", SUBSTITUIR_TERMO(TERMO_VAR("x"), "x", TERMO_CONST(7)), TERMO_CONST(7))
    quantificada = PARA_TODO_QUANTIFICADO("x", ATOMICA("=", TERMO_VAR("x"), TERMO_VAR("x")))
    verificar("substituição não desce em variável ligada com mesmo nome", SUBSTITUIR_LIVRE_FINITA(quantificada, "x", TERMO_CONST(9)), quantificada)

    # --- Etapa 354/355: atribuição e satisfação atômica ---
    verificar("atribuição atualizada não muta original", ATUALIZAR_ATRIBUICAO({"x": 1}, "y", 2), {"x": 1, "y": 2})
    at_teste = ATRIBUICAO_FINITA({"x": 0, "y": 1})
    verificar("satisfaz suc(0,1) em Esuc", b(SATISFAZ_ATOMICA_FINITA(Esuc, ATOMICA("suc", TERMO_VAR("x"), TERMO_VAR("y")), at_teste)), True)
    verificar("não satisfaz suc(1,0) em Esuc", b(SATISFAZ_ATOMICA_FINITA(Esuc, ATOMICA("suc", TERMO_VAR("y"), TERMO_VAR("x")), at_teste)), False)

    # --- Etapa 359: modelo finito — axiomas de grupo de Z_3 (FACTO INDEPENDENTE) ---
    e0 = TERMO_CONST(0)
    associatividade = PARA_TODO_QUANTIFICADO("x", PARA_TODO_QUANTIFICADO("y", PARA_TODO_QUANTIFICADO("z",
        ATOMICA("=", soma(soma(x, y), z), soma(x, soma(y, z))))))
    identidade = PARA_TODO_QUANTIFICADO("x", E_FORMULA(
        ATOMICA("=", soma(x, e0), x), ATOMICA("=", soma(e0, x), x)))
    inverso = PARA_TODO_QUANTIFICADO("x", EXISTE_QUANTIFICADO("y", ATOMICA("=", soma(x, y), e0)))
    verificar("Z3 satisfaz associatividade", b(SATISFAZ_FINITA(Ez3, associatividade)), True)
    verificar("Z3 satisfaz elemento neutro 0", b(SATISFAZ_FINITA(Ez3, identidade)), True)
    verificar("Z3 satisfaz existência de inverso", b(SATISFAZ_FINITA(Ez3, inverso)), True)
    verificar("Z3 é modelo dos 3 axiomas de grupo", b(EH_MODELO_FINITO(Ez3, (associatividade, identidade, inverso))), True)

    # Contraexemplo: domínio SEM identidade (tabela sem elemento neutro real)
    D2 = (0, 1)
    soma_sem_neutro = {(0, 0): 1, (0, 1): 0, (1, 0): 0, (1, 1): 1}
    E_sem_grupo = ESTRUTURA_FINITA(D2, {"=": IGUALDADE_DIAGONAL_FINITA(D2)}, {"+": soma_sem_neutro})
    identidade_d2 = PARA_TODO_QUANTIFICADO("x", E_FORMULA(
        ATOMICA("=", soma(x, e0), x), ATOMICA("=", soma(e0, x), x)))
    verificar("tabela sem neutro não satisfaz axioma de identidade", b(SATISFAZ_FINITA(E_sem_grupo, identidade_d2)), False)

    # --- Etapa 360: validade sobre amostra finita de estruturas ---
    verificar("associatividade de Z3 válida sobre {Z3}", b(VALIDA_SOBRE_ESTRUTURAS_FINITA(associatividade, (Ez3,))), True)
    verificar("identidade não é válida sobre {Z3, estrutura sem neutro}", b(VALIDA_SOBRE_ESTRUTURAS_FINITA(identidade, (Ez3, E_sem_grupo))), False)
    verificar("fechamento lógica de predicados até 360", b(FECHAMENTO_LOGICA_PREDICADOS_ATE_360()), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
