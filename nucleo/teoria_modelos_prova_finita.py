# ==============================================================================
# TEORIA DE MODELOS FINITA REVISITADA + PROVA DE PRIMEIRA ORDEM COMO OBJETO
# FINITO — Etapas 361 a 380 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   depois da lógica de predicados finita (341-360, com estrutura, termo e
#   satisfação ⊨ já construídos), o próximo passo que nasce sem violar a lei
#   das fórmulas é comparar estruturas entre si (subestrutura, homomorfismo,
#   isomorfismo, equivalência elementar sobre uma família FINITA de
#   sentenças) e formalizar prova como objeto finito verificável: sequente,
#   regra de inferência como transição finita, derivação como sequência de
#   sequentes.
#
#   Nenhuma regra "gera" uma prova por mágica — cada `_..._valida` só
#   VERIFICA se um passo já proposto é uma instância legítima da regra
#   correspondente. Isto é deliberado: o projeto constrói verificadores,
#   não um provador automático (mesmo espírito de VERIFICAR_INDUCAO em
#   calculo_discreto.py).
# ==============================================================================
from .primitivas import V, F
from .logica_predicados_finita import (
    ATOMICA,
    DOMINIO_DE,
    EH_SENTENCA_FINITA,
    ESTRUTURA_FINITA,
    SATISFAZ_FINITA,
    SUBSTITUIR_LIVRE_FINITA,
    VARIAVEIS_LIVRES_FINITA,
)


def _bool(condicao):
    return V if condicao else F


def _bool_to_py(valor):
    return valor(True)(False)


def _contem(seq, elemento):
    return any(x == elemento for x in seq)


def _unicos(seq):
    saida = []
    for x in seq:
        if not _contem(saida, x):
            saida.append(x)
    return tuple(saida)


def _igual_conjunto(a, b):
    return all(_contem(b, x) for x in a) and all(_contem(a, x) for x in b)


# ==========================================================================
# Etapas 361-370 — Teoria de modelos finita revisitada.
# ==========================================================================

# --------------------------------------------------------------------
# Etapa 361 — Subestrutura finita.
# --------------------------------------------------------------------
def SUBESTRUTURA_FINITA(estrutura, subdominio):
    subdominio = tuple(subdominio)
    predicados = {
        nome: tuple(t for t in extensao if all(_contem(subdominio, x) for x in t))
        for nome, extensao in estrutura["predicados"].items()
    }
    funcoes = {
        nome: {entrada: saida for entrada, saida in tabela.items() if all(_contem(subdominio, x) for x in entrada)}
        for nome, tabela in estrutura["funcoes"].items()
    }
    return ESTRUTURA_FINITA(subdominio, predicados, funcoes)


def EH_SUBESTRUTURA_FECHADA(estrutura_maior, subdominio):
    for tabela in estrutura_maior["funcoes"].values():
        for entrada, saida in tabela.items():
            if all(_contem(subdominio, x) for x in entrada) and not _contem(subdominio, saida):
                return F
    return V


def EH_SUBESTRUTURA_FINITA(maior, menor):
    dominio_menor = DOMINIO_DE(menor)
    if not all(_contem(DOMINIO_DE(maior), x) for x in dominio_menor):
        return F
    if not _bool_to_py(EH_SUBESTRUTURA_FECHADA(maior, dominio_menor)):
        return F
    esperado = SUBESTRUTURA_FINITA(maior, dominio_menor)
    return _bool(esperado["predicados"] == menor["predicados"] and esperado["funcoes"] == menor["funcoes"])


# --------------------------------------------------------------------
# Etapa 362 — Subestrutura gerada por um conjunto (fecho sob funções).
# --------------------------------------------------------------------
def SUBESTRUTURA_GERADA_FINITA(estrutura, geradores):
    atual = _unicos(tuple(geradores))
    mudou = True
    while mudou:
        mudou = False
        for tabela in estrutura["funcoes"].values():
            for entrada, saida in tabela.items():
                if all(_contem(atual, x) for x in entrada) and not _contem(atual, saida):
                    atual = atual + (saida,)
                    mudou = True
    return SUBESTRUTURA_FINITA(estrutura, atual)


