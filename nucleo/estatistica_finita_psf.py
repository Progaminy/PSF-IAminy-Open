"""Estatística finita PSF — etapas 961-990."""
from __future__ import annotations


def frequencias(dados):
    f = {}
    for x in dados:
        f[x] = f.get(x, 0) + 1
    return f


def media_par(dados):
    total = 0
    quantidade = 0
    for x in dados:
        total += x
        quantidade += 1
    return (total, quantidade)


def _metade_e_paridade(n):
    """Devolve (metade_truncada, eh_impar) por subtração repetida de dois."""
    metade = 0
    resto = n
    while resto >= 2:
        resto -= 2
        metade += 1
    return metade, (resto == 1)


def mediana_finita(dados):
    s = sorted(dados)
    n = len(s)
    if n == 0:
        raise ValueError("sem dados")
    meio, impar = _metade_e_paridade(n)
    if impar:
        return (s[meio], 1)
    return (s[meio - 1] + s[meio], 2)


def moda_finita(dados):
    f = frequencias(dados)
    maior = None
    saida = []
    for valor, qtd in f.items():
        if maior is None or qtd > maior:
            maior = qtd
            saida = [valor]
        elif qtd == maior:
            saida.append(valor)
    return sorted(saida)


def amplitude_finita(dados):
    if not dados:
        raise ValueError("sem dados")
    return max(dados) - min(dados)


def variancia_par(dados):
    total, n = media_par(dados)
    acumulado = 0
    for x in dados:
        d = x * n - total
        acumulado += d * d
    return (acumulado, n * n * n)


def erro_modelo(dados, modelo):
    erro = 0
    for entrada, esperado in dados:
        d = modelo(entrada) - esperado
        erro += d * d
    return erro
