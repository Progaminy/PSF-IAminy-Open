#!/usr/bin/env python3
"""Classifica a coleta real do pytest por finalidade documental.

A unidade de classificação é o ficheiro. Isso torna a contagem reproduzível,
mas não prova profundidade nem impede que um ficheiro misture finalidades.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import subprocess
import sys

RAIZ = Path(__file__).resolve().parents[1]

SEGURANCA = {"test_seguranca_conversas.py", "test_seguranca_servidor.py"}
AUDITORIA = {
    "test_coerencia_readme_plano_relatorio_regras.py",
    "test_protecao_contra_fingimento.py",
    "test_auditoria_conhecimento_total.py",
    "test_auditoria_formulas.py",
    "test_pontes_conhecimento_matematico.py",
    "test_resolucao_profunda_pontes.py",
    "test_cobertura_total.py",
}
ENSINO = {
    "test_exercicio_real.py",
    "test_pacotes_reais.py",
    "test_navegacao_pacotes.py",
    "test_problemas_historicos.py",
}
INTEGRACAO = {
    "test_motores_dominio_comum.py",
    "test_portugues_aproveita_matematica.py",
    "test_motor_auxiliar_tolerancia.py",
    "test_validacao_auxiliar_lei_geradora.py",
    "test_decisao_auxiliar.py",
    "test_investigacao.py",
    "test_corretor_integracao.py",
    "test_chat_rotas_corretor.py",
}
TERMOS_PORTUGUES = (
    "portugues", "lexico", "morf", "normalizacao", "gramatica",
    "canal_ruidoso", "paradigmas", "corpus", "corretor", "fonetica",
    "proximidade_semantica", "distancia_edicao", "modelo_ngramas",
    "candidatos_lexicais", "espaco_lexical", "espaco_combinatorio_palavras",
    "figuras_de_som", "indice_fuzzy", "paronimos", "frequencia", "teclado",
    "uso_do_se", "verbos_irregulares", "desambiguacao", "ditongo",
)


def categoria(nome: str) -> str:
    if nome in SEGURANCA:
        return "Segurança"
    if nome.startswith("test_interface_"):
        return "Interface"
    if nome in AUDITORIA:
        return "Integridade e auditoria"
    if nome in ENSINO:
        return "Ensino e exercícios"
    if nome in INTEGRACAO:
        return "Integração e motores"
    if any(termo in nome for termo in TERMOS_PORTUGUES):
        return "Português"
    return "Matemática e estruturas finitas"


def coletar() -> Counter[str]:
    processo = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only", "-q"],
        cwd=RAIZ,
        text=True,
        capture_output=True,
        check=False,
    )
    if processo.returncode != 0:
        print(processo.stdout, end="")
        print(processo.stderr, end="", file=sys.stderr)
        raise SystemExit(processo.returncode)
    return Counter(
        linha.split("::", 1)[0]
        for linha in processo.stdout.splitlines()
        if linha.startswith("testes/") and "::" in linha
    )


def main() -> int:
    ficheiros = coletar()
    testes_por_categoria: Counter[str] = Counter()
    ficheiros_por_categoria: Counter[str] = Counter()
    for caminho, quantidade in ficheiros.items():
        grupo = categoria(Path(caminho).name)
        testes_por_categoria[grupo] += quantidade
        ficheiros_por_categoria[grupo] += 1

    print("Categoria | Testes | Ficheiros")
    print("--- | ---: | ---:")
    for grupo in sorted(testes_por_categoria):
        print(f"{grupo} | {testes_por_categoria[grupo]} | {ficheiros_por_categoria[grupo]}")
    print(f"Total | {sum(testes_por_categoria.values())} | {len(ficheiros)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

