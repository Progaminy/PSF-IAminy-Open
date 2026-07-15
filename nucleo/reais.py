# ==============================================================================
# REAIS APROXIMADOS — raiz quadrada por Newton-Raphson, em racionais exatos.
# ==============================================================================
# HISTÓRICO HONESTO — duas tentativas anteriores, ambas testadas e
# descartadas por razões diferentes, documentadas aqui porque o motivo
# de cada falha ensina algo real sobre numerais unários:
#
#   TENTATIVA 1 — busca binária direta no espaço de milésimos (M/1000).
#   Falhou por PROFUNDIDADE: um numeral de Church é avaliado de forma
#   ESTRITA (não preguiçosa) em Python — aplicar um numeral de valor N a
#   uma função exige N chamadas Python aninhadas, literalmente. Só
#   escalar √2 por 1000² já cria um numeral de 2.000.000 — impossível de
#   avaliar em qualquer pilha razoável (não é "aumentar o limite", é
#   memória física).
#
#   TENTATIVA 2 — Newton-Raphson em racionais exatos, SEM simplificar
#   entre iterações. Falhou por CRESCIMENTO: multiplicação cruzada de
#   frações sem reduzir ao MDC faz numerador/denominador crescerem a
#   cada passo, ultrapassando rapidamente o que dá para avaliar.
#
#   TENTATIVA 3 (esta) — Newton-Raphson + SIMPLIFICAR a cada passo.
#   Funciona matematicamente, mas revelou um limite mais profundo:
#   DESEMPENHO, não profundidade. A causa raiz: numerais de Church NÃO
#   TÊM PREDECESSOR EM O(1) — é um facto conhecido da lambda calculus
#   pura (o "problema do predecessor" que Kleene resolveu com o truque
#   do par deslizante que usamos em `aritmetica.PRED`). Esse truque
#   funciona, mas custa O(n) POR CHAMADA — e como `SUB(m)(n)` chama
#   `PRED` repetidamente (uma vez por unidade de n, cada chamada sobre
#   um valor decrescente), o custo real de `SUB`/`DIV`/`MDC` sobre dois
#   números GRANDES é O(n·m), não O(n). Isto é invisível no resto do
#   projeto (todo o resto usa operandos pequenos), mas Newton-Raphson
#   produz exatamente o cenário que expõe o problema: dois racionais de
#   magnitude comparável, repetidamente. CONSERTAR ISTO DE VERDADE
#   exigiria trocar a representação unária por uma posicional (binária)
#   — um projeto à parte, não um ajuste deste módulo.
#
# ESCOPO TESTADO (não assumido — ver testes/test_nucleo.py): correto e
# verificado, com um chute inicial melhorado (ver RAIZ_PISO_PURA abaixo),
# para alvo ∈ {2, 3, 5, 8, 9, 10, 11, 12, 20} — testado explicitamente,
# tempos entre 0.003s e ~7s. Outros valores (6, 7, 13, 15, 17, ...) foram
# testados e FALHAM na mesma janela de tempo, com a mesma causa: SUB/DIV
# custam O(n·m), não O(n), e alguns numeradores/denominadores intermédios
# calham a ser coprimos, o pior caso. Melhorar isto de forma genérica
# exigiria representação binária (ver README.md).
#
# MELHORIA NESTA RONDA — chute inicial: a primeira versão começava de
# x₀=alvo/1, um chute muito pior que a raiz de facto (para alvo=20,
# x₀=20 está a um fator de ~4.5 da resposta certa ≈4.47). Isso exigia
# mais iterações, logo números maiores, logo mais lentidão. Agora
# começa-se de x₀=⌊√alvo⌋/1, achado por uma busca barata (só MULT e
# comparação, sem DIV) — o mesmo tipo de busca já usado em EH_PRIMO.
# Resultado real, testado: alvo=5 passou de "falha" para "correto em
# 0.34s"; o conjunto verificado cresceu de {2,3} para 9 valores.
# ==============================================================================
from .primitivas import V, ZERO, S, Y
from .aritmetica import IS_ZERO, PRED, MULT, MAIOR, _UM
from .racionais import RAC, NUM, DEN, MULT_RAC, SOMA_RAC, SIMPLIFICAR, RECIPROCO_RAC

_DOIS = S(_UM)
_TRES = S(_DOIS)
_ITERACOES_PADRAO = _TRES

_METADE = RAC(_UM)(_DOIS)

# --------------------------------------------------------------------------
# RAIZ_PISO_PURA — maior natural i tal que i² <= alvo. Busca linear
# simples, barata porque só usa MULT e comparação (nunca DIV/MOD) — o
# mesmo padrão de custo que já sabemos ser seguro (ver EH_PRIMO). Só
# prático para alvo pequeno (o mesmo domínio onde este módulo já opera).
# --------------------------------------------------------------------------
_RAIZ_PISO_REC = Y(lambda buscar: lambda alvo: lambda i:
    MAIOR(MULT(S(i))(S(i)))(alvo)(
        lambda _: i
    )(
        lambda _: buscar(alvo)(S(i))
    )(V)
)
RAIZ_PISO_PURA = lambda alvo: _RAIZ_PISO_REC(alvo)(ZERO)

# --------------------------------------------------------------------------
# UM PASSO DE NEWTON PARA RAIZ QUADRADA: x -> (x + alvo/x) / 2
# SIMPLIFICAR ao final de cada passo é essencial, não cosmético: sem
# reduzir ao MDC, numerador/denominador crescem por multiplicação
# cruzada a cada iteração e ultrapassam rapidamente o que este núcleo
# unário consegue processar (ver histórico no topo do ficheiro).
# --------------------------------------------------------------------------
_PASSO_NEWTON = lambda alvo_rac: lambda x: SIMPLIFICAR(MULT_RAC(
    SOMA_RAC(x)(MULT_RAC(alvo_rac)(RECIPROCO_RAC(x)))
)(_METADE))

# --------------------------------------------------------------------------
# ITERA _ITERACOES vezes, a partir do chute inicial x0 = alvo/1
# --------------------------------------------------------------------------
_ITERAR_NEWTON = Y(lambda iterar: lambda alvo_rac: lambda x: lambda k:
    IS_ZERO(k)(
        lambda _: x
    )(
        lambda _: iterar(alvo_rac)(_PASSO_NEWTON(alvo_rac)(x))(PRED(k))
    )(V)
)

# --------------------------------------------------------------------------
# API — RAIZ_QUADRADA_RAC_N(alvo)(n): itera `n` vezes a partir do chute
# ⌊√alvo⌋/1 (não mais alvo/1). RAIZ_QUADRADA_RAC(alvo) é o caso n=3.
# --------------------------------------------------------------------------
RAIZ_QUADRADA_RAC_N = lambda alvo: lambda n: _ITERAR_NEWTON(
    RAC(alvo)(_UM)
)(
    RAC(RAIZ_PISO_PURA(alvo))(_UM)
)(n)

RAIZ_QUADRADA_RAC = lambda alvo: RAIZ_QUADRADA_RAC_N(alvo)(_ITERACOES_PADRAO)
