"""Reescrita e transformação de provas finitas — etapas 721-760."""
from __future__ import annotations


def aplica_regra_termo(termo, esquerda, direita):
    """Substitui ocorrências exatas de esquerda por direita numa árvore finita."""
    if termo == esquerda:
        return direita, True
    if isinstance(termo, tuple):
        novos = []
        mudou = False
        for filho in termo:
            n, m = aplica_regra_termo(filho, esquerda, direita)
            novos.append(n)
            mudou = mudou or m
        return tuple(novos), mudou
    return termo, False


def passo_reescrita(termo, regras):
    for esquerda, direita in regras:
        novo, mudou = aplica_regra_termo(termo, esquerda, direita)
        if mudou:
            return novo
    return termo


def forma_normal_limitada(termo, regras, limite=50):
    atual = termo
    for _ in range(limite):
        proximo = passo_reescrita(atual, regras)
        if proximo == atual:
            return atual
        atual = proximo
    raise RuntimeError("limite de normalização atingido")


def sequencia_reescrita(termo, regras, limite=50):
    atual = termo
    seq = [atual]
    for _ in range(limite):
        proximo = passo_reescrita(atual, regras)
        if proximo == atual:
            return seq
        seq.append(proximo)
        atual = proximo
    raise RuntimeError("limite de reescrita atingido")


def equivalente_por_reescrita(a, b, regras, limite=50):
    return forma_normal_limitada(a, regras, limite) == forma_normal_limitada(b, regras, limite)


def derivacao_valida(inicio, fim, regras, passos):
    atual = inicio
    for esperado in passos:
        atual = passo_reescrita(atual, regras)
        if atual != esperado:
            return False
    return atual == fim


def grafo_reescrita(catalogo, regras):
    return {termo: passo_reescrita(termo, regras) for termo in catalogo}
