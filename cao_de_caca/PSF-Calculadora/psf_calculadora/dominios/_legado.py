"""Ponte temporária para migrar motores do módulo legado por etapas."""

from importlib import import_module


def resolver(nome):
    return getattr(import_module("assistente_psf"), nome)
