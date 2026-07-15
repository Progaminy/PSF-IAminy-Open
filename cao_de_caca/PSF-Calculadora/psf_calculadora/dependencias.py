"""Deteção centralizada das dependências científicas opcionais."""

from importlib.util import find_spec

PACOTES_OPCIONAIS = {
    "numpy": "NumPy",
    "sympy": "SymPy",
    "pandas": "Pandas",
    "matplotlib": "Matplotlib",
    "scipy": "SciPy",
    "networkx": "NetworkX",
    "mpmath": "mpmath",
    "sklearn": "scikit-learn",
}


class DependenciaAusenteError(RuntimeError):
    """Erro de domínio emitido antes de executar um motor indisponível."""

    def __init__(self, motor, modulos):
        self.motor = motor
        self.modulos = tuple(modulos)
        nomes = [PACOTES_OPCIONAIS.get(m, m) for m in self.modulos]
        super().__init__(
            f"O motor '{motor}' requer {', '.join(nomes)}. "
            "Instale com: pip install 'psf-calculadora[completo]'"
        )


def disponivel(modulo):
    return find_spec(modulo) is not None


def ausentes():
    return [nome for modulo, nome in PACOTES_OPCIONAIS.items() if not disponivel(modulo)]


def modulos_ausentes(modulos):
    return tuple(modulo for modulo in modulos if not disponivel(modulo))


def mensagem_instalacao():
    faltam = ausentes()
    if not faltam:
        return None
    return "Recursos avançados indisponíveis: " + ", ".join(faltam) + ". Instale com: pip install 'psf-calculadora[completo]'"
