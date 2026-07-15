"""Complexidade por recursos finitos — etapas 801-840."""
from __future__ import annotations
import time


def conta_passos(transicao, estado_inicial, final, limite=1000):
    estado = estado_inicial
    passos = 0
    while not final(estado):
        if passos >= limite:
            return {"terminou": False, "passos": passos, "estado": estado}
        estado = transicao(estado)
        passos += 1
    return {"terminou": True, "passos": passos, "estado": estado}


def tabela_custos(algoritmo, entradas):
    tabela = []
    for entrada in entradas:
        inicio = time.monotonic()
        saida = algoritmo(entrada)
        segundos = time.monotonic() - inicio
        tabela.append({"entrada": entrada, "saida": saida, "segundos": segundos})
    return tabela


def pior_caso_por_catalogo(custos, chave="passos"):
    if not custos:
        return None
    melhor = custos[0]
    for item in custos[1:]:
        if item[chave] > melhor[chave]:
            melhor = item
    return melhor


def melhor_caso_por_catalogo(custos, chave="passos"):
    if not custos:
        return None
    melhor = custos[0]
    for item in custos[1:]:
        if item[chave] < melhor[chave]:
            melhor = item
    return melhor


def cabe_no_orcamento(custo, orcamento):
    return custo <= orcamento


def reducao_finita(instancias, transformar, solucionador_a, solucionador_b):
    """Confere num catálogo que transformar instância de A preserva resposta em B."""
    for x in instancias:
        if solucionador_a(x) != solucionador_b(transformar(x)):
            return False
    return True
