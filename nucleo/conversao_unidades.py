"""Conversão entre unidades da mesma espécie de grandeza — fator racional exato.

Liga `_GrandezaEscalar` (ETAPA 1036): duas unidades da mesma espécie
(metro/centímetro, quilo/grama, hora/minuto) diferem por um fator
racional fixo. Converter é multiplicar pelo fator; a conferência desfaz a
conversão com o recíproco e exige devolver o valor original — a mesma
disciplina de "ida e volta" já usada em `nucleo/funcoes_avancadas.py`.
"""
from __future__ import annotations

from dataclasses import dataclass

from .medidas_grandezas import _GrandezaEscalar
from .reais_intervalos_naturais import RacionalAssinado


@dataclass(frozen=True, slots=True)
class FatorConversao:
    """Quantas unidades de destino cabem numa unidade de origem."""

    de: str
    para: str
    fator: RacionalAssinado

    def __post_init__(self) -> None:
        if self.fator.numerador <= 0:
            raise ValueError("fator de conversão deve ser positivo")


def converter(grandeza: _GrandezaEscalar, conversao: FatorConversao) -> _GrandezaEscalar:
    """Converte o valor de uma grandeza pelo fator, preservando a espécie.

    Conferido desfazendo a conversão com o fator recíproco: o valor
    original tem que voltar exatamente, não só aproximadamente.
    """
    novo_valor = grandeza.valor.multiplicar(conversao.fator)
    convertida = type(grandeza)(novo_valor)
    de_volta = novo_valor.multiplicar(conversao.fator.reciproco())
    if de_volta != grandeza.valor:
        raise ValueError("conversão não é reversível pelo fator recíproco")
    return convertida


# Fatores de conversão usuais, exatos — cada um é só uma declaração de
# quantas unidades de destino cabem numa unidade de origem, não uma
# grandeza nova.
METRO_PARA_CENTIMETRO = FatorConversao("metro", "centímetro", RacionalAssinado(100))
CENTIMETRO_PARA_METRO = FatorConversao("centímetro", "metro", RacionalAssinado(1, 100))
QUILO_PARA_GRAMA = FatorConversao("quilograma", "grama", RacionalAssinado(1000))
GRAMA_PARA_QUILO = FatorConversao("grama", "quilograma", RacionalAssinado(1, 1000))
HORA_PARA_MINUTO = FatorConversao("hora", "minuto", RacionalAssinado(60))
MINUTO_PARA_HORA = FatorConversao("minuto", "hora", RacionalAssinado(1, 60))
