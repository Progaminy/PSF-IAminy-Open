# ==============================================================================
# ELIMINAÇÃO GAUSSIANA E SISTEMAS LINEARES — Etapas 108 a 110 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   eliminação gaussiana nasce depois de matriz (etapa 106) e precisa do
#   inverso multiplicativo do corpo (etapa 94) para normalizar pivôs.
#
# Representação: matriz = lista de linhas (tuplas de escalares do corpo).
# Trabalha por CÓPIA (nunca modifica a matriz de entrada) — consistente
# com o estilo funcional/imutável do resto do projeto.
#
# Conceitos permitidos: tudo o que nasceu nas etapas 1-107.
# Conceitos proibidos: eliminação sobre corpos infinitos, decomposição
# LU/QR, valores singulares, estruturas ainda não construídas.
# ==============================================================================
from .primitivas import V, F
from .aritmetica import IGUAL
from .traducao import para_bool


def _reciproco_por_busca(c, dominio, produto_corpo, unidade):
    """Acha o inverso multiplicativo de c por busca no domínio finito —
    o corpo já foi validado (etapa 94), então sabemos que existe para
    todo c != 0; aqui só localizamos o valor concreto."""
    for candidato in dominio:
        if para_bool(IGUAL(produto_corpo(c)(candidato))(unidade)):
            return candidato
    raise ValueError("elemento sem inverso no domínio fornecido — corpo mal formado?")


# ----------------------------------------------------------------------------
# Etapa 108 — eliminação gaussiana finita: forma escalonada por linhas.
# ----------------------------------------------------------------------------
def ELIMINACAO_GAUSSIANA_PURA(matriz, dominio, soma_corpo, sub_corpo, produto_corpo, zero, unidade):
    linhas = [list(linha) for linha in matriz]
    n_linhas, n_colunas = len(linhas), len(linhas[0]) if linhas else 0
    linha_pivo = 0

    for coluna in range(n_colunas):
        if linha_pivo >= n_linhas:
            break
        candidata = None
        for i in range(linha_pivo, n_linhas):
            if not para_bool(IGUAL(linhas[i][coluna])(zero)):
                candidata = i
                break
        if candidata is None:
            continue
        linhas[linha_pivo], linhas[candidata] = linhas[candidata], linhas[linha_pivo]

        inverso_pivo = _reciproco_por_busca(linhas[linha_pivo][coluna], dominio, produto_corpo, unidade)
        linhas[linha_pivo] = [produto_corpo(inverso_pivo)(x) for x in linhas[linha_pivo]]

        for i in range(n_linhas):
            if i == linha_pivo:
                continue
            fator = linhas[i][coluna]
            if para_bool(IGUAL(fator)(zero)):
                continue
            linhas[i] = [
                sub_corpo(linhas[i][j])(produto_corpo(fator)(linhas[linha_pivo][j]))
                for j in range(n_colunas)
            ]
        linha_pivo += 1

    return tuple(tuple(linha) for linha in linhas)


# ----------------------------------------------------------------------------
# Etapa 109 — posto de uma matriz: número de linhas não-nulas depois da
# eliminação gaussiana.
# ----------------------------------------------------------------------------
def POSTO_PURO(matriz, dominio, soma_corpo, sub_corpo, produto_corpo, zero, unidade):
    escalonada = ELIMINACAO_GAUSSIANA_PURA(matriz, dominio, soma_corpo, sub_corpo, produto_corpo, zero, unidade)
    return sum(1 for linha in escalonada if any(not para_bool(IGUAL(x)(zero)) for x in linha))


# ----------------------------------------------------------------------------
# Etapa 110 — sistemas lineares finitos: Ax=b, por eliminação sobre a
# matriz aumentada [A|b].
# ----------------------------------------------------------------------------
def RESOLVER_SISTEMA_PURO(A, b, dominio, soma_corpo, sub_corpo, produto_corpo, zero, unidade):
    """Devolve a solução (tupla) se o sistema é determinado, ou None se
    for impossível ou indeterminado — verificação estrutural, não uma
    parametrização geral de infinitas soluções."""
    n = len(A)
    aumentada = [list(A[i]) + [b[i]] for i in range(n)]
    escalonada = [list(linha) for linha in ELIMINACAO_GAUSSIANA_PURA(
        aumentada, dominio, soma_corpo, sub_corpo, produto_corpo, zero, unidade
    )]

    for linha in escalonada:
        if all(para_bool(IGUAL(x)(zero)) for x in linha[:-1]) and not para_bool(IGUAL(linha[-1])(zero)):
            return None  # sistema impossível

    posto = sum(1 for linha in escalonada if any(not para_bool(IGUAL(x)(zero)) for x in linha[:-1]))
    if posto < n:
        return None  # indeterminado — fora do escopo desta etapa

    solucao = [zero] * n
    for linha in escalonada:
        for j in range(n):
            if not para_bool(IGUAL(linha[j])(zero)):
                solucao[j] = linha[-1]
                break
    return tuple(solucao)
