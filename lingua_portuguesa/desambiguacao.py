"""Desambiguação de leitura por gramática real -- Fase 6.2 do plano de
corretor, substituto honesto da técnica 8 (BERT/homónimos em contexto).

`AnaliseToken.principal` é sempre `leituras[0]`, cego a contexto -- quando
uma palavra tem leituras de classes diferentes (ex.: "banco" substantivo
vs "bancar" verbo), a primeira leitura pode ser a errada para a frase.
`escolher_leitura()` usa gramática real (a mesma deteção de verbo ausente
de `gramatica.RegraCategoriaIncompativel`) para escolher, não um
transformer treinado em contexto.

**Limite de escopo declarado, não escondido**: isto resolve homónimo ENTRE
classes diferentes (a mesma forma lida como substantivo ou como verbo).
Não resolve homónimo semântico DENTRO da mesma classe (ex.: "manga" fruta
vs "manga" de camisa, ambos substantivo) -- isso exigiria dado de
regência/seleção verbal que o projeto não tem. Fica registado como decisão
de dado futura e separada, mesmo status da fonte de vocabulário da Fase 3.
"""
from __future__ import annotations

from .tipos import AnaliseToken, ClasseGramatical, LeituraMorfologica


def escolher_leitura(
    analise: AnaliseToken, vizinhanca: tuple[AnaliseToken, ...]
) -> LeituraMorfologica:
    """Escolhe, entre as leituras de `analise`, a que melhor se encaixa no
    contexto sintático dado por `vizinhanca` (o resto da frase, sem
    incluir `analise`)."""
    if len(analise.leituras) <= 1:
        return analise.principal

    ha_verbo_na_vizinhanca = any(
        outro.leituras and outro.principal.classe == ClasseGramatical.VERBO
        for outro in vizinhanca
    )
    leitura_nao_verbo = next(
        (leitura for leitura in analise.leituras if leitura.classe != ClasseGramatical.VERBO), None
    )
    leitura_verbo = next(
        (leitura for leitura in analise.leituras if leitura.classe == ClasseGramatical.VERBO), None
    )

    if ha_verbo_na_vizinhanca and leitura_nao_verbo is not None:
        # a frase já tem verbo em outro token -- a leitura de verbo desta
        # palavra provavelmente está errada aqui.
        return leitura_nao_verbo

    if not ha_verbo_na_vizinhanca and leitura_verbo is not None:
        # a frase parece sem verbo nenhum, e esta palavra pode ser um --
        # é exatamente o caso que RegraCategoriaIncompativel sinaliza.
        return leitura_verbo

    return analise.principal
