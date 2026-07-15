"""
Suite de testes do PSF-IAminy. Roda com: python3 testes/test_nucleo.py
Não usa pytest nem nenhuma dependência externa — só a biblioteca padrão —
para manter o espírito "zero dependências" do projeto.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.primitivas import V, F
from nucleo.logica import DE_MORGAN_1, DE_MORGAN_2, IMPLICA, SSE
from nucleo.aritmetica import SOMA, SUB, MULT, POT, DIV, MOD, MDC, MMC, IGUAL, MENOR
from nucleo.primos import EH_PRIMO, PRIMO_N, DECOMPOR, TOTIENTE, COPRIMOS
from nucleo.racionais import RAC, EQ_RAC, SOMA_RAC
from nucleo.geometria import PONTO, DIST_MANHATTAN, ALINHADOS, PERPENDICULARES, PARALELAS
from nucleo.inteiros import DE_NATURAL, SUB_INT, EQ_INT
from nucleo.predicados import PARA_TODO, EXISTE
from nucleo.calculo_discreto import SOMATORIO, PRODUTORIO, FATORIAL, VERIFICAR_INDUCAO, FIBONACCI
from nucleo.reais import RAIZ_QUADRADA_RAC
from nucleo.divisores import (
    MULTIPLO, EH_COMPOSTO, LISTA_DIVISORES, QTD_DIVISORES, SOMA_DIVISORES,
    PRODUTO_DIVISORES, PERFEITO, CONGRUENTE, MERSENNE, EH_MERSENNE_PRIMO,
    FERMAT, EH_TERNA_PITAGORICA,
)
from nucleo.numeros_figurados import TRIANGULAR, QUADRADO_FIGURADO, PENTAGONAL, HEXAGONAL
from nucleo.harmonicos import HARMONICO
from nucleo.racionais import SUB_RAC, DIV_RAC, RECIPROCO_RAC
from nucleo.porcentagem import PORCENTAGEM_DE, AUMENTAR_PERCENTUAL, DIMINUIR_PERCENTUAL
from nucleo.proporcionalidade import (
    RAZAO, EH_PROPORCAO, REGRA_DE_TRES_DIRETA, REGRA_DE_TRES_INVERSA,
    REGRA_DE_TRES_COMPOSTA_2, DIVISAO_PROPORCIONAL_3, ESCALA, DISTANCIA_REAL, DISTANCIA_MAPA,
)
from nucleo.inteiros import DE_NATURAL, SUB_INT, EQ_INT, OPOSTO_INT
from nucleo.binario import PARA_BINARIO, DE_BINARIO
from nucleo.combinatoria import (
    PRINCIPIO_FUNDAMENTAL_CONTAGEM_2, PERMUTACAO_SIMPLES, PERMUTACAO_REPETICAO_2,
    PERMUTACAO_CIRCULAR, ARRANJO_SIMPLES, ARRANJO_REPETICAO, COMBINACAO_SIMPLES, COMBINACAO_REPETICAO,
)
from nucleo.probabilidade import PROBABILIDADE, PROB_CONDICIONAL, EVENTOS_INDEPENDENTES, PROB_UNIAO, PROBABILIDADE_BINOMIAL
from nucleo.traducao import de_int, para_int, para_bool, para_rac, para_lista, para_int_assinado, para_bits
from nucleo.catalan_stirling import CATALAN, STIRLING2
from caixa import caixa, SemSolucaoExata, raiz_quadrada_aproximada
from estatistica import media, mediana, moda

_falhas = []
RODAR_LENTOS = "--lento" in sys.argv or os.environ.get("PSF_TESTES_LENTOS") == "1"


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"  [{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        _falhas.append(nome)


def main():
    print("=" * 70)
    print("PSF-IAMINY — CERTIFICAÇÃO DO NÚCLEO")
    print("Tudo derivado exclusivamente de: V, F, 0, S, PAR, ITER, Y")
    print("=" * 70)

    print("\n[1] LÓGICA")
    verificar("De Morgan 1", para_bool(DE_MORGAN_1(V)(F)), True)
    verificar("De Morgan 2", para_bool(DE_MORGAN_2(F)(F)), True)
    verificar("Implicação F->V", para_bool(IMPLICA(F)(V)), True)
    verificar("SSE V,V", para_bool(SSE(V)(V)), True)

    print("\n[2] ARITMÉTICA")
    verificar("3+4", para_int(SOMA(de_int(3))(de_int(4))), 7)
    verificar("7-2", para_int(SUB(de_int(7))(de_int(2))), 5)
    verificar("2-7 (truncada)", para_int(SUB(de_int(2))(de_int(7))), 0)
    verificar("4*5", para_int(MULT(de_int(4))(de_int(5))), 20)
    verificar("3^4", para_int(POT(de_int(3))(de_int(4))), 81)
    verificar("10÷3", para_int(DIV(de_int(10))(de_int(3))), 3)
    verificar("10 mod 3", para_int(MOD(de_int(10))(de_int(3))), 1)
    verificar("MDC(12,30)", para_int(MDC(de_int(12))(de_int(30))), 6)
    verificar("MMC(12,30)", para_int(MMC(de_int(12))(de_int(30))), 60)

    print("\n[3] NÚMEROS PRIMOS")
    casos_primos = [(2, True), (3, True), (4, False), (9, False)]
    casos_primos.append((97, True) if RODAR_LENTOS else (17, True))
    for n, esperado in casos_primos:
        verificar(f"{n} é primo?", para_bool(EH_PRIMO(de_int(n))), esperado)
    verificar(
        "10 primeiros primos",
        [para_int(PRIMO_N(de_int(i))) for i in range(1, 11)],
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    )
    verificar("Fatores de 60", para_lista(DECOMPOR(de_int(60))), [2, 2, 3, 5])
    verificar("φ(12)", para_int(TOTIENTE(de_int(12))), 4)
    verificar("φ(7)", para_int(TOTIENTE(de_int(7))), 6)
    verificar("coprimos(14,15)", para_bool(COPRIMOS(de_int(14))(de_int(15))), True)
    verificar("coprimos(14,21)", para_bool(COPRIMOS(de_int(14))(de_int(21))), False)

    print("\n[4] RACIONAIS")
    verificar("1/2 == 4/8", para_bool(EQ_RAC(RAC(de_int(1))(de_int(2)))(RAC(de_int(4))(de_int(8)))), True)
    r = SOMA_RAC(RAC(de_int(1))(de_int(3)))(RAC(de_int(1))(de_int(6)))
    verificar("1/3 + 1/6 (não simplificado)", para_rac(r), "9/18")

    print("\n[5] INTEIROS ASSINADOS (preenche lacuna da SUB truncada)")
    z = SUB_INT(DE_NATURAL(de_int(2)))(DE_NATURAL(de_int(7)))
    verificar("2 - 7 (assinada)", para_int_assinado(z), -5)

    print("\n[6] GEOMETRIA (corrigida para usar inteiros assinados)")
    A, B = PONTO(de_int(0))(de_int(0)), PONTO(de_int(1))(de_int(1))
    C, D = PONTO(de_int(2))(de_int(2)), PONTO(de_int(1))(de_int(0))
    verificar("Manhattan(A,B)", para_int(DIST_MANHATTAN(A)(B)), 2)
    verificar("A,B,C alinhados", para_bool(ALINHADOS(A)(B)(C)), True)
    verificar("A,B,D alinhados", para_bool(ALINHADOS(A)(B)(D)), False)
    verificar("AB perp CD (era bug, agora False)", para_bool(PERPENDICULARES(A)(B)(C)(D)), False)
    E, Fp = PONTO(de_int(3))(de_int(3)), PONTO(de_int(4))(de_int(2))
    verificar("AB perp EF (dot real = 0)", para_bool(PERPENDICULARES(A)(B)(E)(Fp)), True)

    print("\n[7] LÓGICA DE PREDICADOS — quantificadores limitados (∀, ∃)")
    verificar("∀k em [0,10], V", para_bool(PARA_TODO(de_int(10))(lambda k: V)), True)
    limite_existe = 28 if RODAR_LENTOS else 7
    verificar(f"∃ primo em [0,{limite_existe}]", para_bool(EXISTE(de_int(limite_existe))(lambda k: EH_PRIMO(k))), True)
    verificar("∃ primo em [0,1]", para_bool(EXISTE(de_int(1))(lambda k: EH_PRIMO(k))), False)

    print("\n[8] CÁLCULO DISCRETO — Σ, Π, indução, sequências")
    verificar("Σ i, 1..10", para_int(SOMATORIO(lambda i: i)(de_int(1))(de_int(10))), 55)
    verificar("Π i, 1..5", para_int(PRODUTORIO(lambda i: i)(de_int(1))(de_int(5))), 120)
    verificar("5!", para_int(FATORIAL(de_int(5))), 120)
    verificar("7!", para_int(FATORIAL(de_int(7))), 5040)
    verificar(
        "Fibonacci 0..10",
        [para_int(FIBONACCI(de_int(i))) for i in range(11)],
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
    )
    _P_gauss = lambda n: IGUAL(
        SOMATORIO(lambda i: i)(de_int(1))(n)
    )(
        DIV(MULT(n)(SOMA(n)(de_int(1))))(de_int(2))
    )
    limite_inducao = 20 if RODAR_LENTOS else 5
    verificar(f"Indução (soma de Gauss) em [0,{limite_inducao}]", para_bool(VERIFICAR_INDUCAO(_P_gauss)(de_int(limite_inducao))), True)

    print("\n[9] CAIXA UNIFICADA ⟦ ⟧ (Aula 18 — radiciação e log, um só símbolo)")
    verificar("⟦2,3⟧=?", caixa(2, 3, None), 8)
    verificar("⟦?,3⟧=8", caixa(None, 3, 8), 2)
    verificar("⟦2,?⟧=8", caixa(2, None, 8), 3)
    verificar("⟦?,2⟧=49", caixa(None, 2, 49), 7)
    verificar("⟦3,?⟧=81", caixa(3, None, 81), 4)
    try:
        caixa(None, 2, 10)
        verificar("⟦?,2⟧=10 deveria lançar exceção", False, True)
    except SemSolucaoExata:
        verificar("⟦?,2⟧=10 lança SemSolucaoExata", True, True)

    print("\n[10] REAIS APROXIMADOS — conjunto verificado expandido (chute inicial melhorado)")
    verificar("√9 ≈ 3 casas (rápido, <0.01s)", raiz_quadrada_aproximada(9), "3.000")
    verificar("√12 ≈ 3 casas (rápido, ~0.1s)", raiz_quadrada_aproximada(12), "3.464")
    verificar("√20 ≈ 3 casas (rápido, ~0.3s)", raiz_quadrada_aproximada(20), "4.472")
    if RODAR_LENTOS:
        print("      (alvo=2,8,10 demoram vários segundos — ver nucleo/reais.py para o motivo)")
        r2 = RAIZ_QUADRADA_RAC(de_int(2))
        verificar("√2 racional exato do núcleo", (para_int(r2(V)), para_int(r2(F))), (577, 408))
        verificar("√2 ≈ 3 casas (via caixa.py)", raiz_quadrada_aproximada(2), "1.414")
        verificar("√3 ≈ 3 casas (via caixa.py)", raiz_quadrada_aproximada(3), "1.732")
        verificar("√5 ≈ 3 casas (via caixa.py)", raiz_quadrada_aproximada(5), "2.236")
        verificar("√8 ≈ 3 casas (via caixa.py)", raiz_quadrada_aproximada(8), "2.828")
        verificar("√10 ≈ 3 casas (via caixa.py)", raiz_quadrada_aproximada(10), "3.162")
        verificar("√11 ≈ 3 casas (via caixa.py)", raiz_quadrada_aproximada(11), "3.317")
    else:
        print("      Testes lentos omitidos por padrão. Use: python3 testes/test_nucleo.py --lento")
        verificar("modo rápido ativo", True, True)

    print("\n[11] ÁREA 1 — divisores, figurados, harmônicos (ROADMAP.md)")
    verificar("12 múltiplo de 3", para_bool(MULTIPLO(de_int(3))(de_int(12))), True)
    verificar("8 composto", para_bool(EH_COMPOSTO(de_int(8))), True)
    verificar("7 composto", para_bool(EH_COMPOSTO(de_int(7))), False)
    verificar("divisores de 12", sorted(para_lista(LISTA_DIVISORES(de_int(12)))), [1, 2, 3, 4, 6, 12])
    verificar("τ(12)", para_int(QTD_DIVISORES(de_int(12))), 6)
    verificar("σ(12)", para_int(SOMA_DIVISORES(de_int(12))), 28)
    verificar("produto divisores de 6", para_int(PRODUTO_DIVISORES(de_int(6))), 36)
    verificar("6 é perfeito", para_bool(PERFEITO(de_int(6))), True)
    verificar("28 é perfeito", para_bool(PERFEITO(de_int(28))), True)
    verificar("12 é perfeito", para_bool(PERFEITO(de_int(12))), False)
    verificar("17 ≡ 5 (mod 6)", para_bool(CONGRUENTE(de_int(17))(de_int(5))(de_int(6))), True)
    verificar("Mersenne(5) = 2^5-1", para_int(MERSENNE(de_int(5))), 31)
    verificar("Mersenne(5) é primo", para_bool(EH_MERSENNE_PRIMO(de_int(5))), True)
    verificar("Fermat(2) = 2^4+1", para_int(FERMAT(de_int(2))), 17)
    verificar("(3,4,5) é terna pitagórica", para_bool(EH_TERNA_PITAGORICA(de_int(3))(de_int(4))(de_int(5))), True)
    verificar("(3,4,6) não é terna pitagórica", para_bool(EH_TERNA_PITAGORICA(de_int(3))(de_int(4))(de_int(6))), False)
    verificar("Triangulares 1..6", [para_int(TRIANGULAR(de_int(i))) for i in range(1, 7)], [1, 3, 6, 10, 15, 21])
    verificar("Quadrados 1..6", [para_int(QUADRADO_FIGURADO(de_int(i))) for i in range(1, 7)], [1, 4, 9, 16, 25, 36])
    verificar("Pentagonais 1..6", [para_int(PENTAGONAL(de_int(i))) for i in range(1, 7)], [1, 5, 12, 22, 35, 51])
    verificar("Hexagonais 1..6", [para_int(HEXAGONAL(de_int(i))) for i in range(1, 7)], [1, 6, 15, 28, 45, 66])
    verificar("3/4 − 1/4 (não simplificado)", para_rac(SUB_RAC(RAC(de_int(3))(de_int(4)))(RAC(de_int(1))(de_int(4)))), "8/16")
    verificar("1/2 ÷ 1/4 (não simplificado)", para_rac(DIV_RAC(RAC(de_int(1))(de_int(2)))(RAC(de_int(1))(de_int(4)))), "4/2")
    h5 = HARMONICO(de_int(5))
    verificar("H(5) = 137/60", (para_int(h5(V)), para_int(h5(F))), (137, 60))

    if not RODAR_LENTOS:
        print("\n[12-14] SEÇÕES MAIS LENTAS OMITIDAS NO MODO RÁPIDO")
        print("      Use: python3 testes/test_nucleo.py --lento")
        print("      Para domínio grande validado rapidamente, use: python3 testes/test_modelo_eficiente.py")
        print("\n" + "=" * 70)
        if _falhas:
            print(f"  {len(_falhas)} TESTE(S) FALHARAM: {_falhas}")
            print("=" * 70)
            sys.exit(1)
        else:
            print("  TODOS OS TESTES RÁPIDOS PASSARAM")
            print("=" * 70)
            return

    print("\n[12] ÁREA 1 — porcentagem, razão, proporção, regra de três (ROADMAP.md)")
    verificar("25% de 80", para_rac(PORCENTAGEM_DE(de_int(25))(de_int(80))), "2000/100")
    verificar("80 + 25%", para_rac(AUMENTAR_PERCENTUAL(de_int(80))(de_int(25))), "10000/100")
    verificar("80 - 25%", para_rac(DIMINUIR_PERCENTUAL(de_int(80))(de_int(25))), "6000/100")
    verificar("razão 3:4", para_rac(RAZAO(de_int(3))(de_int(4))), "3/4")
    verificar("2,3,4,6 é proporção", para_bool(EH_PROPORCAO(de_int(2))(de_int(3))(de_int(4))(de_int(6))), True)
    verificar("2,3,4,7 não é proporção", para_bool(EH_PROPORCAO(de_int(2))(de_int(3))(de_int(4))(de_int(7))), False)
    verificar("regra de 3 direta (3:12=5:x)", para_rac(REGRA_DE_TRES_DIRETA(de_int(3))(de_int(12))(de_int(5))), "60/3")
    verificar("regra de 3 inversa (4·15=6·x)", para_rac(REGRA_DE_TRES_INVERSA(de_int(4))(de_int(15))(de_int(6))), "60/6")
    r_composta = REGRA_DE_TRES_COMPOSTA_2(de_int(6))(de_int(3))(de_int(6))(F)(de_int(10))(de_int(20))(V)
    verificar("regra de 3 composta", para_rac(r_composta), "360/60")
    partes = DIVISAO_PROPORCIONAL_3(de_int(60))(de_int(2))(de_int(3))(de_int(5))
    verificar(
        "60 dividido em 2:3:5",
        (para_rac(partes(V)), para_rac(partes(F)(V)), para_rac(partes(F)(F))),
        ("120/10", "180/10", "300/10"),
    )
    _escala = ESCALA(de_int(1))(de_int(100))
    verificar("escala 1:100, 5cm mapa -> real", para_rac(DISTANCIA_REAL(_escala)(de_int(5))), "500/1")
    verificar("escala 1:100, 500cm real -> mapa", para_rac(DISTANCIA_MAPA(_escala)(de_int(500))), "500/100")
    verificar("oposto de 7", para_int_assinado(OPOSTO_INT(DE_NATURAL(de_int(7)))), -7)
    verificar("recíproco de 2/5", para_rac(RECIPROCO_RAC(RAC(de_int(2))(de_int(5)))), "5/2")

    print("\n[13] SISTEMA BINÁRIO — vetor de largura fixa, O(n) não O(n²) (Tópico 45)")
    verificar("0 em binário", para_bits(PARA_BINARIO(de_int(0))), "0b0000000000")
    verificar("42 em binário", para_bits(PARA_BINARIO(de_int(42))), "0b0000101010")
    verificar("255 em binário", para_bits(PARA_BINARIO(de_int(255))), "0b0011111111")
    verificar("1023 em binário", para_bits(PARA_BINARIO(de_int(1023))), "0b1111111111")
    verificar("ida-volta 1023", para_int(DE_BINARIO(PARA_BINARIO(de_int(1023)))), 1023)
    verificar("overflow 1024 -> 0", para_int(DE_BINARIO(PARA_BINARIO(de_int(1024)))), 0)
    verificar("overflow 2000 -> 976 (2000 mod 1024)", para_int(DE_BINARIO(PARA_BINARIO(de_int(2000)))), 976)

    print("\n[14] ÁREA 8 — combinatória, probabilidade, estatística (ROADMAP.md)")
    verificar("princípio fundamental 3×4", para_int(PRINCIPIO_FUNDAMENTAL_CONTAGEM_2(de_int(3))(de_int(4))), 12)
    verificar("P(5) = 5!", para_int(PERMUTACAO_SIMPLES(de_int(5))), 120)
    verificar("anagramas ARARA (5;3,2)", para_int(PERMUTACAO_REPETICAO_2(de_int(5))(de_int(3))(de_int(2))), 10)
    verificar("permutação circular de 5", para_int(PERMUTACAO_CIRCULAR(de_int(5))), 24)
    verificar("A(5,2)", para_int(ARRANJO_SIMPLES(de_int(5))(de_int(2))), 20)
    verificar("AR(5,2) = 5²", para_int(ARRANJO_REPETICAO(de_int(5))(de_int(2))), 25)
    verificar("C(5,2)", para_int(COMBINACAO_SIMPLES(de_int(5))(de_int(2))), 10)
    verificar("CR(5,2) = C(6,2)", para_int(COMBINACAO_REPETICAO(de_int(5))(de_int(2))), 15)

    print("\n[14b] CATALAN E STIRLING — tópicos 88 e 90, domínio pequeno do núcleo puro")
    verificar("Catalan C0..C3", [para_int(CATALAN(de_int(i))) for i in range(4)], [1, 1, 2, 5])
    verificar("Stirling S(3,2)", para_int(STIRLING2(de_int(3))(de_int(2))), 3)

    _p_a = RAC(de_int(1))(de_int(2))
    _p_b = RAC(de_int(1))(de_int(3))
    _p_a_e_b = RAC(de_int(1))(de_int(6))
    verificar("P(dado par) = 3/6", para_rac(PROBABILIDADE(de_int(3))(de_int(6))), "3/6")
    verificar("P(A|B)", para_rac(PROB_CONDICIONAL(_p_a_e_b)(_p_b)), "3/6")
    verificar("A,B independentes", para_bool(EVENTOS_INDEPENDENTES(_p_a)(_p_b)(_p_a_e_b)), True)
    verificar("P(A∪B) = 24/36 (=2/3)", para_rac(PROB_UNIAO(_p_a)(_p_b)(_p_a_e_b)), "24/36")
    _moeda = RAC(de_int(1))(de_int(2))
    verificar(
        "P(2 caras em 3 lançamentos) = 3/8",
        para_rac(PROBABILIDADE_BINOMIAL(de_int(3))(de_int(2))(_moeda)),
        "3/8",
    )

    _dados = [4, 8, 6, 5, 3, 8, 9, 8]
    verificar("média de [4,8,6,5,3,8,9,8]", media(_dados), "51/8")
    verificar("mediana de [4,8,6,5,3,8,9,8]", mediana(_dados), 7.0)
    verificar("moda de [4,8,6,5,3,8,9,8]", moda(_dados), [8])

    print("\n" + "=" * 70)
    if _falhas:
        print(f"  {len(_falhas)} TESTE(S) FALHARAM: {_falhas}")
        print("=" * 70)
        sys.exit(1)
    else:
        print("  TODOS OS TESTES PASSARAM")
        print("=" * 70)


if __name__ == "__main__":
    main()
