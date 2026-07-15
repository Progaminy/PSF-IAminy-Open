import json
from importlib.resources import files

import pytest

from lingua_portuguesa.lexico import Dicionario
from lingua_portuguesa.lexico_expansao import (
    _ADJETIVOS,
    _NOMES,
    _PALAVRAS_FUNCIONAIS,
    _VERBOS,
    _forma_adj,
    _forma_nome,
    _verbo,
    entradas_expandidas,
)
from lingua_portuguesa.tipos import ClasseGramatical, Genero


def _formas(lema, definicao="x"):
    return {entrada.forma for entrada in _forma_adj(lema, definicao)}


def _formas_nome(lema, genero=Genero.FEMININO, definicao="x"):
    return {entrada.forma for entrada in _forma_nome(lema, genero, definicao)}


def test_adjetivo_terminado_em_al_pluraliza_em_ais():
    # achado real: a versão anterior gerava "reals"/"naturals" (não
    # existem em português) em vez de "reais"/"naturais".
    assert _formas("real") == {"real", "reais"}
    assert _formas("natural") == {"natural", "naturais"}


def test_adjetivo_terminado_em_o_continua_com_quatro_formas():
    assert _formas("claro") == {"claro", "clara", "claros", "claras"}


def test_entradas_expandidas_nao_gera_plural_invalido_em_al():
    entradas = entradas_expandidas()
    formas_adjetivo_real = {
        e.forma for e in entradas if e.classe == ClasseGramatical.ADJETIVO and e.lema == "real"
    }
    assert "reals" not in formas_adjetivo_real
    assert "reais" in formas_adjetivo_real


def test_substantivo_terminado_em_cao_pluraliza_em_coes():
    # achado real: a versão anterior gerava "intençãos"/"construçãos" (não
    # existem em português) em vez de "intenções"/"construções".
    assert _formas_nome("intenção") == {"intenção", "intenções"}
    assert _formas_nome("construção") == {"construção", "construções"}


def test_substantivo_terminado_em_m_pluraliza_trocando_por_ns():
    # achado real: "item" (já existente) gerava "items" em vez de "itens".
    assert _formas_nome("item", Genero.MASCULINO) == {"item", "itens"}
    assert _formas_nome("som", Genero.MASCULINO) == {"som", "sons"}
    assert _formas_nome("linguagem") == {"linguagem", "linguagens"}


def test_substantivo_terminado_em_r_ou_z_continua_com_es():
    assert _formas_nome("professor", Genero.MASCULINO) == {"professor", "professores"}


def test_entradas_expandidas_nao_gera_plural_invalido_em_cao():
    entradas = entradas_expandidas()
    formas_intencao = {e.forma for e in entradas if e.lema == "intenção"}
    assert "intençãos" not in formas_intencao
    assert "intenções" in formas_intencao


def test_verbo_terminado_em_cer_troca_c_por_c_cedilha_antes_de_a_ou_o():
    # achado real ao adicionar "nascer" como candidato do corpus: a versão
    # anterior gerava "nasco"/"nasca" (não existem em português) em vez de
    # "nasço"/"nasça" -- "c" antes de "a"/"o" precisa virar "ç" pra manter
    # o som /s/ em verbos "-cer"/"-cir".
    formas = {e.forma for e in _verbo("nascer", "x")}
    assert "nasço" in formas
    assert "nasça" in formas
    assert "nasco" not in formas
    assert "nasca" not in formas
    # formas que não ficam antes de "a"/"o" continuam sem alteração.
    assert "nasce" in formas
    assert "nasceu" in formas


def _dicionario_base_sem_palavras_funcionais() -> Dicionario:
    """Léxico vivo (JSON + nomes/adjetivos/verbos), sem `_PALAVRAS_FUNCIONAIS`
    -- baseline real para achar colisão, não um dicionário vazio."""
    caminho = files("lingua_portuguesa.dados").joinpath("lexico_base.json")
    with caminho.open("r", encoding="utf-8") as arquivo:
        base = Dicionario._de_dados(json.load(arquivo))
    for lema, genero, definicao in _NOMES:
        for entrada in _forma_nome(lema, genero, definicao):
            base.adicionar(entrada)
    for lema, definicao in _ADJETIVOS:
        for entrada in _forma_adj(lema, definicao):
            base.adicionar(entrada)
    for infinitivo, definicao in _VERBOS:
        for entrada in _verbo(infinitivo, definicao):
            base.adicionar(entrada)
    return base


