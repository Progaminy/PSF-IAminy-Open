"""PSF-IAminy — Binário posicional finito, Etapa 134.
Roda com: python3 testes/test_binario_posicional_finito.py
"""
import ast
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.fluxo import relatorio_fluxo
from nucleo.traducao import de_int, para_bits, para_bool, para_int
from nucleo.binario import (
    DE_BINARIO,
    PARA_BINARIO,
    SOMA_BINARIA,
    SOMA_BINARIA_CONFERE,
    SOMA_NATURAL_BINARIA,
)

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def n(x):
    return de_int(x)


def verificar_pureza_binaria():
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "binario.py")
    with open(caminho, "r", encoding="utf-8") as f:
        arvore = ast.parse(f.read(), filename=caminho)
    importados_proibidos = {"DIV", "MOD", "MDC", "MMC"}
    modulos_proibidos = {"primos", "divisores"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em binario.py")
        if isinstance(no, ast.ImportFrom):
            modulo = (no.module or "").split(".")[-1]
            if modulo in modulos_proibidos:
                falhas.append(f"módulo proibido {no.module}")
            for alias in no.names:
                if alias.name in importados_proibidos:
                    falhas.append(f"import proibido {alias.name}")


def main():
    print("PSF-IAminy — binário posicional finito, Etapa 134")
    verificar_pureza_binaria()

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 134", r["maior_etapa"] >= 134, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    verificar("5 + 9 em binário", para_bits(SOMA_NATURAL_BINARIA(n(5))(n(9))), "0b0000001110")
    verificar("5 + 9 reconstrói 14", para_int(DE_BINARIO(SOMA_NATURAL_BINARIA(n(5))(n(9)))), 14)
    verificar("1023 + 1 tem overflow para zero", para_int(DE_BINARIO(SOMA_NATURAL_BINARIA(n(1023))(n(1)))), 0)
    verificar("900 + 200 = 1100 ≡ 76 mod 1024", para_int(DE_BINARIO(SOMA_NATURAL_BINARIA(n(900))(n(200)))), 76)

    binarios = {i: PARA_BINARIO(n(i)) for i in range(32)}
    exaustivo_ok = True
    for a in range(32):
        for b in range(32):
            obtido = para_int(DE_BINARIO(SOMA_BINARIA(binarios[a])(binarios[b])))
            esperado = a + b
            if obtido != esperado:
                falhas.append(f"soma exaustiva 0..31 falhou em {a}+{b}: {obtido} != {esperado}")
                exaustivo_ok = False
                break
        if not exaustivo_ok:
            break
    verificar("soma exaustiva em [0,31]x[0,31]", exaustivo_ok, True)

    for a, b in [(0, 0), (3, 4), (15, 17), (31, 31), (255, 1), (700, 500)]:
        verificar(
            f"SOMA_BINARIA_CONFERE({a},{b})",
            para_bool(SOMA_BINARIA_CONFERE(PARA_BINARIO(n(a)))(PARA_BINARIO(n(b)))),
            True,
        )

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
