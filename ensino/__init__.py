"""Camada auxiliar de ensino do PSF-IAminy.

Esta camada não contém conhecimento puro nem aulas prontas antigas. Ela mantém
somente estruturas auxiliares ainda coerentes: pacotes, progresso, revisão,
exercícios e leitura/execução. Conhecimento puro fica em `conhecimento/`,
`nucleo/` e `lingua_portuguesa/`.
"""

from .curriculos import CURRICULOS, PACOTES_MATEMATICA, PACOTES_PORTUGUES
from .exercicios import GeradorExercicios, ModeloExercicio
from .motor import MotorAulas
from .progresso import EstadoPacote, RegistroProgresso
from .revisao import RegistroRevisao, RevisaoPacote
from .tipos import AulaPacote, FormatoAula, PacoteConhecimento

__all__ = [
    "AulaPacote",
    "CURRICULOS",
    "EstadoPacote",
    "FormatoAula",
    "GeradorExercicios",
    "ModeloExercicio",
    "MotorAulas",
    "PACOTES_MATEMATICA",
    "PACOTES_PORTUGUES",
    "PacoteConhecimento",
    "RegistroProgresso",
    "RegistroRevisao",
    "RevisaoPacote",
]
