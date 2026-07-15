"""Prefixos e sufixos produtivos — reconhecimento conferido contra o léxico, nunca por regra decorada.

Fecha dois limites operacionais registrados em `conhecimento_puro.py`:
'prefixo' ("Lista produtiva de prefixos ainda deve crescer") e 'sufixo'
("Lista produtiva de sufixos ainda deve crescer"). A lista abaixo é real —
prefixos e sufixos latinos/gregos produtivos em português, cada um com
sentido estável e documentado — mas o reconhecimento não aceita por
adivinhação de padrão: só declara um prefixo ou sufixo reconhecido quando
o radical que sobra depois de removê-lo já existe como entrada própria
no léxico (`Dicionario`). Sem essa conferência, "resto" seria lido como
"re-" + "sto" só porque começa com "re" — e "sto" não é palavra nenhuma.

`segmentar_morfemas` liga os dois: tenta primeiro prefixo e sufixo juntos
(o corte mais informativo), depois só prefixo, depois só sufixo, sempre
exigindo que o radical do meio já exista no léxico. Fecha o limite
operacional de 'morfema' ("a segmentação automática ainda é inicial") em
cima da mesma conferência — não por um algoritmo maior, por reaproveitar
o que os dois primeiros já provam.

Escopo honesto: só decomposição puramente concatenativa (sem mudança de
acento, de letra ou de vogal temática no radical), e só quando o radical
tem ao menos 3 letras — sem esse mínimo, o próprio teste deste módulo
pegou "desumano" sendo lido como "des-" + "um" + "-ano" só porque "um"
(numeral) é palavra válida, uma coincidência sem nenhuma relação
morfológica real. "desumano" (que também perde o h de "humano" ao
juntar) ou "rapidamente" (que perde o acento de "rápida") não são
reconhecidos por este módulo — exigiriam regras morfofonológicas que não
estão construídas aqui. Declarar None nesses casos é a resposta honesta,
não uma falha.
"""
from __future__ import annotations

from dataclasses import dataclass

from .lexico import Dicionario
from .tipos import ClasseGramatical


@dataclass(frozen=True, slots=True)
class Prefixo:
    forma: str
    sentido: str


@dataclass(frozen=True, slots=True)
class Sufixo:
    forma: str
    sentido: str
    classe_resultante: ClasseGramatical


PREFIXOS_PRODUTIVOS: tuple[Prefixo, ...] = (
    Prefixo("ante", "anterioridade no tempo ou no espaço"),
    Prefixo("anti", "oposição, contrariedade"),
    Prefixo("auto", "de si mesmo, sobre si próprio"),
    Prefixo("bi", "dois, duplicidade"),
    Prefixo("co", "companhia, junção"),
    Prefixo("contra", "oposição, posição contrária"),
    Prefixo("des", "negação, ação inversa"),
    Prefixo("ex", "estado anterior; para fora"),
    Prefixo("extra", "fora de, além de"),
    Prefixo("hiper", "excesso, grau muito elevado"),
    Prefixo("in", "negação, interioridade"),
    Prefixo("inter", "posição entre dois pontos"),
    Prefixo("intra", "posição dentro de"),
    Prefixo("mono", "unicidade"),
    Prefixo("multi", "pluralidade, muitos"),
    Prefixo("pos", "posterioridade no tempo"),
    Prefixo("pre", "anterioridade no tempo"),
    Prefixo("re", "repetição ou intensificação"),
    Prefixo("semi", "metade, parcialidade"),
    Prefixo("sub", "posição inferior, subordinação"),
    Prefixo("super", "posição superior, grau elevado"),
    Prefixo("trans", "atravessamento, mudança de lugar"),
    Prefixo("tri", "três"),
    Prefixo("ultra", "grau extremo, além do limite"),
)

