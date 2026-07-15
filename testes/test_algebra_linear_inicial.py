"""PSF-IAminy — Polinómios e Álgebra Linear Finita Inicial, Etapas 101 a 107.
Roda com: python3 testes/test_algebra_linear_inicial.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.aritmetica import SOMA, MULT, MOD, SUB
from nucleo.traducao import de_int, para_int, para_bool
from nucleo.algebra_linear_inicial import (
    GRAU_PURO, SOMA_POLINOMIOS_PURA, MULT_POLINOMIOS_PURA, AVALIAR_POLINOMIO_PURO,
    RAIZES_EM_DOMINIO_PURA, SOMA_VETORES_PURA, ESCALAR_VEZES_VETOR_PURA,
    BASE_GERA_ESPACO_PURA, APLICAR_MATRIZ_PURA, DETERMINANTE_2X2_PURO, DETERMINANTE_3X3_PURO,
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
    print("PSF-IAminy — Polinómios e Álgebra Linear Finita Inicial, Etapas 101 a 107")

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 107", r["maior_etapa"] >= 107, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    CINCO = de_int(5)
    ZERO = de_int(0)
    SOMA5 = lambda a: lambda b: MOD(SOMA(a)(b))(CINCO)
    MULT5 = lambda a: lambda b: MOD(MULT(a)(b))(CINCO)
    SUB5 = lambda a: lambda b: MOD(SOMA(a)(SUB(CINCO)(b)))(CINCO)
    dominio5 = [de_int(i) for i in range(5)]

    print("\n[Etapa 101-102] Polinómios: grau, soma, produto — sobre Z/5Z")
    p = (de_int(1), de_int(0), de_int(1))  # x²+1
    verificar("grau(x²+1) = 2", GRAU_PURO(p, ZERO), 2)
    q = (de_int(2), de_int(3))  # 3x+2
    soma_pq = [para_int(c) for c in SOMA_POLINOMIOS_PURA(p, q, SOMA5, ZERO)]
    verificar("(x²+1)+(3x+2) = 3+3x+x²", soma_pq, [3, 3, 1])
    mult_pq = [para_int(c) for c in MULT_POLINOMIOS_PURA(p, q, SOMA5, MULT5, ZERO)]
    verificar("(x²+1)×(3x+2) = 2+3x+2x²+3x³", mult_pq, [2, 3, 2, 3])

    print("\n[Etapa 103] Raízes — x²+1 sobre Z/5Z tem raízes {2,3} (2²+1=5≡0, 3²+1=10≡0)")
    raizes = sorted(para_int(x) for x in RAIZES_EM_DOMINIO_PURA(p, dominio5, SOMA5, MULT5, ZERO))
    verificar("raízes de x²+1 em Z/5Z", raizes, [2, 3])

    print("\n[Etapa 104] Espaço vetorial finito — soma e escalar sobre Z/5Z²")
    u, v = (de_int(1), de_int(2)), (de_int(3), de_int(4))
    verificar("(1,2)+(3,4) mod5", [para_int(c) for c in SOMA_VETORES_PURA(u, v, SOMA5)], [4, 1])
    verificar("2·(1,2) mod5", [para_int(c) for c in ESCALAR_VEZES_VETOR_PURA(de_int(2), u, MULT5)], [2, 4])

    print("\n[Etapa 105] Base — {e1,e2} gera Z/5Z²  inteiro (25 vetores)")
    e1, e2 = (de_int(1), de_int(0)), (de_int(0), de_int(1))
    espaco = [(de_int(a), de_int(b)) for a in range(5) for b in range(5)]
    verificar("base canónica gera Z/5Z² inteiro", para_bool(BASE_GERA_ESPACO_PURA([e1, e2], espaco, dominio5, SOMA5, MULT5, (ZERO, ZERO))), True)
    verificar("só {e1} NÃO gera Z/5Z² inteiro", para_bool(BASE_GERA_ESPACO_PURA([e1], espaco, dominio5, SOMA5, MULT5, (ZERO, ZERO))), False)

    print("\n[Etapa 106] Matriz como aplicação linear — M·(1,2) mod5")
    M = ((de_int(1), de_int(2)), (de_int(3), de_int(4)))
    aplicado = [para_int(c) for c in APLICAR_MATRIZ_PURA(M, u, SOMA5, MULT5, ZERO)]
    verificar("M·(1,2) mod5 = (1·1+2·2, 3·1+4·2) mod5 = (5,11) mod5", aplicado, [0, 1])

    print("\n[Etapa 107] Determinante — casos independentes conhecidos, sobre Z/5Z")
    M2 = ((de_int(8), de_int(3)), (de_int(4), de_int(6)))
    verificar("det([[8,3],[4,6]]) mod5 = 36 mod5", para_int(DETERMINANTE_2X2_PURO(M2, SOMA5, MULT5, SUB5)), 36 % 5)
    M3 = ((de_int(1), de_int(2), de_int(3)), (de_int(0), de_int(1), de_int(4)), (de_int(0), de_int(1), de_int(0)))
    verificar("det(matriz 3×3) mod5 = -4 mod5 (calculado à mão)", para_int(DETERMINANTE_3X3_PURO(M3, SOMA5, MULT5, SUB5)), (-4) % 5)
    identidade3 = ((de_int(1), de_int(0), de_int(0)), (de_int(0), de_int(1), de_int(0)), (de_int(0), de_int(0), de_int(1)))
    verificar("det(identidade 3×3) = 1 (fato universal)", para_int(DETERMINANTE_3X3_PURO(identidade3, SOMA5, MULT5, SUB5)), 1)
    linha_zero = ((de_int(0), de_int(0), de_int(0)), (de_int(1), de_int(2), de_int(3)), (de_int(4), de_int(0), de_int(1)))
    verificar("det(linha de zeros) = 0 (fato universal)", para_int(DETERMINANTE_3X3_PURO(linha_zero, SOMA5, MULT5, SUB5)), 0)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
