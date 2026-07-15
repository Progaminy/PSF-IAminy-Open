"""Testes da Combinatória Natural PSF-IAminy.
Roda com: python3 testes/test_combinatoria_natural.py

Etapas validadas: 36 a 60.
"""
import ast
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.traducao import de_int, para_bool, para_int
from nucleo.combinatoria_natural import (
    PRINCIPIO_ADITIVO_PURO,
    PRINCIPIO_MULTIPLICATIVO_PURO,
    ESCOLHAS_ORDENADAS_COM_REPETICAO_PURO,
    FATORIAL_NATURAL_PURO,
    PERMUTACOES_SIMPLES_PURO,
    ARRANJOS_SIMPLES_PURO,
    COMBINACOES_SIMPLES_PURO,
    BINOMIAL_PASCAL_PURO,
    BINOMIAL_SIMETRIA_CONFERE_PURO,
    BINOMIO_EXPANSAO_SOMA_PURO,
    BINOMIO_CONFERE_PURO,
    INCLUSAO_EXCLUSAO_DOIS_PURO,
    PA_TERMO_PURO,
    PG_TERMO_PURO,
    FIBONACCI_NATURAL_PURO,
    LUCAS_NATURAL_PURO,
    TRIANGULAR_NATURAL_PURO,
    QUADRADO_NATURAL_PURO,
    PENTAGONAL_NATURAL_PURO,
    HEXAGONAL_NATURAL_PURO,
    CATALAN_NATURAL_PURO,
    STIRLING2_NATURAL_PURO,
    BELL_NATURAL_PURO,
    PARTICOES_INTEIRAS_PURO,
    FATORIAL_MODULAR_PURO,
    BINOMIAL_MODULAR_PURO,
    FIBONACCI_MODULAR_PURO,
    COMBINATORIA_FECHA_BLOCO_PURO,
)
from motor.fluxo import relatorio_fluxo, proxima_etapa_natural

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def n(x):
    return de_int(x)


def i(x):
    return para_int(x)


def b(x):
    return para_bool(x)


def verificar_motor_e_pureza():
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "combinatoria_natural.py")
    with open(caminho, "r", encoding="utf-8") as f:
        arvore = ast.parse(f.read(), filename=caminho)
    nomes_proibidos = {
        "DIV", "MOD", "MMC", "COMBINACAO_SIMPLES", "CATALAN", "STIRLING2"
    }
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em combinatoria_natural.py")
        if isinstance(no, ast.Name) and no.id in nomes_proibidos:
            falhas.append(f"nome proibido {no.id} em combinatoria_natural.py")

    r = relatorio_fluxo()
    verificar("motor avançou pelo menos até 60", r["maior_etapa"] >= 60, True)
    verificar("motor sem lacunas até a etapa atual", r["faltando_ate_maior"], [])
    verificar("próxima etapa depois de 60 é 61", proxima_etapa_natural(60)[0], 61)


def main():
    print("PSF-IAminy — Combinatória Natural, Etapas 36 a 60")
    verificar_motor_e_pureza()

    verificar("princípio aditivo 3+4", i(PRINCIPIO_ADITIVO_PURO(n(3))(n(4))), 7)
    verificar("princípio multiplicativo 3*4", i(PRINCIPIO_MULTIPLICATIVO_PURO(n(3))(n(4))), 12)
    verificar("escolhas ordenadas com repetição 3^4", i(ESCOLHAS_ORDENADAS_COM_REPETICAO_PURO(n(3))(n(4))), 81)

    verificar("0!", i(FATORIAL_NATURAL_PURO(n(0))), 1)
    verificar("5!", i(FATORIAL_NATURAL_PURO(n(5))), 120)
    verificar("permutações simples 4", i(PERMUTACOES_SIMPLES_PURO(n(4))), 24)
    verificar("arranjos A(5,2)", i(ARRANJOS_SIMPLES_PURO(n(5))(n(2))), 20)
    verificar("arranjos A(2,5) sentinela", i(ARRANJOS_SIMPLES_PURO(n(2))(n(5))), 0)
    verificar("combinações C(5,2)", i(COMBINACOES_SIMPLES_PURO(n(5))(n(2))), 10)
    verificar("Pascal C(5,2)", i(BINOMIAL_PASCAL_PURO(n(5))(n(2))), 10)
    verificar("simetria binomial C(5,2)=C(5,3)", b(BINOMIAL_SIMETRIA_CONFERE_PURO(n(5))(n(2))), True)

    verificar("binómio expansão n=3 a=2 b=1", i(BINOMIO_EXPANSAO_SOMA_PURO(n(3))(n(2))(n(1))), 27)
    verificar("binómio confere n=3 a=2 b=1", b(BINOMIO_CONFERE_PURO(n(3))(n(2))(n(1))), True)
    verificar("inclusão-exclusão 5+7-2", i(INCLUSAO_EXCLUSAO_DOIS_PURO(n(5))(n(7))(n(2))), 10)

    verificar("PA a0=2 d=3 n=4", i(PA_TERMO_PURO(n(2))(n(3))(n(4))), 14)
    verificar("PG a0=2 r=3 n=4", i(PG_TERMO_PURO(n(2))(n(3))(n(4))), 162)
    verificar("Fibonacci 7", i(FIBONACCI_NATURAL_PURO(n(7))), 13)
    verificar("Lucas 5", i(LUCAS_NATURAL_PURO(n(5))), 11)

    verificar("triangular 5", i(TRIANGULAR_NATURAL_PURO(n(5))), 15)
    verificar("quadrado 5", i(QUADRADO_NATURAL_PURO(n(5))), 25)
    verificar("pentagonal 4", i(PENTAGONAL_NATURAL_PURO(n(4))), 22)
    verificar("hexagonal 4", i(HEXAGONAL_NATURAL_PURO(n(4))), 28)

    verificar("Catalan 4", i(CATALAN_NATURAL_PURO(n(4))), 14)
    verificar("Stirling S(5,2)", i(STIRLING2_NATURAL_PURO(n(5))(n(2))), 15)
    verificar("Bell 4", i(BELL_NATURAL_PURO(n(4))), 15)
    verificar("partições inteiras de 5", i(PARTICOES_INTEIRAS_PURO(n(5))), 7)

    verificar("5! mod 7", i(FATORIAL_MODULAR_PURO(n(5))(n(7))), 1)
    verificar("C(5,2) mod 7", i(BINOMIAL_MODULAR_PURO(n(5))(n(2))(n(7))), 3)
    verificar("Fib(7) mod 5", i(FIBONACCI_MODULAR_PURO(n(7))(n(5))), 3)
    verificar("fechamento combinatório n=5", b(COMBINATORIA_FECHA_BLOCO_PURO(n(5))), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
