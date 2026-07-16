#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exemplo aprofundado do motor de Português.

Uso: python3 exemplos/portugues.py

Cobertura de teste correspondente: testes/test_corretor.py,
testes/test_corretor_integracao.py, testes/test_morfemas_afixais.py,
testes/test_morfologia_derivacional.py.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def secao(titulo: str) -> None:
    print(f"\n=== {titulo} ===")


def main() -> None:
    from lingua_portuguesa.corretor import Corretor
    from lingua_portuguesa.lexico import Dicionario
    from lingua_portuguesa.morfemas_afixais import segmentar_morfemas

    secao("Correção ortográfica: sugere, não reescreve às cegas")
    corretor = Corretor()
    frase = "Ela nao sabia nda sobre o assunto."
    resultado = corretor.corrigir_texto(frase)
    print(f"original:  {resultado.original}")
    print(f"corrigido: {resultado.corrigido}  (igual ao original -- o motor sugere, não decide sozinho)")
    for palavra, sugestoes in resultado.sugestoes_ortografia:
        print(f"  sugestão para {palavra!r}: {', '.join(sugestoes)}")

    secao("Segmentação morfológica: só aceita radical confirmado no léxico")
    dicionario = Dicionario.padrao()
    for palavra in ("felizmente", "incomum", "desumano"):
        seg = segmentar_morfemas(palavra, dicionario)
        if seg is None:
            print(f"{palavra!r} -> None (nenhum corte produziu radical confirmado -- honesto, não força uma segmentação)")
        else:
            partes = [p for p in (
                seg.prefixo.forma if seg.prefixo else None,
                seg.radical,
                seg.sufixo.forma if seg.sufixo else None,
            ) if p]
            print(f"{palavra!r} -> {'+'.join(partes)}")

    secao("Auditoria estrutural do conhecimento vivo de Português")
    from lingua_portuguesa import MotorPortugues

    motor = MotorPortugues()
    aud = motor.auditar_estrutura_portugues()
    print(f"conceitos: {aud.conceitos}  relações diretas: {aud.relacoes_diretas}")
    print(f"raízes: {aud.raizes}  duplicações: {len(aud.nomes_duplicados)}  ciclos: {len(aud.ciclos)}")


if __name__ == "__main__":
    main()
