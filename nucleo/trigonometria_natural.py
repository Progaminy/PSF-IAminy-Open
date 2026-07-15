"""Trigonometria natural PSF construída por razões em triângulos retângulos.

O módulo não usa ``math.sin``, ``math.cos`` nem tabelas de ângulos. O ponto de
partida operacional é um triângulo retângulo já medido. Semelhança conserva as
razões dos lados e permite que elas caracterizem o ângulo agudo escolhido.
"""
from __future__ import annotations

from dataclasses import dataclass

from .aritmetica_escolar_nativa import multiplicar, somar, validar_natural


@dataclass(frozen=True, slots=True)
class RazaoExata:
    numerador: int
    denominador: int

    def __post_init__(self) -> None:
        validar_natural(self.numerador, "numerador")
        validar_natural(self.denominador, "denominador")
        if self.denominador == 0:
            raise ValueError("uma razão exige termo de comparação não nulo")
        divisor = _mdc_por_retiradas(self.numerador, self.denominador)
        object.__setattr__(self, "numerador", _dividir_exato(self.numerador, divisor))
        object.__setattr__(self, "denominador", _dividir_exato(self.denominador, divisor))

    def texto(self) -> str:
        if self.denominador == 1:
            return str(self.numerador)
        return f"{self.numerador}/{self.denominador}"

    def igual(self, outra: "RazaoExata") -> bool:
        return multiplicar(self.numerador, outra.denominador) == multiplicar(
            outra.numerador, self.denominador
        )

    def quadrado(self) -> "RazaoExata":
        return RazaoExata(
            multiplicar(self.numerador, self.numerador),
            multiplicar(self.denominador, self.denominador),
        )

    def somar(self, outra: "RazaoExata") -> "RazaoExata":
        return RazaoExata(
            somar(
                multiplicar(self.numerador, outra.denominador),
                multiplicar(outra.numerador, self.denominador),
            ),
            multiplicar(self.denominador, outra.denominador),
        )

    def dividir_por(self, outra: "RazaoExata") -> "RazaoExata":
        if outra.numerador == 0:
            raise ValueError("não se pode formar uma razão dividindo por zero")
        return RazaoExata(
            multiplicar(self.numerador, outra.denominador),
            multiplicar(self.denominador, outra.numerador),
        )


def _mdc_por_retiradas(a: int, b: int) -> int:
    if a == 0:
        return b
    x, y = a, b
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def _dividir_exato(total: int, parte: int) -> int:
    restante = total
    quantidade = 0
    while restante >= parte:
        restante -= parte
        quantidade += 1
    if restante != 0:
        raise ValueError("repartição não exata")
    return quantidade


@dataclass(frozen=True, slots=True)
class TrianguloRetangulo:
    """Lados relativos a um dos ângulos agudos do triângulo."""

    cateto_adjacente: int
    cateto_oposto: int
    hipotenusa: int

    def __post_init__(self) -> None:
        for nome, valor in (
            ("cateto_adjacente", self.cateto_adjacente),
            ("cateto_oposto", self.cateto_oposto),
            ("hipotenusa", self.hipotenusa),
        ):
            validar_natural(valor, nome)
            if valor == 0:
                raise ValueError("os lados de um triângulo devem ter medida positiva")
        soma_quadrados = somar(
            multiplicar(self.cateto_adjacente, self.cateto_adjacente),
            multiplicar(self.cateto_oposto, self.cateto_oposto),
        )
        quadrado_hipotenusa = multiplicar(self.hipotenusa, self.hipotenusa)
        if soma_quadrados != quadrado_hipotenusa:
            raise ValueError("os lados não formam um triângulo retângulo")

    def ampliar(self, fator: int) -> "TrianguloRetangulo":
        validar_natural(fator, "fator")
        if fator == 0:
            raise ValueError("semelhança exige fator positivo")
        return TrianguloRetangulo(
            multiplicar(self.cateto_adjacente, fator),
            multiplicar(self.cateto_oposto, fator),
            multiplicar(self.hipotenusa, fator),
        )


def seno(t: TrianguloRetangulo) -> RazaoExata:
    return RazaoExata(t.cateto_oposto, t.hipotenusa)


def cosseno(t: TrianguloRetangulo) -> RazaoExata:
    return RazaoExata(t.cateto_adjacente, t.hipotenusa)


def tangente(t: TrianguloRetangulo) -> RazaoExata:
    return RazaoExata(t.cateto_oposto, t.cateto_adjacente)


def cotangente(t: TrianguloRetangulo) -> RazaoExata:
    return RazaoExata(t.cateto_adjacente, t.cateto_oposto)


def secante(t: TrianguloRetangulo) -> RazaoExata:
    return RazaoExata(t.hipotenusa, t.cateto_adjacente)


def cossecante(t: TrianguloRetangulo) -> RazaoExata:
    return RazaoExata(t.hipotenusa, t.cateto_oposto)


