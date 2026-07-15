"""Parser aritmético PSF para naturais e racionais não negativos.

A sintaxe é interpretada aqui; o valor é construído pelas operações PSF.
Divisão não exata é preservada como fração e expandida decimalmente passo a passo.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from .divisao import (
    RacionalPSF,
    dividir_racionais,
    expandir_decimal,
    multiplicar_racionais,
    potencia_racional,
    somar_racionais,
    subtrair_racionais,
)
from .tipos import PassoMatematico, ResolucaoMatematica


@dataclass(frozen=True, slots=True)
class Token:
    tipo: str
    valor: str


_PEDIDO_CASAS = re.compile(
    r"\s+com\s+(\d+)\s+casas?(?:\s+decimais?)?(?:\s+(truncad[oa]|arredondad[oa]))?\s*$",
    re.IGNORECASE,
)


def _separar_pedido(texto: str, casas: int | None, modo: str) -> tuple[str, int | None, str]:
    limpo = texto.strip()
    encontrado = _PEDIDO_CASAS.search(limpo)
    if encontrado:
        if casas is None:
            casas = int(encontrado.group(1))
        palavra = (encontrado.group(2) or "").lower()
        if palavra.startswith("arredond"):
            modo = "arredondar"
        elif palavra.startswith("trunc"):
            modo = "truncar"
        limpo = limpo[: encontrado.start()].strip()
    return limpo, casas, modo


def tokenizar(texto: str) -> tuple[Token, ...]:
    tokens: list[Token] = []
    i = 0
    while i < len(texto):
        c = texto[i]
        if c.isspace():
            i += 1
            continue
        if c.isdigit():
            j = i + 1
            while j < len(texto) and texto[j].isdigit():
                j += 1
            tokens.append(Token("NUM", texto[i:j]))
            i = j
            continue
        if c == ":":
            c = "/"
        if c in "+-*/^()":
            tokens.append(Token(c, c))
            i += 1
            continue
        raise ValueError(f"símbolo ainda não suportado: {c!r}")
    tokens.append(Token("FIM", ""))
    return tuple(tokens)


class ParserAritmetico:
    def __init__(self, texto: str) -> None:
        self.texto = texto
        self.tokens = tokenizar(texto)
        self.i = 0
        self.passos: list[PassoMatematico] = []
        self.conhecimento: list[str] = []

    @property
    def atual(self) -> Token:
        return self.tokens[self.i]

    def consumir(self, tipo: str) -> Token:
        if self.atual.tipo != tipo:
            raise ValueError(f"esperado {tipo}, encontrado {self.atual.valor or self.atual.tipo}")
        token = self.atual
        self.i += 1
        return token

    def registrar(self, operacao: str, entrada: str, saida: RacionalPSF, justificacao: str) -> RacionalPSF:
        self.passos.append(PassoMatematico(len(self.passos) + 1, operacao, entrada, saida.exato(), justificacao))
        if operacao not in self.conhecimento:
            self.conhecimento.append(operacao)
        return saida

    def analisar(self) -> RacionalPSF:
        valor = self.expressao()
        if self.atual.tipo != "FIM":
            raise ValueError(f"trecho não consumido: {self.atual.valor}")
        return valor

    def expressao(self) -> RacionalPSF:
        valor = self.termo()
        while self.atual.tipo in ("+", "-"):
            op = self.consumir(self.atual.tipo).tipo
            direito = self.termo()
            anterior = valor
            if op == "+":
                valor = somar_racionais(valor, direito)
                self.registrar("soma racional", f"{anterior.exato()} + {direito.exato()}", valor, "igualar partes e reunir quantidades")
            else:
                valor = subtrair_racionais(valor, direito)
                self.registrar("subtração racional", f"{anterior.exato()} - {direito.exato()}", valor, "igualar partes e retirar sem produzir negativo")
        return valor

    def termo(self) -> RacionalPSF:
        valor = self.potencia()
        while self.atual.tipo in ("*", "/"):
            op = self.consumir(self.atual.tipo).tipo
            direito = self.potencia()
            anterior = valor
            if op == "*":
                valor = multiplicar_racionais(valor, direito)
                self.registrar("multiplicação racional", f"{anterior.exato()} × {direito.exato()}", valor, "combinar numeradores e denominadores construídos")
            else:
                try:
                    valor = dividir_racionais(valor, direito)
                except ZeroDivisionError as erro:
                    raise ZeroDivisionError(str(erro)) from erro
                self.registrar(
                    "divisão racional",
                    f"{anterior.exato()} : {direito.exato()}",
                    valor,
                    "procurar a quantidade que recompõe o dividendo; preservar quociente, resto e fração",
                )
        return valor

    def potencia(self) -> RacionalPSF:
        base = self.primario()
        if self.atual.tipo == "^":
            self.consumir("^")
            expoente_valor = self.potencia()
            if not expoente_valor.inteiro:
                raise ValueError("expoente racional ainda não foi reconstruído neste resolvedor")
            resultado = potencia_racional(base, expoente_valor.numerador)
            self.registrar(
                "potência racional finita",
                f"{base.exato()} ^ {expoente_valor.numerador}",
                resultado,
                "multiplicar a base por si mesma um número natural finito de vezes",
            )
            return resultado
        return base

    def primario(self) -> RacionalPSF:
        if self.atual.tipo == "NUM":
            return RacionalPSF(int(self.consumir("NUM").valor), 1)
        if self.atual.tipo == "(":
            self.consumir("(")
            valor = self.expressao()
            self.consumir(")")
            return valor
        raise ValueError(f"número ou parêntese esperado, encontrado {self.atual.valor or self.atual.tipo}")


def _resposta_divisao_zero(texto: str, parser: ParserAritmetico, dividendo: str) -> ResolucaoMatematica:
    passos = list(parser.passos)
    passos.extend(
        (
            PassoMatematico(
                len(passos) + 1,
                "reconstrução da divisão",
                f"{dividendo} : 0",
                "sem quociente produzido",
                "procurar q tal que 0 × q recomponha o dividendo",
            ),
            PassoMatematico(
                len(passos) + 2,
                "teste da multiplicação por zero",
                "0 × q para qualquer q natural finito",
                "0",
                "somar zero repetidamente conserva zero",
            ),
        )
    )
    return ResolucaoMatematica(
        problema=texto,
        estado="DIVISÃO_POR_ZERO_NÃO_DEFINIDA_POR_CONSTRUÇÃO_PSF",
        resultado=None,
        passos=tuple(passos),
        conhecimento_usado=tuple(dict.fromkeys(parser.conhecimento + ["divisão", "multiplicação por zero"])),
        limites=(
            "Para dividendo não nulo, 0 × q conserva zero e nenhum quociente recompõe o dividendo.",
            "Para 0:0, todo q satisfaz 0 × q = 0; por isso não existe quociente único.",
        ),
        referencia_convencional=(),
        investigacao=(),
    )


def resolver_expressao(
    texto: str,
    casas_decimais: int | None = None,
    modo: str = "truncar",
) -> ResolucaoMatematica:
    expressao, casas_decimais, modo = _separar_pedido(texto, casas_decimais, modo)
    parser = ParserAritmetico(expressao)
    try:
        valor = parser.analisar()
    except ZeroDivisionError as erro:
        return _resposta_divisao_zero(texto, parser, str(erro))
    except (ValueError, TypeError) as erro:
        return ResolucaoMatematica(
            problema=texto,
            estado="NÃO_RESOLVIDO_SEM_FINGIR",
            resultado=None,
            passos=tuple(parser.passos),
            conhecimento_usado=tuple(parser.conhecimento),
            limites=(str(erro), "O resolvedor atual trabalha com racionais não negativos e expressões finitas."),
        )

    if valor.inteiro and casas_decimais is None:
        return ResolucaoMatematica(
            problema=texto,
            estado="RESOLVIDO_POR_CONSTRUÇÃO_PSF",
            resultado=str(valor.numerador),
            resultado_exato=str(valor.numerador),
            passos=tuple(parser.passos),
            conhecimento_usado=tuple(parser.conhecimento),
        )

    expansao = expandir_decimal(valor, casas_decimais, modo)
    passos = list(parser.passos)
    for descricao in expansao.passos:
        passos.append(
            PassoMatematico(
                len(passos) + 1,
                "expansão decimal por resto",
                valor.exato(),
                expansao.decimal,
                descricao,
            )
        )
    estado = "RESOLVIDO_EXATAMENTE_POR_CONSTRUÇÃO_PSF" if expansao.terminou else "RESOLVIDO_COM_APROXIMAÇÃO_CONTROLADA_PSF"
    limites: tuple[str, ...] = ()
    if not expansao.terminou:
        limites = (f"A forma decimal foi {expansao.modo} em {expansao.casas} casas; a fração exata foi preservada.",)
    return ResolucaoMatematica(
        problema=texto,
        estado=estado,
        resultado=expansao.decimal,
        resultado_exato=expansao.exato,
        aproximacao=expansao.decimal,
        casas_decimais=expansao.casas,
        modo_aproximacao=expansao.modo,
        passos=tuple(passos),
        conhecimento_usado=tuple(dict.fromkeys(parser.conhecimento + ["quociente", "resto", "expansão decimal"])),
        limites=limites,
    )
