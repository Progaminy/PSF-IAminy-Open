"""Ponto de entrada: resolve os exercícios de um anexo com o resolvedor
"modo cientista" (ensino/resolvedor_exercicios.py).

Uso: python3 ensino/resolver_anexo.py [caminho]

Sem caminho, resolve `privado/avalmath.docx` -- o anexo real (avaliações
de matemática por país/classe) que motivou este resolvedor.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
if str(RAIZ) not in sys.path:
    sys.path.insert(0, str(RAIZ))

from ensino.leitura_documentos import ler_anexo  # noqa: E402
from ensino.resolvedor_exercicios import Resolucao, resolver  # noqa: E402

ANEXO_PADRAO = RAIZ / "privado" / "avalmath.docx"

_PADRAO_CLASSE = re.compile(r"^\d{1,2}$")
_PADRAO_PERGUNTA = re.compile(r"^([1-9])\.\s+(.*)$")


def extrair_avaliacoes_por_classe(texto: str) -> dict[int, list[str]]:
    """Agrupa perguntas por classe, guardando só a primeira ocorrência de
    cada classe -- o documento repete as mesmas perguntas por país, só o
    nome do país muda (ver estrutura inspecionada em `privado/avalmath.docx`:
    linha "país" -> linha "classe" (só dígitos) -> linhas "N. pergunta")."""
    linhas = [linha.strip() for linha in texto.splitlines() if linha.strip()]
    por_classe: dict[int, list[str]] = {}
    i = 0
    while i < len(linhas):
        if not _PADRAO_CLASSE.match(linhas[i]):
            i += 1
            continue
        classe = int(linhas[i])
        j = i + 1
        perguntas: list[str] = []
        while j < len(linhas):
            m_pergunta = _PADRAO_PERGUNTA.match(linhas[j])
            if not m_pergunta:
                break
            perguntas.append(m_pergunta.group(2))
            j += 1
        if perguntas and classe not in por_classe:
            por_classe[classe] = perguntas
        i = j
    return por_classe


def resolver_texto_por_classe(texto: str) -> dict[int, list[Resolucao]]:
    """Extrai perguntas por classe de um texto já extraído (ver
    `extrair_avaliacoes_por_classe`) e resolve cada uma. Devolve vazio
    quando o texto não tem essa estrutura tabular por classe -- ver
    `ensino.dialogo` para o que fazer nesse caso (cair para tentar
    resolver o texto inteiro como uma única pergunta)."""
    return {
        classe: [resolver(p) for p in perguntas]
        for classe, perguntas in extrair_avaliacoes_por_classe(texto).items()
    }


def resolver_anexo(caminho: "Path | str") -> dict[int, list[Resolucao]]:
    """Lê o anexo, extrai as perguntas por classe e resolve cada uma.
    Devolve {classe: [Resolucao, ...]}."""
    documentos = ler_anexo(caminho)
    resultado: dict[int, list[Resolucao]] = {}
    for texto in documentos.values():
        resultado.update(resolver_texto_por_classe(texto))
    return resultado


def imprimir_relatorio(resultado: dict[int, list[Resolucao]]) -> None:
    total = sum(len(rs) for rs in resultado.values())
    resolvidas = sum(1 for rs in resultado.values() for r in rs if r.resolvida)
    print(f"PSF-IAminy — relatório de resolução ({len(resultado)} classes, {total} perguntas)")
    print("=" * 70)
    for classe in sorted(resultado):
        print(f"\nClasse {classe}")
        for r in resultado[classe]:
            marca = "OK" if r.resolvida else "??"
            print(f"  [{marca}] {r.pergunta}")
            if r.resolvida:
                print(f"       resposta: {r.resposta}")
                print(f"       raciocínio: {r.raciocinio}")
            else:
                print(f"       {r.raciocinio}")
    print("\n" + "=" * 70)
    if total:
        print(f"Resolvidas: {resolvidas}/{total} ({resolvidas / total:.0%})")


def main(argv: "list[str] | None" = None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    caminho = Path(argv[0]) if argv else ANEXO_PADRAO
    imprimir_relatorio(resolver_anexo(caminho))


if __name__ == "__main__":
    main()
