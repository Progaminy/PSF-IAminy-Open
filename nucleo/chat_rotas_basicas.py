# -*- coding: utf-8 -*-
"""Rotas básicas: social, identidade e diálogo legado controlado."""
from __future__ import annotations

import re
from typing import TYPE_CHECKING

from nucleo.chat_texto import detectar_tom, eh_pergunta, normalizar
from nucleo.chat_tipos import RespostaChat

if TYPE_CHECKING:
    from ensino.dialogo import MotorDialogo

def _responder_social(texto: str, tom: str) -> RespostaChat | None:
    if tom == "saudacao":
        return RespostaChat(
            "Olá. Sou o PSF-IAminy. Estou pronto para responder em linguagem normal, procurar no índice local e dizer quando houver lacuna.",
            "saudacao",
            tom,
            90,
            conhecimento_encontrado=True,
        )
    if tom == "agradecimento":
        return RespostaChat("De nada. Continuo daqui contigo quando quiseres.", "agradecimento", tom, 90)
    if tom == "elogio":
        return RespostaChat("Boa. Recebi isso como confirmação positiva e vou manter a rota que funcionou.", "elogio", tom, 88)
    if tom == "alivio":
        return RespostaChat("Boa. Reconheci isso como alívio/satisfação, não como pedido de aula. Seguimos.", "conversa_informal", tom, 88)
    if tom == "raiva":
        return RespostaChat(
            "Entendi que estás frustrado. Tens razão em cobrar resposta real: vou tratar como falha de rota ou conhecimento quando eu não encontrar algo, sem cair em fallback antigo.",
            "raiva_reconhecida",
            tom,
            82,
            deve_melhorar=True,
        )
    if tom == "correcao":
        return RespostaChat(
            "Entendi como pedido de correção. Vou tratar isto como algo a corrigir, não como pedido de aula nem busca aleatória.",
            "pedido_correcao",
            tom,
            82,
            deve_melhorar=True,
            lacunas=["pedido de correção registrado"],
        )
    if tom == "reclamacao":
        return RespostaChat(
            "Tens razão. Isso deve virar correção de rota/conhecimento, não desculpa. Vou registrar o padrão e responder com origem quando o assunto estiver materializado.",
            "reclamacao",
            tom,
            82,
            deve_melhorar=True,
            lacunas=["reclamação do usuário registrada como sinal de melhoria"],
        )
    t = normalizar(texto)
    if "eu sei" in t and "voce vai aprender" in t:
        return RespostaChat(
            "Certo. Recebi isso como encorajamento e orientação de melhoria: quando falhar, devo registrar o padrão e ajustar a rota.",
            "conversa_informal",
            "conversa_informal",
            84,
        )
    return None


def _pergunta_criador_restrita(texto: str) -> bool:
    t = normalizar(texto)
    return "criador" in t or "dono" in t or "administrador" in t


def _responder_criador_restrito() -> RespostaChat:
    return RespostaChat(
        "Informação humana específica sobre criador/dono é restrita sem reconhecimento. A parte pública é: fui criado dentro do projeto PSF-IAminy por Pensador Sem Fronteiras.",
        "identidade_restrita",
        "pergunta",
        90,
        origem="politica_identidade",
        conhecimento_encontrado=True,
        contexto_chat={"ultimo_titulo": "Identidade restrita", "ultima_origem": "política de identidade"},
    )


def _responder_criador_reconhecido(dialogo: "MotorDialogo | None") -> RespostaChat:
    motor = _obter_dialogo(dialogo)
    nome = motor.geral.nome_do_criador()
    if nome:
        texto = f"O meu criador -- a forma humana do Pensador Sem Fronteiras -- chama-se {nome}."
        intencao = "sobre_criador"
        confianca = 92
    else:
        texto = "Já te reconheci, mas ainda não sei o teu nome -- a entrevista não chegou a essa pergunta, ou foi cancelada antes do fim."
        intencao = "sobre_criador_desconhecido"
        confianca = 72
    return RespostaChat(
        texto,
        intencao,
        "pergunta",
        confianca,
        origem="identidade_humana_reconhecida",
        conhecimento_encontrado=bool(nome),
        lacunas=[] if nome else ["nome humano não materializado"],
        contexto_chat={"ultimo_titulo": "Criador reconhecido", "ultima_origem": "identidade_humana"},
    )


def _parece_rota_legada_ensino(texto: str) -> bool:
    t = normalizar(texto)
    return bool(
        re.search(r"\b(?:mat|por)-\d{3}\b", t, flags=re.I)
        or "mapa de matematica" in t
        or "mapa de portugues" in t
        or "proxima aula" in t
        or "proximo pacote" in t
        or t.startswith(("entendi ", "pratiquei ", "exercicios mat", "exercicios por"))
    )


def _obter_dialogo(dialogo: "MotorDialogo | None") -> "MotorDialogo":
    if dialogo is None:
        raise RuntimeError(
            "a rota legada de ensino/identidade requer um MotorDialogo injetado; "
            "ensino.dialogo não existe nesta árvore"
        )
    return dialogo


def _delegar_dialogo(
    texto: str,
    *,
    id_conversa: str,
    dialogo: "MotorDialogo | None",
    anexos: dict[str, str] | None = None,
    estado_psf: dict | None = None,
    reconhecido: bool = False,
    contexto_dialogo: dict | None = None,
) -> RespostaChat:
    motor = _obter_dialogo(dialogo)
    resposta = motor.responder(
        id_conversa,
        texto,
        anexos=anexos,
        estado_psf=estado_psf,
        reconhecido=reconhecido,
        contexto=contexto_dialogo if isinstance(contexto_dialogo, dict) else {},
    )
    return RespostaChat(
        texto=resposta.texto,
        intencao=resposta.intencao,
        tom=detectar_tom(texto),
        confianca=82,
        origem="dialogo_legado_controlado",
        conhecimento_encontrado=True,
        estado_psf=resposta.estado_psf,
        contexto_dialogo=resposta.contexto,
        contexto_chat={"ultimo_titulo": resposta.intencao, "ultima_origem": "MotorDialogo"},
    )


