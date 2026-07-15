"""Contas armadas — soma e subtração em colunas, como no papel escolar.

A aritmética escolar nativa (Etapa 31) já constrói soma e subtração por
sucessão/retirada repetida, mas devolve só o resultado final — não a conta
armada que a criança escreve no papel, coluna por coluna, com "vai um" e
"empresta um" visíveis. Este módulo constrói essa camada, dígito a dígito,
e confere cada resultado contra a soma/subtração já provada na Etapa 31:
a conta armada não é uma segunda fonte de verdade, é uma forma de mostrar
o mesmo resultado já provado, com o procedimento visível.

Nenhum `//`, `%` ou `**` nativo é usado para os dígitos: `dividir_com_resto`
(Etapa 31) extrai dígitos por subtração repetida, na mesma linha.
"""
from __future__ import annotations

from dataclasses import dataclass

from .aritmetica_escolar_nativa import (
    dividir_com_resto,
    multiplicar,
    somar,
    subtrair,
    validar_natural,
)


def digitos(n: int) -> tuple[int, ...]:
    """Dígitos de n da esquerda para a direita (mais significativo primeiro).

    Ler os dígitos de um numeral escrito não é, em si, a conta armada — é
    o mesmo passo que uma criança faz olhando o número, antes de armar a
    conta. Por isso usa a leitura direta dos algarismos, não
    `dividir_com_resto` (Etapa 31): esse repartidor chama `subtrair`, que
    chama `predecessor`, que busca por sucessão a partir de zero a cada
    chamada — seguro para números pequenos, mas custa mais a cada
    algarismo a mais (testado: decompor 9801 assim passa de um minuto). O
    vai-um, o empréstimo, o produto parcial e o dígito trazido — a conta
    em si — continuam por `dividir_com_resto` sobre valores de uma
    coluna, nunca sobre o número inteiro.
    """
    validar_natural(n)
    return tuple(int(c) for c in str(n))


def _valor_a_partir_dos_digitos(digitos_unidades_primeiro: list[int]) -> int:
    valor = 0
    potencia = 1
    for digito in digitos_unidades_primeiro:
        valor = somar(valor, _vezes_potencia(digito, potencia))
        potencia = _vezes_potencia(potencia, 10)
    return valor


def _vezes_potencia(digito: int, potencia: int) -> int:
    """digito * potencia construído por soma repetida (sem `*` nativo)."""
    total = 0
    contador = 0
    while contador < digito:
        total = somar(total, potencia)
        contador = somar(contador, 1)
    return total


@dataclass(frozen=True, slots=True)
class ColunaSomaArmada:
    posicao: int
    digito_a: int
    digito_b: int
    vem_um: int
    digito_resultado: int
    vai_um: int


@dataclass(frozen=True, slots=True)
class RegistroSomaArmada:
    a: int
    b: int
    colunas: tuple[ColunaSomaArmada, ...]
    resultado: int

    def texto(self) -> str:
        largura = len(str(self.resultado)) + 2
        return "\n".join((
            f"  {self.a}".rjust(largura),
            f"+ {self.b}".rjust(largura),
            "-" * largura,
            f"  {self.resultado}".rjust(largura),
        ))


def soma_armada(a: int, b: int) -> RegistroSomaArmada:
    validar_natural(a, "a")
    validar_natural(b, "b")
    digitos_a = list(reversed(digitos(a)))  # unidades primeiro
    digitos_b = list(reversed(digitos(b)))
    tamanho = max(len(digitos_a), len(digitos_b))
    colunas: list[ColunaSomaArmada] = []
    digitos_resultado: list[int] = []
    vai_um = 0
    for posicao in range(tamanho):
        da = digitos_a[posicao] if posicao < len(digitos_a) else 0
        db = digitos_b[posicao] if posicao < len(digitos_b) else 0
        soma_coluna = somar(somar(da, db), vai_um)
        novo_vai_um, digito_resultado = dividir_com_resto(soma_coluna, 10)
        colunas.append(ColunaSomaArmada(posicao, da, db, vai_um, digito_resultado, novo_vai_um))
        digitos_resultado.append(digito_resultado)
        vai_um = novo_vai_um
    if vai_um > 0:
        digitos_resultado.append(vai_um)
    resultado = _valor_a_partir_dos_digitos(digitos_resultado)
    esperado = somar(a, b)
    if resultado != esperado:
        raise ValueError("conta armada divergiu da soma já provada por sucessão repetida")
    return RegistroSomaArmada(a, b, tuple(colunas), resultado)


