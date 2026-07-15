"""Tokenizador Unicode com posições no texto original."""
from __future__ import annotations

import re

from .normalizacao import normalizar_chave
from .tipos import TipoToken, Token

_TOKEN = re.compile(
    r"\d+(?:[.,]\d+)*|[^\W\d_]+(?:[-'][^\W\d_]+)*|[^\w\s]",
    re.UNICODE,
)
_PONTUACAO = frozenset(".,;:!?…()[]{}«»“”\"'—–-")


class Tokenizador:
    """Converte texto em tokens, preservando grafia e offsets."""

    def tokenizar(self, texto: str) -> tuple[Token, ...]:
        if not isinstance(texto, str):
            raise TypeError("texto deve ser uma string")
        resultado: list[Token] = []
        for ocorrencia in _TOKEN.finditer(texto):
            valor = ocorrencia.group(0)
            if valor[0].isdigit():
                tipo = TipoToken.NUMERO
            elif valor[0].isalpha():
                tipo = TipoToken.PALAVRA
            elif valor in _PONTUACAO:
                tipo = TipoToken.PONTUACAO
            else:
                tipo = TipoToken.SIMBOLO
            resultado.append(
                Token(
                    texto=valor,
                    normalizado=normalizar_chave(valor),
                    tipo=tipo,
                    inicio=ocorrencia.start(),
                    fim=ocorrencia.end(),
                )
            )
        return tuple(resultado)

