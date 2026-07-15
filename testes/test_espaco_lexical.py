import pytest

from lingua_portuguesa.espaco_lexical import (
    ALFABETO_PT,
    TAMANHO_ALFABETO,
    palavra_da_posicao,
    posicao_da_palavra,
    total_palavras_possiveis,
)
from lingua_portuguesa.lexico import Dicionario


def test_alfabeto_tem_26_letras_sem_acento():
    assert TAMANHO_ALFABETO == 26
    assert ALFABETO_PT == "abcdefghijklmnopqrstuvwxyz"


def test_total_palavras_possiveis_bate_com_arranjo_com_repeticao():
    assert total_palavras_possiveis(1) == 26
    assert total_palavras_possiveis(2) == 676
    assert total_palavras_possiveis(4) == 456976


def test_posicao_de_letras_isoladas():
    assert posicao_da_palavra("a") == 0
    assert posicao_da_palavra("z") == 25


def test_posicao_ignora_maiuscula_minuscula():
    assert posicao_da_palavra("A") == posicao_da_palavra("a")


def test_posicao_de_palavra_de_duas_letras():
    assert posicao_da_palavra("aa") == 0
    assert posicao_da_palavra("az") == 25
    assert posicao_da_palavra("ba") == 26
    assert posicao_da_palavra("zz") == 675


def test_palavra_da_posicao_e_inversa_de_posicao_da_palavra():
    for palavra in ("sol", "casa", "psf", "zzzz", "abacate", "abacateiro"):
        posicao = posicao_da_palavra(palavra)
        assert palavra_da_posicao(posicao, len(palavra)) == palavra


def test_palavra_da_posicao_recusa_comprimento_fora_de_qualquer_escala_pratica():
    # bem além do limite de sanidade (10**15) -- tem que recusar com erro
    # claro, nunca travar tentando calcular um total astronómico.
    with pytest.raises(ValueError):
        total_palavras_possiveis(1000)


def test_letra_acentuada_nao_pertence_ao_alfabeto_base():
    # decisão de design explícita do módulo: acento não é símbolo próprio
    # nesta camada -- "ação" precisa passar por outra camada (ainda não
    # construída) antes de ter posição aqui.
    with pytest.raises(ValueError):
        posicao_da_palavra("ação")


def test_palavra_vazia_nao_tem_posicao():
    with pytest.raises(ValueError):
        posicao_da_palavra("")


def test_combinacoes_de_letras_so_devolvem_palavras_do_dicionario():
    dicionario = Dicionario.padrao()
    palavras = dicionario.palavras_com_letras("casa", comprimento_minimo=2)

    assert "casa" in palavras
    assert "zzzz" not in palavras
    assert all(palavra in dicionario for palavra in palavras)


def test_combinacoes_respeitam_repeticao_e_podem_exigir_todas_as_letras():
    dicionario = Dicionario.padrao()

    assert "casa" not in dicionario.palavras_com_letras("cas", comprimento_minimo=2)
    assert dicionario.palavras_com_letras("asac", usar_todas=True) == ("casa",)


def test_combinacoes_encontram_ortografia_acentuada_com_letras_base():
    dicionario = Dicionario.padrao()

    assert "oração" in dicionario.palavras_com_letras("oracao", usar_todas=True)
