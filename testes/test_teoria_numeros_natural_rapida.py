"""Testes da Etapa 9 rápida do fluxo natural PSF-IAminy.
Roda com: python3 testes/test_teoria_numeros_natural_rapida.py

Etapas validadas: 20 a 35.
"""
import ast
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.traducao import de_int, para_bool, para_int, para_lista, para_int_assinado
from nucleo.primitivas import V, F
from nucleo.teoria_numeros_natural import (
    DIVISIBILIDADE_FECHADA_SOMA_PURO,
    DIVISIBILIDADE_FECHADA_PRODUTO_DIREITA_PURO,
    DIVISIBILIDADE_FECHADA_PRODUTO_ESQUERDA_PURO,
    MODULO_VALIDO_PURO,
    CONGRUENTES_PURO,
    CONGRUENCIA_REFLEXIVA_PURO,
    CONGRUENCIA_SIMETRICA_PURO,
    CONGRUENCIA_TRANSITIVA_PURO,
    CLASSE_RESIDUAL_ATE_PURO,
    REPRESENTANTE_CANONICO_PURO,
    SOMA_MODULAR_PURA,
    MULT_MODULAR_PURA,
    POT_MODULAR_PURA,
    INVERSO_MODULAR_EXISTE_PURO,
    INVERSO_MODULAR_PURO,
    INVERSO_MODULAR_CONFERE_PURO,
    PHI_EULER_PURO,
    FERMAT_PEQUENO_TEOREMA_PURO,
    TEOREMA_EULER_PURO,
    CRT_HIPOTESE_PURA,
    CRT_SOLUCAO_PURA,
    CRT_CONFERE_PURO,
    DIOFANTINA_LINEAR_SOLUVEL_PURO,
    SOLUCAO_DIOFANTINA_LINEAR_PURA,
    DIOFANTINA_X_PURO,
    DIOFANTINA_Y_PURO,
    DIOFANTINA_CONFERE_PURO,
    TAU_DIVISORES_PURO,
    SIGMA_DIVISORES_PURO,
    SOMA_ALIQUOTA_PURO,
    AMIGAVEIS_PURO,
    MERSENNE_NUMERO_PURO,
    MERSENNE_PRIMO_PURO,
    FERMAT_NUMERO_PURO,
    FERMAT_PRIMO_PURO,
    PERFEITO_REVISITADO_PURO,
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


def z(x):
    return para_int_assinado(x)


def lista(x):
    return sorted(para_lista(x))


def verificar_sem_dependencias_indevidas():
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "teoria_numeros_natural.py")
    with open(caminho, "r", encoding="utf-8") as f:
        fonte = f.read()
    arvore = ast.parse(fonte, filename=caminho)
    importados_proibidos = {"DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "FATORES", "DECOMPOR"}
    modulos_proibidos = {"primos"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em teoria_numeros_natural.py")
        if isinstance(no, ast.ImportFrom):
            modulo = (no.module or "").split(".")[-1]
            if modulo in modulos_proibidos:
                falhas.append(f"módulo proibido {no.module}")
            for alias in no.names:
                if alias.name in importados_proibidos:
                    falhas.append(f"import proibido {alias.name}")


def main():
    print("PSF-IAminy — teoria dos números natural rápida, etapas 20 a 35")
    verificar_sem_dependencias_indevidas()

    verificar("divisibilidade fecha por soma: 3|6 e 3|9 => 3|15", b(DIVISIBILIDADE_FECHADA_SOMA_PURO(n(3))(n(6))(n(9))), True)
    verificar("divisibilidade fecha por produto direita: 4|12 => 4|60", b(DIVISIBILIDADE_FECHADA_PRODUTO_DIREITA_PURO(n(4))(n(12))(n(5))), True)
    verificar("divisibilidade fecha por produto esquerda: 4|12 => 4|60", b(DIVISIBILIDADE_FECHADA_PRODUTO_ESQUERDA_PURO(n(4))(n(12))(n(5))), True)

    verificar("módulo 5 válido", b(MODULO_VALIDO_PURO(n(5))), True)
    verificar("módulo 0 inválido", b(MODULO_VALIDO_PURO(n(0))), False)
    verificar("17 ≡ 2 mod 5", b(CONGRUENTES_PURO(n(17))(n(2))(n(5))), True)
    verificar("17 não ≡ 3 mod 5", b(CONGRUENTES_PURO(n(17))(n(3))(n(5))), False)
    verificar("congruência reflexiva", b(CONGRUENCIA_REFLEXIVA_PURO(n(17))(n(5))), True)
    verificar("congruência simétrica", b(CONGRUENCIA_SIMETRICA_PURO(n(17))(n(2))(n(5))), True)
    verificar("congruência transitiva", b(CONGRUENCIA_TRANSITIVA_PURO(n(17))(n(2))(n(7))(n(5))), True)
    verificar("classe residual 2 mod 5 até 17", lista(CLASSE_RESIDUAL_ATE_PURO(n(2))(n(5))(n(17))), [2, 7, 12, 17])
    verificar("representante canônico 17 mod 5", i(REPRESENTANTE_CANONICO_PURO(n(17))(n(5))), 2)

    verificar("soma modular 4+5 mod 7", i(SOMA_MODULAR_PURA(n(4))(n(5))(n(7))), 2)
    verificar("multiplicação modular 4*5 mod 7", i(MULT_MODULAR_PURA(n(4))(n(5))(n(7))), 6)
    verificar("potência modular 3^4 mod 5", i(POT_MODULAR_PURA(n(3))(n(4))(n(5))), 1)
    verificar("inverso modular existe 3 mod 7", b(INVERSO_MODULAR_EXISTE_PURO(n(3))(n(7))), True)
    verificar("inverso modular de 3 mod 7", i(INVERSO_MODULAR_PURO(n(3))(n(7))), 5)
    verificar("inverso modular confere 3 mod 7", b(INVERSO_MODULAR_CONFERE_PURO(n(3))(n(7))), True)
    verificar("inverso modular não existe 2 mod 4", b(INVERSO_MODULAR_EXISTE_PURO(n(2))(n(4))), False)

    verificar("phi(1)", i(PHI_EULER_PURO(n(1))), 1)
    verificar("phi(9)", i(PHI_EULER_PURO(n(9))), 6)
    verificar("phi(6)", i(PHI_EULER_PURO(n(6))), 2)
    verificar("Fermat: 2^4 ≡ 1 mod 5", b(FERMAT_PEQUENO_TEOREMA_PURO(n(2))(n(5))), True)
    verificar("Euler: 3^phi(4) ≡ 1 mod 4", b(TEOREMA_EULER_PURO(n(3))(n(4))), True)

    verificar("CRT hipótese 3 e 5", b(CRT_HIPOTESE_PURA(n(3))(n(5))), True)
    verificar("CRT solução x≡2 mod3, x≡3 mod5", i(CRT_SOLUCAO_PURA(n(2))(n(3))(n(3))(n(5))), 8)
    verificar("CRT confere", b(CRT_CONFERE_PURO(n(2))(n(3))(n(3))(n(5))), True)

    verificar("Diofantina 6x+9y=3 solúvel", b(DIOFANTINA_LINEAR_SOLUVEL_PURO(n(6))(n(9))(n(3))), True)
    sol = SOLUCAO_DIOFANTINA_LINEAR_PURA(n(6))(n(9))(n(3))
    verificar("Diofantina x para 6x+9y=3", z(DIOFANTINA_X_PURO(sol)), -1)
    verificar("Diofantina y para 6x+9y=3", z(DIOFANTINA_Y_PURO(sol)), 1)
    verificar("Diofantina confere 6x+9y=3", b(DIOFANTINA_CONFERE_PURO(n(6))(n(9))(n(3))), True)
    verificar("Diofantina 6x+9y=4 não solúvel", b(DIOFANTINA_LINEAR_SOLUVEL_PURO(n(6))(n(9))(n(4))), False)

    verificar("tau(12)", i(TAU_DIVISORES_PURO(n(12))), 6)
    verificar("sigma(12)", i(SIGMA_DIVISORES_PURO(n(12))), 28)
    verificar("soma alíquota 6", i(SOMA_ALIQUOTA_PURO(n(6))), 6)
    verificar("6 e 8 não são amigáveis", b(AMIGAVEIS_PURO(n(6))(n(8))), False)
    verificar("Mersenne número p=3", i(MERSENNE_NUMERO_PURO(n(3))), 7)
    verificar("Mersenne primo p=3", b(MERSENNE_PRIMO_PURO(n(3))), True)
    verificar("Fermat número n=1", i(FERMAT_NUMERO_PURO(n(1))), 5)
    verificar("Fermat primo n=1", b(FERMAT_PRIMO_PURO(n(1))), True)
    verificar("6 perfeito revisitado", b(PERFEITO_REVISITADO_PURO(n(6))), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
