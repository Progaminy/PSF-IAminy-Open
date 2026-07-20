"""Reconstrução local de formas verbais regulares para o corretor.

O recurso empacotado guarda apenas infinitivos revistos. As formas são
reconstruídas por regras neste módulo, sem rede, pacote linguístico, arquivo do
sistema ou dicionário importado. A camada é somente ortográfica: não inventa
definição nem análise morfológica para aumentar a contagem.
"""
from __future__ import annotations

import json
from functools import lru_cache
from importlib.resources import files

from .lexico_expansao import _corrigir_ortografia_raiz
from .normalizacao import normalizar_chave


_ORIGEM_ESPERADA = "curadoria_autoral_local_sem_fonte_externa"
_TERMINACOES_NAO_MECANICAS = (
    "ear", "iar", "guar", "quar", "aizar", "uizar", "iudar", "iuvar",
)
_LEMAS_IRREGULARES_CONHECIDOS = frozenset({"dar", "estar", "saudar"})


def _formas_por_sufixo(infinitivo: str) -> set[str]:
    raiz = infinitivo[:-2]
    conjugacao = infinitivo[-2:]

    if conjugacao != "ar":  # protegido também pela validação do manifesto
        raise ValueError(f"conjugação não suportada: {infinitivo!r}")
    grupos = (
        ("o", "as", "a", "amos", "ais", "am"),
        ("ei", "aste", "ou", "amos", "astes", "aram"),
        ("ava", "avas", "ava", "ávamos", "áveis", "avam"),
        ("ara", "aras", "ara", "áramos", "áreis", "aram"),
        ("e", "es", "e", "emos", "eis", "em"),
        ("asse", "asses", "asse", "ássemos", "ásseis", "assem"),
        ("ar", "ares", "ar", "armos", "ardes", "arem"),
    )
    gerundio = "ando"
    participio = "ado"
    imperativo_vos = "ai"
    variante_preterito_nos = "ámos"

    formas = {infinitivo, raiz + gerundio, raiz + imperativo_vos}
    formas.update({
        raiz + participio,
        raiz + participio + "s",
        raiz + participio[:-1] + "a",
        raiz + participio[:-1] + "as",
    })
    formas.add(raiz + variante_preterito_nos)
    for grupo in grupos:
        formas.update(raiz + sufixo for sufixo in grupo)

    # Futuro do presente e condicional usam o infinitivo inteiro.
    formas.update(infinitivo + sufixo for sufixo in ("ei", "ás", "á", "emos", "eis", "ão"))
    formas.update(infinitivo + sufixo for sufixo in ("ia", "ias", "íamos", "íeis", "iam"))

    corrigidas = _corrigir_ortografia_raiz(
        {forma: None for forma in formas}, raiz, infinitivo
    )
    return set(corrigidas)


def formas_do_paradigma_regular(infinitivo: str) -> tuple[str, ...]:
    """Devolve formas simples seguras da primeira conjugação regular."""
    lema = normalizar_chave(infinitivo)
    if lema != infinitivo or not lema.isalpha() or not lema.endswith("ar"):
        raise ValueError(f"infinitivo regular inválido: {infinitivo!r}")
    if lema in _LEMAS_IRREGULARES_CONHECIDOS or lema.endswith(_TERMINACOES_NAO_MECANICAS):
        raise ValueError(f"infinitivo fora do paradigma mecânico seguro: {infinitivo!r}")
    return tuple(sorted(_formas_por_sufixo(lema)))


@lru_cache(maxsize=1)
def lemas_regulares_curados() -> tuple[str, ...]:
    """Lê o inventário de infinitivos empacotado no próprio projeto."""
    caminho = files("lingua_portuguesa.dados").joinpath("verbos_regulares_curados.json")
    with caminho.open("r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    if dados.get("versao") != 1 or dados.get("origem") != _ORIGEM_ESPERADA:
        raise ValueError("manifesto local de verbos sem versão/origem reconhecida")
    lemas = tuple(dados.get("verbos", ()))
    if lemas != tuple(sorted(set(lemas))):
        raise ValueError("verbos locais devem estar ordenados e sem repetição")
    for lema in lemas:
        formas_do_paradigma_regular(lema)
    return lemas


@lru_cache(maxsize=1)
def formas_verbais_regulares_locais() -> tuple[str, ...]:
    """União determinística das formas reconstruídas dos lemas curados."""
    formas: set[str] = set()
    for lema in lemas_regulares_curados():
        formas.update(formas_do_paradigma_regular(lema))
    return tuple(sorted(formas))
