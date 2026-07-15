"""Fecha um achado real de auditoria externa: os 11 verbos irregulares
comuns (ser, estar, ter, fazer, ir, querer, poder, saber, dizer, ver, dar)
só tinham formas do presente em `lexico_base.json` -- por isso "foi"
(pretérito comuníssimo de "ir"/"ser") não estava no dicionário e o
corretor sugeria "oi" no lugar. Este ficheiro prende o pretérito perfeito
das formas mais comuns em texto corrido (3ª pessoa singular/plural, mais
1ª pessoa onde a forma é inequívoca).
"""
from lingua_portuguesa import Dicionario, MotorPortugues
from lingua_portuguesa.corretor import Corretor
from lingua_portuguesa.tipos import Pessoa, Numero


def test_foi_esta_no_dicionario_com_pessoa_e_numero_reais():
    dicionario = Dicionario.padrao()
    leituras = dicionario.buscar("foi")
    assert leituras
    lemas = {leitura.lema for leitura in leituras}
    # "foi" é homógrafo real entre "ir" e "ser" -- as duas leituras devem
    # existir, nenhuma escondida.
    assert lemas == {"ir", "ser"}
    for leitura in leituras:
        assert leitura.pessoa == Pessoa.TERCEIRA
        assert leitura.numero == Numero.SINGULAR


def test_formas_irregulares_centrais_estao_no_dicionario():
    dicionario = Dicionario.padrao()
    formas_esperadas = (
        "fui", "foi", "fomos", "foram",  # ser/ir
        "estive", "esteve", "estivemos", "estiveram",  # estar
        "tive", "teve", "tivemos", "tiveram",  # ter
        "fiz", "fez", "fizemos", "fizeram",  # fazer
        "quis", "quisemos", "quiseram",  # querer
        "pude", "pôde", "pudemos", "puderam",  # poder
        "soube", "soubemos", "souberam",  # saber
        "disse", "dissemos", "disseram",  # dizer
        "vi", "viu", "vimos", "viram",  # ver
        "dei", "deu", "demos", "deram",  # dar
    )
    for forma in formas_esperadas:
        assert forma in dicionario, f"{forma!r} deveria estar no dicionário"


def test_formas_ambiguas_entre_primeira_e_terceira_pessoa_nao_fingem_pessoa_unica():
    # "quis"/"soube"/"disse" são genuinamente a mesma forma para "eu" e
    # "ele" no pretérito -- o índice deve preservar as duas leituras, sem
    # escolher uma pessoa por acaso nem apagar esse traço gramatical.
    dicionario = Dicionario.padrao()
    for forma, lema in (("quis", "querer"), ("soube", "saber"), ("disse", "dizer")):
        flexoes = {
            (leitura.pessoa, leitura.numero)
            for leitura in dicionario.buscar(forma)
            if leitura.lema == lema
        }
        assert flexoes == {
            (Pessoa.PRIMEIRA, Numero.SINGULAR),
            (Pessoa.TERCEIRA, Numero.SINGULAR),
        }


def test_corretor_nao_confunde_foi_com_interjeicao_oi():
    resultado = Corretor().corrigir_texto("Ele foi a escola.")
    sugestoes = dict(resultado.sugestoes_ortografia)
    assert "foi" not in sugestoes


def test_concordancia_verbal_pega_discordancia_real_com_viram():
    motor = MotorPortugues()
    analise = motor.analisar("O menino viram a casa.")
    codigos = [d.codigo for d in analise.diagnosticos]
    assert "CONCORDANCIA_VERBO_SUJEITO" in codigos
