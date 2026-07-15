"""Fase 1-C: prova fim-a-fim de que o intent "corrigir" (antes morto em
`nucleo/chat_texto.py::detectar_modo`) agora produz uma resposta real,
passando pela normalização de texto corrido (Fase 1-B), whitelist
ortográfica, aviso de parônimo e sugestão por distância de edição
(Fase 1), na mesma ordem conservadora sempre usada no projeto.
"""
from nucleo.chat_rotas_corretor import _responder_corrigir
from nucleo.chat_texto import detectar_modo
from nucleo.chat_vivo import responder


def test_detectar_modo_reconhece_intent_corrigir():
    assert detectar_modo("pode corrigir resposta por favor") == "corrigir"
    assert detectar_modo("corrige a resposta, por favor") == "corrigir"


def test_responder_corrigir_normaliza_espaco_maiuscula_e_pontuacao_final():
    resposta = _responder_corrigir(
        "  isto e uma frase mal formatada ,com espaco errado  e sem ponto final",
        "neutro",
    )
    assert resposta.intencao == "corrigir"
    assert "Isto e uma frase" in resposta.texto
    assert ", com" in resposta.texto
    assert ",com" not in resposta.texto
    assert "final." in resposta.texto


def test_responder_corrigir_aplica_whitelist_ortografica_conhecida():
    resposta = _responder_corrigir("a reposta esta correta.", "neutro")
    assert "resposta" in resposta.texto
    assert "reposta -> resposta" in resposta.texto


def test_responder_corrigir_avisa_paronimo_sem_trocar_sozinho():
    resposta = _responder_corrigir("marquei a sessão para amanhã.", "neutro")
    assert "cessão" in resposta.texto or "seção" in resposta.texto
    # nunca troca sozinho: a palavra original continua no texto final.
    assert "sessão" in resposta.texto


def test_responder_corrigir_sugere_palavra_fora_do_dicionario():
    resposta = _responder_corrigir("estudo protugues todos os dias.", "neutro")
    assert "português" in resposta.texto


def test_responder_corrigir_texto_ja_perfeito_nao_inventa_correcao():
    resposta = _responder_corrigir("Este texto já está correto.", "neutro")
    assert "Ortografia (erro conhecido corrigido)" not in resposta.texto


def test_chat_vivo_liga_intent_corrigir_a_rota_real():
    resposta = responder(
        "corrigir resposta: isto e um texto sem pontuacao final e com  espacos  errados"
    )
    assert resposta.intencao == "corrigir"
    assert resposta.conhecimento_encontrado is True
    assert resposta.origem == "lingua_portuguesa.corretor"
