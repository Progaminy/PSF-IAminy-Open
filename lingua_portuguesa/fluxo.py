"""Fluxo natural da língua portuguesa.

Este módulo não tenta transformar texto em áudio real. Ele modela uma escada
linguística útil para um motor computacional: unidades sonoras abstratas sem
significado, grafemas, combinações, palavras, sentido, frases, orações e texto.
"""
from __future__ import annotations

import unicodedata

from .normalizacao import normalizar_chave, normalizar_texto, sem_acentos
from .tipos import (
    AnaliseToken,
    ClasseGramatical,
    CombinacaoGrafica,
    Constituinte,
    Diagnostico,
    EstagioLinguistico,
    FluxoLinguistico,
    FraseConstruida,
    Grafema,
    OracaoConstruida,
    PalavraConstruida,
    SomIsolado,
    TipoToken,
    Token,
)


_VOGAIS = set("aeiouáàâãéêíóôõúü")
_PONTUACAO_FRASE = {".", "!", "?"}
_PONTUACAO_NOMES = {
    ".": "ponto final",
    ",": "vírgula",
    ";": "ponto e vírgula",
    ":": "dois pontos",
    "!": "ponto de exclamação",
    "?": "ponto de interrogação",
    "-": "hífen",
    "—": "travessão",
    "(": "parêntese esquerdo",
    ")": "parêntese direito",
    "[": "colchete esquerdo",
    "]": "colchete direito",
    "{": "chave esquerda",
    "}": "chave direita",
    '"': "aspas",
    "'": "apóstrofo",
}
_ACENTOS = {
    "\u0301": "agudo",
    "\u0300": "grave",
    "\u0302": "circunflexo",
    "\u0303": "til",
    "\u0308": "trema",
    "\u0327": "cedilha",
}
_DIGRAFOS = ("ch", "lh", "nh", "rr", "ss", "qu", "gu")


