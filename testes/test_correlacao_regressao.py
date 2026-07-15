import pytest

from nucleo.correlacao_regressao import coeficiente_determinacao, regressao_linear
from nucleo.reais_intervalos_naturais import RacionalAssinado


def test_regressao_linear_dados_perfeitamente_lineares():
    dados = [(1, 2), (2, 4), (3, 6)]  # y = 2x exato
    reta = regressao_linear(dados)
    assert reta.inclinacao == RacionalAssinado(2)
    assert reta.intercepto == RacionalAssinado(0)
    assert coeficiente_determinacao(reta, dados) == RacionalAssinado(1)


def test_regressao_linear_dados_com_ruido():
    dados = [(1, 2), (2, 3), (3, 5)]
    reta = regressao_linear(dados)
    assert reta.inclinacao == RacionalAssinado(3, 2)
    assert reta.intercepto == RacionalAssinado(1, 3)
    assert coeficiente_determinacao(reta, dados) == RacionalAssinado(27, 28)


def test_prever_usa_a_reta_calculada():
    dados = [(1, 2), (2, 4), (3, 6)]
    reta = regressao_linear(dados)
    assert reta.prever(RacionalAssinado(10)) == RacionalAssinado(20)


def test_regressao_linear_exige_pelo_menos_dois_pontos():
    with pytest.raises(ValueError, match="pelo menos dois pontos"):
        regressao_linear([(1, 2)])


def test_regressao_linear_rejeita_x_todos_iguais():
    with pytest.raises(ValueError, match="todos os x são iguais"):
        regressao_linear([(5, 1), (5, 2), (5, 3)])


def test_coeficiente_determinacao_rejeita_y_todos_iguais():
    dados = [(1, 7), (2, 7), (3, 7)]
    reta = regressao_linear(dados)
    with pytest.raises(ValueError, match="todos os y são iguais"):
        coeficiente_determinacao(reta, dados)
