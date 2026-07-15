"""Trie e árvore BK — índice para busca fuzzy sem scan linear.

Duas estruturas de dados clássicas, implementadas do zero (sem biblioteca
externa): `Trie` (prefixos) e `ArvoreBK` (busca por distância de edição,
usando a desigualdade triangular para podar ramos inteiros da árvore em vez
de comparar o alvo contra cada palavra do dicionário, um a um).

Nenhuma das duas é um modelo estatístico ou aprendido — são algoritmos de
indexação determinísticos, a mesma categoria de "primitiva PSF" que
`distancia_edicao.py`.
"""
from __future__ import annotations

from typing import Callable, Iterable

from .distancia_edicao import distancia_damerau_levenshtein

FuncaoDistancia = Callable[[str, str], int]


class Trie:
    """Árvore de prefixos simples (dict-de-dicts)."""

    _FIM = "$"

    def __init__(self) -> None:
        self._raiz: dict = {}

    def inserir(self, chave: str) -> None:
        no = self._raiz
        for caractere in chave:
            no = no.setdefault(caractere, {})
        no[self._FIM] = True

    def contem(self, chave: str) -> bool:
        no = self._raiz
        for caractere in chave:
            if caractere not in no:
                return False
            no = no[caractere]
        return self._FIM in no

    def prefixos(self, chave: str) -> tuple[str, ...]:
        """Todas as chaves inseridas que começam por `chave` (inclui a própria, se existir)."""
        no = self._raiz
        for caractere in chave:
            if caractere not in no:
                return ()
            no = no[caractere]
        encontrados: list[str] = []
        self._coletar(no, chave, encontrados)
        return tuple(sorted(encontrados))

    def _coletar(self, no: dict, prefixo: str, saida: list[str]) -> None:
        if self._FIM in no:
            saida.append(prefixo)
        for caractere, filho in no.items():
            if caractere == self._FIM:
                continue
            self._coletar(filho, prefixo + caractere, saida)


class _NoBK:
    __slots__ = ("chave", "filhos")

    def __init__(self, chave: str) -> None:
        self.chave = chave
        self.filhos: dict[int, "_NoBK"] = {}


class ArvoreBK:
    """Árvore BK (Burkhard-Keller) indexada por uma função de distância.

    Poda por desigualdade triangular: se a raiz de um ramo está a distância
    real `d` do alvo, qualquer palavra dentro desse ramo só pode estar a uma
    distância no intervalo [d - raio, d + raio] do alvo — ramos fora desse
    intervalo são descartados sem visitar nenhuma palavra dentro deles. Por
    isso a distância usada para decidir poda é sempre calculada sem corte
    (sem `limite`): um valor cortado subestimaria `d` e poderia excluir por
    engano um ramo que na verdade contém resultados válidos.
    """

    def __init__(self, distancia: FuncaoDistancia = distancia_damerau_levenshtein) -> None:
        self._distancia = distancia
        self._raiz: _NoBK | None = None

    @classmethod
    def construir(
        cls,
        chaves: Iterable[str],
        distancia: FuncaoDistancia = distancia_damerau_levenshtein,
    ) -> "ArvoreBK":
        arvore = cls(distancia)
        for chave in chaves:
            arvore.inserir(chave)
        return arvore

    def inserir(self, chave: str) -> None:
        if self._raiz is None:
            self._raiz = _NoBK(chave)
            return
        no = self._raiz
        while True:
            d = self._distancia(chave, no.chave)
            if d == 0:
                return  # já indexada, nada a fazer
            filho = no.filhos.get(d)
            if filho is None:
                no.filhos[d] = _NoBK(chave)
                return
            no = filho

    def buscar(self, alvo: str, raio: int) -> tuple[str, ...]:
        """Todas as chaves indexadas a distância <= raio de `alvo`."""
        if self._raiz is None:
            return ()
        encontrados: list[str] = []
        pilha = [self._raiz]
        while pilha:
            no = pilha.pop()
            d = self._distancia(alvo, no.chave)
            if d <= raio:
                encontrados.append(no.chave)
            for distancia_filho, filho in no.filhos.items():
                if d - raio <= distancia_filho <= d + raio:
                    pilha.append(filho)
        return tuple(encontrados)
