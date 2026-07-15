"""Marcador 1076 -- potenciação (multiplicação repetida)."""
from nucleo.aritmetica import MULT, POT
from nucleo.traducao import de_int, para_int


def test_expoente_zero_da_elemento_neutro_um():
    for k in range(1, 10):
        assert para_int(POT(de_int(k))(de_int(0))) == 1


def test_expoente_um_devolve_a_propria_base():
    for k in range(10):
        assert para_int(POT(de_int(k))(de_int(1))) == k


def test_potenciacao_simples():
    assert para_int(POT(de_int(2))(de_int(4))) == 16
    assert para_int(POT(de_int(3))(de_int(3))) == 27


def test_potenciacao_e_de_fato_multiplicacao_repetida():
    dois = de_int(2)
    mult_repetida = MULT(MULT(MULT(dois)(dois))(dois))(dois)
    assert para_int(POT(de_int(2))(de_int(4))) == para_int(mult_repetida)
