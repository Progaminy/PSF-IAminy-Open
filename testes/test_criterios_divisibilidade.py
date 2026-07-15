from nucleo.criterios_divisibilidade import (
    divisivel_por_cinco,
    divisivel_por_dez,
    divisivel_por_dois,
    divisivel_por_nove,
    divisivel_por_tres,
)


def test_divisivel_por_dois():
    assert divisivel_por_dois(1234) is True
    assert divisivel_por_dois(1235) is False


def test_divisivel_por_cinco():
    assert divisivel_por_cinco(1235) is True
    assert divisivel_por_cinco(1230) is True
    assert divisivel_por_cinco(1234) is False


def test_divisivel_por_dez():
    assert divisivel_por_dez(1230) is True
    assert divisivel_por_dez(1235) is False


def test_divisivel_por_tres():
    assert divisivel_por_tres(123) is True
    assert divisivel_por_tres(124) is False


def test_divisivel_por_nove():
    assert divisivel_por_nove(18) is True
    assert divisivel_por_nove(19) is False
    assert divisivel_por_nove(123456789) is True


def test_divisivel_por_numero_de_varios_digitos_fica_rapido():
    # trava de regressão de performance: dividir_com_resto sobre o número
    # inteiro (em vez de dígito a dígito) já causou lentidão real antes
    import time

    inicio = time.time()
    divisivel_por_tres(987654321)
    assert time.time() - inicio < 2.0
