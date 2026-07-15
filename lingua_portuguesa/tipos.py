"""Tipos públicos do motor de língua portuguesa.

Os objetos deste módulo são imutáveis: cada etapa do pipeline recebe dados e
devolve novos dados, o que facilita testes, paralelização e futuras trocas de
implementação.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from types import MappingProxyType
from typing import Any, Mapping


class TipoToken(str, Enum):
    PALAVRA = "palavra"
    NUMERO = "numero"
    PONTUACAO = "pontuacao"
    SIMBOLO = "simbolo"


class ClasseGramatical(str, Enum):
    SUBSTANTIVO = "substantivo"
    ADJETIVO = "adjetivo"
    VERBO = "verbo"
    ADVERBIO = "adverbio"
    PRONOME = "pronome"
    DETERMINANTE = "determinante"
    PREPOSICAO = "preposicao"
    CONJUNCAO = "conjuncao"
    INTERJEICAO = "interjeicao"
    NUMERAL = "numeral"
    DESCONHECIDA = "desconhecida"


class Genero(str, Enum):
    MASCULINO = "masculino"
    FEMININO = "feminino"
    COMUM = "comum"


class Numero(str, Enum):
    SINGULAR = "singular"
    PLURAL = "plural"


class Pessoa(str, Enum):
    PRIMEIRA = "primeira"
    SEGUNDA = "segunda"
    TERCEIRA = "terceira"


@dataclass(frozen=True, slots=True)
class Token:
    texto: str
    normalizado: str
    tipo: TipoToken
    inicio: int
    fim: int


@dataclass(frozen=True, slots=True)
class EntradaLexical:
    lema: str
    forma: str
    classe: ClasseGramatical
    definicoes: tuple[str, ...] = ()
    genero: Genero | None = None
    numero: Numero | None = None
    pessoa: Pessoa | None = None
    atributos: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "atributos", MappingProxyType(dict(self.atributos)))


@dataclass(frozen=True, slots=True)
class LeituraMorfologica:
    token: Token
    lema: str
    classe: ClasseGramatical
    genero: Genero | None = None
    numero: Numero | None = None
    pessoa: Pessoa | None = None
    definicoes: tuple[str, ...] = ()
    atributos: Mapping[str, Any] = field(default_factory=dict)
    confianca: float = 1.0
    origem: str = "dicionario"

    def __post_init__(self) -> None:
        object.__setattr__(self, "atributos", MappingProxyType(dict(self.atributos)))


@dataclass(frozen=True, slots=True)
class AnaliseToken:
    token: Token
    leituras: tuple[LeituraMorfologica, ...]

    @property
    def principal(self) -> LeituraMorfologica:
        return self.leituras[0]


@dataclass(frozen=True, slots=True)
class Diagnostico:
    codigo: str
    mensagem: str
    inicio: int
    fim: int
    severidade: str = "aviso"
    sugestao: str | None = None


@dataclass(frozen=True, slots=True)
class Constituinte:
    funcao: str
    texto: str
    inicio: int
    fim: int


@dataclass(frozen=True, slots=True)
class SomIsolado:
    """Unidade sonora abstrata, ainda sem significado lexical."""

    simbolo: str
    nome: str
    classe: str
    inicio: int
    fim: int
    tem_significado: bool = False


@dataclass(frozen=True, slots=True)
class Grafema:
    """Representação escrita: letra, acento, algarismo, pontuação ou espaço."""

    texto: str
    base: str
    tipo: str
    nome: str
    inicio: int
    fim: int
    acento: str | None = None


@dataclass(frozen=True, slots=True)
class CombinacaoGrafica:
    """Agrupamento de grafemas: dígrafo, sílaba aproximada ou palavra."""

    texto: str
    tipo: str
    inicio: int
    fim: int
    componentes: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class PalavraConstruida:
    """Palavra como ponte entre forma gráfica e significado."""

    texto: str
    normalizado: str
    inicio: int
    fim: int
    silabas: tuple[str, ...]
    conhecida: bool
    lema: str | None = None
    classe: ClasseGramatical = ClasseGramatical.DESCONHECIDA
    definicoes: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class FraseConstruida:
    texto: str
    inicio: int
    fim: int
    tokens: tuple[Token, ...]


@dataclass(frozen=True, slots=True)
class OracaoConstruida:
    texto: str
    inicio: int
    fim: int
    tem_verbo: bool
    verbo: str | None = None
    constituintes: tuple[Constituinte, ...] = ()


@dataclass(frozen=True, slots=True)
class EstagioLinguistico:
    ordem: int
    nome: str
    descricao: str
    quantidade: int
    exemplos: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class FluxoLinguistico:
    """A escada natural da língua: som, escrita, palavra, sentido e texto."""

    texto: str
    texto_normalizado: str
    sons: tuple[SomIsolado, ...]
    grafemas: tuple[Grafema, ...]
    combinacoes: tuple[CombinacaoGrafica, ...]
    palavras: tuple[PalavraConstruida, ...]
    frases: tuple[FraseConstruida, ...]
    oracoes: tuple[OracaoConstruida, ...]
    estagios: tuple[EstagioLinguistico, ...]
    diagnosticos: tuple[Diagnostico, ...] = ()
    constituintes: tuple[Constituinte, ...] = ()

    def estagio(self, nome: str) -> EstagioLinguistico | None:
        alvo = nome.casefold()
        return next((item for item in self.estagios if item.nome.casefold() == alvo), None)


@dataclass(frozen=True, slots=True)
class AnaliseTexto:
    texto: str
    texto_normalizado: str
    tokens: tuple[Token, ...]
    morfologia: tuple[AnaliseToken, ...]
    diagnosticos: tuple[Diagnostico, ...]
    constituintes: tuple[Constituinte, ...] = ()
    fluxo: FluxoLinguistico | None = None

    @property
    def valido(self) -> bool:
        return not any(item.severidade == "erro" for item in self.diagnosticos)
