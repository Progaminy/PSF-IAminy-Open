"""Trigonometria plana — lei dos cossenos e lei dos senos para triângulos quaisquer.

A trigonometria natural (ETAPA 1033) fechou os ângulos agudos de um
triângulo retângulo. "Lei dos cossenos" e "lei dos senos" existiam neste
projeto só como texto de resposta legada (`matematica/candidatos.py`,
`nucleo/conceitos_avancados_puros.py`) — explicação e exemplo prontos, sem
prova PSF nem código nem teste por trás. Este módulo constrói as duas de
verdade, sem importar `math.cos`/`math.sin` e sem exigir ângulo reto.

A ideia central: um ângulo não precisa de uma função trigonométrica para
ser usado.

- o produto escalar entre os dois lados que formam um ângulo já carrega
  "comprimento × comprimento × cosseno do ângulo entre eles" (é assim que
  o cosseno costuma ser definido em geometria de coordenadas) — usado pela
  lei dos cossenos;
- o produto vetorial (determinante) entre os mesmos dois lados já carrega
  "comprimento × comprimento × seno do ângulo entre eles", e é o dobro da
  área do triângulo — usado pela lei dos senos.

Nenhuma raiz quadrada é necessária: tudo fica em comprimento-ao-quadrado
ou área, exato, em `RacionalAssinado` (ETAPA 1034/1035).
"""
from __future__ import annotations

from dataclasses import dataclass

from .medidas_grandezas import Area
from .reais_intervalos_naturais import RacionalAssinado

_DOIS = RacionalAssinado(2)
_METADE = RacionalAssinado(1, 2)


@dataclass(frozen=True, slots=True)
class Ponto:
    x: RacionalAssinado
    y: RacionalAssinado


@dataclass(frozen=True, slots=True)
class Vetor:
    dx: RacionalAssinado
    dy: RacionalAssinado

    @staticmethod
    def entre(origem: Ponto, destino: Ponto) -> "Vetor":
        return Vetor(destino.x.subtrair(origem.x), destino.y.subtrair(origem.y))

    def produto_escalar(self, outro: "Vetor") -> RacionalAssinado:
        return self.dx.multiplicar(outro.dx).somar(self.dy.multiplicar(outro.dy))

    def produto_vetorial(self, outro: "Vetor") -> RacionalAssinado:
        """Componente z do produto vetorial em 2D: dx1·dy2 − dy1·dx2.

        Magnitude = |u|·|v|·sen(ângulo entre eles) = o dobro da área do
        paralelogramo formado pelos dois vetores.
        """
        return self.dx.multiplicar(outro.dy).subtrair(self.dy.multiplicar(outro.dx))

    def norma_ao_quadrado(self) -> RacionalAssinado:
        return self.produto_escalar(self)


@dataclass(frozen=True, slots=True)
class TrianguloGeral:
    """Três pontos não colineares — nenhuma exigência de ângulo reto."""

    a: Ponto
    b: Ponto
    c: Ponto

    def __post_init__(self) -> None:
        v1 = Vetor.entre(self.a, self.b)
        v2 = Vetor.entre(self.a, self.c)
        # área dobrada (produto vetorial); zero só quando os pontos são colineares
        determinante = v1.produto_vetorial(v2)
        if determinante.numerador == 0:
            raise ValueError("três pontos colineares não formam um triângulo")

    def lado_ao_quadrado(self, origem: Ponto, destino: Ponto) -> RacionalAssinado:
        return Vetor.entre(origem, destino).norma_ao_quadrado()

    def _vertices(self) -> dict[str, Ponto]:
        return {"a": self.a, "b": self.b, "c": self.c}


def produto_dos_lados_vezes_cosseno(triangulo: TrianguloGeral, vertice: str) -> RacionalAssinado:
    """u·v no vértice escolhido — é exatamente (lado1 × lado2 × cos do ângulo).

    Não calcula comprimento nem ângulo isoladamente: o produto escalar já
    é essa grandeza combinada, e é ela que a lei dos cossenos usa.
    """
    pontos = triangulo._vertices()
    if vertice not in pontos:
        raise ValueError("vértice deve ser 'a', 'b' ou 'c'")
    origem = pontos[vertice]
    outros = [ponto for chave, ponto in pontos.items() if chave != vertice]
    u = Vetor.entre(origem, outros[0])
    v = Vetor.entre(origem, outros[1])
    return u.produto_escalar(v)


