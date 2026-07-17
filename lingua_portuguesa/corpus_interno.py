"""Corpus interno real -- primeiro corpus de texto PT para o corretor
(Fase 4.3 do plano), construído inteiramente a partir de prosa PT já real
e autoral dentro deste repositório: os campos construção/função/lacuna/
exemplos mínimos/distinções de cada um dos conceitos reais de
`conhecimento_puro.py`. Zero fonte externa nova.

`conhecimento/PORTUGUES_CONHECIMENTO_PURO.md` foi conferido e não é usado
aqui: o próprio cabeçalho do ficheiro declara que é "materializado a
partir da linha canónica em lingua_portuguesa/conhecimento_puro.py" -- é
uma renderização mecânica dos MESMOS dados, não uma segunda fonte de
prosa independente. Somá-lo inflaria a contagem de tokens sem acrescentar
nenhum texto genuinamente novo.

`frases_do_conhecimento_puro()`/`tokens_do_corpus()` continuam exatamente
como estavam (testados com conteúdo e ordem específicos) -- este módulo só
GANHOU uma segunda fonte, não substituiu a primeira.

Corpus AMPLO (`tokens_do_corpus_amplo`, item da meta de vocabulário --
mesma decisão que estava em aberto desde a Fase 3): lê a prosa PT genuína
já autoral do resto do repositório -- `README.md`, `RELATORIO_UNICO.md`,
`PLANO_PSF_IAMINY.md`, `COMO_RODAR.md` e todo `conhecimento/*.md`. Zero
fonte nova: é só ler o que o próprio projeto já escreveu. Blocos de código
cercados (```...```) e trechos de código inline (`...`) são removidos
antes de tokenizar -- identificadores de código (`SOMA`, `MULT`, `ITER`)
e notação de fórmula (`a × k = b`) não são vocabulário de português, e
misturá-los inflaria a contagem sem acrescentar palavra real nenhuma.
Tokens com menos de 3 letras também ficam de fora deste corpus amplo (não
do léxico em si) -- auditoria real (script ad-hoc, não neste módulo)
mediu que são quase todos variável de fórmula matemática solta ("a", "k",
"ab"), não palavra portuguesa de verdade.

**Aviso honesto, não escondido**: mesmo ampliado, este corpus continua
enviesado para vocabulário técnico/matemático/didático -- não é
representativo do português geral falado ou escrito. Um corpus geral
externo continua fora de cogitação (decisão do autor: zero fonte externa).
"""
from __future__ import annotations

import re
from pathlib import Path

from psf_iaminy.recursos import caminho_documento

from .conhecimento_puro import CONCEITOS_PORTUGUES_PURO
from .tipos import TipoToken
from .tokenizacao import Tokenizador

_tokenizador = Tokenizador()

_RAIZ = Path(__file__).resolve().parent.parent

_DOCUMENTOS_PROSA_AMPLA: tuple[str, ...] = (
    "README.md",
    "RELATORIO_UNICO.md",
    "PLANO_PSF_IAMINY.md",
    "COMO_RODAR.md",
)

_BLOCO_CODIGO = re.compile(r"```.*?```", re.DOTALL)
_CODIGO_INLINE = re.compile(r"`[^`]*`")


def frases_do_conhecimento_puro() -> tuple[str, ...]:
    """Toda a prosa PT real (não listas de nomes/dependências) dos
    conceitos puros: construção, função, lacuna (quando existe), exemplos
    mínimos e notas de distinção."""
    frases: list[str] = []
    for conceito in CONCEITOS_PORTUGUES_PURO:
        if conceito.construcao:
            frases.append(conceito.construcao)
        if conceito.funcao:
            frases.append(conceito.funcao)
        if conceito.lacuna:
            frases.append(conceito.lacuna)
        frases.extend(exemplo for exemplo in conceito.exemplos_minimos if exemplo)
        frases.extend(nota for nota in conceito.nao_confundir_com if nota)
    return tuple(frases)


def tokens_do_corpus() -> tuple[str, ...]:
    """Todas as formas de PALAVRA (sem pontuação/números/símbolos) do
    corpus, em ordem -- unidade básica para os modelos de frequência e
    n-grama das próximas fases (5)."""
    tokens: list[str] = []
    for frase in frases_do_conhecimento_puro():
        for token in _tokenizador.tokenizar(frase):
            if token.tipo == TipoToken.PALAVRA:
                tokens.append(token.normalizado)
    return tuple(tokens)


def _caminhos_prosa_ampla() -> tuple[Path, ...]:
    caminhos = [caminho_documento(nome) for nome in _DOCUMENTOS_PROSA_AMPLA]
    caminhos.extend(sorted((_RAIZ / "conhecimento").glob("*.md")))
    return tuple(p for p in caminhos if p.is_file())


def _limpar_codigo(texto: str) -> str:
    """Remove blocos de código cercados e trechos inline antes de tokenizar
    -- identificador de código e notação de fórmula não são vocabulário de
    português, mesmo sendo só letras (`SOMA`, `MULT`, `a × k = b`)."""
    texto = _BLOCO_CODIGO.sub(" ", texto)
    texto = _CODIGO_INLINE.sub(" ", texto)
    return texto


def frases_da_prosa_autoral_ampla() -> tuple[str, ...]:
    """Texto (fora de blocos/trechos de código) de `README.md`,
    `RELATORIO_UNICO.md`, `PLANO_PSF_IAMINY.md`, `COMO_RODAR.md` e de todo
    `conhecimento/*.md` -- prosa real já autoral deste projeto, nenhuma
    fonte nova."""
    return tuple(_limpar_codigo(caminho.read_text(encoding="utf-8")) for caminho in _caminhos_prosa_ampla())


def tokens_do_corpus_amplo(minimo_letras: int = 3) -> tuple[str, ...]:
    """`tokens_do_corpus()` (conhecimento_puro.py) mais a prosa autoral
    ampla (README/RELATORIO_UNICO/PLANO/COMO_RODAR/conhecimento/*.md).
    Tokens com menos de `minimo_letras` ficam de fora deste corpus amplo
    (ruído de variável de fórmula matemática solta, não palavra real --
    ver docstring do módulo); `tokens_do_corpus()` em si não é filtrado."""
    tokens = list(tokens_do_corpus())
    for frase in frases_da_prosa_autoral_ampla():
        for token in _tokenizador.tokenizar(frase):
            if token.tipo == TipoToken.PALAVRA and len(token.normalizado) >= minimo_letras:
                tokens.append(token.normalizado)
    return tuple(tokens)
