"""Corpus minúsculo construído à mão -- todo valor esperado abaixo foi
calculado manualmente (janela=2), exatamente porque coocorrência contada
+ cosseno é aritmética simples e verificável, ao contrário de um
embedding treinado.
"""
from lingua_portuguesa.proximidade_semantica import (
    proximidade,
    similaridade_cosseno,
    vetor_de,
    vetores_coocorrencia,
)

_TOKENS = ("rei", "governa", "reino", "rainha", "governa", "reino", "pedra", "rola", "montanha")
# vetor(rei)      = {governa:1, reino:1}
# vetor(rainha)   = {governa:2, reino:2}          -- proporcional a rei, cosseno = 1.0
# vetor(pedra)    = {governa:1, reino:1, rola:1, montanha:1}
# vetor(montanha) = {pedra:1, rola:1}              -- nenhuma dimensão em comum com rei


def _vetores():
    return vetores_coocorrencia(_TOKENS, janela=2)


def test_vetores_de_coocorrencia_valores_exatos():
    vetores = _vetores()
    assert vetor_de("rei", vetores) == {"governa": 1, "reino": 1}
    assert vetor_de("rainha", vetores) == {"governa": 2, "reino": 2}
    assert vetor_de("pedra", vetores) == {"governa": 1, "reino": 1, "rola": 1, "montanha": 1}


def test_palavra_ausente_tem_vetor_vazio():
    vetores = _vetores()
    assert vetor_de("inexistente", vetores) == {}


def test_similaridade_cosseno_vetores_proporcionais_e_exatamente_um():
    vetores = _vetores()
    resultado = similaridade_cosseno(vetor_de("rei", vetores), vetor_de("rainha", vetores))
    assert abs(resultado - 1.0) < 1e-9


def test_similaridade_cosseno_valor_exato_para_vetores_parcialmente_sobrepostos():
    # produto = 1*1 + 1*1 = 2; norma(rei) = sqrt(2); norma(pedra) = sqrt(4) = 2
    # cosseno = 2 / (sqrt(2) * 2) = 1/sqrt(2)
    vetores = _vetores()
    resultado = similaridade_cosseno(vetor_de("rei", vetores), vetor_de("pedra", vetores))
    assert abs(resultado - (1 / (2 ** 0.5))) < 1e-9


def test_similaridade_cosseno_zero_sem_dimensao_em_comum():
    vetores = _vetores()
    assert similaridade_cosseno(vetor_de("rei", vetores), vetor_de("montanha", vetores)) == 0.0


def test_similaridade_cosseno_vetor_vazio_e_zero():
    assert similaridade_cosseno({}, {"x": 1}) == 0.0
    assert similaridade_cosseno({"x": 1}, {}) == 0.0


def test_proximidade_escolhe_candidato_mais_proximo_em_cenario_construido():
    vetores = _vetores()
    # "rainha" é o candidato mais próximo de "rei" (cosseno 1.0) do que
    # "pedra" (≈0.707) ou "montanha" (0.0) -- desambiguação real, não
    # adivinhada.
    candidatos = ("pedra", "rainha", "montanha")
    melhor = max(candidatos, key=lambda c: proximidade("rei", c, vetores))
    assert melhor == "rainha"


def test_proximidade_padrao_usa_corpus_interno_sem_quebrar():
    valor = proximidade("que", "que")
    assert abs(valor - 1.0) < 1e-9
