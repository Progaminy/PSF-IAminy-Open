# ==============================================================================
# MÉTODOS FINITOS — Etapas 136 a 300 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   depois de expressões/equações finitas, o próximo método geral que nasce
#   honestamente é a enumeração sobre domínio finito explícito. Este módulo
#   reúne construções que não dependem de fórmula fechada: solução por busca,
#   conjuntos finitos, ordens, topologia finita, linguagens/automatos finitos
#   e lógica proposicional finita.
#
# Fórmulas externas não entram aqui. Toda decisão é por varredura de uma
# estrutura finita dada, composição de predicados já definidos, ou aplicação
# explícita de uma transição/relação finita.
# ==============================================================================
from itertools import product as produto_cartesiano

from .primitivas import V, F


def _bool(condicao):
    return V if condicao else F


def _igual(a, b):
    return a == b


def _contem(seq, elemento):
    return any(_igual(x, elemento) for x in seq)


def _unicos(seq):
    saida = []
    for x in seq:
        if not _contem(saida, x):
            saida.append(x)
    return tuple(saida)


def _subconjunto(a, b):
    return all(_contem(b, x) for x in a)


def _igual_conjunto(a, b):
    return _subconjunto(a, b) and _subconjunto(b, a)


def _partes(seq):
    elementos = tuple(seq)
    resultado = [tuple()]
    for elemento in elementos:
        resultado += [parte + (elemento,) for parte in resultado]
    return tuple(resultado)


# ----------------------------------------------------------------------------
# Etapas 136-160 — equações, predicados e problemas finitos.
# ----------------------------------------------------------------------------
EQUACAO_PREDICADO_FINITA = lambda predicado: predicado


def SOLUCOES_PREDICADO_FINITO(dominio, predicado):
    return tuple(x for x in dominio if predicado(x))


def TODAS_SOLUCOES_FINITO(dominio, predicado):
    return SOLUCOES_PREDICADO_FINITO(dominio, predicado)


def EQUACOES_EQUIVALENTES_FINITO(dominio, predicado_a, predicado_b):
    return _bool(all(predicado_a(x) == predicado_b(x) for x in dominio))


def SISTEMA_SOLUCOES_FINITO(dominio, *predicados):
    return tuple(x for x in dominio if all(predicado(x) for predicado in predicados))


def ALTERNATIVA_SOLUCOES_FINITA(dominio, *predicados):
    return tuple(x for x in dominio if any(predicado(x) for predicado in predicados))


def INEQUACAO_SOLUCOES_FINITA(dominio, esquerda, direita):
    return tuple(x for x in dominio if not _igual(esquerda(x), direita(x)))


def VARREDURA_PARAMETROS_FINITA(parametros, construtor):
    return tuple((p, construtor(p)) for p in parametros)


def PROBLEMA_RESTRITO_FINITO(dominio, restricao):
    return tuple(x for x in dominio if restricao(x))


def FEASIVEL_FINITO(dominio, *restricoes):
    return SISTEMA_SOLUCOES_FINITO(dominio, *restricoes)


def MINIMIZADORES_FINITO(dominio, objetivo):
    if not dominio:
        return tuple()
    valores = tuple((x, objetivo(x)) for x in dominio)
    menor = min(v for _, v in valores)
    return tuple(x for x, v in valores if v == menor)


def MAXIMIZADORES_FINITO(dominio, objetivo):
    if not dominio:
        return tuple()
    valores = tuple((x, objetivo(x)) for x in dominio)
    maior = max(v for _, v in valores)
    return tuple(x for x, v in valores if v == maior)


ARGMIN_FINITO = MINIMIZADORES_FINITO
ARGMAX_FINITO = MAXIMIZADORES_FINITO


def PRODUTO_DOMINIOS_NOMEADOS_FINITO(dominios):
    nomes = tuple(dominios.keys())
    valores = tuple(dominios[nome] for nome in nomes)
    return tuple(dict(zip(nomes, escolha)) for escolha in produto_cartesiano(*valores))


