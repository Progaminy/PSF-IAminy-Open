"""Motores de álgebra."""

from ._legado import resolver

__all__ = ["MotorEquacaoPrimeiroGrau", "MotorEquacaoSegundoGrau", "MotorPolinomios", "MotorMatrizes", "MotorSistemasLineares"]


def __getattr__(nome):
    if nome in __all__:
        return resolver(nome)
    raise AttributeError(nome)
