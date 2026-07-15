"""Medidas e grandezas — nasce de comparar e combinar, não de uma unidade pronta.

A trigonometria natural (ETAPA 1033) já usa "unidade", "medida de comprimento"
e "razão" como passos narrativos do seu fluxo, mas nunca os tornou operação
própria: eram nome e descrição, não código executável e testável. Esta etapa
constrói essa camada de verdade, reaproveitando `RacionalAssinado` (ETAPA
1034/1035) em vez de reinventar aritmética racional.

Uma grandeza (no sentido clássico, de Euclides) é qualquer coisa que se pode:
- comparar com outra da mesma espécie (ordem);
- combinar com outra da mesma espécie (adição).

Medir é escolher uma grandeza como unidade e contar, por subtração
repetida, quantas vezes ela cabe dentro de outra — exatamente a mesma
construção já usada em `nucleo/divisao_euclidiana_pura.py` e
`nucleo/euclides_subtracao_pura.py`, aplicada agora a grandezas em vez de
números soltos.

Comprimento, massa e tempo são espécies independentes: nenhuma nasce das
outras, e por isso são tipos Python distintos — somar `Massa` com `Tempo`
não deve sequer fazer sentido, em vez de fingir que grandezas diferentes
são a mesma coisa. Área e volume, ao contrário, não são espécies
independentes: nascem de multiplicar comprimentos, e por isso têm função
própria de construção (`area_retangulo`, `volume_paralelepipedo`) em vez
de entrar como grandeza solta.
"""
from __future__ import annotations

from dataclasses import dataclass

from .reais_intervalos_naturais import RacionalAssinado


class _GrandezaEscalar:
    """Comparar, somar e subtrair para qualquer grandeza sobre `RacionalAssinado`.

    Cada espécie concreta (`Comprimento`, `Massa`, `Tempo`, `Area`,
    `Volume`) herda daqui em vez de repetir a mesma lógica cinco vezes.
    `type(self)(...)` preserva a espécie do resultado: `Massa.somar` nunca
    devolve `Comprimento`, mesmo reaproveitando o código.
    """

    valor: RacionalAssinado

    def __post_init__(self) -> None:
        if self.valor.numerador < 0:
            raise ValueError(f"{type(self).__name__} é uma grandeza; não admite valor negativo")

    def comparar(self, outro: "_GrandezaEscalar") -> int:
        if self.valor.menor_ou_igual(outro.valor) and outro.valor.menor_ou_igual(self.valor):
            return 0
        return -1 if self.valor.menor_ou_igual(outro.valor) else 1

    def somar(self, outro: "_GrandezaEscalar") -> "_GrandezaEscalar":
        return type(self)(self.valor.somar(outro.valor))

    def subtrair(self, outro: "_GrandezaEscalar") -> "_GrandezaEscalar":
        if self.comparar(outro) < 0:
            raise ValueError("grandeza não admite retirar mais do que existe")
        return type(self)(self.valor.subtrair(outro.valor))


@dataclass(frozen=True, slots=True)
class Comprimento(_GrandezaEscalar):
    """Grandeza de comprimento, representada em uma unidade de referência."""

    valor: RacionalAssinado


@dataclass(frozen=True, slots=True)
class Massa(_GrandezaEscalar):
    """Grandeza de massa — espécie independente de comprimento e tempo."""

    valor: RacionalAssinado


@dataclass(frozen=True, slots=True)
class Tempo(_GrandezaEscalar):
    """Grandeza de tempo — espécie independente de comprimento e massa."""

    valor: RacionalAssinado


@dataclass(frozen=True, slots=True)
class Area(_GrandezaEscalar):
    """Grandeza derivada: só nasce de multiplicar comprimentos (`area_retangulo`)."""

    valor: RacionalAssinado


@dataclass(frozen=True, slots=True)
class Volume(_GrandezaEscalar):
    """Grandeza derivada: só nasce de multiplicar comprimentos (`volume_paralelepipedo`)."""

    valor: RacionalAssinado


def area_retangulo(base: Comprimento, altura: Comprimento) -> Area:
    """Área de um retângulo: produto de dois comprimentos, não fórmula solta."""
    return Area(base.valor.multiplicar(altura.valor))


def volume_paralelepipedo(comprimento: Comprimento, largura: Comprimento, altura: Comprimento) -> Volume:
    """Volume de um paralelepípedo: produto de três comprimentos, não fórmula solta."""
    return Volume(comprimento.valor.multiplicar(largura.valor).multiplicar(altura.valor))


@dataclass(frozen=True, slots=True)
class Medida:
    """Resultado de medir uma grandeza com uma unidade: quantidade inteira + resto."""

    quantidade: int
    resto: _GrandezaEscalar
    unidade: _GrandezaEscalar

    def certificado(self) -> dict[str, object]:
        return {
            "quantidade_unidades": self.quantidade,
            "resto_menor_que_unidade": self.resto.comparar(self.unidade) < 0,
            "estado": "MEDIDA_POR_CONTAGEM_DE_UNIDADES; resto pode ser refinado com subunidade",
        }


def medir(grandeza: _GrandezaEscalar, unidade: _GrandezaEscalar) -> Medida:
    """Conta, por subtração repetida, quantas vezes `unidade` cabe em `grandeza`.

    Mesma ideia de ETAPA_08_RESTO_E_DIVISAO_EUCLIDIANA, generalizada de
    números para grandezas: nenhuma divisão nativa, apenas comparar e
    subtrair até a unidade não caber mais. Funciona para qualquer espécie
    (comprimento, massa, tempo, área, volume) — medir não depende de qual
    grandeza está sendo medida, só de que ela saiba comparar e subtrair.
    """
    if type(grandeza) is not type(unidade):
        raise ValueError("só se mede uma grandeza com unidade da mesma espécie")
    if unidade.valor.numerador == 0:
        raise ValueError("unidade de medida não pode ser grandeza nula")
    restante = grandeza
    quantidade = 0
    while restante.comparar(unidade) >= 0:
        restante = restante.subtrair(unidade)
        quantidade += 1
    return Medida(quantidade=quantidade, resto=restante, unidade=unidade)


def sao_grandezas_proporcionais(
    a1: _GrandezaEscalar, a2: _GrandezaEscalar, b1: _GrandezaEscalar, b2: _GrandezaEscalar
) -> bool:
    """a1/a2 == b1/b2 por multiplicação cruzada exata, sem calcular razão decimal.

    A mesma ideia de "proporção" já citada em ETAPA_1033, agora testável:
    duas razões de grandezas são proporcionais quando o produto cruzado dos
    numeradores/denominadores (já em `RacionalAssinado`) coincide.
    """
    if a2.valor.numerador == 0 or b2.valor.numerador == 0:
        raise ValueError("proporção exige termo de comparação não nulo")
    cruzado_1 = a1.valor.multiplicar(b2.valor)
    cruzado_2 = b1.valor.multiplicar(a2.valor)
    return cruzado_1 == cruzado_2
