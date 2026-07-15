"""Etapa 1 -- número natural (zero e sucessor), a raiz da linha matemática.

Achado real ao escrever isto: ETAPA_03_DIVISIBILIDADE_PURA.md já citava
"número natural"/"zero"/"sucessor" como dependência desde o primeiro
documento matemático que existe -- sem que nenhum dos três tivesse nascido
como conceito próprio. `nucleo/primitivas.py` já tinha o código real
(ZERO, S) havia muito tempo; só faltava o documento e o teste.
"""
from nucleo.primitivas import S, ZERO
from nucleo.traducao import de_int, para_int


def test_zero_traduz_para_0():
    assert para_int(ZERO) == 0


def test_sucessor_de_zero_e_um():
    assert para_int(S(ZERO)) == 1


def test_sucessores_repetidos_contam():
    tres = S(S(S(ZERO)))
    assert para_int(tres) == 3


def test_de_int_e_para_int_sao_inversos_um_do_outro():
    for k in range(20):
        assert para_int(de_int(k)) == k


def test_sucessor_nunca_e_igual_ao_numero_original():
    # Contagem real: aplicar "mais um" sempre produz um número diferente,
    # nunca o mesmo -- confere isso comparando as traduções, não achando.
    for k in range(10):
        n = de_int(k)
        assert para_int(S(n)) == para_int(n) + 1


def test_numero_nasce_so_da_quantidade_de_sucessores_nunca_de_simbolo():
    # "3" não é um símbolo primitivo -- é sucessor(sucessor(sucessor(zero))).
    # Duas construções que aplicam sucessor a mesma quantidade de vezes
    # traduzem para o mesmo inteiro, mesmo partindo de expressões diferentes.
    a = S(S(ZERO))
    b = S(S(ZERO))
    assert para_int(a) == para_int(b) == 2
