"""Teste de nucleo/ordenacao_finita.py.

Roda com: python3 testes/test_ordenacao_finita.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.ordenacao_finita import esta_ordenada_crescente, ordenar_crescente, ordenar_decrescente

falhas = []


def ok(nome, obtido, esperado):
    passou = obtido == esperado
    print(("[OK]" if passou else "[FALHOU]"), nome, obtido, esperado)
    if not passou:
        falhas.append(nome)


def main():
    print("PSF-IAminy — teste de ordenação finita")

    ok("crescente do exemplo da avaliação", ordenar_crescente([6, 2, 9, 1]), [1, 2, 6, 9])
    ok("decrescente do exemplo da avaliação", ordenar_decrescente([6, 2, 9, 1]), [9, 6, 2, 1])
    ok("lista vazia", ordenar_crescente([]), [])
    ok("um elemento", ordenar_crescente([5]), [5])
    ok("já ordenada", ordenar_crescente([1, 2, 3]), [1, 2, 3])
    ok("ordem inversa", ordenar_crescente([3, 2, 1]), [1, 2, 3])
    ok("com repetidos", ordenar_crescente([4, 1, 4, 2, 1]), [1, 1, 2, 4, 4])
    ok("não modifica a lista original", [6, 2, 9, 1], [6, 2, 9, 1])

    ok("esta_ordenada_crescente true", esta_ordenada_crescente([1, 2, 6, 9]), True)
    ok("esta_ordenada_crescente false", esta_ordenada_crescente([6, 2, 9, 1]), False)
    ok("esta_ordenada_crescente lista vazia", esta_ordenada_crescente([]), True)

    if falhas:
        print("FALHAS", falhas)
        raise SystemExit(1)
    print("Tudo passou.")


if __name__ == "__main__":
    main()
