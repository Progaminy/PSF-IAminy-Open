"""Domínio do logaritmo composto com expressão linear — liga logaritmos a inequações.

Liga `logaritmos` (ETAPA 1045, que já recusa `x ≤ 0` internamente) a
`inequações` (ETAPA 1041): a resposta legada de
`nucleo/conceitos_avancados_puros.py` ("Qual é o domínio de f(x) =
ln(x - 4)?" → "x > 4", justificado por "logaritmo natural exige
argumento positivo") tinha só o resultado citado. Aqui o domínio nasce
de resolver `a·x+b > 0` como inequação linear de verdade — a mesma
restrição que `logaritmo_exato` já impõe internamente ao recusar
argumento não positivo, agora isolada para x em vez de checada só no
ponto de avaliação.

Não é o logaritmo natural (base `e`, irracional) especificamente: a
exigência de argumento positivo vale para logaritmo de qualquer base
válida, e é isso que esta etapa constrói e testa — a base concreta usada
na conferência é só uma testemunha racional qualquer.
"""
from __future__ import annotations

from .inequacoes import Comparador, SolucaoInequacao, resolver_inequacao_linear
from .logaritmos import logaritmo_exato
from .reais_intervalos_naturais import RacionalAssinado

_ZERO = RacionalAssinado(0)


def dominio_de_logaritmo_linear(a: RacionalAssinado, b: RacionalAssinado) -> SolucaoInequacao:
    """Domínio de log(a·x+b): resolve a·x+b > 0 como inequação linear."""
    return resolver_inequacao_linear(a, b, Comparador.MAIOR, _ZERO)


def confirmar_fronteira_de_dominio(
    a: RacionalAssinado,
    b: RacionalAssinado,
    base: RacionalAssinado,
    x_dentro: RacionalAssinado,
    x_fora: RacionalAssinado,
) -> bool:
    """Confere a fronteira testando `logaritmo_exato` de verdade nos dois lados.

    `x_dentro` precisa satisfazer o domínio calculado e ter argumento que
    seja potência exata de `base` (para `logaritmo_exato` não levantar
    por outro motivo); `x_fora` precisa violar o domínio, o que sempre
    faz `logaritmo_exato` levantar (o primeiro código que ele checa).
    """
    solucao = dominio_de_logaritmo_linear(a, b)
    if not solucao.satisfaz(x_dentro):
        raise ValueError("x_dentro não satisfaz o domínio calculado")
    if solucao.satisfaz(x_fora):
        raise ValueError("x_fora deveria violar o domínio calculado")

    logaritmo_exato(base, a.multiplicar(x_dentro).somar(b))

    try:
        logaritmo_exato(base, a.multiplicar(x_fora).somar(b))
    except ValueError:
        return True
    raise ValueError("fora do domínio, logaritmo deveria levantar erro")
