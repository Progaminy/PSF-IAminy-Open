"""Dicionário extensível e persistência lexical em JSON."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from importlib.resources import files
from pathlib import Path
from typing import Iterable

from .normalizacao import normalizar_chave, sem_acentos
from .tipos import ClasseGramatical, EntradaLexical, Genero, Numero, Pessoa
from .lexico_expansao import entradas_expandidas
from .distancia_edicao import distancia_damerau_levenshtein

# O JSON codifica pessoa gramatical como inteiro (1/2/3), convenção própria
# dos dados de origem -- os outros traços (`Genero`/`Numero`) já são
# strings descritivas, então `Pessoa` segue o mesmo estilo internamente e
# esta tabela faz a ponte entre os dois formatos.
_MAPA_PESSOA_JSON: dict[int, Pessoa] = {1: Pessoa.PRIMEIRA, 2: Pessoa.SEGUNDA, 3: Pessoa.TERCEIRA}
META_FORMAS_ATOMICAS_CORRETOR = 600_000
_DIRETORIO_DADOS_LOCAL = Path(__file__).resolve().parent / "dados"


class Dicionario:
    """Índice lexical que admite várias leituras para a mesma forma."""

    def __init__(self, entradas: Iterable[EntradaLexical] = ()) -> None:
        self._indice: dict[str, list[EntradaLexical]] = defaultdict(list)
        self._formas_ortograficas: set[str] = set()
        self._origens_ortograficas: dict[str, str] = {}
        self._cache_fuzzy: tuple[dict[int, tuple[str, ...]], dict[str, tuple[str, ...]]] | None = None
        for entrada in entradas:
            self.adicionar(entrada)

    @classmethod
    def padrao(cls) -> "Dicionario":
        caminho = files("lingua_portuguesa.dados").joinpath("lexico_base.json")
        with caminho.open("r", encoding="utf-8") as arquivo:
            dicionario = cls._de_dados(json.load(arquivo))
        caminho_local = files("lingua_portuguesa.dados").joinpath("lexico_validado_local.json")
        with caminho_local.open("r", encoding="utf-8") as arquivo:
            for entradas in cls._de_dados(json.load(arquivo))._indice.values():
                for entrada in entradas:
                    dicionario.adicionar(entrada)
        for entrada in entradas_expandidas():
            dicionario.adicionar(entrada)
        from .lexico_verbos_regulares import (
            formas_do_paradigma_regular,
            lemas_regulares_curados,
        )

        for lema in lemas_regulares_curados():
            for forma in formas_do_paradigma_regular(lema):
                dicionario.adicionar_forma_ortografica(
                    forma, f"paradigma_verbal_regular_curado_local:{lema}"
                )
        return dicionario

    @classmethod
    def de_json(cls, caminho: str | Path) -> "Dicionario":
        """Carrega somente JSON pertencente aos dados locais do pacote."""
        try:
            resolvido = Path(caminho).resolve(strict=True)
            resolvido.relative_to(_DIRETORIO_DADOS_LOCAL.resolve(strict=True))
        except (FileNotFoundError, OSError, ValueError) as erro:
            raise ValueError("o léxico só aceita fontes em lingua_portuguesa/dados") from erro
        if not resolvido.is_file():
            raise ValueError("fonte lexical local deve ser um arquivo")
        with resolvido.open("r", encoding="utf-8") as arquivo:
            return cls._de_dados(json.load(arquivo))

    @classmethod
    def _de_dados(cls, dados: list[dict]) -> "Dicionario":
        entradas: list[EntradaLexical] = []
        for item in dados:
            classe = ClasseGramatical(item["classe"])
            definicoes = tuple(item.get("definicoes", ()))
            lema = item["lema"]
            for forma, atributos in item.get("formas", {lema: {}}).items():
                extras = {
                    chave: valor
                    for chave, valor in atributos.items()
                    if chave not in {"genero", "numero", "pessoa"}
                }
                entradas.append(
                    EntradaLexical(
                        lema=lema,
                        forma=forma,
                        classe=classe,
                        definicoes=definicoes,
                        genero=Genero(atributos["genero"]) if atributos.get("genero") else None,
                        numero=Numero(atributos["numero"]) if atributos.get("numero") else None,
                        pessoa=_MAPA_PESSOA_JSON.get(atributos.get("pessoa")),
                        atributos=extras,
                    )
                )
        return cls(entradas)

    def adicionar(self, entrada: EntradaLexical) -> None:
        chave = normalizar_chave(entrada.forma)
        nova_chave = chave not in self._indice
        if entrada not in self._indice[chave]:
            self._indice[chave].append(entrada)
            if nova_chave:
                self._cache_fuzzy = None

    def adicionar_forma_ortografica(self, forma: str, origem: str) -> None:
        """Reconhece grafia comprovada sem inventar análise ou definição."""
        chave = normalizar_chave(forma)
        if not chave:
            raise ValueError("forma ortográfica não pode ser vazia")
        if chave not in self._indice and chave not in self._formas_ortograficas:
            self._cache_fuzzy = None
        self._formas_ortograficas.add(chave)
        self._origens_ortograficas.setdefault(chave, origem)

    def origem_ortografica(self, forma: str) -> str | None:
        return self._origens_ortograficas.get(normalizar_chave(forma))

    def buscar(self, forma: str) -> tuple[EntradaLexical, ...]:
        return tuple(self._indice.get(normalizar_chave(forma), ()))

    def definir(self, forma: str) -> tuple[str, ...]:
        definicoes: list[str] = []
        for entrada in self.buscar(forma):
            for definicao in entrada.definicoes:
                if definicao not in definicoes:
                    definicoes.append(definicao)
        return tuple(definicoes)

    def sugerir(self, forma: str, limite: int = 5) -> tuple[str, ...]:
        """Sugestões por distância de edição, indexadas por comprimento.

        Damerau-Levenshtein restrita não satisfaz a desigualdade triangular
        necessária à poda de uma árvore BK em todos os casos. O índice por
        comprimento é simples e exato: uma forma a distância ``r`` só pode
        ter comprimento entre ``len(alvo)-r`` e ``len(alvo)+r``.
        """
        if limite < 1:
            return ()
        alvo = sem_acentos(forma)
        distancia_maxima = 1 if len(alvo) <= 5 else 2
        por_comprimento, mapa = self._indice_fuzzy()
        candidatos: list[tuple[int, str]] = []
        minimo = max(0, len(alvo) - distancia_maxima)
        maximo = len(alvo) + distancia_maxima
        for comprimento in range(minimo, maximo + 1):
            for chave_sem_acentos in por_comprimento.get(comprimento, ()):
                distancia = distancia_damerau_levenshtein(
                    alvo, chave_sem_acentos, distancia_maxima
                )
                if distancia <= distancia_maxima:
                    for chave_original in mapa[chave_sem_acentos]:
                        candidatos.append((distancia, chave_original))
        candidatos.sort(key=lambda item: (item[0], len(item[1]), item[1]))
        return tuple(chave for _, chave in candidatos[:limite])

    def _indice_fuzzy(self) -> tuple[dict[int, tuple[str, ...]], dict[str, tuple[str, ...]]]:
        if self._cache_fuzzy is None:
            mapa: dict[str, list[str]] = defaultdict(list)
            for chave in self.chaves():
                mapa[sem_acentos(chave)].append(chave)
            por_comprimento: dict[int, list[str]] = defaultdict(list)
            for chave_sem_acentos in mapa:
                por_comprimento[len(chave_sem_acentos)].append(chave_sem_acentos)
            self._cache_fuzzy = (
                {tamanho: tuple(chaves) for tamanho, chaves in por_comprimento.items()},
                {chave: tuple(originais) for chave, originais in mapa.items()},
            )
        return self._cache_fuzzy

    def __contains__(self, forma: str) -> bool:
        chave = normalizar_chave(forma)
        return chave in self._indice or chave in self._formas_ortograficas

    def lemas(self) -> tuple[str, ...]:
        """Lista estável dos lemas conhecidos, sem repetir flexões."""
        vistos: set[str] = set()
        for entradas in self._indice.values():
            for entrada in entradas:
                vistos.add(entrada.lema)
        return tuple(sorted(vistos))

    def chaves(self) -> tuple[str, ...]:
        """Lista estável de todas as formas (chaves) indexadas."""
        return tuple(sorted(set(self._indice) | self._formas_ortograficas))

    def palavras_com_letras(
        self,
        letras: str,
        *,
        comprimento_minimo: int = 1,
        usar_todas: bool = False,
    ) -> tuple[str, ...]:
        """Formas do dicionário que podem ser construídas com ``letras``.

        Cada letra fornecida só pode ser usada tantas vezes quanto aparece.
        A comparação ignora acentos e cedilha apenas para encaixar a forma no
        alfabeto-base: ``acao`` pode, por exemplo, encontrar ``ação``. O
        resultado conserva a ortografia cadastrada no dicionário.

        Quando ``usar_todas`` é verdadeiro, devolve somente anagramas que
        consomem todas as letras. Caso contrário, inclui palavras formadas por
        subconjuntos delas. Nunca cria uma sequência fora do dicionário.
        """
        if not isinstance(letras, str):
            raise TypeError("letras deve ser uma string")
        if comprimento_minimo < 1:
            raise ValueError("comprimento_minimo deve ser pelo menos 1")

        letras_base = sem_acentos(letras)
        if not letras_base or any(letra not in "abcdefghijklmnopqrstuvwxyz" for letra in letras_base):
            raise ValueError("letras deve conter somente letras de a a z, com ou sem acento")

        disponiveis = Counter(letras_base)
        quantidade = len(letras_base)
        encontradas: list[str] = []
        for forma in self.chaves():
            forma_base = sem_acentos(forma)
            if not forma_base.isalpha() or len(forma_base) < comprimento_minimo:
                continue
            if usar_todas and len(forma_base) != quantidade:
                continue
            if len(forma_base) > quantidade:
                continue
            necessarias = Counter(forma_base)
            if all(total <= disponiveis[letra] for letra, total in necessarias.items()):
                encontradas.append(forma)
        return tuple(encontradas)

    def total_formas(self) -> int:
        """Quantidade de formas lexicais indexadas."""
        return len(set(self._indice) | self._formas_ortograficas)

    def total_formas_atomicas(self) -> int:
        """Quantidade real de chaves sem espaço (palavras, não expressões)."""
        return sum(" " not in forma for forma in self.chaves())

    def total_formas_atomicas_com_leitura(self) -> int:
        """Formas atômicas que possuem ao menos uma entrada lexical."""
        return sum(" " not in forma for forma in self._indice)

    def total_formas_atomicas_apenas_ortograficas(self) -> int:
        """Grafias atômicas aceitas sem análise semântica inventada."""
        return sum(
            " " not in forma
            for forma in self._formas_ortograficas.difference(self._indice)
        )

    def total_expressoes_multipalavra(self) -> int:
        """Quantidade de chaves com espaço, separada da meta do corretor."""
        return sum(" " in forma for forma in self.chaves())

    def cobertura_atomica(self, meta: int = META_FORMAS_ATOMICAS_CORRETOR) -> float:
        """Percentagem medida sobre uma meta explícita de formas atômicas."""
        if meta <= 0:
            raise ValueError("meta deve ser positiva")
        return self.total_formas_atomicas() * 100 / meta

    def __len__(self) -> int:
        return sum(len(entradas) for entradas in self._indice.values())