def lei_dos_cossenos_confere(triangulo: TrianguloGeral) -> bool:
    """Confere lado² == soma dos outros dois lados² − 2×(produto×cosseno), nos três vértices.

    Nasce de pura álgebra vetorial: para o lado oposto a C,
    ``|AB|² = |(A−C) − (B−C)|² = |A−C|² + |B−C|² − 2·(A−C)·(B−C)``.
    Quando o ângulo em C é reto, ``(A−C)·(B−C) = 0`` e a fórmula volta a
    ser exatamente a relação pitagórica — a lei dos cossenos não é um
    resultado novo e isolado; é a mesma relação, generalizada pelo termo
    do produto escalar.
    """
    lado_a2 = triangulo.lado_ao_quadrado(triangulo.b, triangulo.c)
    lado_b2 = triangulo.lado_ao_quadrado(triangulo.a, triangulo.c)
    lado_c2 = triangulo.lado_ao_quadrado(triangulo.a, triangulo.b)

    def _relacao_em(lado_oposto: RacionalAssinado, lado1: RacionalAssinado, lado2: RacionalAssinado, vertice: str) -> bool:
        ajuste = _DOIS.multiplicar(produto_dos_lados_vezes_cosseno(triangulo, vertice))
        return lado_oposto == lado1.somar(lado2).subtrair(ajuste)

    return (
        _relacao_em(lado_c2, lado_a2, lado_b2, "c")
        and _relacao_em(lado_b2, lado_a2, lado_c2, "b")
        and _relacao_em(lado_a2, lado_b2, lado_c2, "a")
    )


def area_dobrada_no_vertice(triangulo: TrianguloGeral, vertice: str) -> RacionalAssinado:
    """|produto vetorial| dos dois lados que se encontram no vértice — o dobro da área.

    É exatamente (lado1 × lado2 × sen do ângulo), a mesma ideia de
    `produto_dos_lados_vezes_cosseno`, agora com produto vetorial em vez
    de escalar. Não precisa de seno nem de raiz quadrada: a área dobrada
    sai direto do determinante, o mesmo que já garante em `__post_init__`
    que os três pontos não são colineares.
    """
    pontos = triangulo._vertices()
    if vertice not in pontos:
        raise ValueError("vértice deve ser 'a', 'b' ou 'c'")
    origem = pontos[vertice]
    outros = [ponto for chave, ponto in pontos.items() if chave != vertice]
    u = Vetor.entre(origem, outros[0])
    v = Vetor.entre(origem, outros[1])
    produto = u.produto_vetorial(v)
    return produto if produto.numerador >= 0 else RacionalAssinado(0).subtrair(produto)


def area_triangulo(triangulo: TrianguloGeral) -> Area:
    """Área do triângulo — metade da área dobrada, como grandeza (ETAPA 1036)."""
    return Area(area_dobrada_no_vertice(triangulo, "a").multiplicar(_METADE))


def lei_dos_senos_confere(triangulo: TrianguloGeral) -> bool:
    """A área dobrada é a mesma vista de qualquer vértice — a forma exata da lei dos senos.

    ``bc·senA = ac·senB = ab·senC`` (todas iguais ao dobro da área) é
    algebricamente equivalente a ``a/senA = b/senB = c/senC``: dividindo
    ``bc·senA = ac·senB`` dos dois lados por ``senA·senB`` sobra
    ``b/senB = a/senA``. Aqui a igualdade é conferida em racionais
    exatos, nos três vértices, sem calcular nenhum seno.
    """
    dobrada_a = area_dobrada_no_vertice(triangulo, "a")
    dobrada_b = area_dobrada_no_vertice(triangulo, "b")
    dobrada_c = area_dobrada_no_vertice(triangulo, "c")
    return dobrada_a == dobrada_b == dobrada_c
