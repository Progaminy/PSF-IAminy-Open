from lingua_portuguesa.distancia_edicao import (
    distancia_levenshtein,
    distancia_damerau_levenshtein,
)


def test_levenshtein_casos_basicos():
    assert distancia_levenshtein("casa", "casa") == 0
    assert distancia_levenshtein("", "casa") == 4
    assert distancia_levenshtein("casa", "") == 4
    assert distancia_levenshtein("casa", "caza") == 1  # substituição
    assert distancia_levenshtein("casa", "casas") == 1  # inserção
    assert distancia_levenshtein("casas", "casa") == 1  # remoção


def test_levenshtein_respeita_limite():
    assert distancia_levenshtein("abcdef", "uvwxyz", limite=2) == 3


def test_levenshtein_nao_trata_transposicao_como_um_so_erro():
    # "hte" -> "the": trocar 'h' e 't' de posição. Levenshtein simples
    # não reconhece transposição, então conta como 2 substituições.
    assert distancia_levenshtein("hte", "the") == 2


def test_damerau_levenshtein_casos_basicos():
    assert distancia_damerau_levenshtein("casa", "casa") == 0
    assert distancia_damerau_levenshtein("", "casa") == 4
    assert distancia_damerau_levenshtein("casa", "") == 4
    assert distancia_damerau_levenshtein("casa", "caza") == 1
    assert distancia_damerau_levenshtein("casa", "casas") == 1


def test_damerau_levenshtein_reconhece_transposicao_adjacente_como_um_erro():
    # Esta é a diferença real que justifica ter as duas funções: a mesma
    # troca "hte" -> "the" custa 1 em Damerau-Levenshtein, não 2.
    assert distancia_damerau_levenshtein("hte", "the") == 1
    assert distancia_damerau_levenshtein("pssoa", "psosa") == 1
    assert distancia_damerau_levenshtein("form", "from") == 1


def test_damerau_levenshtein_respeita_limite():
    assert distancia_damerau_levenshtein("abcdef", "uvwxyz", limite=2) == 3


def test_damerau_levenshtein_nao_reconhece_transposicao_nao_adjacente_como_um_so_erro():
    # "abc" -> "cba": 'a' e 'c' trocam de posição mas não são adjacentes
    # na string de origem — a variante restrita (optimal string alignment)
    # não cobre isso como transposição única, deve custar mais que 1.
    assert distancia_damerau_levenshtein("abc", "cba") > 1
