"""Canal ruidoso -- Fase 5.2 do plano de corretor (técnica 9: "pondera
probabilidade do erro").

`classificar_erro()` é determinístico: usa adjacência de teclado
(`teclado.py`), classe fonética (`fonetica_computavel.py`) e comparação
direta de comprimento/posição entre duas strings -- não é modelo
estatístico nem treinado.

**Diferença consciente do desenho original do plano**: em vez de persistir
o tipo de erro como uma coluna nova no TSV de
`corretor_ortografico_sessao.aprender_correcao` (o que exigiria migrar um
formato já em uso por esse módulo), o tipo é sempre CALCULADO na hora a
partir do par (errado, certo) -- `classificar_erro` é puro e
determinístico, então guardar o resultado seria dado redundante, com risco
real de ficar desatualizado se a classificação evoluir. `contar_erros_da_memoria()`
deriva a distribuição real de tipos de erro já aprovados/aprendidos sem
tocar no ficheiro TSV nem no formato de `aprender_correcao`.
"""
from __future__ import annotations

from collections import Counter
from enum import Enum

from .corretor_ortografico_sessao import pares_aprovados
from .fonetica_computavel import mesma_classe_fonetica
from .normalizacao import sem_acentos
from .teclado import sao_adjacentes


class TipoErro(str, Enum):
    SUBSTITUICAO_TECLADO_ADJACENTE = "substituicao_teclado_adjacente"
    TRANSPOSICAO_ADJACENTE = "transposicao_adjacente"
    INSERCAO = "insercao"
    DELECAO = "delecao"
    SUBSTITUICAO_FONETICA = "substituicao_fonetica"
    ACENTO_AUSENTE = "acento_ausente"
    OUTRO = "outro"


# Pesos iniciais, cada um com racional documentado -- pensados para serem
# REFINADOS (não substituídos) por contagens reais à medida que a memória
# de sessão de `corretor_ortografico_sessao` cresce (ver
# `contar_erros_da_memoria`). Sempre uma tabela de peso transparente e
# editável à mão, nunca um modelo treinado no sentido estatístico.
PESOS_ERRO_BASE: dict[TipoErro, float] = {
    # troca de tecla vizinha é o erro de digitação mais comum -- peso alto.
    TipoErro.SUBSTITUICAO_TECLADO_ADJACENTE: 0.30,
    # trocar duas letras adjacentes de posição é igualmente comum e
    # mecanicamente simples (dedo rápido demais) -- mesmo peso.
    TipoErro.TRANSPOSICAO_ADJACENTE: 0.30,
    # esquecer ou trocar acento é muito comum e quase nunca muda a
    # identidade da palavra -- peso alto.
    TipoErro.ACENTO_AUSENTE: 0.25,
    # confundir grafias que soam parecido (s/ç/z, etc.) é comum em quem
    # escreve de ouvido -- peso alto, um pouco abaixo dos erros mecânicos.
    TipoErro.SUBSTITUICAO_FONETICA: 0.20,
    # inserir ou esquecer uma letra a mais são erros reais, mas menos
    # sistemáticos que os acima -- peso moderado.
    TipoErro.INSERCAO: 0.10,
    TipoErro.DELECAO: 0.10,
    # "outro" cobre qualquer coisa que não bateu em nenhum padrão
    # reconhecido -- peso baixo de propósito, sinal fraco.
    TipoErro.OUTRO: 0.05,
}


def _e_insercao_unica(curto: str, longo: str) -> bool:
    """True se inserir exatamente 1 caractere em `curto` produz `longo`."""
    if len(longo) != len(curto) + 1:
        return False
    i = j = 0
    diferencas = 0
    while i < len(curto) and j < len(longo):
        if curto[i] == longo[j]:
            i += 1
            j += 1
        else:
            diferencas += 1
            j += 1
            if diferencas > 1:
                return False
    return True


def classificar_erro(original: str, candidato: str) -> TipoErro:
    """Classifica de forma determinística o tipo de erro que transforma
    `original` (o que foi escrito) em `candidato` (a forma correta)."""
    if original == candidato:
        raise ValueError("original e candidato são iguais -- não há erro para classificar")

    if sem_acentos(original).casefold() == sem_acentos(candidato).casefold():
        return TipoErro.ACENTO_AUSENTE

    if len(original) == len(candidato):
        posicoes = [i for i, (a, b) in enumerate(zip(original, candidato)) if a != b]
        if len(posicoes) == 1:
            i = posicoes[0]
            if sao_adjacentes(original[i], candidato[i]):
                return TipoErro.SUBSTITUICAO_TECLADO_ADJACENTE
            if mesma_classe_fonetica(original[i], candidato[i]):
                return TipoErro.SUBSTITUICAO_FONETICA
            return TipoErro.OUTRO
        if len(posicoes) == 2:
            i, j = posicoes
            if j == i + 1 and original[i] == candidato[j] and original[j] == candidato[i]:
                return TipoErro.TRANSPOSICAO_ADJACENTE
        return TipoErro.OUTRO

    if len(candidato) == len(original) + 1 and _e_insercao_unica(original, candidato):
        return TipoErro.INSERCAO
    if len(original) == len(candidato) + 1 and _e_insercao_unica(candidato, original):
        return TipoErro.DELECAO

    return TipoErro.OUTRO


def contar_erros_da_memoria() -> Counter:
    """Distribuição real de tipos de erro entre os pares já aprovados
    (whitelist base + memória de sessão aprendida) -- material honesto
    para, no futuro, refinar `PESOS_ERRO_BASE` com contagens reais em vez
    da estimativa inicial."""
    contagem: Counter = Counter()
    for errado, certo, _motivo in pares_aprovados():
        if errado == certo:
            continue
        contagem[classificar_erro(errado, certo)] += 1
    return contagem
