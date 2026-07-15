"""Otimização e modelos finitos — etapas 991-1030."""
from __future__ import annotations


def minimo_global(candidatos, objetivo):
    candidatos = list(candidatos)
    if not candidatos:
        raise ValueError("sem candidatos")
    melhor = candidatos[0]
    melhor_valor = objetivo(melhor)
    for c in candidatos[1:]:
        v = objetivo(c)
        if v < melhor_valor:
            melhor, melhor_valor = c, v
    return melhor, melhor_valor


def maximo_global(candidatos, objetivo):
    candidatos = list(candidatos)
    if not candidatos:
        raise ValueError("sem candidatos")
    melhor = candidatos[0]
    melhor_valor = objetivo(melhor)
    for c in candidatos[1:]:
        v = objetivo(c)
        if v > melhor_valor:
            melhor, melhor_valor = c, v
    return melhor, melhor_valor


def minimo_local(candidato, vizinhos, objetivo):
    valor = objetivo(candidato)
    for v in vizinhos(candidato):
        if objetivo(v) < valor:
            return False
    return True


def busca_gulosa(inicial, vizinhos, objetivo, limite=100):
    atual = inicial
    for _ in range(limite):
        candidatos = list(vizinhos(atual))
        if not candidatos:
            return atual
        melhor, valor = minimo_global(candidatos, objetivo)
        if valor < objetivo(atual):
            atual = melhor
        else:
            return atual
    return atual


def perda_quadratica_catalogo(modelo, dados):
    total = 0
    for x, y in dados:
        e = modelo(x) - y
        total += e * e
    return total


def treinar_por_busca(parametros, fabrica_modelo, dados):
    return minimo_global(parametros, lambda p: perda_quadratica_catalogo(fabrica_modelo(p), dados))[0]


def comparar_modelos(modelos, dados):
    return minimo_global(modelos, lambda m: perda_quadratica_catalogo(m, dados))
