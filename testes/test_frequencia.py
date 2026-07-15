from lingua_portuguesa.frequencia import frequencia_de, ordenar_por_frequencia


def test_palavra_frequente_no_corpus_tem_frequencia_real():
    # "que" aparece dezenas de vezes no corpus interno (conector comum em
    # frases de definição) -- tem que ter frequência real, positiva.
    freq = frequencia_de("que")
    assert freq is not None
    assert freq > 0


def test_palavra_ausente_do_corpus_devolve_none_nao_zero():
    freq = frequencia_de("xablincrunfotron")
    assert freq is None


def test_frequencia_e_sensivel_a_maiuscula_e_acento():
    assert frequencia_de("QUE") == frequencia_de("que")


def test_ordenar_por_frequencia_poe_palavra_comum_antes_de_palavra_rara():
    ordenado = ordenar_por_frequencia(("xablincrunfotron", "que"))
    assert ordenado == ("que", "xablincrunfotron")


def test_ordenar_por_frequencia_preserva_ordem_original_entre_desconhecidas():
    ordenado = ordenar_por_frequencia(("zzzznada", "wwwwoutro"))
    assert ordenado == ("zzzznada", "wwwwoutro")
