# ==============================================================================
# GRAMÁTICAS FORMAIS FINITAS — Etapas 441 a 480 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   depois de computabilidade finita (401-440), a linguagem formal deve nascer
#   como objeto próprio: alfabeto, palavra, símbolo terminal/não-terminal,
#   produção, derivação e reconhecimento finito. Nada aqui usa análise real,
#   infinitos atuais, cardinalidade infinita, primalidade/fatoração, nem
#   divisão/resto nativos. Todo teste é sobre catálogos finitos declarados.
# ==============================================================================
from .primitivas import V, F
from .metodos_finitos import DFA_FINITO, ACEITA_DFA_FINITO


def _bool(condicao):
    return V if condicao else F


def _bool_to_py(valor):
    return valor(True)(False)


def _unicos(seq):
    saida = []
    for x in seq:
        if x not in saida:
            saida.append(x)
    return tuple(saida)


# ------------------------------------------------------------------------------
# Etapas 441-450 — alfabetos, palavras, produções e derivação finita.
# ------------------------------------------------------------------------------
def ALFABETO_GRAMATICAL_FINITO(simbolos):
    return tuple(_unicos(tuple(simbolos)))


def PALAVRA_GRAMATICAL_FINITA(*simbolos):
    return tuple(simbolos)


def TERMINAIS_E_NAO_TERMINAIS_FINITOS(terminais, nao_terminais):
    terminais = ALFABETO_GRAMATICAL_FINITO(terminais)
    nao_terminais = ALFABETO_GRAMATICAL_FINITO(nao_terminais)
    colisao = tuple(s for s in terminais if s in nao_terminais)
    if colisao:
        raise ValueError(f"símbolo terminal também declarado não-terminal: {colisao}")
    return terminais, nao_terminais


def PRODUCAO_FINITA(esquerda, direita):
    return (esquerda, tuple(direita))


def GRAMATICA_FINITA(nao_terminais, terminais, inicial, producoes):
    terminais, nao_terminais = TERMINAIS_E_NAO_TERMINAIS_FINITOS(terminais, nao_terminais)
    if inicial not in nao_terminais:
        raise ValueError("símbolo inicial precisa ser não-terminal")
    normalizadas = []
    for esquerda, direita in producoes:
        if esquerda not in nao_terminais:
            raise ValueError(f"lado esquerdo não-terminal desconhecido: {esquerda}")
        for simbolo in direita:
            if simbolo not in terminais and simbolo not in nao_terminais:
                raise ValueError(f"símbolo fora do alfabeto gramatical: {simbolo}")
        normalizadas.append(PRODUCAO_FINITA(esquerda, direita))
    return {
        "nao_terminais": nao_terminais,
        "terminais": terminais,
        "inicial": inicial,
        "producoes": tuple(normalizadas),
    }


def EH_TERMINAL_FINITO(gramatica, simbolo):
    return _bool(simbolo in gramatica["terminais"])


def EH_NAO_TERMINAL_FINITO(gramatica, simbolo):
    return _bool(simbolo in gramatica["nao_terminais"])


def FORMA_SENTENCIAL_INICIAL_FINITA(gramatica):
    return (gramatica["inicial"],)


def EH_PALAVRA_TERMINAL_FINITA(gramatica, forma):
    return _bool(all(simbolo in gramatica["terminais"] for simbolo in forma))


def DERIVACAO_UM_PASSO_FINITA(gramatica, forma):
    forma = tuple(forma)
    saidas = []
    for indice, simbolo in enumerate(forma):
        if simbolo not in gramatica["nao_terminais"]:
            continue
        for esquerda, direita in gramatica["producoes"]:
            if esquerda != simbolo:
                continue
            nova = forma[:indice] + direita + forma[indice + 1:]
            if nova not in saidas:
                saidas.append(nova)
    return tuple(saidas)


def DERIVAR_ATE_FINITO(gramatica, passos):
    atuais = (FORMA_SENTENCIAL_INICIAL_FINITA(gramatica),)
    vistas = list(atuais)
    for _ in range(passos):
        proximas = []
        for forma in atuais:
            for nova in DERIVACAO_UM_PASSO_FINITA(gramatica, forma):
                if nova not in vistas:
                    vistas.append(nova)
                if nova not in proximas:
                    proximas.append(nova)
        atuais = tuple(proximas)
        if not atuais:
            break
    return tuple(vistas)


def PALAVRAS_GERADAS_ATE_FINITO(gramatica, passos, tamanho_maximo=None):
    palavras = []
    for forma in DERIVAR_ATE_FINITO(gramatica, passos):
        if not _bool_to_py(EH_PALAVRA_TERMINAL_FINITA(gramatica, forma)):
            continue
        if tamanho_maximo is not None and len(forma) > tamanho_maximo:
            continue
        if forma not in palavras:
            palavras.append(forma)
    return tuple(palavras)


def DERIVAVEL_EM_ATE_FINITO(gramatica, palavra, passos):
    return _bool(tuple(palavra) in PALAVRAS_GERADAS_ATE_FINITO(gramatica, passos))


