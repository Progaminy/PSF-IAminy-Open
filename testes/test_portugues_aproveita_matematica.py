"""A Matemática valida e explica Português sem virar fundamento linguístico."""
from __future__ import annotations

import ast
from pathlib import Path

from lingua_portuguesa import MotorPortugues


def test_grafo_de_dependencias_e_auditado_sem_alterar_conhecimento():
    motor = MotorPortugues()
    auditoria = motor.auditar_estrutura_portugues()
    assert auditoria.aprovada
    assert auditoria.conceitos == 1141
    assert auditoria.relacoes_diretas == 2545
    assert auditoria.raizes == ("diferença",)
    assert auditoria.profundidade_maxima > 10


def test_caminho_minimo_usa_dependencias_reais_e_nao_toda_a_lista_anterior():
    motor = MotorPortugues()
    caminho = motor.caminho_minimo_conceito_puro("texto")
    assert caminho[0] == "diferença"
    assert caminho[-1] == "texto"
    assert len(caminho) < motor.caminho_conhecimento_portugues().index("texto") + 1
    assert motor.ponte_matematica.validar_cadeia_de_dependencias(caminho)
    assert motor.caminho_minimo_conceito_puro("conceito inexistente") == ()


def test_gramatica_finita_e_comparador_nao_juiz_total_da_lingua():
    motor = MotorPortugues()
    coberto = motor.comparar_padrao_gramatical_finito("As meninas estudam rapidamente.")
    assert coberto.padrao == ("DET", "N", "V", "ADV")
    assert coberto.coberto

    fora = motor.comparar_padrao_gramatical_finito("Linguagem profundamente azul talvez.")
    assert not fora.coberto
    assert "não é prova de erro" in fora.conclusao


def test_alias_tem_prova_de_reescrita_auditavel():
    motor = MotorPortugues()
    prova = motor.provar_equivalencia_terminologica("variação diatópica")
    assert prova.destino == "variação regional"
    assert prova.passos == ("variação diatópica", "variação regional")
    assert prova.valida

    ausente = motor.provar_equivalencia_terminologica("termo não materializado")
    assert not ausente.valida


def test_ponte_matematica_nao_vira_fundamento_do_conhecimento_puro():
    raiz = Path(__file__).resolve().parents[1]
    puro = ast.parse((raiz / "lingua_portuguesa" / "conhecimento_puro.py").read_text(encoding="utf-8"))
    importados = set()
    for no in ast.walk(puro):
        if isinstance(no, ast.Import):
            importados.update(alias.name.split(".")[0] for alias in no.names)
        elif isinstance(no, ast.ImportFrom) and no.module:
            importados.add(no.module.split(".")[0])
    assert "nucleo" not in importados

    ponte = (raiz / "lingua_portuguesa" / "ponte_matematica.py").read_text(encoding="utf-8")
    assert "não-fundacional" in ponte
    assert "não é prova de erro linguístico" in ponte
