# -*- coding: utf-8 -*-
"""Formatação de respostas em texto corrido, para web e terminal.

Substitui o bloco burocrático `Chave: valor.` por uma resposta com abertura,
raciocínio e resultado final em destaque. Usa Markdown leve (**negrito**) e
notação matemática em Unicode simples (², ³, √) -- sem LaTeX: a interface web
(`interface/estatico/`) não tem nenhuma dependência externa (sem CDN, sem
biblioteca de renderização), e o CLI (`psf_chat.py`) imprime texto puro no
terminal. Unicode e `**negrito**` são lidos da mesma forma nos dois lugares
sem precisar de renderizador nenhum -- LaTeX exigiria vendorizar uma
biblioteca só para a web, quebrando essa simetria.
"""
from __future__ import annotations

_ABERTURAS_POR_PADRAO = {
    "hipotenusa_pitagoras": "Vamos calcular a hipotenusa usando o teorema de Pitágoras.",
    "distancia_pontos": "Vamos calcular a distância entre os dois pontos.",
    "area_retangulo": "Vamos calcular a área do retângulo.",
    "percentagem": "Vamos calcular essa porcentagem.",
    "equacao_linear_simples": "Vamos isolar x nessa equação.",
    "fatorar_quadratica": "Vamos fatorar essa expressão quadrática.",
    "velocidade_media": "Vamos calcular a velocidade média.",
    "media_de_lista": "Vamos calcular essa média.",
}

_FONTES_NATURAIS = {
    "resolvedor_exercicios": "Resolvido pelo motor de exercícios do PSF, com o raciocínio reconstruído acima.",
    "motor.matematica:calcular": "Calculado pelo motor de matemática do PSF, com os passos reconstruídos acima.",
}


def _abertura_natural(padrao: str | None) -> str:
    if padrao and padrao in _ABERTURAS_POR_PADRAO:
        return _ABERTURAS_POR_PADRAO[padrao]
    if padrao:
        assunto = padrao.replace("_", " ")
        return f"Vamos resolver isso ({assunto})."
    return "Vamos resolver isso passo a passo."


def _fonte_natural(origem: str, lacunas: list[str] | None = None) -> str:
    base = _FONTES_NATURAIS.get(origem, f"Fonte: {origem}.")
    if lacunas:
        return base + " Atenção: " + "; ".join(lacunas) + "."
    return base


def resposta_natural(
    raciocinio: str,
    resposta_final: str,
    *,
    origem: str,
    padrao: str | None = None,
    lacunas: list[str] | None = None,
) -> str:
    """Monta o texto de resposta em prosa: abertura, raciocínio, resultado final, fonte."""
    partes = [
        _abertura_natural(padrao),
        "",
        raciocinio.strip(),
        "",
        f"**Resposta final:** {resposta_final}",
        "",
        _fonte_natural(origem, lacunas),
    ]
    return "\n".join(partes)
