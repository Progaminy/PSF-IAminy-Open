"""PSF-IAminy — Eliminação Gaussiana e Sistemas Lineares, Etapas 108 a 110.
Roda com: python3 testes/test_eliminacao_gaussiana_finita.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.aritmetica import SOMA, MULT, MOD, SUB
from nucleo.traducao import de_int, para_int
from nucleo.eliminacao_gaussiana_finita import POSTO_PURO, RESOLVER_SISTEMA_PURO
from motor.fluxo import relatorio_fluxo

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def main():
    print("PSF-IAminy — Eliminação Gaussiana e Sistemas Lineares, Etapas 108 a 110")

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 110", r["maior_etapa"] >= 110, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    CINCO = de_int(5)
    ZERO, UM = de_int(0), de_int(1)
    SOMA5 = lambda a: lambda b: MOD(SOMA(a)(b))(CINCO)
    MULT5 = lambda a: lambda b: MOD(MULT(a)(b))(CINCO)
    SUB5 = lambda a: lambda b: MOD(SOMA(a)(SUB(CINCO)(b)))(CINCO)
    dominio5 = [de_int(i) for i in range(5)]

    print("\n[Etapa 108-110] Sobre Z/5Z")
    A = ((de_int(1), de_int(1)), (de_int(2), de_int(3)))
    b = (de_int(3), de_int(1))
    sol = RESOLVER_SISTEMA_PURO(A, b, dominio5, SOMA5, SUB5, MULT5, ZERO, UM)
    verificar("resolve x+y=3, 2x+3y=1 (mod5) -> (3,0)", [para_int(s) for s in sol], [3, 0])

    A_imp = ((de_int(1), de_int(1)), (de_int(1), de_int(1)))
    b_imp = (de_int(1), de_int(2))
    verificar("sistema impossível devolve None", RESOLVER_SISTEMA_PURO(A_imp, b_imp, dominio5, SOMA5, SUB5, MULT5, ZERO, UM), None)

    I3 = ((UM, ZERO, ZERO), (ZERO, UM, ZERO), (ZERO, ZERO, UM))
    verificar("posto(identidade 3×3) = 3", POSTO_PURO(I3, dominio5, SOMA5, SUB5, MULT5, ZERO, UM), 3)

    M_dep = ((UM, ZERO, ZERO), (ZERO, UM, ZERO), (UM, UM, ZERO))
    verificar("posto(linha 3 = linha1+linha2) = 2", POSTO_PURO(M_dep, dominio5, SOMA5, SUB5, MULT5, ZERO, UM), 2)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
