"""Localização de recursos na árvore fonte e em instalações por wheel."""
from __future__ import annotations

import os
import sys
from pathlib import Path

RAIZ_CODIGO = Path(__file__).resolve().parents[1]
RAIZ_COMPARTILHADA = Path(sys.prefix) / "share" / "psf-iaminy"


def em_arvore_fonte() -> bool:
    """Indica se o pacote está a correr diretamente num checkout do projeto."""
    return (RAIZ_CODIGO / "pyproject.toml").is_file()


def caminho_documento(nome: str) -> Path:
    """Devolve o documento canónico na fonte ou na área ``share`` instalada."""
    local = RAIZ_CODIGO / nome
    if local.is_file():
        return local
    instalado = RAIZ_COMPARTILHADA / nome
    if instalado.is_file():
        return instalado
    return local


def raiz_dados_usuario() -> Path:
    """Diretório persistente e gravável para dados gerados pelo utilizador.

    ``PSF_IAMINY_DATA_DIR`` permite escolher explicitamente outro local.
    Num checkout preserva os caminhos históricos do projeto; numa instalação
    por wheel evita escrever dentro de ``site-packages``.
    """
    configurado = os.environ.get("PSF_IAMINY_DATA_DIR")
    if configurado:
        return Path(configurado).expanduser().resolve()
    if em_arvore_fonte():
        return RAIZ_CODIGO
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
        return base / "PSF-IAminy"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "PSF-IAminy"
    base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    return base / "psf-iaminy"


def caminho_dado_mutavel(*partes: str) -> Path:
    """Devolve um caminho gravável para conversas, auditorias e históricos."""
    return raiz_dados_usuario().joinpath(*partes)
