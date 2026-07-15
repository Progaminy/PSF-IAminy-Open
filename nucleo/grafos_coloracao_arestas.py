# ==============================================================================
# COLORAÇÃO DE ARESTAS — Etapa 1069 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   não recomeça do zero — reaproveita a mesma disciplina de busca
#   exaustiva de EXISTE_COLORACAO_PURA (etapa 118, coloração de
#   VÉRTICES), só trocando o que é colorido: agora são as arestas não-
#   dirigidas, e duas arestas que compartilham um vértice não podem ter
#   a mesma cor (em vez de dois vértices ligados por uma aresta).
#
# Conceitos permitidos: grafo como relação binária (etapa 111) e tudo o
# que ele já permite (etapas 1-127).
# Conceitos proibidos: os mesmos já proibidos no bloco de grafos —
# grafos infinitos, fluxo em redes, planaridade, teoria espectral,
# estruturas ainda não construídas. Coloração de arestas ÓTIMA (índice
# cromático exato, Teorema de Vizing) e Teorema de Ramsey (que esta
# etapa serve de pré-requisito para) ficam fora — aqui só existência por
# busca exaustiva, mesma disciplina de EXISTE_COLORACAO_PURA/
# HAMILTONIANO_PURA.
# ==============================================================================
from .traducao import para_int
from .relacoes_funcoes_naturais import PRIMEIRO, SEGUNDO


def _chave_aresta(a):
    u, v = para_int(PRIMEIRO(a)), para_int(SEGUNDO(a))
    return (min(u, v), max(u, v))


# ----------------------------------------------------------------------------
# A convenção do projeto representa uma aresta não-dirigida {a,b} por DOIS
# pares na tupla (PAR(a)(b) e PAR(b)(a)) — para colorir arestas, cada par
# {a,b} conta uma única vez, não duas.
# ----------------------------------------------------------------------------
def ARESTAS_NAO_DIRIGIDAS_PURA(arestas):
    vistas = set()
    unicas = []
    for a in arestas:
        chave = _chave_aresta(a)
        if chave not in vistas:
            vistas.add(chave)
            unicas.append(a)
    return tuple(unicas)


# ----------------------------------------------------------------------------
# Coloração de arestas válida: nenhum par de arestas que compartilham um
# vértice tem a mesma cor. `cores` é um dict {(min,max) da aresta: cor}.
# ----------------------------------------------------------------------------
def COLORACAO_ARESTAS_VALIDA_PURA(arestas_nao_dirigidas, cores):
    lista = list(arestas_nao_dirigidas)
    for i in range(len(lista)):
        u1, v1 = para_int(PRIMEIRO(lista[i])), para_int(SEGUNDO(lista[i]))
        for j in range(i + 1, len(lista)):
            u2, v2 = para_int(PRIMEIRO(lista[j])), para_int(SEGUNDO(lista[j]))
            compartilha_vertice = u1 in (u2, v2) or v1 in (u2, v2)
            if compartilha_vertice and cores[_chave_aresta(lista[i])] == cores[_chave_aresta(lista[j])]:
                return False
    return True


# ----------------------------------------------------------------------------
# Existe atribuição de até `k` cores às arestas onde nenhum par que
# compartilha vértice repete cor? Busca exaustiva — correta para grafos
# pequenos, mesma disciplina de EXISTE_COLORACAO_PURA (NP-difícil em
# geral, o domínio aqui é sempre pequeno).
# ----------------------------------------------------------------------------
def EXISTE_COLORACAO_ARESTAS_PURA(arestas, k):
    from itertools import product

    unicas = ARESTAS_NAO_DIRIGIDAS_PURA(arestas)
    chaves = [_chave_aresta(a) for a in unicas]
    for atribuicao in product(range(k), repeat=len(unicas)):
        cores = dict(zip(chaves, atribuicao))
        if COLORACAO_ARESTAS_VALIDA_PURA(unicas, cores):
            return True
    return False
