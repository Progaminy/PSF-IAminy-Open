"""Função por ramos — cada entrada cai em exatamente um ramo, ou é erro.

"Função por ramos" existia neste projeto só como resposta legada
(`nucleo/conceitos_avancados_puros.py`), sem prova, código ou teste. Liga
a `função como relação especial` (ETAPA 70): uma função por ramos não é
conhecimento novo, é uma função cuja relação é a união de várias
sub-relações, cada uma válida numa parte do domínio.

Uma função por ramos só está bem definida quando os ramos particionam o
domínio: nenhum x cabe em dois ramos (a função seria ambígua) e nenhum x
fica sem ramo (a função seria parcial sem avisar). Isto não é assumido —
`avaliar` confere as duas condições a cada chamada, sobre o x pedido.
"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from .reais_intervalos_naturais import RacionalAssinado


@dataclass(frozen=True, slots=True)
class Ramo:
    nome: str
    pertence: Callable[[RacionalAssinado], bool]
    formula: Callable[[RacionalAssinado], RacionalAssinado]


@dataclass(frozen=True, slots=True)
class FuncaoPorRamos:
    ramos: tuple[Ramo, ...]

    def __post_init__(self) -> None:
        if not self.ramos:
            raise ValueError("função por ramos exige ao menos um ramo")

    def avaliar(self, x: RacionalAssinado) -> RacionalAssinado:
        """Aplica o ramo cujo domínio contém x, conferindo que é o único.

        Levanta erro se nenhum ramo contiver x (domínio não cobre esse
        ponto) ou se mais de um ramo contiver x (domínio sobreposto,
        função ambígua nesse ponto) — nunca escolhe um ramo por ordem
        arbitrária.
        """
        candidatos = [ramo for ramo in self.ramos if ramo.pertence(x)]
        if not candidatos:
            raise ValueError(f"x={x.numerador}/{x.denominador} não pertence a nenhum ramo do domínio")
        if len(candidatos) > 1:
            nomes = ", ".join(r.nome for r in candidatos)
            raise ValueError(
                f"x={x.numerador}/{x.denominador} pertence a mais de um ramo ({nomes}); domínio não particiona"
            )
        return candidatos[0].formula(x)
