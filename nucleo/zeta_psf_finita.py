"""Função zeta reconstruída em camada finita PSF — etapa 1032.

Este módulo NÃO prova a Hipótese de Riemann e NÃO usa a fórmula clássica
como fundamento. Ele constrói a primeira camada possível da zeta:

    natural n
    ↓
    potência n^s por multiplicação repetida
    ↓
    peso racional 1/(n^s) representado como par (numerador, denominador)
    ↓
    soma finita dos pesos
    ↓
    produto de Euler FINITO apenas como validação estrutural posterior

Convenção: um racional positivo é representado por (num, den), com den > 0.
Não simplificamos por mdc para não transformar a simplificação em dependência
oculta. Igualdade racional é testada por multiplicação cruzada construída.

Dependências proibidas aqui:
- módulos antigos de aritmética/primos/divisores;
- operador de divisão/reste/potência nativo: /, //, %, **;
- math, fractions, decimal, numpy, sympy, scipy.
"""
from __future__ import annotations

from .sequencias_calculo_psf import (
    adicionar,
    multiplicar,
    subtrair_controlado,
    potencia,
    sucessor,
)

Racional = tuple[int, int]


def _validar_natural(n: int, nome: str = "n") -> None:
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"{nome} deve ser natural finito")


def _validar_positivo(n: int, nome: str = "n") -> None:
    _validar_natural(n, nome)
    if n == 0:
        raise ValueError(f"{nome} deve ser positivo")


def racional(num: int, den: int) -> Racional:
    """Cria racional positivo sem simplificar."""
    _validar_natural(num, "num")
    _validar_positivo(den, "den")
    return (num, den)


def racional_um() -> Racional:
    return (1, 1)


def racional_zero() -> Racional:
    return (0, 1)


def racional_somar(a: Racional, b: Racional) -> Racional:
    """Soma racional por construção multiplicativa cruzada.

    (a_num/a_den) + (b_num/b_den) nasce como:
    partes comuns de denominador a_den*b_den, acumulando numeradores
    a_num*b_den e b_num*a_den.
    """
    an, ad = a
    bn, bd = b
    esquerda = multiplicar(an, bd)
    direita = multiplicar(bn, ad)
    num = adicionar(esquerda, direita)
    den = multiplicar(ad, bd)
    return racional(num, den)


def racional_multiplicar(a: Racional, b: Racional) -> Racional:
    an, ad = a
    bn, bd = b
    return racional(multiplicar(an, bn), multiplicar(ad, bd))


def racional_igual(a: Racional, b: Racional) -> bool:
    """Igualdade por produto cruzado, sem divisão."""
    an, ad = a
    bn, bd = b
    return multiplicar(an, bd) == multiplicar(bn, ad)


def peso_zeta(n: int, expoente: int) -> Racional:
    """Peso 1/(n^s) com n positivo e s natural."""
    _validar_positivo(n, "n")
    _validar_natural(expoente, "expoente")
    den = potencia(n, expoente)
    return racional(1, den)


def zeta_finita_por_soma(expoente: int, limite: int) -> Racional:
    """Camada PSF da zeta: soma finita dos pesos 1/(n^s), n=1..limite."""
    _validar_natural(expoente, "expoente")
    _validar_natural(limite, "limite")
    total = racional_zero()
    n = 1
    while n <= limite:
        total = racional_somar(total, peso_zeta(n, expoente))
        n = sucessor(n)
    return total


def _resto_por_retirada(n: int, d: int) -> int:
    """Resto por retirada repetida; ferramenta interna finita."""
    _validar_natural(n, "n")
    _validar_positivo(d, "d")
    r = n
    while r >= d:
        r = subtrair_controlado(r, d)
    return r


def divide_por_retirada(d: int, n: int) -> bool:
    _validar_positivo(d, "d")
    _validar_natural(n, "n")
    return _resto_por_retirada(n, d) == 0


def primo_por_retirada(n: int) -> bool:
    """Primalidade finita por ausência de divisor interno; sem importar primos."""
    _validar_natural(n, "n")
    if n < 2:
        return False
    d = 2
    while d < n:
        if divide_por_retirada(d, n):
            return False
        d = sucessor(d)
    return True


def primos_ate_por_retirada(limite: int) -> list[int]:
    _validar_natural(limite, "limite")
    saida: list[int] = []
    n = 2
    while n <= limite:
        if primo_por_retirada(n):
            saida.append(n)
        n = sucessor(n)
    return saida


def produto_euler_finito_validacao(expoente: int, limite_primo: int) -> Racional:
    """Produto de Euler finito como validação, não como fundamento.

    Para cada primo p observado até limite_primo, cria-se o fator finito
    p^s / (p^s - 1). Este produto é uma camada de comparação estrutural:
    usa a reconstrução de primalidade finita por retirada, e não uma tabela
    pronta de primos.
    """
    _validar_natural(expoente, "expoente")
    _validar_natural(limite_primo, "limite_primo")
    total = racional_um()
    for p in primos_ate_por_retirada(limite_primo):
        ps = potencia(p, expoente)
        fator = racional(ps, subtrair_controlado(ps, 1))
        total = racional_multiplicar(total, fator)
    return total


def rastro_pesos_zeta(expoente: int, limite: int) -> list[dict[str, object]]:
    """Catálogo de pesos: mostra de onde cada parcela da zeta finita nasceu."""
    _validar_natural(expoente, "expoente")
    _validar_natural(limite, "limite")
    saida: list[dict[str, object]] = []
    n = 1
    while n <= limite:
        den = potencia(n, expoente)
        saida.append({
            "n": n,
            "expoente": expoente,
            "potencia_construida": den,
            "peso": racional(1, den),
            "leitura": f"peso de {n} no nível {expoente}: 1/{den}",
        })
        n = sucessor(n)
    return saida


def reconstrucao_zeta_finita(expoente: int, limite_soma: int, limite_primo: int) -> dict[str, object]:
    """Pacote de reconstrução finita da zeta para auditoria PSF.

    A soma finita é a construção principal. O produto de Euler finito fica
    marcado no próprio retorno como validação, para não fingir fundamento.
    """
    return {
        "estado": "camada finita; não é continuação analítica; não é RH",
        "fundamento": "soma de pesos racionais construídos por repetição",
        "pesos": rastro_pesos_zeta(expoente, limite_soma),
        "zeta_finita_soma": zeta_finita_por_soma(expoente, limite_soma),
        "validacao_euler_finita": {
            "papel": "comparação estrutural posterior, não fundamento",
            "limite_primo": limite_primo,
            "primos_recriados": primos_ate_por_retirada(limite_primo),
            "produto": produto_euler_finito_validacao(expoente, limite_primo),
        },
        "bloqueios_para_RH": [
            "números reais completos",
            "números complexos",
            "séries infinitas",
            "continuação analítica",
            "zeros complexos",
            "operadores/espectro",
        ],
    }
