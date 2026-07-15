"""PSF-IAminy — Expressões Simbólicas e Equações de Primeiro Grau, Etapas 131 a 133.
Roda com: python3 testes/test_expressoes_simbolicas_finitas.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.aritmetica import SOMA, MULT, MOD, SUB, POT
from nucleo.traducao import de_int, para_int
from nucleo.expressoes_simbolicas_finitas import (
    CONST, VAR, SOMA_EXPR, MULT_EXPR, POT_EXPR,
    AVALIAR_EXPRESSAO_PURA, RESOLVER_LINEAR_FORMULA_PURA, RESOLVER_EXPRESSAO_POR_BUSCA_PURA,
)
from motor.fluxo import relatorio_fluxo

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def main():
    print("PSF-IAminy — Expressões Simbólicas e Equações de Primeiro Grau, Etapas 131 a 133")

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 133", r["maior_etapa"] >= 133, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    CINCO, UM = de_int(5), de_int(1)
    SOMA5 = lambda a: lambda b: MOD(SOMA(a)(b))(CINCO)
    MULT5 = lambda a: lambda b: MOD(MULT(a)(b))(CINCO)
    SUB5 = lambda a: lambda b: MOD(SOMA(a)(SUB(CINCO)(b)))(CINCO)
    POT5 = lambda a: lambda n: MOD(POT(a)(n))(CINCO)
    dominio5 = [de_int(i) for i in range(5)]

    print("\n[Etapa 131-132] Expressão 3x+2, avaliada sobre Z/5Z")
    expr = SOMA_EXPR(MULT_EXPR(CONST(de_int(3)))(VAR))(CONST(de_int(2)))
    valores = [para_int(AVALIAR_EXPRESSAO_PURA(expr, de_int(x), SOMA5, SUB5, MULT5, POT5)) for x in range(5)]
    verificar("(3x+2) mod5 para x=0..4", valores, [2, 0, 3, 1, 4])

    print("\n[Etapa 133] Equação 3x+2=1 (mod5) — fórmula fechada vs. busca exaustiva")
    a, b, c = de_int(3), de_int(2), de_int(1)
    sol_formula = RESOLVER_LINEAR_FORMULA_PURA(a, b, c, dominio5, SOMA5, SUB5, MULT5, UM)
    sol_busca = RESOLVER_EXPRESSAO_POR_BUSCA_PURA(expr, c, dominio5, SOMA5, SUB5, MULT5, POT5)
    verificar("fórmula fechada dá x=3", para_int(sol_formula), 3)
    verificar("busca exaustiva concorda com a fórmula", para_int(sol_busca), para_int(sol_formula))
    verificar("substituindo x=3 de volta: 3·3+2 mod5", para_int(AVALIAR_EXPRESSAO_PURA(expr, sol_formula, SOMA5, SUB5, MULT5, POT5)), 1)

    print("\n[Cross-check] x²+1=0 sobre Z/5Z deve concordar com as raízes já achadas na etapa 103 ({2,3})")
    expr_quad = SOMA_EXPR(POT_EXPR(VAR)(2))(CONST(de_int(1)))
    todas_solucoes = sorted(x for x in range(5) if para_int(AVALIAR_EXPRESSAO_PURA(expr_quad, de_int(x), SOMA5, SUB5, MULT5, POT5)) == 0)
    verificar("raízes de x²+1=0 mod5 via expressão simbólica", todas_solucoes, [2, 3])

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
