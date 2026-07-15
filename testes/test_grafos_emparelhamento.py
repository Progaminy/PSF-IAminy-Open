"""PSF-IAminy — Emparelhamento e Teorema de Hall, Etapa 1066.
Roda com: python3 testes/test_grafos_emparelhamento.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.primitivas import PAR
from nucleo.traducao import de_int, para_int
from nucleo.grafos_emparelhamento import (
    PARTES_BIPARTIDO_PURA, EH_EMPARELHAMENTO_PURA,
    EXISTE_EMPARELHAMENTO_PERFEITO_PURA, VIZINHANCA_PURA,
    SATISFAZ_CONDICAO_HALL_PURA, TEOREMA_DE_HALL_CONFERE_PURA,
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
    print("PSF-IAminy — Emparelhamento e Teorema de Hall, Etapa 1066")

    print("\n[bipartição] grafo com emparelhamento perfeito: v0-v2, v0-v3, v1-v2")
    vertices = [_v(i) for i in range(4)]
    arestas = _simetrico([(0, 2), (0, 3), (1, 2)])
    partes = PARTES_BIPARTIDO_PURA(vertices, arestas)
    verificar("bipartição encontrada", partes is not None, True)
    grupo_a, grupo_b = partes
    grupo_a_ord = sorted(para_int(v) for v in grupo_a)
    grupo_b_ord = sorted(para_int(v) for v in grupo_b)
    verificar("grupo com v0 tem {0,1}", grupo_a_ord if 0 in grupo_a_ord else grupo_b_ord, [0, 1])
    verificar("grupo com v2 tem {2,3}", grupo_b_ord if 2 in grupo_b_ord else grupo_a_ord, [2, 3])

    print("\n[emparelhamento] arestas sem vértice repetido são emparelhamento válido")
    par_valido = (PAR(_v(0))(_v(3)), PAR(_v(1))(_v(2)))
    verificar("{0-3, 1-2} é emparelhamento (nenhum vértice repete)", EH_EMPARELHAMENTO_PURA(par_valido), True)
    par_invalido = (PAR(_v(0))(_v(2)), PAR(_v(1))(_v(2)))
    verificar("{0-2, 1-2} NÃO é emparelhamento (v2 repete)", EH_EMPARELHAMENTO_PURA(par_invalido), False)

    print("\n[Hall — caso positivo] v0-v2, v0-v3, v1-v2: cobre grupo {v0,v1}")
    grupo_a1 = tuple(v for v in vertices if para_int(v) in (0, 1))
    grupo_b1 = tuple(v for v in vertices if para_int(v) in (2, 3))
    verificar("existe emparelhamento perfeito cobrindo {v0,v1}", EXISTE_EMPARELHAMENTO_PERFEITO_PURA(grupo_a1, grupo_b1, arestas), True)
    verificar("condição de Hall vale para {v0,v1}", SATISFAZ_CONDICAO_HALL_PURA(grupo_a1, arestas), True)
    verificar("Teorema de Hall confere (caso positivo)", TEOREMA_DE_HALL_CONFERE_PURA(grupo_a1, grupo_b1, arestas), True)

    print("\n[Hall — caso negativo] v0 e v1 só se ligam a v2 (competem pelo mesmo vértice)")
    vertices2 = [_v(i) for i in range(3)]
    arestas2 = _simetrico([(0, 2), (1, 2)])
    grupo_a2 = tuple(v for v in vertices2 if para_int(v) in (0, 1))
    grupo_b2 = tuple(v for v in vertices2 if para_int(v) == 2)
    verificar("vizinhança de {v0,v1} é só {v2}", sorted(para_int(v) for v in VIZINHANCA_PURA(grupo_a2, arestas2)), [2])
    verificar("condição de Hall FALHA para {v0,v1} (|N|=1 < |S|=2)", SATISFAZ_CONDICAO_HALL_PURA(grupo_a2, arestas2), False)
    verificar("NÃO existe emparelhamento perfeito cobrindo {v0,v1}", EXISTE_EMPARELHAMENTO_PERFEITO_PURA(grupo_a2, grupo_b2, arestas2), False)
    verificar("Teorema de Hall confere (caso negativo, ambos False)", TEOREMA_DE_HALL_CONFERE_PURA(grupo_a2, grupo_b2, arestas2), True)

    print("\n[Hall — caso negativo com |A|=|B|] v0,v1 só ligam a v3; v2 liga a v4")
    vertices3 = [_v(i) for i in range(6)]
    arestas3 = _simetrico([(0, 3), (1, 3), (2, 4)])
    grupo_a3 = tuple(v for v in vertices3 if para_int(v) in (0, 1, 2))
    grupo_b3 = tuple(v for v in vertices3 if para_int(v) in (3, 4, 5))
    verificar("condição de Hall FALHA (v0,v1 competem por v3)", SATISFAZ_CONDICAO_HALL_PURA(grupo_a3, arestas3), False)
    verificar("NÃO existe emparelhamento perfeito, mesmo com |A|=|B|=3", EXISTE_EMPARELHAMENTO_PERFEITO_PURA(grupo_a3, grupo_b3, arestas3), False)
    verificar("Teorema de Hall confere (|A|=|B| mas estrutura bloqueia)", TEOREMA_DE_HALL_CONFERE_PURA(grupo_a3, grupo_b3, arestas3), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
