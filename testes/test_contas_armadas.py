import pytest

from nucleo.contas_armadas import (
    digitos,
    divisao_armada,
    multiplicacao_armada,
    soma_armada,
    subtracao_armada,
)


def test_digitos_decompoe_da_esquerda_para_a_direita():
    assert digitos(0) == (0,)
    assert digitos(7) == (7,)
    assert digitos(408) == (4, 0, 8)
    assert digitos(1970) == (1, 9, 7, 0)


def test_soma_armada_sem_vai_um():
    registro = soma_armada(123, 45)
    assert registro.resultado == 168
    assert registro.colunas[0].vai_um == 0


def test_soma_armada_com_vai_um_em_cadeia():
    # 999 + 1 = 1000: "vai um" se propaga por todas as colunas.
    registro = soma_armada(999, 1)
    assert registro.resultado == 1000
    assert [c.vai_um for c in registro.colunas] == [1, 1, 1]
    assert [c.digito_resultado for c in registro.colunas] == [0, 0, 0]


def test_soma_armada_confere_cada_coluna():
    registro = soma_armada(48, 27)
    # 48 + 27 = 75: unidades 8+7=15 -> digito 5, vai 1; dezenas 4+2+1=7 -> digito 7, vai 0
    assert registro.resultado == 75
    unidades, dezenas = registro.colunas
    assert (unidades.digito_a, unidades.digito_b, unidades.vem_um) == (8, 7, 0)
    assert (unidades.digito_resultado, unidades.vai_um) == (5, 1)
    assert (dezenas.digito_a, dezenas.digito_b, dezenas.vem_um) == (4, 2, 1)
    assert (dezenas.digito_resultado, dezenas.vai_um) == (7, 0)


def test_subtracao_armada_sem_emprestimo():
    registro = subtracao_armada(75, 23)
    assert registro.resultado == 52
    assert all(not c.emprestou for c in registro.colunas)


def test_subtracao_armada_com_emprestimo():
    # 52 - 27 = 25: unidades 2-7 empresta -> 12-7=5; dezenas 5-1(emprestado)-2=2
    registro = subtracao_armada(52, 27)
    assert registro.resultado == 25
    unidades, dezenas = registro.colunas
    assert unidades.emprestou is True
    assert unidades.digito_resultado == 5
    assert dezenas.digito_resultado == 2


def test_subtracao_armada_com_emprestimo_em_cadeia():
    # 1000 - 1 = 999: empréstimo se propaga por todas as colunas com zero.
    registro = subtracao_armada(1000, 1)
    assert registro.resultado == 999
    assert [c.digito_resultado for c in registro.colunas] == [9, 9, 9, 0]


def test_subtracao_armada_rejeita_retirar_mais_do_que_existe():
    with pytest.raises(ValueError, match="não admite retirar"):
        subtracao_armada(3, 10)


def test_texto_produz_layout_de_conta_armada():
    registro = soma_armada(48, 27)
    texto = registro.texto()
    assert "48" in texto
    assert "27" in texto
    assert "75" in texto
    assert "+" in texto


def test_multiplicacao_armada_por_digito_unico():
    registro = multiplicacao_armada(23, 4)
    assert registro.resultado == 92
    assert len(registro.linhas) == 1
    assert registro.linhas[0].valor == 92


def test_multiplicacao_armada_com_linhas_deslocadas():
    # 23 x 14: linha das unidades (23x4=92) + linha das dezenas (23x1, deslocada) = 230
    registro = multiplicacao_armada(23, 14)
    assert registro.resultado == 322
    unidades, dezenas = registro.linhas
    assert unidades.valor == 92
    assert dezenas.valor == 230


def test_multiplicacao_armada_com_vai_um_em_cadeia():
    registro = multiplicacao_armada(99, 99)
    assert registro.resultado == 9801


def test_multiplicacao_armada_por_zero():
    registro = multiplicacao_armada(456, 0)
    assert registro.resultado == 0


def test_divisao_armada_com_multiplos_digitos_do_quociente():
    # 456 / 23 = 19 resto 19 (dígito de quociente 0 no primeiro passo)
    registro = divisao_armada(456, 23)
    assert registro.quociente == 19
    assert registro.resto == 19
    assert [c.digito_quociente for c in registro.colunas] == [0, 1, 9]


def test_divisao_armada_exata():
    registro = divisao_armada(84, 7)
    assert registro.quociente == 12
    assert registro.resto == 0


def test_divisao_armada_dividendo_menor_que_divisor():
    registro = divisao_armada(3, 23)
    assert registro.quociente == 0
    assert registro.resto == 3


def test_divisao_armada_rejeita_divisor_zero():
    with pytest.raises(ValueError, match="não existe divisão por zero"):
        divisao_armada(10, 0)
