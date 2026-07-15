"""
PSF-IAminy — a "caixa potente" ⟦ ⟧: um único símbolo para radiciação e logaritmo.

Uso:
    >>> caixa(2, 3)          # ⟦2, 3⟧  = ?      -> potenciação:   2**3
    8
    >>> caixa(None, 3, 8)    # ⟦?, 3⟧  = 8       -> radiciação:    raiz cúbica de 8
    2
    >>> caixa(2, None, 8)    # ⟦2, ?⟧  = 8       -> logaritmo:     log base 2 de 8
    3

Só uma função, três "portas de entrada" — exatamente a proposta da Aula 18:
"por que não criar um símbolo único que gere os dois valores da operação?"

Esta é a única camada do projeto que fala em `int` nativo do Python; por
baixo, tudo é resolvido pelas 5 primitivas em `nucleo/`.
"""
from nucleo.traducao import de_int, para_int
from nucleo.inversa_potencia import (
    INV_BASE, INV_EXPO, EXISTE_RAIZ_EXATA, EXISTE_LOG_EXATO,
)
from nucleo.aritmetica import POT
from nucleo.reais import RAIZ_QUADRADA_RAC_N
from nucleo.racionais import NUM, DEN


class SemSolucaoExata(Exception):
    """Lançada quando não existe base/expoente inteiro exato para a caixa."""


def caixa(a: int | None = None, b: int | None = None, c: int | None = None) -> int:
    """
    A "caixa potente" ⟦a, b⟧ = c. Exatamente UM dos três argumentos deve
    ser None (o "?" da Aula 18) — essa é a incógnita que a função resolve.

      caixa(a, b, None)  ->  potenciação:  c = a**b
      caixa(None, b, c)  ->  radiciação:   a = b-ésima raiz de c
      caixa(a, None, c)  ->  logaritmo:    b = log_a(c)
    """
    incognitas = [x is None for x in (a, b, c)]
    if sum(incognitas) != 1:
        raise ValueError(
            "Exatamente um dos três valores (a, b ou c) deve ser None — "
            "essa é a posição do '?' na caixa ⟦ ⟧."
        )

    if c is None:  # ⟦a, b⟧ = ?  -> potenciação direta
        return para_int(POT(de_int(a))(de_int(b)))

    if a is None:  # ⟦?, b⟧ = c  -> radiciação disfarçada
        if not para_int(EXISTE_RAIZ_EXATA(de_int(b))(de_int(c))):
            raise SemSolucaoExata(
                f"Não existe raiz {b}-ésima inteira exata de {c}."
            )
        return para_int(INV_BASE(de_int(b))(de_int(c)))

    # b is None: ⟦a, ?⟧ = c  -> logaritmo disfarçado
    if not para_int(EXISTE_LOG_EXATO(de_int(a))(de_int(c))):
        raise SemSolucaoExata(f"Não existe log inteiro exato de {c} na base {a}.")
    return para_int(INV_EXPO(de_int(a))(de_int(c)))


# Alvos verificados (tempo e precisão testados — ver nucleo/reais.py e
# testes/test_nucleo.py). NÃO é uma lista de "valores permitidos" — é
# só o que foi de fato confirmado até agora, com o chute inicial
# melhorado (RAIZ_PISO_PURA) e a lógica adaptativa abaixo (2 iterações
# primeiro, 3 só se preciso).
_ALVOS_VERIFICADOS = {2, 3, 5, 8, 9, 10, 11, 12, 20}


def _precisao_suficiente(p: int, q: int, alvo: int) -> bool:
    """|p/q - √alvo| < 0.0005, testado em aritmética inteira exata (sem
    float): equivalente a |p²-alvo·q²|·1000 < p·q (ver derivação no
    histórico desta função — mesma disciplina de nunca usar float, mesmo
    aqui na fronteira, onde já teríamos "licença" para isso)."""
    return abs(p * p - alvo * q * q) * 1000 < p * q


def raiz_quadrada_aproximada(alvo: int) -> str:
    """
    APROXIMAÇÃO de √alvo com exatamente 3 casas decimais — DIFERENTE de
    `caixa()`, que só devolve resultados EXATOS (e lança SemSolucaoExata
    quando não existem). Esta função nunca finge exatidão: o retorno é
    uma STRING ("1.414", não um número), precisamente para não ser
    confundida com um resultado exato em nenhum código que a chame.

    Por baixo: Newton-Raphson em RACIONAIS EXATOS (nucleo/reais.py),
    partindo de ⌊√alvo⌋ (não de alvo — chute muito melhor, ver
    nucleo/reais.py). Tenta primeiro com 2 iterações; só usa uma 3ª se a
    precisão de 2 não bastar. O núcleo nunca usa float — só a checagem
    de precisão e o arredondamento final usam inteiros nativos do
    Python, e só porque nesse ponto os números já são pequenos.

    ESCOPO HONESTO: verificado rápido e correto para alvo em
    {2,3,5,8,9,10,11,12,20} (testado explicitamente — ver
    nucleo/reais.py para os tempos de cada um). Outros valores (6, 7,
    13, 15, 17, ...) foram testados e FALHAM na mesma janela de tempo —
    a causa continua a ser que numerais de Church não têm predecessor
    em O(1). Chamar isto fora do conjunto verificado ainda funciona
    matematicamente, mas sem garantia de tempo.
    """
    if alvo not in _ALVOS_VERIFICADOS:
        import sys
        print(
            f"aviso: alvo={alvo} não está no conjunto verificado {sorted(_ALVOS_VERIFICADOS)} — "
            "pode ser lento (segundos a minutos) ou impreciso. Ver nucleo/reais.py.",
            file=sys.stderr,
        )

    for n_iteracoes_int in (2, 3):
        n_iteracoes = de_int(n_iteracoes_int)
        r = RAIZ_QUADRADA_RAC_N(de_int(alvo))(n_iteracoes)
        p, q = para_int(NUM(r)), para_int(DEN(r))
        if _precisao_suficiente(p, q, alvo):
            break

    # arredondamento ao milésimo mais próximo, em aritmética inteira pura
    # (sem float): round(p*1000/q) == (p*1000 + q//2) // q para q par ou
    # ímpar, arredondamento "meio para cima".
    milesimos = (p * 1000 + q // 2) // q
    return f"{milesimos // 1000}.{milesimos % 1000:03d}"


if __name__ == "__main__":
    print("⟦2, 3⟧ = ?  ->", caixa(2, 3, None), " (potenciação: 2^3)")
    print("⟦?, 3⟧ = 8  ->", caixa(None, 3, 8), " (radiciação: raiz cúbica de 8)")
    print("⟦2, ?⟧ = 8  ->", caixa(2, None, 8), " (logaritmo: log base 2 de 8)")
    print("√2 ≈", raiz_quadrada_aproximada(2), " (real: 1.41421356...)")
    print("√3 ≈", raiz_quadrada_aproximada(3), " (real: 1.73205081...)")
