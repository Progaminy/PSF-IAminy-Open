import pytest

from nucleo.geometria_analitica import (
    Circunferencia,
    Reta,
    circunferencia_por_centro_e_ponto,
    coeficiente_angular,
    distancia_exata_ou_none,
    pertence_a_circunferencia,
    pertence_a_reta,
    ponto_medio,
    retas_paralelas,
    retas_perpendiculares,
)
from nucleo.reais_intervalos_naturais import RacionalAssinado
from nucleo.trigonometria_plana import Ponto


def _p(x: int, y: int) -> Ponto:
    return Ponto(RacionalAssinado(x), RacionalAssinado(y))


def test_reta_rejeita_dois_pontos_iguais():
    with pytest.raises(ValueError, match="dois pontos distintos"):
        Reta(_p(1, 1), _p(1, 1))


def test_coeficiente_angular_exato():
    reta = Reta(_p(0, 0), _p(2, 4))
    assert coeficiente_angular(reta) == RacionalAssinado(2)


def test_coeficiente_angular_reta_vertical_rejeitado():
    reta = Reta(_p(3, 0), _p(3, 5))
    with pytest.raises(ValueError, match="reta vertical"):
        coeficiente_angular(reta)


def test_pertence_a_reta():
    reta = Reta(_p(0, 0), _p(2, 4))  # y = 2x
    assert pertence_a_reta(_p(1, 2), reta) is True
    assert pertence_a_reta(_p(1, 3), reta) is False


def test_retas_paralelas_por_mesma_direcao():
    r1 = Reta(_p(0, 0), _p(2, 4))
    r2 = Reta(_p(1, 1), _p(3, 5))  # mesma direção (2,4)
    assert retas_paralelas(r1, r2) is True
    r3 = Reta(_p(0, 0), _p(1, 1))  # direção diferente
    assert retas_paralelas(r1, r3) is False


def test_retas_perpendiculares_por_produto_escalar_nulo():
    r1 = Reta(_p(0, 0), _p(2, 4))  # direção (2,4)
    r2 = Reta(_p(0, 0), _p(4, -2))  # direção (4,-2): 2*4+4*-2=0
    assert retas_perpendiculares(r1, r2) is True
    assert retas_perpendiculares(r1, r1) is False


def test_ponto_medio():
    medio = ponto_medio(_p(0, 0), _p(4, 6))
    assert medio == _p(2, 3)


def test_ponto_medio_com_coordenadas_fracionarias():
    medio = ponto_medio(_p(1, 1), _p(2, 2))
    assert medio == Ponto(RacionalAssinado(3, 2), RacionalAssinado(3, 2))


def test_distancia_exata_quando_quadrado_perfeito():
    # triângulo 3-4-5
    assert distancia_exata_ou_none(_p(0, 0), _p(3, 4)) == RacionalAssinado(5)


def test_distancia_exata_none_quando_nao_e_quadrado_perfeito():
    assert distancia_exata_ou_none(_p(0, 0), _p(1, 1)) is None


def test_circunferencia_por_centro_e_ponto_e_pertencimento():
    circ = circunferencia_por_centro_e_ponto(_p(0, 0), _p(3, 4))
    assert circ.raio_ao_quadrado == RacionalAssinado(25)
    assert pertence_a_circunferencia(_p(0, 5), circ) is True
    assert pertence_a_circunferencia(_p(5, 0), circ) is True
    assert pertence_a_circunferencia(_p(1, 1), circ) is False


def test_circunferencia_rejeita_raio_nao_positivo():
    with pytest.raises(ValueError, match="raio ao quadrado"):
        Circunferencia(_p(0, 0), RacionalAssinado(0))
