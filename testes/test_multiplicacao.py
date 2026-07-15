"""Marcador 1075 -- multiplicação (adição repetida)."""
from nucleo.aritmetica import MULT, SOMA
from nucleo.traducao import de_int, para_int


def test_multiplicar_por_zero_da_zero():
    for k in range(10):
        assert para_int(MULT(de_int(k))(de_int(0))) == 0


def test_multiplicacao_simples():
    assert para_int(MULT(de_int(3))(de_int(4))) == 12
    assert para_int(MULT(de_int(7))(de_int(6))) == 42


def test_multiplicacao_e_comutativa():
    for a in range(6):
        for b in range(6):
            assert para_int(MULT(de_int(a))(de_int(b))) == para_int(MULT(de_int(b))(de_int(a)))


def test_multiplicacao_e_associativa():
    a, b, c = de_int(2), de_int(3), de_int(4)
    esquerda = MULT(MULT(a)(b))(c)
    direita = MULT(a)(MULT(b)(c))
    assert para_int(esquerda) == para_int(direita) == 24


def test_multiplicacao_e_de_fato_soma_repetida():
    # 3 x 4 tem que bater com 3+3+3+3, construído por soma independente,
    # não só aceito por sair da fórmula de MULT.
    tres = de_int(3)
    soma_repetida = SOMA(SOMA(SOMA(tres)(tres))(tres))(tres)
    assert para_int(MULT(de_int(3))(de_int(4))) == para_int(soma_repetida)
