"""Autômatos com pilha finita — etapas 761-800."""
from __future__ import annotations


def aceita_pilha(entrada, estado_inicial, estados_finais, pilha_inicial, transicoes, limite=200, aceitar_pilha_vazia=False):
    """Simula AP finito por busca em configurações limitadas.

    Transição: (estado, simbolo_entrada_ou_None, topo_ou_None) -> lista[(novo_estado, empilhar_tuple)]
    `empilhar_tuple` substitui o topo consumido; tupla vazia desempilha.
    """
    inicial = (estado_inicial, 0, tuple(pilha_inicial))
    fronteira = [inicial]
    visitados = {inicial}
    passos = 0
    while fronteira and passos < limite:
        estado, pos, pilha = fronteira.pop(0)
        if pos == len(entrada) and ((estado in estados_finais) or (aceitar_pilha_vazia and not pilha)):
            return True
        simbolos = [None]
        if pos < len(entrada):
            simbolos.append(entrada[pos])
        topo = pilha[-1] if pilha else None
        for s in simbolos:
            chave = (estado, s, topo)
            for novo_estado, empilha in transicoes.get(chave, []):
                nova_pos = pos + (0 if s is None else 1)
                base = pilha[:-1] if topo is not None else pilha
                nova_pilha = tuple(base + tuple(empilha))
                conf = (novo_estado, nova_pos, nova_pilha)
                if conf not in visitados:
                    visitados.add(conf)
                    fronteira.append(conf)
        passos += 1
    return False


def reconhece_catalogo(linguagem, automato, limite=200):
    estado_inicial, finais, pilha_inicial, transicoes = automato
    return {palavra: aceita_pilha(palavra, estado_inicial, finais, pilha_inicial, transicoes, limite) for palavra in linguagem}


def parenteses_balanceados_finito(palavra):
    altura = 0
    for ch in palavra:
        if ch == '(':
            altura += 1
        elif ch == ')':
            if altura == 0:
                return False
            altura -= 1
        else:
            return False
    return altura == 0
