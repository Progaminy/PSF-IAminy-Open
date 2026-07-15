# ==============================================================================
# ÁRVORE GERADORA MÍNIMA E CAMINHO MÍNIMO — Etapas 128 a 130 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   árvore geradora mínima nasce depois de árvore (etapa 116) e peso de
#   aresta (etapa 126); caminho mínimo nasce depois de caminho (etapa 113)
#   e peso.
#
# Algoritmos clássicos, adaptados à disciplina do projeto: PSO
# (Kruskal) para árvore geradora mínima, Dijkstra para caminho mínimo —
# ambos corretos sobre pesos NÃO-NEGATIVOS (numerais PSF nunca são
# negativos, então essa condição do algoritmo de Dijkstra é automática).
#
# Conceitos permitidos: tudo o que nasceu nas etapas 1-127.
# Conceitos proibidos: grafos com pesos negativos, ciclos negativos,
# fluxo em redes, estruturas ainda não construídas.
# ==============================================================================
from .aritmetica import ZERO, SOMA
from .traducao import para_int
from .grafos_finitos import PRIMEIRO, SEGUNDO


# ----------------------------------------------------------------------------
# Etapa 128 — árvore geradora mínima, por Kruskal: ordena as arestas por
# peso, adiciona gulosamente cada uma que não forma ciclo (usando
# union-find), até ter |V|-1 arestas.
# ----------------------------------------------------------------------------
def _find(pai, x):
    while pai[x] != x:
        pai[x] = pai[pai[x]]  # compressão de caminho
        x = pai[x]
    return x


def _union(pai, a, b):
    ra, rb = _find(pai, a), _find(pai, b)
    if ra == rb:
        return False
    pai[ra] = rb
    return True


def ARVORE_GERADORA_MINIMA_PURA(vertices, arestas, pesos):
    """`arestas` já vem no formato simétrico (etapa 111); só se considera
    cada par não-ordenado uma vez, usando (int(a) < int(b)) como filtro."""
    indices = {para_int(v): v for v in vertices}
    unicas = []
    vistas = set()
    for a in arestas:
        i, j = para_int(PRIMEIRO(a)), para_int(SEGUNDO(a))
        chave = (min(i, j), max(i, j))
        if chave not in vistas:
            vistas.add(chave)
            unicas.append((chave, pesos[chave]))

    unicas.sort(key=lambda par: para_int(par[1]))

    pai = {para_int(v): para_int(v) for v in vertices}
    escolhidas = []
    peso_total = ZERO
    for (i, j), peso in unicas:
        if _union(pai, i, j):
            escolhidas.append((indices[i], indices[j]))
            peso_total = SOMA(peso_total)(peso)
    return escolhidas, peso_total


# ----------------------------------------------------------------------------
# Etapa 129 — caminho mínimo em grafo ponderado, por Dijkstra. Correto
# porque pesos PSF são sempre >= 0 (não há numeral negativo).
# ----------------------------------------------------------------------------
def CAMINHO_MINIMO_PURO(origem, destino, vertices, arestas, pesos):
    """Devolve (distância_total, caminho) ou (None, None) se inalcançável."""
    alvo_origem = para_int(origem)
    alvo_destino = para_int(destino)

    nao_visitados = {para_int(v) for v in vertices}
    dist = {chave: None for chave in nao_visitados}
    dist[alvo_origem] = ZERO
    anterior = {}

    def _vizinhos_com_peso(chave_v):
        for a in arestas:
            if para_int(PRIMEIRO(a)) == chave_v:
                chave_u = para_int(SEGUNDO(a))
                par_peso = (min(chave_v, chave_u), max(chave_v, chave_u))
                yield chave_u, pesos[par_peso]

    while nao_visitados:
        candidatos = [(dist[c], c) for c in nao_visitados if dist[c] is not None]
        if not candidatos:
            break
        _, atual = min(candidatos, key=lambda par: para_int(par[0]))
        nao_visitados.remove(atual)
        if atual == alvo_destino:
            break
        for vizinho, peso in _vizinhos_com_peso(atual):
            if vizinho not in nao_visitados:
                continue
            candidato = SOMA(dist[atual])(peso)
            if dist[vizinho] is None or para_int(candidato) < para_int(dist[vizinho]):
                dist[vizinho] = candidato
                anterior[vizinho] = atual

    if dist[alvo_destino] is None:
        return None, None

    caminho_chaves = [alvo_destino]
    while caminho_chaves[-1] != alvo_origem:
        caminho_chaves.append(anterior[caminho_chaves[-1]])
    caminho_chaves.reverse()
    indices = {para_int(v): v for v in vertices}
    return dist[alvo_destino], [indices[c] for c in caminho_chaves]


# ----------------------------------------------------------------------------
# Etapa 130 — fechamento discreto geral: confirma o arco completo do
# projeto até aqui — relação → função → grupo/anel/corpo → grafo →
# árvore geradora mínima e caminho mínimo (que combinam TUDO: pesos
# vêm da aritmética, escolha gulosa vem de comparação/ordem, união vem
# de relação de equivalência por componentes).
# ----------------------------------------------------------------------------
def FECHAMENTO_DISCRETO_GERAL_PURO(vertices, arestas, pesos):
    _, peso_mst = ARVORE_GERADORA_MINIMA_PURA(vertices, arestas, pesos)
    origem = vertices[0]
    alcanca_todos = all(
        CAMINHO_MINIMO_PURO(origem, v, vertices, arestas, pesos)[0] is not None
        for v in vertices
    )
    return alcanca_todos and para_int(peso_mst) >= 0
