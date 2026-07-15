"""Testes da continuação natural PSF-IAminy.
Roda com: python3 testes/test_primalidade_fatoracao_pura.py

Etapas validadas:
- primalidade sem fatoração prévia;
- composto como existência de divisor interno;
- menor fator por busca;
- fatoração pura usando quociente já construído;
- crivo por enumeração.
"""
import ast
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.traducao import de_int, para_bool, para_int, para_lista
from nucleo.primalidade_pura import (
    DIVIDE_POR_RESTO_PURO,
    DIVISOR_INTERNO_PURO,
    POSSUI_DIVISOR_INTERNO_PURO,
    PRIMO_PURO,
    COMPOSTO_PURO,
    MENOR_FATOR_PURO,
    CRIVO_ENUMERACAO_PURO,
    QTD_PRIMOS_ATE_PURO,
)
from nucleo.fatoracao_pura import FATORACAO_PURA

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def n(x):
    return de_int(x)


def b(x):
    return para_bool(x)


def i(x):
    return para_int(x)


def lista(x):
    return para_lista(x)


def verificar_sem_dependencias_indevidas():
    base = os.path.join(os.path.dirname(__file__), "..", "nucleo")
    arquivos = [
        os.path.join(base, "primalidade_pura.py"),
        os.path.join(base, "fatoracao_pura.py"),
    ]
    nomes_importados_proibidos = {"DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "FATORES", "DECOMPOR"}
    modulos_proibidos = {"primos"}
    for caminho in arquivos:
        with open(caminho, "r", encoding="utf-8") as f:
            fonte = f.read()
        arvore = ast.parse(fonte, filename=caminho)
        for no in ast.walk(arvore):
            if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
                falhas.append(f"operador nativo proibido em {os.path.basename(caminho)}")
            if isinstance(no, ast.ImportFrom):
                modulo = (no.module or "").split(".")[-1]
                if modulo in modulos_proibidos:
                    falhas.append(f"módulo proibido {no.module} em {os.path.basename(caminho)}")
                for alias in no.names:
                    if alias.name in nomes_importados_proibidos:
                        falhas.append(f"import proibido {alias.name} em {os.path.basename(caminho)}")


def main():
    print("PSF-IAminy — primalidade, fatoração e crivo puros")
    verificar_sem_dependencias_indevidas()

    casos_primo = {
        0: False, 1: False, 2: True, 3: True, 4: False,
        5: True, 6: False, 7: True, 8: False, 9: False,
        10: False, 11: True, 12: False, 13: True, 15: False,
    }
    for x, esperado in casos_primo.items():
        verificar(f"PRIMO_PURO({x})", b(PRIMO_PURO(n(x))), esperado)

    casos_composto = {
        0: False, 1: False, 2: False, 3: False, 4: True,
        5: False, 6: True, 8: True, 9: True, 10: True,
        11: False, 12: True, 13: False, 15: True,
    }
    for x, esperado in casos_composto.items():
        verificar(f"COMPOSTO_PURO({x})", b(COMPOSTO_PURO(n(x))), esperado)

    verificar("divide por resto puro 3 | 12", b(DIVIDE_POR_RESTO_PURO(n(3))(n(12))), True)
    verificar("divide por resto puro 5 não | 12", b(DIVIDE_POR_RESTO_PURO(n(5))(n(12))), False)
    verificar("divisor interno 3 em 12", b(DIVISOR_INTERNO_PURO(n(3))(n(12))), True)
    verificar("divisor interno 12 em 12 é falso", b(DIVISOR_INTERNO_PURO(n(12))(n(12))), False)
    verificar("possui divisor interno 29", b(POSSUI_DIVISOR_INTERNO_PURO(n(29))), False)
    verificar("possui divisor interno 30", b(POSSUI_DIVISOR_INTERNO_PURO(n(30))), True)

    fatores_menores = {
        2: 2,
        3: 3,
        4: 2,
        9: 3,
        12: 2,
        15: 3,
        25: 5,
    }
    for x, esperado in fatores_menores.items():
        verificar(f"MENOR_FATOR_PURO({x})", i(MENOR_FATOR_PURO(n(x))), esperado)

    casos_fatoracao = {
        1: [],
        2: [2],
        3: [3],
        4: [2, 2],
        12: [2, 2, 3],
        18: [2, 3, 3],
        25: [5, 5],
        28: [2, 2, 7],
    }
    for x, esperado in casos_fatoracao.items():
        verificar(f"FATORACAO_PURA({x})", lista(FATORACAO_PURA(n(x))), esperado)

    primos_ate_15 = [2, 3, 5, 7, 11, 13]
    verificar("CRIVO_ENUMERACAO_PURO(15)", sorted(lista(CRIVO_ENUMERACAO_PURO(n(15)))), primos_ate_15)
    verificar("QTD_PRIMOS_ATE_PURO(15)", i(QTD_PRIMOS_ATE_PURO(n(15))), len(primos_ate_15))

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
