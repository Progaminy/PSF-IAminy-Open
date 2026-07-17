#!/usr/bin/env python3
"""Avaliação pública pequena do comportamento matemático documentado."""
from __future__ import annotations

import json
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

from matematica import MotorMatematica


CASOS = (
    ("precedência", "2+2*3", {}, "8", "8", "RESOLVIDO_POR_CONSTRUÇÃO_PSF"),
    ("parênteses", "(2+2)*3", {}, "12", "12", "RESOLVIDO_POR_CONSTRUÇÃO_PSF"),
    ("divisão exata racional", "12:5", {}, "2,4", "12/5", "RESOLVIDO_EXATAMENTE_POR_CONSTRUÇÃO_PSF"),
    ("decimal periódico truncado", "1:3", {"casas_decimais": 4}, "0,3333", "1/3", "RESOLVIDO_COM_APROXIMAÇÃO_CONTROLADA_PSF"),
    ("decimal arredondado", "2:3", {"casas_decimais": 3, "modo": "arredondar"}, "0,667", "2/3", "RESOLVIDO_COM_APROXIMAÇÃO_CONTROLADA_PSF"),
    ("divisão por zero", "12:0", {}, None, None, "DIVISÃO_POR_ZERO_NÃO_DEFINIDA_POR_CONSTRUÇÃO_PSF"),
    ("indeterminação zero por zero", "0:0", {}, None, None, "DIVISÃO_POR_ZERO_NÃO_DEFINIDA_POR_CONSTRUÇÃO_PSF"),
)


def main() -> int:
    motor = MotorMatematica()
    resultados = []
    for nome, expressao, kwargs, esperado, exato, estado in CASOS:
        r = motor.calcular(expressao, **kwargs)
        verificacoes = {
            "resultado": r.resultado == esperado,
            "resultado_exato": r.resultado_exato == exato,
            "estado": r.estado == estado,
            "passos": bool(r.passos),
            "justificativas": all(p.justificacao.strip() for p in r.passos),
            "limite_quando_aproximado_ou_indefinido": (
                bool(r.limites)
                if "APROXIMAÇÃO" in r.estado or "ZERO" in r.estado
                else True
            ),
        }
        resultados.append({
            "caso": nome,
            "expressao": expressao,
            "aprovado": all(verificacoes.values()),
            "verificacoes": verificacoes,
            "estado_observado": r.estado,
        })

    imp = lambda a, b: ("implica", a, b)
    prova = motor.provar_finito(("p", imp("p", "q"), imp("q", "r")), "r")
    prova_ok = prova.valida and bool(prova.passos) and "finito" in prova.limite.casefold()
    resumo = {
        "casos_calculo": len(resultados),
        "casos_calculo_aprovados": sum(r["aprovado"] for r in resultados),
        "prova_finita_aprovada": prova_ok,
        "resultado": "APROVADO_NO_ESCOPO_FINITO" if all(r["aprovado"] for r in resultados) and prova_ok else "DIVERGENCIA",
        "casos": resultados,
    }
    print(json.dumps(resumo, ensure_ascii=False, indent=2))
    return 0 if resumo["resultado"] == "APROVADO_NO_ESCOPO_FINITO" else 1


if __name__ == "__main__":
    raise SystemExit(main())

