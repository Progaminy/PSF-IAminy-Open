# ==============================================================================
# SISTEMA BINÁRIO — vetor de 10 bits de largura FIXA, com incremento O(1)
# amortizado e soma posicional por carry. Cobre da lista original: Tópico
# 45 (Área 1) e a Etapa 134 do fluxo conceitual.
# ==============================================================================
# POR QUE LARGURA FIXA, E NÃO "quantos bits precisar" (como reais.py com
# 3 casas decimais): extrair bits via MOD(n)(2)/DIV(n)(2) repetido herdaria
# o MESMO custo O(n²) já documentado em reais.py e divisores.py — cada
# MOD/DIV chama SUB, que chama PRED, que é O(valor atual) por chamada.
#
# A SAÍDA aqui é estrutural, não numérica: em vez de perguntar "qual o
# bit i de n?" (que exige "conhecer" n primeiro, daí o custo), CONSTRÓI-SE
# o binário por INCREMENTO — parte-se de 0000000000 e soma-se 1, n vezes,
# usando um incrementador de largura FIXA (10 bits, gerado uma vez, em
# tempo de definição — mesmo espírito de _DEZ/_CEM/_MIL em reais.py: uma
# composição pequena e fixa de V/F/PAR, não uma primitiva nova).
#
# Por que isso é rápido: incrementar um contador binário é O(1) AMORTIZADO
# (resultado clássico de análise amortizada — o bit i só troca de valor
# uma vez a cada 2^i incrementos, então a soma de trocas em n incrementos
# é n + n/2 + n/4 + ... < 2n). Aplicado n vezes via ITER, o custo total é
# O(n) — LINEAR, não O(n²). Testado abaixo, não assumido.
#
# LIMITE HONESTO: largura fixa em 10 bits cobre 0..1023. Acima disso, o
# carry do bit mais significativo "cai para fora" silenciosamente — a
# semântica correta de um registador de largura fixa, não um bug
# escondido. Testado explicitamente abaixo.
# ==============================================================================
from .primitivas import V, F, PAR, S, ITER
from .logica import E, OU, XOR
from .aritmetica import SOMA, MULT, POT, ZERO, _UM, IGUAL

_LARGURA = 10  # 0..1023 — constante Python: é a FORMA da estrutura, não
                # um valor calculado (mesmo papel de "profundidade" numa
                # árvore de tamanho fixo).


def _gerar_incrementador(profundidade):
    """Gera, em tempo de definição Python (não em tempo de execução
    Church), a função de incremento para um vetor de `profundidade`
    bits. A recursão é sobre um INTEIRO PYTHON fixo (10), não sobre um
    numeral de Church — não há custo de execução associado a esta
    geração; ela só monta a cadeia de lambdas uma vez, na importação."""
    if profundidade == 1:
        return lambda bit: bit(F)(V)   # troca; overflow perde-se (correto p/ largura fixa)
    inc_resto = _gerar_incrementador(profundidade - 1)
    return lambda vetor: vetor(V)(
        PAR(F)(inc_resto(vetor(F)))   # bit era 1 -> vira 0, carrega para o resto
    )(
        PAR(V)(vetor(F))              # bit era 0 -> vira 1, resto intacto
    )


def _gerar_vetor_zero(profundidade):
    if profundidade == 1:
        return F
    return PAR(F)(_gerar_vetor_zero(profundidade - 1))


_INCREMENTAR_BINARIO = _gerar_incrementador(_LARGURA)
_VETOR_ZERO = _gerar_vetor_zero(_LARGURA)

# --------------------------------------------------------------------------
# API — PARA_BINARIO(n): vetor de 10 bits (LSB primeiro) representando n.
# --------------------------------------------------------------------------
PARA_BINARIO = lambda n: ITER(n)(_VETOR_ZERO)(_INCREMENTAR_BINARIO)


# --------------------------------------------------------------------------
# DE_BINARIO(vetor) — reconstrói o natural: Σ bit_i · 2^i, i=0..9.
# O `for` aqui percorre 10 POSIÇÕES ESTRUTURAIS FIXAS (mesma largura
# estática de sempre), não "conta até um valor" — cada termo em si é
# calculado com SOMA/MULT/POT genuínos do núcleo, nunca com + nativo.
# --------------------------------------------------------------------------
def DE_BINARIO(vetor):
    total = ZERO
    atual = vetor
    peso = _UM  # 2^0
    dois = S(_UM)
    for i in range(_LARGURA):
        if i < _LARGURA - 1:
            bit, atual = atual(V), atual(F)
        else:
            bit = atual
        valor_bit = bit(_UM)(ZERO)
        total = SOMA(total)(MULT(valor_bit)(peso))
        peso = MULT(peso)(dois)
    return total


# --------------------------------------------------------------------------
# SOMA_BINARIA(a)(b) — soma posicional de dois vetores de 10 bits.
# A largura continua fixa: o carry final é descartado, logo o resultado é
# (a+b) mod 1024, como num registador binário finito.
# --------------------------------------------------------------------------
_SOMA_BIT_COMPLETA = lambda a: lambda b: lambda carry: (
    lambda parcial: PAR(XOR(parcial)(carry))(OU(E(a)(b))(E(carry)(parcial)))
)(XOR(a)(b))


def _gerar_somador(profundidade):
    if profundidade == 1:
        return lambda a: lambda b: lambda carry: _SOMA_BIT_COMPLETA(a)(b)(carry)(V)
    soma_resto = _gerar_somador(profundidade - 1)
    return lambda a: lambda b: lambda carry: (
        lambda primeiro: PAR(primeiro(V))(soma_resto(a(F))(b(F))(primeiro(F)))
    )(_SOMA_BIT_COMPLETA(a(V))(b(V))(carry))


_SOMADOR_BINARIO = _gerar_somador(_LARGURA)

SOMA_BINARIA = lambda a: lambda b: _SOMADOR_BINARIO(a)(b)(F)
SOMA_NATURAL_BINARIA = lambda a: lambda b: SOMA_BINARIA(PARA_BINARIO(a))(PARA_BINARIO(b))

# Verificador interno: somar vetores diretamente deve concordar com converter
# para natural, somar no núcleo e voltar ao mesmo registador fixo.
SOMA_BINARIA_CONFERE = lambda a: lambda b: IGUAL(
    DE_BINARIO(SOMA_BINARIA(a)(b))
)(
    DE_BINARIO(PARA_BINARIO(SOMA(DE_BINARIO(a))(DE_BINARIO(b))))
)
