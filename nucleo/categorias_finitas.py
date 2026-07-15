# ==============================================================================
# CATEGORIAS FINITAS — Etapas 301 a 340 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   depois de relações, funções, composição, identidade e métodos finitos,
#   uma categoria finita nasce como estrutura operacional finita:
#   objetos, morfismos, origem, alvo, identidades e composição.
#
# Não usamos teoremas externos. Os axiomas de categoria, functor e
# naturalidade são verificados por enumeração explícita das tabelas finitas.
# ==============================================================================
from .primitivas import V, F


def _bool(condicao):
    return V if condicao else F


def _py_bool(valor):
    return valor(True)(False)


def CATEGORIA_FINITA(objetos, morfismos, origem, alvo, identidade, composicao):
    return {
        "objetos": tuple(objetos),
        "morfismos": tuple(morfismos),
        "origem": dict(origem),
        "alvo": dict(alvo),
        "identidade": dict(identidade),
        "composicao": dict(composicao),
    }


OBJETOS_DE = lambda categoria: categoria["objetos"]
MORFISMOS_DE = lambda categoria: categoria["morfismos"]
ORIGEM_DE = lambda categoria, morfismo: categoria["origem"][morfismo]
ALVO_DE = lambda categoria, morfismo: categoria["alvo"][morfismo]
IDENTIDADE_DE = lambda categoria, objeto: categoria["identidade"][objeto]


def COMPONIVEIS(categoria, g, f):
    return ALVO_DE(categoria, f) == ORIGEM_DE(categoria, g)


def COMPOR(categoria, g, f):
    return categoria["composicao"][(g, f)]


def HOM_FINITO(categoria, origem, alvo):
    return tuple(
        f for f in MORFISMOS_DE(categoria)
        if ORIGEM_DE(categoria, f) == origem and ALVO_DE(categoria, f) == alvo
    )


def ENDOMORFISMOS_FINITO(categoria, objeto):
    return HOM_FINITO(categoria, objeto, objeto)


def _estrutura_basica_valida(categoria):
    objetos = OBJETOS_DE(categoria)
    morfismos = MORFISMOS_DE(categoria)
    origem = categoria["origem"]
    alvo = categoria["alvo"]
    identidade = categoria["identidade"]

    if set(identidade.keys()) != set(objetos):
        return False
    for f in morfismos:
        if f not in origem or f not in alvo:
            return False
        if origem[f] not in objetos or alvo[f] not in objetos:
            return False
    for objeto in objetos:
        ident = identidade[objeto]
        if ident not in morfismos:
            return False
        if origem[ident] != objeto or alvo[ident] != objeto:
            return False
    return True


def EH_CATEGORIA_FINITA(categoria):
    if not _estrutura_basica_valida(categoria):
        return F

    morfismos = MORFISMOS_DE(categoria)
    composicao = categoria["composicao"]

    for g in morfismos:
        for f in morfismos:
            if not COMPONIVEIS(categoria, g, f):
                continue
            if (g, f) not in composicao:
                return F
            gf = composicao[(g, f)]
            if gf not in morfismos:
                return F
            if ORIGEM_DE(categoria, gf) != ORIGEM_DE(categoria, f):
                return F
            if ALVO_DE(categoria, gf) != ALVO_DE(categoria, g):
                return F

    for f in morfismos:
        id_origem = IDENTIDADE_DE(categoria, ORIGEM_DE(categoria, f))
        id_alvo = IDENTIDADE_DE(categoria, ALVO_DE(categoria, f))
        if COMPOR(categoria, f, id_origem) != f:
            return F
        if COMPOR(categoria, id_alvo, f) != f:
            return F

    for h in morfismos:
        for g in morfismos:
            for f in morfismos:
                if COMPONIVEIS(categoria, g, f) and COMPONIVEIS(categoria, h, g):
                    esquerda = COMPOR(categoria, h, COMPOR(categoria, g, f))
                    direita = COMPOR(categoria, COMPOR(categoria, h, g), f)
                    if esquerda != direita:
                        return F
    return V


def ISOMORFISMOS_FINITO(categoria, a, b):
    saida = []
    for f in HOM_FINITO(categoria, a, b):
        for g in HOM_FINITO(categoria, b, a):
            if (
                COMPOR(categoria, g, f) == IDENTIDADE_DE(categoria, a)
                and COMPOR(categoria, f, g) == IDENTIDADE_DE(categoria, b)
            ):
                saida.append(f)
    return tuple(saida)


