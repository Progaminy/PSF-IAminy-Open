"""Ordenação finita — ordenar uma lista pequena de inteiros do zero.

Insertion sort: cada elemento é deslocado para trás até achar o seu
lugar certo entre os já ordenados. O(n²), mas simples e verificável a
olho -- adequado ao tamanho das listas que aparecem em exercícios
(poucas dezenas de itens, não milhões). A comparação e a troca são
escritas aqui, passo a passo -- em vez de chamar `sorted()`/`list.sort()`
já prontos da biblioteca padrão.
"""
from __future__ import annotations


def ordenar_crescente(valores: list[int]) -> list[int]:
    lista = list(valores)
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual
    return lista


def ordenar_decrescente(valores: list[int]) -> list[int]:
    lista = list(valores)
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] < atual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual
    return lista


def esta_ordenada_crescente(valores: list[int]) -> bool:
    return all(valores[i] <= valores[i + 1] for i in range(len(valores) - 1))
