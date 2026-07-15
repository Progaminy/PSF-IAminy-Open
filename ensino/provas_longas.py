"""Acesso às provas longas da Etapa 44."""
from __future__ import annotations
from nucleo.aprofundamento_provas import buscar_aprofundamento, itens_aprofundados_etapa44, relatorio_etapa44


def resposta_completa(id_item: str) -> str:
    return buscar_aprofundamento(id_item).resposta_completa


def prova_longa(id_item: str) -> str:
    return buscar_aprofundamento(id_item).prova_longa


def aula_completa(id_item: str, modo: str = "detalhada") -> str:
    item = buscar_aprofundamento(id_item)
    if modo == "passo_a_passo":
        return item.aula_passo_a_passo
    return item.aula_detalhada


def pacote_completo(id_item: str) -> dict[str, str]:
    item = buscar_aprofundamento(id_item)
    return {
        "id": item.id,
        "origem": item.id_origem,
        "pergunta": item.pergunta,
        "resposta_completa": item.resposta_completa,
        "prova_longa": item.prova_longa,
        "aula_detalhada": item.aula_detalhada,
        "aula_passo_a_passo": item.aula_passo_a_passo,
        "teste_profundidade": item.teste_profundidade,
        "estado": item.estado,
    }


def resumo_etapa44():
    return relatorio_etapa44()
