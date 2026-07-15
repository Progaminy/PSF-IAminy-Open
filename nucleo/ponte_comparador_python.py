
"""Etapa 59 — Ponte do cérebro único para o motor Python comparador.

Este módulo não coloca Python dentro do método PSF. Ele apenas permite que o
cérebro único peça comparação externa quando a pergunta exige valor preciso,
teste numérico, métrica empírica ou investigação com cálculo auxiliar.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

try:
    from validacao_externa.motor_calculo_python import (
        calcular_expressao,
        detectar_uso_indevido,
        politica_do_motor,
        validar_metricas_empiricas,
        validar_resposta_numerica,
    )
except Exception:  # pragma: no cover - defesa para ambientes incompletos
    calcular_expressao = None
    detectar_uso_indevido = None
    politica_do_motor = None
    validar_metricas_empiricas = None
    validar_resposta_numerica = None

TIPOS_QUE_PODEM_USAR_COMPARADOR = (
    "calculo_preciso",
    "validacao_numerica",
    "teste_de_formula",
    "comparacao_de_resultado",
    "metrica_empirica",
    "investigacao_auxiliar",
)

TIPOS_QUE_NAO_PODEM_USAR_COMPARADOR_COMO_METODO = (
    "prova_formal",
    "teorema",
    "axioma_psf",
    "definicao_fundamental",
    "problema_em_aberto",
)

def decidir_uso_comparador(tipo_pergunta: str, exige_valor_preciso: bool = False) -> Dict[str, Any]:
    tipo = tipo_pergunta.strip().lower()
    permitido = tipo in TIPOS_QUE_PODEM_USAR_COMPARADOR or exige_valor_preciso
    proibido_como_metodo = tipo in TIPOS_QUE_NAO_PODEM_USAR_COMPARADOR_COMO_METODO
    return {
        "usar_comparador": permitido,
        "usar_como_metodo": False,
        "proibido_como_metodo": proibido_como_metodo,
        "motivo": "valor preciso/teste/comparação" if permitido else "não exige cálculo externo",
        "regra": "comparador auxilia; PSF decide método pela construção nativa",
    }

def validar_com_motor_python(pergunta: str, valor_psf: Any, expressao_python: str, tolerancia: float = 1e-9) -> Dict[str, Any]:
    if validar_resposta_numerica is None:
        return {"estado": "MOTOR_COMPARADOR_INDISPONIVEL"}
    relatorio = validar_resposta_numerica(pergunta, valor_psf, expressao_python, tolerancia)
    return {
        "estado": relatorio.estado,
        "valor_psf": relatorio.valor_psf,
        "valor_python": relatorio.comparacao.valor_python,
        "erro_absoluto": relatorio.comparacao.erro_absoluto,
        "erro_relativo": relatorio.comparacao.erro_relativo,
        "aprovado": relatorio.comparacao.aprovado,
        "passos": relatorio.passos,
        "lacunas": relatorio.lacunas,
        "aviso": relatorio.comparacao.aviso,
    }

def resposta_sobre_comparador() -> str:
    return (
        "Tenho um motor Python comparador separado. Ele usa Python como máquina de calcular "
        "para conferir valores, medir erro e auxiliar testes. Ele não é o método PSF, "
        "não prova teoremas e não substitui a construção nativa."
    )

def auditar_texto_para_dependencia_indevida(texto: str) -> Dict[str, Any]:
    if detectar_uso_indevido is None:
        return {"alertas": ["motor_indisponivel"]}
    alertas = detectar_uso_indevido(texto)
    return {
        "alertas": alertas,
        "aprovado": len(alertas) == 0,
        "regra": "Não transformar comparação Python em prova PSF.",
    }