def EPSILON_FINITO():
    return tuple()


def FECHAMENTO_DERIVACAO_FINITA():
    return V


# ------------------------------------------------------------------------------
# Etapas 451-460 — gramáticas regulares, tradução para DFA e operações finitas.
# ------------------------------------------------------------------------------
def EH_GRAMATICA_REGULAR_DIREITA_FINITA(gramatica):
    for esquerda, direita in gramatica["producoes"]:
        if esquerda not in gramatica["nao_terminais"]:
            return F
        if direita == tuple():
            continue
        if len(direita) == 1 and direita[0] in gramatica["terminais"]:
            continue
        if len(direita) == 2 and direita[0] in gramatica["terminais"] and direita[1] in gramatica["nao_terminais"]:
            continue
        return F
    return V


def GRAMATICA_REGULAR_PARA_DFA_FINITO(gramatica):
    if not _bool_to_py(EH_GRAMATICA_REGULAR_DIREITA_FINITA(gramatica)):
        raise ValueError("só gramáticas lineares à direita podem ser traduzidas aqui")
    final = "__FINAL__"
    estados = _unicos(gramatica["nao_terminais"] + (final, "__LIXO__"))
    transicao = {}
    finais = [final]
    if any(esq == gramatica["inicial"] and dir_ == tuple() for esq, dir_ in gramatica["producoes"]):
        finais.append(gramatica["inicial"])
    for estado in estados:
        for terminal in gramatica["terminais"]:
            transicao[(estado, terminal)] = "__LIXO__"
    for esquerda, direita in gramatica["producoes"]:
        if direita == tuple():
            if esquerda not in finais:
                finais.append(esquerda)
        elif len(direita) == 1:
            transicao[(esquerda, direita[0])] = final
        else:
            transicao[(esquerda, direita[0])] = direita[1]
    return DFA_FINITO(estados, gramatica["terminais"], transicao, gramatica["inicial"], tuple(finais))


def GRAMATICA_E_DFA_CONCORDAM_FINITO(gramatica, palavras, passos):
    dfa = GRAMATICA_REGULAR_PARA_DFA_FINITO(gramatica)
    geradas = set(PALAVRAS_GERADAS_ATE_FINITO(gramatica, passos))
    for palavra in palavras:
        por_gramatica = tuple(palavra) in geradas
        por_dfa = _bool_to_py(ACEITA_DFA_FINITO(dfa, palavra))
        if por_gramatica != por_dfa:
            return F
    return V


def UNIAO_GRAMATICAS_FINITA(g1, g2, novo_inicial="S_UNIAO"):
    terminais = _unicos(g1["terminais"] + g2["terminais"])
    n1 = tuple(f"A_{x}" for x in g1["nao_terminais"])
    n2 = tuple(f"B_{x}" for x in g2["nao_terminais"])
    mapa1 = dict(zip(g1["nao_terminais"], n1))
    mapa2 = dict(zip(g2["nao_terminais"], n2))

    def renomear(mapa, producoes):
        saida = []
        for esq, dir_ in producoes:
            direita = tuple(mapa.get(s, s) for s in dir_)
            saida.append((mapa[esq], direita))
        return tuple(saida)

    producoes = (
        (novo_inicial, (mapa1[g1["inicial"]],)),
        (novo_inicial, (mapa2[g2["inicial"]],)),
    ) + renomear(mapa1, g1["producoes"]) + renomear(mapa2, g2["producoes"])
    return GRAMATICA_FINITA((novo_inicial,) + n1 + n2, terminais, novo_inicial, producoes)


def CONCATENACAO_GRAMATICAS_REGULARES_FINITA(g1, g2):
    # Construção operacional simples: substitui epsilon de g1 pelo inicial de g2.
    terminais = _unicos(g1["terminais"] + g2["terminais"])
    n1 = tuple(f"A_{x}" for x in g1["nao_terminais"])
    n2 = tuple(f"B_{x}" for x in g2["nao_terminais"])
    mapa1 = dict(zip(g1["nao_terminais"], n1))
    mapa2 = dict(zip(g2["nao_terminais"], n2))
    producoes = []
    for esq, dir_ in g1["producoes"]:
        if dir_ == tuple():
            producoes.append((mapa1[esq], (mapa2[g2["inicial"]],)))
        else:
            producoes.append((mapa1[esq], tuple(mapa1.get(s, s) for s in dir_)))
    for esq, dir_ in g2["producoes"]:
        producoes.append((mapa2[esq], tuple(mapa2.get(s, s) for s in dir_)))
    return GRAMATICA_FINITA(n1 + n2, terminais, mapa1[g1["inicial"]], tuple(producoes))


def ESTRELA_LIMITADA_LINGUAGEM_FINITA(linguagem, limite_repeticoes):
    linguagem = tuple(tuple(p) for p in linguagem)
    resultado = {tuple()}
    fronteira = {tuple()}
    for _ in range(limite_repeticoes):
        nova = set()
        for base in fronteira:
            for palavra in linguagem:
                nova.add(base + palavra)
        resultado |= nova
        fronteira = nova
    return tuple(sorted(resultado, key=lambda p: (len(p), p)))


