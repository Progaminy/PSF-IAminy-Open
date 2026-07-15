# -*- coding: utf-8 -*-
"""Tipos públicos do Chat Vivo PSF."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True, slots=True)
class RegistroCanonico:
    dados: dict[str, Any]
    tokens: frozenset[str]

    @property
    def id(self) -> str:
        return str(self.dados.get("id", "SEM-ID"))

    @property
    def titulo(self) -> str:
        return str(self.dados.get("titulo", self.id))

    @property
    def origem(self) -> str:
        return str(self.dados.get("etapa_origem", "base canônica"))


@dataclass(slots=True)
class RespostaChat:
    texto: str
    intencao: str
    tom: str
    confianca: int
    origem: str = "chat_vivo"
    conhecimento_encontrado: bool = False
    lacunas: list[str] = field(default_factory=list)
    fallback_usado: bool = False
    deve_melhorar: bool = False
    estado_psf: dict | None = None
    contexto_dialogo: dict | None = None
    contexto_chat: dict | None = None
    auditoria: dict[str, Any] = field(default_factory=dict)

    def como_dict(self) -> dict[str, Any]:
        return {
            "texto": self.texto,
            "intencao": self.intencao,
            "tom": self.tom,
            "confianca": self.confianca,
            "origem": self.origem,
            "conhecimento_encontrado": self.conhecimento_encontrado,
            "lacunas": list(self.lacunas),
            "fallback_usado": self.fallback_usado,
            "deve_melhorar": self.deve_melhorar,
            "estado_psf": self.estado_psf,
            "contexto_dialogo": self.contexto_dialogo,
            "contexto_chat": self.contexto_chat,
            "auditoria": dict(self.auditoria),
        }
