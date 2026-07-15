"""Ordem entre leis geradoras — terceiro dos quatro itens pendentes de reais completos.

Liga `ordem total` (ETAPA 69, já construída sobre racionais) e
`equivalência leis geradoras` (ETAPA 1061): a mesma ideia de comparar
intervalos usada para checar consistência agora decide `<` ou `>` entre
duas leis, refinando cada uma até largura <= epsilon/2 e comparando os
intervalos resultantes.

```text
i1 = lei1 refinada; i2 = lei2 refinada
→ i1.superior < i2.inferior: prova definitiva de lei1 < lei2
→ i2.superior < i1.inferior: prova definitiva de lei1 > lei2
→ nenhum dos dois: indeterminado nesse epsilon (podem ser iguais, ou
  só ainda não refinados o suficiente)
```

A assimetria é a mesma de `sao_consistentes_ate_epsilon`: um resultado
`MENOR`/`MAIOR` é prova definitiva e finita (os intervalos não se tocam,
então nenhum valor cabe nos dois ao mesmo tempo do lado errado).
`INDETERMINADA` não é "são iguais" — é honestamente "não decidido nesse
epsilon", porque poderia ser diferença pequena ainda não separada, ou
poderia ser mesmo valor. `decidir_ordem` refina epsilon repetidamente
até decidir ou desistir honestamente: se as leis representam valores
diferentes, a diferença é um racional fixo positivo e refinar o
suficiente sempre a encontra; se representam o mesmo valor, nunca
decide — não finge uma prova de igualdade que este módulo não tem.
"""
from __future__ import annotations

from enum import Enum

from .lei_geradora_real import LeiGeradoraIntervalos, modulo_convergencia
from .reais_intervalos_naturais import RacionalAssinado

_METADE = RacionalAssinado(1, 2)


class RelacaoOrdem(Enum):
    MENOR = "<"
    MAIOR = ">"
    INDETERMINADA = "?"


def _estritamente_menor(x: RacionalAssinado, y: RacionalAssinado) -> bool:
    return x.menor_ou_igual(y) and x != y


def comparar_leis_ate_epsilon(
    lei1: LeiGeradoraIntervalos,
    lei2: LeiGeradoraIntervalos,
    epsilon: RacionalAssinado,
    limite_passos: int = 1000,
) -> RelacaoOrdem:
    """Refina as duas leis até largura <= epsilon/2 e compara os intervalos resultantes."""
    if epsilon.numerador <= 0:
        raise ValueError("epsilon deve ser racional positivo")
    metade_epsilon = epsilon.multiplicar(_METADE)
    n1 = modulo_convergencia(lei1, metade_epsilon, limite_passos)
    n2 = modulo_convergencia(lei2, metade_epsilon, limite_passos)
    i1 = lei1.passo(n1)
    i2 = lei2.passo(n2)
    if _estritamente_menor(i1.superior, i2.inferior):
        return RelacaoOrdem.MENOR
    if _estritamente_menor(i2.superior, i1.inferior):
        return RelacaoOrdem.MAIOR
    return RelacaoOrdem.INDETERMINADA


def decidir_ordem(
    lei1: LeiGeradoraIntervalos,
    lei2: LeiGeradoraIntervalos,
    epsilon_inicial: RacionalAssinado = RacionalAssinado(1, 10),
    limite_refinamentos: int = 50,
    limite_passos: int = 1000,
) -> RelacaoOrdem:
    """Refina epsilon pela metade repetidamente até decidir ou desistir honestamente."""
    epsilon = epsilon_inicial
    for _ in range(limite_refinamentos):
        resultado = comparar_leis_ate_epsilon(lei1, lei2, epsilon, limite_passos)
        if resultado is not RelacaoOrdem.INDETERMINADA:
            return resultado
        epsilon = epsilon.multiplicar(_METADE)
    return RelacaoOrdem.INDETERMINADA
