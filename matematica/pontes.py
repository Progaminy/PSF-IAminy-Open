"""Pontes canônicas entre documentos matemáticos da linha única.

Uma ponte não prova o conceito de destino. Ela declara de onde a construção
parte e impede que um documento ou fórmula seja usado como unidade isolada.
Dependências escritas no próprio documento têm prioridade. Este registro cobre
somente documentos históricos cujo formato antigo não possuía a seção canônica
``Dependências permitidas``.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class PonteConhecimento:
    destino: str
    origens: tuple[str, ...]
    justificacao: str


_INICIAIS = {
    3: ("primitivas PSF", "igualdade", "ordem", "adição", "multiplicação"),
    4: ("divisibilidade pura", "ordem finita"),
    5: ("subtração natural", "divisor comum"),
    6: ("diferença controlada", "MDC puro"),
    7: ("adição", "multiplicação", "ordem", "subtração controlada"),
    8: ("quociente puro", "subtração controlada"),
    9: ("resto e divisão euclidiana", "MDC puro"),
    10: ("divisibilidade pura", "divisor próprio", "ordem"),
    11: ("primalidade pura", "divisibilidade pura", "produto finito"),
    12: ("divisibilidade pura", "múltiplos", "enumeração finita"),
    13: ("primalidade pura", "fatoração pura", "indução finita"),
    14: ("existência da fatoração prima", "lema de Euclides"),
    15: ("fatoração prima", "MDC puro", "multiplicação"),
    16: ("números naturais", "diferença", "par ordenado"),
    17: ("inteiros relativos", "Euclides por resto", "combinação linear"),
    18: ("identidade de Bézout", "divisibilidade pura", "primalidade pura"),
    19: ("existência da fatoração prima", "lema de Euclides"),
    20: ("divisibilidade pura", "adição"),
    21: ("divisibilidade pura", "multiplicação"),
    22: ("resto euclidiano puro", "igualdade"),
    23: ("congruência por igualdade de restos", "igualdade"),
    24: ("congruência", "igualdade de restos"),
    25: ("classes residuais", "adição"),
    26: ("classes residuais", "multiplicação"),
    27: ("multiplicação modular", "potência por repetição"),
    28: ("multiplicação modular", "Bézout", "coprimalidade"),
    29: ("primalidade", "potência modular", "divisibilidade"),
    30: ("coprimalidade", "enumeração finita"),
    31: ("função phi de Euler", "potência modular", "Bézout"),
    32: ("congruência", "inverso modular", "coprimalidade"),
    33: ("inteiros relativos", "Bézout", "MDC"),
    34: ("divisibilidade", "enumeração finita", "soma finita"),
    35: ("funções aritméticas", "divisores", "fatoração"),
}

_BLOCOS = {
    301: ("métodos finitos", "funções", "composição", "identidade"),
    481: ("gramáticas finitas", "transições", "reescrita finita"),
    521: ("semântica operacional finita", "estado finito", "transição"),
    561: ("autômatos finitos", "palavras finitas", "aceitação"),
    601: ("linguagens regulares", "gramáticas finitas", "derivação"),
    641: ("semântica operacional", "tipos finitos", "relações"),
    681: ("gramáticas finitas", "árvores finitas", "derivação"),
    701: ("semântica operacional", "funções finitas", "estado"),
    721: ("expressões finitas", "reescrita", "provas finitas"),
    761: ("autômatos finitos", "pilha finita", "gramáticas"),
    801: ("execução finita", "contagem", "recursos"),
    841: ("sequências finitas", "diferenças", "somas finitas"),
    881: ("conjuntos finitos", "relações", "abertos finitos"),
    921: ("conjuntos finitos", "pesos racionais", "soma finita"),
    961: ("medida finita", "dados finitos", "frequência"),
    991: ("ordem finita", "função objetivo", "modelos finitos"),
    1031: ("sucessor", "adição", "multiplicação", "potência por repetição"),
    1032: ("potência por repetição", "racionais finitos", "soma finita", "primalidade"),
}


def ponte_historica(arquivo: str, destino: str) -> PonteConhecimento | None:
    nome = Path(arquivo).name
    if not nome.startswith("ETAPA_"):
        return None
    partes = nome.split("_")
    try:
        marcador = int(partes[1])
    except (IndexError, ValueError):
        return None
    origens = _INICIAIS.get(marcador) or _BLOCOS.get(marcador)
    if not origens:
        return None
    return PonteConhecimento(
        destino=destino,
        origens=origens,
        justificacao="ponte canônica explícita para documento em formato histórico",
    )


def _tem_dependente_real(conceito, conceitos: tuple[object, ...]) -> bool:
    """Um conceito sem dependências pode ser uma RAIZ real (nada depende
    de nada antes dela, mas outros conceitos dependem dela) ou um
    conceito genuinamente isolado (nada aponta para ele nos dois
    sentidos). Achado real: antes desta função, `auditar_pontes` marcava
    QUALQUER dependências vazias como "isolado" -- confundia "não precisa
    de nada antes" com "ninguém usa isto", exatamente o tipo de raiz que
    Português já tem ("diferença") mas Matemática nunca teve até a
    Etapa 1 (número natural)."""
    from .resolucao_pontes import ALIASES_CONCEITOS, normalizar_termo

    alvo = normalizar_termo(getattr(conceito, "nome", ""))
    for outro in conceitos:
        if outro is conceito:
            continue
        for dep in getattr(outro, "dependencias_declaradas", ()):
            termo = normalizar_termo(dep)
            termo = ALIASES_CONCEITOS.get(termo, termo)
            if termo == alvo:
                return True
    return False


def auditar_pontes(conceitos: tuple[object, ...]) -> dict[str, object]:
    isolados: list[str] = []
    sem_construcao: list[str] = []
    sem_implementacao: list[str] = []
    sem_validacao: list[str] = []
    for conceito in conceitos:
        if not getattr(conceito, "dependencias_declaradas", ()) and not _tem_dependente_real(conceito, conceitos):
            isolados.append(getattr(conceito, "nome", "?"))
        construcao = getattr(conceito, "construcao", "")
        if not construcao or "ainda não extraída" in construcao:
            sem_construcao.append(getattr(conceito, "nome", "?"))
        if not getattr(conceito, "implementacoes", ()):
            sem_implementacao.append(getattr(conceito, "nome", "?"))
        if not getattr(conceito, "testes", ()):
            sem_validacao.append(getattr(conceito, "nome", "?"))
    return {
        "conceitos": len(conceitos),
        "isolados": tuple(isolados),
        "sem_construcao": tuple(sem_construcao),
        "sem_implementacao": tuple(sem_implementacao),
        "sem_validacao": tuple(sem_validacao),
        "todos_tem_ponte": not isolados,
        "regra_de_uso": "conceito sem ponte fica bloqueado; fórmula isolada nunca é fundamento",
    }
