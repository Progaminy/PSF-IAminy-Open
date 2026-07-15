"""Testes de Relações e Funções Naturais PSF-IAminy.
Roda com: python3 testes/test_relacoes_funcoes_naturais.py

Etapas validadas: 61 a 80.
"""
import ast
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.primitivas import PAR
from nucleo.traducao import de_int, para_bool, para_int
from nucleo.relacoes_funcoes_naturais import (
    PRIMEIRO,
    SEGUNDO,
    DOMINIO_FINITO_PURO,
    RELACAO_BINARIA_FINITA_PURA,
    PAR_ORDENADO_PURO,
    PAR_IGUAL_PURO,
    PERTENCE_RELACAO_PURA,
    REFLEXIVA_PURA,
    SIMETRICA_PURA,
    TRANSITIVA_PURA,
    EQUIVALENCIA_PURA,
    CLASSE_EQUIVALENCIA_PURA,
    ANTISSIMETRICA_PURA,
    ORDEM_PARCIAL_PURA,
    ORDEM_TOTAL_PURA,
    FUNCIONAL_PURA,
    TOTAL_SOBRE_DOMINIO_PURA,
    FUNCAO_RELACAO_PURA,
    APLICAR_FUNCAO_FINITA_PURA,
    FUNCAO_IDENTIDADE_PURA,
    FUNCAO_CONSTANTE_PURA,
    COMPOSICAO_FUNCOES_FINITA_PURA,
    INJETORA_PURA,
    SOBREJETORA_PURA,
    BIJETORA_PURA,
    INVERSA_RELACAO_PURA,
    IMAGEM_FUNCAO_PURA,
    PREIMAGEM_FUNCAO_PURA,
    FECHAMENTO_RELACOES_FUNCOES_PURO,
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


def lista_int(seq):
    return [i(x) for x in seq]


def verificar_motor_e_pureza():
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "relacoes_funcoes_naturais.py")
    with open(caminho, "r", encoding="utf-8") as f:
        arvore = ast.parse(f.read(), filename=caminho)
    nomes_proibidos = {
        "DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "FATORACAO", "CARDINALIDADE",
        "DERIVADA", "INTEGRAL", "PROBABILIDADE",
    }
    chamadas_proibidas = {"set"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em relacoes_funcoes_naturais.py")
        if isinstance(no, ast.Name) and no.id in nomes_proibidos:
            falhas.append(f"nome proibido {no.id} em relacoes_funcoes_naturais.py")
        if isinstance(no, ast.Call) and isinstance(no.func, ast.Name) and no.func.id in chamadas_proibidas:
            falhas.append(f"chamada proibida {no.func.id} em relacoes_funcoes_naturais.py")

    r = relatorio_fluxo()
    numeros_encontrados = {n for n in range(61, 81) if any(f"ETAPA_{n}_" in a or f"ETAPA_0{n}_" in a for a in r["arquivos_documentados"])}
    verificar("motor contabiliza etapa máxima >= 80 (relações/funções completas)", r["maior_etapa"] >= 80, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])
    verificar("etapas 61-80 (relações/funções) todas documentadas", sorted(numeros_encontrados), list(range(61, 81)))


