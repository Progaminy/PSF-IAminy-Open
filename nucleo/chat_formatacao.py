# -*- coding: utf-8 -*-
"""Formatação de respostas do Chat Vivo."""
from __future__ import annotations

import re
from typing import Any

from nucleo.base_curiosidades_reais import PerguntaCuriosidade
from nucleo.chat_tipos import RegistroCanonico, RespostaChat

def _lista(valor: Any) -> list[str]:
    if isinstance(valor, list):
        return [str(v) for v in valor if str(v).strip()]
    if isinstance(valor, tuple):
        return [str(v) for v in valor if str(v).strip()]
    if valor:
        return [str(valor)]
    return []


def _nivel_confianca(score: int) -> str:
    if score >= 85:
        return "alta"
    if score >= 60:
        return "média"
    return "baixa"


def _fonte_publica_registro(registro: RegistroCanonico) -> str:
    return f"base canônica ({registro.id}: {registro.titulo})"


def _limpar_rastro_tecnico(texto: str) -> str:
    t = str(texto)
    t = re.sub(r"\b[Dd]e que etapa veio\b", "De que fonte veio", t)
    t = re.sub(r"\b[Nn]úmero da etapa\b", "identificador do registro", t)
    t = re.sub(r"\b[Cc]ada etapa\b", "cada registro", t)
    t = re.sub(r"\b[Pp]or etapas\b", "como blocos técnicos", t)
    t = re.sub(r"\b(?:ETAPA|Etapa|etapa)[_\-\s]*\d+[A-Za-z0-9_\-\s/]*", "registro interno", t)
    t = re.sub(r"\b[Ee]tapas\b", "registros internos", t)
    t = re.sub(r"\b[Ee]tapa\b", "registro interno", t)
    t = re.sub(r"\bPSF-K\s*-?\s*\d+\b", "registro interno", t, flags=re.IGNORECASE)
    t = re.sub(r"\b(?:DOSSIE|AUDITORIA|INDICE|REGRA)_registro interno[A-Za-z0-9_\-]*", "registro interno", t)
    return t


def _bloco_final(confianca: int, origem: str, lacunas: list[str]) -> str:
    linhas = [f"Confiança: {_nivel_confianca(confianca)}.", f"Fonte: {origem}."]
    if lacunas:
        linhas.append("Atenção: " + "; ".join(lacunas) + ".")
    return "\n".join(linhas)


def _bloco_cientista(dados: dict[str, Any], confianca: int, lacunas: list[str], fonte: str) -> str:
    estado = dados.get("estado", "conhecido")
    prova = "sim" if dados.get("tem_prova") else "não"
    lacuna = "sim" if dados.get("tem_lacuna") else "não"
    return "\n".join(
        [
            "Modo cientista:",
            f"- tipo: {dados.get('tipo', 'conceito')}",
            f"- estado: {estado}",
            f"- tem prova: {prova}",
            f"- tem lacuna: {lacuna}",
            f"- confiança medida: {_nivel_confianca(confianca)} ({confianca})",
            f"- fonte viva: {fonte}",
            "- rastro técnico antigo: guardado só para auditoria",
            f"- auditoria: {'lacuna detectada' if lacunas else 'sem lacuna crítica nesta resposta'}",
        ]
    )


