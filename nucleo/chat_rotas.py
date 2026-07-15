# -*- coding: utf-8 -*-
"""Orquestração das rotas do Chat Vivo."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from motor.identidade_humana import CODIGO_RECONHECIMENTO
from nucleo.base_curiosidades_reais import procurar as procurar_curiosidade
from nucleo.chat_base_canonica import buscar_base_canonica
from nucleo.chat_formatacao import _formatar_curiosidade, _formatar_registro
from nucleo.chat_rotas_auditoria import _responder_auditoria_por_assunto, _responder_operacional_sem_contexto
from nucleo.chat_rotas_basicas import (
    _delegar_dialogo,
    _parece_rota_legada_ensino,
    _pergunta_criador_restrita,
    _responder_criador_reconhecido,
    _responder_criador_restrito,
    _responder_social,
)
from nucleo.chat_rotas_corretor import _responder_corrigir
from nucleo.chat_rotas_materializacao import _responder_comando_adicionar_conhecimento, _responder_fora_escopo_sem_inventar
from nucleo.chat_rotas_resolvedores import _responder_contexto, _responder_indice_total, _responder_nao_encontrado, _responder_resolvedor
from nucleo.chat_texto import detectar_modo, detectar_tom, eh_pergunta
from nucleo.chat_tipos import RespostaChat

if TYPE_CHECKING:
    from ensino.dialogo import MotorDialogo

def _responder_unidade(
    texto: str,
    *,
    id_conversa: str,
    contexto_chat: dict[str, Any] | None,
    contexto_dialogo: dict[str, Any] | None,
    estado_psf: dict | None,
    reconhecido: bool,
    dialogo: "MotorDialogo | None",
) -> RespostaChat:
    tom = detectar_tom(texto)

    materializacao = _responder_comando_adicionar_conhecimento(texto)
    if materializacao is not None:
        return materializacao

    fora_escopo = _responder_fora_escopo_sem_inventar(texto)
    if fora_escopo is not None:
        return fora_escopo

    auditoria_assunto = _responder_auditoria_por_assunto(texto)
    if auditoria_assunto is not None:
        return auditoria_assunto

    operacional = _responder_operacional_sem_contexto(texto, contexto_chat)
    if operacional is not None:
        return operacional

    contextual = _responder_contexto(texto, contexto_chat)
    if contextual is not None:
        return contextual

    if estado_psf is not None or CODIGO_RECONHECIMENTO in texto:
        return _delegar_dialogo(
            texto,
            id_conversa=id_conversa,
            dialogo=dialogo,
            estado_psf=estado_psf,
            reconhecido=reconhecido,
            contexto_dialogo=contexto_dialogo,
        )

    if reconhecido and _pergunta_criador_restrita(texto):
        return _responder_criador_reconhecido(dialogo)
    if _pergunta_criador_restrita(texto):
        return _responder_criador_restrito()

    social = _responder_social(texto, tom)
    if social is not None and not eh_pergunta(texto):
        return social

    modo = detectar_modo(texto)
    if modo == "corrigir":
        return _responder_corrigir(texto, tom)

    t_norm = texto.casefold().strip()
    seguimentos_curtos = {
        "dá outro exemplo", "da outro exemplo", "dê outro exemplo", "de outro exemplo",
        "mais simples", "passo a passo", "mostra passos", "mostra passo",
        "modo cientista", "exercícios", "exercicios", "continua", "continue",
    }
    if modo in {"passos", "simples", "exemplo", "exercicios", "cientista"} and not eh_pergunta(texto) and t_norm in seguimentos_curtos:
        return RespostaChat(
            "Consigo fazer isso, mas preciso de um assunto anterior. Pergunta primeiro sobre um conceito, fórmula, problema ou curiosidade; depois eu simplifico, mostro passos, dou exemplo ou abro o modo cientista.",
            "seguimento_sem_contexto",
            tom,
            78,
            origem="chat_vivo_contexto",
            conhecimento_encontrado=False,
            lacunas=["pedido de modo sem assunto anterior"],
            deve_melhorar=False,
        )

    registro, score = buscar_base_canonica(texto)
    if registro is not None:
        resposta = _formatar_registro(registro, modo, max(score, 82))
        resposta.tom = tom
        return resposta

    curiosidade = procurar_curiosidade(texto)
    if curiosidade is not None:
        resposta = _formatar_curiosidade(curiosidade, modo)
        resposta.tom = tom
        return resposta

    resolvida = _responder_resolvedor(texto)
    if resolvida is not None:
        resolvida.tom = tom
        return resolvida

    if _parece_rota_legada_ensino(texto):
        return _delegar_dialogo(
            texto,
            id_conversa=id_conversa,
            dialogo=dialogo,
            reconhecido=reconhecido,
            contexto_dialogo=contexto_dialogo,
        )

    if eh_pergunta(texto) or modo in {"passos", "simples", "exemplo", "exercicios", "cientista"}:
        por_indice = _responder_indice_total(texto)
        if por_indice is not None:
            por_indice.tom = tom
            return por_indice

    if social is not None:
        return social
    return _responder_nao_encontrado(texto)

