"""Geometria analítica — reta por coordenadas, sem sair do exato.

"Geometria analítica" existia neste projeto só como resposta legada
(`nucleo/conceitos_avancados_puros.py`): explicação e exemplo prontos, sem
prova, código ou teste. Este módulo não parte do zero — reaproveita
`Ponto` e `Vetor` já construídos e provados em ETAPA 1038 (trigonometria
plana), o mesmo ramo, não um recomeço.

Pertencimento, paralelismo e perpendicularidade de retas nascem dos
mesmos produtos já usados em ETAPA 1038: produto vetorial nulo entre duas
direções significa paralelas (mesmo teste já usado para rejeitar pontos
colineares); produto escalar nulo significa perpendiculares (mesmo teste
já usado para reduzir a lei dos cossenos a Pitágoras). Nenhuma raiz
quadrada é necessária para nada disto — tudo fica em comparação exata.
"""
from __future__ import annotations

from dataclasses import dataclass

from .equacao_quadratica_exata import raiz_quadrada_exata_ou_none
from .reais_intervalos_naturais import RacionalAssinado
from .trigonometria_plana import Ponto, Vetor

_METADE = RacionalAssinado(1, 2)


@dataclass(frozen=True, slots=True)
class Reta:
    """Reta definida por dois pontos distintos."""

    p1: Ponto
    p2: Ponto

    def __post_init__(self) -> None:
        direcao = Vetor.entre(self.p1, self.p2)
        if direcao.dx.numerador == 0 and direcao.dy.numerador == 0:
            raise ValueError("uma reta exige dois pontos distintos")

    def direcao(self) -> Vetor:
        return Vetor.entre(self.p1, self.p2)


def pertence_a_reta(ponto: Ponto, reta: Reta) -> bool:
    """P pertence à reta quando (P − p1) é paralelo à direção da reta.

    Paralelo, aqui, é produto vetorial nulo — nenhuma equação Ax+By=C
    precisa ser montada à parte; é a mesma verificação de colinearidade já
    usada por `TrianguloGeral` para rejeitar três pontos alinhados.
    """
    v = Vetor.entre(reta.p1, ponto)
    return v.produto_vetorial(reta.direcao()).numerador == 0


def retas_paralelas(r1: Reta, r2: Reta) -> bool:
    """Duas retas são paralelas quando suas direções têm produto vetorial nulo."""
    return r1.direcao().produto_vetorial(r2.direcao()).numerador == 0


def retas_perpendiculares(r1: Reta, r2: Reta) -> bool:
    """Duas retas são perpendiculares quando suas direções têm produto escalar nulo."""
    return r1.direcao().produto_escalar(r2.direcao()).numerador == 0


def coeficiente_angular(reta: Reta) -> RacionalAssinado:
    """dy/dx da reta, exato. Reta vertical não tem coeficiente angular."""
    direcao = reta.direcao()
    if direcao.dx.numerador == 0:
        raise ValueError("reta vertical não tem coeficiente angular")
    return direcao.dy.multiplicar(direcao.dx.reciproco())


def ponto_medio(p1: Ponto, p2: Ponto) -> Ponto:
    """Ponto médio: média de cada coordenada, exata.

    Conferido contra a própria definição de "médio": a distância ao
    quadrado do ponto médio até cada extremo deve ser igual — não é
    aceito só por sair da fórmula de média.
    """
    x = p1.x.somar(p2.x).multiplicar(_METADE)
    y = p1.y.somar(p2.y).multiplicar(_METADE)
    medio = Ponto(x, y)
    d1 = Vetor.entre(p1, medio).norma_ao_quadrado()
    d2 = Vetor.entre(medio, p2).norma_ao_quadrado()
    if d1 != d2:
        raise ValueError("ponto médio não fica equidistante dos extremos")
    return medio


def distancia_exata_ou_none(p1: Ponto, p2: Ponto) -> RacionalAssinado | None:
    """Distância entre p1 e p2, exata, só quando o quadrado da distância é quadrado perfeito.

    Liga `norma_ao_quadrado` (ETAPA 1038) a `raiz_quadrada_exata_ou_none`
    (ETAPA 1048). Quando não é quadrado perfeito, devolve `None`: a
    distância seria irracional, fora do escopo desta etapa — não finge
    aproximar.
    """
    quadrado = Vetor.entre(p1, p2).norma_ao_quadrado()
    return raiz_quadrada_exata_ou_none(quadrado)


@dataclass(frozen=True, slots=True)
class Circunferencia:
    """(x−centro.x)² + (y−centro.y)² = raio_ao_quadrado."""

    centro: Ponto
    raio_ao_quadrado: RacionalAssinado

    def __post_init__(self) -> None:
        if self.raio_ao_quadrado.numerador <= 0:
            raise ValueError("raio ao quadrado deve ser positivo")


def circunferencia_por_centro_e_ponto(centro: Ponto, ponto_na_borda: Ponto) -> Circunferencia:
    """Constrói a circunferência a partir do centro e de um ponto conhecido da borda."""
    raio_ao_quadrado = Vetor.entre(centro, ponto_na_borda).norma_ao_quadrado()
    return Circunferencia(centro, raio_ao_quadrado)


def pertence_a_circunferencia(ponto: Ponto, circunferencia: Circunferencia) -> bool:
    """P pertence à circunferência quando a distância² ao centro bate com o raio²."""
    return Vetor.entre(circunferencia.centro, ponto).norma_ao_quadrado() == circunferencia.raio_ao_quadrado
