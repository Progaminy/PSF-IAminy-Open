"""Tipos do pipeline de corretor (Fase 6) -- específicos deste pipeline,
não do motor de português em geral, por isso não vivem em `tipos.py`.

Nota: `TipoErro` (a outra peça de tipo do plano de corretor) já foi
construída em `canal_ruidoso.py` na Fase 5, antes deste ficheiro existir
-- fica lá (é usada só por esse módulo), não duplicada aqui.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Candidato:
    """Uma palavra candidata a correção, com cada sinal componente
    guardado separadamente -- nunca reduzido a um único score opaco antes
    da hora. Um sinal ausente (`None`) significa "sem dado para este
    candidato", nunca um valor fabricado."""

    forma: str
    distancia_edicao: int | None = None
    similaridade_fonetica: float | None = None
    frequencia: float | None = None
    probabilidade_contexto: float | None = None
    proximidade_semantica: float | None = None
    peso_erro: float | None = None
    compatibilidade_gramatical: bool | None = None


@dataclass(frozen=True, slots=True)
class ResultadoCorrecao:
    """Resultado de `Corretor.corrigir_texto()` -- cada camada do pipeline
    (normalização, whitelist, parônimo, sugestão) fica visível
    separadamente, nunca colapsada num único texto sem explicação."""

    original: str
    normalizado: str
    corrigido: str
    sugestoes_ortografia: tuple[tuple[str, tuple[str, ...]], ...] = ()
    notas_paronimo: tuple[str, ...] = ()
    alteracoes_whitelist: tuple[tuple[str, str, str], ...] = ()
