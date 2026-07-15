"""Normalização mecânica de texto corrido: espaçamento, maiúscula de
início de frase, pontuação final ausente, parágrafo.

Fase 1-B do plano de corretor: o autor pediu poder colar "uma palavra,
texto ou mesmo livro" e receber de volta com "vírgula no lugar, pontos,
espaço, indentação, letras maiúsculas". O que este módulo faz é
deliberadamente limitado ao que é **mecanicamente decidível sem adivinhar
intenção**:

- espaço correto ao redor de pontuação já existente;
- maiúscula no início de cada frase já delimitada por `.`/`!`/`?`/`…`;
- ponto final no fim do texto, se faltar;
- separador de parágrafo consistente (uma linha em branco, nunca mais).

O que este módulo **não** faz, de propósito: inserir vírgula ou ponto no
meio de um texto que não tem pontuação nenhuma. Isso exigiria julgamento
sintático/semântico real sobre onde termina uma oração — o motor de
gramática (`gramatica.py`) ainda não tem essa maturidade (só concordância
determinante/nome e nome/adjetivo; concordância verbal é a Fase 2 deste
plano). Fingir esse julgamento seria inventar pontuação, não corrigi-la;
fica registado como fronteira aberta, não como capacidade escondida.

Capitalização de nomes próprios também fica fora: exigiria uma lista real
de nomes próprios que o projeto não tem — capitalizar por adivinhação
seria o mesmo tipo de erro.
"""
from __future__ import annotations

import re

from .tokenizacao import Tokenizador

_FECHAMENTO = frozenset(",.;:!?…)]}»")
_ABERTURA = frozenset("([{«")
_FIM_DE_FRASE = re.compile(r"[.!?…]+")
_ABERTURA_PRECEDENTE = frozenset("\"'«([{")

_tokenizador = Tokenizador()


def normalizar_espacos_pontuacao(texto: str) -> str:
    """Sem espaço antes de `,.;:!?…)]}»`; exatamente um espaço depois
    (exceto fim de texto ou antes de outra pontuação de fechamento); sem
    espaço depois de `([{«`. Quebras de linha na lacuna original nunca são
    tocadas — preserva separação de parágrafo, que é assunto de
    `normalizar_paragrafos`, não desta função.
    """
    tokens = _tokenizador.tokenizar(texto)
    if not tokens:
        return texto
    partes: list[str] = [texto[: tokens[0].inicio]]
    total = len(tokens)
    for indice, token in enumerate(tokens):
        partes.append(token.texto)
        if indice + 1 >= total:
            partes.append(texto[token.fim :])
            break
        proximo = tokens[indice + 1]
        lacuna_original = texto[token.fim : proximo.inicio]
        if "\n" in lacuna_original:
            partes.append(lacuna_original)
            continue
        if proximo.texto in _FECHAMENTO:
            partes.append("")
        elif token.texto in _ABERTURA:
            partes.append("")
        elif token.texto in _FECHAMENTO:
            partes.append(" ")
        elif proximo.texto in _ABERTURA:
            partes.append(" ")
        elif lacuna_original:
            partes.append(" ")
        else:
            partes.append("")
    return "".join(partes)


def _capitalizar_primeira_letra(segmento: str) -> str:
    indice = 0
    while indice < len(segmento) and (
        segmento[indice].isspace() or segmento[indice] in _ABERTURA_PRECEDENTE
    ):
        indice += 1
    if indice < len(segmento) and segmento[indice].isalpha():
        return segmento[:indice] + segmento[indice].upper() + segmento[indice + 1 :]
    return segmento


def capitalizar_inicio_de_frases(texto: str) -> str:
    """Maiúscula na primeira letra do texto e após cada `.`/`!`/`?`/`…`.

    Só atua onde a pontuação de fim de frase já existe — não inventa
    limite de frase novo (ver limite de escopo no docstring do módulo).
    """
    if not texto:
        return texto
    partes = _FIM_DE_FRASE.split(texto)
    delimitadores = _FIM_DE_FRASE.findall(texto)
    resultado: list[str] = []
    deve_capitalizar = True
    for indice, parte in enumerate(partes):
        if deve_capitalizar:
            parte = _capitalizar_primeira_letra(parte)
            if parte.strip():
                deve_capitalizar = False
        resultado.append(parte)
        if indice < len(delimitadores):
            resultado.append(delimitadores[indice])
            deve_capitalizar = True
    return "".join(resultado)


def garantir_pontuacao_final(texto: str) -> str:
    """Acrescenta `.` ao final do texto se não terminar em `./!/…/?`.

    Extensão direta do padrão já real de
    `lingua_portuguesa/motor.py::MotorPortugues.produzir_texto` (que já faz
    isto por unidade gerada internamente) para texto arbitrário de entrada.
    """
    aparado = texto.rstrip()
    if not aparado or aparado[-1] in ".!?…":
        return texto
    sufixo = texto[len(aparado) :]
    return aparado + "." + sufixo


_QUEBRA_MULTIPLA = re.compile(r"\n[ \t]*\n(?:[ \t]*\n)*")
_ESPACO_ANTES_DE_QUEBRA = re.compile(r"[ \t]+\n")


def normalizar_paragrafos(texto: str) -> str:
    """Separador de parágrafo consistente: uma linha em branco, nunca mais.
    Também apara espaço em branco nas duas pontas do texto inteiro (mas
    nunca no meio) — mecânico e seguro, sem exigir julgamento nenhum.

    Estende o padrão já real de
    `ensino/leitura_documentos.py::_LINHAS_VAZIAS` (que colapsa linhas
    vazias múltiplas) para qualquer texto de entrada, não só extração de
    `.docx`.
    """
    normalizado = texto.replace("\r\n", "\n").replace("\r", "\n")
    normalizado = _ESPACO_ANTES_DE_QUEBRA.sub("\n", normalizado)
    normalizado = _QUEBRA_MULTIPLA.sub("\n\n", normalizado)
    return normalizado.strip()


def normalizar_texto_corrido(texto: str) -> str:
    """Aplica as quatro normalizações mecânicas da Fase 1-B, em ordem.

    Ponto de entrada único para o resto do pipeline (Fase 1-C liga isto ao
    chat). Nunca insere pontuação que exigiria julgamento sintático não
    construído ainda — ver limite de escopo no docstring do módulo.
    """
    texto = normalizar_espacos_pontuacao(texto)
    texto = capitalizar_inicio_de_frases(texto)
    texto = garantir_pontuacao_final(texto)
    texto = normalizar_paragrafos(texto)
    return texto
