"""Espaço combinatório de sequências: posição de uma sequência de símbolos
dentro do total de arranjos com repetição de comprimento fixo sobre um
alfabeto de tamanho `k` -- e o caminho inverso, decompor uma posição de
volta em sequência de símbolos.

Fundamento formal já provado: `nucleo/combinatoria_natural.py::
ESCOLHAS_ORDENADAS_COM_REPETICAO_PURO` (Etapa 39) já prova que o total de
sequências de comprimento `r` sobre `n` símbolos é POT(n)(r) = n^r --
"arranjo com repetição", `n` opções em cada uma das `r` posições.
`testes/test_espaco_combinatorio_palavras.py` confere este módulo contra
essa versão pura para um alfabeto pequeno (a via de Church só é viável em
escala de brinquedo -- ver aviso em `nucleo/combinatoria.py`).

**Por que este módulo usa inteiro nativo do Python, não a camada
"escolar nativa" (`aritmetica_escolar_nativa.py`)**: esta é uma camada de
TRADUÇÃO/ENDEREÇAMENTO -- localizar ou reconstruir uma sequência dentro de
um total já provado, não provar um fato aritmético novo (mesmo papel que
`nucleo/traducao.py` já assume como "o ÚNICO ponto de contacto com tipos
nativos"). Tentar fazer isso pela camada escolar nativa foi tentado e
mediu-se, na prática, que trava: `dividir_com_resto` chama `subtrair`, que
chama `predecessor`, que **busca por sucessão a partir de zero a cada
chamada** (não é `n - 1`) -- o próprio `nucleo/contas_armadas.py` já
registra essa armadilha ("decompor 9801 assim passa de um minuto"), e a
posição de uma palavra de só 3 letras (~12500, bem menor que 9801) já
reproduziu o mesmo travamento aqui (medido, não suposto). `contas_armadas.
py::digitos()` já resolve isso da mesma forma que este módulo: lendo o
numeral nativamente (`str(n)`/`divmod`) para a decomposição externa,
reservando a camada escolar nativa só para a aritmética de coluna sobre
dígitos únicos.

Cada sequência de símbolos de comprimento `r` sobre um alfabeto de `k`
símbolos é, literalmente, um numeral em base `k` com `r` dígitos.
"""
from __future__ import annotations

_LIMITE_SEGURO_TOTAL_SEQUENCIAS = 10**15


def _validar_natural(valor: int, nome: str) -> None:
    if not isinstance(valor, int) or valor < 0:
        raise ValueError(f"{nome} deve ser natural finito")


def _verificar_escala_segura(tamanho_alfabeto: int, comprimento: int) -> None:
    """Pré-checagem barata (usa `**` nativo só como estimativa de tamanho,
    nunca como o cálculo endereçado em si) para recusar cedo qualquer
    pedido cujo total ultrapasse o limite de sanidade -- nunca calcular o
    total gigante primeiro para só depois perceber que era grande demais."""
    if tamanho_alfabeto > 1 and comprimento > 200:
        raise ValueError(f"comprimento {comprimento} claramente fora de qualquer escala prática")
    estimativa = tamanho_alfabeto**comprimento
    if estimativa > _LIMITE_SEGURO_TOTAL_SEQUENCIAS:
        raise ValueError(
            f"comprimento {comprimento} sobre alfabeto de {tamanho_alfabeto} dá {estimativa} sequências -- "
            f"acima do limite de sanidade ({_LIMITE_SEGURO_TOTAL_SEQUENCIAS}). Use comprimento menor."
        )


def total_sequencias(tamanho_alfabeto: int, comprimento: int) -> int:
    """Quantas sequências de `comprimento` símbolos existem sobre um
    alfabeto de `tamanho_alfabeto` símbolos, com repetição e ordem
    importando -- arranjo com repetição, Etapa 39: k^r."""
    _validar_natural(tamanho_alfabeto, "tamanho_alfabeto")
    _validar_natural(comprimento, "comprimento")
    _verificar_escala_segura(tamanho_alfabeto, comprimento)
    if tamanho_alfabeto == 0 and comprimento > 0:
        return 0
    return tamanho_alfabeto**comprimento


def posicao_da_sequencia(indices: tuple[int, ...], tamanho_alfabeto: int) -> int:
    """Posição (0-based) de uma sequência de índices de símbolo (cada um em
    [0, tamanho_alfabeto)) dentro da ordem lexicográfica de todas as
    sequências do mesmo comprimento -- lê a sequência como um numeral em
    base `tamanho_alfabeto`, dígito mais significativo primeiro (método de
    Horner: posicao = posicao*base + próximo_dígito)."""
    _validar_natural(tamanho_alfabeto, "tamanho_alfabeto")
    _verificar_escala_segura(tamanho_alfabeto, len(indices))
    for indice in indices:
        if not (0 <= indice < tamanho_alfabeto):
            raise ValueError(f"índice {indice} fora do alfabeto de tamanho {tamanho_alfabeto}")
    posicao = 0
    for indice in indices:
        posicao = posicao * tamanho_alfabeto + indice
    return posicao


def sequencia_da_posicao(posicao: int, tamanho_alfabeto: int, comprimento: int) -> tuple[int, ...]:
    """Caminho inverso: decompõe uma posição em `comprimento` índices de
    símbolo (dígito mais significativo primeiro) -- extrai dígito a dígito
    por `divmod` nativo (menos significativo primeiro) e depois inverte,
    mesma técnica de conversão de base que `contas_armadas.py::digitos()`
    já usa para a mesma razão (ver docstring do módulo)."""
    _validar_natural(posicao, "posicao")
    total = total_sequencias(tamanho_alfabeto, comprimento)
    if posicao >= total:
        raise ValueError(
            f"posição {posicao} fora do intervalo -- só existem {total} sequências de comprimento {comprimento}"
        )
    digitos_lsb_primeiro: list[int] = []
    restante = posicao
    for _ in range(comprimento):
        restante, resto = divmod(restante, tamanho_alfabeto)
        digitos_lsb_primeiro.append(resto)
    digitos_lsb_primeiro.reverse()
    return tuple(digitos_lsb_primeiro)
