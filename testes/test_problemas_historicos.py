# -*- coding: utf-8 -*-
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from nucleo.problemas_historicos_resolvidos import PROBLEMAS_HISTORICOS_RESOLVIDOS, validar_cobertura, aula, resposta_curta

def test_total_10():
    assert len(PROBLEMAS_HISTORICOS_RESOLVIDOS) == 10

def test_cobertura_total():
    ok, item, campo = validar_cobertura()
    assert ok, (item, campo)

def test_aulas_tres_modos():
    for p in PROBLEMAS_HISTORICOS_RESOLVIDOS:
        for modo in ("direta", "detalhada", "passo_a_passo"):
            txt = aula(p["id"], modo)
            assert p["nome"].split()[0] in txt or "Tema:" in txt

def test_resposta_curta_existe():
    for p in PROBLEMAS_HISTORICOS_RESOLVIDOS:
        assert len(resposta_curta(p["id"])) > 30

def run():
    test_total_10(); test_cobertura_total(); test_aulas_tres_modos(); test_resposta_curta_existe()
    print("test_problemas_historicos_etapa49: OK")

if __name__ == "__main__":
    run()
