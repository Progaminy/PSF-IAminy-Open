"""Marcador 1073 -- subtração natural truncada (predecessor + subtração)."""
from nucleo.aritmetica import PRED, SUB, SOMA
from nucleo.traducao import de_int, para_int


def test_predecessor_de_zero_e_zero():
    assert para_int(PRED(de_int(0))) == 0


def test_predecessor_desfaz_um_sucessor():
    for k in range(1, 10):
        assert para_int(PRED(de_int(k))) == k - 1


def test_subtracao_normal():
    assert para_int(SUB(de_int(7))(de_int(3))) == 4
    assert para_int(SUB(de_int(10))(de_int(10))) == 0


def test_subtracao_trunca_em_zero_quando_n_maior_que_m():
    assert para_int(SUB(de_int(2))(de_int(5))) == 0


def test_subtracao_desfaz_adicao_quando_nao_trunca():
    # (m - n) + n == m, sempre que n <= m -- prova real, não só "parece certo".
    for m in range(10):
        for n in range(m + 1):
            resultado = SOMA(SUB(de_int(m))(de_int(n)))(de_int(n))
            assert para_int(resultado) == m
