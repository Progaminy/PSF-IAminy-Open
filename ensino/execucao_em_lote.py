"""Execução em lote por fila natural do PSF — Etapa 34.

Regra:
o utilizador pode fazer muitas perguntas numa só entrada. O PSF não mistura
tudo numa resposta caótica. Ele cria um plano, coloca cada pergunta numa fila
e executa uma tarefa de cada vez até terminar.

Este módulo é síncrono: não promete trabalho em segundo plano. Ele representa
como o motor local deve executar agora, no próprio ciclo de chamada.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from nucleo.aritmetica_escolar_nativa import somar


@dataclass(frozen=True, slots=True)
class TarefaLote:
    numero: int
    pergunta: str
    estado: str = "pendente"


@dataclass(frozen=True, slots=True)
class ResultadoLote:
    numero: int
    pergunta: str
    resposta: str
    estado: str = "concluida"


@dataclass(frozen=True, slots=True)
class PlanoLote:
    total: int
    tarefas: tuple[TarefaLote, ...]
    regra: str = "executar uma pergunta por vez, na ordem, até terminar"


class ExecutorLotePSF:
    """Fila sequencial de perguntas.

    A fila não usa concorrência, API externa nem motor paralelo. O plano é
    simples e rastreável: pergunta 1, pergunta 2, pergunta 3, até acabar.
    """

    def __init__(self, perguntas: tuple[str, ...] | list[str]) -> None:
        tarefas: list[TarefaLote] = []
        indice = 0
        for pergunta in perguntas:
            indice = somar(indice, 1)
            tarefas.append(TarefaLote(indice, pergunta))
        self._tarefas = tuple(tarefas)
        self._cursor = 0
        self._resultados: list[ResultadoLote] = []

    def plano(self) -> PlanoLote:
        return PlanoLote(total=len(self._tarefas), tarefas=self._tarefas)

    def terminou(self) -> bool:
        return self._cursor >= len(self._tarefas)

    def executar_proxima(self, resolvedor: Callable[[str], str]) -> ResultadoLote:
        if self.terminou():
            raise StopIteration("não há mais perguntas na fila")
        tarefa = self._tarefas[self._cursor]
        resposta = resolvedor(tarefa.pergunta)
        resultado = ResultadoLote(tarefa.numero, tarefa.pergunta, resposta)
        self._resultados.append(resultado)
        self._cursor = somar(self._cursor, 1)
        return resultado

    def executar_tudo(self, resolvedor: Callable[[str], str]) -> tuple[ResultadoLote, ...]:
        while not self.terminou():
            self.executar_proxima(resolvedor)
        return tuple(self._resultados)

    def progresso(self) -> dict[str, int]:
        concluidas = len(self._resultados)
        total = len(self._tarefas)
        pendentes = total - concluidas
        return {"total": total, "concluidas": concluidas, "pendentes": pendentes}