def identidade_fundamental_confere(t: TrianguloRetangulo) -> bool:
    """Certifica sen² + cos² = 1 a partir de a² + b² = h²."""
    return seno(t).quadrado().somar(cosseno(t).quadrado()).igual(RazaoExata(1, 1))


def identidades_de_quociente_conferem(t: TrianguloRetangulo) -> bool:
    return (
        seno(t).dividir_por(cosseno(t)).igual(tangente(t))
        and cosseno(t).dividir_por(seno(t)).igual(cotangente(t))
    )


def identidades_reciprocas_conferem(t: TrianguloRetangulo) -> bool:
    um = RazaoExata(1, 1)
    return (
        um.dividir_por(cosseno(t)).igual(secante(t))
        and um.dividir_por(seno(t)).igual(cossecante(t))
        and um.dividir_por(tangente(t)).igual(cotangente(t))
    )


@dataclass(frozen=True, slots=True)
class PassoTrigonometrico:
    nome: str
    depende_de: tuple[str, ...]
    construcao: str


FLUXO_TRIGONOMETRICO_NATURAL = (
    PassoTrigonometrico("diferença", (), "Distinguir duas marcas ou posições."),
    PassoTrigonometrico("unidade", ("diferença",), "Escolher uma diferença como unidade repetível."),
    PassoTrigonometrico("medida de comprimento", ("unidade",), "Contar quantas unidades cobrem um segmento."),
    PassoTrigonometrico("segmento", ("medida de comprimento",), "Ligar dois pontos e conservar a distância entre eles."),
    PassoTrigonometrico("razão", ("medida de comprimento",), "Comparar duas medidas sem apagar qual divide qual."),
    PassoTrigonometrico("proporção", ("razão",), "Reconhecer razões iguais por multiplicação cruzada."),
    PassoTrigonometrico("direção", ("segmento",), "Prolongar mentalmente o percurso orientado de um segmento."),
    PassoTrigonometrico("ângulo", ("direção",), "Comparar a abertura entre duas direções com origem comum."),
    PassoTrigonometrico("perpendicularidade", ("ângulo",), "Construir direções cuja abertura divide uma volta em quatro partes iguais."),
    PassoTrigonometrico("ângulo reto", ("perpendicularidade",), "Nomear uma dessas quatro aberturas iguais."),
    PassoTrigonometrico("triângulo", ("segmento", "ângulo"), "Fechar três segmentos em três pontos não alinhados."),
    PassoTrigonometrico("triângulo retângulo", ("triângulo", "ângulo reto"), "Escolher o triângulo que contém um ângulo reto."),
    PassoTrigonometrico("hipotenusa e catetos", ("triângulo retângulo",), "Distinguir o lado oposto ao ângulo reto dos dois lados que o formam."),
    PassoTrigonometrico("cateto oposto e adjacente", ("hipotenusa e catetos", "ângulo"), "Fixar um ângulo agudo e nomear os catetos relativamente a ele."),
    PassoTrigonometrico("semelhança", ("proporção", "triângulo retângulo"), "Ampliar ou reduzir todos os lados pelo mesmo fator, conservando os ângulos."),
    PassoTrigonometrico("razões invariantes do ângulo", ("semelhança", "cateto oposto e adjacente"), "Mostrar que lados correspondentes mudam pelo mesmo fator e suas razões não mudam."),
    PassoTrigonometrico("seno", ("razões invariantes do ângulo",), "Comparar cateto oposto com hipotenusa."),
    PassoTrigonometrico("cosseno", ("razões invariantes do ângulo",), "Comparar cateto adjacente com hipotenusa."),
    PassoTrigonometrico("tangente", ("seno", "cosseno"), "Comparar cateto oposto com adjacente; equivale a seno dividido por cosseno."),
    PassoTrigonometrico("cotangente", ("tangente",), "Inverter a comparação da tangente: adjacente sobre oposto."),
    PassoTrigonometrico("secante", ("cosseno",), "Inverter a comparação do cosseno: hipotenusa sobre adjacente."),
    PassoTrigonometrico("cossecante", ("seno",), "Inverter a comparação do seno: hipotenusa sobre oposto."),
    PassoTrigonometrico("identidade fundamental", ("seno", "cosseno", "triângulo retângulo"), "Dividir a relação pitagórica pelo quadrado da hipotenusa para obter sen² + cos² = 1."),
)


def auditar_fluxo_trigonometrico() -> dict[str, object]:
    vistos: set[str] = set()
    duplicados: list[str] = []
    ausentes: list[tuple[str, str]] = []
    for passo in FLUXO_TRIGONOMETRICO_NATURAL:
        if passo.nome in vistos:
            duplicados.append(passo.nome)
        for dependencia in passo.depende_de:
            if dependencia not in vistos:
                ausentes.append((passo.nome, dependencia))
        vistos.add(passo.nome)
    return {
        "passos": len(FLUXO_TRIGONOMETRICO_NATURAL),
        "duplicados": tuple(duplicados),
        "dependencias_ausentes_ou_futuras": tuple(ausentes),
        "sem_lacunas_internas": not duplicados and not ausentes,
    }
