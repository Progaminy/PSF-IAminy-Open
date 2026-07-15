# ==============================================================================
# ESTRUTURAS ALGÉBRICAS II — Etapas 91 a 100 do PSF-IAminy.
# ==============================================================================
# Lei PSF-IAminy:
#   corpo nasce depois de domínio de integridade; homomorfismo nasce depois
#   de grupo (dos dois lados) e de função (etapas 70-80); subgrupo nasce
#   depois de grupo; classe lateral nasce depois de subgrupo.
#
# Reaproveita, sem redefinir: FUNÇÃO como tupla finita de PAR(a)(f(a))
# (etapas 70-80, relacoes_funcoes_naturais.py) e GRUPO/ANEL (etapas 86-90,
# operacoes_algebricas_naturais.py).
#
# Conceitos permitidos aqui:
#   V/F, igualdade, lógica booleana, domínio finito explícito,
#   tudo o que já nasceu nas etapas 1-90.
# Conceitos proibidos aqui:
#   corpos infinitos, extensões de corpo, espaços vetoriais, módulos,
#   categoria, teoria de Galois, estruturas ainda não construídas.
# ==============================================================================
from .primitivas import V, F
from .logica import E, NAO
from .aritmetica import IGUAL
from .traducao import para_bool
from .relacoes_funcoes_naturais import (
    TODO_FINITO_PURO, EXISTE_FINITO_PURO, APLICAR_FUNCAO_FINITA_PURA, BIJETORA_PURA,
)
from .operacoes_algebricas_naturais import (
    ANEL_INICIAL_PURO, COMUTATIVA_PURA, EXISTE_NEUTRO_PURA, NEUTRO_CONCRETO_PURA,
    GRUPO_PURO, SEMIGRUPO_PURO,
)


# ----------------------------------------------------------------------------
# Etapa 91 — anel comutativo: anel onde o produto também é comutativo.
# ----------------------------------------------------------------------------
def ANEL_COMUTATIVO_PURO(dominio, soma, produto):
    return E(ANEL_INICIAL_PURO(dominio, soma, produto))(COMUTATIVA_PURA(dominio)(produto))


# ----------------------------------------------------------------------------
# Etapa 92 — anel com unidade: existe elemento neutro para o produto
# (diferente do neutro da soma — por isso "unidade", não "zero").
# ----------------------------------------------------------------------------
def ANEL_COM_UNIDADE_PURO(dominio, soma, produto):
    return E(ANEL_INICIAL_PURO(dominio, soma, produto))(EXISTE_NEUTRO_PURA(dominio)(produto))


# ----------------------------------------------------------------------------
# Etapa 93 — domínio de integridade: anel comutativo com unidade, sem
# divisores de zero (a×b=0 ⟹ a=0 ou b=0), e com zero ≠ unidade (exclui o
# anel trivial {0}).
# ----------------------------------------------------------------------------
def SEM_DIVISORES_DE_ZERO_PURA(dominio, soma, produto):
    zero = NEUTRO_CONCRETO_PURA(dominio, soma)
    resultado = V
    for a in dominio:
        for b in dominio:
            produto_zero = IGUAL(produto(a)(b))(zero)
            a_ou_b_zero = para_bool(IGUAL(a)(zero)) or para_bool(IGUAL(b)(zero))
            implicacao = V if (not para_bool(produto_zero) or a_ou_b_zero) else F
            resultado = E(resultado)(implicacao)
    return resultado


def DOMINIO_INTEGRIDADE_PURO(dominio, soma, produto):
    zero = NEUTRO_CONCRETO_PURA(dominio, soma)
    unidade = NEUTRO_CONCRETO_PURA(dominio, produto)
    if zero is None or unidade is None:
        return F
    zero_diferente_unidade = NAO(IGUAL(zero)(unidade))
    return E(
        ANEL_COMUTATIVO_PURO(dominio, soma, produto)
    )(
        E(EXISTE_NEUTRO_PURA(dominio)(produto))(
            E(zero_diferente_unidade)(SEM_DIVISORES_DE_ZERO_PURA(dominio, soma, produto))
        )
    )


# ----------------------------------------------------------------------------
# Etapa 94 — corpo finito inicial: domínio de integridade onde todo
# elemento não-nulo tem inverso multiplicativo. Ex.: Z/5Z é corpo (5 é
# primo); Z/4Z não é (2 não tem inverso multiplicativo mod 4).
# ----------------------------------------------------------------------------
def CORPO_FINITO_PURO(dominio, soma, produto):
    if not para_bool(DOMINIO_INTEGRIDADE_PURO(dominio, soma, produto)):
        return F
    zero = NEUTRO_CONCRETO_PURA(dominio, soma)
    nao_nulos = [x for x in dominio if not para_bool(IGUAL(x)(zero))]
    return GRUPO_PURO(nao_nulos, produto)


