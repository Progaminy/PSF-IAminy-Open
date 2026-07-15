from nucleo.desvio_padrao_exato import desvio_padrao_exato_ou_none
from nucleo.reais_intervalos_naturais import RacionalAssinado


def test_desvio_padrao_exato_exemplo_classico():
    # dados 2,4,4,4,5,5,7,9: média 5, variância populacional 4, desvio 2
    dados = [2, 4, 4, 4, 5, 5, 7, 9]
    assert desvio_padrao_exato_ou_none(dados) == RacionalAssinado(2)


def test_desvio_padrao_exato_dados_constantes_e_zero():
    assert desvio_padrao_exato_ou_none([7, 7, 7]) == RacionalAssinado(0)


def test_desvio_padrao_none_quando_variancia_nao_e_quadrado_perfeito():
    assert desvio_padrao_exato_ou_none([1, 2, 3]) is None