def main():
    print("PSF-IAminy — Relações e Funções Naturais, Etapas 61 a 80")
    verificar_motor_e_pureza()

    zero, um, dois, tres = n(0), n(1), n(2), n(3)
    dominio = DOMINIO_FINITO_PURO(zero, um, dois)

    par_01 = PAR_ORDENADO_PURO(zero)(um)
    verificar("par primeiro", i(PRIMEIRO(par_01)), 0)
    verificar("par segundo", i(SEGUNDO(par_01)), 1)
    verificar("par igual", b(PAR_IGUAL_PURO(par_01)(PAR(zero)(um))), True)

    equivalencia_mod2_pequena = RELACAO_BINARIA_FINITA_PURA(
        PAR(zero)(zero), PAR(um)(um), PAR(dois)(dois),
        PAR(zero)(dois), PAR(dois)(zero),
    )
    verificar("pertence relação 0R2", b(PERTENCE_RELACAO_PURA(zero)(dois)(equivalencia_mod2_pequena)), True)
    verificar("não pertence relação 1R2", b(PERTENCE_RELACAO_PURA(um)(dois)(equivalencia_mod2_pequena)), False)
    verificar("reflexiva", b(REFLEXIVA_PURA(dominio)(equivalencia_mod2_pequena)), True)
    verificar("simétrica", b(SIMETRICA_PURA(equivalencia_mod2_pequena)), True)
    verificar("transitiva", b(TRANSITIVA_PURA(equivalencia_mod2_pequena)), True)
    verificar("equivalência", b(EQUIVALENCIA_PURA(dominio)(equivalencia_mod2_pequena)), True)
    verificar("classe de equivalência de 0", lista_int(CLASSE_EQUIVALENCIA_PURA(zero, dominio, equivalencia_mod2_pequena)), [0, 2])

    ordem_leq_012 = RELACAO_BINARIA_FINITA_PURA(
        PAR(zero)(zero), PAR(zero)(um), PAR(zero)(dois),
        PAR(um)(um), PAR(um)(dois),
        PAR(dois)(dois),
    )
    verificar("antissimétrica", b(ANTISSIMETRICA_PURA(ordem_leq_012)), True)
    verificar("ordem parcial", b(ORDEM_PARCIAL_PURA(dominio)(ordem_leq_012)), True)
    verificar("ordem total", b(ORDEM_TOTAL_PURA(dominio, ordem_leq_012)), True)

    f = RELACAO_BINARIA_FINITA_PURA(
        PAR(zero)(um),
        PAR(um)(dois),
        PAR(dois)(tres),
    )
    g = RELACAO_BINARIA_FINITA_PURA(
        PAR(um)(dois),
        PAR(dois)(tres),
        PAR(tres)(n(4)),
    )
    codominio_f = DOMINIO_FINITO_PURO(um, dois, tres)
    verificar("funcional", b(FUNCIONAL_PURA(f)), True)
    verificar("total no domínio", b(TOTAL_SOBRE_DOMINIO_PURA(dominio, f)), True)
    verificar("função como relação especial", b(FUNCAO_RELACAO_PURA(dominio)(f)), True)
    verificar("aplicar f(2)", i(APLICAR_FUNCAO_FINITA_PURA(f, dois)), 3)
    verificar("injetora", b(INJETORA_PURA(dominio, f)), True)
    verificar("sobrejetora no codomínio {1,2,3}", b(SOBREJETORA_PURA(codominio_f, f)), True)
    verificar("bijetora", b(BIJETORA_PURA(dominio)(codominio_f)(f)), True)

    identidade = FUNCAO_IDENTIDADE_PURA(dominio)
    constante = FUNCAO_CONSTANTE_PURA(dominio, tres)
    composta = COMPOSICAO_FUNCOES_FINITA_PURA(g, f, dominio)
    verificar("identidade é função", b(FUNCAO_RELACAO_PURA(dominio)(identidade)), True)
    verificar("identidade aplica 2", i(APLICAR_FUNCAO_FINITA_PURA(identidade, dois)), 2)
    verificar("constante aplica 1", i(APLICAR_FUNCAO_FINITA_PURA(constante, um)), 3)
    verificar("composição g(f(1))", i(APLICAR_FUNCAO_FINITA_PURA(composta, um)), 3)

    inversa = INVERSA_RELACAO_PURA(f)
    verificar("inversa contém 3R2", b(PERTENCE_RELACAO_PURA(tres)(dois)(inversa)), True)
    verificar("imagem de f", lista_int(IMAGEM_FUNCAO_PURA(f)), [1, 2, 3])
    verificar("pré-imagem de 2", lista_int(PREIMAGEM_FUNCAO_PURA(dois, dominio, f)), [1])
    verificar("fechamento relacional-funcional", b(FECHAMENTO_RELACOES_FUNCOES_PURO(dominio)), True)

    relacao_nao_funcao = RELACAO_BINARIA_FINITA_PURA(PAR(zero)(um), PAR(zero)(dois))
    verificar("não funcional quando uma entrada tem duas saídas", b(FUNCIONAL_PURA(relacao_nao_funcao)), False)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
