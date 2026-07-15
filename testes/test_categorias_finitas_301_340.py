"""PSF-IAminy — Categorias finitas, Etapas 301 a 340.
Roda com: python3 testes/test_categorias_finitas_301_340.py
"""
import ast
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.fluxo import relatorio_fluxo
from nucleo.traducao import para_bool
from nucleo.categorias_finitas import (
    ALVO_DE,
    AUTOMORFISMOS_FINITO,
    AUDITORIA_CATEGORICA_FINITA,
    CATEGORIA_FINITA,
    CATEGORIA_DISCRETA_FINITA,
    CATEGORIA_FUNCTORES_FINITA_INICIAL,
    CATEGORIA_MONOIDE_UM_OBJETO,
    CATEGORIA_OPOSTA_FINITA,
    CATEGORIA_PREORDEM_FINITA,
    COCONE_FINITO,
    COMPOR,
    COMPOR_FUNCTORES_FINITO,
    CONE_FINITO,
    COPRODUTOS_BINARIOS_FINITO,
    DIAGRAMA_FINITO,
    EH_CATEGORIA_FINITA,
    EH_COCONE_FINITO,
    EH_CONE_FINITO,
    EH_FUNCTOR_FINITO,
    EH_SUBCATEGORIA_FINITA,
    EH_TRANSFORMACAO_NATURAL_FINITA,
    EQUIVALENCIA_FINITA_INICIAL,
    FECHAMENTO_CATEGORIAS_FINITAS_ATE_340,
    FUNCTOR_FINITO,
    FUNCTOR_IDENTIDADE_FINITO,
    HOM_FINITO,
    ISOMORFISMOS_FINITO,
    OBJETOS_ISOMORFOS_FINITO,
    OBJETOS_INICIAIS_FINITO,
    OBJETOS_TERMINAIS_FINITO,
    ORIGEM_DE,
    PRODUTOS_BINARIOS_FINITO,
    SUBCATEGORIA_FINITA,
    TRANSFORMACAO_NATURAL_FINITA,
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
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "categorias_finitas.py")
    with open(caminho, "r", encoding="utf-8") as f:
        arvore = ast.parse(f.read(), filename=caminho)
    proibidos = {"DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "DECOMPOR"}
    modulos_proibidos = {"primos", "divisores"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em categorias_finitas.py")
        if isinstance(no, ast.Name) and no.id in proibidos:
            falhas.append(f"nome proibido {no.id}")
        if isinstance(no, ast.ImportFrom):
            modulo = (no.module or "").split(".")[-1]
            if modulo in modulos_proibidos:
                falhas.append(f"módulo proibido {no.module}")


def categoria_dois_objetos():
    objetos = ("A", "B")
    morfismos = ("idA", "idB", "f", "g")
    origem = {"idA": "A", "idB": "B", "f": "A", "g": "B"}
    alvo = {"idA": "A", "idB": "B", "f": "B", "g": "A"}
    identidade = {"A": "idA", "B": "idB"}
    composicao = {
        ("idA", "idA"): "idA",
        ("idB", "idB"): "idB",
        ("f", "idA"): "f",
        ("idB", "f"): "f",
        ("g", "idB"): "g",
        ("idA", "g"): "g",
        ("g", "f"): "idA",
        ("f", "g"): "idB",
    }
    return CATEGORIA_FINITA(objetos, morfismos, origem, alvo, identidade, composicao)


def main():
    print("PSF-IAminy — Categorias finitas, Etapas 301 a 340")
    verificar_pureza()

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 340", r["maior_etapa"] >= 340, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    C = categoria_dois_objetos()
    verificar("categoria finita válida", b(EH_CATEGORIA_FINITA(C)), True)
    verificar("origem de f", ORIGEM_DE(C, "f"), "A")
    verificar("alvo de f", ALVO_DE(C, "f"), "B")
    verificar("composição g∘f", COMPOR(C, "g", "f"), "idA")
    verificar("hom(A,B)", HOM_FINITO(C, "A", "B"), ("f",))
    verificar("isomorfismos A->B", ISOMORFISMOS_FINITO(C, "A", "B"), ("f",))
    verificar("objetos isomorfos", b(OBJETOS_ISOMORFOS_FINITO(C, "A", "B")), True)
    verificar("automorfismos de A", AUTOMORFISMOS_FINITO(C, "A"), ("idA",))
    verificar("objetos terminais na groupoide pequena", OBJETOS_TERMINAIS_FINITO(C), ("A", "B"))
    verificar("objetos iniciais na groupoide pequena", OBJETOS_INICIAIS_FINITO(C), ("A", "B"))
    verificar("produto binário A×A existe por busca", bool(PRODUTOS_BINARIOS_FINITO(C, "A", "A")), True)
    verificar("coproduto binário A+A existe por busca", bool(COPRODUTOS_BINARIOS_FINITO(C, "A", "A")), True)

    sub = SUBCATEGORIA_FINITA(C, ("A",), ("idA",))
    verificar("subcategoria unitária", b(EH_SUBCATEGORIA_FINITA(C, sub)), True)

    Cop = CATEGORIA_OPOSTA_FINITA(C)
    verificar("categoria oposta válida", b(EH_CATEGORIA_FINITA(Cop)), True)
    verificar("na oposta, origem de f vira B", ORIGEM_DE(Cop, "f"), "B")
    verificar("na oposta, alvo de f vira A", ALVO_DE(Cop, "f"), "A")

    Id = FUNCTOR_IDENTIDADE_FINITO(C)
    verificar("functor identidade", b(EH_FUNCTOR_FINITO(Id)), True)

    troca = FUNCTOR_FINITO(
        C,
        C,
        {"A": "B", "B": "A"},
        {"idA": "idB", "idB": "idA", "f": "g", "g": "f"},
    )
    verificar("functor de troca", b(EH_FUNCTOR_FINITO(troca)), True)
    verificar("compor troca com troca preserva objeto A", COMPOR_FUNCTORES_FINITO(troca, troca)["objetos"]["A"], "A")
    verificar("compor troca com troca preserva morfismo f", COMPOR_FUNCTORES_FINITO(troca, troca)["morfismos"]["f"], "f")
    verificar("troca é equivalência finita inicial", b(EQUIVALENCIA_FINITA_INICIAL(troca, troca)), True)

    eta = TRANSFORMACAO_NATURAL_FINITA(Id, troca, {"A": "f", "B": "g"})
    verificar("transformação natural Id=>troca", b(EH_TRANSFORMACAO_NATURAL_FINITA(eta)), True)

    J = CATEGORIA_DISCRETA_FINITA(("j",))
    verificar("categoria discreta de um objeto", b(EH_CATEGORIA_FINITA(J)), True)
    diag = DIAGRAMA_FINITO(J, C, {"j": "A"}, {("id", "j"): "idA"})
    verificar("diagrama como functor", b(EH_FUNCTOR_FINITO(diag)), True)
    cone = CONE_FINITO(diag, "B", {"j": "g"})
    cocone = COCONE_FINITO(diag, "B", {"j": "f"})
    verificar("cone finito", b(EH_CONE_FINITO(cone)), True)
    verificar("cocone finito", b(EH_COCONE_FINITO(cocone)), True)

    preordem = CATEGORIA_PREORDEM_FINITA((1, 2, 3), lambda a, c: a <= c)
    verificar("pré-ordem como categoria", b(EH_CATEGORIA_FINITA(preordem)), True)
    monoide = CATEGORIA_MONOIDE_UM_OBJETO(("e", "a"), lambda x, y: "e" if x == y else "a", "e")
    verificar("monoide como categoria de um objeto", b(EH_CATEGORIA_FINITA(monoide)), True)
    cat_fun = CATEGORIA_FUNCTORES_FINITA_INICIAL(C, C, (Id, troca), (eta,))
    verificar("categoria de functores inicial guarda dois functores", len(cat_fun["functores"]), 2)
    verificar("auditoria categórica finita", b(AUDITORIA_CATEGORICA_FINITA(C)), True)
    verificar("fechamento categorias até 340", b(FECHAMENTO_CATEGORIAS_FINITAS_ATE_340()), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
