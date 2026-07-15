"""'Se' apassivador vs índice de indeterminação do sujeito — dois usos distintos do mesmo pronome.

Liga `voz passiva` (o "se" apassivador é a voz passiva sintética: "vendem-se
casas" = "casas são vendidas") e `sujeito indeterminado` (o "se" índice de
indeterminação não tem sujeito nenhum para concordar: "precisa-se de
funcionários"). A gramática escolar separa os dois por uma regra sintática
verificável, não por decoreba — este módulo aplica a mesma regra sobre o
léxico (`Dicionario`), não aceita por adivinhação:

```text
verbo + "se" + preposição              -> índice de indeterminação
                                           (verbo fica sempre na 3ª singular,
                                           não há objeto direto para concordar)
verbo + "se" + substantivo, concordando
em número com o verbo                  -> apassivador (voz passiva sintética)
verbo + "se" + substantivo, SEM
concordar em número                    -> nenhum dos dois padrões — não
                                           arrisca uma classificação errada
```

Como o tokenizador mantém "explicam-se" como uma palavra só (hífen de
ênclise), a extração do verbo é feita removendo o "-se" final e conferindo
o resultado contra o léxico como forma verbal de verdade — nunca aceita só
porque a palavra termina em "se".
"""
from __future__ import annotations

from enum import Enum

from .lexico import Dicionario
from .tipos import ClasseGramatical
from .tokenizacao import Tokenizador

_TOKENIZADOR = Tokenizador()


class UsoDoSe(Enum):
    APASSIVADOR = "apassivador"
    INDETERMINACAO = "indeterminacao"


def identificar_uso_de_se(frase: str, dicionario: Dicionario) -> UsoDoSe | None:
    """Identifica o uso do "se" numa frase, ou None quando não há prova suficiente."""
    tokens = [t for t in _TOKENIZADOR.tokenizar(frase) if t.tipo.value == "palavra"]
    for indice, token in enumerate(tokens):
        minusculo = token.texto.casefold()
        if not minusculo.endswith("se") or len(minusculo) < 4:
            continue
        candidato_verbo = token.texto[:-2].rstrip("-")
        formas_verbo = [
            e for e in dicionario.buscar(candidato_verbo)
            if e.classe == ClasseGramatical.VERBO and e.numero is not None
        ]
        if not formas_verbo:
            continue
        numero_verbo = formas_verbo[0].numero

        seguinte = tokens[indice + 1] if indice + 1 < len(tokens) else None
        if seguinte is None:
            return None
        if any(e.classe == ClasseGramatical.PREPOSICAO for e in dicionario.buscar(seguinte.texto)):
            return UsoDoSe.INDETERMINACAO

        for posterior in tokens[indice + 1: indice + 4]:
            substantivos = [
                e for e in dicionario.buscar(posterior.texto)
                if e.classe == ClasseGramatical.SUBSTANTIVO and e.numero is not None
            ]
            if substantivos:
                if substantivos[0].numero == numero_verbo:
                    return UsoDoSe.APASSIVADOR
                return None
        return None
    return None
