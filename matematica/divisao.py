"""Divisão reconstruída pelo PSF a partir de quociente, resto e sistema decimal.

Não usa `/`, `//`, `%`, ``decimal`` ou ``fractions`` como fundamento.
As dependências externas podem comparar o resultado depois, nunca produzi-lo.
"""
from __future__ import annotations

from dataclasses import dataclass

from nucleo.aritmetica_escolar_nativa import (
    dividir_exato,
    multiplicar,
    somar,
    subtrair,
    sucessor,
    validar_natural,
)


@dataclass(frozen=True, slots=True)
class QuocienteResto:
    dividendo: int
    divisor: int
    quociente: int
    resto: int
    retiradas: int


@dataclass(frozen=True, slots=True)
class ExpansaoDecimalPSF:
    exato: str
    decimal: str
    casas: int
    modo: str
    terminou: bool
    resto_final: int
    passos: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class RacionalPSF:
    numerador: int
    denominador: int = 1

    def __post_init__(self) -> None:
        validar_natural(self.numerador, "numerador")
        validar_natural(self.denominador, "denominador")
        if self.denominador == 0:
            raise ValueError("denominador zero não define um racional")
        divisor = mdc_por_retirada(self.numerador, self.denominador)
        if divisor > 1:
            object.__setattr__(self, "numerador", dividir_exato(self.numerador, divisor))
            object.__setattr__(self, "denominador", dividir_exato(self.denominador, divisor))

    @property
    def inteiro(self) -> bool:
        return self.denominador == 1

    def exato(self) -> str:
        if self.denominador == 1:
            return str(self.numerador)
        return f"{self.numerador}/{self.denominador}"


def quociente_resto(total: int, partes: int) -> QuocienteResto:
    """Constrói q e r tais que total = partes*q + r, com 0 <= r < partes."""
    validar_natural(total, "total")
    validar_natural(partes, "partes")
    if partes == 0:
        raise ValueError("divisão por zero não é definida")
    restante = total
    quociente = 0
    retiradas = 0
    while restante >= partes:
        restante = subtrair(restante, partes)
        quociente = sucessor(quociente)
        retiradas = sucessor(retiradas)
    return QuocienteResto(total, partes, quociente, restante, retiradas)


def mdc_por_retirada(a: int, b: int) -> int:
    validar_natural(a, "a")
    validar_natural(b, "b")
    if a == 0:
        return b if b != 0 else 1
    if b == 0:
        return a
    x, y = a, b
    while y != 0:
        qr = quociente_resto(x, y)
        x, y = y, qr.resto
    return x


def somar_racionais(a: RacionalPSF, b: RacionalPSF) -> RacionalPSF:
    esquerdo = multiplicar(a.numerador, b.denominador)
    direito = multiplicar(b.numerador, a.denominador)
    return RacionalPSF(somar(esquerdo, direito), multiplicar(a.denominador, b.denominador))


def subtrair_racionais(a: RacionalPSF, b: RacionalPSF) -> RacionalPSF:
    esquerdo = multiplicar(a.numerador, b.denominador)
    direito = multiplicar(b.numerador, a.denominador)
    if direito > esquerdo:
        raise ValueError("resultado negativo ainda não foi solicitado nesta construção natural")
    return RacionalPSF(subtrair(esquerdo, direito), multiplicar(a.denominador, b.denominador))


def multiplicar_racionais(a: RacionalPSF, b: RacionalPSF) -> RacionalPSF:
    return RacionalPSF(
        multiplicar(a.numerador, b.numerador),
        multiplicar(a.denominador, b.denominador),
    )


def dividir_racionais(a: RacionalPSF, b: RacionalPSF) -> RacionalPSF:
    if b.numerador == 0:
        raise ZeroDivisionError(a.exato())
    return RacionalPSF(
        multiplicar(a.numerador, b.denominador),
        multiplicar(a.denominador, b.numerador),
    )


def potencia_racional(base: RacionalPSF, expoente: int) -> RacionalPSF:
    validar_natural(expoente, "expoente")
    resultado = RacionalPSF(1, 1)
    contador = 0
    while contador < expoente:
        resultado = multiplicar_racionais(resultado, base)
        contador = sucessor(contador)
    return resultado


def _incrementar_decimal(inteiro: int, digitos: list[int]) -> tuple[int, list[int]]:
    if not digitos:
        return sucessor(inteiro), digitos
    i = len(digitos) - 1
    while i >= 0:
        novo = sucessor(digitos[i])
        if novo < 10:
            digitos[i] = novo
            return inteiro, digitos
        digitos[i] = 0
        i -= 1
    return sucessor(inteiro), digitos


def expandir_decimal(
    valor: RacionalPSF,
    casas: int | None = None,
    modo: str = "truncar",
    casas_padrao: int = 4,
) -> ExpansaoDecimalPSF:
    """Constrói a expansão decimal por transporte repetido do resto.

    Sem pedido explícito, para quando o resto zera ou em `casas_padrao`.
    Com pedido explícito, preserva exatamente a quantidade pedida, inclusive zeros.
    """
    if casas is not None:
        validar_natural(casas, "casas")
    modo_normalizado = modo.strip().lower()
    if modo_normalizado not in {"truncar", "arredondar"}:
        raise ValueError("modo deve ser 'truncar' ou 'arredondar'")

    inicial = quociente_resto(valor.numerador, valor.denominador)
    inteiro = inicial.quociente
    resto = inicial.resto
    passos: list[str] = [
        f"{valor.numerador} = {valor.denominador} × {inteiro} + {resto}",
        "O resto é transportado para a casa seguinte multiplicando-o por 10.",
    ]

    limite = casas if casas is not None else casas_padrao
    gerar = limite + (1 if modo_normalizado == "arredondar" and casas is not None else 0)
    digitos: list[int] = []
    posicao = 0
    while posicao < gerar:
        if resto == 0:
            if casas is None:
                break
            digitos.append(0)
            passos.append(f"Casa {posicao + 1}: resto zero; acrescenta-se 0 para respeitar a precisão pedida.")
            posicao = sucessor(posicao)
            continue
        transportado = multiplicar(resto, 10)
        qr = quociente_resto(transportado, valor.denominador)
        digitos.append(qr.quociente)
        passos.append(
            f"Casa {posicao + 1}: resto {resto} → {transportado}; "
            f"{transportado} = {valor.denominador} × {qr.quociente} + {qr.resto}."
        )
        resto = qr.resto
        posicao = sucessor(posicao)

    if modo_normalizado == "arredondar" and casas is not None:
        extra = digitos.pop() if digitos else 0
        if extra >= 5:
            inteiro, digitos = _incrementar_decimal(inteiro, digitos)
            passos.append(f"Casa de decisão = {extra}; arredondamento acrescenta uma unidade à última casa mantida.")
        else:
            passos.append(f"Casa de decisão = {extra}; a última casa mantida não é alterada.")

    if casas is not None:
        while len(digitos) < casas:
            digitos.append(0)

    if digitos:
        decimal = f"{inteiro}," + "".join(str(d) for d in digitos)
    else:
        decimal = str(inteiro)

    terminou = resto == 0
    return ExpansaoDecimalPSF(
        exato=valor.exato(),
        decimal=decimal,
        casas=len(digitos),
        modo=modo_normalizado,
        terminou=terminou,
        resto_final=resto,
        passos=tuple(passos),
    )
