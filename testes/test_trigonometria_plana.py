import pytest

from nucleo.medidas_grandezas import Area
from nucleo.trigonometria_plana import (
    Ponto,
    TrianguloGeral,
    Vetor,
    area_dobrada_no_vertice,
    area_triangulo,
    lei_dos_cossenos_confere,
    lei_dos_senos_confere,
    produto_dos_lados_vezes_cosseno,
)
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _p(x: int, y: int) -> Ponto:
    return Ponto(RacionalAssinado(x), RacionalAssinado(y))


def test_triangulo_rejeita_pontos_colineares():
    with pytest.raises(ValueError, match="colineares"):
        TrianguloGeral(_p(0, 0), _p(1, 1), _p(2, 2))


def test_vetor_produto_escalar_e_norma_ao_quadrado():
    v = Vetor.entre(_p(0, 0), _p(3, 4))
    assert v.norma_ao_quadrado() == RacionalAssinado(25)
    perpendicular = Vetor.entre(_p(0, 0), _p(-4, 3))
    assert v.produto_escalar(perpendicular) == RacionalAssinado(0)


def test_angulo_reto_reduz_lei_dos_cossenos_a_pitagoras():
    # C na origem, ângulo reto em C: CA=(3,0), CB=(0,4) -> produto escalar 0
    triangulo = TrianguloGeral(a=_p(3, 0), b=_p(0, 4), c=_p(0, 0))
    assert produto_dos_lados_vezes_cosseno(triangulo, "c") == RacionalAssinado(0)
    # 3-4-5: lado oposto a C (AB) ao quadrado deve ser 3² + 4² = 25
    assert triangulo.lado_ao_quadrado(triangulo.a, triangulo.b) == RacionalAssinado(25)
    assert lei_dos_cossenos_confere(triangulo)


def test_lei_dos_cossenos_confere_em_triangulo_obliquo_nao_retangulo():
    # A=(0,0) B=(4,0) C=(1,3): nenhum ângulo é reto (produto escalar != 0 em nenhum vértice)
    triangulo = TrianguloGeral(a=_p(0, 0), b=_p(4, 0), c=_p(1, 3))
    for vertice in ("a", "b", "c"):
        assert produto_dos_lados_vezes_cosseno(triangulo, vertice) != RacionalAssinado(0)
    assert lei_dos_cossenos_confere(triangulo)


def test_produto_dos_lados_vezes_cosseno_rejeita_vertice_invalido():
    triangulo = TrianguloGeral(a=_p(0, 0), b=_p(4, 0), c=_p(1, 3))
    with pytest.raises(ValueError, match="vértice"):
        produto_dos_lados_vezes_cosseno(triangulo, "d")


def test_area_dobrada_e_a_mesma_nos_tres_vertices_triangulo_retangulo():
    # 3-4-5 com ângulo reto em C: área = (1/2)*3*4 = 6, área dobrada = 12
    triangulo = TrianguloGeral(a=_p(3, 0), b=_p(0, 4), c=_p(0, 0))
    assert area_dobrada_no_vertice(triangulo, "a") == RacionalAssinado(12)
    assert area_dobrada_no_vertice(triangulo, "b") == RacionalAssinado(12)
    assert area_dobrada_no_vertice(triangulo, "c") == RacionalAssinado(12)
    assert lei_dos_senos_confere(triangulo)
    assert area_triangulo(triangulo) == Area(RacionalAssinado(6))


def test_lei_dos_senos_confere_em_triangulo_obliquo():
    # A=(0,0) B=(4,0) C=(1,3): shoelace dá área 6, área dobrada 12
    triangulo = TrianguloGeral(a=_p(0, 0), b=_p(4, 0), c=_p(1, 3))
    assert lei_dos_senos_confere(triangulo)
    assert area_triangulo(triangulo) == Area(RacionalAssinado(6))


def test_area_dobrada_rejeita_vertice_invalido():
    triangulo = TrianguloGeral(a=_p(0, 0), b=_p(4, 0), c=_p(1, 3))
    with pytest.raises(ValueError, match="vértice"):
        area_dobrada_no_vertice(triangulo, "z")
