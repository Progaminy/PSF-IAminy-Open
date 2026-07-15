import pytest

from lingua_portuguesa.paronimos_comuns import PARONIMOS_COMUNS, ParPeronimo, buscar_par


def test_lista_tem_pares_reais_com_significados_distintos():
    assert len(PARONIMOS_COMUNS) >= 10
    for par in PARONIMOS_COMUNS:
        assert len(par.palavras) == len(par.significados)
        assert len(set(par.significados)) == len(par.significados)


def test_busca_encontra_par_por_qualquer_palavra_do_grupo():
    par = buscar_par("descrição")
    assert par is not None
    assert "discrição" in par.palavras

    par2 = buscar_par("discrição")
    assert par2 is not None
    assert par2 == par


def test_grupo_triplo_cessao_sessao_secao():
    par = buscar_par("seção")
    assert par is not None
    assert set(par.palavras) == {"cessão", "sessão", "seção"}


def test_busca_e_insensivel_a_maiusculas():
    assert buscar_par("DESCRIÇÃO") == buscar_par("descrição")


def test_none_para_palavra_fora_da_lista():
    assert buscar_par("palavra_qualquer_inexistente") is None


def test_rejeita_par_mal_formado():
    with pytest.raises(ValueError, match="significado correspondente"):
        ParPeronimo(("a", "b"), ("só um significado",))
    with pytest.raises(ValueError, match="ao menos duas palavras"):
        ParPeronimo(("a",), ("x",))
