"""Parônimos comuns do português — lista real e sourced, ligada a `paronímia`.

Fecha o gap de "pares de confusão ortográfica didáticos" apontado na
auditoria de currículo: cada par é uma distinção lexical real (dois
significados genuinamente diferentes), não uma coincidência sonora sem
sentido. A maioria dessas palavras é formal/técnica demais para o léxico
pequeno deste projeto (`lingua_portuguesa/dados/lexico_base.json`), então
esta lista não é conferida por busca no `Dicionario` como
`morfemas_afixais.py` fez com prefixos/sufixos — é conhecimento lexical
direto, com a definição de cada palavra do par escrita por extenso, para
que a diferença fique auditável na própria leitura, não escondida atrás
de um rótulo.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ParPeronimo:
    palavras: tuple[str, ...]
    significados: tuple[str, ...]

    def __post_init__(self) -> None:
        if len(self.palavras) != len(self.significados):
            raise ValueError("cada palavra do par precisa de um significado correspondente")
        if len(self.palavras) < 2:
            raise ValueError("um par de parônimos precisa de ao menos duas palavras")


PARONIMOS_COMUNS: tuple[ParPeronimo, ...] = (
    ParPeronimo(("comprimento", "cumprimento"), ("extensão, tamanho", "saudação, ou ato de cumprir")),
    ParPeronimo(("descrição", "discrição"), ("ato de descrever", "qualidade de ser discreto, reservado")),
    ParPeronimo(("estrato", "extrato"), ("camada (geológica, social)", "resumo ou trecho extraído")),
    ParPeronimo(("flagrante", "fragrante"), ("evidente, surpreendido no ato", "que tem fragrância, perfumado")),
    ParPeronimo(("censo", "senso"), ("levantamento estatístico populacional", "faculdade de juízo, percepção")),
    ParPeronimo(("cessão", "sessão", "seção"), ("ato de ceder", "reunião ou intervalo de tempo", "divisão, parte de um todo")),
    ParPeronimo(("concerto", "conserto"), ("espetáculo musical", "reparo")),
    ParPeronimo(("emergir", "imergir"), ("vir à superfície", "mergulhar, afundar-se")),
    ParPeronimo(("eminente", "iminente"), ("notável, ilustre", "prestes a acontecer")),
    ParPeronimo(("ratificar", "retificar"), ("confirmar, validar", "corrigir")),
    ParPeronimo(("trás", "traz", "atrás"), ("usado em locuções como para trás", "forma do verbo trazer", "localização, posição atrás de algo")),
)


def buscar_par(palavra: str) -> ParPeronimo | None:
    """Devolve o grupo de parônimos que contém `palavra`, ou None se não estiver na lista."""
    alvo = palavra.casefold()
    for par in PARONIMOS_COMUNS:
        if alvo in {p.casefold() for p in par.palavras}:
            return par
    return None