def test_palavras_funcionais_nao_duplicam_lexico_ja_existente():
    # achado real: um primeiro lote incluiu "eu"/"e"/"muito"/"do"/"com" etc.
    # que já existiam em lexico_base.json com a mesma classe -- removidos.
    # Este teste vira o guarda permanente contra repetir o mesmo erro.
    base = _dicionario_base_sem_palavras_funcionais()
    colisoes = [
        (entrada.forma, entrada.classe.value)
        for entrada in _PALAVRAS_FUNCIONAIS
        if any(existente.classe == entrada.classe for existente in base.buscar(entrada.forma))
    ]
    assert colisoes == []


def test_palavras_funcionais_sem_duplicata_interna():
    chaves = [(entrada.forma, entrada.classe) for entrada in _PALAVRAS_FUNCIONAIS]
    assert len(chaves) == len(set(chaves))


def test_palavras_funcionais_nao_tem_lema_e_forma_trocados():
    # achado real: um lote de plurais/gênero (teus/tuas/estas/mesma/toda...)
    # foi escrito com EntradaLexical(forma, lema, ...) em vez de
    # EntradaLexical(lema, forma, ...) -- a forma inflectida virava "lema"
    # e o radical base virava "forma", quebrando a busca real ("tuas" não
    # existia no dicionário, "teu" aparecia com forma="teu" quatro vezes).
    # Nenhuma entrada aqui deve ter `forma` mais longa que `lema` sem que
    # `forma` comece pelo prefixo do próprio `lema` OU seja igual a ele --
    # sinal simples e real de troca de argumento.
    # "teu"/"tua" e "seu"/"sua" são exceções genuínas (não compartilham
    # prefixo -- "e" vs "u" na 2ª letra), diferente de este/esta, esse/essa,
    # aquele/aquela (esses sim compartilham prefixo).
    excecoes_irregulares = {
        ("teu", "tua"), ("teu", "tuas"),
        ("seu", "sua"), ("seu", "suas"),
    }
    suspeitas = [
        e for e in _PALAVRAS_FUNCIONAIS
        if e.forma != e.lema
        and not e.forma.startswith(e.lema[:3])
        and (e.lema, e.forma) not in excecoes_irregulares
    ]
    assert suspeitas == []


@pytest.mark.parametrize(
    "forma",
    ["teus", "tuas", "seus", "suas", "nossos", "nossas", "estes", "estas",
     "esses", "essas", "aqueles", "aquelas", "alguma", "alguns", "algumas",
     "nenhuma", "toda", "todos", "todas", "outra", "outros", "outras",
     "mesma", "mesmos", "mesmas", "quais", "quanta", "quantos", "quantas"],
)
def test_forma_flexionada_de_palavra_funcional_esta_no_dicionario(forma):
    assert forma in Dicionario.padrao()


def test_palavra_polissemica_mantem_mais_de_uma_classe():
    dicionario = Dicionario.padrao()
    classes_que = {entrada.classe for entrada in dicionario.buscar("que")}
    assert ClasseGramatical.CONJUNCAO in classes_que
    assert ClasseGramatical.PRONOME in classes_que

    classes_mesmo = {entrada.classe for entrada in dicionario.buscar("mesmo")}
    assert {ClasseGramatical.ADJETIVO, ClasseGramatical.PRONOME, ClasseGramatical.ADVERBIO} <= classes_mesmo


def test_contracao_plural_nova_esta_no_dicionario_vivo():
    dicionario = Dicionario.padrao()
    for forma in ("dos", "das", "nos", "nas", "pelo", "pela", "numa", "nesta"):
        assert forma in dicionario
