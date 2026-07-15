# ==============================================================================
# LINGUAGENS REGULARES NATURAIS — Etapas 561 a 600 do PSF-IAminy.
# ==============================================================================
# Expressões regulares aparecem depois de autômatos finitos. Toda operação de
# estrela é limitada por profundidade declarada quando enumerada.
# ==============================================================================
from .primitivas import V, F
from .automatos_finitos_naturais import NFA_NATURAL_FINITO, ACEITA_NFA_NATURAL, NFA_PARA_DFA_NATURAL, ACEITA_DFA_NATURAL


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


def VAZIO_REGEX():
    return ("vazio",)


def EPSILON_REGEX():
    return ("epsilon",)


def SIMBOLO_REGEX(simbolo):
    return ("simbolo", simbolo)


def UNIAO_REGEX(a, b):
    return ("uniao", a, b)


def CONCAT_REGEX(a, b):
    return ("concat", a, b)


def ESTRELA_REGEX(a):
    return ("estrela", a)


def ENUMERAR_REGEX_LIMITADO(regex, limite_estrela=3, tamanho_maximo=6):
    tipo = regex[0]
    if tipo == "vazio":
        return tuple()
    if tipo == "epsilon":
        return (tuple(),)
    if tipo == "simbolo":
        return ((regex[1],),) if tamanho_maximo >= 1 else tuple()
    if tipo == "uniao":
        return _unicos(ENUMERAR_REGEX_LIMITADO(regex[1], limite_estrela, tamanho_maximo) + ENUMERAR_REGEX_LIMITADO(regex[2], limite_estrela, tamanho_maximo))
    if tipo == "concat":
        saida = []
        for a in ENUMERAR_REGEX_LIMITADO(regex[1], limite_estrela, tamanho_maximo):
            for b in ENUMERAR_REGEX_LIMITADO(regex[2], limite_estrela, tamanho_maximo):
                p = a + b
                if len(p) <= tamanho_maximo and p not in saida:
                    saida.append(p)
        return tuple(saida)
    if tipo == "estrela":
        base = ENUMERAR_REGEX_LIMITADO(regex[1], limite_estrela, tamanho_maximo)
        palavras = [tuple()]
        atuais = [tuple()]
        for _ in range(limite_estrela):
            proximas = []
            for pref in atuais:
                for frag in base:
                    p = pref + frag
                    if len(p) <= tamanho_maximo:
                        if p not in palavras:
                            palavras.append(p)
                        if p not in proximas:
                            proximas.append(p)
            atuais = proximas
        return tuple(palavras)
    raise ValueError(f"regex desconhecida: {tipo}")


def LINGUAGEM_REGEX_CONTEM_LIMITADO(regex, palavra, limite_estrela=3):
    return _bool(tuple(palavra) in ENUMERAR_REGEX_LIMITADO(regex, limite_estrela, len(tuple(palavra))))


def ALFABETO_REGEX(regex):
    tipo = regex[0]
    if tipo in {"vazio", "epsilon"}:
        return tuple()
    if tipo == "simbolo":
        return (regex[1],)
    if tipo == "estrela":
        return ALFABETO_REGEX(regex[1])
    return _unicos(ALFABETO_REGEX(regex[1]) + ALFABETO_REGEX(regex[2]))


def REGEX_PARA_NFA_NATURAL(regex):
    contador = {"n": 0}

    def novo():
        contador["n"] += 1
        return f"q{contador['n']}"

    def construir(r):
        tipo = r[0]
        inicio, fim = novo(), novo()
        if tipo == "vazio":
            return (inicio, fim, (inicio, fim), {})
        if tipo == "epsilon":
            return (inicio, fim, (inicio, fim), {(inicio, "ε"): (fim,)})
        if tipo == "simbolo":
            return (inicio, fim, (inicio, fim), {(inicio, r[1]): (fim,)})
        if tipo == "uniao":
            i1, f1, e1, t1 = construir(r[1])
            i2, f2, e2, t2 = construir(r[2])
            estados = (inicio, fim) + e1 + e2
            trans = dict(t1)
            trans.update(t2)
            trans[(inicio, "ε")] = (i1, i2)
            trans[(f1, "ε")] = (fim,)
            trans[(f2, "ε")] = (fim,)
            return inicio, fim, estados, trans
        if tipo == "concat":
            i1, f1, e1, t1 = construir(r[1])
            i2, f2, e2, t2 = construir(r[2])
            trans = dict(t1)
            trans.update(t2)
            trans[(f1, "ε")] = (i2,)
            return i1, f2, e1 + e2, trans
        if tipo == "estrela":
            i1, f1, e1, t1 = construir(r[1])
            trans = dict(t1)
            trans[(inicio, "ε")] = (i1, fim)
            trans[(f1, "ε")] = (i1, fim)
            return inicio, fim, (inicio, fim) + e1, trans
        raise ValueError("regex desconhecida")

    inicial, final, estados, trans = construir(regex)
    return NFA_NATURAL_FINITO(_unicos(estados), ALFABETO_REGEX(regex), trans, inicial, (final,))


def REGEX_E_NFA_CONCORDAM_CATALOGO(regex, catalogo, limite_estrela=4):
    nfa = REGEX_PARA_NFA_NATURAL(regex)
    for palavra in catalogo:
        a = _bool_to_py(LINGUAGEM_REGEX_CONTEM_LIMITADO(regex, palavra, limite_estrela))
        b = _bool_to_py(ACEITA_NFA_NATURAL(nfa, palavra))
        if a != b:
            return F
    return V


def REGEX_E_DFA_CONCORDAM_CATALOGO(regex, catalogo, limite_estrela=4):
    dfa = NFA_PARA_DFA_NATURAL(REGEX_PARA_NFA_NATURAL(regex))
    for palavra in catalogo:
        a = _bool_to_py(LINGUAGEM_REGEX_CONTEM_LIMITADO(regex, palavra, limite_estrela))
        b = _bool_to_py(ACEITA_DFA_NATURAL(dfa, palavra))
        if a != b:
            return F
    return V


def FECHAMENTO_LINGUAGENS_REGULARES_NATURAIS():
    return V
