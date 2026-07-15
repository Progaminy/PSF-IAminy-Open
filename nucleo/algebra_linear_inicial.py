# ==============================================================================
# POLINÓMIOS E ÁLGEBRA LINEAR FINITA INICIAL — Etapas 101 a 107 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   polinómio nasce depois de anel (precisa de soma e produto); vetor nasce
#   depois de corpo (precisa de escalares com inverso); matriz nasce depois
#   de vetor; determinante nasce depois de matriz.
#
# Representação: um polinómio é uma tupla finita de coeficientes (a0, a1,
# ..., an) representando a0 + a1·x + ... + an·xⁿ — mesma disciplina das
# etapas 61-100: estrutura finita explícita (tupla Python), operações
# feitas com SOMA/MULT do anel/corpo já validado (nunca + ou × nativos
# sobre os coeficientes).
#
# Conceitos permitidos aqui:
#   V/F, igualdade, domínio finito explícito, tudo o que nasceu nas
#   etapas 1-100 (grupo, anel, corpo).
# Conceitos proibidos aqui:
#   polinómios sobre corpos infinitos, espaços vetoriais de dimensão
#   infinita, autovalores/autovetores, formas quadráticas, estruturas
#   ainda não construídas.
# ==============================================================================
from .primitivas import V, F
from .logica import E
from .aritmetica import IGUAL
from .traducao import para_bool


# ----------------------------------------------------------------------------
# Etapa 101 — polinómio sobre um anel: tupla de coeficientes, índice = grau.
# ----------------------------------------------------------------------------
POLINOMIO_PURO = lambda *coeficientes: tuple(coeficientes)


# ----------------------------------------------------------------------------
# Etapa 102 — grau e operações polinomiais.
# ----------------------------------------------------------------------------
def GRAU_PURO(p, zero):
    """Maior índice com coeficiente não-nulo. Polinómio nulo -> grau None
    (grau do polinómio zero não está definido classicamente)."""
    for i in range(len(p) - 1, -1, -1):
        if not para_bool(IGUAL(p[i])(zero)):
            return i
    return None


def SOMA_POLINOMIOS_PURA(p, q, soma_anel, zero):
    n = max(len(p), len(q))
    p_estendido = p + (zero,) * (n - len(p))
    q_estendido = q + (zero,) * (n - len(q))
    return tuple(soma_anel(p_estendido[i])(q_estendido[i]) for i in range(n))


def MULT_POLINOMIOS_PURA(p, q, soma_anel, produto_anel, zero):
    if not p or not q:
        return ()
    n = len(p) + len(q) - 1
    resultado = [zero] * n
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            resultado[i + j] = soma_anel(resultado[i + j])(produto_anel(a)(b))
    return tuple(resultado)


# ----------------------------------------------------------------------------
# Etapa 103 — avaliação e raízes de polinómios.
# Avaliação por Horner: evita potências repetidas, só soma e produto.
# ----------------------------------------------------------------------------
def AVALIAR_POLINOMIO_PURO(p, x, soma_anel, produto_anel, zero):
    resultado = zero
    for coeficiente in reversed(p):
        resultado = soma_anel(produto_anel(resultado)(x))(coeficiente)
    return resultado


def EH_RAIZ_PURA(p, x, soma_anel, produto_anel, zero):
    return IGUAL(AVALIAR_POLINOMIO_PURO(p, x, soma_anel, produto_anel, zero))(zero)


def RAIZES_EM_DOMINIO_PURA(p, dominio, soma_anel, produto_anel, zero):
    """Busca exaustiva das raízes de p dentro de um domínio finito
    explícito — não um método analítico (não existe um aqui; correto
    porque o domínio é finito e pequeno, mesma disciplina de sempre)."""
    return tuple(x for x in dominio if para_bool(EH_RAIZ_PURA(p, x, soma_anel, produto_anel, zero)))


# ----------------------------------------------------------------------------
# Etapa 104 — espaço vetorial finito inicial: vetor = tupla de escalares
# de um corpo já validado; soma componente-a-componente, escalar×vetor.
# ----------------------------------------------------------------------------
def SOMA_VETORES_PURA(u, v, soma_corpo):
    return tuple(soma_corpo(u[i])(v[i]) for i in range(len(u)))


def ESCALAR_VEZES_VETOR_PURA(c, v, produto_corpo):
    return tuple(produto_corpo(c)(vi) for vi in v)


def ESPACO_VETORIAL_FECHADO_PURO(vetores, escalares, soma_corpo, produto_corpo):
    """Confere fechamento: soma de dois vetores do conjunto e escalar×vetor
    continuam representáveis (mesma dimensão) — verificação estrutural,
    não uma prova formal dos oito axiomas de espaço vetorial (esses
    seguem diretamente de (corpo,+,×) já validados nas etapas 91-94)."""
    dimensao = len(vetores[0]) if vetores else 0
    fechada_soma = all(len(SOMA_VETORES_PURA(u, v, soma_corpo)) == dimensao for u in vetores for v in vetores)
    fechada_escalar = all(len(ESCALAR_VEZES_VETOR_PURA(c, v, produto_corpo)) == dimensao for c in escalares for v in vetores)
    return V if (fechada_soma and fechada_escalar) else F


