"""Critérios de divisibilidade — provados por construção, não por regra decorada.

"Critérios de divisibilidade" (olhar só o último dígito, ou a soma dos
dígitos) existiam neste projeto apenas implícitos na base de
`divisibilidade pura` (ETAPA 3) e `resto e divisão euclidiana` (ETAPA 8).
Este módulo liga `digitos()` (ETAPA 1037) a essa base: cada critério é
conferido contra o resto real de dividir o número inteiro — nunca aceito
como regra escolar decorada. Se o critério e o resto real discordarem em
algum caso, o código lança erro em vez de devolver resposta errada
silenciosa.

A conferência não chama `dividir_com_resto` sobre o número inteiro: para
um divisor pequeno (2, 3, 5, 9, 10), isso repete o mesmo custo escondido
já corrigido em ETAPA 1037 (`dividir_com_resto` passa por `subtrair` e
`predecessor`, que busca por sucessão a partir de zero). O resto real é
calculado dígito a dígito, como em `divisao_armada` — trazendo um dígito
por vez, sempre sobre valores pequenos.
"""
from __future__ import annotations

from .aritmetica_escolar_nativa import dividir_com_resto, somar
from .contas_armadas import _vezes_potencia, digitos
from .paridade import eh_par


def _resto_por_digitos(n: int, divisor: int) -> int:
    """Resto de n por um divisor pequeno, trazendo um dígito por vez (como divisao_armada)."""
    resto_parcial = 0
    for digito in digitos(n):
        trazido = somar(_vezes_potencia(resto_parcial, 10), digito)
        _, resto_parcial = dividir_com_resto(trazido, divisor)
    return resto_parcial


def _soma_digitos(n: int) -> int:
    total = 0
    for digito in digitos(n):
        total = somar(total, digito)
    return total


def _confere(nome: str, criterio: bool, n: int, divisor: int) -> bool:
    direto = _resto_por_digitos(n, divisor) == 0
    if criterio != direto:
        raise ValueError(f"critério de divisibilidade por {nome} divergiu do resto real")
    return criterio


def divisivel_por_dois(n: int) -> bool:
    """Critério: último dígito par."""
    criterio = eh_par(digitos(n)[-1])
    return _confere("2", criterio, n, 2)


def divisivel_por_cinco(n: int) -> bool:
    """Critério: último dígito 0 ou 5."""
    ultimo = digitos(n)[-1]
    criterio = ultimo == 0 or ultimo == 5
    return _confere("5", criterio, n, 5)


def divisivel_por_dez(n: int) -> bool:
    """Critério: último dígito 0."""
    criterio = digitos(n)[-1] == 0
    return _confere("10", criterio, n, 10)


def divisivel_por_tres(n: int) -> bool:
    """Critério: soma dos dígitos divisível por 3."""
    _, resto_soma = dividir_com_resto(_soma_digitos(n), 3)
    criterio = resto_soma == 0
    return _confere("3", criterio, n, 3)


def divisivel_por_nove(n: int) -> bool:
    """Critério: soma dos dígitos divisível por 9."""
    _, resto_soma = dividir_com_resto(_soma_digitos(n), 9)
    criterio = resto_soma == 0
    return _confere("9", criterio, n, 9)
