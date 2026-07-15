import pytest

from nucleo.regra_de_tres import regra_de_tres_direta, regra_de_tres_inversa
from nucleo.reais_intervalos_naturais import RacionalAssinado


def test_regra_de_tres_direta_classica():
    # 2 kg custam 10 reais; quanto custam 5 kg?
    x = regra_de_tres_direta(RacionalAssinado(2), RacionalAssinado(10), RacionalAssinado(5))
    assert x == RacionalAssinado(25)


def test_regra_de_tres_direta_rejeita_primeiro_termo_zero():
    with pytest.raises(ValueError, match="primeiro termo"):
        regra_de_tres_direta(RacionalAssinado(0), RacionalAssinado(10), RacionalAssinado(5))


def test_regra_de_tres_inversa_classica():
    # 3 trabalhadores constroem um muro em 12 dias; quantos dias com 4 trabalhadores?
    x = regra_de_tres_inversa(RacionalAssinado(3), RacionalAssinado(12), RacionalAssinado(4))
    assert x == RacionalAssinado(9)


def test_regra_de_tres_inversa_rejeita_segundo_termo_zero():
    with pytest.raises(ValueError, match="segundo termo"):
        regra_de_tres_inversa(RacionalAssinado(3), RacionalAssinado(12), RacionalAssinado(0))