@dataclass(frozen=True, slots=True)
class ColunaSubtracaoArmada:
    posicao: int
    digito_a: int
    digito_b: int
    emprestou: bool
    digito_resultado: int


@dataclass(frozen=True, slots=True)
class RegistroSubtracaoArmada:
    a: int
    b: int
    colunas: tuple[ColunaSubtracaoArmada, ...]
    resultado: int

    def texto(self) -> str:
        largura = len(str(self.a)) + 2
        return "\n".join((
            f"  {self.a}".rjust(largura),
            f"- {self.b}".rjust(largura),
            "-" * largura,
            f"  {self.resultado}".rjust(largura),
        ))


def subtracao_armada(a: int, b: int) -> RegistroSubtracaoArmada:
    validar_natural(a, "a")
    validar_natural(b, "b")
    if b > a:
        raise ValueError("subtração armada escolar não admite retirar mais do que existe")
    digitos_a = list(reversed(digitos(a)))  # unidades primeiro
    digitos_b = list(reversed(digitos(b)))
    tamanho = max(len(digitos_a), len(digitos_b))
    colunas: list[ColunaSubtracaoArmada] = []
    digitos_resultado: list[int] = []
    emprestimo = 0
    for posicao in range(tamanho):
        da = digitos_a[posicao] if posicao < len(digitos_a) else 0
        db = digitos_b[posicao] if posicao < len(digitos_b) else 0
        db_com_emprestimo = somar(db, emprestimo)
        if da >= db_com_emprestimo:
            digito_resultado = subtrair(da, db_com_emprestimo)
            proximo_emprestimo = 0
        else:
            digito_resultado = subtrair(somar(da, 10), db_com_emprestimo)
            proximo_emprestimo = 1
        colunas.append(
            ColunaSubtracaoArmada(posicao, da, db, bool(proximo_emprestimo), digito_resultado)
        )
        digitos_resultado.append(digito_resultado)
        emprestimo = proximo_emprestimo
    resultado = _valor_a_partir_dos_digitos(digitos_resultado)
    esperado = subtrair(a, b)
    if resultado != esperado:
        raise ValueError("conta armada divergiu da subtração já provada por retirada repetida")
    return RegistroSubtracaoArmada(a, b, tuple(colunas), resultado)


def _linha_parcial_digitos(digitos_a_unidades_primeiro: list[int], digito_multiplicador: int) -> list[int]:
    """a × dígito único, dígito a dígito com vai-um — a tabuada armada de uma linha."""
    resultado: list[int] = []
    vai_um = 0
    for da in digitos_a_unidades_primeiro:
        produto_coluna = somar(_vezes_potencia(da, digito_multiplicador), vai_um)
        vai_um, digito_resultado = dividir_com_resto(produto_coluna, 10)
        resultado.append(digito_resultado)
    if vai_um > 0:
        resultado.append(vai_um)
    return resultado


@dataclass(frozen=True, slots=True)
class LinhaParcialMultiplicacao:
    posicao: int
    digito_multiplicador: int
    valor: int


@dataclass(frozen=True, slots=True)
class RegistroMultiplicacaoArmada:
    a: int
    b: int
    linhas: tuple[LinhaParcialMultiplicacao, ...]
    resultado: int

    def texto(self) -> str:
        largura = len(str(self.resultado)) + 2
        linhas_texto = [f"  {self.a}".rjust(largura), f"x {self.b}".rjust(largura), "-" * largura]
        for linha in self.linhas:
            linhas_texto.append(f"  {linha.valor}".rjust(largura))
        linhas_texto.append("-" * largura)
        linhas_texto.append(f"  {self.resultado}".rjust(largura))
        return "\n".join(linhas_texto)