SUFIXOS_PRODUTIVOS: tuple[Sufixo, ...] = (
    Sufixo("mente", "modo, maneira", ClasseGramatical.ADVERBIO),
    Sufixo("agem", "ação, resultado ou conjunto", ClasseGramatical.SUBSTANTIVO),
    Sufixo("ismo", "doutrina, sistema, tendência", ClasseGramatical.SUBSTANTIVO),
    Sufixo("ista", "seguidor de doutrina; profissão; relativo a", ClasseGramatical.ADJETIVO),
    Sufixo("mento", "ação ou resultado de ação", ClasseGramatical.SUBSTANTIVO),
    Sufixo("oso", "abundância, qualidade em grau elevado", ClasseGramatical.ADJETIVO),
    Sufixo("al", "relação, pertencimento", ClasseGramatical.ADJETIVO),
    Sufixo("ico", "relação, pertencimento", ClasseGramatical.ADJETIVO),
    Sufixo("ano", "relação, origem", ClasseGramatical.ADJETIVO),
)


@dataclass(frozen=True, slots=True)
class SegmentacaoMorfologica:
    palavra: str
    prefixo: Prefixo | None
    radical: str
    sufixo: Sufixo | None


_TAMANHO_MINIMO_RADICAL = 3


def _radical_plausivel(radical: str, dicionario: Dicionario) -> bool:
    """Um radical só conta se tiver corpo próprio, não só coincidir com uma palavra curta.

    Sem o mínimo de tamanho, "desumano" seria lido como "des-" + "um" +
    "-ano" só porque "um" (numeral) é palavra válida — coincidência, não
    estrutura morfológica real. Radicais derivacionais genuínos quase
    sempre têm ao menos 3 letras; abaixo disso é função gramatical
    (numeral, artigo, pronome), não base de derivação.
    """
    return len(radical) >= _TAMANHO_MINIMO_RADICAL and radical in dicionario


def _prefixos_candidatos(palavra: str) -> list[Prefixo]:
    minusculo = palavra.casefold()
    candidatos = [p for p in PREFIXOS_PRODUTIVOS if minusculo.startswith(p.forma)]
    candidatos.sort(key=lambda p: -len(p.forma))
    return candidatos


def _sufixos_candidatos(palavra: str) -> list[Sufixo]:
    minusculo = palavra.casefold()
    candidatos = [s for s in SUFIXOS_PRODUTIVOS if minusculo.endswith(s.forma)]
    candidatos.sort(key=lambda s: -len(s.forma))
    return candidatos


def reconhecer_prefixo(palavra: str, dicionario: Dicionario) -> Prefixo | None:
    """Reconhece um prefixo produtivo só se o radical restante já existe no léxico."""
    for prefixo in _prefixos_candidatos(palavra):
        radical = palavra[len(prefixo.forma):]
        if _radical_plausivel(radical, dicionario):
            return prefixo
    return None


def reconhecer_sufixo(palavra: str, dicionario: Dicionario) -> Sufixo | None:
    """Reconhece um sufixo produtivo só se o radical restante já existe no léxico."""
    for sufixo in _sufixos_candidatos(palavra):
        radical = palavra[: len(palavra) - len(sufixo.forma)]
        if _radical_plausivel(radical, dicionario):
            return sufixo
    return None


def segmentar_morfemas(palavra: str, dicionario: Dicionario) -> SegmentacaoMorfologica | None:
    """Decompõe palavra em prefixo?+radical+sufixo?, exigindo radical já no léxico.

    Tenta a decomposição que remove mais material primeiro (prefixo e
    sufixo juntos), depois só prefixo, depois só sufixo. Declara ``None``
    quando nenhum corte produz um radical independentemente confirmado —
    nunca arrisca uma segmentação sem essa conferência.
    """
    prefixos = _prefixos_candidatos(palavra)
    sufixos = _sufixos_candidatos(palavra)

    for prefixo in prefixos:
        for sufixo in sufixos:
            inicio, fim = len(prefixo.forma), len(palavra) - len(sufixo.forma)
            if inicio < fim and _radical_plausivel(palavra[inicio:fim], dicionario):
                return SegmentacaoMorfologica(palavra, prefixo, palavra[inicio:fim], sufixo)

    for prefixo in prefixos:
        radical = palavra[len(prefixo.forma):]
        if _radical_plausivel(radical, dicionario):
            return SegmentacaoMorfologica(palavra, prefixo, radical, None)

    for sufixo in sufixos:
        radical = palavra[: len(palavra) - len(sufixo.forma)]
        if _radical_plausivel(radical, dicionario):
            return SegmentacaoMorfologica(palavra, None, radical, sufixo)

    return None
