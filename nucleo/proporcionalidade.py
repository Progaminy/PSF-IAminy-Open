# ==============================================================================
# RAZÃO, PROPORÇÃO E REGRA DE TRÊS — construídos sobre racionais.py.
# Cobre da lista original: Tópicos 35-40 (Área 1).
# ==============================================================================
from .primitivas import V, PAR
from .aritmetica import SOMA, MULT, DIV, _UM
from .racionais import RAC, NUM, DEN, MULT_RAC, EQ_RAC

# --------------------------------------------------------------------------
# Tópico 35: RAZÃO — a razão entre a e b é exatamente o racional a/b.
# Nome próprio para deixar explícito que o Tópico 35 está coberto — é o
# mesmo RAC já usado em todo o núcleo (mesma ideia da Aula 17: uma
# estrutura, vários nomes conforme o contexto pedagógico).
# --------------------------------------------------------------------------
RAZAO = lambda a: lambda b: RAC(a)(b)

# --------------------------------------------------------------------------
# Tópico 36: PROPORÇÃO — quatro números a,b,c,d estão em proporção
# quando a/b == c/d ("produto dos meios = produto dos extremos", que é
# exatamente a multiplicação cruzada que EQ_RAC já faz).
# --------------------------------------------------------------------------
EH_PROPORCAO = lambda a: lambda b: lambda c: lambda d: EQ_RAC(RAC(a)(b))(RAC(c)(d))

# --------------------------------------------------------------------------
# Tópico 37a: REGRA DE TRÊS SIMPLES DIRETA — a/b = c/x  =>  x = b*c/a
# (grandezas que crescem juntas: mais horas, mais produção)
# --------------------------------------------------------------------------
REGRA_DE_TRES_DIRETA = lambda a: lambda b: lambda c: RAC(MULT(b)(c))(a)

# --------------------------------------------------------------------------
# Tópico 37b: REGRA DE TRÊS SIMPLES INVERSA — a*b = c*x  =>  x = a*b/c
# (grandezas que crescem uma contra a outra: mais operários, menos tempo)
# --------------------------------------------------------------------------
REGRA_DE_TRES_INVERSA = lambda a: lambda b: lambda c: RAC(MULT(a)(b))(c)

# --------------------------------------------------------------------------
# Tópico 38: REGRA DE TRÊS COMPOSTA (2 grandezas) — a incógnita d2 se
# relaciona com duas outras grandezas (a, b), cada uma direta ou
# inversamente. `direta_a`/`direta_b` são booleanos de Church (V/F):
#
#   d2 = d1 * (a2/a1 se direta, senão a1/a2) * (b2/b1 se direta, senão b1/b2)
#
# Seleção direta (sem thunk): ambos os ramos são construções baratas de
# RAC, não chamadas recursivas — mesmo estilo de NUM/DEN em racionais.py.
# --------------------------------------------------------------------------
REGRA_DE_TRES_COMPOSTA_2 = lambda d1: lambda a1: lambda a2: lambda direta_a: lambda b1: lambda b2: lambda direta_b: MULT_RAC(
    MULT_RAC(
        RAC(d1)(_UM)
    )(
        direta_a(RAC(a2)(a1))(RAC(a1)(a2))
    )
)(
    direta_b(RAC(b2)(b1))(RAC(b1)(b2))
)

# --------------------------------------------------------------------------
# Tópico 39: DIVISÃO PROPORCIONAL (3 partes) — divide `total` em partes
# proporcionais aos pesos w1,w2,w3. parte_i = total * wi / (w1+w2+w3).
# Devolve PAR(p1)(PAR(p2)(p3)) — trinca aninhada, sem depender da
# convenção cons/nil (que usa F como terminador e não é distinguível de
# uma célula real só por aplicação — ver nota em traducao.para_lista).
# --------------------------------------------------------------------------
DIVISAO_PROPORCIONAL_3 = lambda total: lambda w1: lambda w2: lambda w3: (
    lambda soma_pesos: PAR(
        RAC(MULT(total)(w1))(soma_pesos)
    )(
        PAR(
            RAC(MULT(total)(w2))(soma_pesos)
        )(
            RAC(MULT(total)(w3))(soma_pesos)
        )
    )
)(SOMA(SOMA(w1)(w2))(w3))

# --------------------------------------------------------------------------
# Tópico 40: ESCALA — razão entre medida no desenho/mapa e medida real.
# É outro nome para RAZAO (mesmo padrão do Tópico 35); os dois helpers
# abaixo convertem nos dois sentidos, dada uma escala e=RAC(1)(k).
# --------------------------------------------------------------------------
ESCALA = RAZAO

DISTANCIA_REAL = lambda escala: lambda distancia_mapa: RAC(
    MULT(distancia_mapa)(DEN(escala))
)(
    NUM(escala)
)

DISTANCIA_MAPA = lambda escala: lambda distancia_real: RAC(
    MULT(distancia_real)(NUM(escala))
)(
    DEN(escala)
)
