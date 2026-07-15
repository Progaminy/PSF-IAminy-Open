from nucleo.equivalencia_leis_geradoras import sao_consistentes_ate_epsilon
from nucleo.lei_geradora_real import lei_geradora_raiz_quadrada
from nucleo.operacoes_leis_geradoras import (
    lei_geradora_constante,
    lei_geradora_produto,
    lei_geradora_soma,
)
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _r(n: int, d: int = 1) -> RacionalAssinado:
    return RacionalAssinado(n, d)


def test_lei_constante_tem_largura_zero_em_qualquer_passo():
    lei = lei_geradora_constante(_r(7))
    for indice in (0, 1, 5):
        intervalo = lei.passo(indice)
        assert intervalo.inferior == _r(7)
        assert intervalo.superior == _r(7)
        assert intervalo.largura() == _r(0)


def test_soma_de_raizes_de_quadrados_perfeitos_e_consistente_com_a_soma_exata():
    # sqrt(4) + sqrt(9) = 2 + 3 = 5
    soma = lei_geradora_soma(lei_geradora_raiz_quadrada(4), lei_geradora_raiz_quadrada(9))
    esperado = lei_geradora_constante(_r(5))
    assert sao_consistentes_ate_epsilon(soma, esperado, _r(1, 100)) is True


def test_soma_nao_e_consistente_com_valor_errado():
    soma = lei_geradora_soma(lei_geradora_raiz_quadrada(4), lei_geradora_raiz_quadrada(9))
    valor_errado = lei_geradora_constante(_r(6))
    assert sao_consistentes_ate_epsilon(soma, valor_errado, _r(1, 100)) is False


def test_produto_de_raiz_de_dois_consigo_mesma_e_consistente_com_dois():
    # sqrt(2) * sqrt(2) = 2
    produto = lei_geradora_produto(lei_geradora_raiz_quadrada(2), lei_geradora_raiz_quadrada(2))
    esperado = lei_geradora_constante(_r(2))
    assert sao_consistentes_ate_epsilon(produto, esperado, _r(1, 100)) is True


def test_produto_de_raizes_de_quadrados_perfeitos_e_consistente_com_raiz_do_produto():
    # sqrt(4) * sqrt(9) = 6 = sqrt(36)
    produto = lei_geradora_produto(lei_geradora_raiz_quadrada(4), lei_geradora_raiz_quadrada(9))
    referencia = lei_geradora_raiz_quadrada(36)
    assert sao_consistentes_ate_epsilon(produto, referencia, _r(1, 100)) is True


def test_soma_e_produto_produzem_prefixo_encaixado():
    soma = lei_geradora_soma(lei_geradora_raiz_quadrada(2), lei_geradora_raiz_quadrada(3))
    produto = lei_geradora_produto(lei_geradora_raiz_quadrada(2), lei_geradora_raiz_quadrada(3))
    assert soma.prefixo(6).certificado_finito()["encaixados"] is True
    assert produto.prefixo(6).certificado_finito()["encaixados"] is True
