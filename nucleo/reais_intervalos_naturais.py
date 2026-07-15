"""Ponte natural dos racionais assinados para aproximações de reais.

Isto não declara a completude dos reais. Constrói certificados finitos de
intervalos racionais encaixados, que serão a entrada para essa construção.
"""
from __future__ import annotations

from dataclasses import dataclass


def _mdc(a: int, b: int) -> int:
    # Euclides por resto, não por subtração: a lei geradora de raiz quadrada
    # dobra a quantidade de dígitos a cada passo (convergência quadrática de
    # Newton), e gcd(número_grande, 1) por subtração exigiria uma subtração
    # por unidade do número grande — o mesmo tipo de custo O(valor) já
    # documentado em nucleo/reais.py para o núcleo unário. Resto é O(dígitos).
    x, y = abs(a), abs(b)
    if x == 0:
        return y or 1
    if y == 0:
        return x
    while y:
        x, y = y, x % y
    return x


def _dividir_exato_assinado(valor: int, divisor: int) -> int:
    if divisor <= 0:
        raise ValueError("divisor de normalização deve ser positivo")
    sinal = -1 if valor < 0 else 1
    restante = abs(valor)
    # Mesmo motivo do Euclides por resto acima: repartição por subtração
    # repetida é O(quociente); floor division nativa é O(dígitos).
    quociente, sobra = divmod(restante, divisor)
    if sobra != 0:
        raise ValueError("normalização exige repartição exata")
    return sinal * quociente


@dataclass(frozen=True, slots=True)
class RacionalAssinado:
    numerador: int
    denominador: int = 1

    def __post_init__(self) -> None:
        if not isinstance(self.numerador, int) or not isinstance(self.denominador, int):
            raise ValueError("racional exige inteiros")
        if self.denominador == 0:
            raise ValueError("denominador zero não define racional")
        n, d = self.numerador, self.denominador
        if d < 0:
            n, d = -n, -d
        divisor = _mdc(n, d)
        object.__setattr__(self, "numerador", _dividir_exato_assinado(n, divisor))
        object.__setattr__(self, "denominador", _dividir_exato_assinado(d, divisor))

    def menor_ou_igual(self, outro: "RacionalAssinado") -> bool:
        return self.numerador * outro.denominador <= outro.numerador * self.denominador

    def subtrair(self, outro: "RacionalAssinado") -> "RacionalAssinado":
        return RacionalAssinado(
            self.numerador * outro.denominador - outro.numerador * self.denominador,
            self.denominador * outro.denominador,
        )

    def somar(self, outro: "RacionalAssinado") -> "RacionalAssinado":
        return RacionalAssinado(
            self.numerador * outro.denominador + outro.numerador * self.denominador,
            self.denominador * outro.denominador,
        )

    def multiplicar(self, outro: "RacionalAssinado") -> "RacionalAssinado":
        return RacionalAssinado(self.numerador * outro.numerador, self.denominador * outro.denominador)

    def reciproco(self) -> "RacionalAssinado":
        if self.numerador == 0:
            raise ValueError("zero não tem recíproco")
        return RacionalAssinado(self.denominador, self.numerador)


@dataclass(frozen=True, slots=True)
class IntervaloRacional:
    inferior: RacionalAssinado
    superior: RacionalAssinado

    def __post_init__(self) -> None:
        if not self.inferior.menor_ou_igual(self.superior):
            raise ValueError("limite inferior não pode ultrapassar o superior")

    def contem_intervalo(self, outro: "IntervaloRacional") -> bool:
        return self.inferior.menor_ou_igual(outro.inferior) and outro.superior.menor_ou_igual(self.superior)

    def largura(self) -> RacionalAssinado:
        return self.superior.subtrair(self.inferior)


@dataclass(frozen=True, slots=True)
class AproximacaoReal:
    intervalos: tuple[IntervaloRacional, ...]

    def __post_init__(self) -> None:
        if not self.intervalos:
            raise ValueError("aproximação exige pelo menos um intervalo")
        for anterior, atual in zip(self.intervalos, self.intervalos[1:]):
            if not anterior.contem_intervalo(atual):
                raise ValueError("os intervalos devem ser encaixados")
            if not atual.largura().menor_ou_igual(anterior.largura()):
                raise ValueError("a incerteza não pode crescer")

    def certificado_finito(self) -> dict[str, object]:
        return {
            "intervalos": len(self.intervalos),
            "encaixados": True,
            "largura_final": self.intervalos[-1].largura(),
            "estado": "APROXIMAÇÃO_RACIONAL_CERTIFICADA; NÃO É COMPLETUDE DOS REAIS",
        }
