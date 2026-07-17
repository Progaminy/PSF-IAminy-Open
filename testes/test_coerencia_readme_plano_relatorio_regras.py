"""Terceiro item pendente desde cedo no README: "criar verificador de
coerência entre README, plano, relatório e regras". Este ficheiro prende
`motor/coerencia.py` e `verificar_integridade.py` como testes reais -- até
agora eram scripts que alguém precisava lembrar de rodar manualmente.
"""
from __future__ import annotations

import ast
import importlib
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import verificar_integridade
from motor.coerencia import (
    arquivos_que_violam_regra_versao_unica,
    divergencia_contagem_testes_entre_documentos,
    divergencias_lexico_no_readme,
    divergencias_readme_vs_auditoria_portugues,
    itens_do_plano_fora_de_ordem,
    modulos_da_interface_falham_ao_importar,
    nomes_de_teste_declarados_sem_ficheiro_real,
)
from motor.rastreabilidade import imports_python_quebrados
from nucleo.chat_rotas_basicas import _obter_dialogo


def test_itens_do_plano_sao_estritamente_sequenciais():
    assert itens_do_plano_fora_de_ordem() == ()


def test_numeros_da_auditoria_estrutural_no_readme_batem_com_o_motor():
    assert divergencias_readme_vs_auditoria_portugues() == ()


def test_numeros_do_lexico_no_readme_batem_com_o_dicionario_vivo():
    assert divergencias_lexico_no_readme() == ()


def test_nenhum_arquivo_viola_a_regra_de_versao_unica():
    assert arquivos_que_violam_regra_versao_unica() == ()


def test_readme_e_como_rodar_declaram_a_mesma_contagem_de_testes():
    assert divergencia_contagem_testes_entre_documentos() == ()


def test_perfis_de_teste_nao_declaram_ficheiro_fantasma():
    assert nomes_de_teste_declarados_sem_ficheiro_real() == ()


def test_pacote_interface_importa_sem_erro():
    assert modulos_da_interface_falham_ao_importar() == ()


def test_verificar_integridade_aprova():
    assert verificar_integridade.main() == 0


def test_imports_python_do_nucleo_resolvem_sem_executar_modulos():
    assert imports_python_quebrados() == []


def test_percurso_de_imports_funciona_sem_ast_trystar(monkeypatch):
    """Python 3.10 não expõe ``ast.TryStar`` (criado no Python 3.11)."""
    import motor.rastreabilidade as rastreabilidade

    monkeypatch.delattr(ast, "TryStar", raising=False)
    modulo_sem_try_star = importlib.reload(rastreabilidade)
    try:
        arvore = ast.parse(
            "try:\n"
            "    import modulo_dentro_do_try\n"
            "except Exception:\n"
            "    import modulo_dentro_do_except\n"
        )
        nomes = {
            apelido.name
            for no in modulo_sem_try_star._imports_fora_de_type_checking(arvore.body)
            for apelido in no.names
        }
        assert nomes == {"modulo_dentro_do_try", "modulo_dentro_do_except"}
        assert modulo_sem_try_star._TIPOS_TRY == (ast.Try,)
    finally:
        monkeypatch.undo()
        importlib.reload(rastreabilidade)


def test_detector_de_imports_aponta_modulo_atributo_e_sintaxe(tmp_path):
    nucleo = tmp_path / "nucleo"
    nucleo.mkdir()
    (nucleo / "__init__.py").write_text("", encoding="utf-8")
    (nucleo / "bom.py").write_text("VALOR = 1\n", encoding="utf-8")
    (nucleo / "perigoso.py").write_text(
        "raise RuntimeError('não pode ser executado pela auditoria')\nEXPORTADO = 1\n",
        encoding="utf-8",
    )
    (nucleo / "consumidor.py").write_text(
        "from typing import TYPE_CHECKING\n"
        "from .bom import VALOR, AUSENTE\n"
        "from .inexistente import X\n"
        "from .perigoso import EXPORTADO\n"
        "if TYPE_CHECKING:\n"
        "    from .apenas_tipagem_inexistente import Tipo\n"
        "def usar_import_tardio():\n"
        "    from .tardio_inexistente import Y\n",
        encoding="utf-8",
    )
    (nucleo / "sintaxe_ruim.py").write_text("def quebrada(:\n", encoding="utf-8")

    falhas = imports_python_quebrados(tmp_path, diretorios=("nucleo",))

    assert len(falhas) == 4
    assert any("atributo 'AUSENTE' inexistente em 'nucleo.bom'" in falha for falha in falhas)
    assert any("módulo 'nucleo.inexistente' inexistente" in falha for falha in falhas)
    assert any("módulo 'nucleo.tardio_inexistente' inexistente" in falha for falha in falhas)
    assert not any("apenas_tipagem_inexistente" in falha for falha in falhas)
    assert any("sintaxe_ruim.py: erro de sintaxe" in falha for falha in falhas)


def test_rota_legada_exige_dialogo_injetado_em_vez_de_import_fantasma():
    dialogo = object()
    assert _obter_dialogo(dialogo) is dialogo
    with pytest.raises(RuntimeError, match="MotorDialogo injetado"):
        _obter_dialogo(None)
