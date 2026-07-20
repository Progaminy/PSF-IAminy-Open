"""Testes da raiz quadrada reconstruída por pares de algarismos.

Roda com: python3 -m pytest testes/test_raiz_quadrada_pura.py
"""
import math
import random

import pytest

from matematica.raiz import raiz_quadrada


@pytest.mark.parametrize("n, raiz_esperada", [(0, 0), (1, 1), (4, 2), (9, 3), (25, 5), (100, 10), (144, 12), (10000, 100)])
def test_quadrado_perfeito_devolve_inteiro_exato(n, raiz_esperada):
    resultado = raiz_quadrada(n)
    assert resultado.quadrado_perfeito is True
    assert resultado.decimal == str(raiz_esperada)
    assert resultado.resto_final == 0
    assert resultado.casas == 0


@pytest.mark.parametrize("n", [2, 3, 5, 8, 13, 50, 1000, 9999])
def test_nao_perfeito_nao_e_marcado_como_perfeito(n):
    resultado = raiz_quadrada(n)
    assert resultado.quadrado_perfeito is False
    assert "," in resultado.decimal


def test_raiz_de_13_bate_com_valor_conhecido_truncado():
    resultado = raiz_quadrada(13, casas=4, modo="truncar")
    assert resultado.decimal == "3,6055"


def test_raiz_de_13_bate_com_valor_conhecido_arredondado():
    resultado = raiz_quadrada(13, casas=4, modo="arredondar")
    assert resultado.decimal == "3,6056"


def test_raiz_de_2_com_oito_casas():
    resultado = raiz_quadrada(2, casas=8, modo="truncar")
    assert resultado.decimal == "1,41421356"


def test_modo_invalido_levanta_erro():
    with pytest.raises(ValueError):
        raiz_quadrada(13, modo="qualquer")


def test_radicando_negativo_levanta_erro():
    with pytest.raises(ValueError):
        raiz_quadrada(-1)


def test_casas_negativas_levanta_erro():
    with pytest.raises(ValueError):
        raiz_quadrada(13, casas=-1)


def test_passos_documentam_a_construcao():
    resultado = raiz_quadrada(13)
    assert resultado.passos
    assert all(isinstance(p, str) and p for p in resultado.passos)


def test_arredondar_sem_casas_explicitas_nao_muda_ultima_casa():
    truncado = raiz_quadrada(13, modo="truncar")
    arredondado = raiz_quadrada(13, modo="arredondar")
    assert truncado.decimal == arredondado.decimal


@pytest.mark.parametrize("semente", range(5))
def test_amostra_aleatoria_confere_com_oraculo_nativo(semente):
    """Cross-check com math.sqrt/isqrt como calculadora de validação (nunca a fonte da resposta)."""
    aleatorio = random.Random(semente)
    for _ in range(40):
        n = aleatorio.randint(0, 200_000)
        resultado = raiz_quadrada(n, casas=6, modo="truncar")
        raiz_inteira = math.isqrt(n)
        if raiz_inteira * raiz_inteira == n:
            assert resultado.quadrado_perfeito is True
            assert resultado.decimal == str(raiz_inteira)
        else:
            assert resultado.quadrado_perfeito is False
            obtido = float(resultado.decimal.replace(",", "."))
            assert abs(obtido - math.sqrt(n)) < 1e-5
