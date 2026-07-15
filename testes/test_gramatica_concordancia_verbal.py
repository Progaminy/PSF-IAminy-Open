"""Fase 2 do plano de corretor: concordância verbal real (sujeito-verbo)
e a fatia estreita e honesta de "categoria incompatível" (substituto da
técnica 8/BERT). Fecha a lacuna documentada no conceito 203
("Casos especiais permanecem para crescimento") -- até aqui só existiam
regras de concordância determinante/nome e nome/adjetivo.
"""
from lingua_portuguesa import ClasseGramatical, Dicionario, EntradaLexical, Genero, MotorPortugues, Numero
from lingua_portuguesa.tipos import Pessoa
from lingua_portuguesa.lexico_expansao import entradas_expandidas


def _codigos(analise):
    return tuple(d.codigo for d in analise.diagnosticos)


# --- Pessoa fim-a-fim: do dado real do JSON até o campo do dataclass -----

def test_pessoa_vem_do_json_para_pronomes_e_verbos():
    dicionario = Dicionario.padrao()
    eu = dicionario.buscar("eu")[0]
    assert eu.pessoa == Pessoa.PRIMEIRA
    assert eu.numero == Numero.SINGULAR

    nos = dicionario.buscar("nós")[0]
    assert nos.pessoa == Pessoa.PRIMEIRA
    assert nos.numero == Numero.PLURAL

    estudam = dicionario.buscar("estudam")[0]
    assert estudam.pessoa == Pessoa.TERCEIRA
    assert estudam.numero == Numero.PLURAL


def test_pessoa_gerada_por_verbo_novo_em_lexico_expansao():
    # "conversar" só existe via _VERBOS (lexico_expansao.py), não no JSON
    # base -- prova que a geração nova (Fase 2.1) etiqueta pessoa/número
    # por si só, não só repassa dado já pronto do JSON.
    formas = {e.forma: e for e in entradas_expandidas() if e.lema == "conversar"}
    assert formas["converso"].pessoa == Pessoa.PRIMEIRA
    assert formas["converso"].numero == Numero.SINGULAR
    assert formas["conversamos"].pessoa == Pessoa.PRIMEIRA
    assert formas["conversamos"].numero == Numero.PLURAL
    assert formas["conversam"].pessoa == Pessoa.TERCEIRA
    assert formas["conversam"].numero == Numero.PLURAL
    assert formas["conversar"].pessoa is None
    assert formas["conversar"].numero is None


# --- RegraConcordanciaVerboSujeito, sujeito substantivo (só número) ------

def test_sujeito_substantivo_concorda_nao_gera_diagnostico():
    motor = MotorPortugues()
    analise = motor.analisar("O livro come.")
    assert "CONCORDANCIA_VERBO_SUJEITO" not in _codigos(analise)


def test_sujeito_substantivo_discorda_em_numero_e_sinalizado():
    motor = MotorPortugues()
    analise = motor.analisar("O livro comem.")
    assert "CONCORDANCIA_VERBO_SUJEITO" in _codigos(analise)
    diagnostico = next(d for d in analise.diagnosticos if d.codigo == "CONCORDANCIA_VERBO_SUJEITO")
    assert "número" in diagnostico.mensagem


# --- RegraConcordanciaVerboSujeito, sujeito pronome (número e pessoa) ----

def test_sujeito_pronome_concorda_nao_gera_diagnostico():
    motor = MotorPortugues()
    for frase in ("Eu como.", "Nós comemos."):
        analise = motor.analisar(frase)
        assert "CONCORDANCIA_VERBO_SUJEITO" not in _codigos(analise), frase


def test_sujeito_pronome_discorda_so_em_pessoa():
    # "come" é 3ª pessoa SINGULAR (como "eu" também é singular) -- só a
    # pessoa diverge, não o número.
    motor = MotorPortugues()
    analise = motor.analisar("Eu come.")
    diagnostico = next(d for d in analise.diagnosticos if d.codigo == "CONCORDANCIA_VERBO_SUJEITO")
    assert "pessoa" in diagnostico.mensagem
    assert "número" not in diagnostico.mensagem


def test_sujeito_pronome_discorda_so_em_numero():
    motor = MotorPortugues()
    analise = motor.analisar("Eu estudamos.")
    diagnostico = next(d for d in analise.diagnosticos if d.codigo == "CONCORDANCIA_VERBO_SUJEITO")
    assert "número" in diagnostico.mensagem
    assert "pessoa" not in diagnostico.mensagem


def test_sujeito_pronome_discorda_em_numero_e_pessoa():
    motor = MotorPortugues()
    analise = motor.analisar("Nós come.")
    diagnostico = next(d for d in analise.diagnosticos if d.codigo == "CONCORDANCIA_VERBO_SUJEITO")
    assert "número" in diagnostico.mensagem
    assert "pessoa" in diagnostico.mensagem


# --- RegraCategoriaIncompativel -------------------------------------------

def _dicionario_com_palavra_ambigua() -> Dicionario:
    dicionario = Dicionario()
    dicionario.adicionar(
        EntradaLexical("eu", "eu", ClasseGramatical.PRONOME, pessoa=Pessoa.PRIMEIRA, numero=Numero.SINGULAR)
    )
    dicionario.adicionar(
        EntradaLexical(
            "banco", "banco", ClasseGramatical.SUBSTANTIVO,
            ("Assento comprido.",), genero=Genero.MASCULINO, numero=Numero.SINGULAR,
        )
    )
    dicionario.adicionar(
        EntradaLexical(
            "bancar", "banco", ClasseGramatical.VERBO,
            ("Sustentar financeiramente.",), pessoa=Pessoa.PRIMEIRA, numero=Numero.SINGULAR,
        )
    )
    dicionario.adicionar(
        EntradaLexical("gostar", "gosto", ClasseGramatical.VERBO, pessoa=Pessoa.PRIMEIRA, numero=Numero.SINGULAR)
    )
    return dicionario


def test_categoria_incompativel_sinaliza_verbo_escondido_atras_da_leitura_principal():
    motor = MotorPortugues(dicionario=_dicionario_com_palavra_ambigua())
    analise = motor.analisar("Eu banco.")
    assert "CATEGORIA_INCOMPATIVEL" in _codigos(analise)
    diagnostico = next(d for d in analise.diagnosticos if d.codigo == "CATEGORIA_INCOMPATIVEL")
    assert "banco" in diagnostico.mensagem


def test_categoria_incompativel_nao_dispara_quando_ja_ha_verbo_real_na_frase():
    # "banco" continua ambíguo, mas "gosto" já é um verbo real e claro na
    # frase -- a regra só olha para segmentos sem NENHUM verbo principal.
    motor = MotorPortugues(dicionario=_dicionario_com_palavra_ambigua())
    analise = motor.analisar("Eu gosto de banco.")
    assert "CATEGORIA_INCOMPATIVEL" not in _codigos(analise)


def test_categoria_incompativel_nao_dispara_para_frase_genuinamente_sem_verbo():
    # Nenhuma leitura alternativa esconde um verbo aqui -- não é para
    # marcar toda frase sem verbo, só o caso em que existe uma leitura de
    # verbo real sendo ignorada.
    motor = MotorPortugues()
    analise = motor.analisar("A casa grande.")
    assert "CATEGORIA_INCOMPATIVEL" not in _codigos(analise)
