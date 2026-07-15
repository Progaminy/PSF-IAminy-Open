import pytest

from nucleo.dominio_logaritmo import confirmar_fronteira_de_dominio, dominio_de_logaritmo_linear
from nucleo.inequacoes import Comparador
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _r(n: int) -> RacionalAssinado:
    return RacionalAssinado(n)


def test_dominio_do_exemplo_legado_ln_x_menos_quatro():
    # ln(x-4): domínio x > 4, exatamente a resposta legada.
    solucao = dominio_de_logaritmo_linear(_r(1), _r(-4))
    assert solucao.comparador is Comparador.MAIOR
    assert solucao.limite == _r(4)


def test_fronteira_confirmada_com_logaritmo_exato_de_verdade():
    assert confirmar_fronteira_de_dominio(_r(1), _r(-4), _r(2), x_dentro=_r(5), x_fora=_r(3)) is True


def test_dominio_com_coeficiente_positivo_diferente():
    # log(2x+6): domínio x > -3.
    solucao = dominio_de_logaritmo_linear(_r(2), _r(6))
    assert solucao.comparador is Comparador.MAIOR
    assert solucao.limite == _r(-3)
    assert confirmar_fronteira_de_dominio(_r(2), _r(6), _r(2), x_dentro=_r(-1), x_fora=_r(-4)) is True


def test_dominio_com_coeficiente_negativo_inverte_comparador():
    # log(-x+5): domínio x < 5 (coeficiente negativo inverte o comparador).
    solucao = dominio_de_logaritmo_linear(_r(-1), _r(5))
    assert solucao.comparador is Comparador.MENOR
    assert solucao.limite == _r(5)
    assert confirmar_fronteira_de_dominio(_r(-1), _r(5), _r(3), x_dentro=_r(4), x_fora=_r(6)) is True


def test_rejeita_coeficiente_de_x_zero():
    with pytest.raises(ValueError, match="não pode ser zero"):
        dominio_de_logaritmo_linear(_r(0), _r(1))
