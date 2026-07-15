import pytest

from nucleo.conversao_unidades import (
    CENTIMETRO_PARA_METRO,
    FatorConversao,
    GRAMA_PARA_QUILO,
    HORA_PARA_MINUTO,
    METRO_PARA_CENTIMETRO,
    MINUTO_PARA_HORA,
    QUILO_PARA_GRAMA,
    converter,
)
from nucleo.medidas_grandezas import Comprimento, Massa, Tempo
from nucleo.reais_intervalos_naturais import RacionalAssinado


def test_converter_metro_para_centimetro():
    dois_metros = Comprimento(RacionalAssinado(2))
    convertido = converter(dois_metros, METRO_PARA_CENTIMETRO)
    assert convertido == Comprimento(RacionalAssinado(200))
    assert type(convertido) is Comprimento


def test_converter_centimetro_para_metro_e_volta():
    duzentos_cm = Comprimento(RacionalAssinado(200))
    metros = converter(duzentos_cm, CENTIMETRO_PARA_METRO)
    assert metros == Comprimento(RacionalAssinado(2))
    de_volta = converter(metros, METRO_PARA_CENTIMETRO)
    assert de_volta == duzentos_cm


def test_converter_quilo_para_grama_e_massa_preservada():
    massa = Massa(RacionalAssinado(3, 2))  # 1.5 kg
    convertida = converter(massa, QUILO_PARA_GRAMA)
    assert convertida == Massa(RacionalAssinado(1500))
    assert type(convertida) is Massa


def test_converter_grama_para_quilo():
    massa = Massa(RacionalAssinado(500))
    convertida = converter(massa, GRAMA_PARA_QUILO)
    assert convertida == Massa(RacionalAssinado(1, 2))


def test_converter_hora_para_minuto_e_tempo_preservado():
    tempo = Tempo(RacionalAssinado(2))
    convertido = converter(tempo, HORA_PARA_MINUTO)
    assert convertido == Tempo(RacionalAssinado(120))
    assert type(convertido) is Tempo


def test_converter_minuto_para_hora():
    tempo = Tempo(RacionalAssinado(90))
    convertido = converter(tempo, MINUTO_PARA_HORA)
    assert convertido == Tempo(RacionalAssinado(3, 2))


def test_fator_conversao_rejeita_fator_nao_positivo():
    with pytest.raises(ValueError, match="fator de conversão"):
        FatorConversao("a", "b", RacionalAssinado(0))
