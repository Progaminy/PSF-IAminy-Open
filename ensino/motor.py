"""Motor auxiliar de pacotes do PSF-IAminy."""
from __future__ import annotations

from .curriculos import CURRICULOS
from .exercicios import GeradorExercicios
from .tipos import AulaPacote, FormatoAula, PacoteConhecimento


class MotorAulas:
    """Gera material didático auxiliar a partir de pacotes sequenciais."""

    def __init__(
        self,
        curriculos: dict[str, tuple[PacoteConhecimento, ...]] | None = None,
        exercicios: GeradorExercicios | None = None,
    ) -> None:
        self._curriculos = curriculos or CURRICULOS
        self._exercicios = exercicios or GeradorExercicios()
        self._indice = {
            area: {pacote.codigo: pacote for pacote in pacotes}
            for area, pacotes in self._curriculos.items()
        }

    def areas(self) -> tuple[str, ...]:
        return tuple(sorted(self._curriculos))

    def curriculo(self, area: str) -> tuple[PacoteConhecimento, ...]:
        chave = _normalizar_area(area)
        if chave not in self._curriculos:
            raise KeyError(f"área desconhecida: {area!r}")
        return self._curriculos[chave]

    def pacote(self, area: str, codigo: str) -> PacoteConhecimento:
        chave = _normalizar_area(area)
        try:
            return self._indice[chave][codigo.upper()]
        except KeyError as erro:
            raise KeyError(f"pacote desconhecido: {area!r}/{codigo!r}") from erro

    def proximo(
        self,
        area: str,
        concluidos: tuple[str, ...] | list[str] | set[str] = (),
    ) -> PacoteConhecimento | None:
        feitos = {codigo.upper() for codigo in concluidos}
        return next((pacote for pacote in self.curriculo(area) if pacote.codigo not in feitos), None)

    def gerar(
        self,
        area: str,
        codigo: str,
        formato: int | str | FormatoAula = FormatoAula.CURTA,
    ) -> AulaPacote:
        pacote = self.pacote(area, codigo)
        modo = FormatoAula.de(formato)
        linhas = _renderizar(pacote, modo)
        return AulaPacote(pacote=pacote, formato=modo, linhas=tuple(linhas))

    def gerar_proximo(
        self,
        area: str,
        concluidos: tuple[str, ...] | list[str] | set[str] = (),
        formato: int | str | FormatoAula = FormatoAula.CURTA,
    ) -> AulaPacote | None:
        pacote = self.proximo(area, concluidos)
        if pacote is None:
            return None
        return self.gerar(area, pacote.codigo, formato)

    def mapa(self, area: str) -> tuple[str, ...]:
        return tuple(f"{pacote.codigo} — {pacote.titulo}" for pacote in self.curriculo(area))


    def exercicios_variados(
        self,
        area: str,
        codigo: str,
        quantidade: int = 3,
        semente: int | None = None,
    ) -> tuple[str, ...]:
        pacote = self.pacote(area, codigo)
        return self._exercicios.gerar(pacote, quantidade, semente)


def _normalizar_area(area: str) -> str:
    texto = area.strip().casefold()
    if texto in {"matemática", "matematica", "math"}:
        return "matematica"
    if texto in {"português", "portugues", "língua portuguesa", "lingua portuguesa"}:
        return "portugues"
    return texto


def _renderizar(pacote: PacoteConhecimento, formato: FormatoAula) -> list[str]:
    if formato == FormatoAula.CURTA:
        return _aula_curta(pacote)
    if formato == FormatoAula.EXPLICADA:
        return _aula_explicada(pacote)
    if formato == FormatoAula.COM_EXEMPLO:
        return _aula_com_exemplo(pacote)
    if formato == FormatoAula.COM_EXERCICIOS:
        return _aula_com_exercicios(pacote)
    return _aula_desmontada(pacote)


def _cabecalho(pacote: PacoteConhecimento, formato: str) -> list[str]:
    return [
        f"{pacote.codigo} — {pacote.titulo}",
        f"Formato: {formato}",
        f"Objetivo: {pacote.objetivo}",
    ]


def _aula_curta(pacote: PacoteConhecimento) -> list[str]:
    linhas = [f"{pacote.codigo} — {pacote.titulo}", pacote.objetivo]
    linhas.extend(pacote.passos)
    linhas.append("Pronto: repita até ficar fácil.")
    return linhas


def _aula_explicada(pacote: PacoteConhecimento) -> list[str]:
    linhas = _cabecalho(pacote, "2 — explicada")
    linhas.extend(
        (
            "",
            "Ideia",
            pacote.explicacao,
            "",
            "Passos",
        )
    )
    linhas.extend(_numerar(pacote.passos))
    linhas.extend(("", "Palavras-chave", ", ".join(pacote.palavras_chave)))
    return linhas


def _aula_com_exemplo(pacote: PacoteConhecimento) -> list[str]:
    linhas = _aula_explicada(pacote)
    linhas.extend(("", "Exemplo"))
    linhas.extend(_marcar(pacote.exemplos))
    return linhas


def _aula_com_exercicios(pacote: PacoteConhecimento) -> list[str]:
    linhas = _aula_com_exemplo(pacote)
    linhas.extend(("", "Exercícios"))
    linhas.extend(_numerar(pacote.exercicios))
    return linhas


def _aula_desmontada(pacote: PacoteConhecimento) -> list[str]:
    linhas = _cabecalho(pacote, "5 — detalhada e desmontada")
    linhas.extend(
        (
            "",
            "Pré-requisitos",
            _pre_requisitos(pacote),
            "",
            "Ideia central",
            pacote.explicacao,
            "",
            "Desmontagem",
        )
    )
    linhas.extend(_numerar(pacote.desmontagem))
    linhas.extend(("", "Passo a passo falado"))
    linhas.extend(_numerar(pacote.passos))
    linhas.extend(("", "Exemplos"))
    linhas.extend(_marcar(pacote.exemplos))
    linhas.extend(("", "Exercícios"))
    linhas.extend(_numerar(pacote.exercicios))
    linhas.extend(("", "Como saber que entendeu", "A pessoa consegue explicar com palavras próprias e criar outro exemplo."))
    if pacote.melhorias:
        linhas.extend(("", "Pode melhorar neste pacote"))
        linhas.extend(_marcar(pacote.melhorias))
    return linhas


def _pre_requisitos(pacote: PacoteConhecimento) -> str:
    return ", ".join(pacote.pre_requisitos) if pacote.pre_requisitos else "nenhum; começa do zero absoluto"


def _numerar(itens: tuple[str, ...]) -> list[str]:
    return [f"{indice}. {item}" for indice, item in enumerate(itens, 1)]


def _marcar(itens: tuple[str, ...]) -> list[str]:
    return [f"- {item}" for item in itens]
