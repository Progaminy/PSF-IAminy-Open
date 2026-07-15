import pytest

from nucleo.equacao_quadratica_exata import (
    raiz_quadrada_exata_ou_none,
    resolver_quadratica_exata,
)
from nucleo.reais_intervalos_naturais import RacionalAssinado


def test_raiz_quadrada_exata_de_inteiro_perfeito():
    assert raiz_quadrada_exata_ou_none(RacionalAssinado(16)) == RacionalAssinado(4)
    assert raiz_quadrada_exata_ou_none(RacionalAssinado(0)) == RacionalAssinado(0)


def test_raiz_quadrada_exata_de_fracao():
    # 4/9 = (2/3)²
    assert raiz_quadrada_exata_ou_none(RacionalAssinado(4, 9)) == RacionalAssinado(2, 3)


def test_raiz_quadrada_nao_exata_devolve_none():
    assert raiz_quadrada_exata_ou_none(RacionalAssinado(8)) is None
    assert raiz_quadrada_exata_ou_none(RacionalAssinado(2)) is None


def test_raiz_quadrada_de_negativo_devolve_none():
    assert raiz_quadrada_exata_ou_none(RacionalAssinado(-4)) is None


def test_quadratica_com_raizes_inteiras():
    # x² - 5x + 6 = 0  ->  raízes 2 e 3
    raizes = resolver_quadratica_exata(RacionalAssinado(1), RacionalAssinado(-5), RacionalAssinado(6))
    assert raizes is not None
    assert set(raizes) == {RacionalAssinado(2), RacionalAssinado(3)}


def test_quadratica_com_discriminante_zero():
    # x² - 4x + 4 = 0  ->  raiz dupla 2
    raizes = resolver_quadratica_exata(RacionalAssinado(1), RacionalAssinado(-4), RacionalAssinado(4))
    assert raizes == (RacionalAssinado(2), RacionalAssinado(2))


def test_quadratica_com_discriminante_nao_quadrado_perfeito():
    # x² - 2 = 0 -> raízes ±√2, irracionais
    raizes = resolver_quadratica_exata(RacionalAssinado(1), RacionalAssinado(0), RacionalAssinado(-2))
    assert raizes is None


def test_quadratica_rejeita_a_igual_a_zero():
    with pytest.raises(ValueError, match="não é uma equação quadrática"):
        resolver_quadratica_exata(RacionalAssinado(0), RacionalAssinado(1), RacionalAssinado(1))
