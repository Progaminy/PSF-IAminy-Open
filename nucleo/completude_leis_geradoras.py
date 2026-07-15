"""Completude por sequências de Cauchy de leis geradoras — quarto e último item de reais completos.

A ETAPA 1035 deixou quatro itens pendentes: equivalência (ETAPA 1061),
operações preservadas (ETAPA 1062), ordem (ETAPA 1063) e a prova de
completude. Este módulo fecha o quarto — mas com o escopo que dá para
construir honestamente: **completude por sequências de Cauchy**, não a
propriedade geral do supremo para qualquer conjunto arbitrário de reais.

A diferença importa e não é retórica. A propriedade geral do supremo
("todo conjunto não vazio limitado tem menor cota superior") exigiria
decidir ordem entre reais arbitrários — e a ETAPA 1063 já mostrou,
honestamente, que isso às vezes fica indeterminado (não dá para decidir
com certeza < ou > entre duas leis quaisquer em tempo finito, se elas
representarem o mesmo valor). Fingir a propriedade geral do supremo
seria fingir uma decisão que não existe. O que dá para construir sem
fingir é mais restrito e é exatamente o que basta para o resto do
projeto: dada uma sequência explícita de leis geradoras com um
**certificado de Cauchy** (uma regra `modulo_cauchy(epsilon)` que devolve
um índice N tal que todos os termos a partir de N ficam a distância
<= epsilon entre si — fornecida por quem constrói a sequência, não
adivinhada), constrói-se a lei geradora do limite.

```text
epsilon_k = 1/2^(k+1)  (decresce para zero)
N_k = modulo_cauchy(epsilon_k)
bruto_k = termo(N_k) refinado até largura <= epsilon_k, alargado por epsilon_k
          dos dois lados (o termo N_k pode ainda estar a até epsilon_k do limite)
passo(indice) = interseção de bruto_0, bruto_1, ..., bruto_indice
```

A interseção acumulada garante o encaixamento por construção (interseção
com mais uma restrição só pode manter ou encolher o intervalo, nunca
alargar) — não depende de nenhuma monotonicidade delicada da sequência
original. A largura tende a zero porque `bruto_k` tem largura <= 3·epsilon_k,
que também tende a zero.
"""
from __future__ import annotations

from collections.abc import Callable

from .lei_geradora_real import LeiGeradoraIntervalos, modulo_convergencia
from .reais_intervalos_naturais import IntervaloRacional, RacionalAssinado


def _maior(x: RacionalAssinado, y: RacionalAssinado) -> RacionalAssinado:
    return y if x.menor_ou_igual(y) else x


def _menor(x: RacionalAssinado, y: RacionalAssinado) -> RacionalAssinado:
    return x if x.menor_ou_igual(y) else y


def _potencia_de_dois(expoente: int) -> int:
    """2**expoente por potência por repetição (raiz fundacional), não pelo operador nativo.

    `expoente` aqui é o índice de refinamento (k+1), não o valor sendo
    construído -- cresce um por termo da sequência de Cauchy, nunca em salto,
    então multiplicação repetida é tão barata quanto o operador nativo seria.
    """
    resultado = 1
    for _ in range(expoente):
        resultado *= 2
    return resultado


def lei_geradora_limite_de_sequencia_cauchy(
    termo: Callable[[int], LeiGeradoraIntervalos],
    modulo_cauchy: Callable[[RacionalAssinado], int],
    limite_passos_por_termo: int = 1000,
) -> LeiGeradoraIntervalos:
    """Constrói a lei geradora do limite de uma sequência de Cauchy de leis.

    `modulo_cauchy(epsilon)` é o certificado: garante que, a partir do
    índice devolvido, todos os termos da sequência ficam a distância
    <= epsilon do limite (e portanto entre si). Este construtor confia
    nesse certificado — validá-lo é responsabilidade de quem o fornece,
    o mesmo contrato que `modulo_convergencia` já assume sobre uma lei
    bem formada.
    """

    def _bruto(k: int) -> IntervaloRacional:
        epsilon_k = RacionalAssinado(1, _potencia_de_dois(k + 1))
        n = modulo_cauchy(epsilon_k)
        if n < 0:
            raise ValueError("módulo de Cauchy devolveu índice negativo")
        lei_n = termo(n)
        refinado = lei_n.passo(modulo_convergencia(lei_n, epsilon_k, limite_passos_por_termo))
        return IntervaloRacional(refinado.inferior.subtrair(epsilon_k), refinado.superior.somar(epsilon_k))

    def passo(indice: int) -> IntervaloRacional:
        if indice < 0:
            raise ValueError("passo deve ser não negativo")
        inferior: RacionalAssinado | None = None
        superior: RacionalAssinado | None = None
        for k in range(indice + 1):
            bruto = _bruto(k)
            inferior = bruto.inferior if inferior is None else _maior(inferior, bruto.inferior)
            superior = bruto.superior if superior is None else _menor(superior, bruto.superior)
        if not inferior.menor_ou_igual(superior):
            raise ValueError("certificado de Cauchy inconsistente: interseção acumulada ficou vazia")
        return IntervaloRacional(inferior, superior)

    return LeiGeradoraIntervalos(nome="limite_sequencia_cauchy", passo=passo)
