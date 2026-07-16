#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exemplo aprofundado de rastreabilidade: como o PSF-IAminy prova que uma
citação de dependência aponta para algo real, em vez de confiar na prosa.

Uso: python3 exemplos/rastreabilidade.py

Cobertura de teste correspondente:
testes/test_coerencia_readme_plano_relatorio_regras.py
(test_imports_python_do_nucleo_resolvem_sem_executar_modulos e as demais
funções de motor/coerencia.py e motor/rastreabilidade.py exercitadas ali).
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def secao(titulo: str) -> None:
    print(f"\n=== {titulo} ===")


def main() -> None:
    secao("Cadeia de dependências de um conceito de Português, do fundamento até ele")
    from lingua_portuguesa import MotorPortugues

    motor_pt = MotorPortugues()
    for alvo in ("interpretação", "concordância verbal"):
        caminho = motor_pt.caminho_minimo_conceito_puro(alvo)
        print(f"{alvo!r}: " + " → ".join(caminho))

    secao("Dependências reais de um conceito de Matemática (não só o nome)")
    from motor import MotorGeralIAMiny

    psf = MotorGeralIAMiny()
    unidades = psf.buscar_conhecimento("combinação simples", "matemática")
    alvo = next(u for u in unidades if u.nome == "combinacao simples")
    print(f"{alvo.nome} (origem: {alvo.origem})")
    for dep in alvo.dependencias:
        print(f"  depende de: {dep}")

    secao("Toda referência a ficheiro citada numa ETAPA aponta para algo real?")
    from motor.rastreabilidade import referencias_quebradas

    quebradas = referencias_quebradas()
    print(f"referências quebradas encontradas: {len(quebradas)} (vazio = tudo aponta para ficheiro real)")

    secao("Todo import Python do núcleo resolve, sem executar o módulo auditado?")
    from motor.rastreabilidade import imports_python_quebrados

    falhas = imports_python_quebrados()
    print(f"imports quebrados encontrados: {len(falhas)} (vazio = nenhum módulo/atributo/sintaxe quebrados)")

    secao("README e COMO_RODAR concordam na contagem de testes?")
    from motor.coerencia import divergencia_contagem_testes_entre_documentos

    divergencias = divergencia_contagem_testes_entre_documentos()
    print(f"divergências encontradas: {divergencias if divergencias else '() -- documentos coerentes entre si'}")


if __name__ == "__main__":
    main()
