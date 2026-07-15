"""Etapa 42 — Política de cobertura total PSF.

Regra recebida do usuário: "Todas devem ter resposta, aula e teste".

Esta etapa corrige a política anterior: uma bateria definitiva não pode ficar
aprovada apenas com respostas-base representativas. A partir da etapa 42,
qualquer item definitivo só é considerado completo se possuir simultaneamente:

1. pergunta preservada;
2. resposta;
3. aula;
4. teste individual;
5. estado de aprovação.

Pureza: este módulo não usa math, numpy, sympy, internet, API externa, LLM
externo ou resolvedor externo. Ele é uma regra de auditoria e validação.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True, slots=True)
class CoberturaItem:
    id_item: str
    origem: str
    pergunta: str
    resposta: str
    aula: str
    teste: str
    estado: str

    def completo(self) -> bool:
        return all((
            bool(self.id_item.strip()),
            bool(self.origem.strip()),
            bool(self.pergunta.strip()),
            bool(self.resposta.strip()),
            bool(self.aula.strip()),
            bool(self.teste.strip()),
            self.estado == "DEFINITIVO_COMPLETO",
        ))


@dataclass(frozen=True, slots=True)
class RelatorioCoberturaTotal:
    origem: str
    total_esperado: int
    total_recebido: int
    completos: int
    incompletos: int
    estado: str
    faltas: tuple[str, ...]


def ids_esperados_etapa41() -> tuple[str, ...]:
    ids: list[str] = []
    for prefixo in ("41-I", "41-II"):
        for numero in range(1, 101):
            ids.append(f"{prefixo}-{numero:03d}")
    return tuple(ids)


def validar_cobertura_total(origem: str, total_esperado: int, itens: Iterable[CoberturaItem]) -> RelatorioCoberturaTotal:
    lista = tuple(itens)
    completos = tuple(item for item in lista if item.completo())
    incompletos = tuple(item.id_item for item in lista if not item.completo())

    faltas: list[str] = []
    if len(lista) != total_esperado:
        faltas.append(f"quantidade: esperado {total_esperado}, recebido {len(lista)}")
    faltas.extend(incompletos)

    estado = "COBERTURA_TOTAL_APROVADA" if not faltas and len(completos) == total_esperado else "COBERTURA_TOTAL_REPROVADA"
    return RelatorioCoberturaTotal(
        origem=origem,
        total_esperado=total_esperado,
        total_recebido=len(lista),
        completos=len(completos),
        incompletos=total_esperado - len(completos) if total_esperado >= len(completos) else len(incompletos),
        estado=estado,
        faltas=tuple(faltas),
    )


def exigir_cobertura_total(relatorio: RelatorioCoberturaTotal) -> None:
    if relatorio.estado != "COBERTURA_TOTAL_APROVADA":
        raise AssertionError(
            "Bateria definitiva incompleta: toda pergunta precisa de resposta, aula e teste. "
            f"Origem={relatorio.origem}; completos={relatorio.completos}/{relatorio.total_esperado}; "
            f"faltas={relatorio.faltas[:10]}"
        )
