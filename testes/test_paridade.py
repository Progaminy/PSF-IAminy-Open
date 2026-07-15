from nucleo.paridade import eh_impar, eh_par, paridade, paridade_da_soma


def test_eh_par():
    assert eh_par(0) is True
    assert eh_par(2) is True
    assert eh_par(4) is True
    assert eh_par(1) is False
    assert eh_par(7) is False


def test_eh_impar():
    assert eh_impar(3) is True
    assert eh_impar(4) is False


def test_paridade_texto():
    assert paridade(6) == "par"
    assert paridade(9) == "ímpar"


def test_paridade_da_soma_par_mais_par():
    assert paridade_da_soma(4, 6) == "par"


def test_paridade_da_soma_impar_mais_impar():
    assert paridade_da_soma(3, 5) == "par"


def test_paridade_da_soma_par_mais_impar():
    assert paridade_da_soma(4, 3) == "ímpar"
    assert paridade_da_soma(3, 4) == "ímpar"
