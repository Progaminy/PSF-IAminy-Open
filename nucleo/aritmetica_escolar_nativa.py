"""Aritmética escolar nativa do PSF — Etapa 31.

Este módulo existe para a regra forte do núcleo puro:
Python executa, mas não ensina a matemática.

Aqui NÃO se usa:
- módulo matemático externo do Python;
- numpy, sympy ou qualquer motor externo;
- operador de divisão nativo;
- operador de divisão inteira nativo;
- operador de resto nativo;
- operador de potência nativo.

As operações escolares são reconstruídas por passos finitos:
- sucessor;
- procura de predecessor;
- soma por sucessores repetidos;
- subtração por retirada repetida;
- multiplicação por soma repetida;
- divisão exata por repartição controlada.

Os inteiros Python são usados somente como suporte físico finito para
representar marcas contáveis. A fonte do resultado é o procedimento PSF.
"""
from __future__ import annotations


def validar_natural(n: int, nome: str = "n") -> None:
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"{nome} deve ser natural finito")


def sucessor(n: int) -> int:
    """S(n): acrescentar uma unidade construída."""
    validar_natural(n)
    return n + 1


def predecessor(n: int) -> int:
    """Procura o número cuja sucessão gera n.

    Não devolve n - 1 por atalho: procura a marca anterior por construção.
    """
    validar_natural(n)
    if n == 0:
        raise ValueError("zero não tem predecessor natural")
    candidato = 0
    while sucessor(candidato) != n:
        candidato = sucessor(candidato)
    return candidato


def somar(a: int, b: int) -> int:
    """a + b construído como b sucessões aplicadas a a."""
    validar_natural(a, "a")
    validar_natural(b, "b")
    resultado = a
    passos = 0
    while passos < b:
        resultado = sucessor(resultado)
        passos = sucessor(passos)
    return resultado


def subtrair(a: int, b: int) -> int:
    """a menos b construído por retirada repetida.

    Só resolve subtração natural segura: b não pode ser maior que a.
    """
    validar_natural(a, "a")
    validar_natural(b, "b")
    if b > a:
        raise ValueError("subtração natural não pode retirar mais do que existe")
    resultado = a
    passos = 0
    while passos < b:
        resultado = predecessor(resultado)
        passos = sucessor(passos)
    return resultado


def multiplicar(a: int, b: int) -> int:
    """a vezes b construído como b grupos de a."""
    validar_natural(a, "a")
    validar_natural(b, "b")
    resultado = 0
    grupos = 0
    while grupos < b:
        resultado = somar(resultado, a)
        grupos = sucessor(grupos)
    return resultado


def dividir_exato(total: int, partes: int) -> int:
    """Reparte total em partes iguais quando a repartição fecha sem sobra.

    A pergunta escolar básica só aceita divisão exata nesta etapa.
    O quociente nasce de retirar blocos do tamanho `partes` até zerar.
    """
    validar_natural(total, "total")
    validar_natural(partes, "partes")
    if partes == 0:
        raise ValueError("não existe divisão por zero")
    restante = total
    quociente = 0
    while restante >= partes:
        restante = subtrair(restante, partes)
        quociente = sucessor(quociente)
    if restante != 0:
        raise ValueError("esta divisão não é exata na etapa escolar atual")
    return quociente


def dividir_com_resto(total: int, partes: int) -> tuple[int, int]:
    """Mesma repartição de `dividir_exato`, aceitando sobra: (quociente, resto).

    Base nativa para extrair dígitos (repartir por dez) sem usar // nem %.
    """
    validar_natural(total, "total")
    validar_natural(partes, "partes")
    if partes == 0:
        raise ValueError("não existe divisão por zero")
    restante = total
    quociente = 0
    while restante >= partes:
        restante = subtrair(restante, partes)
        quociente = sucessor(quociente)
    return quociente, restante


def somar_lista(valores: list[int] | tuple[int, ...]) -> int:
    total = 0
    for valor in valores:
        total = somar(total, valor)
    return total


def diferenca(a: int, b: int) -> int:
    """Distância entre duas quantidades naturais."""
    validar_natural(a, "a")
    validar_natural(b, "b")
    if a >= b:
        return subtrair(a, b)
    return subtrair(b, a)


def dobro(n: int) -> int:
    return multiplicar(n, 2)


def triplo(n: int) -> int:
    return multiplicar(n, 3)


def metade(n: int) -> int:
    return dividir_exato(n, 2)


def um_sobre(denominador: int, total: int) -> int:
    """1/denominador de total."""
    return dividir_exato(total, denominador)


def tres_quartos_texto() -> str:
    """Representação simbólica escolar de três quartos."""
    return "3/4"


def um_quarto_texto() -> str:
    """Representação simbólica escolar de uma parte em quatro."""
    return "1/4"


def converter_centavos_para_reais_exato(centavos: int) -> int:
    """Converte centavos para reais quando o valor fecha exatamente."""
    return dividir_exato(centavos, 100)


def dia_depois(dia: str, passos: int) -> str:
    """Avança numa semana finita por sucessão de posições."""
    dias = (
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira",
        "sábado",
        "domingo",
    )
    atual = 0
    while atual < len(dias) and dias[atual] != dia:
        atual = sucessor(atual)
    if atual == len(dias):
        raise ValueError("dia desconhecido")
    contador = 0
    posicao = atual
    while contador < passos:
        posicao = sucessor(posicao)
        if posicao == len(dias):
            posicao = 0
        contador = sucessor(contador)
    return dias[posicao]
