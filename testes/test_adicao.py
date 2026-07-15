"""Etapa 2 -- adição (contar é aplicar sucessor repetidamente)."""
from nucleo.aritmetica import SOMA
from nucleo.traducao import de_int, para_int


def test_somar_zero_nao_muda_nada():
    for k in range(10):
        assert para_int(SOMA(de_int(k))(de_int(0))) == k


def test_soma_conta_certo():
    assert para_int(SOMA(de_int(2))(de_int(3))) == 5
    assert para_int(SOMA(de_int(7))(de_int(8))) == 15


def test_soma_e_comutativa():
    for a in range(6):
        for b in range(6):
            assert para_int(SOMA(de_int(a))(de_int(b))) == para_int(SOMA(de_int(b))(de_int(a)))


def test_soma_e_associativa():
    a, b, c = de_int(2), de_int(3), de_int(4)
    esquerda = SOMA(SOMA(a)(b))(c)
    direita = SOMA(a)(SOMA(b)(c))
    assert para_int(esquerda) == para_int(direita) == 9


def test_somar_sucessivamente_e_contar():
    # 3+3+3+3 (quatro vezes) -- a mesma soma repetida que a Etapa 3
    # (multiplicação) vai formalizar como "3 vezes 4".
    tres = de_int(3)
    total = SOMA(SOMA(SOMA(tres)(tres))(tres))(tres)
    assert para_int(total) == 12
