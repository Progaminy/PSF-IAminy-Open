"""Análise discreta finita — etapas 841-880."""
from __future__ import annotations


def diferencas(seq):
    return [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]


def diferenca_ordem(seq, ordem):
    atual = list(seq)
    for _ in range(ordem):
        atual = diferencas(atual)
    return atual


def soma_acumulada(seq):
    total = 0
    saida = []
    for x in seq:
        total += x
        saida.append(total)
    return saida


def media_como_par(seq):
    total = 0
    quantidade = 0
    for x in seq:
        total += x
        quantidade += 1
    return (total, quantidade)


def erro_absoluto(a, b):
    return a - b if a >= b else b - a


def converge_por_janela(seq, tolerancia, janela):
    if len(seq) < janela or janela <= 1:
        return False
    ultimos = seq[-janela:]
    for i in range(len(ultimos)):
        for j in range(i + 1, len(ultimos)):
            if erro_absoluto(ultimos[i], ultimos[j]) > tolerancia:
                return False
    return True


def integral_discreta(valores):
    total = 0
    for v in valores:
        total += v
    return total


def monotona_crescente_finita(seq):
    return all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1))
