"""Distância de edição entre formas de texto.

`distancia_levenshtein` é a lógica que antes vivia, privada, dentro de
`lexico.py` — só foi realocada para aqui para poder ser reaproveitada por
outros módulos (índice fuzzy, canal ruidoso) sem duplicação.

`distancia_damerau_levenshtein` acrescenta o caso que Levenshtein simples
não cobre: transposição de duas letras adjacentes conta como um único erro
(ex.: "hte" -> "the"), não dois. É a distância certa para erros de digitação
reais, onde trocar a ordem de duas teclas vizinhas é o erro mais comum.

Ambas são algoritmos determinísticos clássicos de programação dinâmica —
nenhuma treina, nenhuma depende de dado externo.
"""
from __future__ import annotations


def distancia_levenshtein(a: str, b: str, limite: int | None = None) -> int:
    """Distância de Levenshtein (inserção/remoção/substituição) com corte opcional."""
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    anterior = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        atual = [i]
        minimo = i
        for j, cb in enumerate(b, 1):
            custo = 0 if ca == cb else 1
            valor = min(atual[-1] + 1, anterior[j] + 1, anterior[j - 1] + custo)
            atual.append(valor)
            minimo = min(minimo, valor)
        if limite is not None and minimo > limite:
            return limite + 1
        anterior = atual
    return anterior[-1]


def distancia_damerau_levenshtein(a: str, b: str, limite: int | None = None) -> int:
    """Damerau-Levenshtein restrita: Levenshtein + transposição adjacente custo 1.

    "Restrita" (optimal string alignment) significa que cada substring só
    pode ser transposta uma vez — é a variante padrão usada em corretores
    ortográficos, mais simples que a Damerau-Levenshtein completa e
    suficiente para o caso real de erro de digitação.
    """
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    len_a, len_b = len(a), len(b)
    # Tabela completa (não só duas linhas) porque a transposição olha duas
    # linhas para trás — precisamos de dp[i-2][j-2].
    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    for i in range(len_a + 1):
        dp[i][0] = i
    for j in range(len_b + 1):
        dp[0][j] = j
    for i in range(1, len_a + 1):
        minimo_linha = dp[i][0]
        for j in range(1, len_b + 1):
            custo = 0 if a[i - 1] == b[j - 1] else 1
            valor = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + custo,
            )
            if (
                i > 1
                and j > 1
                and a[i - 1] == b[j - 2]
                and a[i - 2] == b[j - 1]
            ):
                valor = min(valor, dp[i - 2][j - 2] + 1)
            dp[i][j] = valor
            minimo_linha = min(minimo_linha, valor)
        if limite is not None and minimo_linha > limite:
            return limite + 1
    return dp[len_a][len_b]
