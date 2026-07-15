"""Tipos do motor de ensino do PSF-IAminy."""
from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


class FormatoAula(IntEnum):
    CURTA = 1
    EXPLICADA = 2
    COM_EXEMPLO = 3
    COM_EXERCICIOS = 4
    DESMONTADA = 5

    @classmethod
    def de(cls, valor: int | str | "FormatoAula") -> "FormatoAula":
        if isinstance(valor, cls):
            return valor
        if isinstance(valor, int):
            return cls(valor)
        texto = valor.strip().casefold()
        aliases = {
            "1": cls.CURTA,
            "curta": cls.CURTA,
            "curto": cls.CURTA,
            "2": cls.EXPLICADA,
            "explicada": cls.EXPLICADA,
            "explicacao": cls.EXPLICADA,
            "explicação": cls.EXPLICADA,
            "3": cls.COM_EXEMPLO,
            "exemplo": cls.COM_EXEMPLO,
            "com_exemplo": cls.COM_EXEMPLO,
            "4": cls.COM_EXERCICIOS,
            "exercicios": cls.COM_EXERCICIOS,
            "exercícios": cls.COM_EXERCICIOS,
            "com_exercicios": cls.COM_EXERCICIOS,
            "5": cls.DESMONTADA,
            "detalhada": cls.DESMONTADA,
            "desmontada": cls.DESMONTADA,
        }
        if texto not in aliases:
            raise ValueError(f"formato de aula desconhecido: {valor!r}")
        return aliases[texto]


@dataclass(frozen=True, slots=True)
class PacoteConhecimento:
    codigo: str
    area: str
    nivel: int
    titulo: str
    objetivo: str
    pre_requisitos: tuple[str, ...]
    palavras_chave: tuple[str, ...]
    passos: tuple[str, ...]
    explicacao: str
    exemplos: tuple[str, ...]
    exercicios: tuple[str, ...]
    desmontagem: tuple[str, ...]
    melhorias: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class AulaPacote:
    pacote: PacoteConhecimento
    formato: FormatoAula
    linhas: tuple[str, ...]

    @property
    def texto(self) -> str:
        return "\n".join(self.linhas)
