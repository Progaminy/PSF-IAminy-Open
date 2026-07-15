import pytest

from nucleo.equivalencia_leis_geradoras import (
    intervalos_se_sobrepoem,
    lei_geradora_raiz_quadrada_bissecao,
    sao_consistentes_ate_epsilon,
)
from nucleo.lei_geradora_real import lei_geradora_raiz_quadrada
from nucleo.reais_intervalos_naturais import IntervaloRacional, RacionalAssinado


def _r(n: int, d: int = 1) -> RacionalAssinado:
    return RacionalAssinado(n, d)


def test_bissecao_produz_intervalo_encaixado_contendo_a_raiz():
    lei = lei_geradora_raiz_quadrada_bissecao(2)
    aproximacao = lei.prefixo(8)
    assert aproximacao.certificado_finito()["encaixados"] is True

    ultimo = aproximacao.intervalos[-1]
    assert ultimo.inferior.multiplicar(ultimo.inferior).menor_ou_igual(_r(2))
    assert _r(2).menor_ou_igual(ultimo.superior.multiplicar(ultimo.superior))


def test_intervalos_se_sobrepoem_caso_positivo_e_negativo():
    a = IntervaloRacional(_r(1), _r(2))
    b = IntervaloRacional(_r(3, 2), _r(3))
    c = IntervaloRacional(_r(5), _r(6))
    assert intervalos_se_sobrepoem(a, b) is True
    assert intervalos_se_sobrepoem(a, c) is False


def test_lei_e_consistente_consigo_mesma():
    lei = lei_geradora_raiz_quadrada(2)
    assert sao_consistentes_ate_epsilon(lei, lei, _r(1, 100)) is True


def test_newton_e_bissecao_convergem_para_o_mesmo_valor():
    # Dois algoritmos estruturalmente diferentes (Newton quadrático,
    # bisseção linear) convergindo para a mesma raiz de 2.
    newton = lei_geradora_raiz_quadrada(2)
    bissecao = lei_geradora_raiz_quadrada_bissecao(2)
    assert sao_consistentes_ate_epsilon(newton, bissecao, _r(1, 100)) is True


def test_leis_de_alvos_diferentes_sao_definitivamente_nao_equivalentes():
    # sqrt(2) ~= 1.414 e sqrt(3) ~= 1.732: a um epsilon pequeno o
    # suficiente, os intervalos refinados não podem se sobrepor.
    raiz_de_dois = lei_geradora_raiz_quadrada(2)
    raiz_de_tres = lei_geradora_raiz_quadrada(3)
    assert sao_consistentes_ate_epsilon(raiz_de_dois, raiz_de_tres, _r(1, 10)) is False


def test_rejeita_epsilon_nao_positivo():
    lei = lei_geradora_raiz_quadrada(2)
    with pytest.raises(ValueError, match="positivo"):
        sao_consistentes_ate_epsilon(lei, lei, _r(0))