# ----------------------------------------------------------------------------
# Etapa 105 — combinação linear e base.
# ----------------------------------------------------------------------------
def COMBINACAO_LINEAR_PURA(escalares, vetores, soma_corpo, produto_corpo, zero_vetor):
    resultado = zero_vetor
    for c, v in zip(escalares, vetores):
        resultado = SOMA_VETORES_PURA(resultado, ESCALAR_VEZES_VETOR_PURA(c, v, produto_corpo), soma_corpo)
    return resultado


def GERA_VETOR_PURA(alvo, vetores, escalares_possiveis, soma_corpo, produto_corpo, zero_vetor):
    """alvo é combinação linear de `vetores` usando ALGUMA escolha de
    escalares em `escalares_possiveis`? Busca exaustiva — correta porque
    o corpo e o conjunto de vetores candidatos são finitos e pequenos."""
    from itertools import product as produto_cartesiano

    for combinacao in produto_cartesiano(escalares_possiveis, repeat=len(vetores)):
        candidato = COMBINACAO_LINEAR_PURA(list(combinacao), vetores, soma_corpo, produto_corpo, zero_vetor)
        if all(para_bool(IGUAL(candidato[i])(alvo[i])) for i in range(len(alvo))):
            return True
    return False


def BASE_GERA_ESPACO_PURA(vetores_base, espaco, escalares_possiveis, soma_corpo, produto_corpo, zero_vetor):
    """Todo vetor do espaço é combinação linear da base candidata?"""
    return V if all(
        GERA_VETOR_PURA(alvo, vetores_base, escalares_possiveis, soma_corpo, produto_corpo, zero_vetor)
        for alvo in espaco
    ) else F


# ----------------------------------------------------------------------------
# Etapa 106 — matriz como aplicação linear finita: tupla de tuplas
# (linhas); aplicar a uma matriz a um vetor é multiplicação matriz-vetor.
# ----------------------------------------------------------------------------
def APLICAR_MATRIZ_PURA(matriz, v, soma_corpo, produto_corpo, zero):
    resultado = []
    for linha in matriz:
        soma = zero
        for i, coeficiente in enumerate(linha):
            soma = soma_corpo(soma)(produto_corpo(coeficiente)(v[i]))
        resultado.append(soma)
    return tuple(resultado)


# ----------------------------------------------------------------------------
# Etapa 107 — determinante em dimensão pequena (2×2 e 3×3, por fórmula
# fechada — não eliminação gaussiana geral, fora do escopo desta etapa).
#
# AVISO DE USO (descoberto ao testar, não hipotético): `sub_corpo` PRECISA
# ser uma subtração verdadeira (ex.: SUB modular de Z/nZ, como a etapa 91
# já usa), não a SUB truncada de aritmetica.py. Cofatores intermédios são
# frequentemente negativos (ex.: 1×0 − 4×6 = −24); com SUB truncada isso
# silenciosamente vira 0 em vez de −24, e o determinante final sai errado
# sem qualquer erro ou aviso. Testado: usar SUB truncada sobre uma matriz
# 3×3 comum deu determinante 0 em vez do valor correto — só descoberto
# comparando contra o cálculo à mão. Ver testes/test_algebra_linear_inicial.py.
# ----------------------------------------------------------------------------
def DETERMINANTE_2X2_PURO(matriz, soma_corpo, produto_corpo, sub_corpo=None):
    a, b = matriz[0]
    c, d = matriz[1]
    # det = ad - bc; sem SUB assinada garantida no corpo genérico, usamos
    # a definição via soma com o oposto, mas para os corpos já validados
    # (Z/nZ) a subtração modular do próprio anel já está disponível via
    # `sub_corpo`, quando fornecida pelo chamador.
    ad = produto_corpo(a)(d)
    bc = produto_corpo(b)(c)
    if sub_corpo is not None:
        return sub_corpo(ad)(bc)
    return (ad, bc)  # sem sub_corpo, devolve o par para o chamador decidir


def DETERMINANTE_3X3_PURO(matriz, soma_corpo, produto_corpo, sub_corpo):
    (a, b, c), (d, e, f), (g, h, i) = matriz
    termo1 = produto_corpo(a)(sub_corpo(produto_corpo(e)(i))(produto_corpo(f)(h)))
    termo2 = produto_corpo(b)(sub_corpo(produto_corpo(d)(i))(produto_corpo(f)(g)))
    termo3 = produto_corpo(c)(sub_corpo(produto_corpo(d)(h))(produto_corpo(e)(g)))
    return sub_corpo(soma_corpo(termo1)(termo3))(termo2)
