"""Vigilância de desempenho do motor PSF-IAminy.

Este projeto já foi surpreendido por lentidão real várias vezes — não
por bugs de correção, mas porque numerais de Church não têm predecessor
em O(1) (ver reais.py, divisores.py): √2 demora ~4s; SOMA_DIVISORES(220)
nem termina em tempo razoável. Até agora, essas descobertas só
aconteciam quando alguém testava manualmente e reparava. Este ficheiro
faz o motor vigiar isso sozinho: guarda quanto tempo cada
testes/test_*.py levou da ÚLTIMA vez, e avisa quando um ficheiro fica
significativamente mais lento do que estava — não porque um limite
absoluto foi ultrapassado (isso já é o timeout em motor.execucao), mas
porque *mudou* em relação ao que era normal.

Camada meta — só lê/escreve um histórico local em JSON, não faz
matemática.
"""
from __future__ import annotations

import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
HISTORICO = Path(__file__).resolve().parent / "historico_desempenho.json"

# Um ficheiro só é sinalizado se ficar pelo menos este múltiplo mais
# lento que o registo anterior — evita ruído de variação normal de
# máquina (ex.: 0.03s -> 0.05s não é uma regressão real, é ruído).
FATOR_ALERTA = 2.0
# E só se a diferença absoluta também for relevante — evita alarme por
# um teste que já era trivialmente rápido (0.001s -> 0.003s é 3x, mas
# irrelevante na prática).
MINIMO_SEGUNDOS_RELEVANTE = 0.5

# A linha de base antiga pode ter sido criada num modo mais barato
# (ex.: só meta, cache quente, máquina diferente). Se o tempo anterior era
# muito pequeno, qualquer execução real aparece como "10x mais lenta" mesmo
# sem regressão de código. Só comparamos contra histórico que já tinha custo
# minimamente material.
MINIMO_BASELINE_COMPARAVEL = 0.5

# Além do múltiplo, exige diferença absoluta. Isso corta falsos positivos
# como 0.5s -> 1.1s em ambiente diferente.
MINIMO_DIFERENCA_ABSOLUTA = 1.0


def carregar_historico() -> dict[str, float]:
    if HISTORICO.exists():
        return json.loads(HISTORICO.read_text(encoding="utf-8"))
    return {}


def guardar_historico(tempos: dict[str, float]) -> None:
    HISTORICO.write_text(json.dumps(tempos, indent=2, sort_keys=True), encoding="utf-8")


def comparar_e_atualizar(resultados_execucao: dict[str, dict]) -> dict[str, object]:
    """Compara os tempos desta execução contra o histórico guardado.
    Devolve {regressoes: [...], novos: [...], historico_atualizado: {...}}
    e JÁ atualiza o ficheiro de histórico com os tempos desta execução
    (só para os testes que passaram — tempo de um teste que falhou não é
    um dado de desempenho válido)."""
    anterior = carregar_historico()
    regressoes = []
    novos = []
    atualizado = dict(anterior)

    for nome, r in resultados_execucao.items():
        if not r["passou"]:
            continue
        tempo_atual = r["segundos"]
        tempo_anterior = anterior.get(nome)
        if tempo_anterior is None:
            novos.append(nome)
        elif (
            tempo_anterior >= MINIMO_BASELINE_COMPARAVEL
            and tempo_atual >= tempo_anterior * FATOR_ALERTA
            and tempo_atual >= MINIMO_SEGUNDOS_RELEVANTE
            and (tempo_atual - tempo_anterior) >= MINIMO_DIFERENCA_ABSOLUTA
        ):
            regressoes.append(
                f"{nome}: {tempo_anterior:.3f}s -> {tempo_atual:.3f}s "
                f"({tempo_atual / tempo_anterior:.1f}x mais lento)"
            )
        atualizado[nome] = tempo_atual

    guardar_historico(atualizado)
    return {"regressoes": regressoes, "novos": novos, "historico_atualizado": atualizado}
