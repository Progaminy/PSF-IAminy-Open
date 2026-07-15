# ==============================================================================
# PROBABILIDADE — como racionais (casos favoráveis / casos totais).
# Cobre da lista original: Tópicos 590, 593-596 (Área 8).
# (591 "Espaço amostral" e 592 "Evento" são conceptuais — um conjunto de
# resultados e um subconjunto dele — não pedem uma função dedicada aqui.)
# ==============================================================================
from .racionais import RAC, NUM, DEN, MULT_RAC, SOMA_RAC, SUB_RAC, EQ_RAC, DIV_RAC, POT_RAC
from .combinatoria import COMBINACAO_SIMPLES
from .aritmetica import SUB, _UM

# --------------------------------------------------------------------------
# Tópico 590: PROBABILIDADE — casos favoráveis / casos totais
# --------------------------------------------------------------------------
PROBABILIDADE = lambda favoraveis: lambda totais: RAC(favoraveis)(totais)

# --------------------------------------------------------------------------
# Tópico 593: PROBABILIDADE CONDICIONAL — P(A|B) = P(A∩B) / P(B)
# --------------------------------------------------------------------------
PROB_CONDICIONAL = lambda p_a_e_b: lambda p_b: DIV_RAC(p_a_e_b)(p_b)

# --------------------------------------------------------------------------
# Tópico 594: EVENTOS INDEPENDENTES — A,B independentes <=> P(A∩B)=P(A)·P(B)
# --------------------------------------------------------------------------
EVENTOS_INDEPENDENTES = lambda p_a: lambda p_b: lambda p_a_e_b: EQ_RAC(
    p_a_e_b
)(
    MULT_RAC(p_a)(p_b)
)

# --------------------------------------------------------------------------
# Tópico 595: PROBABILIDADE DA UNIÃO — P(A∪B) = P(A) + P(B) − P(A∩B)
# (SUB_RAC é segura aqui: P(A)+P(B) >= P(A∩B) sempre, matematicamente —
# mesma garantia já usada em DIVISORES_PROPRIOS_SOMA)
# --------------------------------------------------------------------------
PROB_UNIAO = lambda p_a: lambda p_b: lambda p_a_e_b: SUB_RAC(SOMA_RAC(p_a)(p_b))(p_a_e_b)

# --------------------------------------------------------------------------
# Tópico 596: PROBABILIDADE BINOMIAL — P(X=k) = C(n,k) · p^k · (1-p)^(n-k)
# `p` é um racional (probabilidade de sucesso numa tentativa).
# --------------------------------------------------------------------------
_UM_RAC = RAC(_UM)(_UM)

PROBABILIDADE_BINOMIAL = lambda n: lambda k: lambda p: MULT_RAC(
    MULT_RAC(
        RAC(COMBINACAO_SIMPLES(n)(k))(_UM)
    )(
        POT_RAC(p)(k)
    )
)(
    POT_RAC(SUB_RAC(_UM_RAC)(p))(SUB(n)(k))
)
