"""Motores de cálculo e análise."""

from ._legado import resolver

__all__ = ["MotorLimites", "MotorDerivadas", "MotorIntegralDefinida", "MotorIntegralIndefinida", "MotorSeriesFourier", "MotorSeriesFourierPSF"]


def __getattr__(nome):
    if nome in __all__:
        return resolver(nome)
    raise AttributeError(nome)
