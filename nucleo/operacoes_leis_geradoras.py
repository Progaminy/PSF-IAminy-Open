"""Operações preservadas entre leis geradoras — soma e produto por aritmética de intervalos.

Segundo dos quatro itens que a ETAPA 1035 deixou pendentes (depois de
`equivalência entre leis geradoras`, ETAPA 1061): soma e produto de duas
leis geradoras são construídas combinando os intervalos de cada uma no
mesmo passo, não avaliando nenhum valor real diretamente (que não
existe fora do encaixe de intervalos).

```text
soma: [a_inf, a_sup] + [b_inf, b_sup] = [a_inf+b_inf, a_sup+b_sup]
produto: [a_inf,a_sup] × [b_inf,b_sup] = [min(4 cantos), max(4 cantos)]
```

Soma é monótona em cada lado, então basta somar os limites correspondentes.
Produto usa os quatro produtos dos cantos (não só canto-a-canto) porque,
diferente da soma, o produto não é monótono da mesma forma quando os
intervalos podem conter valores negativos — os quatro cantos cobrem
todo caso de sinal sem assumir que os valores são sempre positivos.

Cada lei combinada preserva o encaixamento (nested) das leis originais:
se os intervalos de entrada encolhem, a soma e o produto também
encolhem, e a prova de que a construção é a "soma certa"/"produto
certo" é feita reaproveitando `sao_consistentes_ate_epsilon` (ETAPA
1061) contra uma lei geradora constante de valor conhecido, quando esse
valor existe (por exemplo `√4 × √9` tem que ficar consistente com `6`).
"""
from __future__ import annotations

from .lei_geradora_real import LeiGeradoraIntervalos
from .reais_intervalos_naturais import IntervaloRacional, RacionalAssinado


def lei_geradora_constante(valor: RacionalAssinado) -> LeiGeradoraIntervalos:
    """Lei trivial: todo passo devolve o mesmo ponto, largura zero desde o início.

    Serve de testemunha exata para conferir soma e produto de outras leis
    (quando o resultado esperado já é um racional conhecido).
    """

    def passo(indice: int) -> IntervaloRacional:
        if indice < 0:
            raise ValueError("passo deve ser não negativo")
        return IntervaloRacional(valor, valor)

    return LeiGeradoraIntervalos(nome=f"constante({valor.numerador}/{valor.denominador})", passo=passo)


def _minimo(valores: tuple[RacionalAssinado, ...]) -> RacionalAssinado:
    menor = valores[0]
    for v in valores[1:]:
        if v.menor_ou_igual(menor):
            menor = v
    return menor


def _maximo(valores: tuple[RacionalAssinado, ...]) -> RacionalAssinado:
    maior = valores[0]
    for v in valores[1:]:
        if maior.menor_ou_igual(v):
            maior = v
    return maior


def lei_geradora_soma(lei1: LeiGeradoraIntervalos, lei2: LeiGeradoraIntervalos) -> LeiGeradoraIntervalos:
    """Soma de duas leis: intervalos somados ponto a ponto no mesmo passo."""

    def passo(indice: int) -> IntervaloRacional:
        i1 = lei1.passo(indice)
        i2 = lei2.passo(indice)
        return IntervaloRacional(i1.inferior.somar(i2.inferior), i1.superior.somar(i2.superior))

    return LeiGeradoraIntervalos(nome=f"soma({lei1.nome},{lei2.nome})", passo=passo)


def lei_geradora_produto(lei1: LeiGeradoraIntervalos, lei2: LeiGeradoraIntervalos) -> LeiGeradoraIntervalos:
    """Produto de duas leis: envoltória dos quatro produtos dos cantos, no mesmo passo."""

    def passo(indice: int) -> IntervaloRacional:
        i1 = lei1.passo(indice)
        i2 = lei2.passo(indice)
        cantos = (
            i1.inferior.multiplicar(i2.inferior),
            i1.inferior.multiplicar(i2.superior),
            i1.superior.multiplicar(i2.inferior),
            i1.superior.multiplicar(i2.superior),
        )
        return IntervaloRacional(_minimo(cantos), _maximo(cantos))

    return LeiGeradoraIntervalos(nome=f"produto({lei1.nome},{lei2.nome})", passo=passo)
