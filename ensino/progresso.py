"""Progresso do aluno por pacote do PSF-IAminy.

Antes, `MotorAulas.proximo` só recebia uma lista solta de códigos
"concluídos" que o chamador tinha que montar e lembrar sozinho — não havia
lugar nenhum que guardasse se uma pessoa realmente viu, entendeu ou
praticou um pacote. Este módulo fecha essa lacuna: por pessoa e por área,
cada pacote sobe uma escada de três estágios (visto -> entendido ->
praticado) e o estado pode ser mantido só em memória ou persistido em JSON.
"""
from __future__ import annotations

import json
from enum import IntEnum
from pathlib import Path


class EstadoPacote(IntEnum):
    VISTO = 1
    ENTENDIDO = 2
    PRATICADO = 3

    @classmethod
    def de(cls, valor: "int | str | EstadoPacote") -> "EstadoPacote":
        if isinstance(valor, cls):
            return valor
        if isinstance(valor, int):
            return cls(valor)
        texto = valor.strip().casefold()
        aliases = {
            "1": cls.VISTO,
            "visto": cls.VISTO,
            "2": cls.ENTENDIDO,
            "entendido": cls.ENTENDIDO,
            "3": cls.PRATICADO,
            "praticado": cls.PRATICADO,
        }
        if texto not in aliases:
            raise ValueError(f"estado de pacote desconhecido: {valor!r}")
        return aliases[texto]


class RegistroProgresso:
    """Progresso de pessoas por área e pacote.

    Sem `caminho`, o registro vive só em memória (uma sessão, ou testes).
    Com `caminho`, cada marcação é lida/gravada em JSON, para o progresso
    sobreviver entre execuções.
    """

    def __init__(self, caminho: "Path | str | None" = None) -> None:
        self._caminho = Path(caminho) if caminho is not None else None
        self._dados: dict[str, dict[str, dict[str, int]]] = self._carregar()

    def _carregar(self) -> dict:
        if self._caminho is not None and self._caminho.exists():
            return json.loads(self._caminho.read_text(encoding="utf-8"))
        return {}

    def _guardar(self) -> None:
        if self._caminho is not None:
            self._caminho.write_text(
                json.dumps(self._dados, indent=2, sort_keys=True, ensure_ascii=False),
                encoding="utf-8",
            )

    def marcar(
        self,
        aluno: str,
        area: str,
        codigo: str,
        estado: "int | str | EstadoPacote",
    ) -> EstadoPacote:
        novo = EstadoPacote.de(estado)
        pacotes = self._dados.setdefault(aluno, {}).setdefault(area, {})
        codigo = codigo.upper()
        atual = pacotes.get(codigo)
        # a escada visto -> entendido -> praticado não regride: marcar um
        # estágio já ultrapassado não apaga o mais avançado que existia.
        if atual is None or novo > atual:
            pacotes[codigo] = int(novo)
        else:
            novo = EstadoPacote(atual)
        self._guardar()
        return novo

    def estado(self, aluno: str, area: str, codigo: str) -> "EstadoPacote | None":
        valor = self._dados.get(aluno, {}).get(area, {}).get(codigo.upper())
        return EstadoPacote(valor) if valor is not None else None

    def concluidos(
        self,
        aluno: str,
        area: str,
        minimo: "int | str | EstadoPacote" = EstadoPacote.PRATICADO,
    ) -> tuple[str, ...]:
        limiar = EstadoPacote.de(minimo)
        pacotes = self._dados.get(aluno, {}).get(area, {})
        return tuple(codigo for codigo, valor in pacotes.items() if valor >= limiar)

    def resumo(self, aluno: str, area: str) -> dict[str, EstadoPacote]:
        pacotes = self._dados.get(aluno, {}).get(area, {})
        return {codigo: EstadoPacote(valor) for codigo, valor in pacotes.items()}
