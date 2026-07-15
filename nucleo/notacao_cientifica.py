"""Notação científica — mantissa × 10^expoente, com 1 ≤ mantissa < 10, exata.

Liga potência (usada em potência modular, ETAPA 27, e em progressão
geométrica, ETAPA 1040) e a decomposição em dígitos (`digitos`, ETAPA
1037): decompor um número inteiro positivo em notação científica é
contar quantas casas o primeiro dígito significativo precisa andar — o
próprio comprimento da lista de dígitos menos um.
"""
from __future__ import annotations

from dataclasses import dataclass

from .contas_armadas import digitos
from .reais_intervalos_naturais import RacionalAssinado

_UM = RacionalAssinado(1)
_DEZ = RacionalAssinado(10)


def _potencia_dez(expoente: int) -> RacionalAssinado:
    """10^expoente, exato, para expoente inteiro positivo, negativo ou zero."""
    resultado = _UM
    for _ in range(abs(expoente)):
        resultado = resultado.multiplicar(_DEZ)
    return resultado if expoente >= 0 else resultado.reciproco()


@dataclass(frozen=True, slots=True)
class NotacaoCientifica:
    """mantissa × 10^expoente, com 1 ≤ mantissa < 10."""

    mantissa: RacionalAssinado
    expoente: int

    def __post_init__(self) -> None:
        if not (_UM.menor_ou_igual(self.mantissa) and self.mantissa.menor_ou_igual(_DEZ) and self.mantissa != _DEZ):
            raise ValueError("mantissa deve satisfazer 1 ≤ mantissa < 10")

    def valor(self) -> RacionalAssinado:
        """Reconstrói o valor original: mantissa × 10^expoente."""
        return self.mantissa.multiplicar(_potencia_dez(self.expoente))


def notacao_cientifica(n: int) -> NotacaoCientifica:
    """Decompõe um número inteiro positivo em notação científica.

    O expoente é a quantidade de dígitos de `n` menos um (quantas casas
    o primeiro dígito precisa andar para virar a mantissa). Conferido
    reconstruindo o valor original a partir da mantissa e do expoente —
    não aceito só por sair da contagem de dígitos.
    """
    if n <= 0:
        raise ValueError("notação científica nesta etapa exige inteiro positivo")
    expoente = len(digitos(n)) - 1
    mantissa = RacionalAssinado(n).multiplicar(_potencia_dez(expoente).reciproco())
    resultado = NotacaoCientifica(mantissa, expoente)
    if resultado.valor() != RacionalAssinado(n):
        raise ValueError("notação científica não reconstrói o valor original")
    return resultado
