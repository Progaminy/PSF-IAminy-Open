# ==============================================================================
# LÓGICA DE PREDICADOS FINITA — Etapas 341 a 360 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   depois da lógica proposicional finita (261-300, nucleo/metodos_finitos.py)
#   e das categorias finitas (301-340, nucleo/categorias_finitas.py), o
#   próximo conceito que nasce sem violar a lei das fórmulas é a lógica de
#   predicados (primeira ordem) sobre um domínio finito explícito: termos,
#   quantificadores como SINTAXE (não atalho semântico), estruturas finitas
#   dadas por extensão, e a relação de satisfação (⊨) definida por recursão
#   estrutural na fórmula + varredura finita do domínio.
#
#   Os conectivos (¬, ∧, ∨, →) NÃO são reinventados aqui — são os mesmos
#   construtores de nucleo/metodos_finitos.py (PROP_NAO, PROP_E, PROP_OU,
#   PROP_IMPLICA), reaproveitados sobre fórmulas atômicas de predicados em
#   vez de variáveis proposicionais. É reaproveitamento legítimo de um
#   conceito já nascido — o mesmo espírito da nota em
#   ETAPA_10_PRIMALIDADE_PURA.md sobre RESTO_PURO ("isso não é salto
#   conceitual; é reaproveitamento legítimo").
#
# Dependências permitidas:
#   metodos_finitos.PROP_NAO/PROP_E/PROP_OU/PROP_IMPLICA (etapa 261-265),
#   predicados.py como precedente operacional do quantificador limitado,
#   tuplas/dicionários finitos já usados desde a etapa 136.
#
# Dependências proibidas:
#   nenhuma lógica externa, nenhum solver/SAT/SMT importado, nenhuma
#   quantificação sobre domínio infinito, DIV/MOD/MDC/MMC nativos ou os
#   módulos antigos primos/divisores.
# ==============================================================================
from .primitivas import V, F
from .metodos_finitos import PROP_NAO, PROP_E, PROP_OU, PROP_IMPLICA


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


# ------------------------------------------------------------------------
# Etapa 341 — Domínio finito de interpretação.
# ------------------------------------------------------------------------
DOMINIO_FINITO = lambda *elementos: tuple(elementos)


# ------------------------------------------------------------------------
# Etapa 342 — Estrutura finita: domínio + interpretação de predicados/funções.
# ------------------------------------------------------------------------
def ESTRUTURA_FINITA(dominio, predicados, funcoes):
    return {
        "dominio": tuple(dominio),
        "predicados": {nome: tuple(extensao) for nome, extensao in predicados.items()},
        "funcoes": {nome: dict(tabela) for nome, tabela in funcoes.items()},
    }


DOMINIO_DE = lambda estrutura: estrutura["dominio"]


def EH_ESTRUTURA_FINITA_VALIDA(estrutura, aridade_predicados=None, aridade_funcoes=None):
    dominio = DOMINIO_DE(estrutura)
    aridade_predicados = aridade_predicados or {}
    aridade_funcoes = aridade_funcoes or {}
    for simbolo, aridade in aridade_predicados.items():
        if not _bool_to_py(EH_EXTENSAO_VALIDA_PREDICADO(estrutura, simbolo, aridade)):
            return F
    for simbolo, aridade in aridade_funcoes.items():
        tabela = INTERPRETACAO_FUNCAO(estrutura, simbolo)
        for entrada, saida in tabela.items():
            if len(entrada) != aridade:
                return F
            if not _contem(dominio, saida) or not all(_contem(dominio, x) for x in entrada):
                return F
    return V


# ------------------------------------------------------------------------
# Etapa 343 — Símbolo de predicado n-ário e sua interpretação (extensão finita).
# ------------------------------------------------------------------------
def INTERPRETACAO_PREDICADO(estrutura, simbolo):
    return estrutura["predicados"][simbolo]


def EH_EXTENSAO_VALIDA_PREDICADO(estrutura, simbolo, aridade):
    extensao = INTERPRETACAO_PREDICADO(estrutura, simbolo)
    dominio = DOMINIO_DE(estrutura)
    return _bool(all(
        len(tupla) == aridade and all(_contem(dominio, x) for x in tupla)
        for tupla in extensao
    ))


