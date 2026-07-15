import pytest

from nucleo.medidas_grandezas import (
    Area,
    Comprimento,
    Massa,
    Tempo,
    Volume,
    area_retangulo,
    medir,
    sao_grandezas_proporcionais,
    volume_paralelepipedo,
)
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _c(numerador: int, denominador: int = 1) -> Comprimento:
    return Comprimento(RacionalAssinado(numerador, denominador))


def test_comprimento_compara_soma_e_subtrai_como_grandeza():
    a = _c(7, 2)  # 3.5
    b = _c(3)
    assert a.comparar(b) == 1
    assert b.comparar(a) == -1
    assert a.comparar(a) == 0
    assert a.somar(b) == _c(13, 2)
    assert a.subtrair(b) == _c(1, 2)


def test_comprimento_rejeita_grandeza_negativa_e_subtracao_maior_que_o_todo():
    with pytest.raises(ValueError, match="negativo"):
        Comprimento(RacionalAssinado(-1))
    with pytest.raises(ValueError, match="não admite retirar"):
        _c(2).subtrair(_c(5))


def test_medir_conta_unidades_por_subtracao_repetida_e_preserva_resto():
    grandeza = _c(17, 2)  # 8.5
    unidade = _c(3)
    medida = medir(grandeza, unidade)
    assert medida.quantidade == 2
    assert medida.resto == _c(5, 2)  # 8.5 - 2*3 = 2.5
    certificado = medida.certificado()
    assert certificado["resto_menor_que_unidade"] is True


def test_medir_grandeza_menor_que_unidade_da_quantidade_zero():
    medida = medir(_c(1, 2), _c(3))
    assert medida.quantidade == 0
    assert medida.resto == _c(1, 2)


def test_medir_rejeita_unidade_nula():
    with pytest.raises(ValueError, match="unidade de medida"):
        medir(_c(5), _c(0))


def test_grandezas_proporcionais_por_produto_cruzado_exato():
    # 2/4 == 3/6
    assert sao_grandezas_proporcionais(_c(2), _c(4), _c(3), _c(6))
    # 2/4 != 3/5
    assert not sao_grandezas_proporcionais(_c(2), _c(4), _c(3), _c(5))


def test_grandezas_proporcionais_rejeita_termo_de_comparacao_nulo():
    with pytest.raises(ValueError, match="proporção"):
        sao_grandezas_proporcionais(_c(2), _c(0), _c(3), _c(6))


def test_massa_e_tempo_sao_especies_independentes_mas_usam_a_mesma_estrutura():
    m1 = Massa(RacionalAssinado(5))
    m2 = Massa(RacionalAssinado(3))
    assert m1.somar(m2) == Massa(RacionalAssinado(8))
    assert type(m1.somar(m2)) is Massa

    t1 = Tempo(RacionalAssinado(10))
    t2 = Tempo(RacionalAssinado(4))
    assert t1.subtrair(t2) == Tempo(RacionalAssinado(6))
    assert type(t1.subtrair(t2)) is Tempo


def test_medir_rejeita_grandeza_e_unidade_de_especies_diferentes():
    with pytest.raises(ValueError, match="mesma espécie"):
        medir(Massa(RacionalAssinado(10)), Tempo(RacionalAssinado(3)))


def test_medir_funciona_para_qualquer_especie_de_grandeza():
    medida = medir(Massa(RacionalAssinado(17)), Massa(RacionalAssinado(5)))
    assert medida.quantidade == 3
    assert medida.resto == Massa(RacionalAssinado(2))


def test_area_retangulo_nasce_do_produto_de_dois_comprimentos():
    area = area_retangulo(_c(3), _c(4))
    assert area == Area(RacionalAssinado(12))
    assert type(area) is Area


def test_volume_paralelepipedo_nasce_do_produto_de_tres_comprimentos():
    volume = volume_paralelepipedo(_c(2), _c(3), _c(4))
    assert volume == Volume(RacionalAssinado(24))
    assert type(volume) is Volume


def test_areas_se_somam_como_grandeza():
    a1 = area_retangulo(_c(2), _c(3))  # 6
    a2 = area_retangulo(_c(1), _c(4))  # 4
    assert a1.somar(a2) == Area(RacionalAssinado(10))


def test_grandeza_negativa_rejeitada_tambem_para_massa_e_area():
    with pytest.raises(ValueError, match="Massa é uma grandeza"):
        Massa(RacionalAssinado(-1))
    with pytest.raises(ValueError, match="Area é uma grandeza"):
        Area(RacionalAssinado(-1))
