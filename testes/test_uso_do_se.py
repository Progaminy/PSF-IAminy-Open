from lingua_portuguesa.lexico import Dicionario
from lingua_portuguesa.uso_do_se import UsoDoSe, identificar_uso_de_se


def _dicionario() -> Dicionario:
    return Dicionario.padrao()


def test_se_apassivador_com_verbo_e_substantivo_no_plural():
    d = _dicionario()
    assert identificar_uso_de_se("Explicam-se os problemas.", d) is UsoDoSe.APASSIVADOR


def test_se_apassivador_com_verbo_e_substantivo_no_singular():
    d = _dicionario()
    assert identificar_uso_de_se("Explica-se o problema.", d) is UsoDoSe.APASSIVADOR


def test_se_indice_de_indeterminacao_antes_de_preposicao():
    d = _dicionario()
    assert identificar_uso_de_se("Entende-se de livros.", d) is UsoDoSe.INDETERMINACAO


def test_nao_arrisca_classificacao_quando_numero_nao_concorda():
    d = _dicionario()
    # "Explicam" (plural) + "o problema" (singular) - português real não usa
    # essa combinação para apassivador; sem concordância, não há prova.
    assert identificar_uso_de_se("Explicam-se o problema.", d) is None


def test_none_quando_nao_ha_padrao_de_se_na_frase():
    d = _dicionario()
    assert identificar_uso_de_se("Explica o problema.", d) is None
    assert identificar_uso_de_se("Os problemas existem.", d) is None
