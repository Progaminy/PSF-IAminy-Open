"""Garante que todo ficheiro test_*.py participa da suíte oficial."""
from __future__ import annotations

import ast
from pathlib import Path


TESTES = Path(__file__).resolve().parent


def _funcoes_pytest(caminho: Path) -> tuple[str, ...]:
    arvore = ast.parse(caminho.read_text(encoding="utf-8"), filename=str(caminho))
    return tuple(
        no.name
        for no in ast.walk(arvore)
        if isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef))
        and no.name.startswith("test_")
    )


def test_nenhum_ficheiro_de_teste_fica_fora_da_coleta_pytest():
    sem_testes = [
        caminho.name
        for caminho in sorted(TESTES.glob("test_*.py"))
        if not _funcoes_pytest(caminho)
    ]
    assert sem_testes == [], (
        "Todo test_*.py deve declarar ao menos uma função test_*; "
        f"ficaram fora da coleta: {sem_testes}"
    )
