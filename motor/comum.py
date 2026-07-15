"""Motor comum do PSF: memória, dependências, auditoria, busca e rastreabilidade."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable


@dataclass(frozen=True, slots=True)
class UnidadeComum:
    dominio: str
    nome: str
    descricao: str
    dependencias: tuple[str, ...]
    origem: str


@dataclass(frozen=True, slots=True)
class RegistroMemoria:
    instante: str
    dominio: str
    acao: str
    referencia: str


class MotorComumPSF:
    """Serviços comuns sem absorver o conhecimento dos domínios."""

    def __init__(self) -> None:
        self._unidades: dict[tuple[str, str], UnidadeComum] = {}
        self._memoria: list[RegistroMemoria] = []

    def registrar(self, unidades: Iterable[UnidadeComum]) -> None:
        for unidade in unidades:
            chave = (unidade.dominio.lower(), unidade.nome.lower())
            self._unidades[chave] = unidade

    def registrar_portugues(self, conceitos) -> None:
        self.registrar(
            UnidadeComum("português", c.nome, c.construcao, tuple(c.depende_de), "lingua_portuguesa/conhecimento_puro.py")
            for c in conceitos
        )

    def registrar_matematica(self, conceitos) -> None:
        self.registrar(
            UnidadeComum("matemática", c.nome, c.construcao, tuple(c.dependencias_declaradas), c.arquivo)
            for c in conceitos
        )

    def lembrar(self, dominio: str, acao: str, referencia: str) -> RegistroMemoria:
        registro = RegistroMemoria(datetime.now(timezone.utc).isoformat(), dominio, acao, referencia)
        self._memoria.append(registro)
        return registro

    def memoria(self, limite: int | None = None) -> tuple[RegistroMemoria, ...]:
        dados = self._memoria if limite is None else self._memoria[-limite:]
        return tuple(dados)

    def buscar(self, texto: str, dominio: str | None = None) -> tuple[UnidadeComum, ...]:
        termos = {t for t in texto.lower().split() if len(t) > 2}
        resultados: list[tuple[int, UnidadeComum]] = []
        for unidade in self._unidades.values():
            if dominio and unidade.dominio.lower() != dominio.lower():
                continue
            alvo = f"{unidade.nome} {unidade.descricao}".lower()
            pontos = sum(1 for termo in termos if termo in alvo)
            if pontos:
                resultados.append((pontos, unidade))
        resultados.sort(key=lambda x: (-x[0], x[1].dominio, x[1].nome))
        return tuple(u for _, u in resultados)

    def dependencias(self, dominio: str, nome: str) -> tuple[str, ...]:
        unidade = self._unidades.get((dominio.lower(), nome.lower()))
        return unidade.dependencias if unidade else ()

    def rastrear(self, dominio: str, nome: str) -> str | None:
        unidade = self._unidades.get((dominio.lower(), nome.lower()))
        return unidade.origem if unidade else None

    def auditar(self) -> dict[str, object]:
        por_dominio: dict[str, int] = {}
        for unidade in self._unidades.values():
            por_dominio[unidade.dominio] = por_dominio.get(unidade.dominio, 0) + 1
        return {
            "unidades": len(self._unidades),
            "por_dominio": dict(sorted(por_dominio.items())),
            "chaves_unicas": len(self._unidades) == len(set(self._unidades)),
            "papel": "serviço comum; não substitui conhecimento de Matemática nem de Português",
        }
