"""PSF-IAminy — teste do controlo de tempo do motor.

Garante que o motor não volta a usar a bateria pesada como padrão e que
um teste que ultrapassa timeout é morto e reportado, não deixa o comando
preso.

Roda com: python3 testes/test_motor_execucao_controle.py
"""
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.execucao import (
    TESTES_PADRAO,
    TESTES_PESADOS_CONHECIDOS,
    testes_do_perfil as _testes_do_perfil,
    _executar_um_teste,
)

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def main():
    print("PSF-IAminy — teste do motor de execução controlada")

    padrao = [p.name for p in _testes_do_perfil("padrao")]
    completo = [p.name for p in _testes_do_perfil("completo")]

    verificar("perfil padrão tem exatamente a lista declarada", padrao, TESTES_PADRAO)
    verificar(
        "perfil padrão não inclui testes pesados conhecidos",
        sorted(set(padrao) & TESTES_PESADOS_CONHECIDOS),
        [],
    )
    verificar(
        "perfil completo contém os testes pesados conhecidos existentes",
        TESTES_PESADOS_CONHECIDOS <= set(completo),
        True,
    )
    verificar("perfil rápido/meta não executa testes", _testes_do_perfil("rapido"), [])

    # Teste real do timeout: script que dorme mais do que o limite. O motor
    # deve retornar em timeout, não ficar bloqueado.
    temp = Path(tempfile.mktemp(suffix="_psf_timeout.py"))
    temp.write_text("import time\ntime.sleep(2)\n", encoding="utf-8")
    try:
        r = _executar_um_teste(temp, timeout_segundos=0.2)
        verificar("teste lento é marcado como timeout", r["timeout"], True)
        verificar("teste lento não passa", r["passou"], False)
    finally:
        temp.unlink(missing_ok=True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
