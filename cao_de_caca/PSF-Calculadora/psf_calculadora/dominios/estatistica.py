"""Motores de estatística e probabilidade."""

from ._legado import resolver

__all__ = ["MotorMedia", "MotorDispersao", "MotorProbabilidade", "MotorEstatisticaCentral"]


def __getattr__(nome):
    if nome in __all__:
        return resolver(nome)
    raise AttributeError(nome)
