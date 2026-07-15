import pytest

from nucleo.completude_leis_geradoras import lei_geradora_limite_de_sequencia_cauchy
from nucleo.equivalencia_leis_geradoras import sao_consistentes_ate_epsilon
from nucleo.lei_geradora_real import lei_geradora_raiz_quadrada, modulo_convergencia
from nucleo.operacoes_leis_geradoras import lei_geradora_constante
from nucleo.reais_intervalos_naturais import RacionalAssinado

_METADE = RacionalAssinado(1, 2)
_RAIZ_DE_DOIS = lei_geradora_raiz_quadrada(2)


def _r(n: int, d: int = 1) -> RacionalAssinado:
    return RacionalAssinado(n, d)


def _termo_ponto_medio(indice: int):
    # Sequência de racionais (empacotados como leis constantes): o ponto
    # médio do intervalo de Newton para raiz de 2 em cada passo — uma
    # sequência de Cauchy genuína, convergindo para √2, construída sem
    # nenhuma referência direta a "raiz quadrada" no valor em si.
    intervalo = _RAIZ_DE_DOIS.passo(indice)
    meio = intervalo.inferior.somar(intervalo.superior).multiplicar(_METADE)
    return lei_geradora_constante(meio)


def _modulo_cauchy_ponto_medio(epsilon: RacionalAssinado) -> int:
    # A partir do passo N onde a largura do intervalo de Newton já é
    # <= epsilon, todo ponto médio posterior fica dentro desse intervalo
    # (encaixado), logo a distância entre quaisquer dois termos a partir
    # de N é <= epsilon.
    return modulo_convergencia(_RAIZ_DE_DOIS, epsilon)


def test_limite_da_sequencia_de_pontos_medios_e_consistente_com_raiz_de_dois():
    limite = lei_geradora_limite_de_sequencia_cauchy(_termo_ponto_medio, _modulo_cauchy_ponto_medio)
    assert sao_consistentes_ate_epsilon(limite, _RAIZ_DE_DOIS, _r(1, 100)) is True


def test_limite_da_sequencia_constante_e_consistente_com_ela_mesma():
    # Sequência trivial: todo termo já é a própria lei de raiz de 2.
    def termo(indice: int):
        return _RAIZ_DE_DOIS

    def modulo_cauchy(epsilon: RacionalAssinado) -> int:
        return 0

    limite = lei_geradora_limite_de_sequencia_cauchy(termo, modulo_cauchy)
    assert sao_consistentes_ate_epsilon(limite, _RAIZ_DE_DOIS, _r(1, 1000)) is True


def test_lei_do_limite_produz_prefixo_encaixado_e_largura_decrescente():
    limite = lei_geradora_limite_de_sequencia_cauchy(_termo_ponto_medio, _modulo_cauchy_ponto_medio)
    aproximacao = limite.prefixo(6)
    certificado = aproximacao.certificado_finito()
    assert certificado["encaixados"] is True
    assert certificado["largura_final"].menor_ou_igual(_r(1))


def test_rejeita_passo_negativo():
    limite = lei_geradora_limite_de_sequencia_cauchy(_termo_ponto_medio, _modulo_cauchy_ponto_medio)
    with pytest.raises(ValueError, match="não negativo"):
        limite.passo(-1)
