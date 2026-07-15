from lingua_portuguesa.candidatos_lexicais import CandidatoLexical, candidatos_lexicais
from lingua_portuguesa.corpus_interno import tokens_do_corpus_amplo
from lingua_portuguesa.lexico import Dicionario


def test_candidatos_nao_estao_no_lexico_atual():
    dicionario = Dicionario.padrao()
    candidatos = candidatos_lexicais()
    assert candidatos, "esperava pelo menos um candidato novo do corpus amplo"
    assert all(candidato.forma not in dicionario for candidato in candidatos)


def test_candidatos_vem_do_corpus_amplo_de_verdade():
    tokens_amplo = set(tokens_do_corpus_amplo())
    candidatos = candidatos_lexicais()
    assert all(candidato.forma in tokens_amplo for candidato in candidatos)


def test_candidatos_ordenados_por_frequencia_decrescente():
    candidatos = candidatos_lexicais()
    frequencias = [candidato.frequencia for candidato in candidatos]
    assert frequencias == sorted(frequencias, reverse=True)


def test_candidatos_desempate_alfabetico_em_frequencia_igual():
    candidatos = candidatos_lexicais()
    mesma_frequencia: dict[int, list[str]] = {}
    for candidato in candidatos:
        mesma_frequencia.setdefault(candidato.frequencia, []).append(candidato.forma)
    for formas in mesma_frequencia.values():
        assert formas == sorted(formas)


def test_candidato_lexical_e_dataclass_imutavel():
    candidato = CandidatoLexical("teste", 3)
    assert candidato.forma == "teste"
    assert candidato.frequencia == 3


def test_candidatos_exclui_autorreferencia_do_projeto():
    # "psf"/"psf-iaminy" aparecem dezenas de vezes em README/RELATÓRIO/
    # PLANO só por serem o nome do projeto -- não são vocabulário comum,
    # não devem poluir o topo da lista de candidatos a lema.
    formas = {candidato.forma for candidato in candidatos_lexicais()}
    assert "psf" not in formas
    assert "psf-iaminy" not in formas