def IGUALDADE_DIAGONAL_FINITA(dominio):
    """Extensão padrão do predicado '=' sobre um domínio: {(d,d) : d em dominio}.

    Construída por enumeração do próprio domínio (etapa 172, produto
    cartesiano finito) — não é um predicado importado de fora do fluxo.
    """
    return tuple((d, d) for d in dominio)


# ------------------------------------------------------------------------
# Etapa 344 — Símbolo de função n-ária e sua interpretação (tabela finita).
# ------------------------------------------------------------------------
def INTERPRETACAO_FUNCAO(estrutura, simbolo):
    return estrutura["funcoes"][simbolo]


def APLICAR_FUNCAO_INTERPRETADA(estrutura, simbolo, argumentos):
    return INTERPRETACAO_FUNCAO(estrutura, simbolo)[tuple(argumentos)]


# ------------------------------------------------------------------------
# Etapa 345 — Termo de primeira ordem (variável, constante ou função aplicada).
# ------------------------------------------------------------------------
TERMO_VAR = lambda nome: ("tvar", nome)
TERMO_CONST = lambda valor: ("tconst", valor)
TERMO_FUNC = lambda simbolo, *args: ("tfunc", simbolo, tuple(args))


def VARIAVEIS_DO_TERMO(termo):
    tag = termo[0]
    if tag == "tvar":
        return (termo[1],)
    if tag == "tconst":
        return tuple()
    if tag == "tfunc":
        variaveis = tuple()
        for sub in termo[2]:
            variaveis = _unicos(variaveis + VARIAVEIS_DO_TERMO(sub))
        return variaveis
    raise ValueError(f"termo desconhecido: {tag}")


# ------------------------------------------------------------------------
# Etapa 346 — Avaliação de termo numa estrutura sob uma atribuição.
# ------------------------------------------------------------------------
def AVALIAR_TERMO(estrutura, termo, atribuicao):
    tag = termo[0]
    if tag == "tvar":
        return atribuicao[termo[1]]
    if tag == "tconst":
        return termo[1]
    if tag == "tfunc":
        simbolo, args = termo[1], termo[2]
        valores = tuple(AVALIAR_TERMO(estrutura, sub, atribuicao) for sub in args)
        return APLICAR_FUNCAO_INTERPRETADA(estrutura, simbolo, valores)
    raise ValueError(f"termo desconhecido: {tag}")


# ------------------------------------------------------------------------
# Etapa 347 — Fórmula atômica (predicado aplicado a termos).
# ------------------------------------------------------------------------
ATOMICA = lambda simbolo, *termos: ("atomica", simbolo, tuple(termos))


# ------------------------------------------------------------------------
# Etapa 348 — Conectivos sobre fórmulas de predicados (reaproveitados de
# nucleo/metodos_finitos.py — mesmos construtores, agora com folhas
# atômicas de predicados em vez de variáveis proposicionais).
# ------------------------------------------------------------------------
NAO = PROP_NAO
E_FORMULA = PROP_E
OU_FORMULA = PROP_OU
IMPLICA_FORMULA = PROP_IMPLICA


# ------------------------------------------------------------------------
# Etapas 349/350 — Variável livre / variável ligada.
# ------------------------------------------------------------------------
def VARIAVEIS_LIVRES_FINITA(formula):
    tag = formula[0]
    if tag == "atomica":
        variaveis = tuple()
        for termo in formula[2]:
            variaveis = _unicos(variaveis + VARIAVEIS_DO_TERMO(termo))
        return variaveis
    if tag == "nao":
        return VARIAVEIS_LIVRES_FINITA(formula[1])
    if tag in ("e", "ou", "implica"):
        return _unicos(VARIAVEIS_LIVRES_FINITA(formula[1]) + VARIAVEIS_LIVRES_FINITA(formula[2]))
    if tag in ("para_todo", "existe"):
        variavel, sub = formula[1], formula[2]
        return tuple(v for v in VARIAVEIS_LIVRES_FINITA(sub) if v != variavel)
    raise ValueError(f"fórmula de predicados desconhecida: {tag}")


