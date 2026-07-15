"""API pública da PSF Calculadora."""

__version__ = "1.0.0"


def criar_calculadora():
    """Cria a calculadora mantendo o carregamento do legado sob demanda."""
    from assistente_psf import PSFCalculadora

    return PSFCalculadora()


__all__ = ["criar_calculadora", "__version__"]
