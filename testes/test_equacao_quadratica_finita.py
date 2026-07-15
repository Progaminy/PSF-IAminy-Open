"""PSF-IAminy — Equação quadrática finita, Etapa 135.
Roda com: python3 testes/test_equacao_quadratica_finita.py
"""
import ast
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.fluxo import relatorio_fluxo
from nucleo.aritmetica import SOMA, SUB, MULT, MOD, POT
from nucleo.traducao import de_int, para_int
from nucleo.algebra_linear_inicial import RAIZES_EM_DOMINIO_PURA
from nucleo.expressoes_simbolicas_finitas import (
    QUADRATICA_EXPR,
    RESOLVER_QUADRATICA_FINITA_PURA,
    RESOLVER_EXPRESSAO_TODAS_SOLUCOES_PURA,
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


def valores(xs):
    return sorted(para_int(x) for x in xs)


def verificar_pureza_expressoes():
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "expressoes_simbolicas_finitas.py")
    with open(caminho, "r", encoding="utf-8") as f:
        arvore = ast.parse(f.read(), filename=caminho)
    importados_proibidos = {"DIV", "MOD", "MDC", "MMC"}
    modulos_proibidos = {"primos", "divisores"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em expressoes_simbolicas_finitas.py")
        if isinstance(no, ast.ImportFrom):
            modulo = (no.module or "").split(".")[-1]
            if modulo in modulos_proibidos:
                falhas.append(f"módulo proibido {no.module}")
            for alias in no.names:
                if alias.name in importados_proibidos:
                    falhas.append(f"import proibido {alias.name}")


def main():
    print("PSF-IAminy — equação quadrática finita, Etapa 135")
    verificar_pureza_expressoes()

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 135", r["maior_etapa"] >= 135, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    CINCO = n(5)
    ZERO = n(0)
    SOMA5 = lambda a: lambda b: MOD(SOMA(a)(b))(CINCO)
    SUB5 = lambda a: lambda b: MOD(SOMA(a)(SUB(CINCO)(b)))(CINCO)
    MULT5 = lambda a: lambda b: MOD(MULT(a)(b))(CINCO)
    POT5 = lambda a: lambda expoente: MOD(POT(a)(expoente))(CINCO)
    dominio5 = [n(i) for i in range(5)]

    verificar(
        "x²+1=0 em Z/5Z",
        valores(RESOLVER_QUADRATICA_FINITA_PURA(n(1), n(0), n(1), dominio5, SOMA5, SUB5, MULT5, POT5, ZERO)),
        [2, 3],
    )
    verificar(
        "x²+2x+1=0 em Z/5Z",
        valores(RESOLVER_QUADRATICA_FINITA_PURA(n(1), n(2), n(1), dominio5, SOMA5, SUB5, MULT5, POT5, ZERO)),
        [4],
    )
    verificar(
        "2x²+3x+1=0 em Z/5Z",
        valores(RESOLVER_QUADRATICA_FINITA_PURA(n(2), n(3), n(1), dominio5, SOMA5, SUB5, MULT5, POT5, ZERO)),
        [2, 4],
    )
    verificar(
        "x²+2=0 não tem raiz em Z/5Z",
        valores(RESOLVER_QUADRATICA_FINITA_PURA(n(1), n(0), n(2), dominio5, SOMA5, SUB5, MULT5, POT5, ZERO)),
        [],
    )
    verificar(
        "a=0 não é quadrática; volta vazia",
        valores(RESOLVER_QUADRATICA_FINITA_PURA(n(0), n(3), n(2), dominio5, SOMA5, SUB5, MULT5, POT5, ZERO)),
        [],
    )

    for a in range(1, 5):
        for b in range(5):
            for c in range(5):
                obtido = valores(RESOLVER_QUADRATICA_FINITA_PURA(n(a), n(b), n(c), dominio5, SOMA5, SUB5, MULT5, POT5, ZERO))
                esperado = [x for x in range(5) if (a * x * x + b * x + c) % 5 == 0]
                if obtido != esperado:
                    falhas.append(f"exaustivo Z/5Z falhou em {a}x²+{b}x+{c}: {obtido} != {esperado}")
                    break
            if falhas:
                break
        if falhas:
            break
    verificar("todas as quadráticas não degeneradas em Z/5Z", not falhas, True)

    expr = QUADRATICA_EXPR(n(1))(n(0))(n(1))
    raizes_expr = valores(RESOLVER_EXPRESSAO_TODAS_SOLUCOES_PURA(expr, ZERO, dominio5, SOMA5, SUB5, MULT5, POT5))
    raizes_polinomio = valores(RAIZES_EM_DOMINIO_PURA((n(1), n(0), n(1)), dominio5, SOMA5, MULT5, ZERO))
    verificar("busca por expressão concorda com raízes polinomiais da etapa 103", raizes_expr, raizes_polinomio)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
