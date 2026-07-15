import pytest

from nucleo.logaritmos import logaritmo_exato
from nucleo.reais_intervalos_naturais import RacionalAssinado


def test_logaritmo_exato_positivo():
    assert logaritmo_exato(RacionalAssinado(2), RacionalAssinado(8)) == 3
    assert logaritmo_exato(RacionalAssinado(10), RacionalAssinado(100)) == 2
    assert logaritmo_exato(RacionalAssinado(3), RacionalAssinado(1)) == 0


def test_logaritmo_exato_negativo_para_x_menor_que_um():
    assert logaritmo_exato(RacionalAssinado(2), RacionalAssinado(1, 8)) == -3
    assert logaritmo_exato(RacionalAssinado(5), RacionalAssinado(1, 25)) == -2


def test_logaritmo_de_base_menor_que_um():
    # log_(1/2)(1/8) = 3, porque (1/2)^3 = 1/8
    assert logaritmo_exato(RacionalAssinado(1, 2), RacionalAssinado(1, 8)) == 3


def test_logaritmo_rejeita_x_que_nao_e_potencia_exata():
    with pytest.raises(ValueError, match="não é potência exata"):
        logaritmo_exato(RacionalAssinado(2), RacionalAssinado(5), limite_busca=20)


def test_logaritmo_rejeita_base_invalida():
    with pytest.raises(ValueError, match="base do logaritmo"):
        logaritmo_exato(RacionalAssinado(1), RacionalAssinado(5))
    with pytest.raises(ValueError, match="base do logaritmo"):
        logaritmo_exato(RacionalAssinado(-2), RacionalAssinado(4))


def test_logaritmo_rejeita_x_nao_positivo():
    with pytest.raises(ValueError, match="x positivo"):
        logaritmo_exato(RacionalAssinado(2), RacionalAssinado(0))
