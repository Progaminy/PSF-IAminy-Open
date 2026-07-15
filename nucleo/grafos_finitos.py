# ==============================================================================
# GRAFOS FINITOS — Etapas 111 a 127 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   um grafo não-dirigido é uma relação binária SIMÉTRICA (etapa 64) sobre
#   um domínio finito de vértices — não uma estrutura nova do zero.
#
# Convenção: uma aresta {a,b} é representada por DOIS pares PAR(a)(b) e
# PAR(b)(a) na tupla de arestas (a relação é simétrica por construção,
# verificável com SIMETRICA_PURA já existente). Um laço {v,v} aparece uma
# vez. Grafos dirigidos (arestas não simétricas) não são o foco desta
# etapa — a maioria dos conceitos abaixo assume simetria.
#
# Conceitos permitidos: tudo o que nasceu nas etapas 1-110 (relação,
# simetria, conectividade via caminho).
# Conceitos proibidos: grafos infinitos, fluxo em redes, planaridade,
# teoria espectral de grafos, estruturas ainda não construídas.
# ==============================================================================
from .primitivas import V, F, PAR
from .logica import E, OU, NAO
from .aritmetica import IGUAL, ZERO, S, SOMA
from .traducao import para_bool, para_int, de_int
from .relacoes_funcoes_naturais import (
    TODO_FINITO_PURO, EXISTE_FINITO_PURO, PRIMEIRO, SEGUNDO,
    PERTENCE_RELACAO_PURA, SIMETRICA_PURA,
)


# ----------------------------------------------------------------------------
# Etapa 111 — grafo como relação binária sobre vértices finitos.
# ----------------------------------------------------------------------------
def GRAFO_PURO(vertices, arestas):
    return (tuple(vertices), tuple(arestas))


VERTICES_DE = lambda g: g[0]
ARESTAS_DE = lambda g: g[1]


def EH_GRAFO_NAO_DIRIGIDO_PURO(g):
    """Confere a convenção: a relação de arestas é simétrica."""
    return SIMETRICA_PURA(ARESTAS_DE(g))


# ----------------------------------------------------------------------------
# Etapa 112 — grau de um vértice: número de vizinhos (arestas com `v`
# como primeiro elemento — cada vizinho aparece exatamente uma vez nessa
# contagem, graças à convenção simétrica).
# ----------------------------------------------------------------------------
def GRAU_VERTICE_PURO(v, arestas):
    return sum(1 for a in arestas if para_bool(IGUAL(PRIMEIRO(a))(v)))


# ----------------------------------------------------------------------------
# Etapa 113 — caminho: sequência de vértices onde cada par consecutivo é
# uma aresta.
# ----------------------------------------------------------------------------
def CAMINHO_PURA(sequencia, arestas):
    if len(sequencia) < 2:
        return V
    return V if all(
        para_bool(PERTENCE_RELACAO_PURA(sequencia[i])(sequencia[i + 1])(arestas))
        for i in range(len(sequencia) - 1)
    ) else F


# ----------------------------------------------------------------------------
# Etapa 114 — ciclo: caminho que volta ao início, com pelo menos 3
# vértices distintos (evita o caso degenerado v→v).
# ----------------------------------------------------------------------------
def CICLO_PURA(sequencia, arestas):
    if len(sequencia) < 4 or not para_bool(IGUAL(sequencia[0])(sequencia[-1])):
        return F
    vertices_distintos = len({para_int(v) for v in sequencia[:-1]})
    if vertices_distintos < 3:
        return F
    return CAMINHO_PURA(sequencia, arestas)


# ----------------------------------------------------------------------------
# Etapa 115 — conectividade: existe caminho entre dois vértices (busca de
# alcançabilidade), e o grafo inteiro é conexo.
# ----------------------------------------------------------------------------
def _vizinhos(v, arestas):
    return [SEGUNDO(a) for a in arestas if para_bool(IGUAL(PRIMEIRO(a))(v))]


def EXISTE_CAMINHO_PURA(origem, destino, vertices, arestas):
    visitados = set()
    fila = [origem]
    alvo = para_int(destino)
    while fila:
        atual = fila.pop()
        chave = para_int(atual)
        if chave == alvo:
            return V
        if chave in visitados:
            continue
        visitados.add(chave)
        fila.extend(_vizinhos(atual, arestas))
    return F


def CONEXO_PURA(vertices, arestas):
    if not vertices:
        return V
    origem = vertices[0]
    return V if all(para_bool(EXISTE_CAMINHO_PURA(origem, v, vertices, arestas)) for v in vertices) else F



