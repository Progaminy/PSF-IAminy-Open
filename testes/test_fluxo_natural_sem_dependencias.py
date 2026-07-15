"""Testes do fluxo natural PSF-IAminy após MDC puro.
Roda com: python3 testes/test_fluxo_natural_sem_dependencias.py

Este teste valida a etapa de diferença controlada e Euclides por subtração,
sem usar divisão, resto, módulo, fatoração, primalidade ou math.gcd.
"""
import ast
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.traducao import de_int, para_bool, para_int
from nucleo.diferenca_controlada import (
    DIFERENCA_DEFINIDA,
    DIFERENCA_CONTROLADA,
    DIFERENCA_POSITIVA_DEFINIDA,
    DIFERENCA_POSITIVA,
    RECONSTITUI_DIFERENCA,
    DIVISOR_COMUM_PRESERVA_DIFERENCA,
    DIVISOR_COMUM_RECOMPOE_ORIGINAL,
    DIVISOR_COMUM_EQUIVALENTE_APOS_SUBTRACAO,
)
from nucleo.euclides_subtracao_pura import (
    MDC_SUBTRACAO_DEFINIDO,
    MDC_SUBTRACAO_PURO,
    MDC_SUBTRACAO_CONFERE_COM_DEFINICAO,
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


def b(x):
    return para_bool(x)


def i(x):
    return para_int(x)


def verificar_sem_operadores_proibidos():
    """Inspeção simples: os novos módulos não podem conter /, //, % nem nomes proibidos."""
    base = os.path.join(os.path.dirname(__file__), "..", "nucleo")
    arquivos = [
        os.path.join(base, "diferenca_controlada.py"),
        os.path.join(base, "euclides_subtracao_pura.py"),
    ]
    nomes_proibidos = {"DIV", "MOD", "MMC"}
    for caminho in arquivos:
        with open(caminho, "r", encoding="utf-8") as f:
            arvore = ast.parse(f.read(), filename=caminho)
        for no in ast.walk(arvore):
            if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
                falhas.append(f"operador proibido em {os.path.basename(caminho)}")
            if isinstance(no, ast.Name) and no.id in nomes_proibidos:
                falhas.append(f"nome proibido {no.id} em {os.path.basename(caminho)}")


def main():
    print("PSF-IAminy — fluxo natural sem dependências indevidas")
    print("Etapas: diferença controlada + Euclides por subtração.")

    verificar_sem_operadores_proibidos()

    verificar("diferença definida 12-5", b(DIFERENCA_DEFINIDA(n(12))(n(5))), True)
    verificar("diferença não definida 5-12", b(DIFERENCA_DEFINIDA(n(5))(n(12))), False)
    verificar("diferença controlada 12-5", i(DIFERENCA_CONTROLADA(n(12))(n(5))), 7)
    verificar("sentinela operacional 5-12", i(DIFERENCA_CONTROLADA(n(5))(n(12))), 0)

    verificar("diferença positiva 12-5 definida", b(DIFERENCA_POSITIVA_DEFINIDA(n(12))(n(5))), True)
    verificar("diferença positiva 12-12 não definida", b(DIFERENCA_POSITIVA_DEFINIDA(n(12))(n(12))), False)
    verificar("diferença positiva 12-5", i(DIFERENCA_POSITIVA(n(12))(n(5))), 7)

    verificar("reconstitui 12-5", b(RECONSTITUI_DIFERENCA(n(12))(n(5))), True)
    verificar("reconstituição é implicação quando 5-12 não definido", b(RECONSTITUI_DIFERENCA(n(5))(n(12))), True)

    verificar(
        "divisor comum preserva diferença: 6 divide 18 e 12, então divide 6",
        b(DIVISOR_COMUM_PRESERVA_DIFERENCA(n(6))(n(18))(n(12))),
        True,
    )
    verificar(
        "divisor comum recompõe original: 6 divide 12 e 6, então divide 18",
        b(DIVISOR_COMUM_RECOMPOE_ORIGINAL(n(6))(n(18))(n(12))),
        True,
    )
    verificar(
        "divisor comum equivalente após subtração",
        b(DIVISOR_COMUM_EQUIVALENTE_APOS_SUBTRACAO(n(6))(n(18))(n(12))),
        True,
    )

    # O algoritmo por subtração é rápido nestes casos.
    # A validação contra o MDC por definição é feita separadamente em casos pequenos,
    # porque a definição pura é propositalmente lenta.
    casos_mdc = [
        (12, 18, 6),
        (18, 12, 6),
        (14, 21, 7),
        (8, 15, 1),
        (12, 0, 12),
        (0, 18, 18),
        (9, 9, 9),
    ]
    for a, c, esperado in casos_mdc:
        verificar(f"MDC_SUBTRACAO({a},{c})", i(MDC_SUBTRACAO_PURO(n(a))(n(c))), esperado)

    casos_conferencia_definicao = [
        (4, 6),
        (6, 9),
        (5, 0),
        (0, 7),
        (5, 5),
        (8, 12),
    ]
    for a, c in casos_conferencia_definicao:
        verificar(
            f"MDC_SUBTRACAO confere com definição ({a},{c})",
            b(MDC_SUBTRACAO_CONFERE_COM_DEFINICAO(n(a))(n(c))),
            True,
        )

    verificar("MDC_SUBTRACAO definido (0,0)", b(MDC_SUBTRACAO_DEFINIDO(n(0))(n(0))), False)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
