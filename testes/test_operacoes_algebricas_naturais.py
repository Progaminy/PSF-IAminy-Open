"""PSF-IAminy — Operações Algébricas Naturais, Etapas 81 a 90.
Roda com: python3 testes/test_operacoes_algebricas_naturais.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.primitivas import V, F
from nucleo.aritmetica import SOMA, MULT, MOD, SUB
from nucleo.traducao import de_int, para_bool
from nucleo.operacoes_algebricas_naturais import (
    FECHADA_PURA, ASSOCIATIVA_PURA, EH_NEUTRO_PURA, EXISTE_NEUTRO_PURA,
    NEUTRO_CONCRETO_PURA, COMUTATIVA_PURA, SEMIGRUPO_PURO, MONOIDE_PURO,
    EH_INVERSO_PURA, TEM_INVERSO_PURA, TODOS_TEM_INVERSO_PURA,
    GRUPO_PURO, GRUPO_ABELIANO_PURO, DISTRIBUTIVA_PURA, ANEL_INICIAL_PURO,
)
from motor.fluxo import relatorio_fluxo

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def main():
    print("PSF-IAminy — Operações Algébricas Naturais, Etapas 81 a 90")

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 90 (álgebra I completa)", r["maior_etapa"] >= 90, True)
    verificar("motor sem lacunas até 90", r["faltando_ate_maior"], [])

    QUATRO = de_int(4)
    CINCO = de_int(5)
    dominio4 = [de_int(i) for i in range(4)]
    dominio5_sem_zero = [de_int(i) for i in range(1, 5)]

    SOMA_MOD4 = lambda a: lambda b: MOD(SOMA(a)(b))(QUATRO)
    MULT_MOD4 = lambda a: lambda b: MOD(MULT(a)(b))(QUATRO)
    MULT_MOD5 = lambda a: lambda b: MOD(MULT(a)(b))(CINCO)

    print("\n[Etapa 82] Fechamento")
    verificar("(Z/4Z,+mod4) fechada", para_bool(FECHADA_PURA(dominio4)(SOMA_MOD4)), True)

    print("\n[Etapa 83] Associatividade")
    verificar("(Z/4Z,+mod4) associativa", para_bool(ASSOCIATIVA_PURA(dominio4)(SOMA_MOD4)), True)

    print("\n[Etapa 84] Elemento neutro")
    verificar("0 é neutro de +mod4", para_bool(EH_NEUTRO_PURA(dominio4)(SOMA_MOD4)(de_int(0))), True)
    verificar("1 não é neutro de +mod4", para_bool(EH_NEUTRO_PURA(dominio4)(SOMA_MOD4)(de_int(1))), False)
    verificar("existe neutro em +mod4", para_bool(EXISTE_NEUTRO_PURA(dominio4)(SOMA_MOD4)), True)
    e4 = NEUTRO_CONCRETO_PURA(dominio4, SOMA_MOD4)
    verificar("neutro concreto de +mod4 é 0", para_bool(EH_NEUTRO_PURA(dominio4)(SOMA_MOD4)(e4)), True)

    print("\n[Etapa 85] Comutatividade")
    verificar("+mod4 comutativa", para_bool(COMUTATIVA_PURA(dominio4)(SOMA_MOD4)), True)
    SUB_TRUNCADA = lambda a: lambda b: SUB(a)(b)
    verificar("subtração truncada NÃO comutativa", para_bool(COMUTATIVA_PURA(dominio4)(SUB_TRUNCADA)), False)

    print("\n[Etapa 86] Semigrupo")
    verificar("(Z/4Z,+mod4) é semigrupo", para_bool(SEMIGRUPO_PURO(dominio4)(SOMA_MOD4)), True)

    print("\n[Etapa 87] Monoide")
    verificar("(Z/4Z,+mod4) é monoide", para_bool(MONOIDE_PURO(dominio4)(SOMA_MOD4)), True)

    print("\n[Etapa 88] Inverso algébrico")
    verificar("2 é o próprio inverso em +mod4", para_bool(EH_INVERSO_PURA(dominio4)(SOMA_MOD4)(de_int(0))(de_int(2))(de_int(2))), True)
    verificar("todo elemento tem inverso em +mod4", para_bool(TODOS_TEM_INVERSO_PURA(dominio4)(SOMA_MOD4)(de_int(0))), True)

    print("\n[Etapa 89] Grupo")
    verificar("(Z/4Z,+mod4) é grupo", para_bool(GRUPO_PURO(dominio4, SOMA_MOD4)), True)
    verificar("(Z/4Z,+mod4) é grupo abeliano", para_bool(GRUPO_ABELIANO_PURO(dominio4, SOMA_MOD4)), True)
    verificar("((Z/5Z)*,×mod5) é grupo abeliano (5 é primo)", para_bool(GRUPO_ABELIANO_PURO(dominio5_sem_zero, MULT_MOD5)), True)
    verificar("(naturais 0..3, subtração truncada) NÃO é grupo", para_bool(GRUPO_PURO(dominio4, SUB_TRUNCADA)), False)

    print("\n[Etapa 90] Anel inicial")
    verificar("distributiva: ×mod4 sobre +mod4", para_bool(DISTRIBUTIVA_PURA(dominio4)(SOMA_MOD4)(MULT_MOD4)), True)
    verificar("(Z/4Z, +mod4, ×mod4) é anel", para_bool(ANEL_INICIAL_PURO(dominio4, SOMA_MOD4, MULT_MOD4)), True)
    verificar("(Z/4Z, +mod4, ×mod5 mal-formado) NÃO é anel", para_bool(ANEL_INICIAL_PURO(dominio4, SOMA_MOD4, MULT_MOD5)), False)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
