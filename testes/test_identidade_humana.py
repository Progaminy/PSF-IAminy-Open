"""Teste de motor/identidade_humana.py.

Roda com: python3 testes/test_identidade_humana.py
"""
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.identidade_humana import CODIGO_RECONHECIMENTO, RegistroIdentidadeHumana

falhas = []


def ok(nome, obtido, esperado):
    passou = obtido == esperado
    print(("[OK]" if passou else "[FALHOU]"), nome, obtido, esperado)
    if not passou:
        falhas.append(nome)


def main():
    print("PSF-IAminy — teste da identidade humana de PSF")

    ok("codigo de reconhecimento é a velocidade da luz", CODIGO_RECONHECIMENTO, "299792458")

    caminho = Path(tempfile.mktemp(suffix=".json"))
    try:
        registro = RegistroIdentidadeHumana(caminho)
        ok("sem factos no início", registro.fatos(), ())

        registrados = registro.registrar_fatos(["gosto de matemática", "nasci em 1990"])
        ok("registra factos novos", registrados, ("gosto de matemática", "nasci em 1990"))
        ok("fatos() reflete o que foi registado", registro.fatos(), ("gosto de matemática", "nasci em 1990"))

        registro.registrar_fatos(["gosto de matemática", "tenho um gato"])
        ok("não duplica facto repetido, acrescenta o novo", registro.fatos(), (
            "gosto de matemática", "nasci em 1990", "tenho um gato",
        ))

        registro.registrar_fatos(["", "   "])
        ok("ignora factos vazios/em branco", len(registro.fatos()), 3)

        # persistência: reabrir o mesmo caminho tem que lembrar os factos.
        outro = RegistroIdentidadeHumana(caminho)
        ok("persiste entre instâncias", outro.fatos(), registro.fatos())

        # pessoas diferentes não se misturam.
        registro.registrar_fatos(["dado de outra pessoa"], pessoa="outra_pessoa")
        ok("pessoa padrão não é afetada por outra pessoa", registro.fatos(), (
            "gosto de matemática", "nasci em 1990", "tenho um gato",
        ))
        ok("outra pessoa tem os seus próprios factos", registro.fatos("outra_pessoa"), ("dado de outra pessoa",))
    finally:
        if caminho.exists():
            caminho.unlink()

    if falhas:
        print("FALHAS", falhas)
        raise SystemExit(1)
    print("Tudo passou.")


if __name__ == "__main__":
    main()
