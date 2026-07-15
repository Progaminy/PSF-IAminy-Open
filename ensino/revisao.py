"""Revisão espaçada por pacote do PSF-IAminy.

`RegistroProgresso` sabe que estágio (visto/entendido/praticado) uma
pessoa alcançou num pacote, mas não sabe quando é hora de revisar de novo
nem quais pacotes ficaram fracos. Este módulo fecha essa lacuna.

A agenda é contada em sessões de estudo, não em relógio real -- o
chamador passa o número da sessão atual (1, 2, 3, ...). Isso segue o
mesmo estilo do resto do motor: finito, determinístico, sem depender de
data/hora do sistema.

Cada revisão de um pacote é acerto ou erro:
- um acerto sobe um degrau na escada de intervalos (a memória segura
  precisa de menos reforço, então o próximo encontro pode demorar mais);
- um erro derruba o pacote para o primeiro degrau -- ele fica "fraco" e
  deve reaparecer já na sessão seguinte.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

# Intervalos entre revisões, em número de sessões, por degrau. Um acerto
# avança um degrau; um erro devolve ao degrau 0. Fixa e pequena de
# propósito -- o motor pode crescer isto depois sem quebrar o formato
# guardado (é só um índice nesta sequência).
DEGRAUS_INTERVALO: tuple[int, ...] = (1, 2, 4, 8, 16)


@dataclass(frozen=True, slots=True)
class RevisaoPacote:
    degrau: int
    proxima_sessao: int
    fraco: bool


class RegistroRevisao:
    """Agenda de revisão espaçada de pacotes, por pessoa e área."""

    def __init__(self, caminho: "Path | str | None" = None) -> None:
        self._caminho = Path(caminho) if caminho is not None else None
        self._dados: dict[str, dict[str, dict[str, dict[str, object]]]] = self._carregar()

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

    def registrar(
        self,
        aluno: str,
        area: str,
        codigo: str,
        acertou: bool,
        sessao_atual: int,
    ) -> RevisaoPacote:
        codigo = codigo.upper()
        pacotes = self._dados.setdefault(aluno, {}).setdefault(area, {})
        anterior = pacotes.get(codigo)
        degrau_anterior = anterior["degrau"] if anterior else -1
        novo_degrau = min(degrau_anterior + 1, len(DEGRAUS_INTERVALO) - 1) if acertou else 0
        proxima = sessao_atual + DEGRAUS_INTERVALO[novo_degrau]
        pacotes[codigo] = {"degrau": novo_degrau, "proxima_sessao": proxima, "fraco": not acertou}
        self._guardar()
        return RevisaoPacote(degrau=novo_degrau, proxima_sessao=proxima, fraco=not acertou)

    def estado(self, aluno: str, area: str, codigo: str) -> "RevisaoPacote | None":
        valor = self._dados.get(aluno, {}).get(area, {}).get(codigo.upper())
        if valor is None:
            return None
        return RevisaoPacote(degrau=valor["degrau"], proxima_sessao=valor["proxima_sessao"], fraco=valor["fraco"])

    def pendentes(self, aluno: str, area: str, sessao_atual: int) -> tuple[str, ...]:
        """Pacotes já revisados ao menos uma vez que estão vencidos nesta
        sessão, mais vencidos e mais fracos primeiro."""
        pacotes = self._dados.get(aluno, {}).get(area, {})
        vencidos = [
            (valor["proxima_sessao"], 0 if valor["fraco"] else 1, codigo)
            for codigo, valor in pacotes.items()
            if valor["proxima_sessao"] <= sessao_atual
        ]
        vencidos.sort()
        return tuple(codigo for _, _, codigo in vencidos)

    def fracos(self, aluno: str, area: str) -> tuple[str, ...]:
        pacotes = self._dados.get(aluno, {}).get(area, {})
        return tuple(sorted(codigo for codigo, valor in pacotes.items() if valor["fraco"]))