def _formatar_registro(registro: RegistroCanonico, modo: str, score: int) -> RespostaChat:
    dados = registro.dados
    lacunas = ["esta entrada ainda precisa de aprofundamento"] if dados.get("tem_lacuna") else []
    if modo == "simples":
        corpo = str(dados.get("resposta_curta") or dados.get("resposta_media") or "")
    elif modo == "passos":
        passos = _lista(dados.get("passo_a_passo"))
        corpo = str(dados.get("resposta_media") or dados.get("resposta_curta") or "")
        if passos:
            corpo += "\n\nPasso PSF:\n" + "\n".join(f"{i}. {p}" for i, p in enumerate(passos, 1))
    elif modo == "exemplo":
        exemplos = _lista(dados.get("exemplos"))
        corpo = str(dados.get("resposta_curta") or dados.get("resposta_media") or "")
        if exemplos:
            corpo += "\n\nExemplo:\n" + "\n".join(f"- {e}" for e in exemplos)
    elif modo == "exercicios":
        testes = _lista(dados.get("testes"))
        corpo = str(dados.get("aula_direta") or dados.get("resposta_media") or dados.get("resposta_curta") or "")
        if testes:
            corpo += "\n\nExercícios:\n" + "\n".join(f"{i}. {t}" for i, t in enumerate(testes, 1))
    else:
        corpo = str(dados.get("resposta_media") or dados.get("resposta_curta") or "")
        exemplos = _lista(dados.get("exemplos"))
        if exemplos and modo == "normal":
            corpo += "\n\nExemplo:\n" + exemplos[0]
    fonte_publica = _fonte_publica_registro(registro)
    if modo == "cientista":
        corpo = str(dados.get("resposta_media") or dados.get("resposta_curta") or "") + "\n\n" + _bloco_cientista(dados, score, lacunas, fonte_publica)
    texto = corpo.strip() + "\n\n" + _bloco_final(score, fonte_publica, lacunas)
    return RespostaChat(
        texto=texto,
        intencao=str(dados.get("tipo", "base_canonica")),
        tom="pergunta",
        confianca=score,
        origem=f"base_canonica:{registro.id}",
        conhecimento_encontrado=True,
        lacunas=lacunas,
        contexto_chat={"ultimo_registro_id": registro.id, "ultima_origem": fonte_publica, "ultimo_titulo": registro.titulo},
    )


def _formatar_curiosidade(item: PerguntaCuriosidade, modo: str) -> RespostaChat:
    # Fusão contextual: encontrado não significa útil. Itens sem resposta
    # específica ficam com confiança média e lacuna explícita, para não fingir
    # profundidade.
    if not getattr(item, "resposta_real", True):
        corpo = (
            f"Encontrei esta pergunta registrada na base de curiosidades "
            f"(item {item.numero}: {item.categoria}), mas a resposta ainda está curta — "
            "só existe o registro, não o conteúdo materializado.\n\n"
            f"Pergunta registrada: {item.pergunta}\n\n"
            "Próximo passo PSF: expandir este item para resposta útil com "
            "explicação, exemplo e teste. Não vou fingir profundidade que ainda não existe."
        )
        texto = corpo + "\n\n" + _bloco_final(
            62,
            f"base de curiosidades (item {item.numero}: {item.categoria})",
            ["item registrado sem resposta materializada"],
        )
        return RespostaChat(
            texto=texto,
            intencao="curiosidade_registrada_sem_conteudo",
            tom="pergunta",
            confianca=62,
            origem=f"curiosidade:{item.numero}",
            conhecimento_encontrado=True,
            lacunas=["item registrado sem resposta materializada"],
            deve_melhorar=True,
            contexto_chat={"ultimo_curiosidade_numero": item.numero, "ultima_origem": f"base de curiosidades item {item.numero}", "ultimo_titulo": item.pergunta},
        )
    corpo = item.resposta
    if modo == "passos":
        corpo += "\n\nPasso PSF:\n1. Identificar a pergunta na base de curiosidades.\n2. Responder pela entrada materializada.\n3. Marcar origem e limite."
    elif modo == "exemplo":
        corpo += "\n\nExemplo:\n" + item.aula
    elif modo == "exercicios":
        corpo += "\n\nExercício:\n" + item.teste
    elif modo == "cientista":
        corpo += (
            "\n\nModo cientista:\n"
            f"- tipo: curiosidade\n- estado: conhecido\n- tem prova: não necessariamente\n"
            f"- fonte viva: base de curiosidades (item {item.numero})\n"
            "- rastro técnico antigo: guardado só para auditoria\n"
            "- auditoria: resposta curta materializada"
        )
    texto = corpo + "\n\n" + _bloco_final(88, f"base de curiosidades (item {item.numero}: {item.categoria})", [])
    return RespostaChat(
        texto=texto,
        intencao="curiosidade",
        tom="pergunta",
        confianca=88,
        origem=f"curiosidade:{item.numero}",
        conhecimento_encontrado=True,
        contexto_chat={"ultimo_curiosidade_numero": item.numero, "ultima_origem": f"base de curiosidades item {item.numero}", "ultimo_titulo": item.pergunta},
    )