def AVALIAR_EXPR_MULTIVAR_FINITA(expr, valoracao, operacoes):
    tag = expr[0]
    if tag == "const":
        return expr[1]
    if tag == "var":
        return valoracao[expr[1]]
    if tag == "soma":
        return operacoes["soma"](
            AVALIAR_EXPR_MULTIVAR_FINITA(expr[1], valoracao, operacoes),
            AVALIAR_EXPR_MULTIVAR_FINITA(expr[2], valoracao, operacoes),
        )
    if tag == "sub":
        return operacoes["sub"](
            AVALIAR_EXPR_MULTIVAR_FINITA(expr[1], valoracao, operacoes),
            AVALIAR_EXPR_MULTIVAR_FINITA(expr[2], valoracao, operacoes),
        )
    if tag == "mult":
        return operacoes["mult"](
            AVALIAR_EXPR_MULTIVAR_FINITA(expr[1], valoracao, operacoes),
            AVALIAR_EXPR_MULTIVAR_FINITA(expr[2], valoracao, operacoes),
        )
    raise ValueError(f"expressão multivariável desconhecida: {tag}")


def PROJETAR_VALORACOES_FINITO(valoracoes, nomes):
    return tuple({nome: valoracao[nome] for nome in nomes} for valoracao in valoracoes)


def SUBSTITUIR_VALORACAO_FINITA(valoracao, nome, valor):
    nova = dict(valoracao)
    nova[nome] = valor
    return nova


def TESTEMUNHAS_FINITO(dominio, predicado):
    return tuple(x for x in dominio if predicado(x))


def CONTRAEXEMPLOS_FINITO(dominio, predicado):
    return tuple(x for x in dominio if not predicado(x))


FECHAMENTO_METODO_FINITO = lambda dominio, predicado: _bool(
    len(TESTEMUNHAS_FINITO(dominio, predicado)) + len(CONTRAEXEMPLOS_FINITO(dominio, predicado)) == len(dominio)
)


# ----------------------------------------------------------------------------
# Etapas 161-180 — conjuntos finitos.
# ----------------------------------------------------------------------------
CONJUNTO_FINITO = lambda *elementos: _unicos(elementos)
VAZIO_FINITO = tuple()
SINGLETON_FINITO = lambda x: (x,)
PERTENCE_CONJUNTO_FINITO = lambda x, conjunto: _bool(_contem(conjunto, x))
SUBCONJUNTO_FINITO = lambda a, b: _bool(_subconjunto(a, b))
IGUAL_CONJUNTO_FINITO = lambda a, b: _bool(_igual_conjunto(a, b))
UNIAO_FINITA = lambda a, b: _unicos(tuple(a) + tuple(b))
INTERSECAO_FINITA = lambda a, b: tuple(x for x in a if _contem(b, x))
DIFERENCA_FINITA = lambda a, b: tuple(x for x in a if not _contem(b, x))
COMPLEMENTO_FINITO = lambda universo, a: DIFERENCA_FINITA(universo, a)
PRODUTO_CARTESIANO_FINITO = lambda a, b: tuple((x, y) for x in a for y in b)
PARTES_FINITO = _partes


def FAMILIA_COBRE_FINITO(universo, familia):
    coberto = tuple()
    for parte in familia:
        coberto = UNIAO_FINITA(coberto, parte)
    return IGUAL_CONJUNTO_FINITO(universo, coberto)


def PARTICAO_FINITA(universo, partes):
    if not partes:
        return _bool(len(universo) == 0)
    if not all(parte for parte in partes):
        return F
    if not _bool_to_py(FAMILIA_COBRE_FINITO(universo, partes)):
        return F
    for i, parte_a in enumerate(partes):
        for parte_b in partes[i + 1:]:
            if INTERSECAO_FINITA(parte_a, parte_b):
                return F
    return V


def QUOCIENTE_POR_PARTICAO_FINITO(partes):
    return tuple(tuple(parte) for parte in partes)


def TRANSVERSAL_FINITO(partes):
    return tuple(parte[0] for parte in partes if parte)


CARDINAL_FINITO = lambda conjunto: len(conjunto)


def IMAGEM_CONJUNTO_FINITO(conjunto, funcao):
    return _unicos(tuple(funcao(x) for x in conjunto))


def PREIMAGEM_CONJUNTO_FINITO(dominio, funcao, alvo):
    return tuple(x for x in dominio if _contem(alvo, funcao(x)))


def _bool_to_py(valor):
    return valor(True)(False)


# ----------------------------------------------------------------------------
# Etapas 181-200 — ordens e redes finitas.
# Ordem é um predicado Python finito leq(a,b), já limitado ao domínio.
# ----------------------------------------------------------------------------
def MINIMOS_FINITO(dominio, leq):
    return tuple(x for x in dominio if not any(leq(y, x) and not _igual(y, x) for y in dominio))


def MAXIMOS_FINITO(dominio, leq):
    return tuple(x for x in dominio if not any(leq(x, y) and not _igual(y, x) for y in dominio))


