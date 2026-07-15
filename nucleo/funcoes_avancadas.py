"""Funções avançadas — domínio controlado, imagem rastreada, inversa e composição.

"Funções avançadas" existia neste projeto só como resposta legada
(`nucleo/conceitos_avancados_puros.py`): explicação e exemplo prontos, sem
prova, código ou teste. Liga a `função como relação especial` (ETAPA 70),
`aplicação finita` (ETAPA 71), `composição de funções` (ETAPA 74),
`injetividade` (ETAPA 75) e `inversa relacional` (ETAPA 78): uma função
avançada não é conhecimento novo, é a mesma função com domínio explícito
e finito, imagem rastreada (não assumida), e — quando injetora — uma
inversa que desfaz a regra, conferida por composição de ida e volta.

Exemplo clássico: `f(x) = 2x-3` tem inversa `f⁻¹(y) = (y+3)/2`, porque
multiplicar por um coeficiente não nulo e somar uma constante é sempre
reversível.
"""
from __future__ import annotations

from dataclasses import dataclass

from .reais_intervalos_naturais import RacionalAssinado

_ZERO = RacionalAssinado(0)


@dataclass(frozen=True, slots=True)
class FuncaoLinear:
    """f(x) = coeficiente·x + constante, com domínio explícito e finito."""

    coeficiente: RacionalAssinado
    constante: RacionalAssinado
    dominio: tuple[RacionalAssinado, ...]

    def __post_init__(self) -> None:
        if not self.dominio:
            raise ValueError("função avançada exige domínio não vazio")

    def aplicar(self, x: RacionalAssinado) -> RacionalAssinado:
        if x not in self.dominio:
            raise ValueError(f"x={x.numerador}/{x.denominador} não pertence ao domínio controlado")
        return self.coeficiente.multiplicar(x).somar(self.constante)

    def imagem(self) -> tuple[RacionalAssinado, ...]:
        """Conjunto de saídas, rastreado aplicando a regra em cada x do domínio — não assumido."""
        return tuple(self.aplicar(x) for x in self.dominio)

    def eh_injetora(self) -> bool:
        """Confere unicidade: nenhum par de entradas diferentes produz a mesma saída."""
        imagens = self.imagem()
        distintas = {(v.numerador, v.denominador) for v in imagens}
        return len(distintas) == len(imagens)

    def inversa(self) -> "FuncaoLinear":
        """f⁻¹(y) = (y − constante)/coeficiente, conferida desfazendo f em cada ponto do domínio.

        Levanta erro se `coeficiente` for zero (função constante não é
        injetora, não tem inversa) ou se a inversa não desfizer f em
        algum ponto — reversibilidade é testada, não assumida.
        """
        if self.coeficiente.numerador == 0:
            raise ValueError("função constante não é injetora; não tem inversa")
        novo_coeficiente = self.coeficiente.reciproco()
        nova_constante = _ZERO.subtrair(self.constante).multiplicar(novo_coeficiente)
        inv = FuncaoLinear(novo_coeficiente, nova_constante, self.imagem())
        for x in self.dominio:
            y = self.aplicar(x)
            if inv.aplicar(y) != x:
                raise ValueError("inversa não desfaz a função original (falha de reversibilidade)")
        return inv


def composicao(f: FuncaoLinear, g: FuncaoLinear) -> FuncaoLinear:
    """(f∘g)(x) = f(g(x)), definida sobre o domínio de g.

    Exige que toda saída de g pertença ao domínio de f — composição
    indefinida é erro, não silenciada. A fórmula fechada da composta é
    conferida ponto a ponto contra aplicar f depois de g diretamente.
    """
    for x in g.dominio:
        y = g.aplicar(x)
        if y not in f.dominio:
            raise ValueError(
                f"composição indefinida: g({x.numerador}/{x.denominador})="
                f"{y.numerador}/{y.denominador} não pertence ao domínio de f"
            )
    novo_coeficiente = f.coeficiente.multiplicar(g.coeficiente)
    nova_constante = f.coeficiente.multiplicar(g.constante).somar(f.constante)
    composta = FuncaoLinear(novo_coeficiente, nova_constante, g.dominio)
    for x in g.dominio:
        esperado = f.aplicar(g.aplicar(x))
        if composta.aplicar(x) != esperado:
            raise ValueError("fórmula da composição divergiu de aplicar f depois de g")
    return composta
