# ==============================================================================
# FATORAÇÃO PURA — construída depois de primo/composto e divisão euclidiana.
# ==============================================================================
# Lei PSF-IAminy:
#   fatoração não é usada para definir primo; ela nasce depois.
#
# A decomposição aqui é por busca finita do menor fator. Quando o menor fator d
# é encontrado, usamos o quociente já construído pela divisão euclidiana pura.
#
# Dependências proibidas aqui:
#   operador nativo /, //, %, MOD, DIV, MMC, fatoração pronta antiga.
# ==============================================================================
from .primitivas import V, F, PAR, Y
from .aritmetica import MAIOR, _UM
from .divisao_euclidiana_pura import QUOCIENTE_PURO
from .primalidade_pura import MENOR_FATOR_PURO


# --------------------------------------------------------------------------
# Fatoração por busca:
#   se n <= 1: lista vazia;
#   se n > 1: d = menor fator de n; devolve d :: fatoracao(n/d).
# O quociente n/d só é tomado depois de d ser confirmado como divisor.
# --------------------------------------------------------------------------
FATORACAO_PURA = Y(lambda fatorar: lambda n:
    MAIOR(n)(_UM)(
        lambda _: (lambda d: PAR(d)(fatorar(QUOCIENTE_PURO(n)(d))))(MENOR_FATOR_PURO(n))
    )(
        lambda _: F
    )(V)
)
