"""Progressões aritméticas e geométricas — fórmula fechada conferida pela recorrência.

"Progressões" existia neste projeto só como resposta legada
(`nucleo/conceitos_avancados_puros.py`), sem prova, código ou teste. Este
módulo liga a `nucleo/recorrencias`-style construção já natural do projeto
(uma progressão é a recorrência mais simples possível: somar sempre a
mesma razão, ou multiplicar sempre pela mesma razão) e usa
`RacionalAssinado` (ETAPA 1034/1035) para tudo ficar exato.

Nenhuma fórmula fechada é aceita "porque é conhecida": cada uma é
conferida contra o cálculo termo a termo pela própria recorrência que a
define, e diverge com erro se não bater — mesma disciplina de
`nucleo/contas_armadas.py`.
"""
from __future__ import annotations

from dataclasses import dataclass

from .reais_intervalos_naturais import RacionalAssinado

_METADE = RacionalAssinado(1, 2)


def _validar_indice(n: int, nome: str) -> None:
    if n < 1:
        raise ValueError(f"{nome} deve ser >= 1")


def _potencia(base: RacionalAssinado, expoente: int) -> RacionalAssinado:
    """base^expoente por multiplicação repetida, expoente >= 0."""
    resultado = RacionalAssinado(1)
    k = 0
    while k < expoente:
        resultado = resultado.multiplicar(base)
        k += 1
    return resultado


@dataclass(frozen=True, slots=True)
class ProgressaoAritmetica:
    """a_1, a_2 = a_1+razão, a_3 = a_2+razão, ... — a recorrência mais simples."""

    primeiro_termo: RacionalAssinado
    razao: RacionalAssinado

    def termo_por_recorrencia(self, n: int) -> RacionalAssinado:
        _validar_indice(n, "n")
        termo = self.primeiro_termo
        k = 1
        while k < n:
            termo = termo.somar(self.razao)
            k += 1
        return termo

    def termo_geral(self, n: int) -> RacionalAssinado:
        """a_n = a_1 + (n−1)·razão, conferido contra a recorrência que o define."""
        _validar_indice(n, "n")
        deslocamento = self.razao.multiplicar(RacionalAssinado(n - 1))
        fechado = self.primeiro_termo.somar(deslocamento)
        if fechado != self.termo_por_recorrencia(n):
            raise ValueError("forma fechada divergiu da recorrência que a define")
        return fechado

    def soma_termos(self, n: int) -> RacionalAssinado:
        """S_n = n·(a_1+a_n)/2, conferida contra a soma termo a termo."""
        _validar_indice(n, "n")
        soma_direta = RacionalAssinado(0)
        for k in range(1, n + 1):
            soma_direta = soma_direta.somar(self.termo_por_recorrencia(k))
        formula = (
            self.primeiro_termo.somar(self.termo_geral(n))
            .multiplicar(RacionalAssinado(n))
            .multiplicar(_METADE)
        )
        if formula != soma_direta:
            raise ValueError("fórmula da soma divergiu da soma termo a termo")
        return formula


@dataclass(frozen=True, slots=True)
class ProgressaoGeometrica:
    """a_1, a_2 = a_1×razão, a_3 = a_2×razão, ... — recorrência multiplicativa."""

    primeiro_termo: RacionalAssinado
    razao: RacionalAssinado

    def __post_init__(self) -> None:
        if self.razao.numerador == 0:
            raise ValueError("razão de progressão geométrica não pode ser nula")

    def termo_geral(self, n: int) -> RacionalAssinado:
        """a_n = a_1 × razão^(n−1), pela mesma recorrência multiplicativa."""
        _validar_indice(n, "n")
        termo = self.primeiro_termo
        k = 1
        while k < n:
            termo = termo.multiplicar(self.razao)
            k += 1
        return termo

    def soma_termos(self, n: int) -> RacionalAssinado:
        """S_n = a_1×(razão^n−1)/(razão−1), conferida contra a soma termo a termo.

        Quando razão = 1, a progressão é constante e a soma é a_1×n.
        """
        _validar_indice(n, "n")
        soma_direta = RacionalAssinado(0)
        for k in range(1, n + 1):
            soma_direta = soma_direta.somar(self.termo_geral(k))
        um = RacionalAssinado(1)
        if self.razao == um:
            formula = self.primeiro_termo.multiplicar(RacionalAssinado(n))
        else:
            razao_n = _potencia(self.razao, n)
            numerador = razao_n.subtrair(um)
            denominador = self.razao.subtrair(um)
            formula = self.primeiro_termo.multiplicar(numerador).multiplicar(denominador.reciproco())
        if formula != soma_direta:
            raise ValueError("fórmula da soma divergiu da soma termo a termo")
        return formula
