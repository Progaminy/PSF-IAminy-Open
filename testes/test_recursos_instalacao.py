"""Testes dos caminhos de recursos em fonte e em instalação isolada."""
from __future__ import annotations

from pathlib import Path

import psf_iaminy.recursos as recursos


def test_caminho_dado_mutavel_respeita_variavel_de_ambiente(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("PSF_IAMINY_DATA_DIR", str(tmp_path))
    assert recursos.caminho_dado_mutavel("dados", "teste.jsonl") == tmp_path / "dados" / "teste.jsonl"


def test_caminho_documento_encontra_readme_na_arvore_fonte() -> None:
    caminho = recursos.caminho_documento("README.md")
    assert caminho.is_file()
    assert caminho.name == "README.md"


def test_dados_de_identidade_criam_diretorio_pai(monkeypatch, tmp_path: Path) -> None:
    import motor.identidade_humana as identidade

    caminho = tmp_path / "motor" / "identidade_humana.json"
    monkeypatch.setattr(identidade, "CAMINHO_PADRAO", caminho)
    registro = identidade.RegistroIdentidadeHumana()
    registro.registrar_fatos(["teste local"])
    assert caminho.is_file()