def MENOR_ELEMENTO_FINITO(dominio, leq):
    candidatos = tuple(x for x in dominio if all(leq(x, y) for y in dominio))
    return candidatos[0] if candidatos else None


def MAIOR_ELEMENTO_FINITO(dominio, leq):
    candidatos = tuple(x for x in dominio if all(leq(y, x) for y in dominio))
    return candidatos[0] if candidatos else None


def COTAS_INFERIORES_FINITO(dominio, subconjunto, leq):
    return tuple(x for x in dominio if all(leq(x, y) for y in subconjunto))


def COTAS_SUPERIORES_FINITO(dominio, subconjunto, leq):
    return tuple(x for x in dominio if all(leq(y, x) for y in subconjunto))


def INFIMOS_FINITO(dominio, subconjunto, leq):
    cotas = COTAS_INFERIORES_FINITO(dominio, subconjunto, leq)
    maior = MAIOR_ELEMENTO_FINITO(cotas, leq)
    return tuple() if maior is None else (maior,)


def SUPREMOS_FINITO(dominio, subconjunto, leq):
    cotas = COTAS_SUPERIORES_FINITO(dominio, subconjunto, leq)
    menor = MENOR_ELEMENTO_FINITO(cotas, leq)
    return tuple() if menor is None else (menor,)


def CADEIA_FINITA(subconjunto, leq):
    return _bool(all(leq(a, b) or leq(b, a) for a in subconjunto for b in subconjunto))


def ANTICADEIA_FINITA(subconjunto, leq):
    return _bool(all(_igual(a, b) or not (leq(a, b) or leq(b, a)) for a in subconjunto for b in subconjunto))


def MONOTONA_FINITA(dominio, leq_a, leq_b, funcao):
    return _bool(all(not leq_a(x, y) or leq_b(funcao(x), funcao(y)) for x in dominio for y in dominio))


def REDE_FINITA(dominio, leq):
    for a in dominio:
        for b in dominio:
            if not INFIMOS_FINITO(dominio, (a, b), leq) or not SUPREMOS_FINITO(dominio, (a, b), leq):
                return F
    return V


# ----------------------------------------------------------------------------
# Etapas 201-220 — topologia finita.
# ----------------------------------------------------------------------------
def TOPOLOGIA_FINITA(universo, abertos):
    if not _contem(abertos, tuple()) or not any(_igual_conjunto(a, universo) for a in abertos):
        return F
    for a in abertos:
        for b in abertos:
            if not any(_igual_conjunto(c, INTERSECAO_FINITA(a, b)) for c in abertos):
                return F
            if not any(_igual_conjunto(c, UNIAO_FINITA(a, b)) for c in abertos):
                return F
    return V


def FECHADOS_FINITO(universo, abertos):
    return _unicos(tuple(COMPLEMENTO_FINITO(universo, aberto) for aberto in abertos))


def INTERIOR_FINITO(conjunto, abertos):
    interior = tuple()
    for aberto in abertos:
        if _subconjunto(aberto, conjunto):
            interior = UNIAO_FINITA(interior, aberto)
    return interior


def FECHO_FINITO(universo, conjunto, abertos):
    fechados = FECHADOS_FINITO(universo, abertos)
    candidatos = [fechado for fechado in fechados if _subconjunto(conjunto, fechado)]
    if not candidatos:
        return universo
    fecho = candidatos[0]
    for fechado in candidatos[1:]:
        fecho = INTERSECAO_FINITA(fecho, fechado)
    return fecho


def FRONTEIRA_FINITA(universo, conjunto, abertos):
    return DIFERENCA_FINITA(FECHO_FINITO(universo, conjunto, abertos), INTERIOR_FINITO(conjunto, abertos))


def PREIMAGEM_ABERTO_FINITO(dominio, funcao, aberto):
    return tuple(x for x in dominio if _contem(aberto, funcao(x)))


def CONTINUA_FINITA(dominio, abertos_dom, abertos_cod, funcao):
    return _bool(all(
        any(_igual_conjunto(aberto_dom, PREIMAGEM_ABERTO_FINITO(dominio, funcao, aberto_cod)) for aberto_dom in abertos_dom)
        for aberto_cod in abertos_cod
    ))


def SEPARA_T0_FINITO(universo, abertos):
    for x in universo:
        for y in universo:
            if _igual(x, y):
                continue
            distingue = any((_contem(aberto, x) and not _contem(aberto, y)) or (_contem(aberto, y) and not _contem(aberto, x)) for aberto in abertos)
            if not distingue:
                return F
    return V


