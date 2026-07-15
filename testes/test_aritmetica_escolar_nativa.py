import pytest

from nucleo.aritmetica_escolar_nativa import dividir_com_resto


def test_dividir_com_resto_reparte_com_sobra():
    assert dividir_com_resto(47, 10) == (4, 7)
    assert dividir_com_resto(100, 10) == (10, 0)
    assert dividir_com_resto(9, 10) == (0, 9)


def test_dividir_com_resto_coincide_com_dividir_exato_quando_fecha():
    assert dividir_com_resto(20, 5) == (4, 0)


def test_dividir_com_resto_rejeita_partes_zero():
    with pytest.raises(ValueError, match="não existe divisão por zero"):
        dividir_com_resto(5, 0)
