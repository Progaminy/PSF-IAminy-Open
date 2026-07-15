"""Equação quadrática exata — fórmula resolvente, só quando o discriminante é quadrado perfeito.

A "equação quadrática finita" já existente (ETAPA 135,
`RESOLVER_QUADRATICA_FINITA_PURA`) testa cada valor de um domínio finito
dado — não usa a fórmula resolvente. Este módulo constrói a fórmula
`x = (−b ± √(b²−4ac)) / 2a` de verdade, mas só aceita o resultado quando
o discriminante é quadrado perfeito de um racional — nesse caso a raiz
sai exata, sem aproximação. Quando não é quadrado perfeito (a maioria dos
casos — a raiz seria irracional), a construção declara isso honestamente
em vez de aproximar: esse caso depende de reais completos (ETAPA 1035).
"""
from __future__ import annotations

from .reais_intervalos_naturais import RacionalAssinado

_ZERO = RacionalAssinado(0)
_DOIS = RacionalAssinado(2)
_QUATRO = RacionalAssinado(4)


def _raiz_inteira_exata(n: int) -> int | None:
    """Maior k tal que k*k <= n, devolvido só se k*k == n exatamente; senão None."""
    if n < 0:
        return None
    if n == 0:
        return 0
    k = 0
    while k * k < n:
        k += 1
    return k if k * k == n else None


def raiz_quadrada_exata_ou_none(valor: RacionalAssinado) -> RacionalAssinado | None:
    """√valor como racional exato, se numerador e denominador (já reduzidos) forem quadrados perfeitos."""
    if valor.numerador < 0:
        return None
    raiz_num = _raiz_inteira_exata(valor.numerador)
    raiz_den = _raiz_inteira_exata(valor.denominador)
    if raiz_num is None or raiz_den is None:
        return None
    return RacionalAssinado(raiz_num, raiz_den)


def resolver_quadratica_exata(
    a: RacionalAssinado, b: RacionalAssinado, c: RacionalAssinado
) -> tuple[RacionalAssinado, RacionalAssinado] | None:
    """Raízes de a·x²+b·x+c=0 pela fórmula resolvente, quando ficam exatas.

    Devolve `(x1, x2)` — pode haver repetição quando o discriminante é
    zero — ou `None` quando o discriminante não é quadrado perfeito
    racional (raízes irracionais, fora do escopo desta etapa). Cada raiz
    devolvida é conferida substituindo de volta em `a·x²+b·x+c`, não
    aceita só por sair da fórmula.
    """
    if a.numerador == 0:
        raise ValueError("a não pode ser zero; não é uma equação quadrática")
    discriminante = b.multiplicar(b).subtrair(_QUATRO.multiplicar(a).multiplicar(c))
    raiz_disc = raiz_quadrada_exata_ou_none(discriminante)
    if raiz_disc is None:
        return None
    dois_a_reciproco = _DOIS.multiplicar(a).reciproco()
    menos_b = _ZERO.subtrair(b)
    x1 = menos_b.somar(raiz_disc).multiplicar(dois_a_reciproco)
    x2 = menos_b.subtrair(raiz_disc).multiplicar(dois_a_reciproco)
    for x in (x1, x2):
        valor = a.multiplicar(x).multiplicar(x).somar(b.multiplicar(x)).somar(c)
        if valor.numerador != 0:
            raise ValueError("raiz da fórmula resolvente não satisfaz a equação original")
    return (x1, x2)