def OBJETOS_ISOMORFOS_FINITO(categoria, a, b):
    return _bool(bool(ISOMORFISMOS_FINITO(categoria, a, b)))


def AUTOMORFISMOS_FINITO(categoria, objeto):
    return ISOMORFISMOS_FINITO(categoria, objeto, objeto)


def SUBCATEGORIA_FINITA(categoria, objetos, morfismos):
    origem = {f: ORIGEM_DE(categoria, f) for f in morfismos}
    alvo = {f: ALVO_DE(categoria, f) for f in morfismos}
    identidade = {obj: IDENTIDADE_DE(categoria, obj) for obj in objetos}
    composicao = {
        (g, f): COMPOR(categoria, g, f)
        for g in morfismos for f in morfismos
        if COMPONIVEIS(categoria, g, f) and COMPOR(categoria, g, f) in morfismos
    }
    return CATEGORIA_FINITA(objetos, morfismos, origem, alvo, identidade, composicao)


def EH_SUBCATEGORIA_FINITA(categoria, subcategoria):
    if not _py_bool(EH_CATEGORIA_FINITA(subcategoria)):
        return F
    if not all(obj in OBJETOS_DE(categoria) for obj in OBJETOS_DE(subcategoria)):
        return F
    if not all(f in MORFISMOS_DE(categoria) for f in MORFISMOS_DE(subcategoria)):
        return F
    return V


def CATEGORIA_OPOSTA_FINITA(categoria):
    composicao_oposta = {}
    for g in MORFISMOS_DE(categoria):
        for f in MORFISMOS_DE(categoria):
            if ALVO_DE(categoria, g) == ORIGEM_DE(categoria, f):
                composicao_oposta[(g, f)] = COMPOR(categoria, f, g)
    return CATEGORIA_FINITA(
        OBJETOS_DE(categoria),
        MORFISMOS_DE(categoria),
        {f: ALVO_DE(categoria, f) for f in MORFISMOS_DE(categoria)},
        {f: ORIGEM_DE(categoria, f) for f in MORFISMOS_DE(categoria)},
        {obj: IDENTIDADE_DE(categoria, obj) for obj in OBJETOS_DE(categoria)},
        composicao_oposta,
    )


def FUNCTOR_FINITO(categoria_origem, categoria_alvo, objetos, morfismos):
    return {
        "origem": categoria_origem,
        "alvo": categoria_alvo,
        "objetos": dict(objetos),
        "morfismos": dict(morfismos),
    }


DIAGRAMA_FINITO = FUNCTOR_FINITO


def EH_FUNCTOR_FINITO(functor):
    c = functor["origem"]
    d = functor["alvo"]
    obj = functor["objetos"]
    mor = functor["morfismos"]

    if set(obj.keys()) != set(OBJETOS_DE(c)):
        return F
    if set(mor.keys()) != set(MORFISMOS_DE(c)):
        return F
    for a in OBJETOS_DE(c):
        if obj[a] not in OBJETOS_DE(d):
            return F
        if mor[IDENTIDADE_DE(c, a)] != IDENTIDADE_DE(d, obj[a]):
            return F
    for f in MORFISMOS_DE(c):
        if mor[f] not in MORFISMOS_DE(d):
            return F
        if ORIGEM_DE(d, mor[f]) != obj[ORIGEM_DE(c, f)]:
            return F
        if ALVO_DE(d, mor[f]) != obj[ALVO_DE(c, f)]:
            return F
    for g in MORFISMOS_DE(c):
        for f in MORFISMOS_DE(c):
            if COMPONIVEIS(c, g, f):
                if mor[COMPOR(c, g, f)] != COMPOR(d, mor[g], mor[f]):
                    return F
    return V


def FUNCTOR_IDENTIDADE_FINITO(categoria):
    return FUNCTOR_FINITO(
        categoria,
        categoria,
        {obj: obj for obj in OBJETOS_DE(categoria)},
        {f: f for f in MORFISMOS_DE(categoria)},
    )


