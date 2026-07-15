"""Testes da Etapa 7 do fluxo natural PSF-IAminy.
Roda com: python3 testes/test_teorema_fundamental_aritmetica.py

Etapas validadas:
- existência operacional da decomposição prima;
- fatores reconstruindo o número;
- todos os fatores sendo primos;
- unicidade operacional por multiconjunto;
- MDC por fatores;
- MMC por fatores;
- relação mdc*mmc = a*b.
"""
import ast
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.primitivas import F, PAR
from nucleo.traducao import de_int, para_bool, para_int, para_lista
from nucleo.teorema_fundamental_aritmetica import (
    LISTA_VAZIA_PURA,
    PRODUTO_LISTA_PURO,
    TODOS_PRIMOS_LISTA_PURO,
    FATORACAO_RECONSTROI_NUMERO,
    FATORACAO_CONTEM_APENAS_PRIMOS,
    TFA_EXISTENCIA_OPERACIONAL,
    CONTA_VALOR_LISTA_PURO,
    REMOVER_UMA_OCORRENCIA_PURO,
    MESMO_MULTICONJUNTO_PURO,
    FATORACAO_EQUIVALE_A_CANONICA,
    MDC_POR_FATORES_PURO,
    MDC_POR_FATORES_CONFERE,
    MMC_POR_FATORES_PURO,
    MDC_MMC_PRODUTO_CONFERE,
)

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


def lista_py(xs):
    return para_lista(xs)


def lista_church(*valores):
    atual = F
    for valor in reversed(valores):
        atual = PAR(n(valor))(atual)
    return atual


def verificar_sem_dependencias_indevidas():
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "teorema_fundamental_aritmetica.py")
    with open(caminho, "r", encoding="utf-8") as f:
        fonte = f.read()
    arvore = ast.parse(fonte, filename=caminho)
    nomes_importados_proibidos = {"DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "FATORES", "DECOMPOR"}
    modulos_proibidos = {"primos"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em teorema_fundamental_aritmetica.py")
        if isinstance(no, ast.ImportFrom):
            modulo = (no.module or "").split(".")[-1]
            if modulo in modulos_proibidos:
                falhas.append(f"módulo proibido {no.module}")
            for alias in no.names:
                if alias.name in nomes_importados_proibidos:
                    falhas.append(f"import proibido {alias.name}")


def main():
    print("PSF-IAminy — Teorema Fundamental da Aritmética, MDC e MMC por fatores")
    verificar_sem_dependencias_indevidas()

    vazia = F
    l_223 = lista_church(2, 2, 3)
    l_322 = lista_church(3, 2, 2)
    l_233 = lista_church(2, 3, 3)

    verificar("LISTA_VAZIA_PURA([])", b(LISTA_VAZIA_PURA(vazia)), True)
    verificar("LISTA_VAZIA_PURA([2,2,3])", b(LISTA_VAZIA_PURA(l_223)), False)
    verificar("PRODUTO_LISTA_PURO([2,2,3])", i(PRODUTO_LISTA_PURO(l_223)), 12)
    verificar("TODOS_PRIMOS_LISTA_PURO([2,2,3])", b(TODOS_PRIMOS_LISTA_PURO(l_223)), True)
    verificar("TODOS_PRIMOS_LISTA_PURO([2,4])", b(TODOS_PRIMOS_LISTA_PURO(lista_church(2, 4))), False)

    for x in [2, 3, 4, 6, 12, 18, 28, 30]:
        verificar(f"FATORACAO_RECONSTROI_NUMERO({x})", b(FATORACAO_RECONSTROI_NUMERO(n(x))), True)
        verificar(f"FATORACAO_CONTEM_APENAS_PRIMOS({x})", b(FATORACAO_CONTEM_APENAS_PRIMOS(n(x))), True)
        verificar(f"TFA_EXISTENCIA_OPERACIONAL({x})", b(TFA_EXISTENCIA_OPERACIONAL(n(x))), True)

    verificar("CONTA_VALOR_LISTA_PURO(2,[2,2,3])", i(CONTA_VALOR_LISTA_PURO(n(2))(l_223)), 2)
    verificar("CONTA_VALOR_LISTA_PURO(3,[2,2,3])", i(CONTA_VALOR_LISTA_PURO(n(3))(l_223)), 1)
    verificar("CONTA_VALOR_LISTA_PURO(5,[2,2,3])", i(CONTA_VALOR_LISTA_PURO(n(5))(l_223)), 0)

    removida = REMOVER_UMA_OCORRENCIA_PURO(n(2))(l_223)
    verificar("REMOVER_UMA_OCORRENCIA_PURO(2,[2,2,3])", lista_py(removida), [2, 3])
    verificar("MESMO_MULTICONJUNTO_PURO([2,2,3],[3,2,2])", b(MESMO_MULTICONJUNTO_PURO(l_223)(l_322)), True)
    verificar("MESMO_MULTICONJUNTO_PURO([2,2,3],[2,3,3])", b(MESMO_MULTICONJUNTO_PURO(l_223)(l_233)), False)
    verificar("FATORACAO_EQUIVALE_A_CANONICA(12,[3,2,2])", b(FATORACAO_EQUIVALE_A_CANONICA(n(12))(l_322)), True)
    verificar("FATORACAO_EQUIVALE_A_CANONICA(12,[2,3,3])", b(FATORACAO_EQUIVALE_A_CANONICA(n(12))(l_233)), False)

    casos_mdc_mmc = {
        (12, 18): (6, 36),
        (8, 12): (4, 24),
        (7, 13): (1, 91),
        (4, 8): (4, 8),
        (10, 15): (5, 30),
    }
    for (a, c), (mdc_esperado, mmc_esperado) in casos_mdc_mmc.items():
        verificar(f"MDC_POR_FATORES_PURO({a},{c})", i(MDC_POR_FATORES_PURO(n(a))(n(c))), mdc_esperado)
        verificar(f"MMC_POR_FATORES_PURO({a},{c})", i(MMC_POR_FATORES_PURO(n(a))(n(c))), mmc_esperado)
        verificar(f"MDC_POR_FATORES_CONFERE({a},{c})", b(MDC_POR_FATORES_CONFERE(n(a))(n(c))), True)
        verificar(f"MDC_MMC_PRODUTO_CONFERE({a},{c})", b(MDC_MMC_PRODUTO_CONFERE(n(a))(n(c))), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
