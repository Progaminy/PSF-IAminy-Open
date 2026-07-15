# -*- coding: utf-8 -*-
"""Entrada oficial do Chat Vivo PSF-IAminy.

Este módulo é apenas o orquestrador público. A lógica foi separada em módulos
canônicos para evitar sobreposição histórica e monólito de manutenção.
"""
from __future__ import annotations

from time import perf_counter
from typing import TYPE_CHECKING, Any

from nucleo.chat_auditoria import _auditar
from nucleo.chat_base_canonica import buscar_base_canonica, carregar_base_canonica
from nucleo.chat_rotas import _delegar_dialogo, _responder_unidade
from nucleo.chat_texto import detectar_tom, dividir_perguntas, normalizar
from nucleo.chat_tipos import RespostaChat

if TYPE_CHECKING:
    from ensino.dialogo import MotorDialogo

def responder(
    mensagem: str,
    *,
    id_conversa: str | None = None,
    contexto: dict[str, Any] | None = None,
    contexto_dialogo: dict[str, Any] | None = None,
    estado_psf: dict | None = None,
    reconhecido: bool = False,
    anexos: dict[str, str] | None = None,
    dialogo: "MotorDialogo | None" = None,
    modo: str | None = None,
    registrar: bool = True,
) -> RespostaChat:
    """Responde a uma mensagem pela entrada única do Chat Vivo."""

    inicio = perf_counter()
    id_real = id_conversa or "chat_vivo"
    texto = str(mensagem or "")

    if anexos:
        resposta = _delegar_dialogo(
            texto,
            id_conversa=id_real,
            dialogo=dialogo,
            anexos=anexos,
            estado_psf=estado_psf,
            reconhecido=reconhecido,
            contexto_dialogo=contexto_dialogo,
        )
    else:
        partes = dividir_perguntas(texto)
        if len(partes) > 1:
            respostas: list[RespostaChat] = []
            contexto_atual = contexto if isinstance(contexto, dict) else {}
            estado_atual = estado_psf
            for parte in partes:
                parcial = _responder_unidade(
                    parte,
                    id_conversa=id_real,
                    contexto_chat=contexto_atual,
                    contexto_dialogo=contexto_dialogo,
                    estado_psf=estado_atual,
                    reconhecido=reconhecido,
                    dialogo=dialogo,
                )
                respostas.append(parcial)
                if parcial.contexto_chat:
                    contexto_atual = parcial.contexto_chat
                estado_atual = parcial.estado_psf
            texto_final = "\n\n".join(f"{i}. {r.texto}" for i, r in enumerate(respostas, 1))
            resposta = RespostaChat(
                texto_final,
                "pergunta_multipla",
                detectar_tom(texto),
                min(r.confianca for r in respostas),
                origem="chat_vivo:multipla",
                conhecimento_encontrado=any(r.conhecimento_encontrado for r in respostas),
                lacunas=[lacuna for r in respostas for lacuna in r.lacunas],
                fallback_usado=any(r.fallback_usado for r in respostas),
                deve_melhorar=any(r.deve_melhorar for r in respostas),
                estado_psf=estado_atual,
                contexto_chat=contexto_atual,
            )
        else:
            resposta = _responder_unidade(
                texto,
                id_conversa=id_real,
                contexto_chat=contexto if isinstance(contexto, dict) else {},
                contexto_dialogo=contexto_dialogo if isinstance(contexto_dialogo, dict) else {},
                estado_psf=estado_psf,
                reconhecido=reconhecido,
                dialogo=dialogo,
            )

    if modo:
        resposta.auditoria["modo_solicitado"] = modo
    resposta.auditoria.update(
        {
            "mensagem_do_usuario": texto,
            "tipo_detectado": resposta.intencao,
            "conhecimento_encontrado": resposta.conhecimento_encontrado,
            "etapa_origem": resposta.origem,
            "confianca": resposta.confianca,
            "lacunas": list(resposta.lacunas),
            "fallback_usado": resposta.fallback_usado,
            "deve_melhorar": resposta.deve_melhorar,
        }
    )
    duracao_ms = int((perf_counter() - inicio) * 1000)
    if registrar:
        _auditar(texto, resposta, duracao_ms)
    return resposta


__all__ = [
    "RespostaChat",
    "buscar_base_canonica",
    "carregar_base_canonica",
    "detectar_tom",
    "dividir_perguntas",
    "normalizar",
    "responder",
]