class ConstrutorFluxoNatural:
    """Constrói a progressão som → escrita → palavra → sentido → texto."""

    def construir(
        self,
        texto: str,
        tokens: tuple[Token, ...],
        morfologia: tuple[AnaliseToken, ...],
        diagnosticos: tuple[Diagnostico, ...],
        constituintes: tuple[Constituinte, ...],
    ) -> FluxoLinguistico:
        grafemas = self._grafemas(texto)
        sons = self._sons(grafemas)
        combinacoes, palavras = self._combinacoes_e_palavras(tokens, morfologia)
        frases = self._frases(texto, tokens)
        oracoes = self._oracoes(frases, morfologia, constituintes)
        estagios = self._estagios(sons, grafemas, combinacoes, palavras, frases, oracoes)
        return FluxoLinguistico(
            texto=texto,
            texto_normalizado=normalizar_texto(texto),
            sons=sons,
            grafemas=grafemas,
            combinacoes=combinacoes,
            palavras=palavras,
            frases=frases,
            oracoes=oracoes,
            estagios=estagios,
            diagnosticos=diagnosticos,
            constituintes=constituintes,
        )

    @staticmethod
    def _grafemas(texto: str) -> tuple[Grafema, ...]:
        grafemas: list[Grafema] = []
        for indice, caractere in enumerate(texto):
            base, acento = _base_e_acento(caractere)
            tipo = _tipo_grafema(caractere)
            grafemas.append(
                Grafema(
                    texto=caractere,
                    base=base,
                    tipo=tipo,
                    nome=_nome_grafema(caractere, base, tipo, acento),
                    inicio=indice,
                    fim=indice + 1,
                    acento=acento,
                )
            )
        return tuple(grafemas)

    @staticmethod
    def _sons(grafemas: tuple[Grafema, ...]) -> tuple[SomIsolado, ...]:
        sons: list[SomIsolado] = []
        for grafema in grafemas:
            if grafema.tipo != "letra":
                continue
            simbolo = sem_acentos(grafema.texto).casefold()
            classe = "vogal" if simbolo in "aeiou" else "consoante"
            sons.append(
                SomIsolado(
                    simbolo=simbolo,
                    nome=f"som {classe} abstrato /{simbolo}/",
                    classe=classe,
                    inicio=grafema.inicio,
                    fim=grafema.fim,
                )
            )
        return tuple(sons)

    @staticmethod
    def _combinacoes_e_palavras(
        tokens: tuple[Token, ...],
        morfologia: tuple[AnaliseToken, ...],
    ) -> tuple[tuple[CombinacaoGrafica, ...], tuple[PalavraConstruida, ...]]:
        combinacoes: list[CombinacaoGrafica] = []
        palavras: list[PalavraConstruida] = []
        analises_por_inicio = {analise.token.inicio: analise for analise in morfologia}

        for token in tokens:
            if token.tipo != TipoToken.PALAVRA:
                if token.tipo == TipoToken.PONTUACAO:
                    combinacoes.append(
                        CombinacaoGrafica(
                            texto=token.texto,
                            tipo="pontuacao",
                            inicio=token.inicio,
                            fim=token.fim,
                            componentes=(token.texto,),
                        )
                    )
                continue

            combinacoes.extend(_digrafos(token))
            silabas = _silabificar(token.texto)
            cursor = token.inicio
            for silaba in silabas:
                combinacoes.append(
                    CombinacaoGrafica(
                        texto=silaba,
                        tipo="silaba_aproximada",
                        inicio=cursor,
                        fim=cursor + len(silaba),
                        componentes=tuple(silaba),
                    )
                )
                cursor += len(silaba)

            analise = analises_por_inicio[token.inicio]
            principal = analise.principal
            conhecida = (
                principal.origem == "dicionario"
                and principal.classe != ClasseGramatical.DESCONHECIDA
            )
            palavras.append(
                PalavraConstruida(
                    texto=token.texto,
                    normalizado=token.normalizado,
                    inicio=token.inicio,
                    fim=token.fim,
                    silabas=silabas,
                    conhecida=conhecida,
                    lema=principal.lema if conhecida else None,
                    classe=principal.classe,
                    definicoes=_definicoes(analise),
                )
            )
            combinacoes.append(
                CombinacaoGrafica(
                    texto=token.texto,
                    tipo="palavra",
                    inicio=token.inicio,
                    fim=token.fim,
                    componentes=silabas,
                )
            )
        return tuple(combinacoes), tuple(palavras)

    @staticmethod
    def _frases(texto: str, tokens: tuple[Token, ...]) -> tuple[FraseConstruida, ...]:
        frases: list[FraseConstruida] = []
        atuais: list[Token] = []
        for token in tokens:
            atuais.append(token)
            if token.texto in _PONTUACAO_FRASE:
                frases.append(_frase(texto, atuais))
                atuais = []
        if atuais:
            frases.append(_frase(texto, atuais))
        return tuple(frases)

    @staticmethod
    def _oracoes(
        frases: tuple[FraseConstruida, ...],
        morfologia: tuple[AnaliseToken, ...],
        constituintes: tuple[Constituinte, ...],
    ) -> tuple[OracaoConstruida, ...]:
        oracoes: list[OracaoConstruida] = []
        for frase in frases:
            analises = [
                item
                for item in morfologia
                if frase.inicio <= item.token.inicio and item.token.fim <= frase.fim
            ]
            verbo = next(
                (
                    leitura.token.texto
                    for analise in analises
                    for leitura in analise.leituras
                    if leitura.classe == ClasseGramatical.VERBO
                ),
                None,
            )
            constituintes_da_frase = tuple(
                item
                for item in constituintes
                if frase.inicio <= item.inicio and item.fim <= frase.fim
            )
            oracoes.append(
                OracaoConstruida(
                    texto=frase.texto,
                    inicio=frase.inicio,
                    fim=frase.fim,
                    tem_verbo=verbo is not None,
                    verbo=verbo,
                    constituintes=constituintes_da_frase,
                )
            )
        return tuple(oracoes)

    @staticmethod
    def _estagios(
        sons: tuple[SomIsolado, ...],
        grafemas: tuple[Grafema, ...],
        combinacoes: tuple[CombinacaoGrafica, ...],
        palavras: tuple[PalavraConstruida, ...],
        frases: tuple[FraseConstruida, ...],
        oracoes: tuple[OracaoConstruida, ...],
    ) -> tuple[EstagioLinguistico, ...]:
        sentidos = tuple(palavra for palavra in palavras if palavra.conhecida)
        return (
            EstagioLinguistico(
                1,
                "sons_isolados",
                "Sons abstratos, separados, ainda sem significado lexical.",
                len(sons),
                tuple(som.simbolo for som in sons[:8]),
            ),
            EstagioLinguistico(
                2,
                "grafia",
                "Sons e pausas representados por letras, acentos, espaços e pontuação.",
                len(grafemas),
                tuple(grafema.texto for grafema in grafemas[:8]),
            ),
            EstagioLinguistico(
                3,
                "combinacao",
                "Grafemas agrupados em dígrafos, sílabas aproximadas e palavras-forma.",
                len(combinacoes),
                tuple(item.texto for item in combinacoes[:8]),
            ),
            EstagioLinguistico(
                4,
                "palavras",
                "Palavras como formas reconhecíveis, ainda separáveis do seu sentido.",
                len(palavras),
                tuple(palavra.texto for palavra in palavras[:8]),
            ),
            EstagioLinguistico(
                5,
                "significado",
                "Palavras ligadas a lema, classe gramatical e definições do dicionário.",
                len(sentidos),
                tuple(palavra.lema or palavra.texto for palavra in sentidos[:8]),
            ),
            EstagioLinguistico(
                6,
                "frases_oracoes",
                "Palavras organizadas em frases e orações com verbo e constituintes.",
                len(frases) + len(oracoes),
                tuple(frase.texto for frase in frases[:4]),
            ),
            EstagioLinguistico(
                7,
                "texto_livro",
                "Frases encadeadas em texto; o mesmo modelo pode indexar capítulos e livros.",
                len(frases),
                tuple(frase.texto for frase in frases[:4]),
            ),
            EstagioLinguistico(
                8,
                "gramatica_aplicada",
                "Regras de concordância e construção aplicadas ao estágio textual atual.",
                len(oracoes),
                tuple(oracao.verbo or "sem_verbo" for oracao in oracoes[:8]),
            ),
        )