# --------------------------------------------------------------------
# Etapa 363 — Homomorfismo de estruturas.
# --------------------------------------------------------------------
def EH_HOMOMORFISMO_ESTRUTURAS(origem, alvo, mapa):
    for x in DOMINIO_DE(origem):
        if x not in mapa or not _contem(DOMINIO_DE(alvo), mapa[x]):
            return F
    for nome, tabela in origem["funcoes"].items():
        tabela_alvo = alvo["funcoes"][nome]
        for entrada, saida in tabela.items():
            entrada_imagem = tuple(mapa[e] for e in entrada)
            if tabela_alvo.get(entrada_imagem) != mapa[saida]:
                return F
    for nome, extensao in origem["predicados"].items():
        extensao_alvo = alvo["predicados"][nome]
        for tupla in extensao:
            imagem = tuple(mapa[x] for x in tupla)
            if not _contem(extensao_alvo, imagem):
                return F
    return V


# --------------------------------------------------------------------
# Etapa 364 — Isomorfismo de estruturas (homomorfismo bijetivo que
# reflete predicados, não só preserva).
# --------------------------------------------------------------------
def EH_ISOMORFISMO_ESTRUTURAS(origem, alvo, mapa):
    if not _bool_to_py(EH_HOMOMORFISMO_ESTRUTURAS(origem, alvo, mapa)):
        return F
    dominio_origem = DOMINIO_DE(origem)
    dominio_alvo = DOMINIO_DE(alvo)
    imagem = tuple(mapa[x] for x in dominio_origem)
    if len(_unicos(imagem)) != len(dominio_origem) or len(dominio_origem) != len(dominio_alvo):
        return F
    if not _igual_conjunto(imagem, dominio_alvo):
        return F
    for nome, extensao in origem["predicados"].items():
        extensao_alvo = alvo["predicados"][nome]
        imagem_extensao = tuple(tuple(mapa[x] for x in tupla) for tupla in extensao)
        if not _igual_conjunto(imagem_extensao, extensao_alvo):
            return F
    return V


# --------------------------------------------------------------------
# Etapa 365 — Mergulho (embedding): isomorfismo da origem sobre a
# subestrutura de alvo restrita à imagem.
# --------------------------------------------------------------------
def EH_MERGULHO_ESTRUTURAS(origem, alvo, mapa):
    dominio_origem = DOMINIO_DE(origem)
    if not all(x in mapa for x in dominio_origem):
        return F
    imagem = _unicos(tuple(mapa[x] for x in dominio_origem))
    if len(imagem) != len(dominio_origem) or not all(_contem(DOMINIO_DE(alvo), x) for x in imagem):
        return F
    sub = SUBESTRUTURA_FINITA(alvo, imagem)
    return EH_ISOMORFISMO_ESTRUTURAS(origem, sub, mapa)


# --------------------------------------------------------------------
# Etapa 366 — Redução de assinatura (reduct): esquece símbolos.
# --------------------------------------------------------------------
def REDUCT_FINITO(estrutura, simbolos_predicados, simbolos_funcoes):
    predicados = {nome: estrutura["predicados"][nome] for nome in simbolos_predicados}
    funcoes = {nome: estrutura["funcoes"][nome] for nome in simbolos_funcoes}
    return ESTRUTURA_FINITA(DOMINIO_DE(estrutura), predicados, funcoes)


# --------------------------------------------------------------------
# Etapa 367 — Expansão de assinatura: acrescenta interpretação nova.
# --------------------------------------------------------------------
def EXPANSAO_FINITA(estrutura, predicados_novos=None, funcoes_novos=None):
    predicados = dict(estrutura["predicados"])
    predicados.update(predicados_novos or {})
    funcoes = dict(estrutura["funcoes"])
    funcoes.update(funcoes_novos or {})
    return ESTRUTURA_FINITA(DOMINIO_DE(estrutura), predicados, funcoes)


# --------------------------------------------------------------------
# Etapa 368 — Equivalência elementar sobre uma teoria finita dada.
#
# Limite honesto: equivalência elementar CLÁSSICA compara satisfação de
# TODA sentença da linguagem (coleção infinita). Esta função só compara
# sobre a família FINITA e explícita `sentencas` fornecida pelo chamador —
# mesma fronteira de `predicados.PARA_TODO/EXISTE` (limitado) e
# `logica_predicados_finita.VALIDA_SOBRE_ESTRUTURAS_FINITA` (amostra
# finita de estruturas, não todas).
# --------------------------------------------------------------------
def EQUIVALENCIA_ELEMENTAR_FINITA(a, b, sentencas):
    for s in sentencas:
        if not _bool_to_py(EH_SENTENCA_FINITA(s)):
            raise ValueError("equivalência elementar finita só considera sentenças")
        if _bool_to_py(SATISFAZ_FINITA(a, s)) != _bool_to_py(SATISFAZ_FINITA(b, s)):
            return F
    return V


