"""Etapa 39 — Política de definitividade PSF.

Regra nova do usuário:
    Tudo que o usuário trouxer deve ser definitivo.

Interpretação PSF:
    Definitivo não significa congelado e impossível de melhorar.
    Definitivo significa que a entrada não é tratada como conversa descartável.
    Ela ganha identidade, estado, rastreio, classe, auditoria e obrigação de
    preservação no projeto.

Sem dependências externas: este módulo só declara estruturas e regras locais.
"""
from __future__ import annotations

from dataclasses import dataclass


ESTADOS_DEFINITIVOS: tuple[str, ...] = (
    "DEFINITIVO_REGISTADO",
    "DEFINITIVO_CLASSIFICADO",
    "DEFINITIVO_COM_RESPOSTA_APROVADA",
    "DEFINITIVO_COM_AULA",
    "DEFINITIVO_EXPANSIVEL",
)

ESTADOS_PROIBIDOS_POR_DEFEITO: tuple[str, ...] = (
    "RASCUNHO",
    "TEMPORARIO",
    "DESCARTAVEL",
    "FRONTEIRA_ABANDONADA",
)


@dataclass(frozen=True, slots=True)
class EntradaDefinitivaPSF:
    id_entrada: str
    origem: str
    tipo: str
    estado: str
    regra: str
    preservacao: str


REGRA_GLOBAL_DEFINITIVIDADE = EntradaDefinitivaPSF(
    id_entrada="REGRA_GLOBAL_ETAPA_39",
    origem="usuario",
    tipo="politica_do_motor",
    estado="DEFINITIVO_EXPANSIVEL",
    regra=(
        "Toda entrada relevante trazida pelo usuário entra no PSF como definitiva: "
        "registada, classificada, auditada e preservada."
    ),
    preservacao=(
        "Pode ser expandida, corrigida e refinada; não pode desaparecer sem ordem explícita."
    ),
)


def estado_eh_definitivo(estado: str) -> bool:
    """Verifica se um estado pertence ao conjunto definitivo permitido."""
    return estado in ESTADOS_DEFINITIVOS


def estado_eh_proibido(estado: str) -> bool:
    """Verifica estados que não podem ser usados por defeito nas entradas do usuário."""
    return estado in ESTADOS_PROIBIDOS_POR_DEFEITO


def normalizar_estado_definitivo(estado: str | None) -> str:
    """Converte ausência ou estado fraco no mínimo definitivo permitido."""
    if not estado:
        return "DEFINITIVO_REGISTADO"
    if estado_eh_proibido(estado):
        return "DEFINITIVO_REGISTADO"
    if estado_eh_definitivo(estado):
        return estado
    return "DEFINITIVO_CLASSIFICADO"


def resumo_politica_definitividade() -> dict[str, object]:
    return {
        "regra_global": REGRA_GLOBAL_DEFINITIVIDADE.regra,
        "estado_da_regra": REGRA_GLOBAL_DEFINITIVIDADE.estado,
        "estados_definitivos": ESTADOS_DEFINITIVOS,
        "estados_proibidos_por_defeito": ESTADOS_PROIBIDOS_POR_DEFEITO,
        "pode_melhorar_sem_deixar_de_ser_definitivo": True,
        "pode_descartar_sem_ordem_do_usuario": False,
    }
