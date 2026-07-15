import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.politica_cobertura_total import CoberturaItem, validar_cobertura_total, exigir_cobertura_total, ids_esperados_etapa41
from ensino.cobertura_total import relatorio_etapa41_pela_regra42, politica_etapa42, OBRIGACOES_ETAPA42


def test_ids_esperados_etapa41():
    ids = ids_esperados_etapa41()
    assert len(ids) == 200
    assert ids[0] == "41-I-001"
    assert ids[99] == "41-I-100"
    assert ids[100] == "41-II-001"
    assert ids[-1] == "41-II-100"


def test_cobertura_total_aprova_quando_tudo_existe():
    itens = (
        CoberturaItem("X-001", "teste", "pergunta", "resposta", "aula", "teste individual", "DEFINITIVO_COMPLETO"),
    )
    rel = validar_cobertura_total("teste", 1, itens)
    assert rel.estado == "COBERTURA_TOTAL_APROVADA"
    exigir_cobertura_total(rel)


def test_cobertura_reprova_sem_aula_ou_teste():
    itens = (
        CoberturaItem("X-001", "teste", "pergunta", "resposta", "", "", "DEFINITIVO_INCOMPLETO"),
    )
    rel = validar_cobertura_total("teste", 1, itens)
    assert rel.estado == "COBERTURA_TOTAL_REPROVADA"
    try:
        exigir_cobertura_total(rel)
    except AssertionError:
        pass
    else:
        raise AssertionError("deveria reprovar item sem aula/teste")


def test_etapa41_reclassificada_como_incompleta_pela_regra42():
    rel = relatorio_etapa41_pela_regra42()
    assert rel.total_esperado == 200
    assert rel.estado == "COBERTURA_TOTAL_REPROVADA"
    assert rel.completos < 200
    pol = politica_etapa42()
    assert pol["respostas_representativas_suficientes"] is False
    assert pol["baterias_parciais_aprovadas"] is False


def test_obrigacoes_sao_todas_obrigatorias():
    assert len(OBRIGACOES_ETAPA42) >= 5
    assert all(o.obrigatorio for o in OBRIGACOES_ETAPA42)
    nomes = {o.nome for o in OBRIGACOES_ETAPA42}
    assert {"pergunta", "resposta", "aula", "teste", "pureza"}.issubset(nomes)
