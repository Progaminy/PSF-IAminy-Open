from lingua_portuguesa.teclado import sao_adjacentes, teclas_adjacentes


def test_adjacencias_conhecidas():
    assert "s" in teclas_adjacentes("a")
    assert "q" in teclas_adjacentes("a")
    assert "z" in teclas_adjacentes("a")
    assert "w" in teclas_adjacentes("a")


def test_nao_adjacentes():
    assert "p" not in teclas_adjacentes("a")
    assert "m" not in teclas_adjacentes("q")


def test_adjacencia_e_simetrica_para_todo_o_alfabeto():
    letras = "abcdefghijklmnopqrstuvwxyz"
    for letra in letras:
        for vizinha in teclas_adjacentes(letra):
            assert letra in teclas_adjacentes(vizinha), (
                f"{letra!r} lista {vizinha!r} como vizinha, mas {vizinha!r} não lista {letra!r} de volta"
            )


def test_sao_adjacentes_ignora_maiusculas():
    assert sao_adjacentes("A", "S")
    assert sao_adjacentes("a", "s")
    assert not sao_adjacentes("a", "p")


def test_letra_desconhecida_devolve_vazio():
    assert teclas_adjacentes("1") == frozenset()
    assert teclas_adjacentes("ç") == frozenset()