def VARIAVEIS_LIGADAS_FINITA(formula):
    tag = formula[0]
    if tag == "atomica":
        return tuple()
    if tag == "nao":
        return VARIAVEIS_LIGADAS_FINITA(formula[1])
    if tag in ("e", "ou", "implica"):
        return _unicos(VARIAVEIS_LIGADAS_FINITA(formula[1]) + VARIAVEIS_LIGADAS_FINITA(formula[2]))
    if tag in ("para_todo", "existe"):
        variavel, sub = formula[1], formula[2]
        return _unicos((variavel,) + VARIAVEIS_LIGADAS_FINITA(sub))
    raise ValueError(f"fórmula de predicados desconhecida: {tag}")


EH_SENTENCA_FINITA = lambda formula: _bool(len(VARIAVEIS_LIVRES_FINITA(formula)) == 0)


# ------------------------------------------------------------------------
# Etapas 351/352 — Quantificador universal / existencial como sintaxe.
# Isto é dado como CONSTRUTOR DE FÓRMULA (dado finito), não como semântica
# ainda — a semântica (satisfação) só nasce nas etapas 357/358.
# ------------------------------------------------------------------------
PARA_TODO_QUANTIFICADO = lambda variavel, formula: ("para_todo", variavel, formula)
EXISTE_QUANTIFICADO = lambda variavel, formula: ("existe", variavel, formula)


# ------------------------------------------------------------------------
# Etapa 353 — Substituição de termo por variável.
# ------------------------------------------------------------------------
def SUBSTITUIR_TERMO(termo, variavel, novo_termo):
    tag = termo[0]
    if tag == "tvar":
        return novo_termo if termo[1] == variavel else termo
    if tag == "tconst":
        return termo
    if tag == "tfunc":
        simbolo, args = termo[1], termo[2]
        return TERMO_FUNC(simbolo, *[SUBSTITUIR_TERMO(sub, variavel, novo_termo) for sub in args])
    raise ValueError(f"termo desconhecido: {tag}")


_CONSTRUTOR_CONECTIVO = {"e": E_FORMULA, "ou": OU_FORMULA, "implica": IMPLICA_FORMULA}


def SUBSTITUIR_LIVRE_FINITA(formula, variavel, novo_termo):
    """Substitui ocorrências LIVRES de `variavel` por `novo_termo` em `formula`.

    Limite honesto: esta função não faz alpha-conversão (renomeação de
    variáveis ligadas). Se `novo_termo` usa uma variável que um
    quantificador interno da fórmula liga com o mesmo nome, o resultado
    não é a substituição lógica de livro-texto — é um caso não resolvido
    por esta etapa. Use com `VARIAVEIS_LIGADAS_FINITA` e
    `VARIAVEIS_DO_TERMO` para confirmar ausência de colisão antes de
    chamar, quando a fórmula tiver quantificadores.
    """
    tag = formula[0]
    if tag == "atomica":
        simbolo, termos = formula[1], formula[2]
        return ATOMICA(simbolo, *[SUBSTITUIR_TERMO(t, variavel, novo_termo) for t in termos])
    if tag == "nao":
        return NAO(SUBSTITUIR_LIVRE_FINITA(formula[1], variavel, novo_termo))
    if tag in ("e", "ou", "implica"):
        construtor = _CONSTRUTOR_CONECTIVO[tag]
        return construtor(
            SUBSTITUIR_LIVRE_FINITA(formula[1], variavel, novo_termo),
            SUBSTITUIR_LIVRE_FINITA(formula[2], variavel, novo_termo),
        )
    if tag in ("para_todo", "existe"):
        v_ligada, sub = formula[1], formula[2]
        construtor = PARA_TODO_QUANTIFICADO if tag == "para_todo" else EXISTE_QUANTIFICADO
        if v_ligada == variavel:
            return formula
        return construtor(v_ligada, SUBSTITUIR_LIVRE_FINITA(sub, variavel, novo_termo))
    raise ValueError(f"fórmula de predicados desconhecida: {tag}")


# ------------------------------------------------------------------------
# Etapa 354 — Atribuição de variáveis (valoração de primeira ordem sobre
# o domínio da estrutura).
# ------------------------------------------------------------------------
def ATRIBUICAO_FINITA(pares):
    return dict(pares)


def ATUALIZAR_ATRIBUICAO(atribuicao, variavel, valor):
    nova = dict(atribuicao)
    nova[variavel] = valor
    return nova


