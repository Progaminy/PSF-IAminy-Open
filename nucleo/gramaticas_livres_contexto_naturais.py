# ==============================================================================
# GRAMÁTICAS LIVRES DE CONTEXTO NATURAIS — Etapas 601 a 640.
# ==============================================================================
# Esta camada não prova teoremas universais de CFL. Ela constrói ferramentas
# finitas: derivação esquerda, CYK finito para CNF declarada, árvore sintática e
# catálogo de comparação. Sem divisão, módulo, primalidade ou infinitos atuais.
# ==============================================================================
from .primitivas import V, F
from .gramaticas_finitas import GRAMATICA_FINITA, PRODUCAO_FINITA, PALAVRAS_GERADAS_ATE_FINITO


def _bool(condicao):
    return V if condicao else F


def _bool_to_py(valor):
    return valor(True)(False)


def CFG_NATURAL_FINITA(nao_terminais, terminais, inicial, producoes):
    return GRAMATICA_FINITA(nao_terminais, terminais, inicial, producoes)


def DERIVACAO_ESQUERDA_UM_PASSO_FINITA(gramatica, forma):
    forma = tuple(forma)
    for indice, simbolo in enumerate(forma):
        if simbolo in gramatica["nao_terminais"]:
            saida = []
            for esquerda, direita in gramatica["producoes"]:
                if esquerda == simbolo:
                    nova = forma[:indice] + direita + forma[indice + 1:]
                    if nova not in saida:
                        saida.append(nova)
            return tuple(saida)
    return tuple()


def DERIVAR_ESQUERDA_ATE_FINITO(gramatica, passos):
    atuais = ((gramatica["inicial"],),)
    vistas = list(atuais)
    for _ in range(passos):
        proximas = []
        for forma in atuais:
            for nova in DERIVACAO_ESQUERDA_UM_PASSO_FINITA(gramatica, forma):
                if nova not in vistas:
                    vistas.append(nova)
                if nova not in proximas:
                    proximas.append(nova)
        atuais = tuple(proximas)
        if not atuais:
            break
    return tuple(vistas)


def EH_CNF_FINITA(gramatica):
    for esquerda, direita in gramatica["producoes"]:
        if esquerda not in gramatica["nao_terminais"]:
            return F
        if len(direita) == 1 and direita[0] in gramatica["terminais"]:
            continue
        if len(direita) == 2 and direita[0] in gramatica["nao_terminais"] and direita[1] in gramatica["nao_terminais"]:
            continue
        if direita == tuple() and esquerda == gramatica["inicial"]:
            continue
        return F
    return V


def CYK_RECONHECE_FINITO(gramatica, palavra):
    palavra = tuple(palavra)
    if not _bool_to_py(EH_CNF_FINITA(gramatica)):
        raise ValueError("CYK aqui exige gramática em forma normal de Chomsky finita")
    if palavra == tuple():
        return _bool(any(esq == gramatica["inicial"] and dir_ == tuple() for esq, dir_ in gramatica["producoes"]))
    n = len(palavra)
    tabela = [[set() for _ in range(n)] for _ in range(n)]
    for i, simbolo in enumerate(palavra):
        for esquerda, direita in gramatica["producoes"]:
            if direita == (simbolo,):
                tabela[i][0].add(esquerda)
    for tamanho in range(2, n + 1):
        for inicio in range(0, n - tamanho + 1):
            celula = tabela[inicio][tamanho - 1]
            for corte in range(1, tamanho):
                esquerda_set = tabela[inicio][corte - 1]
                direita_set = tabela[inicio + corte][tamanho - corte - 1]
                for A, rhs in gramatica["producoes"]:
                    if len(rhs) == 2 and rhs[0] in esquerda_set and rhs[1] in direita_set:
                        celula.add(A)
    return _bool(gramatica["inicial"] in tabela[0][n - 1])


def ARVORE_SINTATICA_FINITA(simbolo, *filhos):
    return (simbolo, tuple(filhos))


def RAIZ_ARVORE_SINTATICA(arvore):
    return arvore[0]


def FOLHAS_ARVORE_SINTATICA(arvore):
    simbolo, filhos = arvore
    if not filhos:
        return (simbolo,)
    saida = []
    for filho in filhos:
        saida.extend(FOLHAS_ARVORE_SINTATICA(filho))
    return tuple(saida)


def PROFUNDIDADE_ARVORE_SINTATICA(arvore):
    _, filhos = arvore
    if not filhos:
        return 1
    maior = 0
    for filho in filhos:
        p = PROFUNDIDADE_ARVORE_SINTATICA(filho)
        if p > maior:
            maior = p
    return 1 + maior


def CFG_E_CYK_CONCORDAM_CATALOGO(gramatica, catalogo, passos_derivacao):
    geradas = set(PALAVRAS_GERADAS_ATE_FINITO(gramatica, passos_derivacao))
    for palavra in catalogo:
        por_geracao = tuple(palavra) in geradas
        por_cyk = _bool_to_py(CYK_RECONHECE_FINITO(gramatica, palavra))
        if por_geracao != por_cyk:
            return F
    return V


def FECHAMENTO_CFG_NATURAL_FINITA():
    return V
