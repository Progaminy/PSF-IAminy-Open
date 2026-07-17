#!/usr/bin/env python3
"""Audita evidência explícita e duplicação sintática das funções de teste."""
from __future__ import annotations

import ast
from collections import defaultdict
import hashlib
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def _eh_pytest_raises(no: ast.AST) -> bool:
    return (
        isinstance(no, ast.Call)
        and isinstance(no.func, ast.Attribute)
        and no.func.attr == "raises"
    )


def main() -> int:
    funcoes = []
    falhas_sintaxe = []
    for caminho in sorted((RAIZ / "testes").rglob("test_*.py")):
        try:
            arvore = ast.parse(caminho.read_text(encoding="utf-8"))
        except SyntaxError as erro:
            falhas_sintaxe.append(f"{caminho.relative_to(RAIZ)}:{erro.lineno}")
            continue
        for no in ast.walk(arvore):
            if not isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef)) or not no.name.startswith("test_"):
                continue
            assercoes = sum(isinstance(item, ast.Assert) for item in ast.walk(no))
            excecoes = sum(_eh_pytest_raises(item) for item in ast.walk(no))
            corpo = ast.dump(ast.Module(body=no.body, type_ignores=[]), include_attributes=False)
            funcoes.append({
                "arquivo": str(caminho.relative_to(RAIZ)),
                "nome": no.name,
                "linha": no.lineno,
                "asserts": assercoes,
                "raises": excecoes,
                "corpo": corpo,
            })

    sem_evidencia = [f for f in funcoes if not f["asserts"] and not f["raises"]]
    por_corpo = defaultdict(list)
    for funcao in funcoes:
        chave = hashlib.sha256(funcao["corpo"].encode("utf-8")).hexdigest()
        por_corpo[chave].append(funcao)
    duplicados = [grupo for grupo in por_corpo.values() if len(grupo) > 1]

    print(f"Ficheiros com erro de sintaxe: {len(falhas_sintaxe)}")
    print(f"Funções test_*: {len(funcoes)}")
    print(f"Instruções assert: {sum(int(f['asserts']) for f in funcoes)}")
    print(f"Usos de pytest.raises: {sum(int(f['raises']) for f in funcoes)}")
    print(f"Funções sem assert/pytest.raises explícito: {len(sem_evidencia)}")
    print(f"Grupos de corpos AST exatamente duplicados: {len(duplicados)}")
    if falhas_sintaxe:
        print("Erros de sintaxe:")
        print("\n".join(f"- {item}" for item in falhas_sintaxe))
    if sem_evidencia:
        print("Sem evidência explícita (revisão manual necessária):")
        for f in sem_evidencia:
            print(f"- {f['arquivo']}:{f['linha']}::{f['nome']}")
    if duplicados:
        print("Corpos duplicados:")
        for grupo in duplicados:
            print("- " + ", ".join(f"{f['arquivo']}:{f['linha']}::{f['nome']}" for f in grupo))
    return 1 if falhas_sintaxe or sem_evidencia or duplicados else 0


if __name__ == "__main__":
    raise SystemExit(main())

