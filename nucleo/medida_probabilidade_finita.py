"""Medida e probabilidade finita — etapas 921-960."""
from __future__ import annotations


def medida(subconjunto, pesos):
    total = 0
    for x in subconjunto:
        total += pesos.get(x, 0)
    return total


def disjuntos(a, b):
    return len(set(a) & set(b)) == 0


def aditividade_disjunta(a, b, pesos):
    if not disjuntos(a, b):
        return False
    return medida(set(a) | set(b), pesos) == medida(a, pesos) + medida(b, pesos)


def probabilidade_como_par(evento, universo, pesos=None):
    if pesos is None:
        pesos = {x: 1 for x in universo}
    return (medida(evento, pesos), medida(universo, pesos))


def condicional_como_par(a, b, universo, pesos=None):
    if pesos is None:
        pesos = {x: 1 for x in universo}
    inter = set(a) & set(b)
    return (medida(inter, pesos), medida(b, pesos))


def independentes_por_produto_cruzado(a, b, universo, pesos=None):
    if pesos is None:
        pesos = {x: 1 for x in universo}
    ma = medida(a, pesos)
    mb = medida(b, pesos)
    mi = medida(set(a) & set(b), pesos)
    mt = medida(universo, pesos)
    return mi * mt == ma * mb


def distribuicao_variavel(universo, variavel, pesos=None):
    if pesos is None:
        pesos = {x: 1 for x in universo}
    dist = {}
    for x in universo:
        v = variavel(x)
        dist[v] = dist.get(v, 0) + pesos.get(x, 0)
    return dist
