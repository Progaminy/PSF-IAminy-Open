"""Testes semânticos da autoridade por domínio na entrada oficial."""
from nucleo.chat_vivo import responder


def _responder(texto: str):
    return responder(texto, registrar=False)


def test_identidade_nao_vaza_codigo_do_indice_total():
    resposta = _responder("quem é você?")
    assert resposta.origem == "motor.geral:identidade"
    assert "PSF-IAminy" in resposta.texto
    assert "PALAVRAS_TIPO" not in resposta.texto


def test_conceito_de_portugues_vem_do_motor_especializado():
    resposta = _responder("o que é ditongo crescente?")
    assert resposta.origem == "motor.portugues:conhecimento_puro"
    assert "semivogal antecede a vogal nuclear" in resposta.texto


def test_analise_linguistica_encontra_as_duas_concordancias():
    resposta = _responder("analise: As menina estudam.")
    assert resposta.origem == "motor.portugues:analisar"
    assert "determinante" in resposta.texto
    assert "sujeito" in resposta.texto


def test_calculo_chega_ao_motor_matematico_com_precisao_pedida():
    resposta = _responder("calcule 12:5 com 3 casas")
    assert resposta.origem == "motor.matematica:calcular"
    assert "2,400" in resposta.texto
    assert "12/5" in resposta.texto


def test_hall_nao_e_confundido_com_bell():
    resposta = _responder("prove o teorema de Hall")
    assert resposta.origem.endswith("grafos emparelhamento hall")
    assert "condição de Hall" in resposta.texto
    assert "Bell" not in resposta.texto
    assert "não substitui uma prova simbólica geral" in resposta.texto


def test_ramsey_33_chega_a_reconstrucao_materializada():
    resposta = _responder("explique R(3,3)=6")
    assert resposta.origem.endswith("ramsey 33")
    assert "K6" in resposta.texto
    assert "K5" in resposta.texto
