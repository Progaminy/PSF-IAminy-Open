"""Aliteração e assonância — repetição sonora contada de verdade, não citada de memória.

Liga `consoante`/`vogal`/`som`: a definição escolar de aliteração e
assonância descreve o efeito, mas não prova a contagem. Aqui a consoante
ou vogal mais repetida é contada de verdade sobre a sequência de
palavras, e só é aceita como figura quando aparece em pelo menos um
número mínimo de palavras (`minimo`) — sem esse limite, qualquer frase
teria "aliteração" por coincidência de uma letra repetida duas vezes.

Escopo honesto: aliteração aqui é a consoante inicial mais repetida
entre as palavras (não qualquer consoante em qualquer posição);
assonância é a primeira vogal de cada palavra mais repetida (não
análise de sílaba tônica, que exigiria tonicidade automática — já
registrada como fronteira aberta em `sílaba tônica`).
"""
from __future__ import annotations

from collections import Counter
from collections.abc import Sequence

from .normalizacao import sem_acentos

_VOGAIS = frozenset("aeiou")


def detectar_aliteracao(palavras: Sequence[str], minimo: int = 3) -> str | None:
    """Consoante inicial mais repetida entre as palavras, se aparecer em >= minimo delas."""
    iniciais = []
    for palavra in palavras:
        letras = sem_acentos(palavra)
        if letras and letras[0] not in _VOGAIS:
            iniciais.append(letras[0])
    if not iniciais:
        return None
    consoante, quantidade = Counter(iniciais).most_common(1)[0]
    return consoante if quantidade >= minimo else None


def detectar_assonancia(palavras: Sequence[str], minimo: int = 3) -> str | None:
    """Primeira vogal de cada palavra mais repetida, se aparecer em >= minimo delas."""
    primeiras_vogais = []
    for palavra in palavras:
        for letra in sem_acentos(palavra):
            if letra in _VOGAIS:
                primeiras_vogais.append(letra)
                break
    if not primeiras_vogais:
        return None
    vogal, quantidade = Counter(primeiras_vogais).most_common(1)[0]
    return vogal if quantidade >= minimo else None
