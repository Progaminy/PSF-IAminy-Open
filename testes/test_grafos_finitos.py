"""PSF-IAminy — Grafos Finitos, Etapas 111 a 127.
Roda com: python3 testes/test_grafos_finitos.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.primitivas import PAR
from nucleo.traducao import de_int, para_int, para_bool
from nucleo.grafos_finitos import (
    GRAFO_PURO, ARESTAS_DE, EH_GRAFO_NAO_DIRIGIDO_PURO, GRAU_VERTICE_PURO,
    CAMINHO_PURA, CICLO_PURA, EXISTE_CAMINHO_PURA, CONEXO_PURA, ARVORE_PURA,
    BIPARTIDO_PURA, EXISTE_COLORACAO_PURA, GRAFO_COMPLETO_PURA,
    COMPLEMENTO_GRAFO_PURO, ISOMORFISMO_GRAFOS_PURA, SUBGRAFO_PURO,
    EULERIANO_PURA, HAMILTONIANO_PURA, MATRIZ_ADJACENCIA_PURA,
    PESO_CAMINHO_PURO, FECHAMENTO_GRAFOS_PURO,
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


def _simetrico(pares):
    arestas = []
    for a, b in pares:
        arestas.append(PAR(_v(a))(_v(b)))
        arestas.append(PAR(_v(b))(_v(a)))
    return tuple(arestas)


def main():
    print("PSF-IAminy — Grafos Finitos, Etapas 111 a 127")

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 127", r["maior_etapa"] >= 127, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    print("\n[111] Grafo como relação simétrica")
    v_c4 = [_v(i) for i in range(4)]
    a_c4 = _simetrico([(0, 1), (1, 2), (2, 3), (3, 0)])
    g_c4 = GRAFO_PURO(v_c4, a_c4)
    verificar("C4 é grafo não-dirigido válido (arestas simétricas)", para_bool(EH_GRAFO_NAO_DIRIGIDO_PURO(g_c4)), True)

    print("\n[112] Grau — K4 tem todo vértice com grau 3")
    v_k4 = [_v(i) for i in range(4)]
    a_k4 = _simetrico([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    verificar("graus de K4", [GRAU_VERTICE_PURO(v, a_k4) for v in v_k4], [3, 3, 3, 3])

    print("\n[113-114] Caminho e ciclo em C4")
    verificar("(0,1,2,3) é caminho em C4", para_bool(CAMINHO_PURA([_v(0), _v(1), _v(2), _v(3)], a_c4)), True)
    verificar("(0,1,2,3,0) é ciclo em C4", para_bool(CICLO_PURA([_v(0), _v(1), _v(2), _v(3), _v(0)], a_c4)), True)

    print("\n[115-116] Conectividade e árvore")
    verificar("C4 é conexo", para_bool(CONEXO_PURA(v_c4, a_c4)), True)
    v_estrela = [_v(i) for i in range(4)]
    a_estrela = _simetrico([(0, 1), (0, 2), (0, 3)])
    verificar("estrela (3 arestas, 4 vértices, conexa) é árvore", para_bool(ARVORE_PURA(v_estrela, a_estrela)), True)
    verificar("K4 (6 arestas) NÃO é árvore", para_bool(ARVORE_PURA(v_k4, a_k4)), False)

    print("\n[117-118] Bipartido e coloração — C4 bipartido; K3 precisa de 3 cores")
    verificar("C4 é bipartido", para_bool(BIPARTIDO_PURA(v_c4, a_c4)), True)
    v_k3 = [_v(i) for i in range(3)]
    a_k3 = _simetrico([(0, 1), (0, 2), (1, 2)])
    verificar("K3 NÃO é bipartido", para_bool(BIPARTIDO_PURA(v_k3, a_k3)), False)
    verificar("K3 não é 2-colorível", para_bool(EXISTE_COLORACAO_PURA(v_k3, a_k3, 2)), False)
    verificar("K3 é 3-colorível", para_bool(EXISTE_COLORACAO_PURA(v_k3, a_k3, 3)), True)

    print("\n[119-120] Completo e complemento")
    verificar("K4 é completo", para_bool(GRAFO_COMPLETO_PURA(v_k4, a_k4)), True)
    complemento_k4 = COMPLEMENTO_GRAFO_PURO(v_k4, a_k4)
    verificar("complemento de K4 não tem arestas", len(ARESTAS_DE(complemento_k4)), 0)

    print("\n[121-122] Isomorfismo e subgrafo")
    bijecao_id = {i: _v(i) for i in range(4)}
    verificar("C4 isomorfo a si mesmo (identidade)", para_bool(ISOMORFISMO_GRAFOS_PURA(v_c4, a_c4, v_c4, a_c4, bijecao_id)), True)
    verificar("K3 é subgrafo de K4", para_bool(SUBGRAFO_PURO(v_k3, a_k3, v_k4, a_k4)), True)

    print("\n[123] Euleriano — Teorema de Euler (1736), Pontes de Königsberg")
    v_konigsberg = [_v(i) for i in range(4)]
    arestas_konigsberg = []
    for (a, b, vezes) in [(0, 1, 2), (0, 2, 2), (0, 3, 1), (1, 3, 1), (2, 3, 1)]:
        for _ in range(vezes):
            arestas_konigsberg.append(PAR(_v(a))(_v(b)))
            arestas_konigsberg.append(PAR(_v(b))(_v(a)))
    arestas_konigsberg = tuple(arestas_konigsberg)
    verificar("graus de Königsberg = [5,3,3,3] (todos ímpares)", [GRAU_VERTICE_PURO(v, arestas_konigsberg) for v in v_konigsberg], [5, 3, 3, 3])
    verificar("Königsberg NÃO é Euleriano (Euler, 1736)", para_bool(EULERIANO_PURA(v_konigsberg, arestas_konigsberg)), False)
    verificar("C4 (todos graus pares) É Euleriano", para_bool(EULERIANO_PURA(v_c4, a_c4)), True)

    print("\n[124] Hamiltoniano — K4 sempre tem; C4 tem (é o próprio ciclo)")
    verificar("K4 é Hamiltoniano", para_bool(HAMILTONIANO_PURA(v_k4, a_k4)), True)
    verificar("C4 é Hamiltoniano", para_bool(HAMILTONIANO_PURA(v_c4, a_c4)), True)

    print("\n[125] Matriz de adjacência de C4")
    M = MATRIZ_ADJACENCIA_PURA(v_c4, a_c4)
    matriz_valores = [[para_int(x) for x in linha] for linha in M]
    verificar("matriz de adjacência de C4", matriz_valores, [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])

    print("\n[126] Peso de caminho")
    pesos = {(0, 1): _v(5), (1, 2): _v(3), (2, 3): _v(7)}
    peso_total = PESO_CAMINHO_PURO([_v(0), _v(1), _v(2), _v(3)], pesos)
    verificar("peso do caminho 0-1-2-3 = 5+3+7", para_int(peso_total), 15)

    print("\n[127] Fechamento de grafos")
    verificar("fechamento de C4", para_bool(FECHAMENTO_GRAFOS_PURO(v_c4, a_c4)), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
