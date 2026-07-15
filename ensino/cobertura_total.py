"""Etapa 42 — Aplicação pedagógica da cobertura total.

A regra vale para todas as baterias definitivas: não basta registrar a pergunta;
não basta ter resposta-base; não basta ter aula geral do tópico. Cada pergunta
precisa de resposta, aula e teste individual.
"""
from __future__ import annotations

from dataclasses import dataclass

from nucleo.politica_cobertura_total import CoberturaItem, validar_cobertura_total, RelatorioCoberturaTotal
from nucleo.calculo_integral_avancado import RESPOSTAS_CALCULO_ETAPA_41, TOTAL_PERGUNTAS_ETAPA_41


@dataclass(frozen=True, slots=True)
class ObrigacaoCobertura:
    nome: str
    regra: str
    obrigatorio: bool


OBRIGACOES_ETAPA42: tuple[ObrigacaoCobertura, ...] = (
    ObrigacaoCobertura("pergunta", "preservar a pergunta literal ou a sua forma normalizada", True),
    ObrigacaoCobertura("resposta", "dar resposta matematicamente verificável", True),
    ObrigacaoCobertura("aula", "explicar o conceito em modo direto, detalhado ou passo a passo", True),
    ObrigacaoCobertura("teste", "ter teste individual que valide resposta e tipo de raciocínio", True),
    ObrigacaoCobertura("pureza", "não usar math/numpy/sympy/API/internet como fundamento", True),
)


def itens_parciais_existentes_etapa41() -> tuple[CoberturaItem, ...]:
    """Converte as respostas-base existentes da Etapa 41 em cobertura.

    Importante: cada item antigo tinha resposta, mas não necessariamente aula e
    teste individual. Por isso estes itens são marcados como incompletos. Esta
    função existe para a auditoria mostrar a verdade, não para fingir completude.
    """
    itens: list[CoberturaItem] = []
    for resposta in RESPOSTAS_CALCULO_ETAPA_41:
        itens.append(CoberturaItem(
            id_item=resposta.id_resposta,
            origem="etapa41",
            pergunta=resposta.pergunta_referencia,
            resposta=resposta.resposta_pronta,
            aula="",  # aula individual ainda precisa ser escrita para este item
            teste="",  # teste individual ainda precisa ser escrito para este item
            estado="DEFINITIVO_INCOMPLETO",
        ))
    return tuple(itens)


def relatorio_etapa41_pela_regra42() -> RelatorioCoberturaTotal:
    return validar_cobertura_total("etapa41", TOTAL_PERGUNTAS_ETAPA_41, itens_parciais_existentes_etapa41())


def politica_etapa42() -> dict[str, object]:
    rel = relatorio_etapa41_pela_regra42()
    return {
        "etapa": 42,
        "regra": "toda pergunta definitiva deve ter resposta, aula e teste individual",
        "baterias_parciais_aprovadas": False,
        "respostas_representativas_suficientes": False,
        "estado_etapa41_pela_regra42": rel.estado,
        "completos_etapa41": rel.completos,
        "total_etapa41": rel.total_esperado,
        "acao_obrigatoria": "expandir cada pergunta ate cobertura total",
    }
