"""Tipos públicos do motor matemático PSF.

São estruturas de transporte. Não constituem conhecimento matemático por si.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConceitoMatematico:
    nome: str
    construcao: str
    dependencias_declaradas: tuple[str, ...]
    implementacoes: tuple[str, ...]
    testes: tuple[str, ...]
    arquivo: str
    marcador_historico: int | None = None
    exemplos_minimos: tuple[str, ...] = ()

    @property
    def eh_conhecimento_psf(self) -> bool:
        """Sem dependências de entrada, o item é material, não conhecimento."""
        return bool(self.dependencias_declaradas and self.construcao.strip())


@dataclass(frozen=True, slots=True)
class PassoMatematico:
    ordem: int
    operacao: str
    entrada: str
    saida: str
    justificacao: str


@dataclass(frozen=True, slots=True)
class ResolucaoMatematica:
    problema: str
    estado: str
    resultado: str | None
    passos: tuple[PassoMatematico, ...]
    conhecimento_usado: tuple[str, ...]
    limites: tuple[str, ...] = ()
    resultado_exato: str | None = None
    aproximacao: str | None = None
    casas_decimais: int | None = None
    modo_aproximacao: str | None = None
    referencia_convencional: tuple[str, ...] = ()
    investigacao: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class ReconstrucaoMatematica:
    conceito: ConceitoMatematico | None
    estado: str
    trilho_documental: tuple[str, ...]
    explicacao: tuple[str, ...]
    limites: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class MonografiaPSF:
    titulo: str
    estado: str
    texto_markdown: str
    conceitos_usados: tuple[str, ...]
    lacunas: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ProvaFinita:
    estado: str
    premissas: tuple[object, ...]
    conclusao: object
    passos: tuple[object, ...]
    valida: bool
    limite: str


@dataclass(frozen=True, slots=True)
class AuditoriaMatematica:
    conceitos: int
    nomes_duplicados: tuple[str, ...]
    referencias_de_implementacao_ausentes: tuple[str, ...]
    referencias_de_teste_ausentes: tuple[str, ...]
    marcadores_historicos_repetidos: tuple[int, ...]
    linha_unica: bool
    observacoes: tuple[str, ...]