# --------------------------------------------------------------------
# Etapa 369 — Isomorfismo elementar finito: isomorfismo + equivalência
# elementar sobre a família de sentenças dada.
# --------------------------------------------------------------------
def ISOMORFISMO_ELEMENTAR_FINITO(a, b, mapa, sentencas):
    return _bool(
        _bool_to_py(EH_ISOMORFISMO_ESTRUTURAS(a, b, mapa))
        and _bool_to_py(EQUIVALENCIA_ELEMENTAR_FINITA(a, b, sentencas))
    )


# --------------------------------------------------------------------
# Etapa 370 — Fechamento da teoria de modelos finita revisitada.
# --------------------------------------------------------------------
def FECHAMENTO_TEORIA_MODELOS_FINITA_ATE_370():
    return V


# ==========================================================================
# Etapas 371-380 — Prova de primeira ordem como objeto finito.
# ==========================================================================

# --------------------------------------------------------------------
# Etapa 371 — Assinatura finita (aridades declaradas explicitamente).
# --------------------------------------------------------------------
def ASSINATURA_FINITA(aridade_predicados, aridade_funcoes):
    return {"predicados": dict(aridade_predicados), "funcoes": dict(aridade_funcoes)}


# --------------------------------------------------------------------
# Etapa 372 — Sequente finito: par (premissas finitas, conclusão).
# --------------------------------------------------------------------
SEQUENTE_FINITO = lambda premissas, conclusao: ("sequente", tuple(premissas), conclusao)
PREMISSAS_DE = lambda sequente: sequente[1]
CONCLUSAO_DE = lambda sequente: sequente[2]


# --------------------------------------------------------------------
# Etapa 373 — Regra de inferência como transição finita: dado o nome da
# regra, os sequentes de entrada, o sequente candidato de saída (e um
# argumento extra para regras de quantificador, que citam um termo), esta
# função DECIDE se o passo é uma instância válida — não gera provas.
# --------------------------------------------------------------------
def PASSO_VALIDO(nome_regra, sequentes_entrada, sequente_saida, argumento=None):
    if nome_regra == "premissa":
        return _bool(_premissa_valida(sequente_saida))
    if nome_regra == "e_intro":
        return _bool(_e_introducao_valida(sequentes_entrada, sequente_saida))
    if nome_regra == "e_elim_esq":
        return _bool(_e_eliminacao_valida(sequentes_entrada, sequente_saida, esquerda=True))
    if nome_regra == "e_elim_dir":
        return _bool(_e_eliminacao_valida(sequentes_entrada, sequente_saida, esquerda=False))
    if nome_regra == "ou_intro":
        return _bool(_ou_introducao_valida(sequentes_entrada, sequente_saida))
    if nome_regra == "ou_elim":
        return _bool(_ou_eliminacao_valida(sequentes_entrada, sequente_saida))
    if nome_regra == "modus_ponens":
        return _bool(_modus_ponens_valida(sequentes_entrada, sequente_saida))
    if nome_regra == "implica_intro":
        return _bool(_implica_introducao_valida(sequentes_entrada, sequente_saida))
    if nome_regra == "para_todo_intro":
        return _bool(_para_todo_introducao_valida(sequentes_entrada, sequente_saida))
    if nome_regra == "para_todo_elim":
        return _bool(_para_todo_eliminacao_valida(sequentes_entrada, sequente_saida, argumento))
    if nome_regra == "existe_intro":
        return _bool(_existe_introducao_valida(sequentes_entrada, sequente_saida, argumento))
    if nome_regra == "existe_elim":
        return _bool(_existe_eliminacao_valida(sequentes_entrada, sequente_saida))
    raise ValueError(f"regra de inferência desconhecida: {nome_regra}")


def _premissa_valida(saida):
    return CONCLUSAO_DE(saida) in PREMISSAS_DE(saida)


