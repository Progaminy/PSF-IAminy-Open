"""Logaritmo exato — log_b(x) por busca, quando x é potência exata de b.

"Logaritmos" existia neste projeto só como resposta legada
(`nucleo/conceitos_avancados_puros.py`), sem prova, código ou teste. Este
módulo liga a potência (já usada em várias etapas: potência modular,
progressão geométrica). O logaritmo geral (base e expoente reais
arbitrários) exige reais completos, ainda em aberto (ETAPA 1035). Aqui a
construção fica no caso exato: busca o expoente inteiro `n` tal que
`base^n = x` exatamente, positivo ou negativo, e declara honestamente
quando `x` não é potência exata de `base` dentro do limite de busca — não
finge uma aproximação onde a resposta deveria ser exata.
"""
from __future__ import annotations

from .reais_intervalos_naturais import RacionalAssinado

_UM = RacionalAssinado(1)


def logaritmo_exato(base: RacionalAssinado, x: RacionalAssinado, limite_busca: int = 200) -> int:
    """Menor |n| tal que base^n = x, buscando por multiplicação repetida.

    Domínio: base > 0, base ≠ 1, x > 0. Busca `n >= 0` multiplicando a
    base por si mesma; se `x` não aparecer aí, busca `n < 0` multiplicando
    o recíproco da base — cobre x > 1 e x < 1 sem precisar decidir de
    antemão em qual direção procurar. Levanta erro se `x` não for
    potência exata de `base` dentro do limite.
    """
    if base.numerador <= 0 or base == _UM:
        raise ValueError("base do logaritmo deve ser positiva e diferente de 1")
    if x.numerador <= 0:
        raise ValueError("logaritmo só está definido para x positivo")
    if x == _UM:
        return 0

    potencia = _UM
    for n in range(1, limite_busca + 1):
        potencia = potencia.multiplicar(base)
        if potencia == x:
            return n

    potencia = _UM
    reciproco_base = base.reciproco()
    for n in range(1, limite_busca + 1):
        potencia = potencia.multiplicar(reciproco_base)
        if potencia == x:
            return -n

    raise ValueError(
        f"{x.numerador}/{x.denominador} não é potência exata de "
        f"{base.numerador}/{base.denominador} dentro do limite de busca"
    )
