import pytest

from nucleo.combinatoria_natural import ESCOLHAS_ORDENADAS_COM_REPETICAO_PURO
from nucleo.traducao import de_int, para_int
from nucleo.espaco_combinatorio_palavras import (
    posicao_da_sequencia,
    sequencia_da_posicao,
    total_sequencias,
)


def test_total_sequencias_casos_pequenos():
    assert total_sequencias(26, 0) == 1
    assert total_sequencias(26, 1) == 26
    assert total_sequencias(26, 2) == 676
    assert total_sequencias(26, 4) == 456976


def test_total_sequencias_confere_contra_versao_pura_church():
    # Só alfabeto/comprimento pequenos -- a via de Church já fica
    # impraticável além de dígito único (aviso documentado em
    # nucleo/combinatoria.py), então a conferência cruzada usa um
    # alfabeto de brinquedo, não o alfabeto real de 26 letras.
    for tamanho_alfabeto in (2, 3, 4):
        for comprimento in (0, 1, 2, 3):
            esperado = para_int(
                ESCOLHAS_ORDENADAS_COM_REPETICAO_PURO(de_int(tamanho_alfabeto))(de_int(comprimento))
            )
            assert total_sequencias(tamanho_alfabeto, comprimento) == esperado


def test_posicao_da_sequencia_ordem_lexicografica():
    # alfabeto de tamanho 3 (símbolos 0,1,2), comprimento 2: ordem
    # esperada é 00,01,02,10,11,12,20,21,22 -> posições 0..8.
    assert posicao_da_sequencia((0, 0), 3) == 0
    assert posicao_da_sequencia((0, 1), 3) == 1
    assert posicao_da_sequencia((0, 2), 3) == 2
    assert posicao_da_sequencia((1, 0), 3) == 3
    assert posicao_da_sequencia((2, 2), 3) == 8


def test_posicao_da_sequencia_rejeita_indice_fora_do_alfabeto():
    with pytest.raises(ValueError):
        posicao_da_sequencia((0, 3), 3)


def test_sequencia_da_posicao_e_inversa_de_posicao_da_sequencia():
    tamanho_alfabeto, comprimento = 5, 3
    total = total_sequencias(tamanho_alfabeto, comprimento)
    for posicao in range(total):
        sequencia = sequencia_da_posicao(posicao, tamanho_alfabeto, comprimento)
        assert len(sequencia) == comprimento
        assert posicao_da_sequencia(sequencia, tamanho_alfabeto) == posicao


def test_sequencia_da_posicao_rejeita_posicao_fora_do_intervalo():
    with pytest.raises(ValueError):
        sequencia_da_posicao(9, 3, 2)  # só existem 9 sequências (posições 0..8)
