"""Geometria no espaço — primitivo Ponto3D/Vetor3D, primeiro passo do espaço.

Item 239 do plano pede geometria no espaço ao lado da geometria plana,
do mesmo porte do bloco de grafos — não uma etapa única. Este módulo é
o menor passo honesto: o primitivo de ponto e vetor em 3 coordenadas,
mesma extensão mecânica que `Ponto`/`Vetor` (ETAPA 1038) já fizeram
sobre `RacionalAssinado`, sem polígono, plano, ângulo diedro ou volume
de sólido arbitrário — esses continuam próximo alvo.

A diferença conceitual real (não só mecânica) está no produto vetorial:
em 2D ele é um número (a componente z do produto vetorial 3D, quando as
duas primeiras coordenadas são z=0); em 3D ele é de novo um vetor,
perpendicular aos dois originais. Isso não é reinventado do zero — é a
mesma definição por determinante, só com a terceira linha/coluna que o
caso 2D descartava.
"""
from __future__ import annotations

from dataclasses import dataclass

from .reais_intervalos_naturais import RacionalAssinado


@dataclass(frozen=True, slots=True)
class Ponto3D:
    x: RacionalAssinado
    y: RacionalAssinado
    z: RacionalAssinado


@dataclass(frozen=True, slots=True)
class Vetor3D:
    dx: RacionalAssinado
    dy: RacionalAssinado
    dz: RacionalAssinado

    @staticmethod
    def entre(origem: Ponto3D, destino: Ponto3D) -> "Vetor3D":
        return Vetor3D(
            destino.x.subtrair(origem.x),
            destino.y.subtrair(origem.y),
            destino.z.subtrair(origem.z),
        )

    def produto_escalar(self, outro: "Vetor3D") -> RacionalAssinado:
        return (
            self.dx.multiplicar(outro.dx)
            .somar(self.dy.multiplicar(outro.dy))
            .somar(self.dz.multiplicar(outro.dz))
        )

    def produto_vetorial(self, outro: "Vetor3D") -> "Vetor3D":
        """Produto vetorial 3D de verdade: devolve um vetor, não um número.

        Perpendicular aos dois vetores originais (conferido em teste via
        produto escalar nulo contra ambos) — mesma definição por
        determinante do caso 2D (ETAPA 1038), com a terceira coordenada
        que aquele caso descartava por assumir z=0 dos dois lados.
        """
        return Vetor3D(
            self.dy.multiplicar(outro.dz).subtrair(self.dz.multiplicar(outro.dy)),
            self.dz.multiplicar(outro.dx).subtrair(self.dx.multiplicar(outro.dz)),
            self.dx.multiplicar(outro.dy).subtrair(self.dy.multiplicar(outro.dx)),
        )

    def norma_ao_quadrado(self) -> RacionalAssinado:
        return self.produto_escalar(self)


def pontos_colineares(p1: Ponto3D, p2: Ponto3D, p3: Ponto3D) -> bool:
    """Três pontos são colineares quando o produto vetorial de dois vetores entre eles é nulo.

    Mesmo teste do caso 2D (ETAPA 1038, `TrianguloGeral`) — em 3D o
    produto vetorial é um vetor, então "nulo" é as três coordenadas
    zeradas, não uma única.
    """
    v1 = Vetor3D.entre(p1, p2)
    v2 = Vetor3D.entre(p1, p3)
    cruzado = v1.produto_vetorial(v2)
    return cruzado.dx.numerador == 0 and cruzado.dy.numerador == 0 and cruzado.dz.numerador == 0