def FECHAMENTO_GRAMATICAS_REGULARES_FINITA():
    return V


# ------------------------------------------------------------------------------
# Etapas 461-480 — gramáticas livres de contexto e autômato de pilha finito.
# ------------------------------------------------------------------------------
def EH_PRODUCAO_LIVRE_CONTEXTO_FINITA(gramatica, producao):
    esquerda, _ = producao
    return _bool(esquerda in gramatica["nao_terminais"])


def ARVORE_DERIVACAO_FINITA(simbolo, filhos=()):
    return (simbolo, tuple(filhos))


def FOLHAS_ARVORE_DERIVACAO_FINITA(arvore):
    simbolo, filhos = arvore
    if not filhos:
        return (simbolo,) if simbolo is not None else tuple()
    resultado = tuple()
    for filho in filhos:
        resultado += FOLHAS_ARVORE_DERIVACAO_FINITA(filho)
    return resultado


def AUTOMATO_PILHA_FINITO(estados, alfabeto, simbolos_pilha, fundo, transicoes, inicial, finais, limite_pilha):
    return {
        "estados": tuple(estados),
        "alfabeto": tuple(alfabeto),
        "pilha": tuple(simbolos_pilha),
        "fundo": fundo,
        "transicoes": dict(transicoes),
        "inicial": inicial,
        "finais": tuple(finais),
        "limite_pilha": limite_pilha,
    }


def CONFIGURACAO_PILHA_FINITA(estado, restante, pilha):
    return (estado, tuple(restante), tuple(pilha))


def PASSOS_AUTOMATO_PILHA_FINITO(automato, configuracao):
    estado, restante, pilha = configuracao
    if not pilha:
        return tuple()
    topo = pilha[-1]
    simbolos_entrada = (None,)
    if restante:
        simbolos_entrada = (None, restante[0])
    saidas = []
    for simbolo in simbolos_entrada:
        chave = (estado, simbolo, topo)
        for novo_estado, empilhar in automato["transicoes"].get(chave, tuple()):
            novo_restante = restante[1:] if simbolo is not None else restante
            nova_pilha = pilha[:-1] + tuple(empilhar)
            if len(nova_pilha) <= automato["limite_pilha"]:
                saidas.append(CONFIGURACAO_PILHA_FINITA(novo_estado, novo_restante, nova_pilha))
    return tuple(saidas)


def ACEITA_PILHA_FINITA(automato, palavra, limite_passos):
    inicial = CONFIGURACAO_PILHA_FINITA(automato["inicial"], tuple(palavra), (automato["fundo"],))
    fronteira = (inicial,)
    vistas = set(fronteira)
    for _ in range(limite_passos + 1):
        for configuracao in fronteira:
            estado, restante, _pilha = configuracao
            if not restante and estado in automato["finais"]:
                return V
        proximas = []
        for configuracao in fronteira:
            for nova in PASSOS_AUTOMATO_PILHA_FINITO(automato, configuracao):
                if nova not in vistas:
                    vistas.add(nova)
                    proximas.append(nova)
        fronteira = tuple(proximas)
        if not fronteira:
            break
    return F


def AUTOMATO_PILHA_PARENTESIS_FINITO(limite_pilha):
    # Reconhece parênteses balanceados sobre '(' e ')' por estado final, com
    # pilha limitada declarada. O topo da pilha fica no fim da tupla.
    transicoes = {
        ("q", "(", "Z"): (("q", ("Z", "(")),),
        ("q", "(", "("): (("q", ("(", "(")),),
        ("q", ")", "("): (("q", tuple()),),
        ("q", None, "Z"): (("f", ("Z",)),),
    }
    return AUTOMATO_PILHA_FINITO(
        estados=("q", "f"),
        alfabeto=("(", ")"),
        simbolos_pilha=("Z", "("),
        fundo="Z",
        transicoes=transicoes,
        inicial="q",
        finais=("f",),
        limite_pilha=limite_pilha,
    )


def GRAMATICA_PARENTESIS_BALANCEADOS_FINITA():
    return GRAMATICA_FINITA(
        nao_terminais=("S",),
        terminais=("(", ")"),
        inicial="S",
        producoes=(
            ("S", tuple()),
            ("S", ("(", "S", ")", "S")),
        ),
    )


def GRAMATICA_E_PILHA_PARENTESIS_CONCORDAM_FINITA(palavras, passos_derivacao, limite_pilha, limite_passos):
    gramatica = GRAMATICA_PARENTESIS_BALANCEADOS_FINITA()
    automato = AUTOMATO_PILHA_PARENTESIS_FINITO(limite_pilha)
    geradas = set(PALAVRAS_GERADAS_ATE_FINITO(gramatica, passos_derivacao))
    for palavra in palavras:
        por_g = tuple(palavra) in geradas
        por_p = _bool_to_py(ACEITA_PILHA_FINITA(automato, palavra, limite_passos))
        if por_g != por_p:
            return F
    return V


def FECHAMENTO_GRAMATICAS_E_PILHA_FINITA():
    return V
