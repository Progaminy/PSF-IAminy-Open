"""Motor modular de língua portuguesa."""

from .conhecimento_puro import ConceitoPortugues, ConstrutorConhecimentoPortugues
from .lexico import Dicionario
from .motor import MotorPortugues
from .ponte_matematica import (
    AuditoriaMatematicaPortugues,
    ComparacaoGramaticalFinita,
    PonteMatematicaPortugues,
    ProvaReescritaTerminologica,
)
from .tipos import (
    AnaliseTexto,
    AnaliseToken,
    ClasseGramatical,
    CombinacaoGrafica,
    Constituinte,
    Diagnostico,
    EntradaLexical,
    EstagioLinguistico,
    FluxoLinguistico,
    FraseConstruida,
    Genero,
    Grafema,
    LeituraMorfologica,
    Numero,
    OracaoConstruida,
    PalavraConstruida,
    SomIsolado,
    TipoToken,
    Token,
)

__all__ = [
    "AnaliseTexto",
    "AuditoriaMatematicaPortugues",
    "ComparacaoGramaticalFinita",
    "PonteMatematicaPortugues",
    "ProvaReescritaTerminologica",
    "ConceitoPortugues",
    "ConstrutorConhecimentoPortugues",
    "AnaliseToken",
    "ClasseGramatical",
    "CombinacaoGrafica",
    "Constituinte",
    "Diagnostico",
    "Dicionario",
    "EntradaLexical",
    "EstagioLinguistico",
    "FluxoLinguistico",
    "FraseConstruida",
    "Genero",
    "Grafema",
    "LeituraMorfologica",
    "MotorPortugues",
    "Numero",
    "OracaoConstruida",
    "PalavraConstruida",
    "SomIsolado",
    "TipoToken",
    "Token",
]