# --------------------------------------------------------------------
# Etapa 374 — ∧-introdução / ∧-eliminação.
# --------------------------------------------------------------------
def _e_introducao_valida(entradas, saida):
    if len(entradas) != 2:
        return False
    s1, s2 = entradas
    mesmas_premissas = (
        _igual_conjunto(PREMISSAS_DE(s1), PREMISSAS_DE(s2))
        and _igual_conjunto(PREMISSAS_DE(s1), PREMISSAS_DE(saida))
    )
    conclusao_esperada = ("e", CONCLUSAO_DE(s1), CONCLUSAO_DE(s2))
    return mesmas_premissas and CONCLUSAO_DE(saida) == conclusao_esperada


def _e_eliminacao_valida(entradas, saida, esquerda):
    if len(entradas) != 1:
        return False
    (s1,) = entradas
    conclusao = CONCLUSAO_DE(s1)
    if conclusao[0] != "e":
        return False
    lado = conclusao[1] if esquerda else conclusao[2]
    return CONCLUSAO_DE(saida) == lado and _igual_conjunto(PREMISSAS_DE(s1), PREMISSAS_DE(saida))


# --------------------------------------------------------------------
# Etapa 375 — ∨-introdução / ∨-eliminação (por casos).
# --------------------------------------------------------------------
def _ou_introducao_valida(entradas, saida):
    if len(entradas) != 1:
        return False
    (s1,) = entradas
    conclusao_saida = CONCLUSAO_DE(saida)
    if conclusao_saida[0] != "ou":
        return False
    if not _igual_conjunto(PREMISSAS_DE(s1), PREMISSAS_DE(saida)):
        return False
    return conclusao_saida[1] == CONCLUSAO_DE(s1) or conclusao_saida[2] == CONCLUSAO_DE(s1)


def _ou_eliminacao_valida(entradas, saida):
    if len(entradas) != 3:
        return False
    s_ou, s1, s2 = entradas
    disjuncao = CONCLUSAO_DE(s_ou)
    if disjuncao[0] != "ou":
        return False
    phi, psi = disjuncao[1], disjuncao[2]
    gamma = PREMISSAS_DE(s_ou)
    chi = CONCLUSAO_DE(saida)
    ok1 = _igual_conjunto(PREMISSAS_DE(s1), gamma + (phi,)) and CONCLUSAO_DE(s1) == chi
    ok2 = _igual_conjunto(PREMISSAS_DE(s2), gamma + (psi,)) and CONCLUSAO_DE(s2) == chi
    ok3 = _igual_conjunto(PREMISSAS_DE(saida), gamma)
    return ok1 and ok2 and ok3


# --------------------------------------------------------------------
# Etapa 376 — →-introdução / modus ponens (→-eliminação).
# --------------------------------------------------------------------
def _modus_ponens_valida(entradas, saida):
    if len(entradas) != 2:
        return False
    s1, s2 = entradas
    conclusao_s2 = CONCLUSAO_DE(s2)
    if conclusao_s2[0] != "implica":
        return False
    phi, psi = conclusao_s2[1], conclusao_s2[2]
    if CONCLUSAO_DE(s1) != phi:
        return False
    premissas_esperadas = _unicos(PREMISSAS_DE(s1) + PREMISSAS_DE(s2))
    return _igual_conjunto(PREMISSAS_DE(saida), premissas_esperadas) and CONCLUSAO_DE(saida) == psi


def _implica_introducao_valida(entradas, saida):
    if len(entradas) != 1:
        return False
    (s1,) = entradas
    conclusao_saida = CONCLUSAO_DE(saida)
    if conclusao_saida[0] != "implica":
        return False
    phi, psi = conclusao_saida[1], conclusao_saida[2]
    return CONCLUSAO_DE(s1) == psi and _igual_conjunto(PREMISSAS_DE(s1), PREMISSAS_DE(saida) + (phi,))


