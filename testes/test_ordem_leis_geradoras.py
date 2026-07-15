import pytest

from nucleo.lei_geradora_real import lei_geradora_raiz_quadrada
from nucleo.equivalencia_leis_geradoras import lei_geradora_raiz_quadrada_bissecao
from nucleo.ordem_leis_geradoras import RelacaoOrdem, comparar_leis_ate_epsilon, decidir_ordem
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _r(n: int, d: int = 1) -> RacionalAssinado:
    return RacionalAssinado(n, d)


def test_raiz_de_dois_e_menor_que_raiz_de_tres():
    resultado = comparar_leis_ate_epsilon(
        lei_geradora_raiz_quadrada(2), lei_geradora_raiz_quadrada(3), _r(1, 10)
    )
    assert resultado is RelacaoOrdem.MENOR


def test_raiz_de_tres_e_maior_que_raiz_de_dois():
    resultado = comparar_leis_ate_epsilon(
        lei_geradora_raiz_quadrada(3), lei_geradora_raiz_quadrada(2), _r(1, 10)
    )
    assert resultado is RelacaoOrdem.MAIOR


def test_lei_comparada_consigo_mesma_fica_indeterminada():
    lei = lei_geradora_raiz_quadrada(2)
    resultado = comparar_leis_ate_epsilon(lei, lei, _r(1, 100))
    assert resultado is RelacaoOrdem.INDETERMINADA


def test_decidir_ordem_encontra_a_diferenca_entre_valores_distintos():
    resultado = decidir_ordem(lei_geradora_raiz_quadrada(2), lei_geradora_raiz_quadrada(3))
    assert resultado is RelacaoOrdem.MENOR


def test_decidir_ordem_nao_finge_decisao_para_leis_do_mesmo_valor():
    # Newton e bisseção convergem para o mesmo valor (raiz de 2, ETAPA
    # 1061) - a ordem nunca deveria ser decidida entre elas.
    newton = lei_geradora_raiz_quadrada(2)
    bissecao = lei_geradora_raiz_quadrada_bissecao(2)
    resultado = decidir_ordem(newton, bissecao, limite_refinamentos=5)
    assert resultado is RelacaoOrdem.INDETERMINADA


def test_rejeita_epsilon_nao_positivo():
    lei = lei_geradora_raiz_quadrada(2)
    with pytest.raises(ValueError, match="positivo"):
        comparar_leis_ate_epsilon(lei, lei, _r(0))
