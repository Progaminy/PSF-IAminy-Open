"""Equações com radical — isolar a raiz, elevar ao índice, conferir o domínio.

"Radicais com variáveis" existia neste projeto só como resposta legada
(`nucleo/conceitos_avancados_puros.py`): explicação e exemplo prontos, sem
prova, código ou teste. Isto não é a mesma coisa que a lei geradora de
raiz quadrada (ETAPA 1035) — aquela aproxima √2 numericamente porque √2 é
irracional; aqui a equação `√(a·x+b) = valor` é montada para que a
resposta seja um racional exato, e o trabalho é algébrico: elevar ao
quadrado desfaz a raiz, e o domínio (radicando ≥ 0, resultado da raiz ≥ 0)
é conferido, não assumido.

Dois casos: `√(linear) = constante` (`EquacaoComRaizQuadrada`, não pode
gerar raiz estranha porque o lado direito já é dado antes de elevar ao
quadrado) e `√(linear) = linear` (`EquacaoComRaizIgualALinear`, completa
ETAPA 1042 — pode gerar raiz estranha, porque o lado direito também
depende de x e pode ficar negativo para algum candidato).
"""
from __future__ import annotations

from dataclasses import dataclass

from .equacao_quadratica_exata import resolver_quadratica_exata
from .reais_intervalos_naturais import RacionalAssinado

_ZERO = RacionalAssinado(0)
_DOIS = RacionalAssinado(2)


@dataclass(frozen=True, slots=True)
class EquacaoComRaizQuadrada:
    """√(coeficiente·x + constante) = valor."""

    coeficiente: RacionalAssinado
    constante: RacionalAssinado
    valor: RacionalAssinado

    def __post_init__(self) -> None:
        if self.coeficiente.numerador == 0:
            raise ValueError("coeficiente de x não pode ser zero")


@dataclass(frozen=True, slots=True)
class SolucaoRaizQuadrada:
    x: RacionalAssinado | None
    tem_solucao: bool
    motivo: str


def resolver_raiz_quadrada(equacao: EquacaoComRaizQuadrada) -> SolucaoRaizQuadrada:
    """Resolve √(a·x+b) = valor isolando o radicando e elevando ao quadrado.

    Domínio: uma raiz quadrada nunca é negativa, então `valor < 0` já
    declara sem solução, sem tentar álgebra nenhuma. Depois de resolver,
    reconstrói o radicando a partir de x e confere que ele bate com
    `valor²` e que não é negativo — a mesma disciplina de conferência já
    usada em `nucleo/contas_armadas.py` e `nucleo/progressoes.py`.
    """
    if equacao.valor.numerador < 0:
        return SolucaoRaizQuadrada(None, False, "raiz quadrada nunca é negativa; equação sem solução")
    valor_ao_quadrado = equacao.valor.multiplicar(equacao.valor)
    x = valor_ao_quadrado.subtrair(equacao.constante).multiplicar(equacao.coeficiente.reciproco())
    radicando = equacao.coeficiente.multiplicar(x).somar(equacao.constante)
    if radicando.numerador < 0:
        return SolucaoRaizQuadrada(None, False, "solução obtida não respeita o domínio (radicando negativo)")
    if radicando != valor_ao_quadrado:
        raise ValueError("solução não reconstrói o radicando esperado")
    return SolucaoRaizQuadrada(x, True, "conferida: eleva ao quadrado e reconstrói o radicando")


@dataclass(frozen=True, slots=True)
class EquacaoComRaizIgualALinear:
    """√(a·x+b) = c·x+d."""

    a: RacionalAssinado
    b: RacionalAssinado
    c: RacionalAssinado
    d: RacionalAssinado

    def __post_init__(self) -> None:
        if self.a.numerador == 0:
            raise ValueError("coeficiente do radicando não pode ser zero")


@dataclass(frozen=True, slots=True)
class SolucoesRaizIgualALinear:
    solucoes: tuple[RacionalAssinado, ...]
    raizes_estranhas_descartadas: tuple[RacionalAssinado, ...]
    tem_solucao: bool
    motivo: str


def resolver_raiz_igual_a_linear(equacao: EquacaoComRaizIgualALinear) -> SolucoesRaizIgualALinear:
    """Resolve √(a·x+b) = c·x+d elevando ao quadrado e filtrando raiz estranha.

    Elevar ao quadrado dá `a·x+b = (c·x+d)²`, uma quadrática em x:
    `c²x² + (2cd−a)x + (d²−b) = 0`, resolvida por
    `equacao_quadratica_exata` (ETAPA 1048). Cada raiz candidata só é
    aceita se o lado direito original (`c·x+d`) for não-negativo — senão
    a raiz satisfaz a equação elevada ao quadrado mas não a original
    (raiz estranha), porque uma raiz quadrada nunca produz valor
    negativo. Isto é a diferença real entre este caso e
    `resolver_raiz_quadrada`: lá o lado direito já era um valor fixo e
    dado; aqui ele também depende de x e pode virar negativo.
    """
    a, b, c, d = equacao.a, equacao.b, equacao.c, equacao.d
    coef_quad = c.multiplicar(c)
    coef_lin = _DOIS.multiplicar(c).multiplicar(d).subtrair(a)
    termo_indep = d.multiplicar(d).subtrair(b)

    if coef_quad.numerador == 0:
        if coef_lin.numerador == 0:
            raise ValueError("equação degenerada: nenhum termo em x depois de elevar ao quadrado")
        candidatos = (_ZERO.subtrair(termo_indep).multiplicar(coef_lin.reciproco()),)
    else:
        raizes = resolver_quadratica_exata(coef_quad, coef_lin, termo_indep)
        if raizes is None:
            return SolucoesRaizIgualALinear(
                (), (), False, "discriminante não é quadrado perfeito; raízes irracionais"
            )
        candidatos = tuple(dict.fromkeys(raizes))

    validas: list[RacionalAssinado] = []
    estranhas: list[RacionalAssinado] = []
    for x in candidatos:
        lado_direito = c.multiplicar(x).somar(d)
        radicando = a.multiplicar(x).somar(b)
        if lado_direito.numerador < 0 or radicando.numerador < 0:
            estranhas.append(x)
            continue
        if radicando != lado_direito.multiplicar(lado_direito):
            raise ValueError("candidato não reconstrói o radicando esperado")
        validas.append(x)

    if not validas:
        return SolucoesRaizIgualALinear((), tuple(estranhas), False, "todas as raízes candidatas eram estranhas")
    return SolucoesRaizIgualALinear(
        tuple(validas),
        tuple(estranhas),
        True,
        "conferida: eleva ao quadrado, filtra raiz estranha pelo sinal do lado direito",
    )
