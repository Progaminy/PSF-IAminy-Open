"""Marcador 1074 -- igualdade e ordem, derivadas da subtração truncada."""
from nucleo.aritmetica import IGUAL, MAIOR, MAIOR_OU_IGUAL, MENOR, MENOR_OU_IGUAL
from nucleo.traducao import de_int, para_bool


def test_igualdade_reflexiva():
    for k in range(10):
        assert para_bool(IGUAL(de_int(k))(de_int(k))) is True


def test_igualdade_distingue_numeros_diferentes():
    assert para_bool(IGUAL(de_int(3))(de_int(4))) is False


def test_menor_e_maior():
    assert para_bool(MENOR(de_int(2))(de_int(5))) is True
    assert para_bool(MENOR(de_int(5))(de_int(2))) is False
    assert para_bool(MAIOR(de_int(5))(de_int(2))) is True


def test_menor_ou_igual_e_maior_ou_igual_incluem_a_igualdade():
    assert para_bool(MENOR_OU_IGUAL(de_int(3))(de_int(3))) is True
    assert para_bool(MAIOR_OU_IGUAL(de_int(3))(de_int(3))) is True


def test_tricotomia_exatamente_uma_e_verdadeira():
    # Para todo par (m, n), exatamente uma de m<n, m=n, m>n é verdadeira.
    for m in range(6):
        for n in range(6):
            resultados = [
                para_bool(MENOR(de_int(m))(de_int(n))),
                para_bool(IGUAL(de_int(m))(de_int(n))),
                para_bool(MAIOR(de_int(m))(de_int(n))),
            ]
            assert sum(resultados) == 1


def test_ordem_e_transitiva():
    a, b, c = de_int(2), de_int(5), de_int(9)
    assert para_bool(MENOR(a)(b)) is True
    assert para_bool(MENOR(b)(c)) is True
    assert para_bool(MENOR(a)(c)) is True
