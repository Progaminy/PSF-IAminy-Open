"""Uso não-fundacional da Matemática no Português PSF.

O conhecimento linguístico continua em :mod:`lingua_portuguesa.conhecimento_puro`.
Este módulo não define o significado de som, palavra, frase ou texto. Ele usa
conhecimento matemático já construído pelo próprio PSF como ferramenta de:

- auditoria de relações e dependências;
- busca de caminhos mínimos no grafo conceitual;
- comparação por gramática formal finita;
- validação de reescritas e equivalências terminológicas;
- seleção explícita de alternativas por critério finito.

Uma gramática finita que não reconhece uma frase apenas declara ``não coberto``;
nunca declara, por esse motivo isolado, que a frase é inválida em português.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterable

from nucleo.gramaticas_finitas import (
    DERIVAVEL_EM_ATE_FINITO,
    GRAMATICA_FINITA,
    PRODUCAO_FINITA,
)
from nucleo.otimizacao_modelos_finitos import maximo_global
from nucleo.reescrita_provas_finitas import derivacao_valida, sequencia_reescrita
from nucleo.traducao import para_bool

from .conhecimento_puro import ConceitoPortugues, ConstrutorConhecimentoPortugues
from .tipos import AnaliseTexto, AnaliseToken, ClasseGramatical, LeituraMorfologica, TipoToken


@dataclass(frozen=True, slots=True)
class AuditoriaMatematicaPortugues:
    """Diagnóstico estrutural do conhecimento, sem alterar o conteúdo."""

    conceitos: int
    relacoes_diretas: int
    nomes_duplicados: tuple[str, ...]
    dependencias_ausentes: tuple[tuple[str, str], ...]
    dependencias_futuras: tuple[tuple[str, str], ...]
    ciclos: tuple[tuple[str, ...], ...]
    raizes: tuple[str, ...]
    folhas: tuple[str, ...]
    profundidade_maxima: int

    @property
    def aprovada(self) -> bool:
        return not (
            self.nomes_duplicados
            or self.dependencias_ausentes
            or self.dependencias_futuras
            or self.ciclos
        )


@dataclass(frozen=True, slots=True)
class ComparacaoGramaticalFinita:
    """Resultado limitado de uma gramática formal usada como comparador."""

    padrao: tuple[str, ...]
    coberto: bool
    limite_passos: int
    conclusao: str


@dataclass(frozen=True, slots=True)
class ProvaReescritaTerminologica:
    """Caminho auditável entre um termo alternativo e o termo canónico."""

    origem: str
    destino: str
    passos: tuple[str, ...]
    valida: bool


_CLASSE_PARA_SIMBOLO: dict[ClasseGramatical, str] = {
    ClasseGramatical.SUBSTANTIVO: "N",
    ClasseGramatical.ADJETIVO: "ADJ",
    ClasseGramatical.VERBO: "V",
    ClasseGramatical.ADVERBIO: "ADV",
    ClasseGramatical.PRONOME: "PRON",
    ClasseGramatical.DETERMINANTE: "DET",
    ClasseGramatical.PREPOSICAO: "PREP",
    ClasseGramatical.CONJUNCAO: "CONJ",
    ClasseGramatical.INTERJEICAO: "INTJ",
    ClasseGramatical.NUMERAL: "NUM",
    ClasseGramatical.DESCONHECIDA: "?",
}


def _gramatica_comparacao_portugues():
    """Pequena gramática formal de padrões já materializados.

    Ela cobre somente construções simples e explícitas. A gramática não é uma
    definição total do português e não substitui o analisador linguístico.
    """

    nao_terminais = ("O", "SN", "SV", "SP")
    terminais = tuple(dict.fromkeys(_CLASSE_PARA_SIMBOLO.values()))
    producoes = (
        PRODUCAO_FINITA("O", ("SN", "SV")),
        PRODUCAO_FINITA("O", ("SV",)),  # sujeito nulo/imperativo: apenas cobertura formal
        PRODUCAO_FINITA("O", ("INTJ",)),
        PRODUCAO_FINITA("SN", ("N",)),
        PRODUCAO_FINITA("SN", ("PRON",)),
        PRODUCAO_FINITA("SN", ("DET", "N")),
        PRODUCAO_FINITA("SN", ("DET", "ADJ", "N")),
        PRODUCAO_FINITA("SN", ("DET", "N", "ADJ")),
        PRODUCAO_FINITA("SN", ("NUM", "N")),
        PRODUCAO_FINITA("SN", ("DET", "NUM", "N")),
        PRODUCAO_FINITA("SP", ("PREP", "SN")),
        PRODUCAO_FINITA("SV", ("V",)),
        PRODUCAO_FINITA("SV", ("V", "ADV")),
        PRODUCAO_FINITA("SV", ("V", "ADJ")),
        PRODUCAO_FINITA("SV", ("V", "SN")),
        PRODUCAO_FINITA("SV", ("V", "SP")),
        PRODUCAO_FINITA("SV", ("V", "SN", "ADV")),
        PRODUCAO_FINITA("SV", ("V", "SN", "SP")),
    )
    return GRAMATICA_FINITA(nao_terminais, terminais, "O", producoes)


_GRAMATICA_COMPARACAO = _gramatica_comparacao_portugues()


class PonteMatematicaPortugues:
    """Aplica estruturas matemáticas sem contaminar o fundamento linguístico."""

    def __init__(self, conhecimento: ConstrutorConhecimentoPortugues | None = None) -> None:
        self.conhecimento = conhecimento or ConstrutorConhecimentoPortugues()

    def auditar_dependencias(self) -> AuditoriaMatematicaPortugues:
        conceitos = self.conhecimento.todos()
        por_nome = {conceito.nome: conceito for conceito in conceitos}
        ordens = {conceito.nome: conceito.ordem for conceito in conceitos}

        vistos: set[str] = set()
        duplicados: list[str] = []
        ausentes: list[tuple[str, str]] = []
        futuras: list[tuple[str, str]] = []
        dependentes: dict[str, list[str]] = {nome: [] for nome in por_nome}

        for conceito in conceitos:
            if conceito.nome in vistos and conceito.nome not in duplicados:
                duplicados.append(conceito.nome)
            vistos.add(conceito.nome)
            for dependencia in conceito.depende_de:
                if dependencia not in por_nome:
                    ausentes.append((conceito.nome, dependencia))
                    continue
                dependentes[dependencia].append(conceito.nome)
                if ordens[dependencia] >= conceito.ordem:
                    futuras.append((conceito.nome, dependencia))

        ciclos = self._detectar_ciclos(por_nome)
        raizes = tuple(c.nome for c in conceitos if not c.depende_de)
        folhas = tuple(c.nome for c in conceitos if not dependentes[c.nome])
        profundidade_maxima = max((self._profundidade(c.nome, por_nome, {}) for c in conceitos), default=0)

        return AuditoriaMatematicaPortugues(
            conceitos=len(conceitos),
            relacoes_diretas=sum(len(c.depende_de) for c in conceitos),
            nomes_duplicados=tuple(duplicados),
            dependencias_ausentes=tuple(ausentes),
            dependencias_futuras=tuple(futuras),
            ciclos=ciclos,
            raizes=raizes,
            folhas=folhas,
            profundidade_maxima=profundidade_maxima,
        )

    @staticmethod
    def _detectar_ciclos(por_nome: dict[str, ConceitoPortugues]) -> tuple[tuple[str, ...], ...]:
        estado: dict[str, int] = {nome: 0 for nome in por_nome}  # 0 novo, 1 aberto, 2 fechado
        pilha: list[str] = []
        ciclos: list[tuple[str, ...]] = []

        def visitar(nome: str) -> None:
            estado[nome] = 1
            pilha.append(nome)
            for dependencia in por_nome[nome].depende_de:
                if dependencia not in por_nome:
                    continue
                if estado[dependencia] == 0:
                    visitar(dependencia)
                elif estado[dependencia] == 1:
                    inicio = pilha.index(dependencia)
                    ciclo = tuple(pilha[inicio:] + [dependencia])
                    if ciclo not in ciclos:
                        ciclos.append(ciclo)
            pilha.pop()
            estado[nome] = 2

        for nome in por_nome:
            if estado[nome] == 0:
                visitar(nome)
        return tuple(ciclos)

    @classmethod
    def _profundidade(
        cls,
        nome: str,
        por_nome: dict[str, ConceitoPortugues],
        memo: dict[str, int],
    ) -> int:
        if nome in memo:
            return memo[nome]
        dependencias = tuple(d for d in por_nome[nome].depende_de if d in por_nome)
        valor = 1 if not dependencias else 1 + max(cls._profundidade(d, por_nome, memo) for d in dependencias)
        memo[nome] = valor
        return valor

    def caminho_minimo_ate(self, nome: str) -> tuple[str, ...]:
        """Menor cadeia de dependências desde uma raiz até o conceito."""
        alvo = self.conhecimento.buscar(nome)
        if alvo is None:
            return ()

        conceitos = self.conhecimento.todos()
        por_nome = {c.nome: c for c in conceitos}
        dependentes: dict[str, list[str]] = {c.nome: [] for c in conceitos}
        for conceito in conceitos:
            for dependencia in conceito.depende_de:
                if dependencia in dependentes:
                    dependentes[dependencia].append(conceito.nome)

        fila: deque[str] = deque(c.nome for c in conceitos if not c.depende_de)
        anterior: dict[str, str | None] = {raiz: None for raiz in fila}
        while fila:
            atual = fila.popleft()
            if atual == alvo.nome:
                break
            for proximo in dependentes[atual]:
                if proximo not in anterior:
                    anterior[proximo] = atual
                    fila.append(proximo)

        if alvo.nome not in anterior:
            return ()
        caminho: list[str] = []
        atual: str | None = alvo.nome
        while atual is not None:
            caminho.append(atual)
            atual = anterior[atual]
        caminho.reverse()
        return tuple(caminho)

    def conceitos_estruturais(self, limite: int = 10) -> tuple[tuple[str, int], ...]:
        """Conceitos com maior quantidade de dependentes diretos."""
        if limite < 1:
            return ()
        contagem = {c.nome: 0 for c in self.conhecimento.todos()}
        for conceito in self.conhecimento.todos():
            for dependencia in conceito.depende_de:
                if dependencia in contagem:
                    contagem[dependencia] += 1
        ordenados = sorted(contagem.items(), key=lambda item: (-item[1], item[0]))
        return tuple(ordenados[:limite])

    @staticmethod
    def melhor_leitura(analise: AnaliseToken) -> LeituraMorfologica:
        """Seleciona a leitura de maior confiança por otimização finita explícita."""
        if not analise.leituras:
            raise ValueError("análise sem leituras")
        melhor, _ = maximo_global(analise.leituras, lambda leitura: leitura.confianca)
        return melhor

    def padrao_morfologico(self, analise: AnaliseTexto) -> tuple[str, ...]:
        padrao: list[str] = []
        for item in analise.morfologia:
            if item.token.tipo in {TipoToken.PONTUACAO, TipoToken.SIMBOLO}:
                continue
            leitura = self.melhor_leitura(item)
            padrao.append(_CLASSE_PARA_SIMBOLO[leitura.classe])
        return tuple(padrao)

    def comparar_gramatica_finita(
        self,
        analise: AnaliseTexto,
        limite_passos: int = 12,
    ) -> ComparacaoGramaticalFinita:
        """Compara uma análise com uma gramática formal pequena.

        ``coberto=False`` nunca significa ``português inválido``. Significa apenas
        que o padrão está fora do catálogo formal atualmente construído.
        """
        padrao = self.padrao_morfologico(analise)
        coberto = bool(padrao) and "?" not in padrao and para_bool(
            DERIVAVEL_EM_ATE_FINITO(_GRAMATICA_COMPARACAO, padrao, limite_passos)
        )
        conclusao = (
            "Padrão coberto pela gramática finita de comparação."
            if coberto
            else "Padrão não coberto pela gramática finita atual; não é prova de erro linguístico."
        )
        return ComparacaoGramaticalFinita(padrao, coberto, limite_passos, conclusao)

    def provar_alias(self, termo: str) -> ProvaReescritaTerminologica:
        origem = str(termo).casefold().strip()
        aliases = {a.casefold(): b.casefold() for a, b in self.conhecimento.aliases().items()}
        destino = aliases.get(origem)
        if destino is None:
            canonico = self.conhecimento.buscar(origem)
            if canonico is None:
                return ProvaReescritaTerminologica(origem, "", (), False)
            return ProvaReescritaTerminologica(origem, canonico.nome, (origem,), True)

        regras = tuple((alias, alvo) for alias, alvo in aliases.items())
        sequencia = tuple(sequencia_reescrita(origem, regras, limite=len(regras) + 1))
        valida = derivacao_valida(origem, destino, regras, list(sequencia[1:]))
        return ProvaReescritaTerminologica(origem, destino, sequencia, valida)

    def validar_cadeia_de_dependencias(self, cadeia: Iterable[str]) -> bool:
        """Confirma que cada salto da cadeia é uma dependência real."""
        nomes = tuple(cadeia)
        if not nomes:
            return False
        for anterior, atual in zip(nomes, nomes[1:]):
            conceito = self.conhecimento.buscar(atual)
            if conceito is None or anterior not in conceito.depende_de:
                return False
        return True
