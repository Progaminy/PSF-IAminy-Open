"""PSF-IAminy — Árvore Geradora Mínima e Caminho Mínimo, Etapas 128 a 130.
Roda com: python3 testes/test_grafos_ponderados_algoritmos.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.primitivas import PAR
from nucleo.traducao import de_int, para_int
from nucleo.grafos_ponderados_algoritmos import (
    ARVORE_GERADORA_MINIMA_PURA, CAMINHO_MINIMO_PURO, FECHAMENTO_DISCRETO_GERAL_PURO,
)
from motor.fluxo import relatorio_fluxo

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def _v(n):
    return de_int(n)


def _simetrico(triplos):
    arestas = []
    for a, b, _ in triplos:
        arestas.append(PAR(_v(a))(_v(b)))
        arestas.append(PAR(_v(b))(_v(a)))
    return tuple(arestas)


def main():
    print("PSF-IAminy — Árvore Geradora Mínima e Caminho Mínimo, Etapas 128 a 130")

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 130", r["maior_etapa"] >= 130, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    vertices = [_v(i) for i in range(4)]

    print("\n[Etapa 128] Árvore geradora mínima — Kruskal")
    lista1 = [(0, 1, 1), (0, 2, 4), (0, 3, 3), (1, 2, 2), (1, 3, 5), (2, 3, 6)]
    arestas1 = _simetrico(lista1)
    pesos1 = {(min(a, b), max(a, b)): de_int(w) for a, b, w in lista1}
    escolhidas, peso_total = ARVORE_GERADORA_MINIMA_PURA(vertices, arestas1, pesos1)
    verificar("MST tem 3 arestas (|V|-1)", len(escolhidas), 3)
    verificar("peso total da MST = 6", para_int(peso_total), 6)
    arestas_escolhidas_pares = sorted((min(para_int(a), para_int(b)), max(para_int(a), para_int(b))) for a, b in escolhidas)
    verificar("MST usa as arestas (0,1),(1,2),(0,3)", arestas_escolhidas_pares, [(0, 1), (0, 3), (1, 2)])

    print("\n[Etapa 129] Caminho mínimo — Dijkstra")
    lista2 = [(0, 1, 4), (0, 2, 1), (2, 1, 1), (1, 3, 1), (2, 3, 5)]
    arestas2 = _simetrico(lista2)
    pesos2 = {(min(a, b), max(a, b)): de_int(w) for a, b, w in lista2}
    dist01, caminho01 = CAMINHO_MINIMO_PURO(_v(0), _v(1), vertices, arestas2, pesos2)
    verificar("dist(0,1) = 2 (via 2, não 4 direto)", para_int(dist01), 2)
    verificar("caminho 0→1 passa por 2", [para_int(v) for v in caminho01], [0, 2, 1])
    dist03, _ = CAMINHO_MINIMO_PURO(_v(0), _v(3), vertices, arestas2, pesos2)
    verificar("dist(0,3) = 3", para_int(dist03), 3)

    print("\n[Etapa 130] Fechamento discreto geral")
    verificar("fechamento (grafo conexo e ponderado)", FECHAMENTO_DISCRETO_GERAL_PURO(vertices, arestas1, pesos1), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
