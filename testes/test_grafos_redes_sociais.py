"""PSF-IAminy — Centralidade de Grau e Coeficiente de Agrupamento, Etapa 1072.
Roda com: python3 testes/test_grafos_redes_sociais.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.primitivas import PAR
from nucleo.traducao import de_int
from nucleo.grafos_redes_sociais import CENTRALIDADE_GRAU_PURA, COEFICIENTE_AGRUPAMENTO_OU_NONE

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


def _fracao(r):
    return (r.numerador, r.denominador)


def main():
    print("PSF-IAminy — Centralidade de Grau e Coeficiente de Agrupamento, Etapa 1072")

    print("\n[K4] grafo completo -- centralidade e agrupamento máximos (1/1)")
    v_k4 = [_v(i) for i in range(4)]
    a_k4 = _simetrico([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    verificar("centralidade de grau de v0 em K4 é 1", _fracao(CENTRALIDADE_GRAU_PURA(_v(0), v_k4, a_k4)), (1, 1))
    verificar("coeficiente de agrupamento de v0 em K4 é 1", _fracao(COEFICIENTE_AGRUPAMENTO_OU_NONE(_v(0), a_k4)), (1, 1))

    print("\n[estrela] centro 0 ligado a 1,2,3; folhas sem ligação entre si")
    v_estrela = [_v(i) for i in range(4)]
    a_estrela = _simetrico([(0, 1), (0, 2), (0, 3)])
    verificar("centralidade de grau do centro é 1 (grau 3 = n-1)", _fracao(CENTRALIDADE_GRAU_PURA(_v(0), v_estrela, a_estrela)), (1, 1))
    verificar("agrupamento do centro é 0 (folhas não ligadas entre si)", _fracao(COEFICIENTE_AGRUPAMENTO_OU_NONE(_v(0), a_estrela)), (0, 1))
    verificar("centralidade de grau de uma folha é 1/3 (grau 1, n-1=3)", _fracao(CENTRALIDADE_GRAU_PURA(_v(1), v_estrela, a_estrela)), (1, 3))
    verificar("agrupamento de folha (grau 1) é indefinido, None", COEFICIENTE_AGRUPAMENTO_OU_NONE(_v(1), a_estrela), None)

    print("\n[triângulo aberto] 0-1, 1-2, sem 0-2 -- vértice 1 tem 2 vizinhos não ligados")
    v_aberto = [_v(i) for i in range(3)]
    a_aberto = _simetrico([(0, 1), (1, 2)])
    verificar("agrupamento de v1 (vizinhos 0,2 não ligados) é 0", _fracao(COEFICIENTE_AGRUPAMENTO_OU_NONE(_v(1), a_aberto)), (0, 1))

    print("\n[triângulo fechado] 0-1, 1-2, 0-2 -- vértice 1 tem 2 vizinhos ligados entre si")
    a_fechado = _simetrico([(0, 1), (1, 2), (0, 2)])
    verificar("agrupamento de v1 (vizinhos 0,2 ligados) é 1", _fracao(COEFICIENTE_AGRUPAMENTO_OU_NONE(_v(1), a_fechado)), (1, 1))

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
