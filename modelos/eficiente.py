"""Modelo operacional eficiente para validação externa do PSF-IAminy.

Importante:
- Este ficheiro NÃO é o fundamento formal do projeto.
- O núcleo formal continua em ``nucleo/`` e deriva tudo de V, F, ZERO, S,
  PAR, ITER e Y.
- Este modelo usa inteiros nativos do Python de forma assumida e explícita
  para testar resultados conhecidos maiores, fechar lacunas de desempenho
  e comparar o núcleo puro contra um oráculo independente.
"""
from __future__ import annotations

from math import comb, gcd, isqrt


def eh_primo_int(n: int) -> bool:
    """Primalidade por divisão até sqrt(n)."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = isqrt(n)
    d = 3
    while d <= limite:
        if n % d == 0:
            return False
        d += 2
    return True


def divisores_int(n: int) -> list[int]:
    """Lista ordenada de divisores positivos de n."""
    if n <= 0:
        raise ValueError("divisores_int espera n positivo")
    pequenos: list[int] = []
    grandes: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            pequenos.append(d)
            outro = n // d
            if outro != d:
                grandes.append(outro)
    return pequenos + grandes[::-1]


def soma_divisores_int(n: int) -> int:
    """σ(n): soma de todos os divisores positivos de n."""
    return sum(divisores_int(n))


def soma_divisores_proprios_int(n: int) -> int:
    """Soma dos divisores próprios de n, excluindo o próprio n."""
    return soma_divisores_int(n) - n


def perfeito_int(n: int) -> bool:
    """Número perfeito: n = soma dos seus divisores próprios."""
    return n > 1 and soma_divisores_proprios_int(n) == n


def perfeitos_ate(limite: int) -> list[int]:
    """Todos os números perfeitos até ``limite``."""
    return [n for n in range(1, limite + 1) if perfeito_int(n)]


def mersenne_int(p: int) -> int:
    """M_p = 2^p - 1."""
    if p < 0:
        raise ValueError("expoente de Mersenne deve ser não-negativo")
    return (1 << p) - 1


def eh_mersenne_primo_int(p: int) -> bool:
    """True quando 2^p - 1 é primo."""
    return eh_primo_int(mersenne_int(p))


def catalan_int(n: int) -> int:
    """Número de Catalan C_n = binom(2n,n)/(n+1)."""
    if n < 0:
        raise ValueError("Catalan espera n >= 0")
    return comb(2 * n, n) // (n + 1)


def stirling2_int(n: int, k: int) -> int:
    """Número de Stirling de segunda espécie S(n,k).

    Conta as partições de n elementos rotulados em k blocos não vazios.
    Implementação dinâmica pela recorrência:
        S(n,k) = k*S(n-1,k) + S(n-1,k-1)
    """
    if n < 0 or k < 0:
        raise ValueError("Stirling espera n,k >= 0")
    tabela = [[0] * (k + 2) for _ in range(n + 1)]
    tabela[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            tabela[i][j] = j * tabela[i - 1][j] + tabela[i - 1][j - 1]
    return tabela[n][k]


def linha_stirling2(n: int) -> list[int]:
    """Linha S(n,0)..S(n,n)."""
    return [stirling2_int(n, k) for k in range(n + 1)]


def simplificar_fracao_int(numerador: int, denominador: int) -> tuple[int, int]:
    """Reduz numerador/denominador pelo mdc, com inteiros nativos.

    Equivalente prático de `nucleo.racionais.SIMPLIFICAR`, que opera sobre
    numerais de Church -- correto, mas impraticável para os numeradores e
    denominadores grandes que aparecem em contas reais (ver `reais.py`).
    """
    if denominador == 0:
        raise ValueError("denominador não pode ser zero")
    divisor = gcd(numerador, denominador) or 1
    return numerador // divisor, denominador // divisor


def potencia_racional_int(numerador: int, denominador: int, expoente: int) -> tuple[int, int]:
    """(numerador/denominador)^expoente, simplificado, com inteiros nativos.

    Fecha a mesma lacuna de desempenho que o resto deste ficheiro: a versão
    pura em numerais de Church (`nucleo.racionais.POT_RAC`) é correta, mas
    o numerador/denominador resultante de uma taxa de crescimento típica
    (ex.: base 500, razão 26/25, 3 passos) já cai fora do que Church
    consegue avaliar em tempo prático -- ver o histórico documentado em
    `nucleo/reais.py`.
    """
    if denominador == 0:
        raise ValueError("denominador não pode ser zero")
    if expoente < 0:
        raise ValueError("potencia_racional_int só aceita expoente >= 0")
    return simplificar_fracao_int(numerador**expoente, denominador**expoente)


def porcentagem_de_int(p: int, n: int) -> tuple[int, int]:
    """p% de n, como fração simplificada, com inteiros nativos.

    Equivalente prático de `nucleo.porcentagem.PORCENTAGEM_DE`: medido em
    tempo real, `PORCENTAGEM_DE(15)(240)` (15% de 240) já levou ~100s em
    numerais de Church -- o produto intermédio (3600) é pequeno para
    Python nativo, mas caro demais para multiplicação unária repetida.
    """
    return simplificar_fracao_int(p * n, 100)


def regra_de_tres_direta_int(a: int, b: int, c: int) -> tuple[int, int]:
    """Regra de três simples direta a/b = c/x  =>  x = b*c/a, com inteiros nativos.

    Equivalente prático de `nucleo.proporcionalidade.REGRA_DE_TRES_DIRETA`
    -- mesma razão de existir que `potencia_racional_int`: correto em
    numerais de Church, mas sem garantia de terminar em tempo prático
    fora de exemplos pequenos.
    """
    if a == 0:
        raise ValueError("regra_de_tres_direta_int espera a != 0")
    return simplificar_fracao_int(b * c, a)


def raiz_quadrada_exata_int(n: int) -> int | None:
    """Raiz quadrada inteira de n, só quando n é um quadrado perfeito;
    devolve None caso contrário (nunca aproxima).

    `nucleo.reais.RAIZ_PISO_PURA` já resolve raiz por Newton-Raphson em
    racionais exatos, mas só está testado para um conjunto pequeno de
    alvos (ver histórico nesse ficheiro) -- para o caso comum de exercício
    escolar (hipotenusa com resultado inteiro), checar quadrado perfeito
    com `isqrt` nativo é direto e sempre exato.
    """
    if n < 0:
        raise ValueError("raiz_quadrada_exata_int espera n >= 0")
    raiz = isqrt(n)
    return raiz if raiz * raiz == n else None
