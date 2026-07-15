"""Exponencial natural para x racional, via limite de Cauchy de somas parciais.

ETAPA 1064 (completude por sequências de Cauchy) já deixou dito que a base
construída "já basta para o resto do projeto (séries, limites, eˣ)". Este
módulo fecha esse alvo, no escopo honesto que a própria base permite: eˣ
para x racional, como limite de Cauchy das somas parciais exatas
`Σ_{k=0}^{n} xᵏ/k!` — não eˣ para x real qualquer, nem a prova de que
eˣ>0 sempre (as duas continuam residuais do item 300).

Cada soma parcial já é um `RacionalAssinado` exato — nenhuma aproximação
até aí. O que falta para reconhecer isso como "o limite" é um
certificado de Cauchy: uma regra que, para qualquer erro racional
positivo, devolve um índice a partir do qual as somas parciais já não se
afastam do valor-limite mais do que esse erro. A cauda da série depois
do termo N é majorada pela série geométrica de razão `|x|/(N+2)` (o
mesmo teste da razão usado para provar convergência de `eˣ` na análise
clássica): quando N é grande o bastante para essa razão ficar <= 1/2, a
cauda inteira fica limitada por 2× o termo seguinte — e esse termo
seguinte encolhe para zero porque o fatorial cresce mais rápido que
qualquer potência fixa de `x`. `lei_geradora_limite_de_sequencia_cauchy`
(ETAPA 1064) recebe exatamente essa dupla (soma parcial exata + módulo
de Cauchy) e devolve a lei geradora do limite, do mesmo jeito já testado
contra Newton de raiz quadrada.
"""
from __future__ import annotations

from .completude_leis_geradoras import lei_geradora_limite_de_sequencia_cauchy
from .lei_geradora_real import LeiGeradoraIntervalos
from .operacoes_leis_geradoras import lei_geradora_constante
from .reais_intervalos_naturais import RacionalAssinado

_ZERO = RacionalAssinado(0)
_UM = RacionalAssinado(1)
_DOIS = RacionalAssinado(2)


def _fatorial(n: int) -> int:
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def _potencia_racional(base: RacionalAssinado, expoente: int) -> RacionalAssinado:
    resultado = _UM
    for _ in range(expoente):
        resultado = resultado.multiplicar(base)
    return resultado


def _modulo(valor: RacionalAssinado) -> RacionalAssinado:
    return valor if _ZERO.menor_ou_igual(valor) else _ZERO.subtrair(valor)


def _termo(x: RacionalAssinado, k: int) -> RacionalAssinado:
    """xᵏ/k!, exato."""
    return _potencia_racional(x, k).multiplicar(RacionalAssinado(1, _fatorial(k)))


def soma_parcial_exponencial(x: RacionalAssinado, n: int) -> RacionalAssinado:
    """Σ_{k=0}^{n} xᵏ/k!, exato — cada termo um `RacionalAssinado`, sem nenhuma aproximação."""
    total = _ZERO
    for k in range(n + 1):
        total = total.somar(_termo(x, k))
    return total


def _modulo_cauchy_exponencial(x: RacionalAssinado):
    modulo_x = _modulo(x)

    def modulo_cauchy(epsilon: RacionalAssinado) -> int:
        n = 0
        while True:
            # razão |x|/(n+2) <= 1/2 garante cauda majorada por série geométrica.
            if _DOIS.multiplicar(modulo_x).menor_ou_igual(RacionalAssinado(n + 2)):
                termo_seguinte = _modulo(_termo(x, n + 1))
                if _DOIS.multiplicar(termo_seguinte).menor_ou_igual(epsilon):
                    return n
            n += 1

    return modulo_cauchy


def exponencial_natural_racional(x: RacionalAssinado) -> LeiGeradoraIntervalos:
    """eˣ para x racional, como lei geradora do limite de Cauchy das somas parciais exatas.

    Escopo deliberado: só x racional. Não prova eˣ>0 em geral nem cobre x
    real arbitrário — os dois continuam residuais do item 300.
    """

    def termo(n: int) -> LeiGeradoraIntervalos:
        return lei_geradora_constante(soma_parcial_exponencial(x, n))

    return lei_geradora_limite_de_sequencia_cauchy(termo, _modulo_cauchy_exponencial(x))
