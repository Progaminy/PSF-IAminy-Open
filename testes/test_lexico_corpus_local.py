import pytest

from lingua_portuguesa.lexico import Dicionario
from lingua_portuguesa.corpus_interno import _caminhos_prosa_ampla
from lingua_portuguesa.lexico_corpus_local import (
    formas_com_evidencia_ampla,
    formas_com_evidencia_canonica,
)


def test_fontes_sao_internas_repetidas_e_deterministicas():
    canonicas = formas_com_evidencia_canonica()
    amplas = formas_com_evidencia_ampla()
    assert canonicas == tuple(sorted(set(canonicas)))
    assert amplas == tuple(sorted(set(amplas)))
    assert set(canonicas) <= set(amplas)


def test_evidencia_repetida_nao_vira_entrada_sem_revisao():
    dicionario = Dicionario.padrao()
    assert "codigo" in formas_com_evidencia_canonica()
    assert "codigo" not in dicionario


def test_erros_conhecidos_nao_entram_por_ocorrencia_isolada():
    dicionario = Dicionario.padrao()
    for erro in (
        "protugues", "intençãos", "items", "reals", "naturals", "asac",
        "portugues", "sto", "hunspell",
    ):
        assert erro not in dicionario


def test_manifesto_exclui_auditorias_de_curriculo_externo():
    nomes = {caminho.name for caminho in _caminhos_prosa_ampla()}
    assert "AUDITORIA_CURRICULO_EXTERNO_400_AULAS.md" not in nomes
    assert "AUDITORIA_CURRICULO_PORTUGUES_1000_AULAS.md" not in nomes


def test_api_json_rejeita_fonte_fora_dos_dados_do_projeto(tmp_path):
    caminho_externo = tmp_path / "lexico.json"
    caminho_externo.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError, match="lingua_portuguesa/dados"):
        Dicionario.de_json(caminho_externo)


def test_metricas_separam_formas_atomicas_de_expressoes():
    dicionario = Dicionario.padrao()
    atomicas = tuple(forma for forma in dicionario.chaves() if " " not in forma)
    expressoes = tuple(forma for forma in dicionario.chaves() if " " in forma)
    assert dicionario.total_formas() == len(atomicas) + len(expressoes)
    assert dicionario.total_formas_atomicas() == len(atomicas)
    assert dicionario.total_expressoes_multipalavra() == len(expressoes)
    assert dicionario.cobertura_atomica() == len(atomicas) * 100 / 600_000
    assert dicionario.total_formas() == 72_824
    assert len(atomicas) == 72_036
    assert len(expressoes) == 788
    assert len(dicionario) == 4_456
    assert len(dicionario.lemas()) == 1_705
    assert dicionario.total_formas_atomicas_com_leitura() == 3_238
    assert dicionario.total_formas_atomicas_apenas_ortograficas() == 68_798
    assert dicionario.cobertura_atomica() == 12.006