# ------------------------------------------------------------------------
# Etapa 355 — Satisfação de fórmula atômica numa estrutura (base da ⊨).
# ------------------------------------------------------------------------
def SATISFAZ_ATOMICA_FINITA(estrutura, formula_atomica, atribuicao):
    simbolo, termos = formula_atomica[1], formula_atomica[2]
    valores = tuple(AVALIAR_TERMO(estrutura, t, atribuicao) for t in termos)
    return _bool(_contem(INTERPRETACAO_PREDICADO(estrutura, simbolo), valores))


# ------------------------------------------------------------------------
# Etapas 356/357/358 — Satisfação por indução na fórmula: conectivos,
# quantificador universal (varredura finita) e existencial (varredura
# finita). Reunidos numa única recursão estrutural, como
# AVALIAR_PROP_FINITA já faz para a lógica proposicional.
# ------------------------------------------------------------------------
def _satisfaz(estrutura, formula, atribuicao):
    tag = formula[0]
    if tag == "atomica":
        return _bool_to_py(SATISFAZ_ATOMICA_FINITA(estrutura, formula, atribuicao))
    if tag == "nao":
        return not _satisfaz(estrutura, formula[1], atribuicao)
    if tag == "e":
        return _satisfaz(estrutura, formula[1], atribuicao) and _satisfaz(estrutura, formula[2], atribuicao)
    if tag == "ou":
        return _satisfaz(estrutura, formula[1], atribuicao) or _satisfaz(estrutura, formula[2], atribuicao)
    if tag == "implica":
        return (not _satisfaz(estrutura, formula[1], atribuicao)) or _satisfaz(estrutura, formula[2], atribuicao)
    if tag == "para_todo":
        variavel, sub = formula[1], formula[2]
        return all(
            _satisfaz(estrutura, sub, ATUALIZAR_ATRIBUICAO(atribuicao, variavel, d))
            for d in DOMINIO_DE(estrutura)
        )
    if tag == "existe":
        variavel, sub = formula[1], formula[2]
        return any(
            _satisfaz(estrutura, sub, ATUALIZAR_ATRIBUICAO(atribuicao, variavel, d))
            for d in DOMINIO_DE(estrutura)
        )
    raise ValueError(f"fórmula de predicados desconhecida: {tag}")


def SATISFAZ_FINITA(estrutura, formula, atribuicao=None):
    return _bool(_satisfaz(estrutura, formula, atribuicao or {}))


# ------------------------------------------------------------------------
# Etapa 359 — Modelo finito de uma teoria (conjunto finito de sentenças).
# ------------------------------------------------------------------------
def EH_MODELO_FINITO(estrutura, sentencas):
    for formula in sentencas:
        if not _bool_to_py(EH_SENTENCA_FINITA(formula)):
            raise ValueError("EH_MODELO_FINITO só aceita sentenças (sem variável livre)")
        if not _satisfaz(estrutura, formula, {}):
            return F
    return V


# ------------------------------------------------------------------------
# Etapa 360 — Validade sobre amostra finita de estruturas + fechamento do
# bloco de lógica de predicados finita.
# ------------------------------------------------------------------------
def VALIDA_SOBRE_ESTRUTURAS_FINITA(sentenca, estruturas):
    """Verifica se `sentenca` é satisfeita por TODAS as estruturas em
    `estruturas` (uma tupla/lista finita e explícita, dada pelo chamador).

    Limite honesto: isto NÃO é validade lógica geral. Validade geral
    (verdade em toda e qualquer estrutura possível, de qualquer domínio,
    para uma assinatura dada) quantifica sobre uma coleção infinita de
    estruturas e não é decidível por enumeração — é o mesmo tipo de
    fronteira que `PARA_TODO`/`EXISTE` em `predicados.py` já respeita ao
    ficar limitado a `[0, limite]`, e que `VERIFICAR_INDUCAO` em
    `calculo_discreto.py` já respeita ao ser verificador, não provador.
    Esta função só dá evidência computacional sobre a amostra fornecida.
    """
    if not _bool_to_py(EH_SENTENCA_FINITA(sentenca)):
        raise ValueError("VALIDA_SOBRE_ESTRUTURAS_FINITA só aceita sentenças")
    return _bool(all(_satisfaz(estrutura, sentenca, {}) for estrutura in estruturas))


def FECHAMENTO_LOGICA_PREDICADOS_ATE_360():
    return V
