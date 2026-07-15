import pytest

from nucleo.inequacoes import Comparador, resolver_inequacao_linear
from nucleo.reais_intervalos_naturais import RacionalAssinado


def test_inequacao_simples_sem_inversao():
    # x - 7 > 5  ->  x > 12  (equivalente a 3x-7 > 2x+5 após combinar termos)
    solucao = resolver_inequacao_linear(
        RacionalAssinado(1), RacionalAssinado(-7), Comparador.MAIOR, RacionalAssinado(5)
    )
    assert solucao.comparador is Comparador.MAIOR
    assert solucao.limite == RacionalAssinado(12)
    assert solucao.satisfaz(RacionalAssinado(13)) is True
    assert solucao.satisfaz(RacionalAssinado(12)) is False
    assert solucao.satisfaz(RacionalAssinado(11)) is False


def test_inequacao_com_coeficiente_negativo_inverte_comparador():
    # -2x + 3 > 7  ->  x < -2
    solucao = resolver_inequacao_linear(
        RacionalAssinado(-2), RacionalAssinado(3), Comparador.MAIOR, RacionalAssinado(7)
    )
    assert solucao.comparador is Comparador.MENOR
    assert solucao.limite == RacionalAssinado(-2)
    assert solucao.satisfaz(RacionalAssinado(-3)) is True
    assert solucao.satisfaz(RacionalAssinado(-1)) is False


def test_inequacao_maior_ou_igual_inclui_o_limite():
    # 2x >= 10 -> x >= 5
    solucao = resolver_inequacao_linear(
        RacionalAssinado(2), RacionalAssinado(0), Comparador.MAIOR_OU_IGUAL, RacionalAssinado(10)
    )
    assert solucao.satisfaz(RacionalAssinado(5)) is True
    assert solucao.satisfaz(RacionalAssinado(4)) is False


def test_inequacao_menor_ou_igual_com_coeficiente_negativo():
    # -x <= 3 -> x >= -3 (MENOR_OU_IGUAL inverte para MAIOR_OU_IGUAL)
    solucao = resolver_inequacao_linear(
        RacionalAssinado(-1), RacionalAssinado(0), Comparador.MENOR_OU_IGUAL, RacionalAssinado(3)
    )
    assert solucao.comparador is Comparador.MAIOR_OU_IGUAL
    assert solucao.limite == RacionalAssinado(-3)
    assert solucao.satisfaz(RacionalAssinado(-3)) is True
    assert solucao.satisfaz(RacionalAssinado(-4)) is False


def test_inequacao_rejeita_coeficiente_zero():
    with pytest.raises(ValueError, match="coeficiente de x"):
        resolver_inequacao_linear(
            RacionalAssinado(0), RacionalAssinado(1), Comparador.MAIOR, RacionalAssinado(2)
        )
