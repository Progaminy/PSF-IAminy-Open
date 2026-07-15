"""PSF-IAminy — Reticulado Finito, Etapa 1067.
Roda com: python3 testes/test_reticulado_finito.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nucleo.primitivas import PAR
from nucleo.traducao import de_int, para_bool, para_int
from nucleo.relacoes_funcoes_naturais import DOMINIO_FINITO_PURO, RELACAO_BINARIA_FINITA_PURA
from nucleo.reticulado_finito import SUPREMO_OU_NONE, INFIMO_OU_NONE, EH_RETICULADO_PURA

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def _v(n):
    return de_int(n)


def main():
    print("PSF-IAminy — Reticulado Finito, Etapa 1067")

    print("\n[reticulado B2] domínio {0,1,2,3}, ordem = subconjunto de {a,b} (0=vazio, 1={a}, 2={b}, 3={a,b})")
    d = [_v(0), _v(1), _v(2), _v(3)]
    dominio = DOMINIO_FINITO_PURO(*d)
    ordem_b2 = RELACAO_BINARIA_FINITA_PURA(
        PAR(_v(0))(_v(0)), PAR(_v(0))(_v(1)), PAR(_v(0))(_v(2)), PAR(_v(0))(_v(3)),
        PAR(_v(1))(_v(1)), PAR(_v(1))(_v(3)),
        PAR(_v(2))(_v(2)), PAR(_v(2))(_v(3)),
        PAR(_v(3))(_v(3)),
    )
    sup_1_2 = SUPREMO_OU_NONE(_v(1), _v(2), dominio, ordem_b2)
    inf_1_2 = INFIMO_OU_NONE(_v(1), _v(2), dominio, ordem_b2)
    verificar("supremo({a},{b}) = {a,b} = 3", para_int(sup_1_2), 3)
    verificar("ínfimo({a},{b}) = vazio = 0", para_int(inf_1_2), 0)
    verificar("supremo(0,3) = 3 (0 é o mínimo)", para_int(SUPREMO_OU_NONE(_v(0), _v(3), dominio, ordem_b2)), 3)
    verificar("ínfimo(0,3) = 0", para_int(INFIMO_OU_NONE(_v(0), _v(3), dominio, ordem_b2)), 0)
    verificar("B2 é reticulado", para_bool(EH_RETICULADO_PURA(dominio, ordem_b2)), True)

    print("\n[não-reticulado] domínio {0,1,2,3,4}: 0 abaixo de tudo; 1,2 abaixo de 3 E de 4; 3,4 incomparáveis")
    d2 = [_v(i) for i in range(5)]
    dominio2 = DOMINIO_FINITO_PURO(*d2)
    ordem_n = RELACAO_BINARIA_FINITA_PURA(
        PAR(_v(0))(_v(0)), PAR(_v(0))(_v(1)), PAR(_v(0))(_v(2)), PAR(_v(0))(_v(3)), PAR(_v(0))(_v(4)),
        PAR(_v(1))(_v(1)), PAR(_v(1))(_v(3)), PAR(_v(1))(_v(4)),
        PAR(_v(2))(_v(2)), PAR(_v(2))(_v(3)), PAR(_v(2))(_v(4)),
        PAR(_v(3))(_v(3)),
        PAR(_v(4))(_v(4)),
    )
    sup_1_2 = SUPREMO_OU_NONE(_v(1), _v(2), dominio2, ordem_n)
    verificar("supremo(1,2) não existe (3 e 4 são cotas superiores incomparáveis, nenhuma é a menor)", sup_1_2, None)
    inf_3_4 = INFIMO_OU_NONE(_v(3), _v(4), dominio2, ordem_n)
    verificar("ínfimo(3,4) também não existe (0,1,2 são cotas inferiores comuns, mas 1 e 2 são incomparáveis entre si)", inf_3_4, None)
    inf_0_3 = INFIMO_OU_NONE(_v(0), _v(3), dominio2, ordem_n)
    verificar("ínfimo(0,3) existe e é 0 (0 é mínimo do domínio)", para_int(inf_0_3), 0)
    verificar("NÃO é reticulado (falta supremo de 1,2 e ínfimo de 3,4)", para_bool(EH_RETICULADO_PURA(dominio2, ordem_n)), False)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
