"""Testes do gerador de exercícios com variação automática (ensino/exercicios.py).

Cobre a lacuna descrita no plano público: antes, os exercícios de cada
pacote eram sempre o mesmo texto fixo em curriculos.py. A semente torna a
variação reprodutível -- mesma semente, mesmo resultado -- para os testes
ficarem determinísticos mesmo usando random.Random por baixo.

Roda com: python3 testes/test_exercicios_variados.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ensino import GeradorExercicios, MotorAulas
from ensino.tipos import PacoteConhecimento
from motor import MotorGeralIAMiny

falhas = []


def ok(nome, obtido, esperado):
    passou = obtido == esperado
    print(("[OK]" if passou else "[FALHOU]"), nome, obtido, esperado)
    if not passou:
        falhas.append(nome)


def main():
    print("PSF-IAminy — teste do gerador de exercícios com variação")

    aulas = MotorAulas()

    ok(
        "MAT-006 semente 1 é reproduzível",
        aulas.exercicios_variados("matematica", "MAT-006", 3, 1),
        (
            "Junte 1 lápis com 2 lápis e conte o total.",
            "Junte 1 lápis com 2 lápis e conte o total.",
            "Junte 1 pedra com 3 pedras e conte o total.",
        ),
    )
    ok(
        "MAT-006 semente 1, chamada de novo, dá o mesmo resultado",
        aulas.exercicios_variados("matematica", "MAT-006", 3, 1),
        aulas.exercicios_variados("matematica", "MAT-006", 3, 1),
    )
    ok(
        "MAT-006 semente 2 dá resultado diferente da semente 1",
        aulas.exercicios_variados("matematica", "MAT-006", 3, 2) == aulas.exercicios_variados("matematica", "MAT-006", 3, 1),
        False,
    )
    ok(
        "POR-002 semente 7 qtd 4",
        aulas.exercicios_variados("portugues", "POR-002", 4, 7),
        (
            "Escreva a letra B e diga uma palavra que começa com ela.",
            "Escreva a letra A e diga uma palavra que começa com ela.",
            "Escreva a letra S e diga uma palavra que começa com ela.",
            "Escreva a letra C e diga uma palavra que começa com ela.",
        ),
    )
    ok("quantidade respeitada", len(aulas.exercicios_variados("matematica", "MAT-001", 5, 3)), 5)

    # todos os 10+10 pacotes iniciais têm modelo -- ninguém deveria cair no
    # texto fixo por falta de cobertura.
    gerador = GeradorExercicios()
    for area in ("matematica", "portugues"):
        for pacote in aulas.curriculo(area):
            ok(f"{pacote.codigo} tem modelo de exercício", gerador.tem_modelo(pacote.codigo), True)

    # fallback: um pacote sem modelo registrado devolve os exercícios fixos
    # do próprio pacote, sem erro.
    pacote_falso = PacoteConhecimento(
        codigo="MAT-999",
        area="matematica",
        nivel=99,
        titulo="Pacote sem modelo",
        objetivo="testar fallback",
        pre_requisitos=(),
        palavras_chave=(),
        passos=(),
        explicacao="",
        exemplos=(),
        exercicios=("exercício fixo 1", "exercício fixo 2"),
        desmontagem=(),
    )
    ok("pacote sem modelo nao esta registrado", gerador.tem_modelo("MAT-999"), False)
    ok(
        "sem modelo, devolve os exercicios fixos do pacote",
        gerador.gerar(pacote_falso, quantidade=3, semente=1),
        ("exercício fixo 1", "exercício fixo 2"),
    )

    # integração com o motor geral.
    geral = MotorGeralIAMiny()
    ok(
        "motor geral exercicios_variados",
        geral.exercicios_variados("matematica", "MAT-006", 3, 1),
        aulas.exercicios_variados("matematica", "MAT-006", 3, 1),
    )

    if falhas:
        print("FALHAS", falhas)
        raise SystemExit(1)
    print("Tudo passou.")


if __name__ == "__main__":
    main()
