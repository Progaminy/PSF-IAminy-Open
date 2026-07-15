"""Lei geradora explícita de aproximações racionais encaixadas.

A ETAPA 1034 certificou intervalos racionais encaixados mas deixou expresso
que ainda faltava "sequência infinita ou lei geradora". Uma lista infinita
não pode ser escrita por um PSF finito; uma regra computável pode. Este
módulo constrói exatamente essa regra — e um módulo de convergência que a
testa contra qualquer erro racional positivo em número finito de passos.

Isto não é prova de completude dos reais. Uma lei geradora garante um
intervalo por passo e um módulo de convergência explícito; equivalência
entre leis diferentes, operações preservadas entre leis, ordem entre leis e
a prova de completude (propriedade do supremo) continuam pendentes.
"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from .reais_intervalos_naturais import AproximacaoReal, IntervaloRacional, RacionalAssinado


@dataclass(frozen=True, slots=True)
class LeiGeradoraIntervalos:
    """Regra computável passo -> intervalo racional encaixado.

    ``passo`` deve ser determinística: o mesmo índice sempre produz o mesmo
    intervalo. A lei não materializa a sequência inteira; é a fórmula que a
    gera sob pedido, para qualquer índice finito.
    """

    nome: str
    passo: Callable[[int], IntervaloRacional]

    def prefixo(self, quantidade: int) -> AproximacaoReal:
        if quantidade < 1:
            raise ValueError("prefixo exige ao menos um passo")
        intervalos = tuple(self.passo(indice) for indice in range(quantidade))
        return AproximacaoReal(intervalos)


def modulo_convergencia(
    lei: LeiGeradoraIntervalos,
    epsilon: RacionalAssinado,
    limite_passos: int = 1000,
) -> int:
    """Menor passo n tal que a largura de ``lei.passo(n)`` já é <= epsilon.

    Busca finita e explícita. Verifica o encaixe a cada passo em vez de
    assumir convergência; se o limite de passos for atingido sem sucesso,
    declara falha honesta em vez de fingir que convergiu.
    """
    if epsilon.numerador <= 0:
        raise ValueError("epsilon deve ser racional positivo")
    anterior: IntervaloRacional | None = None
    for indice in range(limite_passos):
        atual = lei.passo(indice)
        if anterior is not None and not anterior.contem_intervalo(atual):
            raise ValueError(f"lei geradora '{lei.nome}' quebrou o encaixe no passo {indice}")
        if atual.largura().menor_ou_igual(epsilon):
            return indice
        anterior = atual
    raise ValueError(
        f"lei geradora '{lei.nome}' não atingiu erro <= {epsilon.numerador}/{epsilon.denominador}"
        f" em {limite_passos} passos"
    )


def lei_geradora_raiz_quadrada(alvo: int) -> LeiGeradoraIntervalos:
    """Newton para raiz quadrada, empacotado como intervalo encaixado.

    Para ``x > 0`` com ``x*x >= alvo``, o par ``(alvo/x, x)`` sempre contém
    ``√alvo`` (é a desigualdade das médias). Newton, partindo de
    ``x0 = max(alvo, 1) >= √alvo``, preserva ``x_n >= √alvo`` a cada passo e
    decresce; por isso ``alvo/x_n`` cresce até ``x_n`` por baixo. O
    intervalo ``[alvo/x_n, x_n]`` fica encaixado no do passo anterior sem
    depender de nenhuma convergência assumida — cada passo é verificável
    isoladamente, o que ``AproximacaoReal`` já confere na construção.
    """
    if alvo < 0:
        raise ValueError("raiz quadrada racional exige alvo não negativo")
    alvo_rac = RacionalAssinado(alvo)
    chute_inicial = RacionalAssinado(max(alvo, 1))
    metade = RacionalAssinado(1, 2)

    def _iterada(indice: int) -> RacionalAssinado:
        if indice < 0:
            raise ValueError("passo deve ser não negativo")
        atual = chute_inicial
        for _ in range(indice):
            atual = atual.somar(alvo_rac.multiplicar(atual.reciproco())).multiplicar(metade)
        return atual

    def passo(indice: int) -> IntervaloRacional:
        x_n = _iterada(indice)
        par = alvo_rac.multiplicar(x_n.reciproco())
        inferior, superior = (x_n, par) if x_n.menor_ou_igual(par) else (par, x_n)
        return IntervaloRacional(inferior, superior)

    return LeiGeradoraIntervalos(nome=f"newton_raiz_quadrada({alvo})", passo=passo)
