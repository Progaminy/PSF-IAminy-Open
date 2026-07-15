# ==============================================================================
# AUTÔMATOS FINITOS NATURAIS — Etapas 521 a 560 do PSF-IAminy.
# ==============================================================================
# Nasce depois de gramáticas e semântica operacional: uma máquina finita é uma
# relação de transição sobre estados finitos. Sem infinitos atuais, sem divisão,
# sem módulo, sem primalidade/fatoração.
# ==============================================================================
from .primitivas import V, F


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


def DFA_NATURAL_FINITO(estados, alfabeto, transicao, inicial, finais):
    estados = _unicos(tuple(estados))
    alfabeto = _unicos(tuple(alfabeto))
    finais = _unicos(tuple(finais))
    if inicial not in estados:
        raise ValueError("estado inicial fora do conjunto de estados")
    for f in finais:
        if f not in estados:
            raise ValueError("estado final fora do conjunto de estados")
    trans = {}
    for estado in estados:
        for simbolo in alfabeto:
            destino = transicao.get((estado, simbolo))
            if destino not in estados:
                raise ValueError(f"transição ausente ou destino inválido: {(estado, simbolo)}")
            trans[(estado, simbolo)] = destino
    return {"tipo": "dfa", "estados": estados, "alfabeto": alfabeto, "transicao": trans, "inicial": inicial, "finais": finais}


def PASSO_DFA_NATURAL(dfa, estado, simbolo):
    if simbolo not in dfa["alfabeto"]:
        raise ValueError("símbolo fora do alfabeto")
    return dfa["transicao"][(estado, simbolo)]


def EXECUTAR_DFA_NATURAL(dfa, palavra):
    estado = dfa["inicial"]
    traco = [estado]
    for simbolo in tuple(palavra):
        estado = PASSO_DFA_NATURAL(dfa, estado, simbolo)
        traco.append(estado)
    return tuple(traco)


def ACEITA_DFA_NATURAL(dfa, palavra):
    return _bool(EXECUTAR_DFA_NATURAL(dfa, palavra)[-1] in dfa["finais"])


def COMPLEMENTO_DFA_NATURAL(dfa):
    finais = tuple(e for e in dfa["estados"] if e not in dfa["finais"])
    return DFA_NATURAL_FINITO(dfa["estados"], dfa["alfabeto"], dfa["transicao"], dfa["inicial"], finais)


def PRODUTO_DFA_NATURAL(dfa1, dfa2, criterio_final):
    if dfa1["alfabeto"] != dfa2["alfabeto"]:
        raise ValueError("produto exige mesmo alfabeto")
    estados = tuple((a, b) for a in dfa1["estados"] for b in dfa2["estados"])
    trans = {}
    for estado in estados:
        for simbolo in dfa1["alfabeto"]:
            trans[(estado, simbolo)] = (PASSO_DFA_NATURAL(dfa1, estado[0], simbolo), PASSO_DFA_NATURAL(dfa2, estado[1], simbolo))
    finais = tuple(e for e in estados if criterio_final(e[0] in dfa1["finais"], e[1] in dfa2["finais"]))
    return DFA_NATURAL_FINITO(estados, dfa1["alfabeto"], trans, (dfa1["inicial"], dfa2["inicial"]), finais)


def UNIAO_DFA_NATURAL(dfa1, dfa2):
    return PRODUTO_DFA_NATURAL(dfa1, dfa2, lambda a, b: a or b)


def INTERSECAO_DFA_NATURAL(dfa1, dfa2):
    return PRODUTO_DFA_NATURAL(dfa1, dfa2, lambda a, b: a and b)


def NFA_NATURAL_FINITO(estados, alfabeto, transicao, inicial, finais, epsilon="ε"):
    estados = _unicos(tuple(estados))
    alfabeto = _unicos(tuple(alfabeto))
    finais = _unicos(tuple(finais))
    if inicial not in estados:
        raise ValueError("estado inicial fora do conjunto de estados")
    trans = {}
    for chave, destinos in transicao.items():
        estado, simbolo = chave
        if estado not in estados:
            raise ValueError("estado de transição desconhecido")
        if simbolo != epsilon and simbolo not in alfabeto:
            raise ValueError("símbolo de transição desconhecido")
        norm = tuple(d for d in destinos if d in estados)
        if len(norm) != len(tuple(destinos)):
            raise ValueError("destino desconhecido")
        trans[(estado, simbolo)] = _unicos(norm)
    return {"tipo": "nfa", "estados": estados, "alfabeto": alfabeto, "transicao": trans, "inicial": inicial, "finais": finais, "epsilon": epsilon}


def FECHO_EPSILON_NATURAL(nfa, estados):
    vistos = list(_unicos(tuple(estados)))
    mudou = True
    while mudou:
        mudou = False
        for estado in tuple(vistos):
            for destino in nfa["transicao"].get((estado, nfa["epsilon"]), tuple()):
                if destino not in vistos:
                    vistos.append(destino)
                    mudou = True
    return tuple(vistos)


def MOVER_NFA_NATURAL(nfa, estados, simbolo):
    saida = []
    for estado in FECHO_EPSILON_NATURAL(nfa, estados):
        for destino in nfa["transicao"].get((estado, simbolo), tuple()):
            if destino not in saida:
                saida.append(destino)
    return FECHO_EPSILON_NATURAL(nfa, saida)


def ACEITA_NFA_NATURAL(nfa, palavra):
    atuais = FECHO_EPSILON_NATURAL(nfa, (nfa["inicial"],))
    for simbolo in tuple(palavra):
        atuais = MOVER_NFA_NATURAL(nfa, atuais, simbolo)
    return _bool(any(e in nfa["finais"] for e in atuais))


def NFA_PARA_DFA_NATURAL(nfa):
    inicial = tuple(sorted(FECHO_EPSILON_NATURAL(nfa, (nfa["inicial"],)), key=str))
    estados = [inicial]
    trans = {}
    i = 0
    while i < len(estados):
        atual = estados[i]
        for simbolo in nfa["alfabeto"]:
            destino = tuple(sorted(MOVER_NFA_NATURAL(nfa, atual, simbolo), key=str))
            if destino not in estados:
                estados.append(destino)
            trans[(atual, simbolo)] = destino
        i += 1
    finais = tuple(e for e in estados if any(x in nfa["finais"] for x in e))
    return DFA_NATURAL_FINITO(tuple(estados), nfa["alfabeto"], trans, inicial, finais)


def EQUIVALENTES_EM_CATALOGO_DFA(dfa1, dfa2, catalogo):
    for palavra in catalogo:
        if _bool_to_py(ACEITA_DFA_NATURAL(dfa1, palavra)) != _bool_to_py(ACEITA_DFA_NATURAL(dfa2, palavra)):
            return F
    return V


def FECHAMENTO_AUTOMATOS_FINITOS_NATURAIS():
    return V