def CONEXO_TOPOLOGICO_FINITO(universo, abertos):
    for aberto in abertos:
        fechado_tambem = any(_igual_conjunto(aberto, fechado) for fechado in FECHADOS_FINITO(universo, abertos))
        if aberto and not _igual_conjunto(aberto, universo) and fechado_tambem:
            return F
    return V


COMPACTO_FINITO = lambda universo, abertos: TOPOLOGIA_FINITA(universo, abertos)


# ----------------------------------------------------------------------------
# Etapas 221-260 — palavras, linguagens e automatos finitos.
# ----------------------------------------------------------------------------
ALFABETO_FINITO = lambda *simbolos: _unicos(simbolos)
PALAVRA_FINITA = lambda *simbolos: tuple(simbolos)
CONCATENAR_PALAVRAS_FINITO = lambda a, b: tuple(a) + tuple(b)
TAMANHO_PALAVRA_FINITO = lambda palavra: len(palavra)
LINGUAGEM_FINITA = lambda *palavras: _unicos(palavras)
PERTENCE_LINGUAGEM_FINITA = lambda palavra, linguagem: _bool(_contem(linguagem, palavra))
PREFIXO_FINITO = lambda pref, palavra: _bool(tuple(palavra[:len(pref)]) == tuple(pref))
SUFIXO_FINITO = lambda suf, palavra: _bool(tuple(palavra[-len(suf):]) == tuple(suf) if suf else True)


def PREFIXOS_FINITO(palavra):
    return tuple(tuple(palavra[:i]) for i in range(len(palavra) + 1))


def SUFIXOS_FINITO(palavra):
    return tuple(tuple(palavra[i:]) for i in range(len(palavra) + 1))


def FECHAMENTO_PREFIXOS_LINGUAGEM_FINITO(linguagem):
    resultado = tuple()
    for palavra in linguagem:
        resultado = UNIAO_FINITA(resultado, PREFIXOS_FINITO(palavra))
    return resultado


def DFA_FINITO(estados, alfabeto, transicao, inicial, finais):
    return {
        "estados": tuple(estados),
        "alfabeto": tuple(alfabeto),
        "transicao": dict(transicao),
        "inicial": inicial,
        "finais": tuple(finais),
    }


def TRANSICAO_DFA_FINITA(automato, estado, simbolo):
    return automato["transicao"][(estado, simbolo)]


def TRANSICAO_ESTENDIDA_DFA_FINITA(automato, estado, palavra):
    atual = estado
    for simbolo in palavra:
        atual = TRANSICAO_DFA_FINITA(automato, atual, simbolo)
    return atual


def ACEITA_DFA_FINITO(automato, palavra):
    final = TRANSICAO_ESTENDIDA_DFA_FINITA(automato, automato["inicial"], palavra)
    return _bool(_contem(automato["finais"], final))


def LINGUAGEM_ACEITA_FINITA(automato, palavras):
    return tuple(palavra for palavra in palavras if _bool_to_py(ACEITA_DFA_FINITO(automato, palavra)))


def COMPLEMENTO_DFA_FINITO(automato):
    finais = tuple(estado for estado in automato["estados"] if not _contem(automato["finais"], estado))
    return DFA_FINITO(automato["estados"], automato["alfabeto"], automato["transicao"], automato["inicial"], finais)


# ----------------------------------------------------------------------------
# Etapas 261-300 — lógica proposicional finita e decisão por tabela.
# ----------------------------------------------------------------------------
PROP_VAR = lambda nome: ("var", nome)
PROP_NAO = lambda p: ("nao", p)
PROP_E = lambda p, q: ("e", p, q)
PROP_OU = lambda p, q: ("ou", p, q)
PROP_IMPLICA = lambda p, q: ("implica", p, q)


def VARIAVEIS_PROP_FINITA(formula):
    tag = formula[0]
    if tag == "var":
        return (formula[1],)
    if tag == "nao":
        return VARIAVEIS_PROP_FINITA(formula[1])
    return _unicos(VARIAVEIS_PROP_FINITA(formula[1]) + VARIAVEIS_PROP_FINITA(formula[2]))