# --------------------------------------------------------------------
# Etapa 377 — ∀-introdução (generalização, com a condição lateral
# clássica: a variável não pode ocorrer livre em nenhuma premissa) e
# ∀-eliminação (instanciação por substituição).
# --------------------------------------------------------------------
def _para_todo_introducao_valida(entradas, saida):
    if len(entradas) != 1:
        return False
    (s1,) = entradas
    conclusao_saida = CONCLUSAO_DE(saida)
    if conclusao_saida[0] != "para_todo":
        return False
    variavel, corpo = conclusao_saida[1], conclusao_saida[2]
    if CONCLUSAO_DE(s1) != corpo or not _igual_conjunto(PREMISSAS_DE(s1), PREMISSAS_DE(saida)):
        return False
    for premissa in PREMISSAS_DE(s1):
        if _contem(VARIAVEIS_LIVRES_FINITA(premissa), variavel):
            return False
    return True


def _para_todo_eliminacao_valida(entradas, saida, termo):
    if len(entradas) != 1 or termo is None:
        return False
    (s1,) = entradas
    conclusao_s1 = CONCLUSAO_DE(s1)
    if conclusao_s1[0] != "para_todo":
        return False
    variavel, corpo = conclusao_s1[1], conclusao_s1[2]
    esperado = SUBSTITUIR_LIVRE_FINITA(corpo, variavel, termo)
    return CONCLUSAO_DE(saida) == esperado and _igual_conjunto(PREMISSAS_DE(s1), PREMISSAS_DE(saida))


# --------------------------------------------------------------------
# Etapa 378 — ∃-introdução (por testemunha) e ∃-eliminação (com a
# condição lateral: a variável não pode ocorrer livre nas premissas
# nem na conclusão da eliminação).
# --------------------------------------------------------------------
def _existe_introducao_valida(entradas, saida, termo):
    if len(entradas) != 1 or termo is None:
        return False
    (s1,) = entradas
    conclusao_saida = CONCLUSAO_DE(saida)
    if conclusao_saida[0] != "existe":
        return False
    variavel, corpo = conclusao_saida[1], conclusao_saida[2]
    esperado = SUBSTITUIR_LIVRE_FINITA(corpo, variavel, termo)
    return CONCLUSAO_DE(s1) == esperado and _igual_conjunto(PREMISSAS_DE(s1), PREMISSAS_DE(saida))


def _existe_eliminacao_valida(entradas, saida):
    if len(entradas) != 2:
        return False
    s_existe, s_corpo = entradas
    conclusao_existe = CONCLUSAO_DE(s_existe)
    if conclusao_existe[0] != "existe":
        return False
    variavel, corpo = conclusao_existe[1], conclusao_existe[2]
    gamma = PREMISSAS_DE(s_existe)
    chi = CONCLUSAO_DE(saida)
    ok_premissas_corpo = _igual_conjunto(PREMISSAS_DE(s_corpo), gamma + (corpo,))
    ok_conclusao = CONCLUSAO_DE(s_corpo) == chi
    ok_saida = _igual_conjunto(PREMISSAS_DE(saida), gamma)
    livre_em_gamma = any(_contem(VARIAVEIS_LIVRES_FINITA(p), variavel) for p in gamma)
    livre_em_chi = _contem(VARIAVEIS_LIVRES_FINITA(chi), variavel)
    return ok_premissas_corpo and ok_conclusao and ok_saida and not livre_em_gamma and not livre_em_chi


# --------------------------------------------------------------------
# Etapa 379 — Derivação como sequência finita de sequentes, cada passo
# justificado por uma regra e por sequentes anteriores da mesma
# derivação. O objeto `passos` (a derivação) É a prova finita — dado,
# não afirmação.
# --------------------------------------------------------------------
PASSO_DERIVACAO = lambda nome_regra, indices_entrada, sequente_saida, argumento=None: (
    nome_regra, tuple(indices_entrada), sequente_saida, argumento
)


def DERIVACAO_VALIDA(passos):
    sequentes = []
    for nome_regra, indices_entrada, sequente_saida, argumento in passos:
        entradas = tuple(sequentes[i] for i in indices_entrada)
        if not _bool_to_py(PASSO_VALIDO(nome_regra, entradas, sequente_saida, argumento)):
            return F
        sequentes.append(sequente_saida)
    return V


def CONCLUSAO_FINAL_DA_DERIVACAO(passos):
    return CONCLUSAO_DE(passos[-1][2])


# --------------------------------------------------------------------
# Etapa 380 — Fechamento: prova de primeira ordem como objeto finito.
# --------------------------------------------------------------------
def FECHAMENTO_PROVA_FINITA_ATE_380():
    return V