# ----------------------------------------------------------------------------
# Etapa 95 — homomorfismo de grupos: f preserva a operação —
# f(a∘b) = f(a)∘f(b) para todo a,b do domínio. `f` é uma função finita
# (tupla de PAR(a)(f(a)), mesmo formato das etapas 70-80).
# ----------------------------------------------------------------------------
def HOMOMORFISMO_GRUPOS_PURO(dominio, op1, op2, f):
    resultado = V
    for a in dominio:
        for b in dominio:
            esquerda = APLICAR_FUNCAO_FINITA_PURA(f, op1(a)(b))
            direita = op2(APLICAR_FUNCAO_FINITA_PURA(f, a))(APLICAR_FUNCAO_FINITA_PURA(f, b))
            resultado = E(resultado)(IGUAL(esquerda)(direita))
    return resultado


# ----------------------------------------------------------------------------
# Etapa 96 — isomorfismo: homomorfismo que também é bijetor.
# ----------------------------------------------------------------------------
def ISOMORFISMO_PURO(dominio, codominio, op1, op2, f):
    return E(
        HOMOMORFISMO_GRUPOS_PURO(dominio, op1, op2, f)
    )(
        BIJETORA_PURA(dominio)(codominio)(f)
    )


# ----------------------------------------------------------------------------
# Etapa 97 — núcleo e imagem de um homomorfismo.
# Núcleo: elementos de D1 que vão para o neutro de D2.
# Imagem: valores de D2 realmente atingidos (já existe IMAGEM_FUNCAO_PURA
# nas etapas 70-80; aqui só nomeamos o caso homomorfismo explicitamente).
# ----------------------------------------------------------------------------
def NUCLEO_HOMOMORFISMO_PURO(dominio, neutro_codominio, f):
    return tuple(a for a in dominio if para_bool(IGUAL(APLICAR_FUNCAO_FINITA_PURA(f, a))(neutro_codominio)))


def IMAGEM_HOMOMORFISMO_PURO(dominio, f):
    imagem = []
    for a in dominio:
        valor = APLICAR_FUNCAO_FINITA_PURA(f, a)
        if not any(para_bool(IGUAL(valor)(v)) for v in imagem):
            imagem.append(valor)
    return tuple(imagem)


# ----------------------------------------------------------------------------
# Etapa 98 — subgrupo: H ⊆ D é subgrupo de (D,op) se H, com a mesma
# operação restrita, também é grupo — não-vazio, contém o neutro de D, e
# GRUPO_PURO(H,op) confirma fechamento+associatividade+inversos dentro de H.
# ----------------------------------------------------------------------------
def SUBGRUPO_PURO(dominio, op, h):
    if not h:
        return F
    neutro_d = NEUTRO_CONCRETO_PURA(dominio, op)
    contem_neutro = any(para_bool(IGUAL(x)(neutro_d)) for x in h)
    if not contem_neutro:
        return F
    return GRUPO_PURO(list(h), op)


# ----------------------------------------------------------------------------
# Etapa 99 — classes laterais de um subgrupo H em G, pela operação `op`.
# Classe lateral à esquerda de a: {a∘h : h ∈ H}.
# ----------------------------------------------------------------------------
def CLASSE_LATERAL_ESQUERDA_PURA(a, h, op):
    classe = []
    for elemento in h:
        valor = op(a)(elemento)
        if not any(para_bool(IGUAL(valor)(v)) for v in classe):
            classe.append(valor)
    return tuple(classe)


def PARTICAO_EM_CLASSES_LATERAIS_PURA(dominio, h, op):
    """Todas as classes laterais distintas de H em `dominio`.

    Nota de correção: a assinatura de cada classe usa `para_int` (o
    valor real) para comparar, não `str()` do objeto Python. Numerais de
    Church são fechos (closures) — dois numerais que representam o MESMO
    valor mas foram construídos por chamadas diferentes são objetos
    Python DIFERENTES, com `str()` diferente (mostra o endereço de
    memória). Comparar por `str()` fazia cada classe lateral parecer
    "nova" mesmo quando repetida, inflando a contagem. `para_int` dá o
    valor verdadeiro e resolve isso.
    """
    from .traducao import para_int

    classes = []
    vistos = set()
    for a in dominio:
        classe = CLASSE_LATERAL_ESQUERDA_PURA(a, h, op)
        assinatura = tuple(sorted(para_int(x) for x in classe))
        if assinatura not in vistos:
            vistos.add(assinatura)
            classes.append(classe)
    return tuple(classes)


# ----------------------------------------------------------------------------
# Etapa 100 — fechamento algébrico inicial: confirma o ciclo completo
# operação → grupo → anel → corpo → homomorfismo → subgrupo.
# ----------------------------------------------------------------------------
def FECHAMENTO_ALGEBRICO_INICIAL_PURO(dominio, soma, produto):
    grupo_aditivo = GRUPO_PURO(dominio, soma)
    anel = ANEL_COMUTATIVO_PURO(dominio, soma, produto)
    dominio_e_subgrupo_de_si_mesmo = SUBGRUPO_PURO(dominio, soma, tuple(dominio))
    return E(grupo_aditivo)(E(anel)(dominio_e_subgrupo_de_si_mesmo))
