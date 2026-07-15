# ==============================================================================
# EMPARELHAMENTO E TEOREMA DE HALL — Etapa 1066 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   não recomeça do zero — reaproveita grafo bipartido (etapa 117,
#   `BIPARTIDO_PURA`/`_vizinhos` de `grafos_finitos.py`) como ponto de
#   partida. Um emparelhamento é um subconjunto de arestas onde nenhum
#   vértice se repete; o Teorema de Hall (1935) caracteriza quando existe
#   emparelhamento cobrindo TODO o grupo A: sse todo subconjunto S de A
#   tem vizinhança |N(S)| >= |S|.
#
# Conceitos permitidos: grafo bipartido (etapa 117) e tudo o que ele já
# permite (etapas 1-117).
# Conceitos proibidos: os mesmos já proibidos no bloco de grafos —
# grafos infinitos, fluxo em redes, planaridade, teoria espectral,
# estruturas ainda não construídas. Emparelhamento MÁXIMO por algoritmo
# eficiente (Hopcroft-Karp) fica fora — aqui é busca exaustiva, mesma
# disciplina de EXISTE_COLORACAO_PURA/HAMILTONIANO_PURA: correta para
# grafos pequenos, não um algoritmo geral eficiente.
# ==============================================================================
from .traducao import para_bool, para_int
from .relacoes_funcoes_naturais import PRIMEIRO, SEGUNDO, PERTENCE_RELACAO_PURA
from .grafos_finitos import _vizinhos


# ----------------------------------------------------------------------------
# Bipartição explícita: mesma busca (BFS 2-coloração) de BIPARTIDO_PURA
# (etapa 117), mas devolvendo os dois grupos em vez de só V/F — a peça que
# faltava para falar de emparelhamento entre os dois lados.
# ----------------------------------------------------------------------------
def PARTES_BIPARTIDO_PURA(vertices, arestas):
    """Devolve (grupo_a, grupo_b) quando o grafo é bipartido, ou None quando não é."""
    cor = {}
    vertice_de = {para_int(v): v for v in vertices}
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
                    return None
    grupo_a = tuple(vertice_de[k] for k, c in cor.items() if c == 0)
    grupo_b = tuple(vertice_de[k] for k, c in cor.items() if c == 1)
    return grupo_a, grupo_b


# ----------------------------------------------------------------------------
# Emparelhamento: subconjunto de arestas onde nenhum vértice se repete
# (cada vértice cobre, no máximo, uma aresta do emparelhamento).
# ----------------------------------------------------------------------------
def EH_EMPARELHAMENTO_PURA(arestas_candidatas):
    vistos = set()
    for a in arestas_candidatas:
        u, v = para_int(PRIMEIRO(a)), para_int(SEGUNDO(a))
        if u in vistos or v in vistos:
            return False
        vistos.add(u)
        vistos.add(v)
    return True


# ----------------------------------------------------------------------------
# Existe emparelhamento que cobre TODO o grupo_a (bijeção de grupo_a para
# um subconjunto de grupo_b, ligada por arestas reais)? Busca exaustiva
# sobre bijeções candidatas — mesma disciplina de HAMILTONIANO_PURA.
# ----------------------------------------------------------------------------
def EXISTE_EMPARELHAMENTO_PERFEITO_PURA(grupo_a, grupo_b, arestas):
    from itertools import permutations

    if len(grupo_a) > len(grupo_b):
        return False
    for alvo in permutations(grupo_b, len(grupo_a)):
        if all(
            para_bool(PERTENCE_RELACAO_PURA(grupo_a[i])(alvo[i])(arestas))
            for i in range(len(grupo_a))
        ):
            return True
    return False


# ----------------------------------------------------------------------------
# Vizinhança de um subconjunto S do grupo A: vértices do grupo B ligados a
# algum vértice de S, sem repetição.
# ----------------------------------------------------------------------------
def VIZINHANCA_PURA(subconjunto, arestas):
    vistos = set()
    vizinhanca = []
    for v in subconjunto:
        for vizinho in _vizinhos(v, arestas):
            chave = para_int(vizinho)
            if chave not in vistos:
                vistos.add(chave)
                vizinhanca.append(vizinho)
    return tuple(vizinhanca)


# ----------------------------------------------------------------------------
# Condição de Hall: para TODO subconjunto S de grupo_a, |N(S)| >= |S|.
# Busca exaustiva sobre os 2^|grupo_a| subconjuntos não vazios — mesma
# disciplina de EXISTE_COLORACAO_PURA, correta para grupos pequenos.
# ----------------------------------------------------------------------------
def SATISFAZ_CONDICAO_HALL_PURA(grupo_a, arestas):
    from itertools import combinations

    n = len(grupo_a)
    for tamanho in range(1, n + 1):
        for subconjunto in combinations(grupo_a, tamanho):
            if len(VIZINHANCA_PURA(subconjunto, arestas)) < tamanho:
                return False
    return True


# ----------------------------------------------------------------------------
# Teorema de Hall (1935): existe emparelhamento cobrindo grupo_a se e
# somente se grupo_a satisfaz a condição de Hall. Não fingimos a prova
# geral — confirmamos computacionalmente, instância por instância, que as
# duas respostas concordam (mesma disciplina de EULERIANO_PURA
# confirmando o Teorema de Euler contra as Pontes de Königsberg).
# ----------------------------------------------------------------------------
def TEOREMA_DE_HALL_CONFERE_PURA(grupo_a, grupo_b, arestas):
    existe = EXISTE_EMPARELHAMENTO_PERFEITO_PURA(grupo_a, grupo_b, arestas)
    satisfaz = SATISFAZ_CONDICAO_HALL_PURA(grupo_a, arestas)
    return existe == satisfaz
