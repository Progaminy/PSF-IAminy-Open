import pytest

from nucleo.notacao_cientifica import NotacaoCientifica, notacao_cientifica
from nucleo.reais_intervalos_naturais import RacionalAssinado


def test_notacao_cientifica_numero_de_quatro_digitos():
    resultado = notacao_cientifica(1234)
    assert resultado.mantissa == RacionalAssinado(617, 500)  # 1,234
    assert resultado.expoente == 3
    assert resultado.valor() == RacionalAssinado(1234)


def test_notacao_cientifica_digito_unico():
    resultado = notacao_cientifica(7)
    assert resultado.mantissa == RacionalAssinado(7)
    assert resultado.expoente == 0


def test_notacao_cientifica_potencia_exata_de_dez():
    resultado = notacao_cientifica(100)
    assert resultado.mantissa == RacionalAssinado(1)
    assert resultado.expoente == 2
    assert resultado.valor() == RacionalAssinado(100)


def test_notacao_cientifica_numero_grande():
    resultado = notacao_cientifica(602000)
    assert resultado.expoente == 5
    assert resultado.valor() == RacionalAssinado(602000)


def test_notacao_cientifica_rejeita_nao_positivo():
    with pytest.raises(ValueError, match="inteiro positivo"):
        notacao_cientifica(0)
    with pytest.raises(ValueError, match="inteiro positivo"):
        notacao_cientifica(-5)


def test_notacao_cientifica_rejeita_mantissa_fora_do_intervalo():
    with pytest.raises(ValueError, match="mantissa"):
        NotacaoCientifica(RacionalAssinado(10), 2)
    with pytest.raises(ValueError, match="mantissa"):
        NotacaoCientifica(RacionalAssinado(1, 2), 2)
