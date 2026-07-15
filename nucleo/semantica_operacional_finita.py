# ==============================================================================
# SEMÂNTICA OPERACIONAL FINITA — Etapas 481 a 520 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   depois de gramáticas formais finitas, o próximo passo natural é dar
#   significado à execução: configuração, regra de transição, traço finito,
#   reescrita e interpretação limitada. Nada aqui usa divisão, módulo,
#   primalidade, fatoração, infinitos atuais ou linguagem geral sem limite.
# ==============================================================================
from .primitivas import V, F


def _bool(condicao):
    return V if condicao else F


def _bool_to_py(valor):
    return valor(True)(False)


def CONFIGURACAO_OPERACIONAL_FINITA(estado, entrada=(), memoria=None, saida=(), combustivel=None):
    """Configuração finita auditável.

    `combustivel` é opcional, mas quando aparece torna explícito que a execução
    não é infinita. O motor usa também limites externos de passos.
    """
    return {
        "estado": estado,
        "entrada": tuple(entrada),
        "memoria": dict(memoria or {}),
        "saida": tuple(saida),
        "combustivel": combustivel,
    }


def REGRA_OPERACIONAL_FINITA(nome, condicao, acao):
    """Regra finita: se `condicao(config)` vale, `acao(config)` produz nova config."""
    return {"nome": nome, "condicao": condicao, "acao": acao}


def REGRA_APLICAVEL_FINITA(regra, configuracao):
    return _bool(bool(regra["condicao"](configuracao)))


def APLICAR_REGRA_FINITA(regra, configuracao):
    if not _bool_to_py(REGRA_APLICAVEL_FINITA(regra, configuracao)):
        return configuracao
    nova = regra["acao"](configuracao)
    if not isinstance(nova, dict) or "estado" not in nova:
        raise ValueError("ação operacional precisa devolver configuração")
    return nova


def PASSO_OPERACIONAL_FINITO(regras, configuracao):
    """Aplica a primeira regra aplicável, preservando determinismo declarado."""
    for regra in regras:
        if _bool_to_py(REGRA_APLICAVEL_FINITA(regra, configuracao)):
            return APLICAR_REGRA_FINITA(regra, configuracao)
    return configuracao


def EXECUTAR_PASSOS_FINITOS(regras, configuracao, limite_passos):
    atual = configuracao
    traco = [atual]
    for _ in range(limite_passos):
        combustivel = atual.get("combustivel")
        if combustivel is not None and combustivel <= 0:
            break
        proxima = PASSO_OPERACIONAL_FINITO(regras, atual)
        if proxima == atual:
            break
        traco.append(proxima)
        atual = proxima
    return tuple(traco)


def TERMINA_EM_ATE_FINITO(regras, configuracao, limite_passos):
    traco = EXECUTAR_PASSOS_FINITOS(regras, configuracao, limite_passos)
    ultima = traco[-1]
    return _bool(PASSO_OPERACIONAL_FINITO(regras, ultima) == ultima)


# ----------------------------------------------------------------------------
# Linguagem de expressões finitas: nasce como objeto semântico mínimo.
# ----------------------------------------------------------------------------
def LIT(valor):
    return ("lit", valor)


def VAR(nome):
    return ("var", nome)


def ADD(a, b):
    return ("add", a, b)


def MUL(a, b):
    return ("mul", a, b)


def LET(nome, valor, corpo):
    return ("let", nome, valor, corpo)


def EH_VALOR_FINITO(expressao):
    return _bool(isinstance(expressao, tuple) and len(expressao) == 2 and expressao[0] == "lit")


def AVALIAR_EXPRESSAO_FINITA(expressao, ambiente=None, limite_passos=100):
    """Avalia expressão por redução finita, não por mágica externa.

    Operações permitidas aqui: adição e multiplicação já nasceram no fluxo.
    Sem divisão, resto, raiz, primalidade ou modularidade.
    """
    ambiente = dict(ambiente or {})

    def reduzir(expr, env, combustivel):
        if combustivel <= 0:
            raise RuntimeError("limite finito de avaliação esgotado")
        tipo = expr[0]
        if tipo == "lit":
            return expr[1]
        if tipo == "var":
            if expr[1] not in env:
                raise NameError(f"variável sem valor: {expr[1]}")
            return env[expr[1]]
        if tipo == "add":
            return reduzir(expr[1], env, combustivel - 1) + reduzir(expr[2], env, combustivel - 1)
        if tipo == "mul":
            return reduzir(expr[1], env, combustivel - 1) * reduzir(expr[2], env, combustivel - 1)
        if tipo == "let":
            novo = dict(env)
            novo[expr[1]] = reduzir(expr[2], env, combustivel - 1)
            return reduzir(expr[3], novo, combustivel - 1)
        raise ValueError(f"expressão desconhecida: {tipo}")

    return reduzir(expressao, ambiente, limite_passos)


# ----------------------------------------------------------------------------
# Reescrita finita: semântica como transformação de termos.
# ----------------------------------------------------------------------------
def TERMO_FINITO(simbolo, *filhos):
    return (simbolo,) + tuple(filhos)


def REGRA_REESCRITA_FINITA(padrao, substituto):
    return (padrao, substituto)


def REESCREVER_RAIZ_FINITA(regras, termo):
    for padrao, substituto in regras:
        if termo == padrao:
            return substituto
    return termo


def REESCREVER_UM_PASSO_FINITO(regras, termo):
    direto = REESCREVER_RAIZ_FINITA(regras, termo)
    if direto != termo:
        return direto
    if not isinstance(termo, tuple) or len(termo) <= 1:
        return termo
    simbolo = termo[0]
    filhos = list(termo[1:])
    for i, filho in enumerate(filhos):
        novo = REESCREVER_UM_PASSO_FINITO(regras, filho)
        if novo != filho:
            filhos[i] = novo
            return (simbolo,) + tuple(filhos)
    return termo


def FORMA_NORMAL_FINITA(regras, termo, limite_passos):
    atual = termo
    for _ in range(limite_passos):
        proximo = REESCREVER_UM_PASSO_FINITO(regras, atual)
        if proximo == atual:
            return atual
        atual = proximo
    raise RuntimeError("limite finito de reescrita esgotado")


def CONFLUENCIA_POR_CATALOGO_FINITA(regras_a, regras_b, termos, limite_passos):
    """Compara duas estratégias/regras sobre catálogo finito declarado."""
    for termo in termos:
        if FORMA_NORMAL_FINITA(regras_a, termo, limite_passos) != FORMA_NORMAL_FINITA(regras_b, termo, limite_passos):
            return F
    return V


def FECHAMENTO_SEMANTICA_OPERACIONAL_FINITA():
    return V
