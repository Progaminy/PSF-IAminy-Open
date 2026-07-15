"""Validação rápida do modelo operacional eficiente.

Roda com:
    python3 testes/test_modelo_eficiente.py

Este teste não substitui o núcleo puro. Ele fecha lacunas que o núcleo
unário não alcança em tempo prático e fornece um oráculo independente para
comparação futura.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from modelos.eficiente import (  # noqa: E402
    catalan_int,
    divisores_int,
    eh_mersenne_primo_int,
    eh_primo_int,
    linha_stirling2,
    mersenne_int,
    perfeito_int,
    perfeitos_ate,
    porcentagem_de_int,
    potencia_racional_int,
    raiz_quadrada_exata_int,
    regra_de_tres_direta_int,
    simplificar_fracao_int,
    soma_divisores_int,
    stirling2_int,
)
from nucleo.porcentagem import PORCENTAGEM_DE
from nucleo.primitivas import F, V
from nucleo.proporcionalidade import REGRA_DE_TRES_DIRETA
from nucleo.racionais import POT_RAC, RAC, SIMPLIFICAR
from nucleo.traducao import de_int, para_int

falhas: list[str] = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"  [{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def main():
    print("=" * 70)
    print("PSF-IAMINY — VALIDAÇÃO DO MODELO OPERACIONAL EFICIENTE")
    print("Núcleo puro preservado; este modelo é fronteira de validação/execução.")
    print("=" * 70)

    print("\n[1] PRIMALIDADE E MERSENNE")
    verificar("97 é primo", eh_primo_int(97), True)
    verificar("2047 não é primo", eh_primo_int(2047), False)
    verificar("Mersenne(11)=2047", mersenne_int(11), 2047)
    verificar("Mersenne primo p=2,3,5,7", [eh_mersenne_primo_int(p) for p in [2, 3, 5, 7]], [True] * 4)
    verificar("Mersenne p=11 é falso", eh_mersenne_primo_int(11), False)
    verificar("Mersenne p=13 é verdadeiro", eh_mersenne_primo_int(13), True)

    print("\n[2] DIVISORES E NÚMEROS PERFEITOS")
    verificar("divisores de 28", divisores_int(28), [1, 2, 4, 7, 14, 28])
    verificar("σ(496)", soma_divisores_int(496), 992)
    verificar("496 é perfeito", perfeito_int(496), True)
    verificar("8128 é perfeito", perfeito_int(8128), True)
    verificar("perfeitos até 10000", perfeitos_ate(10000), [6, 28, 496, 8128])

    print("\n[3] CATALAN E STIRLING")
    verificar("Catalan C0..C10", [catalan_int(n) for n in range(11)], [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796])
    verificar("Stirling S(5,2)", stirling2_int(5, 2), 15)
    verificar("linha Stirling n=5", linha_stirling2(5), [0, 1, 15, 25, 10, 1])

    print("\n[4] FRAÇÕES E POTÊNCIA RACIONAL (oráculo: nucleo.racionais, numerais de Church)")
    verificar("simplificar 8/12", simplificar_fracao_int(8, 12), (2, 3))
    verificar("simplificar 9/4 (já simples)", simplificar_fracao_int(9, 4), (9, 4))

    def _oraculo_pot_rac(num: int, den: int, expoente: int) -> tuple[int, int]:
        r = RAC(de_int(num))(de_int(den))
        resultado = SIMPLIFICAR(POT_RAC(r)(de_int(expoente)))
        return para_int(resultado(V)), para_int(resultado(F))

    for num, den, expoente in [(3, 2, 2), (6, 5, 2), (7, 3, 3)]:
        verificar(
            f"potencia_racional_int({num},{den},{expoente}) == oráculo puro",
            potencia_racional_int(num, den, expoente),
            _oraculo_pot_rac(num, den, expoente),
        )

    # Escala real (crescimento populacional P(t)=500*(1,04)^t, calcular P(3)):
    # fora do que o oráculo em numerais de Church consegue avaliar em tempo
    # prático (ver o histórico documentado em nucleo/reais.py) -- por isso
    # aqui o valor esperado é conferido por conta direta, não pelo oráculo.
    num, den = potencia_racional_int(26, 25, 3)  # 1,04 = 26/25
    verificar("(26/25)^3 simplificado", (num, den), (17576, 15625))
    verificar("500 * (26/25)^3 simplificado", simplificar_fracao_int(500 * num, den), (70304, 125))
    verificar("500 * (26/25)^3 como decimal", 70304 / 125, 562.432)

    print("\n[5] PORCENTAGEM, REGRA DE TRÊS E RAIZ EXATA (oráculo: nucleo, Church)")

    def _oraculo_rac(church_thunk) -> tuple[int, int]:
        resultado = SIMPLIFICAR(church_thunk)
        return para_int(resultado(V)), para_int(resultado(F))

    verificar(
        "porcentagem_de_int(10,20) == oráculo puro",
        porcentagem_de_int(10, 20),
        _oraculo_rac(PORCENTAGEM_DE(de_int(10))(de_int(20))),
    )
    # Escala real (15% de 240): fora do que o oráculo em Church consegue
    # avaliar em tempo prático (~100s medidos nesta mesma sessão) -- por
    # isso conferido por conta direta, não pelo oráculo.
    verificar("porcentagem_de_int(15,240) == 36/1 (36%)", porcentagem_de_int(15, 240), (36, 1))

    verificar(
        "regra_de_tres_direta_int(2,3,5) == oráculo puro",
        regra_de_tres_direta_int(2, 3, 5),
        _oraculo_rac(REGRA_DE_TRES_DIRETA(de_int(2))(de_int(3))(de_int(5))),
    )
    verificar("regra_de_tres_direta_int(2,3,10) — receita 2:3, 10 copos", regra_de_tres_direta_int(2, 3, 10), (15, 1))
    verificar("regra_de_tres_direta_int(3,5,12) — semelhança 3:5, lado 12", regra_de_tres_direta_int(3, 5, 12), (20, 1))

    verificar("raiz_quadrada_exata_int(100)", raiz_quadrada_exata_int(100), 10)
    verificar("raiz_quadrada_exata_int(99) não é quadrado perfeito", raiz_quadrada_exata_int(99), None)

    print("\n" + "=" * 70)
    if falhas:
        print(f"  {len(falhas)} TESTE(S) FALHARAM: {falhas}")
        print("=" * 70)
        sys.exit(1)
    print("  TODOS OS TESTES PASSARAM")
    print("=" * 70)


if __name__ == "__main__":
    main()
