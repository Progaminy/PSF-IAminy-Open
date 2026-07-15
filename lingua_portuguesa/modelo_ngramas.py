"""Modelo de bigrama sobre o corpus interno -- Fase 5.1 do plano de
corretor (técnica 6: "usa contexto, palavras vizinhas").

Contagem pura + suavização aditiva de Laplace, sem nenhuma biblioteca
estatística -- aritmética explícita e verificável à mão, não um modelo
treinado no sentido estatístico. A fonte de treino é injetável (`tokens`,
por omissão `corpus_interno.tokens_do_corpus()`) para poder retreinar
depois com um corpus maior sem mudar quem chama.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field

from .corpus_interno import tokens_do_corpus


@dataclass
class ModeloNGrama:
    tokens: tuple[str, ...] = field(default_factory=tokens_do_corpus)
    suavizacao: float = 1.0
    _unigramas: Counter = field(init=False, repr=False)
    _bigramas: Counter = field(init=False, repr=False)
    _vocabulario: frozenset = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._unigramas = Counter(self.tokens)
        self._bigramas = Counter(zip(self.tokens, self.tokens[1:]))
        self._vocabulario = frozenset(self._unigramas)

    def contagem_unigrama(self, palavra: str) -> int:
        return self._unigramas.get(palavra, 0)

    def contagem_bigrama(self, anterior: str, palavra: str) -> int:
        return self._bigramas.get((anterior, palavra), 0)

    def probabilidade_condicional(self, palavra: str, anterior: str | None = None) -> float:
        """P(palavra | anterior) com suavização aditiva de Laplace. Se
        `anterior` for `None`, devolve a probabilidade unigrama simples
        (frequência relativa suavizada)."""
        tamanho_vocabulario = len(self._vocabulario) or 1
        if anterior is None:
            total = sum(self._unigramas.values())
            return (self.contagem_unigrama(palavra) + self.suavizacao) / (
                total + self.suavizacao * tamanho_vocabulario
            )
        contagem_anterior = self.contagem_unigrama(anterior)
        return (self.contagem_bigrama(anterior, palavra) + self.suavizacao) / (
            contagem_anterior + self.suavizacao * tamanho_vocabulario
        )

    def escolher_por_contexto(self, candidatos: tuple[str, ...], anterior: str | None = None) -> str:
        """Candidato com maior probabilidade condicional dada a palavra
        anterior (ou frequência unigrama simples se `anterior` for `None`)."""
        return max(candidatos, key=lambda candidato: self.probabilidade_condicional(candidato, anterior))