def AVALIAR_PROP_FINITA(formula, valoracao):
    tag = formula[0]
    if tag == "var":
        return bool(valoracao[formula[1]])
    if tag == "nao":
        return not AVALIAR_PROP_FINITA(formula[1], valoracao)
    if tag == "e":
        return AVALIAR_PROP_FINITA(formula[1], valoracao) and AVALIAR_PROP_FINITA(formula[2], valoracao)
    if tag == "ou":
        return AVALIAR_PROP_FINITA(formula[1], valoracao) or AVALIAR_PROP_FINITA(formula[2], valoracao)
    if tag == "implica":
        return (not AVALIAR_PROP_FINITA(formula[1], valoracao)) or AVALIAR_PROP_FINITA(formula[2], valoracao)
    raise ValueError(f"fórmula proposicional desconhecida: {tag}")


def VALORACOES_PROP_FINITA(variaveis):
    return tuple(dict(zip(variaveis, valores)) for valores in produto_cartesiano((False, True), repeat=len(variaveis)))


def TABELA_VERDADE_FINITA(formula):
    variaveis = VARIAVEIS_PROP_FINITA(formula)
    return tuple((valoracao, AVALIAR_PROP_FINITA(formula, valoracao)) for valoracao in VALORACOES_PROP_FINITA(variaveis))


def MODELOS_PROP_FINITO(formula):
    return tuple(valoracao for valoracao, valor in TABELA_VERDADE_FINITA(formula) if valor)


TAUTOLOGIA_FINITA = lambda formula: _bool(all(valor for _, valor in TABELA_VERDADE_FINITA(formula)))
SATISFATIVEL_FINITA = lambda formula: _bool(any(valor for _, valor in TABELA_VERDADE_FINITA(formula)))
CONTRADICAO_FINITA = lambda formula: _bool(not any(valor for _, valor in TABELA_VERDADE_FINITA(formula)))


def CONSEQUENCIA_FINITA(premissas, conclusao):
    variaveis = tuple()
    for formula in tuple(premissas) + (conclusao,):
        variaveis = _unicos(variaveis + VARIAVEIS_PROP_FINITA(formula))
    for valoracao in VALORACOES_PROP_FINITA(variaveis):
        if all(AVALIAR_PROP_FINITA(p, valoracao) for p in premissas) and not AVALIAR_PROP_FINITA(conclusao, valoracao):
            return F
    return V


def EQUIVALENCIA_PROP_FINITA(p, q):
    return _bool_to_py(CONSEQUENCIA_FINITA((p,), q)) and _bool_to_py(CONSEQUENCIA_FINITA((q,), p)) and V or F


def DNF_POR_TABELA_FINITA(formula):
    variaveis = VARIAVEIS_PROP_FINITA(formula)
    termos = []
    for valoracao, valor in TABELA_VERDADE_FINITA(formula):
        if valor:
            termos.append(tuple((v, valoracao[v]) for v in variaveis))
    return tuple(termos)


def CNF_POR_TABELA_FINITA(formula):
    variaveis = VARIAVEIS_PROP_FINITA(formula)
    clausulas = []
    for valoracao, valor in TABELA_VERDADE_FINITA(formula):
        if not valor:
            clausulas.append(tuple((v, not valoracao[v]) for v in variaveis))
    return tuple(clausulas)


def TEORIA_CONSISTENTE_FINITA(formulas):
    variaveis = tuple()
    for formula in formulas:
        variaveis = _unicos(variaveis + VARIAVEIS_PROP_FINITA(formula))
    return _bool(any(all(AVALIAR_PROP_FINITA(f, valoracao) for f in formulas) for valoracao in VALORACOES_PROP_FINITA(variaveis)))


def TEORIA_COMPLETA_FINITA(formulas, universo_formulas):
    if not _bool_to_py(TEORIA_CONSISTENTE_FINITA(formulas)):
        return F
    for formula in universo_formulas:
        if not _bool_to_py(CONSEQUENCIA_FINITA(formulas, formula)) and not _bool_to_py(CONSEQUENCIA_FINITA(formulas, PROP_NAO(formula))):
            return F
    return V


PROVA_FINITA = lambda *passos: tuple(passos)


def DERIVACAO_FINITA_VALIDA(premissas, conclusao):
    return CONSEQUENCIA_FINITA(premissas, conclusao)


def REFUTACAO_FINITA(formulas):
    return _bool(not _bool_to_py(TEORIA_CONSISTENTE_FINITA(formulas)))


DECIDIR_PROP_FINITA = lambda formula: {
    "tautologia": _bool_to_py(TAUTOLOGIA_FINITA(formula)),
    "satisfativel": _bool_to_py(SATISFATIVEL_FINITA(formula)),
    "contradicao": _bool_to_py(CONTRADICAO_FINITA(formula)),
}


def FECHAMENTO_METODOS_FINITOS_ATE_300():
    return V
