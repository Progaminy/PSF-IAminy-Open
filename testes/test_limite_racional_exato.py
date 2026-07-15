import pytest

from nucleo.limite_racional_exato import (
    eh_indeterminacao_zero_sobre_zero,
    limite_racional_em_ponto,
)
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _r(n: int) -> RacionalAssinado:
    return RacionalAssinado(n)


def _p(*coeficientes: int) -> tuple[RacionalAssinado, ...]:
    return tuple(_r(c) for c in coeficientes)


def test_limite_com_indeterminacao_zero_sobre_zero_classico():
    # lim(x->2) (x²-4)/(x-2) = lim (x-2)(x+2)/(x-2) = 4
    numerador = _p(1, 0, -4)
    denominador = _p(1, -2)
    assert eh_indeterminacao_zero_sobre_zero(numerador, denominador, _r(2)) is True
    assert limite_racional_em_ponto(numerador, denominador, _r(2)) == _r(4)


def test_limite_com_indeterminacao_outro_exemplo_classico():
    # lim(x->1) (x²-1)/(x-1) = lim (x+1) = 2
    numerador = _p(1, 0, -1)
    denominador = _p(1, -1)
    assert eh_indeterminacao_zero_sobre_zero(numerador, denominador, _r(1)) is True
    assert limite_racional_em_ponto(numerador, denominador, _r(1)) == _r(2)


def test_limite_sem_indeterminacao_avaliacao_direta():
    # lim(x->3) (x+5)/(x-1) = 8/2 = 4, sem fatoração nenhuma
    numerador = _p(1, 5)
    denominador = _p(1, -1)
    assert eh_indeterminacao_zero_sobre_zero(numerador, denominador, _r(3)) is False
    assert limite_racional_em_ponto(numerador, denominador, _r(3)) == _r(4)


def test_limite_diverge_quando_denominador_zera_sem_zerar_numerador():
    # lim(x->3) 1/(x-3): denominador zera, numerador não - sem limite finito
    numerador = _p(1)
    denominador = _p(1, -3)
    assert eh_indeterminacao_zero_sobre_zero(numerador, denominador, _r(3)) is False
    assert limite_racional_em_ponto(numerador, denominador, _r(3)) is None


def test_rejeita_denominador_polinomio_nulo():
    with pytest.raises(ValueError, match="não pode ser o polinômio nulo"):
        limite_racional_em_ponto(_p(1), _p(0), _r(1))


def test_rejeita_polinomio_vazio():
    with pytest.raises(ValueError, match="ao menos um coeficiente"):
        limite_racional_em_ponto((), _p(1), _r(1))
