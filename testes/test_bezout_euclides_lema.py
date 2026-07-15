"""Testes da Etapa 8 do fluxo natural PSF-IAminy.
Roda com: python3 testes/test_bezout_euclides_lema.py

Etapas validadas:
- inteiros relativos puros;
- combinação linear;
- Euclides estendido;
- identidade de Bézout;
- coprimalidade revisitada por Bézout;
- lema de Euclides como proposição verificável.
"""
import ast
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.traducao import de_int, para_bool, para_int, para_int_assinado
from nucleo.bezout_euclides_puro import (
    INTEIRO_PURO,
    ZERO_INTEIRO_PURO,
    UM_INTEIRO_PURO,
    NATURAL_COMO_INTEIRO_PURO,
    IGUAL_INTEIRO_PURO,
    OPOSTO_INTEIRO_PURO,
    SOMA_INTEIRO_PURO,
    SUB_INTEIRO_PURO,
    MULT_INTEIRO_PURO,
    MULT_INTEIRO_NATURAL_PURO,
    COMBINACAO_LINEAR_PURA,
    EUCLIDES_ESTENDIDO_PURO,
    BEZOUT_G_PURO,
    BEZOUT_X_PURO,
    BEZOUT_Y_PURO,
    MDC_ESTENDIDO_PURO,
    MDC_ESTENDIDO_CONFERE_PURO,
    BEZOUT_CONFERE_PURO,
    COPRIMOS_BEZOUT_CONFERE_PURO,
    LEMA_EUCLIDES_PURO,
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


def i(x):
    return para_int(x)


def z(x):
    return para_int_assinado(x)


def b(x):
    return para_bool(x)


def int_puro(valor):
    if valor >= 0:
        return INTEIRO_PURO(n(valor))(n(0))
    return INTEIRO_PURO(n(0))(n(-valor))


def verificar_sem_dependencias_indevidas():
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "bezout_euclides_puro.py")
    with open(caminho, "r", encoding="utf-8") as f:
        fonte = f.read()
    arvore = ast.parse(fonte, filename=caminho)
    nomes_importados_proibidos = {"DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "FATORES", "DECOMPOR"}
    modulos_proibidos = {"primos", "inteiros"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em bezout_euclides_puro.py")
        if isinstance(no, ast.ImportFrom):
            modulo = (no.module or "").split(".")[-1]
            if modulo in modulos_proibidos:
                falhas.append(f"módulo proibido {no.module}")
            for alias in no.names:
                if alias.name in nomes_importados_proibidos:
                    falhas.append(f"import proibido {alias.name}")


def main():
    print("PSF-IAminy — Bézout, Euclides estendido e lema de Euclides")
    verificar_sem_dependencias_indevidas()

    menos_3 = int_puro(-3)
    cinco = int_puro(5)
    dois = int_puro(2)

    verificar("ZERO_INTEIRO_PURO", z(ZERO_INTEIRO_PURO), 0)
    verificar("UM_INTEIRO_PURO", z(UM_INTEIRO_PURO), 1)
    verificar("NATURAL_COMO_INTEIRO_PURO(7)", z(NATURAL_COMO_INTEIRO_PURO(n(7))), 7)
    verificar("OPOSTO_INTEIRO_PURO(5)", z(OPOSTO_INTEIRO_PURO(cinco)), -5)
    verificar("SOMA_INTEIRO_PURO(5,-3)", z(SOMA_INTEIRO_PURO(cinco)(menos_3)), 2)
    verificar("SUB_INTEIRO_PURO(2,5)", z(SUB_INTEIRO_PURO(dois)(cinco)), -3)
    verificar("MULT_INTEIRO_PURO(-3,5)", z(MULT_INTEIRO_PURO(menos_3)(cinco)), -15)
    verificar("MULT_INTEIRO_NATURAL_PURO(-3,4)", z(MULT_INTEIRO_NATURAL_PURO(menos_3)(n(4))), -12)
    verificar("IGUAL_INTEIRO_PURO((5,2),(3,0))", b(IGUAL_INTEIRO_PURO(INTEIRO_PURO(n(5))(n(2)))(int_puro(3))), True)

    verificar("COMBINACAO_LINEAR_PURA 30*(-2)+21*3", z(COMBINACAO_LINEAR_PURA(n(30))(n(21))(int_puro(-2))(int_puro(3))), 3)

    casos = [(30, 21, 3), (18, 12, 6), (8, 15, 1), (0, 5, 5), (7, 0, 7)]
    for a, c, mdc_esperado in casos:
        res = EUCLIDES_ESTENDIDO_PURO(n(a))(n(c))
        g = BEZOUT_G_PURO(res)
        x = BEZOUT_X_PURO(res)
        y = BEZOUT_Y_PURO(res)
        combinacao = COMBINACAO_LINEAR_PURA(n(a))(n(c))(x)(y)
        verificar(f"BEZOUT_G_PURO({a},{c})", i(g), mdc_esperado)
        verificar(f"combinação {a}*x+{c}*y", z(combinacao), mdc_esperado)
        verificar(f"MDC_ESTENDIDO_PURO({a},{c})", i(MDC_ESTENDIDO_PURO(n(a))(n(c))), mdc_esperado)
        verificar(f"MDC_ESTENDIDO_CONFERE_PURO({a},{c})", b(MDC_ESTENDIDO_CONFERE_PURO(n(a))(n(c))), True)
        verificar(f"BEZOUT_CONFERE_PURO({a},{c})", b(BEZOUT_CONFERE_PURO(n(a))(n(c))), True)

    verificar("COPRIMOS_BEZOUT_CONFERE_PURO(8,15)", b(COPRIMOS_BEZOUT_CONFERE_PURO(n(8))(n(15))), True)
    verificar("COPRIMOS_BEZOUT_CONFERE_PURO(7,13)", b(COPRIMOS_BEZOUT_CONFERE_PURO(n(7))(n(13))), True)

    casos_lema = [
        (2, 6, 7, True),    # 2 | 42 e 2 | 6
        (3, 4, 6, True),    # 3 | 24 e 3 | 6
        (5, 2, 5, True),    # 5 | 10 e 5 | 5
        (7, 2, 3, True),    # antecedente falso: 7 não divide 6
        (4, 2, 6, True),    # antecedente falso: 4 não é primo
    ]
    for p, a, c, esperado in casos_lema:
        verificar(f"LEMA_EUCLIDES_PURO({p},{a},{c})", b(LEMA_EUCLIDES_PURO(n(p))(n(a))(n(c))), esperado)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
