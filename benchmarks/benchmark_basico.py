#!/usr/bin/env python3
"""Benchmark pequeno e reproduzível do pacote principal.

Não define limiares de aprovação: recolhe mediana, mínimo, máximo e pico de
memória para permitir comparação entre commits no mesmo ambiente.
"""
from __future__ import annotations

import json
from pathlib import Path
from statistics import median
import subprocess
import sys
from time import perf_counter
import tracemalloc

RAIZ = Path(__file__).resolve().parents[1]
REPETICOES = 7


def medir(funcao, repeticoes: int = REPETICOES) -> dict[str, float]:
    tempos = []
    for _ in range(repeticoes):
        inicio = perf_counter()
        funcao()
        tempos.append((perf_counter() - inicio) * 1000)
    return {
        "mediana_ms": round(median(tempos), 3),
        "minimo_ms": round(min(tempos), 3),
        "maximo_ms": round(max(tempos), 3),
    }


def medir_importacao() -> dict[str, float]:
    tempos = []
    for _ in range(REPETICOES):
        inicio = perf_counter()
        subprocess.run(
            [sys.executable, "-c", "import matematica, lingua_portuguesa, motor"],
            cwd=RAIZ,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        tempos.append((perf_counter() - inicio) * 1000)
    return {
        "mediana_ms": round(median(tempos), 3),
        "minimo_ms": round(min(tempos), 3),
        "maximo_ms": round(max(tempos), 3),
    }


def main() -> int:
    sys.path.insert(0, str(RAIZ))
    tracemalloc.start()

    from lingua_portuguesa import MotorPortugues
    from lingua_portuguesa.corretor import Corretor
    from matematica import MotorMatematica
    from motor.rastreabilidade import referencias_quebradas

    matematica = MotorMatematica()
    portugues = MotorPortugues()
    corretor = Corretor()

    inicio_primeira_correcao = perf_counter()
    corretor.corrigir_texto("Ela nao sabia nda sobre o assunto.")
    primeira_correcao_ms = round((perf_counter() - inicio_primeira_correcao) * 1000, 3)

    resultados = {
        "python": sys.version.split()[0],
        "repeticoes": REPETICOES,
        "importacao_processo_novo": medir_importacao(),
        "matematica_expressao": medir(lambda: matematica.calcular("2+2*3")),
        "matematica_divisao": medir(lambda: matematica.calcular("2:3", casas_decimais=8)),
        "portugues_caminho": medir(lambda: portugues.caminho_minimo_conceito_puro("interpretação")),
        "portugues_primeira_correcao_ms": primeira_correcao_ms,
        "portugues_correcao_aquecida": medir(lambda: corretor.corrigir_texto("Ela nao sabia nda sobre o assunto.")),
        "rastreabilidade_referencias": medir(referencias_quebradas, repeticoes=3),
    }
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    resultados["pico_tracemalloc_mib"] = round(pico / (1024 * 1024), 3)
    print(json.dumps(resultados, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
