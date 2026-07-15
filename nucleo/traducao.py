# ==============================================================================
# CAMADA DE TRADUÇÃO — o ÚNICO ponto de contato com tipos nativos do Python.
# ==============================================================================
# Nada aqui participa do processamento matemático. Serve só para
# converter valores para dentro e para fora do núcleo formal, para que
# humanos (e testes) consigam ler o resultado.
from .primitivas import ZERO, S, V, F
from .racionais import NUM, DEN
from .inteiros import INTEIRO, PARTE_POS, PARTE_NEG, EH_NEGATIVO


def de_int(k: int):
    """Converte um inteiro Python >= 0 num numeral de Church (entrada)."""
    if k < 0:
        raise ValueError("Numerais de Church não representam negativos.")
    numeral = ZERO
    for _ in range(k):
        numeral = S(numeral)
    return numeral


def para_bool(b) -> bool:
    """Converte booleano de Church para bool nativo (saída)."""
    return b(True)(False)


def para_int(n) -> int:
    """Converte numeral de Church para int nativo (saída)."""
    return n(lambda x: x + 1)(0)


def para_rac(r) -> str:
    """Converte um racional (par de numerais) para string 'num/den'."""
    return f"{para_int(NUM(r))}/{para_int(DEN(r))}"


def para_int_assinado(z) -> int:
    """Converte um inteiro assinado (par pos/neg) para int nativo (saída)."""
    p = para_int(PARTE_POS(z))
    n = para_int(PARTE_NEG(z))
    return p - n


def para_lista(lst) -> list:
    """Converte uma lista tipo-PAR terminada em F (cons/nil) para list.
    Estrutura: cons(cabeça, cauda) = PAR(cabeça)(cauda); lista vazia = F.
    """
    elementos = []
    atual = lst
    while atual is not F:
        cabeca = atual(V)
        elementos.append(para_int(cabeca))
        atual = atual(F)
    return elementos


def para_bits(vetor, largura: int = 10) -> str:
    """Converte um vetor de bits de largura fixa (nucleo.binario) para
    string '0b...', MSB primeiro para leitura humana (o vetor em si é
    armazenado LSB primeiro — ver nucleo/binario.py)."""
    bits = []
    atual = vetor
    for i in range(largura):
        if i < largura - 1:
            bit_church = atual(V)
            atual = atual(F)
        else:
            bit_church = atual
        bits.append("1" if bit_church(True)(False) else "0")
    return "0b" + "".join(reversed(bits))