def COMPOR_FUNCTORES_FINITO(g, f):
    c = f["origem"]
    e = g["alvo"]
    objetos = {obj: g["objetos"][f["objetos"][obj]] for obj in OBJETOS_DE(c)}
    morfismos = {m: g["morfismos"][f["morfismos"][m]] for m in MORFISMOS_DE(c)}
    return FUNCTOR_FINITO(c, e, objetos, morfismos)


def TRANSFORMACAO_NATURAL_FINITA(functor_f, functor_g, componentes):
    return {"F": functor_f, "G": functor_g, "componentes": dict(componentes)}


def EH_TRANSFORMACAO_NATURAL_FINITA(transformacao):
    ftor = transformacao["F"]
    gtor = transformacao["G"]
    c = ftor["origem"]
    d = ftor["alvo"]
    if gtor["origem"] is not c or gtor["alvo"] is not d:
        return F
    componentes = transformacao["componentes"]
    if set(componentes.keys()) != set(OBJETOS_DE(c)):
        return F
    for a in OBJETOS_DE(c):
        eta = componentes[a]
        if eta not in MORFISMOS_DE(d):
            return F
        if ORIGEM_DE(d, eta) != ftor["objetos"][a]:
            return F
        if ALVO_DE(d, eta) != gtor["objetos"][a]:
            return F
    for m in MORFISMOS_DE(c):
        a = ORIGEM_DE(c, m)
        b = ALVO_DE(c, m)
        esquerda = COMPOR(d, gtor["morfismos"][m], componentes[a])
        direita = COMPOR(d, componentes[b], ftor["morfismos"][m])
        if esquerda != direita:
            return F
    return V


def OBJETOS_TERMINAIS_FINITO(categoria):
    return tuple(
        t for t in OBJETOS_DE(categoria)
        if all(len(HOM_FINITO(categoria, a, t)) == 1 for a in OBJETOS_DE(categoria))
    )


def OBJETOS_INICIAIS_FINITO(categoria):
    return tuple(
        i for i in OBJETOS_DE(categoria)
        if all(len(HOM_FINITO(categoria, i, a)) == 1 for a in OBJETOS_DE(categoria))
    )


def CATEGORIA_DISCRETA_FINITA(objetos):
    morfismos = tuple(("id", obj) for obj in objetos)
    origem = {("id", obj): obj for obj in objetos}
    alvo = {("id", obj): obj for obj in objetos}
    identidade = {obj: ("id", obj) for obj in objetos}
    composicao = {(("id", obj), ("id", obj)): ("id", obj) for obj in objetos}
    return CATEGORIA_FINITA(objetos, morfismos, origem, alvo, identidade, composicao)


def CATEGORIA_PREORDEM_FINITA(objetos, leq):
    morfismos = tuple((a, b) for a in objetos for b in objetos if leq(a, b))
    origem = {m: m[0] for m in morfismos}
    alvo = {m: m[1] for m in morfismos}
    identidade = {obj: (obj, obj) for obj in objetos}
    composicao = {}
    for g in morfismos:
        for f in morfismos:
            if f[1] == g[0]:
                composicao[(g, f)] = (f[0], g[1])
    return CATEGORIA_FINITA(objetos, morfismos, origem, alvo, identidade, composicao)


def CATEGORIA_MONOIDE_UM_OBJETO(elementos, operacao, unidade):
    objeto = "*"
    morfismos = tuple(elementos)
    origem = {m: objeto for m in morfismos}
    alvo = {m: objeto for m in morfismos}
    identidade = {objeto: unidade}
    composicao = {(g, f): operacao(g, f) for g in morfismos for f in morfismos}
    return CATEGORIA_FINITA((objeto,), morfismos, origem, alvo, identidade, composicao)


def CONE_FINITO(diagrama, apex, pernas):
    return {"diagrama": diagrama, "apex": apex, "pernas": dict(pernas)}


def EH_CONE_FINITO(cone):
    diagrama = cone["diagrama"]
    j = diagrama["origem"]
    c = diagrama["alvo"]
    pernas = cone["pernas"]
    apex = cone["apex"]
    if set(pernas.keys()) != set(OBJETOS_DE(j)):
        return F
    for obj in OBJETOS_DE(j):
        perna = pernas[obj]
        if ORIGEM_DE(c, perna) != apex or ALVO_DE(c, perna) != diagrama["objetos"][obj]:
            return F
    for m in MORFISMOS_DE(j):
        a = ORIGEM_DE(j, m)
        b = ALVO_DE(j, m)
        if COMPOR(c, diagrama["morfismos"][m], pernas[a]) != pernas[b]:
            return F
    return V


