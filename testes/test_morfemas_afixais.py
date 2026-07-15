from lingua_portuguesa.lexico import Dicionario
from lingua_portuguesa.morfemas_afixais import (
    PREFIXOS_PRODUTIVOS,
    SUFIXOS_PRODUTIVOS,
    reconhecer_prefixo,
    reconhecer_sufixo,
    segmentar_morfemas,
)
from lingua_portuguesa.tipos import ClasseGramatical


def _dicionario() -> Dicionario:
    return Dicionario.padrao()


def test_reconhece_prefixos_com_radical_confirmado_no_lexico():
    d = _dicionario()
    assert reconhecer_prefixo("refazer", d).forma == "re"
    assert reconhecer_prefixo("desfazer", d).forma == "des"
    assert reconhecer_prefixo("infeliz", d).forma == "in"


def test_reconhece_sufixos_com_radical_confirmado_no_lexico():
    d = _dicionario()
    assert reconhecer_sufixo("certamente", d).forma == "mente"
    assert reconhecer_sufixo("claramente", d).forma == "mente"
    assert reconhecer_sufixo("realmente", d).forma == "mente"
    assert reconhecer_sufixo("totalmente", d).forma == "mente"
    assert reconhecer_sufixo("humanamente", d).forma == "mente"
    sufixo_ista = reconhecer_sufixo("naturalista", d)
    assert sufixo_ista.forma == "ista"
    assert sufixo_ista.classe_resultante == ClasseGramatical.ADJETIVO


def test_nao_reconhece_prefixo_quando_radical_nao_existe():
    d = _dicionario()
    # "resto" começa com "re", mas "sto" não é palavra nenhuma.
    assert reconhecer_prefixo("resto", d) is None


def test_nao_reconhece_prefixo_ou_sufixo_em_palavra_sem_afixo_produtivo():
    d = _dicionario()
    assert reconhecer_prefixo("escola", d) is None
    assert reconhecer_sufixo("escola", d) is None


def test_segmentacao_combinada_prefixo_e_sufixo_juntos():
    d = _dicionario()
    segmento = segmentar_morfemas("infelizmente", d)
    assert segmento is not None
    assert segmento.prefixo.forma == "in"
    assert segmento.radical == "feliz"
    assert segmento.sufixo.forma == "mente"


def test_segmentacao_so_prefixo_quando_nao_ha_sufixo_produtivo():
    d = _dicionario()
    segmento = segmentar_morfemas("refazer", d)
    assert segmento is not None
    assert segmento.prefixo.forma == "re"
    assert segmento.radical == "fazer"
    assert segmento.sufixo is None


def test_segmentacao_so_sufixo_quando_nao_ha_prefixo_produtivo():
    d = _dicionario()
    segmento = segmentar_morfemas("totalmente", d)
    assert segmento is not None
    assert segmento.prefixo is None
    assert segmento.radical == "total"
    assert segmento.sufixo.forma == "mente"


def test_segmentacao_declara_none_honesto_em_vez_de_arriscar_corte_errado():
    d = _dicionario()
    # "desumano" perde o h de "humano" ao se juntar — mudança
    # morfofonológica que este módulo não constrói; None é a resposta certa.
    assert segmentar_morfemas("desumano", d) is None
    assert segmentar_morfemas("escola", d) is None


def test_listas_produtivas_sao_reais_e_documentadas():
    assert len(PREFIXOS_PRODUTIVOS) >= 20
    assert len(SUFIXOS_PRODUTIVOS) >= 8
    assert all(p.forma and p.sentido for p in PREFIXOS_PRODUTIVOS)
    assert all(s.forma and s.sentido for s in SUFIXOS_PRODUTIVOS)
    nomes = [p.forma for p in PREFIXOS_PRODUTIVOS]
    assert len(nomes) == len(set(nomes))