def _metade_por_pares(n):
    metade = 0
    resto = n
    while resto >= 2:
        resto -= 2
        metade += 1
    if resto != 0:
        raise ValueError("quantidade não pareada")
    return metade


def _eh_par_por_subtracao(n):
    resto = n
    while resto >= 2:
        resto -= 2
    return resto == 0

# ----------------------------------------------------------------------------
# Etapa 116 — árvore: grafo conexo com exatamente |V|-1 arestas (contando
# cada aresta não-dirigida uma vez — por isso |arestas|/2). Caracterização
# clássica (conexo + |V|-1 arestas ⟺ árvore), usada em vez de uma busca
# explícita por ciclos.
# ----------------------------------------------------------------------------
def ARVORE_PURA(vertices, arestas):
    if not para_bool(CONEXO_PURA(vertices, arestas)):
        return F
    arestas_nao_dirigidas = _metade_por_pares(len(arestas))
    return V if arestas_nao_dirigidas == len(vertices) - 1 else F


# ----------------------------------------------------------------------------
# Etapa 117 — grafo bipartido: os vértices dividem-se em 2 grupos onde
# toda aresta liga grupos diferentes. Verificado por 2-coloração via
# busca (BFS), não por definição existencial ingênua.
# ----------------------------------------------------------------------------
def BIPARTIDO_PURA(vertices, arestas):
    cor = {}
    for inicio in vertices:
        chave_inicio = para_int(inicio)
        if chave_inicio in cor:
            continue
        cor[chave_inicio] = 0
        fila = [inicio]
        while fila:
            atual = fila.pop()
            chave_atual = para_int(atual)
            for vizinho in _vizinhos(atual, arestas):
                chave_v = para_int(vizinho)
                if chave_v not in cor:
                    cor[chave_v] = 1 - cor[chave_atual]
                    fila.append(vizinho)
                elif cor[chave_v] == cor[chave_atual]:
                    return F
    return V


# ----------------------------------------------------------------------------
# Etapa 118 — coloração de grafo finito: existe atribuição de até `k`
# cores onde vértices adjacentes têm cores diferentes? Busca exaustiva —
# correta para grafos pequenos, não um algoritmo eficiente geral (o
# problema é NP-difícil em geral; aqui o domínio é sempre finito e
# pequeno, mesma disciplina de HAMILTONIANO_PURA abaixo).
# ----------------------------------------------------------------------------
def COLORACAO_VALIDA_PURA(vertices, arestas, cores):
    return V if all(
        cores[para_int(PRIMEIRO(a))] != cores[para_int(SEGUNDO(a))] for a in arestas
    ) else F


def EXISTE_COLORACAO_PURA(vertices, arestas, k):
    from itertools import product as produto_cartesiano

    indices = {para_int(v): i for i, v in enumerate(vertices)}
    for atribuicao in produto_cartesiano(range(k), repeat=len(vertices)):
        cores = {v: atribuicao[i] for v, i in indices.items()}
        valido = all(cores[para_int(PRIMEIRO(a))] != cores[para_int(SEGUNDO(a))] for a in arestas)
        if valido:
            return V
    return F


# ----------------------------------------------------------------------------
# Etapa 119 — grafo completo: toda dupla de vértices distintos é aresta.
# ----------------------------------------------------------------------------
def GRAFO_COMPLETO_PURA(vertices, arestas):
    return V if all(
        para_int(u) == para_int(v) or para_bool(PERTENCE_RELACAO_PURA(u)(v)(arestas))
        for u in vertices for v in vertices
    ) else F


# ----------------------------------------------------------------------------
# Etapa 120 — complemento de um grafo: mesmas vértices, arestas são
# exatamente as NÃO-arestas do original (excluindo laços).
# ----------------------------------------------------------------------------
def COMPLEMENTO_GRAFO_PURO(vertices, arestas):
    complemento = tuple(
        PAR(u)(v)
        for u in vertices for v in vertices
        if para_int(u) != para_int(v) and not para_bool(PERTENCE_RELACAO_PURA(u)(v)(arestas))
    )
    return GRAFO_PURO(vertices, complemento)