def multiplicacao_armada(a: int, b: int) -> RegistroMultiplicacaoArmada:
    """Multiplicação por linhas parciais deslocadas, como no papel escolar.

    Cada dígito de `b` gera uma linha parcial (`a` × esse dígito, com
    vai-um), a linha é deslocada para a casa certa preenchendo zeros à
    direita, e todas as linhas deslocadas são somadas com `soma_armada` —
    reaproveitada, não reinventada. O resultado é conferido contra
    `multiplicar` (Etapa 31, soma repetida), a fonte de verdade original.
    """
    validar_natural(a, "a")
    validar_natural(b, "b")
    digitos_a = list(reversed(digitos(a)))
    digitos_b = list(reversed(digitos(b)))
    linhas: list[LinhaParcialMultiplicacao] = []
    valores_deslocados: list[int] = []
    for posicao, digito_multiplicador in enumerate(digitos_b):
        digitos_linha = _linha_parcial_digitos(digitos_a, digito_multiplicador)
        digitos_deslocados = [0] * posicao + digitos_linha
        valor_linha = _valor_a_partir_dos_digitos(digitos_deslocados)
        linhas.append(LinhaParcialMultiplicacao(posicao, digito_multiplicador, valor_linha))
        valores_deslocados.append(valor_linha)
    resultado = 0
    for valor in valores_deslocados:
        resultado = soma_armada(resultado, valor).resultado
    esperado = multiplicar(a, b)
    if resultado != esperado:
        raise ValueError("conta armada divergiu da multiplicação já provada por soma repetida")
    return RegistroMultiplicacaoArmada(a, b, tuple(linhas), resultado)


@dataclass(frozen=True, slots=True)
class ColunaDivisaoArmada:
    posicao: int
    digito_trazido: int
    resto_antes: int
    digito_quociente: int
    resto_depois: int


@dataclass(frozen=True, slots=True)
class RegistroDivisaoArmada:
    dividendo: int
    divisor: int
    colunas: tuple[ColunaDivisaoArmada, ...]
    quociente: int
    resto: int

    def texto(self) -> str:
        return f"{self.dividendo} ÷ {self.divisor} = {self.quociente} resto {self.resto}"


def divisao_armada(dividendo: int, divisor: int) -> RegistroDivisaoArmada:
    """Divisão longa trazendo um dígito de cada vez, como no papel escolar.

    Cada passo traz o próximo dígito do dividendo (resto_parcial×10+dígito)
    e `dividir_com_resto` (Etapa 31) responde quantas vezes o divisor cabe
    e o que sobra — a mesma pergunta que a criança faz a cada coluna. O
    dígito do quociente sai sempre entre 0 e 9 porque o resto parcial,
    antes de trazer o próximo dígito, já é menor que o divisor por
    construção (invariante mantida a cada passo).
    """
    validar_natural(dividendo, "dividendo")
    validar_natural(divisor, "divisor")
    if divisor == 0:
        raise ValueError("não existe divisão por zero")
    colunas: list[ColunaDivisaoArmada] = []
    digitos_quociente: list[int] = []
    resto_parcial = 0
    for posicao, digito in enumerate(digitos(dividendo)):
        resto_antes = resto_parcial
        trazido = somar(_vezes_potencia(resto_parcial, 10), digito)
        digito_quociente, resto_parcial = dividir_com_resto(trazido, divisor)
        colunas.append(ColunaDivisaoArmada(posicao, digito, resto_antes, digito_quociente, resto_parcial))
        digitos_quociente.append(digito_quociente)
    quociente = _valor_a_partir_dos_digitos(list(reversed(digitos_quociente)))
    esperado = somar(multiplicar(quociente, divisor), resto_parcial)
    if esperado != dividendo:
        raise ValueError("conta armada divergiu: quociente×divisor+resto não reconstrói o dividendo")
    return RegistroDivisaoArmada(dividendo, divisor, tuple(colunas), quociente, resto_parcial)
