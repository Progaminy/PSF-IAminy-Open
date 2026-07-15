"""Sequências de cálculo PSF — etapa 1031.

Este módulo NÃO nasce de fórmulas prontas. Ele constrói uma escada de
operações por repetição finita:

    nível 0: sucessor/repetição unitária
    nível 1: adição construída por sucessor repetido
    nível 2: multiplicação construída por adição repetida
    nível 3: potência construída por multiplicação repetida
    nível 4: superpotência/tetração finita construída por potência repetida
    nível 5+: hiperoperação finita construída pela operação anterior

O objetivo não é ser rápido; é expor a genealogia do cálculo. Fórmulas
clássicas podem validar os resultados nos testes, mas não fundam o módulo.

Dependências proibidas aqui:
- aritmetica.DIV, aritmetica.MOD, aritmetica.MDC, aritmetica.MMC
- primos, divisores
- operador de divisão/reste/potência nativo: /, //, %, **
"""
from __future__ import annotations


def _validar_natural(n: int, nome: str = "n") -> None:
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"{nome} deve ser natural finito")


def sucessor(n: int) -> int:
    """Sucessor finito: S(n)."""
    _validar_natural(n)
    return n + 1


def adicionar(a: int, b: int) -> int:
    """Adição PSF: repetir sucessor de a exatamente b vezes."""
    _validar_natural(a, "a")
    _validar_natural(b, "b")
    r = a
    contador = 0
    while contador < b:
        r = sucessor(r)
        contador = sucessor(contador)
    return r


def predecessor_controlado(n: int) -> int:
    """Antecessor de n quando n não é zero."""
    _validar_natural(n)
    if n == 0:
        raise ValueError("ZERO não tem predecessor natural")
    candidato = 0
    while sucessor(candidato) != n:
        candidato = sucessor(candidato)
    return candidato


def subtrair_controlado(a: int, b: int) -> int:
    """Subtração natural controlada: só existe quando b <= a."""
    _validar_natural(a, "a")
    _validar_natural(b, "b")
    r = a
    contador = 0
    while contador < b:
        r = predecessor_controlado(r)
        contador = sucessor(contador)
    return r


def multiplicar(a: int, b: int) -> int:
    """Multiplicação PSF: somar a consigo mesmo b vezes."""
    _validar_natural(a, "a")
    _validar_natural(b, "b")
    r = 0
    contador = 0
    while contador < b:
        r = adicionar(r, a)
        contador = sucessor(contador)
    return r


def potencia(a: int, b: int) -> int:
    """Potência PSF: multiplicar por a repetidamente b vezes."""
    _validar_natural(a, "a")
    _validar_natural(b, "b")
    r = 1
    contador = 0
    while contador < b:
        r = multiplicar(r, a)
        contador = sucessor(contador)
    return r


def _verificar_limite(valor: int, limite_valor: int | None) -> None:
    if limite_valor is not None and valor > limite_valor:
        raise OverflowError("limite_valor ultrapassado")


def multiplicar_limitado(a: int, b: int, limite_valor: int | None = None) -> int:
    """Multiplicação com trava durante a construção, não depois dela."""
    _validar_natural(a, "a")
    _validar_natural(b, "b")
    if limite_valor is not None:
        _validar_natural(limite_valor, "limite_valor")
    r = 0
    contador = 0
    while contador < b:
        r = adicionar(r, a)
        _verificar_limite(r, limite_valor)
        contador = sucessor(contador)
    return r


def potencia_limitada(a: int, b: int, limite_valor: int | None = None) -> int:
    """Potência com trava durante a construção, não depois dela."""
    _validar_natural(a, "a")
    _validar_natural(b, "b")
    if limite_valor is not None:
        _validar_natural(limite_valor, "limite_valor")
    r = 1
    contador = 0
    while contador < b:
        r = multiplicar_limitado(r, a, limite_valor=limite_valor)
        _verificar_limite(r, limite_valor)
        contador = sucessor(contador)
    return r


