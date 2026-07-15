from nucleo.distancia_intersecao_retas import (
    distancia_ao_quadrado_ponto_reta,
    distancia_ponto_reta_exata_ou_none,
    intersecao_de_retas,
)
from nucleo.geometria_analitica import Reta
from nucleo.reais_intervalos_naturais import RacionalAssinado
from nucleo.trigonometria_plana import Ponto


def _p(x: int, y: int) -> Ponto:
    return Ponto(RacionalAssinado(x), RacionalAssinado(y))


def test_distancia_ponto_reta_quadrado_perfeito():
    eixo_x = Reta(_p(0, 0), _p(1, 0))
    assert distancia_ao_quadrado_ponto_reta(_p(0, 3), eixo_x) == RacionalAssinado(9)
    assert distancia_ponto_reta_exata_ou_none(_p(0, 3), eixo_x) == RacionalAssinado(3)


def test_distancia_ponto_na_propria_reta_e_zero():
    reta = Reta(_p(0, 0), _p(2, 4))
    assert distancia_ao_quadrado_ponto_reta(_p(1, 2), reta) == RacionalAssinado(0)
    assert distancia_ponto_reta_exata_ou_none(_p(1, 2), reta) == RacionalAssinado(0)


def test_distancia_ponto_reta_none_quando_nao_e_quadrado_perfeito():
    diagonal = Reta(_p(0, 0), _p(1, 1))
    assert distancia_ao_quadrado_ponto_reta(_p(0, 1), diagonal) == RacionalAssinado(1, 2)
    assert distancia_ponto_reta_exata_ou_none(_p(0, 1), diagonal) is None


def test_intersecao_de_retas_nao_paralelas():
    r1 = Reta(_p(0, 0), _p(1, 1))  # y = x
    r2 = Reta(_p(0, 2), _p(2, 0))  # y = -x + 2
    assert intersecao_de_retas(r1, r2) == _p(1, 1)


def test_intersecao_de_retas_paralelas_e_none():
    r1 = Reta(_p(0, 0), _p(2, 4))
    r2 = Reta(_p(1, 1), _p(3, 5))  # mesma direção (2, 4)
    assert intersecao_de_retas(r1, r2) is None


def test_intersecao_com_coordenadas_fracionarias():
    r1 = Reta(_p(0, 0), _p(2, 1))  # y = x/2
    r2 = Reta(_p(0, 3), _p(3, 0))  # y = -x + 3
    ponto = intersecao_de_retas(r1, r2)
    assert ponto == Ponto(RacionalAssinado(2), RacionalAssinado(1))
