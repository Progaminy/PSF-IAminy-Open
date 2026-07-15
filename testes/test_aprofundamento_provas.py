import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.aprofundamento_provas import (
    itens_aprofundados_etapa44,
    buscar_aprofundamento,
    relatorio_etapa44,
    exigir_aprofundamento_total_etapa44,
)
from ensino.provas_longas import pacote_completo, aula_completa, prova_longa, resposta_completa


def test_etapa44_tem_200_itens_aprofundados():
    itens = itens_aprofundados_etapa44()
    assert len(itens) == 200
    assert itens[0].id == "44-43-I-001"
    assert itens[-1].id == "44-43-II-100"


def test_todos_tem_resposta_prova_aula_teste_profundos():
    exigir_aprofundamento_total_etapa44()
    assert all(i.completa() for i in itens_aprofundados_etapa44())
    assert all(i.profunda() for i in itens_aprofundados_etapa44())


def test_consulta_por_id_original_e_id_novo():
    a = buscar_aprofundamento("43-I-001")
    b = buscar_aprofundamento("44-43-I-001")
    assert a.id == b.id
    assert "RESPOSTA COMPLETA" in a.resposta_completa
    assert "AULA DETALHADA" in a.aula_detalhada


def test_pacote_completo_tem_todos_campos():
    p = pacote_completo("43-I-001")
    for k in ("resposta_completa", "prova_longa", "aula_detalhada", "aula_passo_a_passo", "teste_profundidade"):
        assert p[k]
    assert p["estado"] == "APROFUNDADO_RESPOSTA_AULA_TESTE"


def test_provas_canonicas_foram_aprofundadas():
    banach = resposta_completa("43-I-001")
    assert "Cauchy" in banach and "ℝⁿ" in banach and "Banach" in banach
    cantor = resposta_completa("43-I-023")
    assert "Cantor" in cantor and "medida 0" in cantor


def test_relatorio_etapa44():
    rel = relatorio_etapa44()
    assert rel["total"] == 200
    assert rel["completos"] == 200
    assert rel["profundos"] == 200
    assert rel["incompletos"] == 0
    assert rel["nao_profundos"] == 0


def test_acesso_ensino():
    assert "AULA PASSO A PASSO" in aula_completa("43-I-001", "passo_a_passo")
    assert "PROVA" in prova_longa("43-I-001") or "DESENVOLVIMENTO" in prova_longa("43-I-001")
