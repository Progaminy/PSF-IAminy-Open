"""PSF-IAminy — Teorema de Ramsey R(3,3)=6, Etapa 1070.
Roda com: python3 testes/test_ramsey_33.py
"""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.ramsey_33 import (
    GRAFO_COMPLETO_ARESTAS_PURA,
    EXISTE_COLORACAO_SEM_TRIANGULO_MONOCROMATICO_PURA,
    RAMSEY_3_3_CONFERE_PURA,
)

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def main():
    print("PSF-IAminy — Teorema de Ramsey R(3,3)=6, Etapa 1070")

    print("\n[K5] 10 arestas -- existe um contraexemplo real (5 é pequeno demais)")
    t0 = time.time()
    k5_tem_contraexemplo = EXISTE_COLORACAO_SEM_TRIANGULO_MONOCROMATICO_PURA(5, 2)
    t_k5 = time.time() - t0
    verificar("K5 admite 2-coloração sem triângulo monocromático", k5_tem_contraexemplo, True)
    verificar("K5 roda em tempo curto (< 5s)", t_k5 < 5, True)

    print("\n[K6] 15 arestas -- NENHUMA coloração escapa de um triângulo monocromático")
    t0 = time.time()
    k6_tem_contraexemplo = EXISTE_COLORACAO_SEM_TRIANGULO_MONOCROMATICO_PURA(6, 2)
    t_k6 = time.time() - t0
    verificar("K6 NÃO admite 2-coloração sem triângulo monocromático", k6_tem_contraexemplo, False)
    verificar("K6 roda em tempo curto (< 30s)", t_k6 < 30, True)

    print("\n[K4] grafo ainda menor -- também deve ter contraexemplo (folga extra)")
    verificar("K4 admite 2-coloração sem triângulo monocromático", EXISTE_COLORACAO_SEM_TRIANGULO_MONOCROMATICO_PURA(4, 2), True)

    print("\n[fechamento] R(3,3)=6 confirmado numa instância só")
    verificar("RAMSEY_3_3_CONFERE_PURA()", RAMSEY_3_3_CONFERE_PURA(), True)

    print("\n[estrutura] K6 tem 15 arestas não-dirigidas, K5 tem 10")
    verificar("|arestas(K6)| = 15 (C(6,2), cada par uma vez)", len(GRAFO_COMPLETO_ARESTAS_PURA(6)), 15)
    verificar("|arestas(K5)| = 10", len(GRAFO_COMPLETO_ARESTAS_PURA(5)), 10)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print(f"\nTudo passou. (K5: {t_k5:.3f}s, K6: {t_k6:.3f}s)")


if __name__ == "__main__":
    main()
