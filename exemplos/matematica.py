#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exemplo aprofundado do motor de Matemática.

Uso: python3 exemplos/matematica.py

Cobertura de teste correspondente: testes/test_motores_dominio_comum.py
(test_divisao_racional_e_decimal_sao_reconstruidas_sem_magia,
test_divisao_periodica_preserva_fracao_e_controla_precisao,
test_divisao_por_zero_e_conhecimento_reconstruido_e_nao_investigacao_aberta,
test_motor_matematica_prova_finita_certificada).
"""
from __future__ import annotations

import os
import sys

# Evita colisão de nome: rodar "python3 exemplos/matematica.py" adiciona
# exemplos/ ao início de sys.path, e este próprio ficheiro se chama
# "matematica.py" -- sem isto, "import matematica" se importaria a si
# mesmo em vez do pacote real na raiz do projeto.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from matematica import MotorMatematica


def secao(titulo: str) -> None:
    print(f"\n=== {titulo} ===")


def main() -> None:
    motor = MotorMatematica()

    secao("Divisão exata vs. periódica, com precisão controlada")
    for expressao, casas, modo in (
        ("12:5", None, None),
        ("1:3", 3, None),
        ("2:3", 3, "arredondar"),
    ):
        kwargs = {}
        if casas is not None:
            kwargs["casas_decimais"] = casas
        if modo is not None:
            kwargs["modo"] = modo
        r = motor.calcular(expressao, **kwargs)
        print(f"{expressao} -> {r.resultado} (exato: {r.resultado_exato}, estado: {r.estado})")

    secao("Divisão por zero: não definida por construção, não escondida")
    r = motor.calcular("12:0")
    print(f"estado: {r.estado}")
    for passo in r.passos:
        print(f"  {passo.ordem}. {passo.operacao} — {passo.justificacao}")

    secao("Expressão composta com precedência real")
    r = motor.calcular("2+2*3")
    print(f"2+2*3 -> {r.resultado} (conhecimento usado: {', '.join(r.conhecimento_usado)})")

    secao("Prova formal no fragmento lógico finito (modus ponens encadeado)")
    imp = lambda a, b: ("implica", a, b)
    premissas = ("p", imp("p", "q"), imp("q", "r"))
    prova = motor.provar_finito(premissas, "r")
    print(f"premissas: {premissas}  conclusão buscada: 'r'")
    print(f"válida: {prova.valida}  estado: {prova.estado}")
    print("passos da prova:")
    for i, passo in enumerate(prova.passos):
        regra = passo[0]
        conclusao = passo[2][2]
        print(f"  {i}. [{regra}] conclui: {conclusao}")

    secao("Hipótese própria pendente (não confundida com conhecimento pronto)")
    for h in motor.hipoteses_pendentes():
        print(f"título: {h.titulo}")
        print(f"estado: {h.estado}")
        print(f"autor: {h.autor}")


if __name__ == "__main__":
    main()
