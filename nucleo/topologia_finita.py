"""Topologia finita — etapas 881-920."""
from __future__ import annotations


def partes(cj):
    itens = list(cj)
    saida = [frozenset()]
    for x in itens:
        saida += [s | {x} for s in list(saida)]
    return set(saida)


def eh_topologia_finita(universo, abertos):
    U = frozenset(universo)
    A = {frozenset(a) for a in abertos}
    if frozenset() not in A or U not in A:
        return False
    lista = list(A)
    for a in lista:
        for b in lista:
            if (a | b) not in A:
                return False
            if (a & b) not in A:
                return False
    return True


def fechado(universo, aberto):
    return frozenset(universo) - frozenset(aberto)


def interior(subconjunto, abertos):
    S = frozenset(subconjunto)
    total = frozenset()
    for a in abertos:
        a = frozenset(a)
        if a <= S:
            total |= a
    return total


def fecho(universo, subconjunto, abertos):
    S = frozenset(subconjunto)
    fechados = [fechado(universo, a) for a in abertos]
    candidatos = [f for f in fechados if S <= f]
    if not candidatos:
        return frozenset(universo)
    atual = candidatos[0]
    for f in candidatos[1:]:
        atual &= f
    return atual


def preimagem(funcao, alvo):
    return frozenset(x for x, y in funcao.items() if y in alvo)


def continua_finita(funcao, abertos_origem, abertos_destino):
    Aorig = {frozenset(a) for a in abertos_origem}
    for aberto in abertos_destino:
        if preimagem(funcao, aberto) not in Aorig:
            return False
    return True
