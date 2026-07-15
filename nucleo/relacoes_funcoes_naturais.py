# ==============================================================================
# RELAÇÕES E FUNÇÕES NATURAIS — Etapas 61 a 80 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   função nasce depois de relação binária; ordem nasce depois de relação;
#   bijeção nasce depois de função, injetividade e sobrejetividade.
#
# Este módulo é uma camada operacional finita: uma relação é uma tupla finita
# de pares PSF (PAR(a)(b)). A estrutura finita permite testar propriedades sem
# invocar conjuntos avançados, topologia, análise, cardinalidade ou álgebra.
#
# Conceitos permitidos aqui:
#   V/F, PAR, igualdade/ordem dos naturais, lógica booleana e etapas anteriores.
# Conceitos proibidos aqui:
#   divisão, módulo, primalidade, fatoração, cardinalidade infinita, análise.
# ==============================================================================
from .primitivas import V, F, PAR
from .logica import E, OU, IMPLICA
from .aritmetica import IGUAL
from .traducao import para_bool


# ----------------------------------------------------------------------------
# Ferramentas locais de leitura de par. Não são novos axiomas.
# ----------------------------------------------------------------------------
PRIMEIRO = lambda p: p(V)
SEGUNDO = lambda p: p(F)
PAR_ORDENADO_PURO = lambda a: lambda b: PAR(a)(b)
RELACAO_BINARIA_FINITA_PURA = lambda *pares: tuple(pares)
DOMINIO_FINITO_PURO = lambda *elementos: tuple(elementos)


# ----------------------------------------------------------------------------
# Auxiliares booleanos sobre estruturas finitas.
# Retornam booleanos PSF (V/F); usam laços Python apenas para percorrer a
# coleção finita operacional. A decisão matemática permanece em IGUAL/E/OU.
# ----------------------------------------------------------------------------
def TODO_FINITO_PURO(elementos, predicado):
    resultado = V
    for elemento in elementos:
        resultado = E(resultado)(predicado(elemento))
    return resultado


def EXISTE_FINITO_PURO(elementos, predicado):
    resultado = F
    for elemento in elementos:
        resultado = OU(resultado)(predicado(elemento))
    return resultado


# ----------------------------------------------------------------------------
# Etapas 61 e 62 — relação binária e pertencimento relacional.
# ----------------------------------------------------------------------------
PAR_IGUAL_PURO = lambda p: lambda q: E(
    IGUAL(PRIMEIRO(p))(PRIMEIRO(q))
)(
    IGUAL(SEGUNDO(p))(SEGUNDO(q))
)

PERTENCE_PAR_RELACAO_PURA = lambda par: lambda relacao: EXISTE_FINITO_PURO(
    relacao,
    lambda p: PAR_IGUAL_PURO(p)(par),
)

PERTENCE_RELACAO_PURA = lambda a: lambda b: lambda relacao: PERTENCE_PAR_RELACAO_PURA(
    PAR(a)(b)
)(relacao)


# ----------------------------------------------------------------------------
# Etapas 63 a 65 — reflexividade, simetria e transitividade.
# ----------------------------------------------------------------------------
REFLEXIVA_PURA = lambda dominio: lambda relacao: TODO_FINITO_PURO(
    dominio,
    lambda x: PERTENCE_RELACAO_PURA(x)(x)(relacao),
)

SIMETRICA_PURA = lambda relacao: TODO_FINITO_PURO(
    relacao,
    lambda p: PERTENCE_RELACAO_PURA(SEGUNDO(p))(PRIMEIRO(p))(relacao),
)


def TRANSITIVA_PURA(relacao):
    resultado = V
    for p in relacao:
        for q in relacao:
            antecedente = IGUAL(SEGUNDO(p))(PRIMEIRO(q))
            consequente = PERTENCE_RELACAO_PURA(PRIMEIRO(p))(SEGUNDO(q))(relacao)
            resultado = E(resultado)(IMPLICA(antecedente)(consequente))
    return resultado


# ----------------------------------------------------------------------------
# Etapas 66 e 67 — equivalência e classes de equivalência gerais.
# ----------------------------------------------------------------------------
EQUIVALENCIA_PURA = lambda dominio: lambda relacao: E(
    REFLEXIVA_PURA(dominio)(relacao)
)(
    E(SIMETRICA_PURA(relacao))(TRANSITIVA_PURA(relacao))
)


def CLASSE_EQUIVALENCIA_PURA(x, dominio, relacao):
    classe = []
    for y in dominio:
        if para_bool(PERTENCE_RELACAO_PURA(x)(y)(relacao)):
            classe.append(y)
    return tuple(classe)


# ----------------------------------------------------------------------------
# Etapas 68 e 69 — antissimetria, ordem parcial e ordem total.
# ----------------------------------------------------------------------------
def ANTISSIMETRICA_PURA(relacao):
    resultado = V
    for p in relacao:
        a = PRIMEIRO(p)
        b = SEGUNDO(p)
        volta = PERTENCE_RELACAO_PURA(b)(a)(relacao)
        igualdade = IGUAL(a)(b)
        resultado = E(resultado)(IMPLICA(volta)(igualdade))
    return resultado


