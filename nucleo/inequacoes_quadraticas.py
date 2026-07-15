"""Inequações do 2º grau — sinal de a·x²+b·x+c decidido pelas raízes e pelo sinal de a.

Liga `equação quadrática exata` (ETAPA 1048, raízes racionais exatas) a
`inequações lineares` (ETAPA 1041, mesma disciplina de conferência por
teste em pontos). "Estudo de sinal" da parábola não é regra decorada:
`satisfaz(x)` sempre avalia `a·x²+b·x+c` de verdade e compara com o
comparador — é essa avaliação direta que decide tudo, inclusive a
classificação textual, que é derivada dela, nunca o contrário.
"""
from __future__ import annotations

from dataclasses import dataclass

from .equacao_quadratica_exata import raiz_quadrada_exata_ou_none
from .inequacoes import Comparador
from .reais_intervalos_naturais import RacionalAssinado

_ZERO = RacionalAssinado(0)
_UM = RacionalAssinado(1)
_DOIS = RacionalAssinado(2)
_QUATRO = RacionalAssinado(4)
_METADE = RacionalAssinado(1, 2)


def _avaliar(a: RacionalAssinado, b: RacionalAssinado, c: RacionalAssinado, x: RacionalAssinado) -> RacionalAssinado:
    return a.multiplicar(x).multiplicar(x).somar(b.multiplicar(x)).somar(c)


def _satisfaz_comparador(comparador: Comparador, valor: RacionalAssinado) -> bool:
    igual_a_zero = valor == _ZERO
    if comparador is Comparador.MAIOR:
        return _ZERO.menor_ou_igual(valor) and not igual_a_zero
    if comparador is Comparador.MENOR:
        return valor.menor_ou_igual(_ZERO) and not igual_a_zero
    if comparador is Comparador.MAIOR_OU_IGUAL:
        return _ZERO.menor_ou_igual(valor)
    return valor.menor_ou_igual(_ZERO)


@dataclass(frozen=True, slots=True)
class SolucaoInequacaoQuadratica:
    """Solução de a·x²+b·x+c ⋈ 0, com as raízes (se existirem) e a classificação."""

    a: RacionalAssinado
    b: RacionalAssinado
    c: RacionalAssinado
    comparador: Comparador
    raizes: tuple[RacionalAssinado, ...]
    classificacao: str

    def satisfaz(self, x: RacionalAssinado) -> bool:
        """Testa x de verdade na expressão original — a única fonte de verdade."""
        return _satisfaz_comparador(self.comparador, _avaliar(self.a, self.b, self.c, x))


def resolver_inequacao_quadratica(
    a: RacionalAssinado, b: RacionalAssinado, c: RacionalAssinado, comparador: Comparador
) -> SolucaoInequacaoQuadratica:
    """Resolve a·x²+b·x+c ⋈ 0.

    Fora de duas raízes reais distintas, o sinal da expressão é sempre o
    sinal de `a`; entre elas, o sinal contrário — porque a parábola só
    troca de sinal ao cruzar uma raiz. Quando o discriminante não é
    quadrado perfeito racional, as raízes ficariam irracionais (fora do
    escopo exato desta etapa) — mas nesse caso o sinal já é decidível sem
    elas: sem raiz real, ele é constante em toda a reta.
    """
    if a.numerador == 0:
        raise ValueError("a não pode ser zero; não é uma inequação do 2º grau")
    discriminante = b.multiplicar(b).subtrair(_QUATRO.multiplicar(a).multiplicar(c))

    if discriminante.numerador < 0:
        raizes: tuple[RacionalAssinado, ...] = ()
    else:
        raiz_disc = raiz_quadrada_exata_ou_none(discriminante)
        if raiz_disc is None:
            raise ValueError("discriminante não é quadrado perfeito racional; fora do escopo exato")
        dois_a_reciproco = _DOIS.multiplicar(a).reciproco()
        menos_b = _ZERO.subtrair(b)
        x1 = menos_b.somar(raiz_disc).multiplicar(dois_a_reciproco)
        x2 = menos_b.subtrair(raiz_disc).multiplicar(dois_a_reciproco)
        raiz_menor, raiz_maior = (x1, x2) if x1.menor_ou_igual(x2) else (x2, x1)
        raizes = (raiz_menor,) if raiz_menor == raiz_maior else (raiz_menor, raiz_maior)

    provisorio = SolucaoInequacaoQuadratica(a, b, c, comparador, raizes, "")

    if not raizes:
        classificacao = "todos_os_reais" if provisorio.satisfaz(_ZERO) else "vazio"
    elif len(raizes) == 1:
        raiz = raizes[0]
        fora = provisorio.satisfaz(raiz.somar(_UM))
        no_ponto = provisorio.satisfaz(raiz)
        if fora and no_ponto:
            classificacao = "todos_os_reais"
        elif fora:
            classificacao = "todos_exceto_um_ponto"
        elif no_ponto:
            classificacao = "um_ponto"
        else:
            classificacao = "vazio"
    else:
        raiz_menor, raiz_maior = raizes
        entre = provisorio.satisfaz(raiz_menor.somar(raiz_maior).multiplicar(_METADE))
        fora = provisorio.satisfaz(raiz_maior.somar(_UM))
        if entre and fora:
            classificacao = "todos_os_reais"
        elif entre:
            classificacao = "entre_raizes"
        elif fora:
            classificacao = "fora_das_raizes"
        else:
            classificacao = "vazio"

    return SolucaoInequacaoQuadratica(a, b, c, comparador, raizes, classificacao)
