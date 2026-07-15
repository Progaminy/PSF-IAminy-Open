import pytest

from lingua_portuguesa.canal_ruidoso import (
    PESOS_ERRO_BASE,
    TipoErro,
    classificar_erro,
    contar_erros_da_memoria,
)


def test_transposicao_adjacente():
    assert classificar_erro("qeu", "que") == TipoErro.TRANSPOSICAO_ADJACENTE


def test_substituicao_teclado_adjacente():
    # "q" e "w" são fisicamente vizinhas no teclado (teclado_pt.json).
    assert classificar_erro("qata", "wata") == TipoErro.SUBSTITUICAO_TECLADO_ADJACENTE


def test_substituicao_fonetica():
    # "s" e "ç" pertencem à mesma classe alveolar/fricativa em
    # fonetica_computavel.TRACOS_GRAFEMA, e "ç" não existe no teclado
    # base (teclado_pt.json), então não é classificado como erro de
    # tecla vizinha primeiro. Não é "ç/c": este projeto trata "c" sempre
    # como velar/oclusivo (simplificação declarada em fonetica_computavel.py,
    # não modela o "c" mole antes de e/i), então c/ç não colapsam aqui.
    assert classificar_erro("casa", "caça") == TipoErro.SUBSTITUICAO_FONETICA


def test_acento_ausente():
    assert classificar_erro("voce", "você") == TipoErro.ACENTO_AUSENTE
    assert classificar_erro("e", "é") == TipoErro.ACENTO_AUSENTE


def test_insercao():
    assert classificar_erro("casa", "casca") == TipoErro.INSERCAO


def test_delecao():
    assert classificar_erro("casca", "casa") == TipoErro.DELECAO


def test_outro_quando_nao_bate_em_nenhum_padrao_reconhecido():
    assert classificar_erro("abcd", "wxyz") == TipoErro.OUTRO


def test_erro_ao_classificar_par_igual():
    with pytest.raises(ValueError):
        classificar_erro("igual", "igual")


def test_pesos_base_cobrem_todos_os_tipos_e_somam_valores_positivos():
    assert set(PESOS_ERRO_BASE) == set(TipoErro)
    assert all(peso > 0 for peso in PESOS_ERRO_BASE.values())


def test_contar_erros_da_memoria_nao_quebra_com_pares_reais():
    # pares_aprovados() inclui frases inteiras, não só palavras -- a
    # classificação tem que aguentar isso sem lançar exceção, mesmo que
    # a maioria caia em OUTRO.
    contagem = contar_erros_da_memoria()
    assert sum(contagem.values()) > 0
    assert set(contagem) <= set(TipoErro)