ORDEM_PARCIAL_PURA = lambda dominio: lambda relacao: E(
    REFLEXIVA_PURA(dominio)(relacao)
)(
    E(ANTISSIMETRICA_PURA(relacao))(TRANSITIVA_PURA(relacao))
)


def ORDEM_TOTAL_PURA(dominio, relacao):
    comparabilidade = V
    for x in dominio:
        for y in dominio:
            xy = PERTENCE_RELACAO_PURA(x)(y)(relacao)
            yx = PERTENCE_RELACAO_PURA(y)(x)(relacao)
            comparabilidade = E(comparabilidade)(OU(xy)(yx))
    return E(ORDEM_PARCIAL_PURA(dominio)(relacao))(comparabilidade)


# ----------------------------------------------------------------------------
# Etapas 70 e 71 — função como relação especial e aplicação finita.
# Uma função total sobre um domínio finito tem exatamente uma imagem para cada x.
# ----------------------------------------------------------------------------
def _mesma_entrada(p, q):
    return IGUAL(PRIMEIRO(p))(PRIMEIRO(q))


def _mesma_saida(p, q):
    return IGUAL(SEGUNDO(p))(SEGUNDO(q))


def FUNCIONAL_PURA(relacao):
    resultado = V
    for p in relacao:
        for q in relacao:
            resultado = E(resultado)(IMPLICA(_mesma_entrada(p, q))(_mesma_saida(p, q)))
    return resultado


def TOTAL_SOBRE_DOMINIO_PURA(dominio, relacao):
    return TODO_FINITO_PURO(
        dominio,
        lambda x: EXISTE_FINITO_PURO(relacao, lambda p: IGUAL(PRIMEIRO(p))(x)),
    )


FUNCAO_RELACAO_PURA = lambda dominio: lambda relacao: E(
    FUNCIONAL_PURA(relacao)
)(
    TOTAL_SOBRE_DOMINIO_PURA(dominio, relacao)
)


def APLICAR_FUNCAO_FINITA_PURA(relacao, x):
    for p in relacao:
        if para_bool(IGUAL(PRIMEIRO(p))(x)):
            return SEGUNDO(p)
    return F


# ----------------------------------------------------------------------------
# Etapas 72 a 74 — função identidade, função constante e composição.
# ----------------------------------------------------------------------------
def FUNCAO_IDENTIDADE_PURA(dominio):
    return tuple(PAR(x)(x) for x in dominio)


def FUNCAO_CONSTANTE_PURA(dominio, c):
    return tuple(PAR(x)(c) for x in dominio)


def COMPOSICAO_FUNCOES_FINITA_PURA(g, f, dominio):
    return tuple(PAR(x)(APLICAR_FUNCAO_FINITA_PURA(g, APLICAR_FUNCAO_FINITA_PURA(f, x))) for x in dominio)


# ----------------------------------------------------------------------------
# Etapas 75 a 77 — injeção, sobrejeção e bijeção.
# ----------------------------------------------------------------------------
def INJETORA_PURA(dominio, relacao):
    resultado = V
    for x in dominio:
        for y in dominio:
            fx = APLICAR_FUNCAO_FINITA_PURA(relacao, x)
            fy = APLICAR_FUNCAO_FINITA_PURA(relacao, y)
            resultado = E(resultado)(IMPLICA(IGUAL(fx)(fy))(IGUAL(x)(y)))
    return E(FUNCAO_RELACAO_PURA(dominio)(relacao))(resultado)


def SOBREJETORA_PURA(codominio, relacao):
    return TODO_FINITO_PURO(
        codominio,
        lambda y: EXISTE_FINITO_PURO(relacao, lambda p: IGUAL(SEGUNDO(p))(y)),
    )


BIJETORA_PURA = lambda dominio: lambda codominio: lambda relacao: E(
    INJETORA_PURA(dominio, relacao)
)(
    SOBREJETORA_PURA(codominio, relacao)
)


# ----------------------------------------------------------------------------
# Etapas 78 e 79 — inversa relacional, imagem e pré-imagem.
# ----------------------------------------------------------------------------
def INVERSA_RELACAO_PURA(relacao):
    return tuple(PAR(SEGUNDO(p))(PRIMEIRO(p)) for p in relacao)


def IMAGEM_FUNCAO_PURA(relacao):
    imagem = []
    for p in relacao:
        y = SEGUNDO(p)
        ja_existe = F
        for z in imagem:
            ja_existe = OU(ja_existe)(IGUAL(y)(z))
        if not para_bool(ja_existe):
            imagem.append(y)
    return tuple(imagem)


def PREIMAGEM_FUNCAO_PURA(y, dominio, relacao):
    pre = []
    for x in dominio:
        if para_bool(IGUAL(APLICAR_FUNCAO_FINITA_PURA(relacao, x))(y)):
            pre.append(x)
    return tuple(pre)


# ----------------------------------------------------------------------------
# Etapa 80 — fechamento relacional-funcional inicial.
# ----------------------------------------------------------------------------
def FECHAMENTO_RELACOES_FUNCOES_PURO(dominio):
    identidade = FUNCAO_IDENTIDADE_PURA(dominio)
    return E(
        REFLEXIVA_PURA(dominio)(identidade)
    )(
        FUNCAO_RELACAO_PURA(dominio)(identidade)
    )
