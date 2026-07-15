"""
PSF-IAminy — estatística descritiva (média, mediana, moda).

POR QUE ISTO NÃO ESTÁ EM nucleo/ como o resto: média/mediana/moda operam
sobre uma coleção de TAMANHO VARIÁVEL. O núcleo puro representa listas
como pares cons/nil (PAR/F) — mas F já é usado como "falso" booleano, e
um par PAR(cabeça)(cauda) tem exatamente a mesma forma de aplicação que
F quando invocado com dois argumentos. Não dá para distinguir "isto é a
lista vazia" de "isto é uma célula real" só por aplicação — só por
identidade do objeto (`is F`), que é uma verificação do Python, não uma
operação pura de lambda calculus. Isto já apareceu antes (ver o comentário
em `nucleo/proporcionalidade.DIVISAO_PROPORCIONAL_3`, que por isso usa
aridade fixa em vez de uma lista genérica).

Em vez de fingir que é "puro" com um truque, a fronteira é explícita: esta
função aceita uma lista Python comum, converte cada elemento com de_int
(entrando no núcleo), faz a SOMA com a aritmética genuína do núcleo, e só
usa Python nativo para o que é genuinamente periférico — iterar "quantos
elementos há" (mediana precisa disso para ordenar) e contar frequências
(moda). Mesmo espírito de caixa.py: fronteira fina, núcleo puro por baixo.
"""
from collections import Counter

from nucleo.traducao import de_int, para_int, para_rac
from nucleo.racionais import RAC
from nucleo.aritmetica import SOMA


def media(valores: list[int]) -> str:
    """Tópico 598: média aritmética, como racional exato (não arredondado)."""
    if not valores:
        raise ValueError("média de lista vazia não está definida")
    total = de_int(0)
    for v in valores:
        total = SOMA(total)(de_int(v))
    return para_rac(RAC(total)(de_int(len(valores))))


def mediana(valores: list[int]) -> float:
    """Tópico 599: mediana. A ORDENAÇÃO é feita em Python (não há
    algoritmo de ordenação no núcleo puro — ordenar é uma estrutura de
    dados nova, fora do escopo desta versão); a aritmética final (média
    dos dois centrais, quando a lista tem tamanho par) usa o núcleo."""
    if not valores:
        raise ValueError("mediana de lista vazia não está definida")
    ordenado = sorted(valores)
    n = len(ordenado)
    meio = n // 2
    if n % 2 == 1:
        return float(ordenado[meio])
    par = SOMA(de_int(ordenado[meio - 1]))(de_int(ordenado[meio]))
    return para_int(par) / 2


def moda(valores: list[int]) -> list[int]:
    """Tópico 600: moda — valor(es) mais frequente(s). Contagem de
    frequência via collections.Counter (bookkeeping periférico sobre
    inteiros Python já materializados, não uma reivindicação de que a
    contagem em si vem das 5 primitivas — ver nota no topo do ficheiro)."""
    if not valores:
        raise ValueError("moda de lista vazia não está definida")
    contagem = Counter(valores)
    maior_freq = max(contagem.values())
    return sorted(v for v, freq in contagem.items() if freq == maior_freq)


if __name__ == "__main__":
    dados = [4, 8, 6, 5, 3, 8, 9, 8]
    print("dados:", dados)
    print("média:", media(dados))
    print("mediana:", mediana(dados))
    print("moda:", moda(dados))
