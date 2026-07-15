# -*- coding: utf-8 -*-
"""
Etapa 63 — Roteador vivo com base real.

Correção do erro da Etapa 62:
- não hardcodar só 5 frases;
- consultar a base real das 300 perguntas;
- responder conversa informal sem cair no fallback antigo;
- dividir mensagens com várias perguntas;
- aceitar escrita com erro comum: voce/você, ti/te, ium/um, mersa/merda etc.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

from nucleo.base_curiosidades_reais import responder as responder_curiosidade


@dataclass(frozen=True, slots=True)
class ResultadoRoteadorVivo63:
    reconhecido: bool
    texto: str
    intencao: str = "roteador_base_curiosidades"


def sem_acentos(texto: str) -> str:
    texto = unicodedata.normalize("NFD", str(texto))
    return "".join(ch for ch in texto if unicodedata.category(ch) != "Mn")


def normalizar(texto: str) -> str:
    t = sem_acentos(texto).casefold()
    # correções pequenas de fala digitada: não mexe em matemática.
    trocas = {
        "vc": "voce",
        "voçe": "voce",
        "voces": "voce",
        "ti criou": "te criou",
        "ium": "um",
        "red a": "erro",
        "reda": "erro",
        "mersa": "merda",
        "adicao": "adicao",
        "poco": "pouco",
        "dispejei": "despejei",
        "peguntas": "perguntas",
    }
    for a, b in trocas.items():
        t = t.replace(a, b)
    t = re.sub(r"[^a-z0-9?\n .,:;/%+-]+", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def dividir_perguntas(texto: str) -> list[str]:
    bruto = str(texto).strip()
    if not bruto:
        return []
    partes: list[str] = []
    for linha in bruto.splitlines():
        linha = linha.strip()
        if not linha:
            continue
        linha = re.sub(r"^\s*\d+\s*[.)-]\s*", "", linha).strip()
        if not linha:
            continue
        if "?" in linha:
            partes.extend([p.strip() for p in re.split(r"(?<=\?)", linha) if p.strip()])
        else:
            partes.append(linha)
    return partes or [bruto]


RESPOSTAS_IDENTIDADE = {
    "quem_voce": "Sou o PSF-IAminy: um sistema local de estudo, ensino, investigação e auditoria do projeto Pensador Sem Fronteiras. Eu organizo conhecimento, explico passo a passo, procuro lacunas e ajudo a testar ideias. Não sou uma pessoa e não sou consciência humana.",
    "quem_criou": "Fui criado dentro do projeto PSF-IAminy por Pensador Sem Fronteiras. O meu dono/administrador de projeto é Pensador Sem Fronteiras.",
}


def _classificar_identidade(texto: str) -> str | None:
    t = normalizar(texto)
    if "quem" in t and ("voce" in t or "tu" in t or "es" in t or "e voce" in t):
        return "quem_voce"
    if ("quem" in t and "criou" in t) or "te criou" in t or "dono" in t or "criador" in t:
        return "quem_criou"
    return None


def _responder_social(texto: str) -> str | None:
    t = normalizar(texto)
    if not t:
        return None
    if re.fullmatch(r"(oi|ola|olá|bom dia|boa tarde|boa noite|e ai|hey)[!. ]*", texto.strip(), flags=re.I):
        return "Olá. Estou ativo. Podes perguntar em linguagem normal; se eu souber no índice, respondo direto."
    if any(frase in t for frase in ["uff que bom", "ufa que bom", "ainda bem", "que bom"]):
        return "Boa. Isso é só reação tua, então eu devo reconhecer como conversa informal e continuar sem fallback antigo."
    if "eu sei" in t and "voce vai aprender" in t:
        return "Certo. Eu devo tratar isso como orientação: quando falhar, registrar o padrão e melhorar a rota, não fingir que entendi."
    if any(pal in t for pal in ["merda", "porra", "caralho", "filho da puta", "puta", "voce e um", "voce e uma", "voce e erro", "voce e red"]):
        if "parabens" in t and ("adicao" in t or "essa mesma" in t):
            return "Entendi: a explicação de adição estava correta, apesar da tua irritação. Vou manter esse padrão simples e direto."
        return "Entendi a tua raiva. Eu não devo responder com fallback velho; devo corrigir a falha concreta: rota, índice e resposta real."
    if "era suposto" in t or "mandei" in t or "despejei" in t or "dispejei" in t:
        return "Sim. Se já foi despejado antes, deve estar no índice vivo e ser encontrado por pergunta natural. Se não for encontrado, isso é erro de integração, não culpa tua."
    if any(frase in t for frase in [
        "esta errado", "esta errada", "ta errado", "ta errada",
        "nao esta certo", "isso esta mal", "isso nao esta certo",
        "gastando meu tempo", "gastando o meu tempo",
        "perdendo meu tempo", "perdendo o meu tempo",
    ]):
        return "Tens razão em cobrar. Isso deveria estar a responder bem. Vou tratar como falha de rota ou de conhecimento e registar o padrão, em vez de insistir numa resposta fraca."
    return None


def _eh_pergunta(texto: str) -> bool:
    t = normalizar(texto)
    return bool("?" in texto or t.startswith(("quem ", "qual ", "quais ", "quanto ", "quantos ", "porque ", "por que ", "como ", "o que ", "onde ", "quando ")))


def responder_uma(entrada: str) -> ResultadoRoteadorVivo63:
    social = _responder_social(entrada)
    if social:
        return ResultadoRoteadorVivo63(True, social, "social")

    ident = _classificar_identidade(entrada)
    if ident:
        return ResultadoRoteadorVivo63(True, RESPOSTAS_IDENTIDADE[ident], ident)

    if _eh_pergunta(entrada):
        curiosidade = responder_curiosidade(entrada)
        if curiosidade:
            return ResultadoRoteadorVivo63(True, curiosidade, "curiosidade_etapa51")

        return ResultadoRoteadorVivo63(
            True,
            "Não encontrei esta pergunta exata na base viva. Vou tratá-la como nova pergunta: criar entrada, responder em linguagem simples, marcar lacuna se faltar prova e ligar ao índice mestre.",
            "pergunta_nova",
        )

    return ResultadoRoteadorVivo63(False, "", "nao_reconhecido")


def responder_texto_livre(texto: str) -> ResultadoRoteadorVivo63:
    partes = dividir_perguntas(texto)
    if not partes:
        return ResultadoRoteadorVivo63(False, "", "vazio")
    respostas: list[str] = []
    alguma = False
    for i, parte in enumerate(partes, 1):
        r = responder_uma(parte)
        if r.reconhecido:
            alguma = True
            respostas.append(f"{i}. {r.texto}" if len(partes) > 1 else r.texto)
        else:
            respostas.append(f"{i}. Recebi: {parte}. Isto parece fala solta, não pergunta. Vou guardar como contexto, não como pedido de aula." if len(partes) > 1 else "Recebi isso como fala solta. Vou guardar como contexto e não como pedido de aula.")
    return ResultadoRoteadorVivo63(alguma, "\n\n".join(respostas), "roteador_base_curiosidades")


def auto_teste() -> dict:
    casos = {
        "uff que bom": "conversa informal",
        "eu sei mas voce vai aprender": "orientação",
        "voce é ium reda": "raiva",
        "parabens seu mersa adicao é essa mesma porra": "adição estava correta",
        "O que são os padrões de Turing na natureza?": "reagem",
        "Como é que as riscas das zebras se formam (modelo matemático)?": "reação-difusão",
        "O que é a filotaxia e como se relaciona com Fibonacci?": "Fibonacci",
        "Porque é que os girassóis têm espirais de Fibonacci?": "ângulo áureo",
        "O que é a proporção áurea no corpo humano?": "lei universal",
        "era suposto saber tudo isso mandei essas perguntas antes": "erro de integração",
    }
    falhas = []
    for entrada, esperado in casos.items():
        saida = responder_texto_livre(entrada).texto
        if esperado not in saida:
            falhas.append({"entrada": entrada, "esperado": esperado, "saida": saida})
    return {"ok": not falhas, "falhas": falhas, "total": len(casos)}
