"""Raiz quadrada reconstruída pelo método de pares de algarismos.

O mesmo procedimento usado à mão no papel (o método ensinado antes das
calculadoras existirem): agrupa o radicando em pares de algarismos e, a cada
passo, descobre o maior dígito seguinte da raiz por tentativa controlada.

Não usa `/`, `//`, `%`, `**`, `math.sqrt`, `isqrt`, `decimal` ou `cmath` como
fundamento -- as mesmas restrições que `matematica.divisao` e
`nucleo.aritmetica_escolar_nativa` já declaram. Soma, subtração e
multiplicação nativas (`+`, `-`, `*`) não estão nessa lista: não são a
operação sendo reconstruída (raiz quadrada), só bookkeeping -- o mesmo papel
que `nucleo.aritmetica_escolar_nativa.sucessor` já cumpre com `n + 1`. A
contagem por sucessor/predecessor daquele módulo é O(n) por chamada; para os
restos que este método gera (multiplicados por 100 a cada casa) isso explode
para bilhões de passos mesmo em radicandos pequenos como 13 -- inviável até
para o "papel". Usar `+`/`-`/`*` nativos aqui é o que mantém o método
praticável para números grandes, como o cálculo manual real também é.
"""
from __future__ import annotations

from dataclasses import dataclass

from .divisao import _incrementar_decimal


@dataclass(frozen=True, slots=True)
class RaizQuadradaPSF:
    radicando: int
    quadrado_perfeito: bool
    decimal: str
    casas: int
    modo: str
    resto_final: int
    passos: tuple[str, ...]


def _validar_natural(n: int, nome: str) -> None:
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"{nome} deve ser natural finito")


def _grupos_de_dois(n: int) -> list[int]:
    """Agrupa os algarismos de n em pares, mais significativo primeiro.

    Puro reconhecimento de dígitos (o que um humano faz olhando o número
    escrito) -- não é cálculo, então não usa nenhuma primitiva aritmética.
    """
    texto = str(n)
    if len(texto) % 2 == 1:
        texto = "0" + texto
    return [int(texto[i : i + 2]) for i in range(0, len(texto), 2)]


def _proximo_digito(raiz_parcial: int, resto: int, grupo: int) -> tuple[int, int, int, str]:
    """Um passo do método de pares: desce `grupo` (0-99) e acha o próximo dígito da raiz."""
    resto_ampliado = resto * 100 + grupo
    base = raiz_parcial * 20
    digito = 0
    while digito < 9 and (base + digito + 1) * (digito + 1) <= resto_ampliado:
        digito += 1
    termo = (base + digito) * digito
    novo_resto = resto_ampliado - termo
    nova_raiz = raiz_parcial * 10 + digito
    passo = (
        f"desce {grupo:02d} -> resto ampliado {resto_ampliado}; "
        f"maior dígito d com ({base}+d)×d ≤ {resto_ampliado} é {digito} "
        f"(({base}+{digito})×{digito}={termo}); raiz parcial {nova_raiz}, resto {novo_resto}"
    )
    return nova_raiz, novo_resto, digito, passo


def raiz_quadrada(
    radicando: int,
    casas: int | None = None,
    modo: str = "truncar",
    casas_padrao: int = 4,
) -> RaizQuadradaPSF:
    """Constrói a raiz quadrada de `radicando` pelo método de pares de algarismos.

    Quando `radicando` é quadrado perfeito, devolve o inteiro exato. Caso
    contrário, expande casas decimais com o mesmo controle de `casas`/`modo`
    (`truncar`/`arredondar`) que `matematica.divisao.expandir_decimal` usa.
    """
    _validar_natural(radicando, "radicando")
    if casas is not None:
        _validar_natural(casas, "casas")
    modo_normalizado = modo.strip().lower()
    if modo_normalizado not in {"truncar", "arredondar"}:
        raise ValueError("modo deve ser 'truncar' ou 'arredondar'")

    raiz = 0
    resto = 0
    passos: list[str] = []
    for grupo in _grupos_de_dois(radicando):
        raiz, resto, _, passo = _proximo_digito(raiz, resto, grupo)
        passos.append(passo)

    if resto == 0:
        return RaizQuadradaPSF(radicando, True, str(raiz), 0, modo_normalizado, 0, tuple(passos))

    parte_inteira = raiz
    limite = casas if casas is not None else casas_padrao
    gerar = limite + (1 if modo_normalizado == "arredondar" and casas is not None else 0)
    digitos: list[int] = []
    posicao = 0
    while posicao < gerar:
        raiz, resto, digito, passo = _proximo_digito(raiz, resto, 0)
        digitos.append(digito)
        passos.append(passo)
        posicao += 1
        if resto == 0 and casas is None:
            break

    if modo_normalizado == "arredondar" and casas is not None:
        extra = digitos.pop() if digitos else 0
        if extra >= 5:
            parte_inteira, digitos = _incrementar_decimal(parte_inteira, digitos)
            passos.append(f"Casa de decisão = {extra}; arredondamento acrescenta uma unidade à última casa mantida.")
        else:
            passos.append(f"Casa de decisão = {extra}; a última casa mantida não é alterada.")

    if casas is not None:
        while len(digitos) < casas:
            digitos.append(0)

    decimal = f"{parte_inteira}," + "".join(str(d) for d in digitos) if digitos else str(parte_inteira)
    return RaizQuadradaPSF(
        radicando=radicando,
        quadrado_perfeito=False,
        decimal=decimal,
        casas=len(digitos),
        modo=modo_normalizado,
        resto_final=resto,
        passos=tuple(passos),
    )
