"""Motores de geometria."""

from ._legado import resolver

__all__ = ["MotorFormas", "MotorPerimetro", "MotorArea", "MotorPitagoras", "MotorGeometriaEspacial"]


def __getattr__(nome):
    if nome in __all__:
        return resolver(nome)
    raise AttributeError(nome)
