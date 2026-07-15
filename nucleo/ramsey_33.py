# ==============================================================================
# TEOREMA DE RAMSEY R(3,3)=6 — Etapa 1070 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   não recomeça do zero — reaproveita coloração de arestas (etapa 1069,
#   `ARESTAS_NAO_DIRIGIDAS_PURA`/`_chave_aresta` de
#   `grafos_coloracao_arestas.py`), que foi construída exatamente para
#   servir de pré-requisito a este resultado. R(3,3)=6 diz duas coisas
#   ao mesmo tempo, provadas aqui por busca exaustiva, não por citação:
#   (a) toda 2-coloração das arestas de K6 tem um triângulo
#   monocromático; (b) 6 é o menor número com essa propriedade — existe
#   uma 2-coloração de K5 SEM nenhum triângulo monocromático (contra-
#   exemplo real, não hipotético).
#
# Conceitos permitidos: coloração de arestas (etapa 1069) e tudo o que
# ela já permite (etapas 1-1069).
# Conceitos proibidos: os mesmos já proibidos no bloco de grafos —
# grafos infinitos, fluxo em redes, planaridade, teoria espectral,
# estruturas ainda não construídas. Ramsey GERAL (R(m,n) para m,n
# arbitrários) fica fora — aqui é só o caso R(3,3), busca exaustiva
# sobre um grafo completo pequeno, mesma disciplina de
# EXISTE_COLORACAO_PURA/HAMILTONIANO_PURA.
# ==============================================================================
from itertools import product, combinations

from .primitivas import PAR
from .traducao import de_int
from .grafos_coloracao_arestas import ARESTAS_NAO_DIRIGIDAS_PURA, _chave_aresta


def GRAFO_COMPLETO_ARESTAS_PURA(n):
    """Arestas não-dirigidas de K_n sobre vértices 0..n-1 (naturais PSF)."""
    vertices = [de_int(i) for i in range(n)]
    arestas = tuple(
        PAR(vertices[i])(vertices[j])
        for i in range(n) for j in range(i + 1, n)
    )
    return arestas


# ----------------------------------------------------------------------------
# Existe 2-coloração (ou k-coloração) das arestas de K_n sem nenhum
# triângulo monocromático? Busca exaustiva sobre as atribuições — mesma
# disciplina de EXISTE_COLORACAO_PURA, viável aqui porque n é pequeno
# (K6 tem 15 arestas, 2^15 = 32768 atribuições, cada uma conferindo 20
# triângulos: da ordem de 650 mil verificações, frações de segundo).
# ----------------------------------------------------------------------------
def EXISTE_COLORACAO_SEM_TRIANGULO_MONOCROMATICO_PURA(n, k=2):
    arestas = GRAFO_COMPLETO_ARESTAS_PURA(n)
    unicas = ARESTAS_NAO_DIRIGIDAS_PURA(arestas)
    chaves = [_chave_aresta(a) for a in unicas]
    triangulos = list(combinations(range(n), 3))
    for atribuicao in product(range(k), repeat=len(chaves)):
        cores = dict(zip(chaves, atribuicao))
        tem_monocromatico = any(
            cores[(i, j)] == cores[(i, l)] == cores[(j, l)]
            for (i, j, l) in triangulos
        )
        if not tem_monocromatico:
            return True
    return False


# ----------------------------------------------------------------------------
# R(3,3)=6: confirma as duas metades do resultado numa instância só —
# K5 admite um contraexemplo (existe coloração sem triângulo
# monocromático), K6 não admite nenhum (toda coloração tem um).
# ----------------------------------------------------------------------------
def RAMSEY_3_3_CONFERE_PURA():
    k5_tem_contraexemplo = EXISTE_COLORACAO_SEM_TRIANGULO_MONOCROMATICO_PURA(5, 2)
    k6_sempre_tem_monocromatico = not EXISTE_COLORACAO_SEM_TRIANGULO_MONOCROMATICO_PURA(6, 2)
    return k5_tem_contraexemplo and k6_sempre_tem_monocromatico
