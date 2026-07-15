import pytest

from nucleo.divisao_polinomios import (
    avaliar_polinomio,
    dividir_por_x_menos_a,
    eh_raiz,
    teorema_do_resto,
)
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _r(n: int) -> RacionalAssinado:
    return RacionalAssinado(n)


def _p(*coeficientes: int) -> tuple[RacionalAssinado, ...]:
    return tuple(_r(c) for c in coeficientes)


# P(x) = x³ - 6x² + 11x - 6 = (x-1)(x-2)(x-3)
POLINOMIO_CLASSICO = _p(1, -6, 11, -6)


def test_avaliar_polinomio_horner():
    assert avaliar_polinomio(POLINOMIO_CLASSICO, _r(1)) == _r(0)
    assert avaliar_polinomio(POLINOMIO_CLASSICO, _r(5)) == _r(24)
    assert avaliar_polinomio(POLINOMIO_CLASSICO, _r(0)) == _r(-6)


def test_dividir_por_x_menos_uma_raiz_da_resto_zero():
    quociente, resto = dividir_por_x_menos_a(POLINOMIO_CLASSICO, _r(1))
    assert resto == _r(0)
    assert quociente == _p(1, -5, 6)  # x² - 5x + 6 = (x-2)(x-3)


def test_dividir_por_x_menos_a_que_nao_e_raiz():
    quociente, resto = dividir_por_x_menos_a(POLINOMIO_CLASSICO, _r(5))
    assert resto == _r(24)
    assert quociente == _p(1, -1, 6)


def test_teorema_do_resto_bate_com_avaliacao_direta():
    for valor in (0, 1, 2, 3, 5, -2):
        assert teorema_do_resto(POLINOMIO_CLASSICO, _r(valor)) == avaliar_polinomio(POLINOMIO_CLASSICO, _r(valor))


def test_eh_raiz_das_tres_raizes_conhecidas():
    assert eh_raiz(POLINOMIO_CLASSICO, _r(1)) is True
    assert eh_raiz(POLINOMIO_CLASSICO, _r(2)) is True
    assert eh_raiz(POLINOMIO_CLASSICO, _r(3)) is True
    assert eh_raiz(POLINOMIO_CLASSICO, _r(4)) is False


def test_dividir_rejeita_polinomio_vazio():
    with pytest.raises(ValueError, match="ao menos um coeficiente"):
        dividir_por_x_menos_a((), _r(1))
