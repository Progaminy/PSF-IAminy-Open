import pytest

from nucleo.probabilidade_condicionada_bayes import bayes_como_par
from nucleo.medida_probabilidade_finita import condicional_como_par


UNIVERSO = (1, 2, 3, 4, 5, 6)
PARES = (2, 4, 6)
MAIOR_QUE_TRES = (4, 5, 6)


def test_bayes_confere_com_probabilidade_condicional_direta():
    # A = pares, B = maior que 3; P(A|B) direto = |{4,6}|/|{4,5,6}| = 2/3
    resultado = bayes_como_par(PARES, MAIOR_QUE_TRES, UNIVERSO)
    direta = condicional_como_par(PARES, MAIOR_QUE_TRES, UNIVERSO)
    assert resultado[0] * direta[1] == resultado[1] * direta[0]
    assert resultado[0] * 3 == resultado[1] * 2  # 2/3 em forma reduzida ou não


def test_bayes_com_pesos_nao_uniformes():
    pesos = {1: 1, 2: 3, 3: 1, 4: 2, 5: 1, 6: 4}
    resultado = bayes_como_par(PARES, MAIOR_QUE_TRES, UNIVERSO, pesos)
    direta = condicional_como_par(PARES, MAIOR_QUE_TRES, UNIVERSO, pesos)
    assert resultado[0] * direta[1] == resultado[1] * direta[0]


def test_bayes_rejeita_evento_b_impossivel():
    with pytest.raises(ValueError, match="P\\(B\\) não pode ser zero"):
        bayes_como_par(PARES, (), UNIVERSO)


def test_bayes_rejeita_evento_a_impossivel():
    with pytest.raises(ValueError, match="P\\(A\\) não pode ser zero"):
        bayes_como_par((), MAIOR_QUE_TRES, UNIVERSO)


def test_bayes_eventos_independentes_da_mesma_probabilidade_marginal():
    # A = {1,2,3}, B = {2,4,6}: P(A)=1/2, P(B)=1/2, A∩B={2}
    a = (1, 2, 3)
    b = (2, 4, 6)
    resultado = bayes_como_par(a, b, UNIVERSO)
    direta = condicional_como_par(a, b, UNIVERSO)
    assert resultado[0] * direta[1] == resultado[1] * direta[0]
