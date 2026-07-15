"""Reconhecimento de intenções naturais do PSF-IAminy.

Este módulo não usa LLM nem dependência externa. Ele transforma frases livres em
intenções por construção simples: normalização, procura de verbos de pedido,
sinónimos frequentes e mapeamento explícito entre temas e conhecimentos já
construídos.

Regra PSF: reconhecer intenção não é fingir entendimento infinito. Quando um
tema ainda não tem destino construído, o módulo devolve intenção de fronteira.
"""
from __future__ import annotations

from dataclasses import dataclass

from lingua_portuguesa.normalizacao import sem_acentos


@dataclass(frozen=True, slots=True)
class IntencaoNatural:
    nome: str
    confianca: float
    alvo: str | None = None
    area: str | None = None
    codigo: str | None = None
    nivel_psf: int | None = None
    motivo: str = ""


def _norm(texto: str) -> str:
    texto = sem_acentos(texto).casefold()
    for sinal in "?!.,;:\n\t()[]{}\"'":
        texto = texto.replace(sinal, " ")
    return " ".join(texto.split())


_VERBOS_AULA = (
    "me ensina", "ensina", "ensinar", "quero aprender", "quero estudar",
    "quero uma aula", "dar aula", "da aula", "dá aula", "explica", "explique",
    "explicar", "como funciona", "fala de", "fale de", "fala sobre", "fale sobre",
    "teoria de", "teoria do", "teoria da", "nao entendi", "não entendi",
    "nao percebi", "não percebi", "mais simples", "explica melhor", "desmonta",
    "passo a passo", "do zero", "aula humana", "me mostra", "mostra",
)

_PEDIDOS_FUTUROS = (
    "conceito futuro", "conceitos futuros", "nao construido", "não construído",
    "ainda nao construido", "ainda não construído", "ainda nao sabe", "ainda não sabe",
    "o que falta", "fronteira", "limite atual", "proxima fronteira", "próxima fronteira",
    "futuro nao construido", "futuro não construído",
)

_PEDIDOS_INFINITO = (
    "matematica infinita", "matemática infinita", "infinito real", "do zero ao infinito",
    "ensinar tudo", "tudo que sabe", "todo conhecimento", "matematica sem fim",
    "matemática sem fim", "sequencia infinita", "sequência infinita",
)

_PEDIDOS_MELHORIA = (
    "melhorar motor", "melhorar motores", "aprimorar motor", "aprimorar motores",
    "deve melhorar", "o que deve melhorar", "ver melhorias", "auditar motores",
    "conversa fluida", "pedidos naturais", "aula humana perfeita", "portugues amplo",
    "português amplo", "dicionario grande", "dicionário grande",
)

_PEDIDOS_PORTUGUES = (
    "portugues", "português", "dicionario", "dicionário", "vocabulario", "vocabulário",
    "lexico", "léxico", "gramatica", "gramática", "sinonimo", "sinônimo", "antonimo", "antônimo",
)

# Pacotes humanos fixos. Mantidos explícitos para não inventar mapa.
_TOPICOS_PACOTES: tuple[tuple[tuple[str, ...], str, str], ...] = (
    (("adicao", "adição", "soma", "somar", "juntar", "mais"), "matematica", "MAT-006"),
    (("subtracao", "subtração", "subtrair", "retirar", "tirar", "menos"), "matematica", "MAT-007"),
    (("multiplicacao", "multiplicação", "multiplicar", "vezes", "grupos iguais"), "matematica", "MAT-014"),
    (("tabuada", "multiplicar por dois", "multiplicar por cinco", "multiplicar por dez"), "matematica", "MAT-015"),
    (("divisao", "divisão", "dividir", "repartir", "partes iguais"), "matematica", "MAT-016"),
    (("dobro", "metade"), "matematica", "MAT-017"),
    (("contar", "contagem", "numero", "número"), "matematica", "MAT-004"),
    (("ordem", "primeiro", "ultimo", "último", "sequencia", "sequência"), "matematica", "MAT-005"),
    (("substantivo", "verbo", "adjetivo", "classes de palavras"), "portugues", "POR-011"),
    (("frase",), "portugues", "POR-007"),
    (("oracao", "oração", "sujeito", "predicado"), "portugues", "POR-008"),
    (("texto", "paragrafo", "parágrafo"), "portugues", "POR-015"),
    (("sinonimo", "sinônimo", "antonimo", "antônimo"), "portugues", "POR-014"),
    (("pontuacao", "pontuação", "virgula", "vírgula", "ponto"), "portugues", "POR-017"),
)