def operacao_nivel(nivel: int, a: int, b: int, limite_valor: int | None = None) -> int:
    """Executa a operação de uma escada PSF.

    Convenção interna:
    - nível 0: deslocamento unitário/repetição de sucessor => a + b
    - nível 1: adição
    - nível 2: multiplicação
    - nível 3: potência
    - nível 4: tetração finita a ↑↑ b
    - nível 5+: hiperoperação finita por iteração da operação anterior.

    `limite_valor` é trava honesta: se o valor ultrapassar o limite,
    levanta OverflowError em vez de fingir que pode calcular tudo.
    """
    _validar_natural(nivel, "nivel")
    _validar_natural(a, "a")
    _validar_natural(b, "b")
    if limite_valor is not None:
        _validar_natural(limite_valor, "limite_valor")

    if nivel == 0:
        r = adicionar(a, b)
    elif nivel == 1:
        r = adicionar(a, b)
    elif nivel == 2:
        r = multiplicar_limitado(a, b, limite_valor=limite_valor)
    elif nivel == 3:
        r = potencia_limitada(a, b, limite_valor=limite_valor)
    else:
        # Hiperoperação finita: para nível 4, repetir potência em torre.
        # Para nível 5+, repetir a operação do nível anterior.
        if b == 0:
            r = 1
        else:
            r = a
            contador = 1
            while contador < b:
                r = operacao_nivel(nivel - 1, a, r, limite_valor=limite_valor)
                contador = sucessor(contador)
                if limite_valor is not None and r > limite_valor:
                    raise OverflowError("limite_valor ultrapassado")
    if limite_valor is not None and r > limite_valor:
        raise OverflowError("limite_valor ultrapassado")
    return r


def nome_nivel(nivel: int) -> str:
    _validar_natural(nivel, "nivel")
    nomes = {
        0: "sucessão/deslocamento",
        1: "adição diagonal / dobro",
        2: "multiplicação diagonal / quadrado",
        3: "potência diagonal",
        4: "superpotência finita / tetração diagonal",
    }
    return nomes.get(nivel, f"hiperoperação finita nível {nivel}")


def simbolo_nivel(nivel: int) -> str:
    _validar_natural(nivel, "nivel")
    simbolos = {
        0: "S repetido",
        1: "+",
        2: "×",
        3: "^",
        4: "↑↑",
    }
    if nivel in simbolos:
        return simbolos[nivel]
    setas = "↑"
    contador = 0
    while contador < nivel:
        setas = setas + "↑"
        contador = sucessor(contador)
    return setas


def expressao_diagonal(nivel: int, n: int) -> str:
    """Representação humana do padrão n op_n n."""
    _validar_natural(nivel, "nivel")
    _validar_natural(n, "n")
    if nivel == 0:
        return f"S repetido de {n} por {n} passos"
    return f"{n} {simbolo_nivel(nivel)} {n}"


def termo_diagonal(nivel: int, n: int, limite_valor: int | None = None) -> dict[str, object]:
    """Um termo do catálogo diagonal: n operado consigo mesmo no nível dado."""
    valor = operacao_nivel(nivel, n, n, limite_valor=limite_valor)
    return {
        "nivel": nivel,
        "nome": nome_nivel(nivel),
        "n": n,
        "expressao": expressao_diagonal(nivel, n),
        "valor": valor,
    }


def sequencia_diagonal(nivel: int, inicio: int = 1, quantidade: int = 6, limite_valor: int | None = None) -> list[dict[str, object]]:
    """Gera catálogo finito do padrão conservado: n op_n n.

    Exemplos naturais:
    - nível 1: 1+1, 2+2, 3+3...
    - nível 2: 1×1, 2×2, 3×3...
    - nível 3: 1^1, 2^2, 3^3...
    - nível 4: 1↑↑1, 2↑↑2, 3↑↑3...
    """
    _validar_natural(nivel, "nivel")
    _validar_natural(inicio, "inicio")
    _validar_natural(quantidade, "quantidade")
    saida: list[dict[str, object]] = []
    n = inicio
    contador = 0
    while contador < quantidade:
        try:
            saida.append(termo_diagonal(nivel, n, limite_valor=limite_valor))
        except OverflowError:
            saida.append({
                "nivel": nivel,
                "nome": nome_nivel(nivel),
                "n": n,
                "expressao": expressao_diagonal(nivel, n),
                "valor": None,
                "bloqueado": "limite_valor ultrapassado",
            })
        n = sucessor(n)
        contador = sucessor(contador)
    return saida


def indice_propulsional(max_nivel: int = 4, max_n: int = 4, limite_valor: int | None = 1000000) -> list[dict[str, object]]:
    """Índice navegável por nível: cada linha conserva o padrão diagonal.

    O nome 'propulsional' é usado aqui no sentido PSF: cada nível propulsiona
    o cálculo pela repetição do nível anterior. Não é uma fórmula clássica;
    é um índice de acesso ao conhecimento por profundidade operacional.
    """
    _validar_natural(max_nivel, "max_nivel")
    _validar_natural(max_n, "max_n")
    saida: list[dict[str, object]] = []
    nivel = 1
    while nivel <= max_nivel:
        saida.append({
            "nivel": nivel,
            "nome": nome_nivel(nivel),
            "termos": sequencia_diagonal(nivel, inicio=1, quantidade=max_n, limite_valor=limite_valor),
        })
        nivel = sucessor(nivel)
    return saida
