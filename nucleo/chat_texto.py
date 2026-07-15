# -*- coding: utf-8 -*-
"""Normalização, tokenização e leitura simples de intenção/tom."""
from __future__ import annotations

import re
import unicodedata

PALAVRAS_FRACAS = {
    "a",
    "as",
    "ao",
    "aos",
    "da",
    "das",
    "de",
    "do",
    "dos",
    "e",
    "em",
    "eu",
    "me",
    "na",
    "nas",
    "no",
    "nos",
    "o",
    "os",
    "ou",
    "para",
    "por",
    "que",
    "qual",
    "quais",
    "quanto",
    "quantos",
    "se",
    "sao",
    "ser",
    "sobre",
    "sem",
    "te",
    "um",
    "uma",
    "voce",
    "você",
}

PALAVRAS_FRACAS.update({
    "explica",
    "explique",
    "ensina",
    "ensinar",
    "mostra",
    "mostrar",
    "fala",
    "falar",
    "diz",
    "pode",
    "quero",
    "saber",
    "sobre",
    "me",
    "mim",
    "isso",
    "isto",
    "aquele",
    "aquela",
    "conte",
    "conta",
})


def sem_acentos(texto: str) -> str:
    texto = unicodedata.normalize("NFD", str(texto))
    return "".join(ch for ch in texto if unicodedata.category(ch) != "Mn")


def normalizar(texto: str) -> str:
    t = sem_acentos(texto).casefold()
    trocas = {
        "voçe": "voce",
        "vc": "voce",
        "vcs": "voce",
        "ti criou": "te criou",
        "ium": "um",
        "mersa": "merda",
        "engeutei": "injetei",
        "enjectei": "injetei",
        "dispejei": "despejei",
        "adicao": "adicao",
        "subtracao": "subtracao",
        "multiplicacao": "multiplicacao",
        "divisao": "divisao",
        "pk": "porque",
        "pq": "porque",
        "oq": "o que",
    }
    # Trocas por palavra/frase, não por substring solta.
    # A troca global quebrava palavras como "coloque" porque continha "oq" no meio.
    for antigo, novo in trocas.items():
        padrao = r"(?<![a-z0-9])" + re.escape(antigo) + r"(?![a-z0-9])"
        t = re.sub(padrao, novo, t)
    t = re.sub(r"[^a-z0-9?\n .,:;/%+\-×÷]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def tokens_de(texto: str) -> frozenset[str]:
    tokens: list[str] = []
    for token in normalizar(texto).replace("?", " ").split():
        if len(token) < 2 or token in PALAVRAS_FRACAS:
            continue
        tokens.append(token)
    return frozenset(tokens)


def dividir_perguntas(texto: str) -> list[str]:
    bruto = str(texto).strip()
    if not bruto:
        return []
    partes: list[str] = []
    for linha in bruto.splitlines():
        linha = re.sub(r"^\s*\d+\s*[.)-]\s*", "", linha.strip())
        if not linha:
            continue
        if "?" in linha:
            partes.extend(p.strip() for p in re.split(r"(?<=\?)", linha) if p.strip())
        else:
            partes.append(linha)
    return partes or [bruto]


def eh_pergunta(texto: str) -> bool:
    t = normalizar(texto)
    return bool(
        "?" in texto
        or t.startswith(
            (
                "quem ",
                "qual ",
                "quais ",
                "quanto ",
                "quantos ",
                "porque ",
                "por que ",
                "como ",
                "o que ",
                "onde ",
                "quando ",
                "de onde ",
                "tem ",
                "tens ",
            )
        )
    )


def detectar_tom(texto: str) -> str:
    t = normalizar(texto)
    if not t:
        return "vazio"
    if any(p in t for p in ("merda", "porra", "caralho", "filho da puta", "puta")):
        return "raiva"
    if any(p in t for p in ("esta errado", "esta errada", "ta errado", "ta errada", "nao esta certo", "isso esta mal")):
        return "correcao"
    if any(p in t for p in ("era suposto", "ja mandei", "gastando meu tempo", "gastar meu tempo", "despejei")):
        return "reclamacao"
    if any(p in t for p in ("parabens", "é isso mesmo", "e isso mesmo", "boa resposta")):
        return "elogio"
    if any(p in t for p in ("uff que bom", "ufa que bom", "ainda bem", "que bom")):
        return "alivio"
    if "obrigad" in t or "valeu" in t:
        return "agradecimento"
    if re.match(r"^(oi|ola|bom dia|boa tarde|boa noite|e ai|hey)\b", t):
        return "saudacao"
    if eh_pergunta(texto):
        return "pergunta"
    return "conversa_informal"


def detectar_modo(texto: str) -> str:
    t = normalizar(texto)
    if "modo cientista" in t or "por que devo confiar" in t or "fontes confiaveis" in t:
        return "cientista"
    if "passo a passo" in t or "mostra passo" in t or "passos" in t or "desmonte" in t:
        return "passos"
    if "mais simples" in t or "simples" in t:
        return "simples"
    if "exemplo" in t:
        return "exemplo"
    if "exercicio" in t or "exercicios" in t:
        return "exercicios"
    if "nao entendi" in t or "nao percebi" in t or "explica melhor" in t or "explicar melhor" in t:
        return "simples"
    if t in {"continua", "continuar", "continue"} or t.startswith("continua "):
        return "passos"
    if "corrigir resposta" in t or "corrige a resposta" in t:
        return "corrigir"
    return "normal"
