#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Demonstração pública mínima do PSF-IAminy.

Uso: python3 exemplo_publico.py

Em poucos segundos mostra: uma entrada, o motor acionado, a
reconstrução/rastreabilidade do resultado, e uma limitação reconhecida
abertamente -- nada aqui é simulado; toda saída vem de chamadas reais aos
motores (ver testes/test_motores_dominio_comum.py e
testes/test_coerencia_readme_plano_relatorio_regras.py para a cobertura
automatizada correspondente).
"""
from __future__ import annotations


def demo_matematica() -> None:
    from matematica import MotorMatematica

    motor = MotorMatematica()
    entrada = "12:5"
    print(f"[Matemática] entrada: {entrada!r}")
    resolucao = motor.calcular(entrada, casas_decimais=3)
    print(f"  motor acionado: MotorMatematica.calcular")
    print(f"  estado: {resolucao.estado}")
    print(f"  resultado: {resolucao.resultado}  (forma exata: {resolucao.resultado_exato})")
    print("  reconstrução passo a passo:")
    for passo in resolucao.passos:
        print(f"    {passo.ordem}. {passo.operacao} — {passo.justificacao}")


def demo_portugues() -> None:
    from lingua_portuguesa.corretor import Corretor

    corretor = Corretor()
    entrada = "Ela nao sabia nda sobre o assunto."
    print(f"\n[Português] entrada: {entrada!r}")
    resultado = corretor.corrigir_texto(entrada)
    print("  motor acionado: Corretor.corrigir_texto")
    if resultado.sugestoes_ortografia:
        for palavra, sugestoes in resultado.sugestoes_ortografia:
            print(f"    sugestão para {palavra!r}: {', '.join(sugestoes)}")
    else:
        print("    nenhuma sugestão -- texto já reconhecido pelo léxico interno")


def demo_rastreabilidade() -> None:
    from lingua_portuguesa import MotorPortugues

    motor = MotorPortugues()
    alvo = "interpretação"
    print(f"\n[Rastreabilidade] caminho mínimo de dependências até {alvo!r}:")
    caminho = motor.caminho_minimo_conceito_puro(alvo)
    print("  " + " → ".join(caminho))
    print("  (cada elo é uma dependência real e auditável, não uma citação solta)")


def demo_limitacao() -> None:
    from matematica import MotorMatematica

    motor = MotorMatematica()
    print("\n[Limitação reconhecida] entrada: '12:0'")
    resolucao = motor.calcular("12:0")
    print(f"  estado: {resolucao.estado}")
    print("  o motor não finge um resultado nem lança erro genérico:")
    print("  divisão por zero é reconstruída como não definida, por construção, não como exceção escondida.")
    print("\n  hipótese própria ainda não integrada (declarada, não escondida):")
    for h in motor.hipoteses_pendentes():
        print(f"    {h.titulo!r} — estado: {h.estado}")


if __name__ == "__main__":
    demo_matematica()
    demo_portugues()
    demo_rastreabilidade()
    demo_limitacao()
    print("\nPara exemplos mais profundos por domínio, ver exemplos/matematica.py, exemplos/portugues.py e exemplos/rastreabilidade.py.")
