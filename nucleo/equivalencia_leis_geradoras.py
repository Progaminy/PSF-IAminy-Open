"""Equivalência entre leis geradoras — quando duas regras convergem para o mesmo real.

A ETAPA 1035 deixou expresso que, depois da lei geradora e do módulo de
convergência, "equivalência entre leis diferentes, operações preservadas
entre leis, ordem entre leis e a prova de completude continuam
pendentes". Este módulo fecha o primeiro desses quatro: dado qualquer
erro racional positivo, refina duas leis (possivelmente algoritmos bem
diferentes) até cada uma ter largura <= epsilon/2, e verifica se os
dois intervalos resultantes se sobrepõem.

Isto não é prova de igualdade para todo epsilon — provar isso exigiria
verificar um número infinito de valores de epsilon, o que nenhum PSF
finito faz. O que a construção garante, honestamente, é assimétrico:

- Se os intervalos NÃO se sobrepõem em algum epsilon, é uma prova
  definitiva e finita de que as duas leis NÃO podem gerar o mesmo real
  (nenhum valor cabe nos dois ao mesmo tempo).
- Se os intervalos se sobrepõem, é evidência consistente com
  equivalência até esse epsilon — não uma prova para todo epsilon menor.

Uma segunda lei geradora de raiz quadrada, por bisseção (convergência
linear, geometricamente diferente de Newton, que é quadrática), serve de
segundo algoritmo genuinamente distinto para testar a equivalência contra
o mesmo alvo.
"""
from __future__ import annotations

from .lei_geradora_real import LeiGeradoraIntervalos, modulo_convergencia
from .reais_intervalos_naturais import IntervaloRacional, RacionalAssinado

_METADE = RacionalAssinado(1, 2)


def lei_geradora_raiz_quadrada_bissecao(alvo: int) -> LeiGeradoraIntervalos:
    """Bisseção para raiz quadrada — mesma raiz de `lei_geradora_raiz_quadrada`, outro algoritmo.

    Mantém o invariante ``lo² <= alvo <= hi²`` a cada passo: parte de
    ``lo=0`` (0² <= alvo, já que alvo >= 0) e ``hi=max(alvo,1)``
    (``hi² >= alvo``, mesma desigualdade usada no chute inicial de
    Newton). A cada passo, o ponto médio troca ``lo`` ou ``hi`` conforme
    o quadrado dele ficar abaixo ou acima do alvo — convergência linear
    (largura cai pela metade a cada passo), bem mais lenta que Newton,
    mas um algoritmo estruturalmente independente convergindo para o
    mesmo valor.
    """
    if alvo < 0:
        raise ValueError("raiz quadrada racional exige alvo não negativo")
    alvo_rac = RacionalAssinado(alvo)
    hi_inicial = RacionalAssinado(max(alvo, 1))
    lo_inicial = RacionalAssinado(0)

    def passo(indice: int) -> IntervaloRacional:
        if indice < 0:
            raise ValueError("passo deve ser não negativo")
        lo, hi = lo_inicial, hi_inicial
        for _ in range(indice):
            meio = lo.somar(hi).multiplicar(_METADE)
            if meio.multiplicar(meio).menor_ou_igual(alvo_rac):
                lo = meio
            else:
                hi = meio
        return IntervaloRacional(lo, hi)

    return LeiGeradoraIntervalos(nome=f"bissecao_raiz_quadrada({alvo})", passo=passo)


def intervalos_se_sobrepoem(i1: IntervaloRacional, i2: IntervaloRacional) -> bool:
    """Dois intervalos fechados se sobrepõem quando compartilham ao menos um ponto."""
    return i1.inferior.menor_ou_igual(i2.superior) and i2.inferior.menor_ou_igual(i1.superior)


def sao_consistentes_ate_epsilon(
    lei1: LeiGeradoraIntervalos,
    lei2: LeiGeradoraIntervalos,
    epsilon: RacionalAssinado,
    limite_passos: int = 1000,
) -> bool:
    """Refina as duas leis até largura <= epsilon/2 e verifica sobreposição.

    ``True`` é evidência consistente com "mesmo real", não uma prova para
    todo epsilon menor. ``False`` é definitivo: nenhum real cabe nos dois
    intervalos refinados ao mesmo tempo, logo as leis não podem gerar o
    mesmo valor.
    """
    if epsilon.numerador <= 0:
        raise ValueError("epsilon deve ser racional positivo")
    metade_epsilon = epsilon.multiplicar(_METADE)
    n1 = modulo_convergencia(lei1, metade_epsilon, limite_passos)
    n2 = modulo_convergencia(lei2, metade_epsilon, limite_passos)
    return intervalos_se_sobrepoem(lei1.passo(n1), lei2.passo(n2))
