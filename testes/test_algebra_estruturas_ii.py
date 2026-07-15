"""PSF-IAminy — Estruturas Algébricas II, Etapas 91 a 100.
Roda com: python3 testes/test_algebra_estruturas_ii.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.primitivas import V, F, PAR
from nucleo.aritmetica import SOMA, MULT, MOD
from nucleo.traducao import de_int, para_bool, para_int
from nucleo.algebra_estruturas_ii import (
    ANEL_COMUTATIVO_PURO, ANEL_COM_UNIDADE_PURO, DOMINIO_INTEGRIDADE_PURO,
    CORPO_FINITO_PURO, HOMOMORFISMO_GRUPOS_PURO, ISOMORFISMO_PURO,
    NUCLEO_HOMOMORFISMO_PURO, IMAGEM_HOMOMORFISMO_PURO, SUBGRUPO_PURO,
    PARTICAO_EM_CLASSES_LATERAIS_PURA, FECHAMENTO_ALGEBRICO_INICIAL_PURO,
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
    print("PSF-IAminy — Estruturas Algébricas II, Etapas 91 a 100")

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 100 (álgebra II completa)", r["maior_etapa"] >= 100, True)
    verificar("motor sem lacunas até 100", r["faltando_ate_maior"], [])

    TRES, QUATRO, CINCO, SEIS = de_int(3), de_int(4), de_int(5), de_int(6)
    dominio3 = [de_int(i) for i in range(3)]
    dominio4 = [de_int(i) for i in range(4)]
    dominio5 = [de_int(i) for i in range(5)]
    dominio6 = [de_int(i) for i in range(6)]

    SOMA_MOD3 = lambda a: lambda b: MOD(SOMA(a)(b))(TRES)
    SOMA_MOD4 = lambda a: lambda b: MOD(SOMA(a)(b))(QUATRO)
    MULT_MOD4 = lambda a: lambda b: MOD(MULT(a)(b))(QUATRO)
    SOMA_MOD5 = lambda a: lambda b: MOD(SOMA(a)(b))(CINCO)
    MULT_MOD5 = lambda a: lambda b: MOD(MULT(a)(b))(CINCO)
    SOMA_MOD6 = lambda a: lambda b: MOD(SOMA(a)(b))(SEIS)

    print("\n[Etapa 91-92] Anel comutativo, anel com unidade — (Z/5Z,+,×)")
    verificar("(Z/5Z) anel comutativo", para_bool(ANEL_COMUTATIVO_PURO(dominio5, SOMA_MOD5, MULT_MOD5)), True)
    verificar("(Z/5Z) anel com unidade", para_bool(ANEL_COM_UNIDADE_PURO(dominio5, SOMA_MOD5, MULT_MOD5)), True)

    print("\n[Etapa 93] Domínio de integridade")
    verificar("(Z/5Z) é domínio de integridade (5 primo)", para_bool(DOMINIO_INTEGRIDADE_PURO(dominio5, SOMA_MOD5, MULT_MOD5)), True)
    verificar("(Z/4Z) NÃO é domínio de integridade (2×2=0 mod 4)", para_bool(DOMINIO_INTEGRIDADE_PURO(dominio4, SOMA_MOD4, MULT_MOD4)), False)

    print("\n[Etapa 94] Corpo finito")
    verificar("(Z/5Z) É corpo (5 é primo)", para_bool(CORPO_FINITO_PURO(dominio5, SOMA_MOD5, MULT_MOD5)), True)
    verificar("(Z/4Z) NÃO é corpo (4 não é primo)", para_bool(CORPO_FINITO_PURO(dominio4, SOMA_MOD4, MULT_MOD4)), False)

    print("\n[Etapa 95-97] Homomorfismo, núcleo e imagem — f:(Z/6Z,+)→(Z/3Z,+), f(x)=x mod 3")
    f = tuple(PAR(x)(MOD(x)(TRES)) for x in dominio6)
    verificar("f é homomorfismo de grupos", para_bool(HOMOMORFISMO_GRUPOS_PURO(dominio6, SOMA_MOD6, SOMA_MOD3, f)), True)
    nucleo_f = sorted(para_int(x) for x in NUCLEO_HOMOMORFISMO_PURO(dominio6, de_int(0), f))
    verificar("núcleo de f = {0,3}", nucleo_f, [0, 3])
    imagem_f = sorted(para_int(x) for x in IMAGEM_HOMOMORFISMO_PURO(dominio6, f))
    verificar("imagem de f = {0,1,2} (sobrejetora)", imagem_f, [0, 1, 2])

    print("\n[Etapa 96] Isomorfismo — identidade em (Z/5Z,+) é isomorfismo trivial")
    identidade5 = tuple(PAR(x)(x) for x in dominio5)
    verificar("identidade é isomorfismo (Z/5Z,+)→(Z/5Z,+)", para_bool(ISOMORFISMO_PURO(dominio5, dominio5, SOMA_MOD5, SOMA_MOD5, identidade5)), True)

    print("\n[Etapa 98] Subgrupo — H={0,2,4} de (Z/6Z,+mod6)")
    H = (de_int(0), de_int(2), de_int(4))
    verificar("{0,2,4} é subgrupo de (Z/6Z,+)", para_bool(SUBGRUPO_PURO(dominio6, SOMA_MOD6, H)), True)
    verificar("{0,1} NÃO é subgrupo (não fechado: 1+1=2∉{0,1})", para_bool(SUBGRUPO_PURO(dominio6, SOMA_MOD6, (de_int(0), de_int(1)))), False)

    print("\n[Etapa 99] Classes laterais — Teorema de Lagrange: |G|/|H| = nº de classes")
    classes = PARTICAO_EM_CLASSES_LATERAIS_PURA(dominio6, H, SOMA_MOD6)
    verificar("|G|=6,|H|=3 → 2 classes laterais (Lagrange)", len(classes), 2)
    classes_valores = sorted(tuple(sorted(para_int(x) for x in c)) for c in classes)
    verificar("classes laterais são {0,2,4} e {1,3,5}", classes_valores, [(0, 2, 4), (1, 3, 5)])

    print("\n[Etapa 100] Fechamento algébrico inicial")
    verificar("fechamento (Z/5Z,+,×)", para_bool(FECHAMENTO_ALGEBRICO_INICIAL_PURO(dominio5, SOMA_MOD5, MULT_MOD5)), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
