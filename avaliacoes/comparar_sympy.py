#!/usr/bin/env python3
"""Compara resultados PSF com SymPy sem ligar SymPy ao motor de conhecimento.

SymPy é importado somente neste processo de avaliação externa. As expressões
são constantes versionadas abaixo; nenhum texto do utilizador chega a
``sympify``.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

from matematica import MotorMatematica

try:
    import sympy
except ImportError:
    print(json.dumps({"estado": "BLOQUEADO_SYMPY_AUSENTE"}, indent=2))
    raise SystemExit(2)


CASOS = (
    ("2+2*3", "2+2*3", "exato"),
    ("(2+2)*3", "(2+2)*3", "exato"),
    ("12:5", "12/5", "exato"),
    ("1:3", "1/3", "exato"),
    ("2:3", "2/3", "exato"),
    ("12:0", "12/0", "nao_finito"),
    ("0:0", "0/0", "nao_finito"),
)


def main() -> int:
    motor = MotorMatematica()
    resultados = []
    for expressao_psf, expressao_sympy, criterio in CASOS:
        psf = motor.calcular(expressao_psf)
        externo = sympy.sympify(expressao_sympy, evaluate=True)
        if criterio == "exato":
            valor_psf = psf.resultado_exato
            valor_externo = str(externo)
            concorda = valor_psf == valor_externo
        else:
            valor_psf = psf.estado
            valor_externo = str(externo)
            concorda = psf.resultado is None and externo in (sympy.zoo, sympy.nan)
        resultados.append({
            "expressao_psf": expressao_psf,
            "expressao_sympy": expressao_sympy,
            "criterio": criterio,
            "psf": valor_psf,
            "sympy": valor_externo,
            "concorda": concorda,
        })

    divergencias = [r for r in resultados if not r["concorda"]]
    relatorio = {
        "sympy": sympy.__version__,
        "casos": len(resultados),
        "concordancias": len(resultados) - len(divergencias),
        "divergencias": divergencias,
        "estado": "CONCORDANCIA_TOTAL_NA_AMOSTRA" if not divergencias else "DIVERGENCIAS_ENCONTRADAS",
        "resultados": resultados,
    }
    print(json.dumps(relatorio, ensure_ascii=False, indent=2))
    return 0 if not divergencias else 1


if __name__ == "__main__":
    raise SystemExit(main())

