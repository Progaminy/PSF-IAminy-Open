"""Leitor histórico da linha matemática única do PSF-IAminy.

Os nomes ETAPA são marcadores de localização preservados por compatibilidade.
Não são versões, camadas de verdade ou fundamento da ordem matemática.

Camada meta, não núcleo matemático. Pode usar Python nativo porque apenas
inspeciona arquivos, nomes e continuidade do projeto. A matemática em si
continua nos módulos de ``nucleo/``.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

RAIZ = Path(__file__).resolve().parents[1]
CONHECIMENTO = RAIZ / "conhecimento"
PADRAO_ETAPA = re.compile(r"ETAPA_(\d{2,4})_(.+)\.md$")
PADRAO_ETAPA_INTERVALO = re.compile(r"ETAPA_(\d{2,4})_(\d{2,4})_(.+)\.md$")
PROXIMO_FLUXO_ARQUIVO = CONHECIMENTO / "PROXIMO_FLUXO_NATURAL.md"
PADRAO_LINHA_PROXIMO = re.compile(r"^\|\s*(\d{1,4})\s*\|\s*([^|]+?)\s*\|")

ETAPAS_IMPLICITAS = {
    1: "núcleo primitivo e aritmética inicial",
    2: "modelo eficiente e validação externa inicial",
}

# Registo histórico do fluxo natural mantido em código só por compatibilidade
# com os primeiros testes do motor (61-135). Fluxo vivo depois disso deve ficar
# em conhecimento/PROXIMO_FLUXO_NATURAL.md, onde pode ser editado como dado.
# Assim o motor deixa de fingir que uma lista antiga no código é a fonte de
# verdade para etapas que já avançaram muito além dela.
PROXIMO_FLUXO_NATURAL = [
    (61, "relações binárias"),
    (62, "pertencimento relacional"),
    (63, "reflexividade"),
    (64, "simetria"),
    (65, "transitividade"),
    (66, "relações de equivalência"),
    (67, "classes de equivalência gerais"),
    (68, "ordens parciais"),
    (69, "ordens totais"),
    (70, "função como relação especial"),
    (71, "aplicação finita"),
    (72, "função identidade"),
    (73, "função constante"),
    (74, "composição de funções"),
    (75, "injetividade"),
    (76, "sobrejetividade"),
    (77, "bijetividade"),
    (78, "inversa relacional"),
    (79, "imagem e pré-imagem"),
    (80, "fechamento relacional-funcional inicial"),
    (81, "operação binária"),
    (82, "fechamento de operação"),
    (83, "associatividade"),
    (84, "elemento neutro"),
    (85, "comutatividade"),
    (86, "semigrupo"),
    (87, "monóide"),
    (88, "inverso algébrico"),
    (89, "grupo"),
    (90, "anel inicial"),
    (91, "anel comutativo"),
    (92, "anel com unidade"),
    (93, "domínio de integridade"),
    (94, "corpo finito inicial"),
    (95, "homomorfismo de grupos"),
    (96, "isomorfismo"),
    (97, "núcleo e imagem de homomorfismo"),
    (98, "subgrupo"),
    (99, "classes laterais"),
    (100, "fechamento algébrico inicial"),
    (101, "polinômios sobre um anel"),
    (102, "grau e operações polinomiais"),
    (103, "raízes de polinômios"),
    (104, "espaço vetorial finito inicial"),
    (105, "combinação linear e base"),
    (106, "matriz como aplicação linear finita"),
    (107, "determinante em dimensão pequena"),
    (108, "eliminação gaussiana finita"),
    (109, "posto de uma matriz"),
    (110, "sistemas lineares finitos"),
    (111, "grafo como relação binária sobre vértices finitos"),
    (112, "grau de um vértice"),
    (113, "caminho em grafo finito"),
    (114, "ciclo em grafo finito"),
    (115, "conectividade"),
    (116, "árvore como grafo especial"),
    (117, "grafo bipartido"),
    (118, "coloração de grafo finito"),
    (119, "grafo completo"),
    (120, "complemento de grafo"),
    (121, "isomorfismo de grafos finito"),
    (122, "subgrafo"),
    (123, "grafo Euleriano"),
    (124, "grafo Hamiltoniano"),
    (125, "matriz de adjacência"),
    (126, "grafo ponderado finito"),
    (127, "fechamento de grafos"),
    (128, "árvore geradora mínima"),
    (129, "caminho mínimo em grafo ponderado"),
    (130, "fechamento discreto geral"),
    (131, "expressão simbólica finita"),
    (132, "avaliação de expressão sobre um domínio finito"),
    (133, "equação de primeiro grau finita"),
    (134, "binário posicional finito"),
    (135, "equação quadrática finita"),
    # Equação quadrática real por fórmula continua bloqueada por raiz
    # quadrada geral. A etapa 135 resolve apenas o caso finito por busca
    # exaustiva, dentro de domínio explícito.
]


@dataclass(frozen=True)
class Etapa:
    numero: int
    nome: str
    arquivo: str


def etapas_documentadas(base: Path | None = None) -> list[Etapa]:
    """Devolve as etapas encontradas em conhecimento/ ordenadas pelo número."""
    base = base or CONHECIMENTO
    etapas: list[Etapa] = []
    for arquivo in sorted(base.glob("ETAPA_*.md")):
        intervalo = PADRAO_ETAPA_INTERVALO.match(arquivo.name)
        if intervalo:
            inicio = int(intervalo.group(1))
            fim = int(intervalo.group(2))
            nome = intervalo.group(3).replace("_", " ").lower()
            for numero in range(inicio, fim + 1):
                etapas.append(Etapa(numero, nome, str(arquivo.relative_to(RAIZ))))
            continue
        m = PADRAO_ETAPA.match(arquivo.name)
        if not m:
            continue
        numero = int(m.group(1))
        nome = m.group(2).replace("_", " ").lower()
        etapas.append(Etapa(numero, nome, str(arquivo.relative_to(RAIZ))))
    return sorted(etapas, key=lambda e: e.numero)


def proximos_documentados(base: Path | None = None) -> list[tuple[int, str]]:
    """Lê conhecimento/PROXIMO_FLUXO_NATURAL.md como dado externo.

    O motor não deve depender eternamente de uma lista fixa escrita no código.
    Este parser aceita linhas de tabela Markdown no formato:

        | 481 | semântica operacional ... |

    Linhas inválidas são ignoradas; se o ficheiro não existir, devolve vazio.
    """
    caminho = base or PROXIMO_FLUXO_ARQUIVO
    if not caminho.exists():
        return []
    saida: list[tuple[int, str]] = []
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        m = PADRAO_LINHA_PROXIMO.match(linha.strip())
        if not m:
            continue
        numero = int(m.group(1))
        conceito = m.group(2).strip().lower()
        saida.append((numero, conceito))
    return sorted(set(saida))


def relatorio_fluxo() -> dict[str, object]:
    """Relatório simples de continuidade do fluxo natural."""
    etapas = etapas_documentadas()
    numeros = set(ETAPAS_IMPLICITAS) | {e.numero for e in etapas}
    maior = max(numeros) if numeros else 0
    faltando = [n for n in range(1, maior + 1) if n not in numeros]
    return {
        "linha_unica": True,
        "etapas_sao_marcadores": True,
        "autoridade_estrutural": "construção, dependências declaradas, implementação e testes",
        "maior_etapa": maior,
        "total_contabilizado": len(numeros),
        "faltando_ate_maior": faltando,
        "proxima": proxima_etapa_natural(maior),
        "arquivos_documentados": [e.arquivo for e in etapas],
    }


def proxima_etapa_natural(atual: int | None = None) -> tuple[int, str]:
    """Compatibilidade: sugere o próximo marcador documental registrado.

    Não cria nova versão nem dá autoridade matemática ao número.

    Sugere a próxima etapa pelo fluxo natural registrado.

    Ordem de confiança:
    1. registo histórico em código (61-135), mantido por compatibilidade;
    2. registo vivo em conhecimento/PROXIMO_FLUXO_NATURAL.md;
    3. fallback explícito, sem fingir nome específico quando nada foi
       declarado.
    """
    if atual is None:
        atual = int(relatorio_fluxo()["maior_etapa"])
    candidatos = sorted(set(PROXIMO_FLUXO_NATURAL + proximos_documentados()))
    for numero, nome in candidatos:
        if numero > atual:
            return numero, nome
    return atual + 1, "novo bloco natural a especificar"
