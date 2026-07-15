# ==============================================================================
# RETICULADO FINITO — Etapa 1067 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   não recomeça do zero — reaproveita ordem parcial (etapa 68,
#   `ORDEM_PARCIAL_PURA` de `relacoes_funcoes_naturais.py`). Um reticulado
#   é um poset onde todo par de elementos tem supremo (menor cota
#   superior) e ínfimo (maior cota inferior) dentro do próprio domínio. A
#   unicidade do supremo/ínfimo, quando existe, já vem de graça da
#   antissimetria da ordem parcial — não precisa ser verificada à parte.
#
# Conceitos permitidos: ordem parcial (etapa 68) e tudo o que ela já
# permite (etapas 1-68).
# Conceitos proibidos: os mesmos já proibidos no bloco de relações e
# funções — divisão, módulo, primalidade, fatoração, cardinalidade
# infinita, análise, estruturas ainda não construídas. Reticulados
# INFINITOS e propriedades de completude geral (Knaster-Tarski) ficam
# fora — aqui é busca exaustiva sobre domínio finito, mesma disciplina
# de EXISTE_COLORACAO_PURA.
# ==============================================================================
from .primitivas import V, F
from .logica import E
from .traducao import para_bool
from .relacoes_funcoes_naturais import ORDEM_PARCIAL_PURA, PERTENCE_RELACAO_PURA


def _cotas_superiores(x, y, dominio, relacao):
    return [
        z for z in dominio
        if para_bool(PERTENCE_RELACAO_PURA(x)(z)(relacao))
        and para_bool(PERTENCE_RELACAO_PURA(y)(z)(relacao))
    ]


def _cotas_inferiores(x, y, dominio, relacao):
    return [
        z for z in dominio
        if para_bool(PERTENCE_RELACAO_PURA(z)(x)(relacao))
        and para_bool(PERTENCE_RELACAO_PURA(z)(y)(relacao))
    ]


# ----------------------------------------------------------------------------
# Supremo (menor cota superior) e ínfimo (maior cota inferior) de x e y,
# buscados por exaustão sobre o domínio finito — None quando não existe
# nenhuma cota comum, ou existem várias sem que nenhuma seja a menor/maior
# (não fingimos escolher uma arbitrariamente).
# ----------------------------------------------------------------------------
def SUPREMO_OU_NONE(x, y, dominio, relacao):
    candidatas = _cotas_superiores(x, y, dominio, relacao)
    for z in candidatas:
        if all(para_bool(PERTENCE_RELACAO_PURA(z)(w)(relacao)) for w in candidatas):
            return z
    return None


def INFIMO_OU_NONE(x, y, dominio, relacao):
    candidatas = _cotas_inferiores(x, y, dominio, relacao)
    for z in candidatas:
        if all(para_bool(PERTENCE_RELACAO_PURA(w)(z)(relacao)) for w in candidatas):
            return z
    return None


# ----------------------------------------------------------------------------
# Reticulado: poset (ordem parcial) onde TODO par de elementos do domínio
# tem supremo e ínfimo dentro do próprio domínio. Busca exaustiva sobre os
# |dominio|² pares — mesma disciplina de ORDEM_TOTAL_PURA (comparabilidade
# de todo par) e EXISTE_COLORACAO_PURA.
# ----------------------------------------------------------------------------
def EH_RETICULADO_PURA(dominio, relacao):
    resultado = ORDEM_PARCIAL_PURA(dominio)(relacao)
    for x in dominio:
        for y in dominio:
            tem_supremo = V if SUPREMO_OU_NONE(x, y, dominio, relacao) is not None else F
            tem_infimo = V if INFIMO_OU_NONE(x, y, dominio, relacao) is not None else F
            resultado = E(resultado)(E(tem_supremo)(tem_infimo))
    return resultado
