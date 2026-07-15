# ==============================================================================
# CENTRALIDADE DE GRAU E COEFICIENTE DE AGRUPAMENTO — Etapa 1072 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   não recomeça do zero — reaproveita `GRAU_VERTICE_PURO` e `_vizinhos`
#   (etapa 112/115, `grafos_finitos.py`) e `RacionalAssinado` (já
#   provado na linha dos reais) para devolver frações exatas, nunca
#   float. Centralidade de grau e coeficiente de agrupamento são as duas
#   métricas mais básicas de análise de redes sociais sobre um grafo já
#   construído — não pedem nenhuma estrutura nova, só razões exatas
#   sobre o que já existe.
#
# Conceitos permitidos: grafo como relação binária (etapa 111) e tudo o
# que ele já permite (etapas 1-127), racional assinado (linha dos reais).
# Conceitos proibidos: os mesmos já proibidos no bloco de grafos —
# grafos infinitos, fluxo em redes, planaridade, teoria espectral,
# estruturas ainda não construídas. Centralidade de intermediação
# (betweenness, exige caminho mínimo entre TODO par) e de proximidade
# (closeness) ficam fora — pedem infraestrutura de caminho ponderado
# ainda não composta com este bloco; este corte é só grau e agrupamento.
# ==============================================================================
from .traducao import para_bool
from .relacoes_funcoes_naturais import PERTENCE_RELACAO_PURA
from .grafos_finitos import GRAU_VERTICE_PURO, _vizinhos
from .reais_intervalos_naturais import RacionalAssinado


# ----------------------------------------------------------------------------
# Centralidade de grau: grau do vértice normalizado pelo maior grau
# possível num grafo simples com n vértices (n-1, sem laço). Fração
# exata, nunca aproximada.
# ----------------------------------------------------------------------------
def CENTRALIDADE_GRAU_PURA(vertice, vertices, arestas):
    n = len(vertices)
    if n < 2:
        raise ValueError("centralidade de grau exige pelo menos 2 vértices")
    grau = GRAU_VERTICE_PURO(vertice, arestas)
    return RacionalAssinado(grau, n - 1)


# ----------------------------------------------------------------------------
# Coeficiente de agrupamento de um vértice: dos pares de vizinhos de v,
# que fração está de facto ligada entre si (triângulos através de v
# sobre o total de pares possíveis). None quando o grau é menor que 2 --
# indefinido de verdade, não fingido como 0.
# ----------------------------------------------------------------------------
def COEFICIENTE_AGRUPAMENTO_OU_NONE(vertice, arestas):
    vizinhos = _vizinhos(vertice, arestas)
    k = len(vizinhos)
    if k < 2:
        return None
    triangulos = 0
    for i in range(k):
        for j in range(i + 1, k):
            if para_bool(PERTENCE_RELACAO_PURA(vizinhos[i])(vizinhos[j])(arestas)):
                triangulos += 1
    # 2*triângulos / k*(k-1) em vez de triângulos / (k*(k-1)/2): a
    # mesma razão, sem precisar de divisão inteira -- RacionalAssinado
    # já reduz a fração sozinho.
    return RacionalAssinado(2 * triangulos, k * (k - 1))