# Temas técnicos do trilho PSF-K. O número aponta para a etapa/nível onde o
# tema começa a existir no conhecimento construído.
_TOPICOS_PSF: tuple[tuple[tuple[str, ...], int], ...] = (
    (("divisibilidade", "divisor", "multiplo", "múltiplo"), 3),
    (("mdc", "maior divisor comum"), 4),
    (("diferenca controlada", "diferença controlada"), 5),
    (("euclides", "algoritmo de euclides"), 9),
    (("primo", "primalidade", "numero primo", "número primo"), 10),
    (("fatoracao", "fatoração", "decomposicao", "decomposição"), 11),
    (("teorema fundamental", "tfa"), 13),
    (("bezout", "bézout"), 17),
    (("congruencia", "congruência", "restos"), 22),
    (("modular", "aritmetica modular", "aritimética modular", "aritmética modular"), 25),
    (("fermat",), 29),
    (("euler", "phi"), 30),
    (("combinatoria", "combinatória", "contagem"), 36),
    (("catalan",), 53),
    (("stirling",), 54),
    (("bell",), 55),
    (("particoes", "partições"), 56),
    (("relacao", "relação", "relacoes", "relações"), 61),
    (("funcao", "função", "funcoes", "funções"), 70),
    (("algebra", "álgebra", "grupo", "anel", "corpo"), 81),
    (("polinomio", "polinômio"), 101),
    (("vetor", "matriz", "algebra linear", "álgebra linear"), 104),
    (("grafo", "grafos"), 111),
    (("logica", "lógica", "modelo", "prova"), 341),
    (("computabilidade", "maquina", "máquina"), 401),
    (("gramatica formal", "gramática formal"), 441),
    (("automato", "autômato", "automatos", "autômatos"), 521),
    (("linguagem regular", "regular"), 561),
    (("complexidade",), 801),
    (("analise discreta", "análise discreta", "aproximacao", "aproximação"), 841),
    (("topologia",), 881),
    (("probabilidade", "medida"), 921),
    (("estatistica", "estatística", "dados"), 961),
    (("otimizacao", "otimização", "modelo finito"), 991),
    (("sequencia", "sequência", "calculo psf", "cálculo psf"), 1031),
    (("zeta", "riemann", "funcao zeta", "função zeta"), 1032),
)


def classificar(texto: str) -> IntencaoNatural:
    normal = _norm(texto)
    if not normal:
        return IntencaoNatural("vazio", 0.0)

    if any(_norm(p) in normal for p in _PEDIDOS_MELHORIA):
        return IntencaoNatural(
            "melhoria_motores",
            0.88,
            alvo="motores",
            motivo="pedido para auditar e aprimorar motores do sistema",
        )

    if any(_norm(p) in normal for p in _PEDIDOS_FUTUROS):
        return IntencaoNatural(
            "fronteira_conhecimento",
            0.9,
            alvo="conceitos futuros",
            motivo="pedido sobre limite/topo do conhecimento construído",
        )

    if any(_norm(p) in normal for p in _PEDIDOS_INFINITO):
        return IntencaoNatural(
            "matematica_infinita_real",
            0.9,
            alvo="zero ao infinito",
            motivo="pedido sobre sequência aberta de conhecimento",
        )

    pedido_aula = any(_norm(v) in normal for v in _VERBOS_AULA)
    if pedido_aula:
        for chaves, area, codigo in _TOPICOS_PACOTES:
            if any(_norm(chave) in normal for chave in chaves):
                return IntencaoNatural(
                    "aula_pacote_natural",
                    0.86,
                    alvo=chaves[0],
                    area=area,
                    codigo=codigo,
                    motivo="pedido natural ligado a pacote fixo",
                )
        for chaves, nivel in _TOPICOS_PSF:
            if any(_norm(chave) in normal for chave in chaves):
                return IntencaoNatural(
                    "aula_psf_natural",
                    0.84,
                    alvo=chaves[0],
                    nivel_psf=nivel,
                    motivo="pedido natural ligado ao trilho PSF-K",
                )
        if any(_norm(p) in normal for p in _PEDIDOS_PORTUGUES):
            return IntencaoNatural("aula_portugues_natural", 0.75, alvo="português", area="portugues")

    # Mesmo sem verbo de aula, perguntas do tipo "zeta?", "divisibilidade?"
    # podem ser curiosidade teórica. A confiança é menor para não atropelar
    # comandos específicos já tratados em dialogo.py.
    for chaves, nivel in _TOPICOS_PSF:
        if any(_norm(chave) in normal for chave in chaves):
            return IntencaoNatural("tema_psf", 0.62, alvo=chaves[0], nivel_psf=nivel)

    if any(_norm(p) in normal for p in _PEDIDOS_PORTUGUES):
        return IntencaoNatural("tema_portugues", 0.56, alvo="português", area="portugues")

    return IntencaoNatural("desconhecida", 0.0)
