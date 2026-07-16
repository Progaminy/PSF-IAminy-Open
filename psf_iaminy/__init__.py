"""Entrada de pacote do PSF-IAminy: `python -m psf_iaminy` ou `psf-iaminy`.

Este pacote não duplica lógica -- apenas expõe `main.main()` (já a entrada
histórica documentada em COMO_RODAR.md) sob um nome de comando único e
instalável, conforme item 10 do plano de melhorias públicas. `main.py`,
`psf.py`, `psf_chat.py` e `motor_iaminy.py` continuam a existir e a
funcionar como antes.
"""
from __future__ import annotations

__all__ = ["main"]


def main() -> int:
    from main import main as _main

    return _main()
