"""Testes da camada de pureza conceitual.
Roda com: python3 testes/test_pureza_conceitual.py
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.traducao import de_int, para_bool, para_int, para_lista
from nucleo.divisibilidade_pura import (
    DIVIDE_BRUTO,
    DIVIDE_PURO,
    LISTA_DIVISORES_PURO,
    QTD_DIVISORES_PURO,
    SOMA_DIVISORES_PURO,
    SOMA_DIVISORES_PROPRIOS_PURO,
    PERFEITO_PURO,
    ABUNDANTE_PURO,
    DEFICIENTE_PURO,
)
from nucleo.mdc_puro import MDC_DEFINIDO_PURO, MDC_PURO, COPRIMOS_PURO

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def main():
    print("PSF-IAminy — teste de pureza conceitual")
    print("Sem divisão, sem resto, sem módulo, sem primos, sem fatoração.")

    verificar("divide_bruto(0,0)", para_bool(DIVIDE_BRUTO(de_int(0))(de_int(0))), True)
    verificar("divide_puro(0,0) exclui degeneração", para_bool(DIVIDE_PURO(de_int(0))(de_int(0))), False)
    verificar("3 | 12", para_bool(DIVIDE_PURO(de_int(3))(de_int(12))), True)
    verificar("5 não divide 12", para_bool(DIVIDE_PURO(de_int(5))(de_int(12))), False)

    verificar("divisores puros de 12", sorted(para_lista(LISTA_DIVISORES_PURO(de_int(12)))), [1, 2, 3, 4, 6, 12])
    verificar("qtd divisores 12", para_int(QTD_DIVISORES_PURO(de_int(12))), 6)
    verificar("soma divisores 12", para_int(SOMA_DIVISORES_PURO(de_int(12))), 28)
    verificar("soma divisores próprios 6", para_int(SOMA_DIVISORES_PROPRIOS_PURO(de_int(6))), 6)

    verificar("6 perfeito", para_bool(PERFEITO_PURO(de_int(6))), True)
    verificar("12 abundante", para_bool(ABUNDANTE_PURO(de_int(12))), True)
    verificar("8 deficiente", para_bool(DEFICIENTE_PURO(de_int(8))), True)

    verificar("MDC definido (0,0)", para_bool(MDC_DEFINIDO_PURO(de_int(0))(de_int(0))), False)
    verificar("MDC(12,18)", para_int(MDC_PURO(de_int(12))(de_int(18))), 6)
    verificar("MDC(12,0)", para_int(MDC_PURO(de_int(12))(de_int(0))), 12)
    verificar("MDC(0,18)", para_int(MDC_PURO(de_int(0))(de_int(18))), 18)
    verificar("coprimos(8,15)", para_bool(COPRIMOS_PURO(de_int(8))(de_int(15))), True)
    verificar("coprimos(8,12)", para_bool(COPRIMOS_PURO(de_int(8))(de_int(12))), False)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