# ----------------------------------------------------------------------------
# Etapa 121 — isomorfismo de grafos finitos: existe bijeção entre os
# vértices que preserva a relação de adjacência dos dois lados.
# ----------------------------------------------------------------------------
def ISOMORFISMO_GRAFOS_PURA(vertices1, arestas1, vertices2, arestas2, bijecao):
    """`bijecao` é um dict {int(v1): v2}."""
    if len(vertices1) != len(vertices2):
        return F
    for u in vertices1:
        for v in vertices1:
            adj1 = para_bool(PERTENCE_RELACAO_PURA(u)(v)(arestas1))
            u2, v2 = bijecao[para_int(u)], bijecao[para_int(v)]
            adj2 = para_bool(PERTENCE_RELACAO_PURA(u2)(v2)(arestas2))
            if adj1 != adj2:
                return F
    return V


# ----------------------------------------------------------------------------
# Etapa 122 — subgrafo: vértices e arestas de H estão contidos em G.
# ----------------------------------------------------------------------------
def SUBGRAFO_PURO(vertices_h, arestas_h, vertices_g, arestas_g):
    chaves_g = {para_int(v) for v in vertices_g}
    if not all(para_int(v) in chaves_g for v in vertices_h):
        return F
    return V if all(
        para_bool(PERTENCE_RELACAO_PURA(PRIMEIRO(a))(SEGUNDO(a))(arestas_g)) for a in arestas_h
    ) else F


# ----------------------------------------------------------------------------
# Etapa 123 — grafo Euleriano: existe um passeio que usa cada aresta
# exatamente uma vez. Teorema de Euler (1736, o problema das pontes de
# Königsberg): existe sse o grafo é conexo e todo vértice tem grau par.
# Usar o TEOREMA em vez de buscar o passeio explicitamente — mais rápido
# e é, ele próprio, um resultado real a confirmar, não só uma busca.
# ----------------------------------------------------------------------------
def EULERIANO_PURA(vertices, arestas):
    if not para_bool(CONEXO_PURA(vertices, arestas)):
        return F
    return V if all(_eh_par_por_subtracao(GRAU_VERTICE_PURO(v, arestas)) for v in vertices) else F


# ----------------------------------------------------------------------------
# Etapa 124 — grafo Hamiltoniano: existe caminho que visita cada vértice
# exatamente uma vez. Busca exaustiva sobre permutações — NP-difícil em
# geral, correta aqui só porque o domínio é pequeno (mesma disciplina de
# EXISTE_COLORACAO_PURA).
# ----------------------------------------------------------------------------
def HAMILTONIANO_PURA(vertices, arestas):
    from itertools import permutations

    if not vertices:
        return V
    primeiro = vertices[0]
    resto = vertices[1:]
    for permutacao in permutations(resto):
        caminho = (primeiro,) + permutacao
        if para_bool(CAMINHO_PURA(caminho, arestas)):
            return V
    return V if len(vertices) == 1 else F


# ----------------------------------------------------------------------------
# Etapa 125 — matriz de adjacência: M[i][j] = 1 se (vi,vj) é aresta, 0
# caso contrário.
# ----------------------------------------------------------------------------
def MATRIZ_ADJACENCIA_PURA(vertices, arestas):
    n = len(vertices)
    um, zero = S(ZERO), ZERO
    return tuple(
        tuple(
            um if para_bool(PERTENCE_RELACAO_PURA(vertices[i])(vertices[j])(arestas)) else zero
            for j in range(n)
        )
        for i in range(n)
    )


# ----------------------------------------------------------------------------
# Etapa 126 — grafo ponderado: cada aresta ganha um peso (natural). Peso
# de um caminho = soma dos pesos das arestas percorridas.
# ----------------------------------------------------------------------------
def PESO_ARESTA_PURA(a, b, pesos):
    """`pesos` é um dict {(int(a),int(b)): peso_PSF}."""
    return pesos[(para_int(a), para_int(b))]


def PESO_CAMINHO_PURO(sequencia, pesos):
    total = ZERO
    for i in range(len(sequencia) - 1):
        total = SOMA(total)(PESO_ARESTA_PURA(sequencia[i], sequencia[i + 1], pesos))
    return total


# ----------------------------------------------------------------------------
# Etapa 127 — fechamento de grafos: confirma o ciclo completo — relação
# simétrica dá grafo; grafo dá grau, caminho, ciclo; caminho dá
# conectividade; conectividade dá árvore; grau par + conexo dá Euleriano.
# ----------------------------------------------------------------------------
def FECHAMENTO_GRAFOS_PURO(vertices, arestas):
    eh_grafo_valido = EH_GRAFO_NAO_DIRIGIDO_PURO(GRAFO_PURO(vertices, arestas))
    conexo = CONEXO_PURA(vertices, arestas)
    return E(eh_grafo_valido)(conexo)