def _base_e_acento(caractere: str) -> tuple[str, str | None]:
    decomposicao = unicodedata.normalize("NFD", caractere)
    if not decomposicao:
        return caractere, None
    base = decomposicao[0]
    marcas = tuple(_ACENTOS[item] for item in decomposicao[1:] if item in _ACENTOS)
    return base, "+".join(marcas) if marcas else None


def _tipo_grafema(caractere: str) -> str:
    if caractere.isspace():
        return "espaco"
    if caractere.isalpha():
        return "letra"
    if caractere.isdigit():
        return "algarismo"
    if unicodedata.category(caractere).startswith("P"):
        return "pontuacao"
    return "simbolo"


def _nome_grafema(caractere: str, base: str, tipo: str, acento: str | None) -> str:
    if tipo == "letra":
        nome = f"letra {base.casefold()}"
        return f"{nome} com {acento}" if acento else nome
    if tipo == "pontuacao":
        return _PONTUACAO_NOMES.get(caractere, "sinal de pontuação")
    if tipo == "espaco":
        return "espaço"
    if tipo == "algarismo":
        return f"algarismo {caractere}"
    return unicodedata.name(caractere, "símbolo")


def _digrafos(token: Token) -> tuple[CombinacaoGrafica, ...]:
    texto = normalizar_chave(token.texto)
    encontrados: list[CombinacaoGrafica] = []
    for indice in range(max(0, len(texto) - 1)):
        par = texto[indice : indice + 2]
        if par in _DIGRAFOS:
            encontrados.append(
                CombinacaoGrafica(
                    texto=token.texto[indice : indice + 2],
                    tipo="digrafo",
                    inicio=token.inicio + indice,
                    fim=token.inicio + indice + 2,
                    componentes=tuple(token.texto[indice : indice + 2]),
                )
            )
    return tuple(encontrados)


def _silabificar(palavra: str) -> tuple[str, ...]:
    """Silabificação leve: boa para fluxo, não para fonologia normativa final."""
    if len(palavra) <= 3:
        return (palavra,)
    partes: list[str] = []
    atual = ""
    for indice, caractere in enumerate(palavra):
        atual += caractere
        proximo = palavra[indice + 1] if indice + 1 < len(palavra) else ""
        seguinte = palavra[indice + 2] if indice + 2 < len(palavra) else ""
        if not proximo:
            continue
        if _eh_vogal(caractere) and _eh_vogal(proximo):
            partes.append(atual)
            atual = ""
        elif _eh_vogal(caractere) and _eh_consoante(proximo) and _eh_vogal(seguinte):
            partes.append(atual)
            atual = ""
    if atual:
        partes.append(atual)
    return tuple(partes) if partes else (palavra,)


def _eh_vogal(caractere: str) -> bool:
    return caractere.casefold() in _VOGAIS


def _eh_consoante(caractere: str) -> bool:
    return caractere.isalpha() and not _eh_vogal(caractere)


def _definicoes(analise: AnaliseToken) -> tuple[str, ...]:
    definicoes: list[str] = []
    for leitura in analise.leituras:
        for definicao in leitura.definicoes:
            if definicao not in definicoes:
                definicoes.append(definicao)
    return tuple(definicoes)


def _frase(texto: str, tokens: list[Token]) -> FraseConstruida:
    inicio = tokens[0].inicio
    fim = tokens[-1].fim
    return FraseConstruida(
        texto=texto[inicio:fim].strip(),
        inicio=inicio,
        fim=fim,
        tokens=tuple(tokens),
    )
