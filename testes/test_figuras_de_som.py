from lingua_portuguesa.figuras_de_som import detectar_aliteracao, detectar_assonancia


def test_aliteracao_classica_o_rato_roeu():
    palavras = "o rato roeu a roupa do rei de Roma".split()
    assert detectar_aliteracao(palavras) == "r"


def test_assonancia_com_vogal_a_repetida():
    palavras = "Amanhã a Ana anda apressada".split()
    assert detectar_assonancia(palavras) == "a"


def test_nenhuma_aliteracao_em_frase_sem_repeticao_suficiente():
    palavras = "o gato subiu no telhado".split()
    assert detectar_aliteracao(palavras) is None


def test_nenhuma_assonancia_em_frase_sem_repeticao_suficiente():
    palavras = "o gato subiu no telhado".split()
    assert detectar_assonancia(palavras) is None


def test_minimo_configuravel_evita_falso_positivo():
    # Duas palavras com "c" inicial não bastam para minimo padrão (3).
    palavras = "casa cor".split()
    assert detectar_aliteracao(palavras) is None
    assert detectar_aliteracao(palavras, minimo=2) == "c"


def test_lista_vazia_nao_gera_erro():
    assert detectar_aliteracao([]) is None
    assert detectar_assonancia([]) is None
