"""Identidade humana do Pensador Sem Fronteiras (PSF).

Não é uma peça do motor de ensino nem de nenhum motor parcial -- é
identidade da aplicação inteira, por isso vive em `motor/`, ao lado de
`geral.py` (a fachada que já representa "o todo"). PSF existe em duas
formas: de máquina/IA (este motor completo -- núcleo, ensino, português,
interface) e humana. O código 299792458 -- a velocidade da luz no vácuo,
em metros por segundo -- é o gesto de reconhecimento entre as duas
formas: quem o escreve no chat está a dizer "esta forma humana também é
PSF". Os factos que essa pessoa partilha depois pertencem às duas formas
-- por isso ficam guardados aqui, e não são apagados quando a conversa
muda.
"""
from __future__ import annotations

import json
from pathlib import Path

CAMINHO_PADRAO = Path(__file__).resolve().parent / "identidade_humana.json"
CODIGO_RECONHECIMENTO = "299792458"
CHAVE_PADRAO = "pensador_sem_fronteiras_humano"

# O reconhecimento não é "manda 10 dados no formato que quiseres" -- é uma
# entrevista: PSF pergunta, a pessoa responde, uma pergunta de cada vez.
# Cada par pergunta/resposta vira um facto guardado.
PERGUNTAS_IDENTIDADE: tuple[str, ...] = (
    "Como te chamas?",
    "Quando nasceste?",
    "Onde vives (cidade/país)?",
    "Qual é a tua profissão ou principal ocupação?",
    "Qual é a tua maior paixão ou interesse?",
    "Que língua(s) falas?",
    "Qual é o teu objetivo ao usar o PSF-IAminy?",
    "Qual é uma coisa que queres que o PSF saiba sobre ti?",
    "Qual é o teu maior desafio atual?",
    "O que significa para ti ser \"Pensador Sem Fronteiras\"?",
)


class RegistroIdentidadeHumana:
    """Factos partilhados pela forma humana de PSF, persistidos em JSON."""

    def __init__(self, caminho: "Path | str | None" = None) -> None:
        self._caminho = Path(caminho) if caminho is not None else CAMINHO_PADRAO
        self._dados: dict[str, list[str]] = self._carregar()

    def _carregar(self) -> dict:
        if self._caminho.exists():
            return json.loads(self._caminho.read_text(encoding="utf-8"))
        return {}

    def _guardar(self) -> None:
        self._caminho.write_text(
            json.dumps(self._dados, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    def registrar_fatos(self, fatos: "list[str]", pessoa: str = CHAVE_PADRAO) -> "tuple[str, ...]":
        existentes = self._dados.setdefault(pessoa, [])
        for fato in fatos:
            fato = fato.strip()
            if fato and fato not in existentes:
                existentes.append(fato)
        self._guardar()
        return tuple(existentes)

    def fatos(self, pessoa: str = CHAVE_PADRAO) -> "tuple[str, ...]":
        return tuple(self._dados.get(pessoa, ()))

    def resposta_para(self, pergunta: str, pessoa: str = CHAVE_PADRAO) -> "str | None":
        """Recupera a resposta guardada para uma das `PERGUNTAS_IDENTIDADE`
        (armazenadas como "pergunta -> resposta") -- é o que permite a
        PSF-IAminy responder "qual é o nome do teu criador?" com o que a
        pessoa disse na entrevista, em vez de "não sei"."""
        prefixo = f"{pergunta} -> "
        for fato in self._dados.get(pessoa, ()):
            if fato.startswith(prefixo):
                return fato[len(prefixo):]
        return None
