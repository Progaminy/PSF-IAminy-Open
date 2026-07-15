"""Testes da continuação natural PSF-IAminy.
Roda com: python3 testes/test_divisao_euclidiana_pura.py

Etapas validadas:
- quociente puro por subtrações repetidas;
- resto puro como sobra final menor que o divisor;
- divisão euclidiana pura;
- Euclides por resto como compressão do Euclides por subtração.
"""
import ast
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.traducao import de_int, para_bool, para_int
from nucleo.primitivas import V, F
from nucleo.divisao_euclidiana_pura import (
    DIVISAO_EUCLIDIANA_DEFINIDA,
    DIVISAO_EUCLIDIANA_PURA,
    QUOCIENTE_PURO,
    RESTO_PURO,
    DIVISAO_EUCLIDIANA_CONFERE,
)
from nucleo.euclides_resto_puro import (
    MDC_RESTO_DEFINIDO,
    MDC_RESTO_PURO,
    MDC_RESTO_CONFERE_COM_SUBTRACAO,
    MDC_RESTO_CONFERE_COM_DEFINICAO,
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


def b(x):
    return para_bool(x)


def i(x):
    return para_int(x)


def verificar_sem_dependencias_indevidas():
    """Os módulos novos não podem importar operadores prontos nem usar símbolos nativos proibidos."""
    base = os.path.join(os.path.dirname(__file__), "..", "nucleo")
    arquivos = [
        os.path.join(base, "divisao_euclidiana_pura.py"),
        os.path.join(base, "euclides_resto_puro.py"),
    ]
    nomes_importados_proibidos = {"DIV", "MOD", "MMC"}
    nomes_exatos_proibidos = {"DIV", "MOD", "MMC", "PRIMO", "FATORACAO"}
    for caminho in arquivos:
        with open(caminho, "r", encoding="utf-8") as f:
            fonte = f.read()
        arvore = ast.parse(fonte, filename=caminho)
        for no in ast.walk(arvore):
            if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
                falhas.append(f"operador nativo proibido em {os.path.basename(caminho)}")
            if isinstance(no, ast.ImportFrom):
                for alias in no.names:
                    if alias.name in nomes_importados_proibidos:
                        falhas.append(f"import proibido {alias.name} em {os.path.basename(caminho)}")
            if isinstance(no, ast.Name) and no.id in nomes_exatos_proibidos:
                falhas.append(f"nome proibido {no.id} em {os.path.basename(caminho)}")


def main():
    print("PSF-IAminy — divisão euclidiana pura e Euclides por resto")
    verificar_sem_dependencias_indevidas()

    verificar("divisão definida 17 por 5", b(DIVISAO_EUCLIDIANA_DEFINIDA(n(17))(n(5))), True)
    verificar("divisão indefinida 17 por 0", b(DIVISAO_EUCLIDIANA_DEFINIDA(n(17))(n(0))), False)

    casos_divisao = [
        (0, 5, 0, 0),
        (2, 5, 0, 2),
        (5, 5, 1, 0),
        (17, 5, 3, 2),
        (18, 6, 3, 0),
        (19, 6, 3, 1),
        (23, 7, 3, 2),
    ]
    for a, c, q, r in casos_divisao:
        verificar(f"QUOCIENTE_PURO({a},{c})", i(QUOCIENTE_PURO(n(a))(n(c))), q)
        verificar(f"RESTO_PURO({a},{c})", i(RESTO_PURO(n(a))(n(c))), r)
        verificar(f"DIVISAO_EUCLIDIANA_CONFERE({a},{c})", b(DIVISAO_EUCLIDIANA_CONFERE(n(a))(n(c))), True)

    p = DIVISAO_EUCLIDIANA_PURA(n(17))(n(5))
    verificar("par divisão 17 por 5: q", i(p(V)), 3)
    verificar("par divisão 17 por 5: r", i(p(F)), 2)

    casos_mdc = [
        (12, 18, 6),
        (18, 12, 6),
        (14, 21, 7),
        (8, 15, 1),
        (35, 10, 5),
        (37, 10, 1),
        (12, 0, 12),
        (0, 18, 18),
        (9, 9, 9),
    ]
    for a, c, esperado in casos_mdc:
        verificar(f"MDC_RESTO_PURO({a},{c})", i(MDC_RESTO_PURO(n(a))(n(c))), esperado)
        verificar(f"MDC_RESTO confere com subtração ({a},{c})", b(MDC_RESTO_CONFERE_COM_SUBTRACAO(n(a))(n(c))), True)

    casos_definicao_pequenos = [
        (4, 6),
        (6, 9),
        (8, 12),
        (5, 0),
        (0, 7),
        (5, 5),
    ]
    for a, c in casos_definicao_pequenos:
        verificar(f"MDC_RESTO confere com definição ({a},{c})", b(MDC_RESTO_CONFERE_COM_DEFINICAO(n(a))(n(c))), True)

    verificar("MDC_RESTO definido (0,0)", b(MDC_RESTO_DEFINIDO(n(0))(n(0))), False)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