def COCONE_FINITO(diagrama, apex, pernas):
    return {"diagrama": diagrama, "apex": apex, "pernas": dict(pernas)}


def EH_COCONE_FINITO(cocone):
    diagrama = cocone["diagrama"]
    j = diagrama["origem"]
    c = diagrama["alvo"]
    pernas = cocone["pernas"]
    apex = cocone["apex"]
    if set(pernas.keys()) != set(OBJETOS_DE(j)):
        return F
    for obj in OBJETOS_DE(j):
        perna = pernas[obj]
        if ORIGEM_DE(c, perna) != diagrama["objetos"][obj] or ALVO_DE(c, perna) != apex:
            return F
    for m in MORFISMOS_DE(j):
        a = ORIGEM_DE(j, m)
        b = ALVO_DE(j, m)
        if COMPOR(c, pernas[b], diagrama["morfismos"][m]) != pernas[a]:
            return F
    return V


def PRODUTOS_BINARIOS_FINITO(categoria, a, b):
    candidatos = []
    for p in OBJETOS_DE(categoria):
        for pi_a in HOM_FINITO(categoria, p, a):
            for pi_b in HOM_FINITO(categoria, p, b):
                universal = True
                for x in OBJETOS_DE(categoria):
                    for f in HOM_FINITO(categoria, x, a):
                        for g in HOM_FINITO(categoria, x, b):
                            mediadores = tuple(
                                u for u in HOM_FINITO(categoria, x, p)
                                if COMPOR(categoria, pi_a, u) == f and COMPOR(categoria, pi_b, u) == g
                            )
                            if len(mediadores) != 1:
                                universal = False
                if universal:
                    candidatos.append((p, pi_a, pi_b))
    return tuple(candidatos)


def COPRODUTOS_BINARIOS_FINITO(categoria, a, b):
    candidatos = []
    for p in OBJETOS_DE(categoria):
        for in_a in HOM_FINITO(categoria, a, p):
            for in_b in HOM_FINITO(categoria, b, p):
                universal = True
                for x in OBJETOS_DE(categoria):
                    for f in HOM_FINITO(categoria, a, x):
                        for g in HOM_FINITO(categoria, b, x):
                            mediadores = tuple(
                                u for u in HOM_FINITO(categoria, p, x)
                                if COMPOR(categoria, u, in_a) == f and COMPOR(categoria, u, in_b) == g
                            )
                            if len(mediadores) != 1:
                                universal = False
                if universal:
                    candidatos.append((p, in_a, in_b))
    return tuple(candidatos)


def ISOMORFISMO_CATEGORIAS_FINITO(functor_f, functor_g):
    if not _py_bool(EH_FUNCTOR_FINITO(functor_f)) or not _py_bool(EH_FUNCTOR_FINITO(functor_g)):
        return F
    c = functor_f["origem"]
    d = functor_f["alvo"]
    if functor_g["origem"] is not d or functor_g["alvo"] is not c:
        return F
    gf = COMPOR_FUNCTORES_FINITO(functor_g, functor_f)
    fg = COMPOR_FUNCTORES_FINITO(functor_f, functor_g)
    if any(gf["objetos"][obj] != obj for obj in OBJETOS_DE(c)):
        return F
    if any(gf["morfismos"][m] != m for m in MORFISMOS_DE(c)):
        return F
    if any(fg["objetos"][obj] != obj for obj in OBJETOS_DE(d)):
        return F
    if any(fg["morfismos"][m] != m for m in MORFISMOS_DE(d)):
        return F
    return V


EQUIVALENCIA_FINITA_INICIAL = ISOMORFISMO_CATEGORIAS_FINITO


def CATEGORIA_FUNCTORES_FINITA_INICIAL(categoria_origem, categoria_alvo, functores, transformacoes):
    return {
        "origem": categoria_origem,
        "alvo": categoria_alvo,
        "functores": tuple(functores),
        "transformacoes": tuple(transformacoes),
    }


def AUDITORIA_CATEGORICA_FINITA(categoria):
    return EH_CATEGORIA_FINITA(categoria)


def FECHAMENTO_CATEGORIAS_FINITAS_ATE_340():
    return V
