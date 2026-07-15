"""Análise morfológica híbrida: léxico explícito e heurísticas transparentes."""
from __future__ import annotations

from .lexico import Dicionario
from .tipos import (
    AnaliseToken,
    ClasseGramatical,
    LeituraMorfologica,
    Numero,
    TipoToken,
    Token,
)


class AnalisadorMorfologico:
    def __init__(self, dicionario: Dicionario) -> None:
        self.dicionario = dicionario

    def analisar(self, tokens: tuple[Token, ...]) -> tuple[AnaliseToken, ...]:
        return tuple(self.analisar_token(token) for token in tokens)

    def analisar_token(self, token: Token) -> AnaliseToken:
        if token.tipo == TipoToken.NUMERO:
            leitura = LeituraMorfologica(
                token, token.normalizado, ClasseGramatical.NUMERAL, origem="tokenizador"
            )
            return AnaliseToken(token, (leitura,))
        if token.tipo != TipoToken.PALAVRA:
            leitura = LeituraMorfologica(
                token, token.normalizado, ClasseGramatical.DESCONHECIDA,
                origem="tokenizador",
            )
            return AnaliseToken(token, (leitura,))

        entradas = self.dicionario.buscar(token.normalizado)
        if entradas:
            leituras = tuple(
                LeituraMorfologica(
                    token=token,
                    lema=entrada.lema,
                    classe=entrada.classe,
                    genero=entrada.genero,
                    numero=entrada.numero,
                    pessoa=entrada.pessoa,
                    definicoes=entrada.definicoes,
                    atributos=entrada.atributos,
                )
                for entrada in entradas
            )
            return AnaliseToken(token, leituras)

        return AnaliseToken(token, (self._inferir(token),))

    @staticmethod
    def _inferir(token: Token) -> LeituraMorfologica:
        palavra = token.normalizado
        classe = ClasseGramatical.DESCONHECIDA
        lema = palavra
        atributos: dict[str, str] = {}
        confianca = 0.20

        if palavra.endswith("mente") and len(palavra) > 6:
            classe = ClasseGramatical.ADVERBIO
            confianca = 0.72
        elif palavra.endswith(("ar", "er", "ir")) and len(palavra) > 3:
            classe = ClasseGramatical.VERBO
            atributos["forma"] = "infinitivo"
            confianca = 0.68
        elif palavra.endswith(("ção", "ções", "dade", "dades", "mento", "mentos")):
            classe = ClasseGramatical.SUBSTANTIVO
            confianca = 0.58

        numero = Numero.PLURAL if palavra.endswith("s") and len(palavra) > 2 else None
        return LeituraMorfologica(
            token=token,
            lema=lema,
            classe=classe,
            numero=numero,
            atributos=atributos,
            confianca=confianca,
            origem="heuristica",
        )
