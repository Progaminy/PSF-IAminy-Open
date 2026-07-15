import pytest

from nucleo.lei_geradora_real import (
    LeiGeradoraIntervalos,
    lei_geradora_raiz_quadrada,
    modulo_convergencia,
)
from nucleo.reais_intervalos_naturais import RacionalAssinado


def test_lei_geradora_raiz_quadrada_produz_prefixo_encaixado_contendo_a_raiz():
    lei = lei_geradora_raiz_quadrada(2)
    aproximacao = lei.prefixo(6)
    certificado = aproximacao.certificado_finito()
    assert certificado["encaixados"] is True

    ultimo = aproximacao.intervalos[-1]
    assert ultimo.inferior.multiplicar(ultimo.inferior).menor_ou_igual(RacionalAssinado(2))
    assert RacionalAssinado(2).menor_ou_igual(ultimo.superior.multiplicar(ultimo.superior))


def test_lei_geradora_raiz_quadrada_de_um_e_ponto_fixo_imediato():
    # alvo=1: chute inicial (max(1,1)=1) já é a própria raiz, então Newton
    # fica parado em 1 desde o passo 0 — o único caso em que a igualdade
    # exata é garantida em racionais (fora isso, Newton só se aproxima).
    lei = lei_geradora_raiz_quadrada(1)
    for indice in (0, 1, 3):
        intervalo = lei.passo(indice)
        assert intervalo.inferior == RacionalAssinado(1)
        assert intervalo.superior == RacionalAssinado(1)


def test_modulo_convergencia_encontra_passo_finito_para_epsilon_dado():
    lei = lei_geradora_raiz_quadrada(2)
    epsilon = RacionalAssinado(1, 1000)

    passo_suficiente = modulo_convergencia(lei, epsilon)

    assert lei.passo(passo_suficiente).largura().menor_ou_igual(epsilon)
    if passo_suficiente > 0:
        assert not lei.passo(passo_suficiente - 1).largura().menor_ou_igual(epsilon)


def test_modulo_convergencia_rejeita_epsilon_nao_positivo():
    lei = lei_geradora_raiz_quadrada(2)
    with pytest.raises(ValueError, match="positivo"):
        modulo_convergencia(lei, RacionalAssinado(0))


def test_modulo_convergencia_declara_falha_em_vez_de_fingir_sucesso():
    intervalo_fixo = lei_geradora_raiz_quadrada(2).passo(0)
    lei_estacionaria = LeiGeradoraIntervalos(
        nome="estacionaria_sem_convergencia",
        passo=lambda indice: intervalo_fixo,
    )
    with pytest.raises(ValueError, match="não atingiu"):
        modulo_convergencia(lei_estacionaria, RacionalAssinado(1, 1000), limite_passos=5)
