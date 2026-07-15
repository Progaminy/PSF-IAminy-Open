import pytest

from nucleo.progressoes import ProgressaoAritmetica, ProgressaoGeometrica
from nucleo.reais_intervalos_naturais import RacionalAssinado


def test_progressao_aritmetica_termo_geral_e_soma():
    # 2, 5, 8, 11, 14 (a1=2, razão=3)
    pa = ProgressaoAritmetica(RacionalAssinado(2), RacionalAssinado(3))
    assert pa.termo_geral(1) == RacionalAssinado(2)
    assert pa.termo_geral(5) == RacionalAssinado(14)
    assert pa.soma_termos(5) == RacionalAssinado(40)


def test_progressao_aritmetica_termo_geral_confere_com_recorrencia():
    pa = ProgressaoAritmetica(RacionalAssinado(1, 2), RacionalAssinado(3, 4))
    for n in range(1, 8):
        assert pa.termo_geral(n) == pa.termo_por_recorrencia(n)


def test_progressao_aritmetica_rejeita_indice_invalido():
    pa = ProgressaoAritmetica(RacionalAssinado(1), RacionalAssinado(1))
    with pytest.raises(ValueError, match="n deve ser"):
        pa.termo_geral(0)


def test_progressao_geometrica_termo_geral_e_soma():
    # 3, 6, 12, 24, 48 (a1=3, razão=2)
    pg = ProgressaoGeometrica(RacionalAssinado(3), RacionalAssinado(2))
    assert pg.termo_geral(1) == RacionalAssinado(3)
    assert pg.termo_geral(5) == RacionalAssinado(48)
    assert pg.soma_termos(5) == RacionalAssinado(93)


def test_progressao_geometrica_com_razao_fracionaria():
    # 8, 4, 2, 1, 1/2 (a1=8, razão=1/2)
    pg = ProgressaoGeometrica(RacionalAssinado(8), RacionalAssinado(1, 2))
    assert pg.termo_geral(5) == RacionalAssinado(1, 2)
    assert pg.soma_termos(5) == RacionalAssinado(31, 2)


def test_progressao_geometrica_razao_um_e_soma_constante():
    pg = ProgressaoGeometrica(RacionalAssinado(7), RacionalAssinado(1))
    assert pg.termo_geral(10) == RacionalAssinado(7)
    assert pg.soma_termos(10) == RacionalAssinado(70)


def test_progressao_geometrica_rejeita_razao_nula():
    with pytest.raises(ValueError, match="razão"):
        ProgressaoGeometrica(RacionalAssinado(5), RacionalAssinado(0))
