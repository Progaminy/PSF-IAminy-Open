import pytest

from nucleo.radicais_variaveis import (
    EquacaoComRaizIgualALinear,
    EquacaoComRaizQuadrada,
    resolver_raiz_igual_a_linear,
    resolver_raiz_quadrada,
)
from nucleo.reais_intervalos_naturais import RacionalAssinado


def test_exemplo_classico_raiz_de_x_mais_tres_igual_cinco():
    # √(x+3) = 5  ->  x+3=25  ->  x=22
    equacao = EquacaoComRaizQuadrada(RacionalAssinado(1), RacionalAssinado(3), RacionalAssinado(5))
    solucao = resolver_raiz_quadrada(equacao)
    assert solucao.tem_solucao is True
    assert solucao.x == RacionalAssinado(22)


def test_raiz_com_coeficiente_fracao_resultante():
    # √(2x-1) = 3  ->  2x-1=9  ->  x=5
    equacao = EquacaoComRaizQuadrada(RacionalAssinado(2), RacionalAssinado(-1), RacionalAssinado(3))
    solucao = resolver_raiz_quadrada(equacao)
    assert solucao.x == RacionalAssinado(5)


def test_raiz_com_valor_zero():
    # √(x-4) = 0  ->  x=4
    equacao = EquacaoComRaizQuadrada(RacionalAssinado(1), RacionalAssinado(-4), RacionalAssinado(0))
    solucao = resolver_raiz_quadrada(equacao)
    assert solucao.x == RacionalAssinado(4)


def test_raiz_igual_a_valor_negativo_nao_tem_solucao():
    equacao = EquacaoComRaizQuadrada(RacionalAssinado(1), RacionalAssinado(3), RacionalAssinado(-5))
    solucao = resolver_raiz_quadrada(equacao)
    assert solucao.tem_solucao is False
    assert solucao.x is None
    assert "nunca é negativa" in solucao.motivo


def test_equacao_rejeita_coeficiente_zero():
    with pytest.raises(ValueError, match="coeficiente de x"):
        EquacaoComRaizQuadrada(RacionalAssinado(0), RacionalAssinado(1), RacionalAssinado(2))


def test_raiz_igual_a_linear_com_raiz_estranha_classica():
    # √(2x+3) = x  ->  x²-2x-3=0  ->  x=3 (válida) ou x=-1 (estranha: -1<0)
    equacao = EquacaoComRaizIgualALinear(
        RacionalAssinado(2), RacionalAssinado(3), RacionalAssinado(1), RacionalAssinado(0)
    )
    solucao = resolver_raiz_igual_a_linear(equacao)
    assert solucao.tem_solucao is True
    assert solucao.solucoes == (RacionalAssinado(3),)
    assert solucao.raizes_estranhas_descartadas == (RacionalAssinado(-1),)


def test_raiz_igual_a_linear_ambas_as_raizes_validas():
    # √x = x  ->  x = x²  ->  x²-x=0 -> x=0 ou x=1, ambas com lado direito x >= 0
    equacao = EquacaoComRaizIgualALinear(
        RacionalAssinado(1), RacionalAssinado(0), RacionalAssinado(1), RacionalAssinado(0)
    )
    solucao = resolver_raiz_igual_a_linear(equacao)
    assert solucao.tem_solucao is True
    assert set(solucao.solucoes) == {RacionalAssinado(0), RacionalAssinado(1)}
    assert solucao.raizes_estranhas_descartadas == ()


def test_raiz_igual_a_linear_todas_estranhas_sem_solucao():
    # √(-17x+98) = x-10: as duas raízes reais (x=1 e x=2) dão lado direito
    # negativo (-9 e -8), então as duas são estranhas.
    equacao = EquacaoComRaizIgualALinear(
        RacionalAssinado(-17), RacionalAssinado(98), RacionalAssinado(1), RacionalAssinado(-10)
    )
    solucao = resolver_raiz_igual_a_linear(equacao)
    assert solucao.tem_solucao is False
    assert solucao.solucoes == ()
    assert set(solucao.raizes_estranhas_descartadas) == {RacionalAssinado(1), RacionalAssinado(2)}
    assert solucao.motivo == "todas as raízes candidatas eram estranhas"


def test_raiz_igual_a_linear_discriminante_nao_quadrado_perfeito():
    equacao = EquacaoComRaizIgualALinear(
        RacionalAssinado(3), RacionalAssinado(4), RacionalAssinado(2), RacionalAssinado(-1)
    )
    solucao = resolver_raiz_igual_a_linear(equacao)
    assert solucao.tem_solucao is False
    assert "não é quadrado perfeito" in solucao.motivo


def test_raiz_igual_a_linear_rejeita_coeficiente_a_zero():
    with pytest.raises(ValueError, match="coeficiente do radicando"):
        EquacaoComRaizIgualALinear(
            RacionalAssinado(0), RacionalAssinado(1), RacionalAssinado(1), RacionalAssinado(1)
        )
