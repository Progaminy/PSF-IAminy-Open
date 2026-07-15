"""PSF-IAminy — Coloração de Arestas, Etapa 1069.
Roda com: python3 testes/test_grafos_coloracao_arestas.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.primitivas import PAR
from nucleo.traducao import de_int
from nucleo.grafos_coloracao_arestas import (
    ARESTAS_NAO_DIRIGIDAS_PURA, COLORACAO_ARESTAS_VALIDA_PURA,
    EXISTE_COLORACAO_ARESTAS_PURA,
)

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def _v(n):
    return de_int(n)


def _simetrico(pares):
    arestas = []
    for a, b in pares:
        arestas.append(PAR(_v(a))(_v(b)))
        arestas.append(PAR(_v(b))(_v(a)))
    return tuple(arestas)


def main():
    print("PSF-IAminy — Coloração de Arestas, Etapa 1069")

    print("\n[arestas não-dirigidas] cada par {a,b} conta uma vez, não duas")
    a_k3 = _simetrico([(0, 1), (0, 2), (1, 2)])
    unicas = ARESTAS_NAO_DIRIGIDAS_PURA(a_k3)
    verificar("K3 tem 3 arestas não-dirigidas (não 6)", len(unicas), 3)

    print("\n[K3, triângulo] cada par de arestas compartilha vértice -- precisa de 3 cores")
    verificar("K3 NÃO é 1-colorível em arestas", EXISTE_COLORACAO_ARESTAS_PURA(a_k3, 1), False)
    verificar("K3 NÃO é 2-colorível em arestas", EXISTE_COLORACAO_ARESTAS_PURA(a_k3, 2), False)
    verificar("K3 é 3-colorível em arestas", EXISTE_COLORACAO_ARESTAS_PURA(a_k3, 3), True)

    print("\n[C4, ciclo de 4] bipartido -- 2 cores bastam (König)")
    a_c4 = _simetrico([(0, 1), (1, 2), (2, 3), (3, 0)])
    verificar("C4 é 2-colorível em arestas", EXISTE_COLORACAO_ARESTAS_PURA(a_c4, 2), True)
    verificar("C4 NÃO é 1-colorível em arestas (arestas adjacentes existem)", EXISTE_COLORACAO_ARESTAS_PURA(a_c4, 1), False)

    print("\n[caminho de 2 arestas] 0-1-2 -- as duas arestas compartilham o vértice 1")
    a_caminho = _simetrico([(0, 1), (1, 2)])
    verificar("caminho NÃO é 1-colorível (arestas adjacentes no vértice 1)", EXISTE_COLORACAO_ARESTAS_PURA(a_caminho, 1), False)
    verificar("caminho é 2-colorível", EXISTE_COLORACAO_ARESTAS_PURA(a_caminho, 2), True)

    print("\n[coloração explícita] confere validade direta, não só existência")
    unicas_c4 = ARESTAS_NAO_DIRIGIDAS_PURA(a_c4)
    cores_alternadas = {(0, 1): 0, (1, 2): 1, (2, 3): 0, (0, 3): 1}
    verificar("coloração alternada de C4 (opostas mesma cor) é válida", COLORACAO_ARESTAS_VALIDA_PURA(unicas_c4, cores_alternadas), True)
    cores_invalidas = {(0, 1): 0, (1, 2): 0, (2, 3): 1, (0, 3): 1}
    verificar("duas arestas adjacentes com mesma cor é inválido", COLORACAO_ARESTAS_VALIDA_PURA(unicas_c4, cores_invalidas), False)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
