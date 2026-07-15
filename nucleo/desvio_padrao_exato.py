"""Desvio padrão exato — raiz quadrada da variância, quando é quadrado perfeito racional.

"Desvio padrão" existia neste projeto só como extensão implícita da
variância (ETAPA 961-990, `variancia_par`): a variância já está
construída e testada; faltava só a raiz. Este módulo liga `variancia_par`
a `raiz_quadrada_exata_ou_none` (ETAPA 1048) — quando a variância não é
quadrado perfeito racional, o desvio padrão fica honestamente sem forma
exata, não aproximado (isso dependeria de reais completos ou da lei
geradora, ETAPA 1035).
"""
from __future__ import annotations

from .equacao_quadratica_exata import raiz_quadrada_exata_ou_none
from .estatistica_finita_psf import variancia_par
from .reais_intervalos_naturais import RacionalAssinado


def desvio_padrao_exato_ou_none(dados: list[int]) -> RacionalAssinado | None:
    """Desvio padrão populacional exato dos dados, quando a variância é quadrado perfeito racional."""
    numerador, denominador = variancia_par(dados)
    variancia = RacionalAssinado(numerador, denominador)
    return raiz_quadrada_exata_ou_none(variancia)
