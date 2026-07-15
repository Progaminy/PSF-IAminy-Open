# ==============================================================================
# VERIFICAÇÃO DIAGNÓSTICA, SOLIDEZ E BUSCA DE DERIVAÇÃO POR ENUMERAÇÃO FINITA
# — Etapas 381 a 400 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   depois de prova de primeira ordem como objeto finito verificável
#   (361-380), o próximo passo que nasce sem violar a lei das fórmulas é
#   perguntar duas coisas sobre o que já existe: (1) as regras registadas
#   são SÓLIDAS — preservam satisfação, não só sintaticamente bem-formadas?
#   (2) uma derivação pode ser ENCONTRADA, não só verificada, dentro de um
#   fragmento decidível e um conjunto finito e explícito de fórmulas?
#
#   A busca aqui NUNCA considera fórmulas fora do fecho por subfórmula de
#   gamma ∪ {chi} — não é procura sobre "todas as fórmulas possíveis"
#   (infinito), é enumeração de um conjunto finito dado. Cobre só o
#   fragmento positivo: premissa, modus ponens, ∧-introdução/eliminação,
#   ∨-introdução. `implica_intro`, `ou_elim` e as regras de quantificador
#   continuam apenas verificáveis (etapa 373-378), não pesquisadas — ver
#   `conhecimento/ETAPA_381_400_BUSCA_DERIVACAO_COMPLETUDE_FINITA.md`.
# ==============================================================================
from .primitivas import V, F
from .teoria_modelos_prova_finita import (
    CONCLUSAO_DE,
    CONCLUSAO_FINAL_DA_DERIVACAO,
    DERIVACAO_VALIDA,
    PASSO_DERIVACAO,
    PASSO_VALIDO,
    PREMISSAS_DE,
    SEQUENTE_FINITO,
)
from .logica_predicados_finita import SATISFAZ_FINITA
from .metodos_finitos import (
    AVALIAR_PROP_FINITA,
    CONSEQUENCIA_FINITA,
    VALORACOES_PROP_FINITA,
    VARIAVEIS_PROP_FINITA,
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


# ==========================================================================
# Etapa 381 — Verificador de derivação com diagnóstico passo-a-passo.
#
# `DERIVACAO_VALIDA` (etapa 379) só devolve V/F agregado. Quando falha,
# não diz QUAL passo quebrou. Este verificador devolve, para cada passo, se
# ele é uma instância legítima da regra citada — reaproveitando
# `PASSO_VALIDO`, não reimplementando a checagem de regra.
# --------------------------------------------------------------------
def DIAGNOSTICO_DERIVACAO_FINITA(passos):
    sequentes = []
    diagnostico = []
    for indice, (nome_regra, indices_entrada, sequente_saida, argumento) in enumerate(passos):
        entradas_ok = all(i < len(sequentes) for i in indices_entrada)
        if not entradas_ok:
            diagnostico.append((indice, nome_regra, False))
            sequentes.append(sequente_saida)
            continue
        entradas = tuple(sequentes[i] for i in indices_entrada)
        valido = _bool_to_py(PASSO_VALIDO(nome_regra, entradas, sequente_saida, argumento))
        diagnostico.append((indice, nome_regra, valido))
        sequentes.append(sequente_saida)
    return tuple(diagnostico)


def PRIMEIRO_PASSO_INVALIDO_FINITO(passos):
    for indice, nome_regra, valido in DIAGNOSTICO_DERIVACAO_FINITA(passos):
        if not valido:
            return (indice, nome_regra)
    return None


# ==========================================================================
# Etapas 382-384 — Solidez (soundness) das regras registadas.
# ==========================================================================

# --------------------------------------------------------------------
# Etapa 382 — Solidez de uma regra proposicional: sobre TODA valoração
# (exaustivo — as variáveis proposicionais envolvidas são sempre um
# conjunto finito) das variáveis do sequente de saída, se as premissas do
# sequente de saída são satisfeitas, então a conclusão também é.
# --------------------------------------------------------------------
def SOLIDEZ_REGRA_PROPOSICIONAL_FINITA(nome_regra, entradas, saida, argumento=None):
    if not _bool_to_py(PASSO_VALIDO(nome_regra, entradas, saida, argumento)):
        return F
    variaveis = _unicos(
        tuple(v for premissa in PREMISSAS_DE(saida) for v in VARIAVEIS_PROP_FINITA(premissa))
        + VARIAVEIS_PROP_FINITA(CONCLUSAO_DE(saida))
    )
    for valoracao in VALORACOES_PROP_FINITA(variaveis):
        premissas_satisfeitas = all(AVALIAR_PROP_FINITA(p, valoracao) for p in PREMISSAS_DE(saida))
        if premissas_satisfeitas and not AVALIAR_PROP_FINITA(CONCLUSAO_DE(saida), valoracao):
            return F
    return V


# --------------------------------------------------------------------
# Etapa 383 — Solidez de uma regra de quantificador: sobre uma AMOSTRA
# explícita de estruturas finitas dadas pelo chamador (mesma fronteira
# honesta de `EQUIVALENCIA_ELEMENTAR_FINITA`, etapa 368 — não é "toda
# estrutura possível"), se a estrutura satisfaz as premissas, satisfaz a
# conclusão.
# --------------------------------------------------------------------
def SOLIDEZ_REGRA_QUANTIFICADOR_FINITA(nome_regra, entradas, saida, argumento, estruturas):
    if not _bool_to_py(PASSO_VALIDO(nome_regra, entradas, saida, argumento)):
        return F
    for estrutura in estruturas:
        premissas_satisfeitas = all(
            _bool_to_py(SATISFAZ_FINITA(estrutura, p)) for p in PREMISSAS_DE(saida)
        )
        if premissas_satisfeitas and not _bool_to_py(SATISFAZ_FINITA(estrutura, CONCLUSAO_DE(saida))):
            return F
    return V


# --------------------------------------------------------------------
# Etapa 384 — Validação cruzada: um passo é sólido sse `PASSO_VALIDO` já
# o aceitava E a checagem semântica (382 ou 383, conforme a regra) também
# concorda. Não é uma nova fonte de verdade — é a confirmação de que as
# duas rotas (sintática e semântica) concordam.
# --------------------------------------------------------------------
_REGRAS_PROPOSICIONAIS = frozenset({
    "premissa", "e_intro", "e_elim_esq", "e_elim_dir",
    "ou_intro", "ou_elim", "modus_ponens", "implica_intro",
})
_REGRAS_QUANTIFICADOR = frozenset({
    "para_todo_intro", "para_todo_elim", "existe_intro", "existe_elim",
})


def REGRA_SOLIDA_FINITA(nome_regra, entradas, saida, argumento=None, estruturas=()):
    if nome_regra in _REGRAS_PROPOSICIONAIS:
        return SOLIDEZ_REGRA_PROPOSICIONAL_FINITA(nome_regra, entradas, saida, argumento)
    if nome_regra in _REGRAS_QUANTIFICADOR:
        return SOLIDEZ_REGRA_QUANTIFICADOR_FINITA(nome_regra, entradas, saida, argumento, estruturas)
    raise ValueError(f"regra desconhecida para checagem de solidez: {nome_regra}")


# ==========================================================================
# Etapas 385-390 — Busca de derivação por enumeração finita.
# ==========================================================================

def _subformulas(formula):
    """Fecho por subfórmula — SEMPRE finito, porque toda fórmula é uma
    árvore finita. Este fecho é o único universo que a busca considera."""
    pendentes = [formula]
    vistas = []
    while pendentes:
        atual = pendentes.pop()
        if _contem(vistas, atual):
            continue
        vistas.append(atual)
        if isinstance(atual, tuple) and len(atual) == 3 and atual[0] in ("e", "ou", "implica"):
            pendentes.append(atual[1])
            pendentes.append(atual[2])
    return tuple(vistas)


# --------------------------------------------------------------------
# Etapa 385 — Estado de busca finito: hipóteses `gamma`, o fecho por
# subfórmula (o universo finito de fórmulas consideradas), o que já foi
# provado (fórmula -> índice do passo que a prova) e os passos acumulados.
# --------------------------------------------------------------------
def ESTADO_BUSCA_FINITO(gamma, chi):
    universo = _unicos(tuple(f for g in gamma for f in _subformulas(g)) + _subformulas(chi))
    passos = tuple(PASSO_DERIVACAO("premissa", (), SEQUENTE_FINITO(gamma, g)) for g in _unicos(gamma))
    provado = {SEQUENTE_FINITO(gamma, g)[2]: i for i, g in enumerate(_unicos(gamma))}
    return {"gamma": tuple(gamma), "universo": universo, "provado": dict(provado), "passos": list(passos)}


# --------------------------------------------------------------------
# Etapa 386 — Passo de busca: uma rodada de encadeamento progressivo.
# Tenta modus ponens, ∧-introdução, ∧-eliminação e ∨-introdução sobre o
# que já está provado, restrito ao universo finito do estado. Devolve um
# NOVO estado e se algo mudou nesta rodada (para detectar ponto fixo).
# --------------------------------------------------------------------
def PASSO_DE_BUSCA_FINITO(estado):
    gamma = estado["gamma"]
    provado = dict(estado["provado"])
    passos = list(estado["passos"])
    mudou = False

    def _marca(formula, passo):
        nonlocal mudou
        if formula not in provado:
            passos.append(passo)
            provado[formula] = len(passos) - 1
            mudou = True

    for formula in estado["universo"]:
        if isinstance(formula, tuple) and len(formula) == 3 and formula[0] == "implica":
            antecedente, consequente = formula[1], formula[2]
            if formula in provado and antecedente in provado and consequente in estado["universo"]:
                _marca(consequente, PASSO_DERIVACAO(
                    "modus_ponens", (provado[antecedente], provado[formula]),
                    SEQUENTE_FINITO(gamma, consequente),
                ))
        if isinstance(formula, tuple) and len(formula) == 3 and formula[0] == "e":
            esquerda, direita = formula[1], formula[2]
            if esquerda in provado and direita in provado:
                _marca(formula, PASSO_DERIVACAO(
                    "e_intro", (provado[esquerda], provado[direita]),
                    SEQUENTE_FINITO(gamma, formula),
                ))
            if formula in provado:
                _marca(esquerda, PASSO_DERIVACAO(
                    "e_elim_esq", (provado[formula],), SEQUENTE_FINITO(gamma, esquerda),
                ))
                _marca(direita, PASSO_DERIVACAO(
                    "e_elim_dir", (provado[formula],), SEQUENTE_FINITO(gamma, direita),
                ))
        if isinstance(formula, tuple) and len(formula) == 3 and formula[0] == "ou":
            esquerda, direita = formula[1], formula[2]
            if esquerda in provado:
                _marca(formula, PASSO_DERIVACAO(
                    "ou_intro", (provado[esquerda],), SEQUENTE_FINITO(gamma, formula),
                ))
            elif direita in provado:
                _marca(formula, PASSO_DERIVACAO(
                    "ou_intro", (provado[direita],), SEQUENTE_FINITO(gamma, formula),
                ))

    novo_estado = {"gamma": gamma, "universo": estado["universo"], "provado": provado, "passos": passos}
    return novo_estado, mudou


# --------------------------------------------------------------------
# Etapa 387 — Poda: `_marca` (386) só acrescenta uma fórmula ainda não em
# `provado`. Como `universo` é finito (385), o número de fórmulas que
# ainda podem ser marcadas cai estritamente a cada rodada que muda algo —
# o que garante término em no máximo `len(universo)` rodadas.
# --------------------------------------------------------------------
def LIMITE_RODADAS_BUSCA_FINITA(estado):
    return len(estado["universo"])


# --------------------------------------------------------------------
# Etapa 388 — Busca de derivação por enumeração finita. Roda o passo de
# busca (386) até ponto fixo (nada muda) ou até `chi` ser provado, dentro
# do limite garantido pela poda (387). Devolve a derivação encontrada
# (tupla de passos) ou `None` se `chi` não está no fecho alcançável.
# --------------------------------------------------------------------
def BUSCA_DERIVACAO_FINITA(gamma, chi):
    estado = ESTADO_BUSCA_FINITO(gamma, chi)
    limite = LIMITE_RODADAS_BUSCA_FINITA(estado)
    for _ in range(limite + 1):
        if chi in estado["provado"]:
            break
        estado, mudou = PASSO_DE_BUSCA_FINITO(estado)
        if not mudou:
            break
    if chi not in estado["provado"]:
        return None
    return RECONSTRUIR_TESTEMUNHA_FINITA(tuple(estado["passos"]), chi)


# --------------------------------------------------------------------
# Etapa 389 — Testemunha construída: trunca a lista de passos logo após o
# passo que prova `formula` — os índices anteriores continuam válidos
# (só referenciam passos ainda mais antigos), e o resultado é uma
# derivação completa e re-verificável por `DERIVACAO_VALIDA`, não uma
# alegação de existência.
# --------------------------------------------------------------------
def RECONSTRUIR_TESTEMUNHA_FINITA(passos, formula):
    for indice, passo in enumerate(passos):
        if CONCLUSAO_DE(passo[2]) == formula:
            return passos[: indice + 1]
    return None


# --------------------------------------------------------------------
# Etapa 390 — Fechamento da busca de derivação.
# --------------------------------------------------------------------
def FECHAMENTO_BUSCA_DERIVACAO_FINITA():
    return V


# ==========================================================================
# Etapas 391-398 — Completude relativa, consistência, independência,
# comprimento, estratégias e correção do buscador.
# ==========================================================================

# --------------------------------------------------------------------
# Etapa 391-392 — Completude relativa ao fragmento de Horn positivo:
# comparação EXAUSTIVA entre `BUSCA_DERIVACAO_FINITA` e o oráculo semântico
# `CONSEQUENCIA_FINITA` (etapa 275) sobre todas as teorias geradas por um
# catálogo finito de cláusulas candidatas.
# --------------------------------------------------------------------
def _potencia_de_dois_por_dobras(n):
    total = 1
    for _ in range(n):
        total = total + total
    return total


def GERAR_TEORIAS_HORN_FINITAS(catalogo):
    n = len(catalogo)
    total_mascaras = _potencia_de_dois_por_dobras(n)
    for mascara in range(total_mascaras):
        yield tuple(catalogo[i] for i in range(n) if (mascara >> i) & 1)


def BUSCA_CONCORDA_COM_ORACULO_FINITA(gamma, chi):
    encontrada = BUSCA_DERIVACAO_FINITA(gamma, chi)
    consequencia_semantica = _bool_to_py(CONSEQUENCIA_FINITA(gamma, chi))
    return _bool(consequencia_semantica if encontrada is not None else not consequencia_semantica)


def COMPLETUDE_HORN_FINITA(catalogo, metas):
    total = 0
    concordou = 0
    for teoria in GERAR_TEORIAS_HORN_FINITAS(catalogo):
        for meta in metas:
            total += 1
            if _bool_to_py(BUSCA_CONCORDA_COM_ORACULO_FINITA(teoria, meta)):
                concordou += 1
    return (concordou, total)


# --------------------------------------------------------------------
# Etapa 393 — Limite honesto: um contraexemplo genuíno fora do fragmento
# (exige ∨-eliminação / prova por casos), onde a busca corretamente NÃO
# encontra uma derivação que o oráculo semântico confirma ser válida.
# --------------------------------------------------------------------
def LIMITE_BUSCA_FORA_DO_FRAGMENTO_FINITA(gamma, chi):
    encontrada = BUSCA_DERIVACAO_FINITA(gamma, chi)
    semantico = CONSEQUENCIA_FINITA(gamma, chi)
    return _bool(encontrada is None and _bool_to_py(semantico))


# --------------------------------------------------------------------
# Etapa 394 — Consistência de uma teoria finita: nenhuma fórmula `f` e sua
# negação estrutural (aqui, sem operador NAO no fragmento positivo, a
# checagem de consistência é: nenhum par de fórmulas antagônicas
# explicitamente fornecido é provado simultaneamente dentro do fecho de
# busca).
# --------------------------------------------------------------------
def CONSISTENTE_POR_BUSCA_FINITA(gamma, pares_antagonicos):
    estado = ESTADO_BUSCA_FINITO(gamma, gamma[0] if gamma else ("var", "_"))
    limite = LIMITE_RODADAS_BUSCA_FINITA(estado)
    for _ in range(limite + 1):
        estado, mudou = PASSO_DE_BUSCA_FINITO(estado)
        if not mudou:
            break
    for a, b in pares_antagonicos:
        if a in estado["provado"] and b in estado["provado"]:
            return F
    return V


# --------------------------------------------------------------------
# Etapa 395 — Independência de premissa: remover a premissa no índice
# `indice` derruba a consequência semântica de `chi` (confirmado pelo
# oráculo, não pela busca — a independência é uma propriedade do
# conteúdo lógico, não do algoritmo de busca).
# --------------------------------------------------------------------
def PREMISSA_INDEPENDENTE_FINITA(gamma, chi, indice):
    resto = gamma[:indice] + gamma[indice + 1:]
    ainda_consequencia = _bool_to_py(CONSEQUENCIA_FINITA(resto, chi)) if resto else False
    return _bool(not ainda_consequencia)


# --------------------------------------------------------------------
# Etapa 396 — Comprimento de derivação e derivação mínima entre
# alternativas já encontradas.
# --------------------------------------------------------------------
def COMPRIMENTO_DERIVACAO_FINITA(passos):
    return len(passos)


def MENOR_DERIVACAO_FINITA(*derivacoes):
    candidatas = tuple(d for d in derivacoes if d is not None)
    if not candidatas:
        return None
    return min(candidatas, key=COMPRIMENTO_DERIVACAO_FINITA)


# --------------------------------------------------------------------
# Etapa 397 — Comparação de estratégias: busca até ponto fixo (388) vs.
# busca limitada a um número fixo de rodadas — mostra concretamente que
# limitar a profundidade pode custar a derivação, sem invalidar a regra.
# --------------------------------------------------------------------
def BUSCA_DERIVACAO_PROFUNDIDADE_LIMITADA_FINITA(gamma, chi, rodadas):
    estado = ESTADO_BUSCA_FINITO(gamma, chi)
    for _ in range(rodadas):
        if chi in estado["provado"]:
            break
        estado, mudou = PASSO_DE_BUSCA_FINITO(estado)
        if not mudou:
            break
    if chi not in estado["provado"]:
        return None
    return RECONSTRUIR_TESTEMUNHA_FINITA(tuple(estado["passos"]), chi)


# --------------------------------------------------------------------
# Etapa 398 — Correção do buscador: toda derivação que ele devolve passa
# por `DERIVACAO_VALIDA` — o verificador da etapa 379, escrito e testado
# independentemente do algoritmo de busca.
# --------------------------------------------------------------------
def BUSCADOR_CORRETO_FINITA(gamma, chi):
    encontrada = BUSCA_DERIVACAO_FINITA(gamma, chi)
    if encontrada is None:
        return V
    return _bool(
        _bool_to_py(DERIVACAO_VALIDA(encontrada))
        and CONCLUSAO_FINAL_DA_DERIVACAO(encontrada) == chi
    )


# --------------------------------------------------------------------
# Etapa 399 — Aplicação de ponta a ponta: a busca encontra sozinha a
# derivação de `s` a partir de `{p, p→q, q→r, r→s}` (três modus ponens em
# cadeia) sem que nenhum passo tenha sido fornecido manualmente.
# --------------------------------------------------------------------
def DEMONSTRACAO_PONTA_A_PONTA_FINITA(gamma, chi):
    derivacao = BUSCA_DERIVACAO_FINITA(gamma, chi)
    if derivacao is None:
        return None
    return derivacao


# --------------------------------------------------------------------
# Etapa 400 — Fechamento do arco lógico 341-400.
# --------------------------------------------------------------------
def FECHAMENTO_ARCO_LOGICO_341_400():
    return V
