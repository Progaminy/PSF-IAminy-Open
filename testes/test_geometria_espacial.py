from nucleo.geometria_espacial import Ponto3D, Vetor3D, pontos_colineares
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _p(x: int, y: int, z: int) -> Ponto3D:
    return Ponto3D(RacionalAssinado(x), RacionalAssinado(y), RacionalAssinado(z))


def test_produto_vetorial_dos_versores_i_j_da_k():
    i = Vetor3D(RacionalAssinado(1), RacionalAssinado(0), RacionalAssinado(0))
    j = Vetor3D(RacionalAssinado(0), RacionalAssinado(1), RacionalAssinado(0))
    k = i.produto_vetorial(j)
    assert k == Vetor3D(RacionalAssinado(0), RacionalAssinado(0), RacionalAssinado(1))


def test_produto_vetorial_e_perpendicular_aos_dois_vetores_originais():
    v1 = Vetor3D.entre(_p(0, 0, 0), _p(1, 2, 3))
    v2 = Vetor3D.entre(_p(0, 0, 0), _p(3, 1, 2))
    cruzado = v1.produto_vetorial(v2)
    assert cruzado.produto_escalar(v1) == RacionalAssinado(0)
    assert cruzado.produto_escalar(v2) == RacionalAssinado(0)


def test_produto_vetorial_de_vetores_paralelos_e_nulo():
    v1 = Vetor3D(RacionalAssinado(2), RacionalAssinado(4), RacionalAssinado(6))
    v2 = Vetor3D(RacionalAssinado(1), RacionalAssinado(2), RacionalAssinado(3))
    cruzado = v1.produto_vetorial(v2)
    assert cruzado == Vetor3D(RacionalAssinado(0), RacionalAssinado(0), RacionalAssinado(0))


def test_norma_ao_quadrado_exata():
    v = Vetor3D.entre(_p(0, 0, 0), _p(1, 2, 2))
    assert v.norma_ao_quadrado() == RacionalAssinado(9)  # 1²+2²+2²


def test_pontos_colineares_na_diagonal():
    assert pontos_colineares(_p(0, 0, 0), _p(1, 1, 1), _p(2, 2, 2)) is True


def test_pontos_nao_colineares_no_plano_xy():
    assert pontos_colineares(_p(0, 0, 0), _p(1, 0, 0), _p(0, 1, 0)) is False


def test_produto_escalar_de_vetores_perpendiculares_e_zero():
    v1 = Vetor3D(RacionalAssinado(1), RacionalAssinado(0), RacionalAssinado(0))
    v2 = Vetor3D(RacionalAssinado(0), RacionalAssinado(1), RacionalAssinado(0))
    assert v1.produto_escalar(v2) == RacionalAssinado(0)
