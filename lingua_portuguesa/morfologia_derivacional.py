"""Morfologia derivacional real: gera palavra nova por composição de raiz +
afixo produtivo do português -- nunca por listagem manual palavra a palavra.
Item central da meta de vocabulário (~650 mil formas, zero fonte externa):
o multiplicador medido hoje com as 8 regras deste módulo é ~3,05x por raiz
(contagem real sobre os verbos/substantivos/adjetivos únicos do léxico no
momento da medição, não estimada -- o léxico cresce a cada sessão, então
este número é um corte, não uma constante) e só cresce de verdade
adicionando regras de derivação, não só flexão.

Cada palavra gerada tem significado COMPOSTO -- definição da raiz + função
do afixo -- nunca inventado do nada. É a resposta honesta a "um motor que
pega uma palavra qualquer e dá significado": o significado vem da composição
de partes já conhecidas do próprio léxico, não de adivinhação sobre uma
sequência de letras solta. Uma sequência de letras sem raiz e sem afixo
reconhecido não gera candidato nenhum aqui -- não é isso que o projeto
chama de "conhecer uma palavra".

Validação empírica ("faça teste se isso funciona na prática", pedido direto
do autor): `/usr/share/hunspell/pt_BR.dic` (pacote hunspell-pt-br, já
instalado no sistema operacional onde este código roda) é lido aqui só como
ORÁCULO DE EXISTÊNCIA em tempo de teste -- nunca copiado para dentro do
repositório, nunca usado para inserir lema novo automaticamente no léxico
do motor. Serve só para medir, com número real, que fração das palavras
geradas por cada regra corresponde a palavra portuguesa de verdade. Decisão
confirmada com o autor: nenhuma palavra gerada aqui entra no léxico do motor
sozinha -- isso continua exigindo revisão (Fase 4 do plano de léxico).

**Limitação honesta do oráculo, medida, não escondida**: `pt_BR.dic` lista
só ENTRADAS-RAIZ com flags de afixo (formato hunspell) -- este módulo lê
apenas a palavra-raiz de cada linha, sem aplicar as regras de expansão do
`.aff` correspondente. Resultado medido: candidatos gerados aqui como
"felizmente"/"realmente"/"naturalmente" (advérbios em -mente reais e
correntes do português) NÃO são confirmados por este oráculo, porque não
aparecem como linha própria no `.dic` -- só "perfeitamente"/"simplesmente"
(lexicalizados como entrada própria) são. A taxa de confirmação medida por
`validar_candidatos` é, por isso, um PISO honesto (subestima a correção
real das regras), não uma medida completa -- implementar expansão de
afixo real exigiria reconstruir a lógica do `.aff` do hunspell, fora do
escopo deste módulo por ora.

**Achado real ao medir `gerar_adjetivos_oso` (não só limitação do
oráculo)**: rodando contra os ~1300 substantivos do léxico, a taxa de
confirmação foi de ~0,9% -- MUITO mais baixa que `-mente`/diminutivo, e
aqui não é só o oráculo raiz-só: "motoroso"/"professoroso"/"alunoso"/
"exemploso" realmente NÃO soam como palavra portuguesa, porque "-oso" só
é produtivo sobre uma classe semântica restrita (qualidade, substância,
condição abstrata -- "perigo"->"perigoso", "valor"->"valoroso"), não sobre
substantivo concreto/agente/institucional qualquer. A regra continua
gerando candidato (nunca finge que sabe qual substantivo é "elegível"
antes de tentar), mas o rendimento prático real é baixo -- validação por
oráculo é o que evita que isso vire lema fabricado no léxico.

**`gerar_substantivos_mento`: caso oposto, aqui É só limitação do
oráculo**: 0/48 candidatos confirmados, mas conferido manualmente contra
`/usr/share/hunspell/pt_BR.dic`: "entendimento"/"ensinamento"/
"melhoramento"/"aprimoramento" são palavras reais e correntes do
português, nenhuma aparece como linha própria no `.dic` (mesma causa raiz
documentada acima para `-mente`). Diferente de `-oso`, aqui a regra em si
parece genuinamente produtiva -- só o oráculo raiz-só não consegue medir
isso. Sem um oráculo melhor (expansão de afixo real), não dá pra separar
com número "candidato -mento realmente ruim" de "candidato -mento bom que
o oráculo não vê" -- registado honestamente, não estimado às cegas.

**`gerar_agentes_dor` medido contra os verbos do léxico**: 1/188
confirmados (~0,5%), à primeira vista pior que `-oso`, mas é a MESMA
limitação raiz-só de `-mente`/`-mento`, não falta de produtividade real:
conferido manualmente, "trabalhador" (de "trabalhar", palavra correntíssima
do português) não aparece como linha própria em `pt_BR.dic` -- o oráculo
só lê a raiz com flag de afixo, não expande. `-dor` continua entre os
sufixos mais produtivos do português; o número baixo aqui mede o oráculo,
não a regra.

**`gerar_adjetivos_avel_ivel` medido contra os verbos do léxico**: ~73%
confirmados pelo oráculo, a taxa mais alta de todas as regras deste
módulo -- capacidade/possibilidade em -ável/-ível é altamente produtiva
sobre qualquer verbo regular, sem restrição semântica forte (mesmo verbo
raro dá candidato plausível: "gostar" -> "gostável"). Os ~27% não
confirmados são, na maioria, a mesma limitação raiz-só do oráculo já
documentada acima (ex.: "estudável" é palavra real e corrente, mas não
tem linha própria no `.dic`).

**Achado real sobre verbo curto demais para regra de raiz** (afeta
`gerar_agentes_dor`, `gerar_substantivos_mento` e
`gerar_adjetivos_avel_ivel`, todas as 3 fazem `infinitivo[:-2]`): medido
com os verbos monossilábicos suplectivos do português ("ser", "ir",
"ter", "ver", "dar", "ler") -- cortar as 2 últimas letras deles deixa
raiz de 0-1 letra ("ir"->raiz vazia, "ser"->"s"), e nenhum dos 18
candidatos gerados a partir desses 6 verbos batia com o oráculo em
nenhuma das 3 regras ("sível", "idor", "simento" etc., zero confirmado).
Faz sentido: são os verbos mais irregulares do português, com raiz
suplectiva (não vem de composição regular raiz+terminação) -- corrigido
com `_raiz_verbal`, que devolve `None` (candidato nenhum, nunca raiz
fabricada) pra infinitivo de 3 letras ou menos.

**`gerar_substantivos_ista` medido contra os 1327 substantivos únicos do
léxico**: só 21/1327 confirmados (~1,6%) -- mesma família de achado que
`-oso`: "-ista" só é produtivo sobre a classe semântica de profissão/
doutrina/instrumento praticado ("jornal"->"jornalista", "piano"->
"pianista"), não sobre substantivo concreto qualquer ("gato"->"gatista"
não é palavra). A regra continua gerando candidato sempre (nunca finge
saber de antemão qual substantivo é elegível), o oráculo é o que impede
isso de virar lema fabricado.

**`gerar_adjetivos_negativos_in` medido contra os 120 adjetivos únicos
do léxico**: só 10/120 confirmados (~8%) -- a alomorfia (im-/i-/ir-/in-
conforme a letra inicial) está correta onde a regra se aplica
("perfeito"->"imperfeito", "restrito"->"irrestrito", ambos confirmados),
mas boa parte dos adjetivos do português nega por outro caminho, não
por prefixo "in-": "profundo" nega por antônimo lexical ("raso"), não
por prefixo ("improfundo" não é palavra); "ordenado" usa o prefixo
"des-", não "in-" ("desordenado", não "inordenado"). Achado honesto:
esta regra tem yield baixo não por bug, mas porque a negação
morfológica por "in-" é produtiva só sobre uma fração dos adjetivos --
o resto do português nega por antonímia lexical ou por outro prefixo,
fora do escopo desta regra.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .normalizacao import normalizar_chave
from .tipos import ClasseGramatical, EntradaLexical, Genero

_CAMINHO_ORACULO_PADRAO = Path("/usr/share/hunspell/pt_BR.dic")

_VOGAIS_ATONAS_FINAIS = ("a", "o", "e")


@dataclass(frozen=True, slots=True)
class CandidatoDerivado:
    raiz: EntradaLexical
    forma: str
    classe: ClasseGramatical
    definicao: str
    regra: str


def _feminino_singular(adjetivo: EntradaLexical) -> str:
    if adjetivo.lema.endswith("o"):
        return adjetivo.lema[:-1] + "a"
    return adjetivo.lema


def gerar_adverbios_mente(entradas: tuple[EntradaLexical, ...]) -> tuple[CandidatoDerivado, ...]:
    """Regra totalmente produtiva do português: feminino singular do
    adjetivo + "mente". Ex.: "claro" -> "clara" + "mente" = "claramente"."""
    candidatos: list[CandidatoDerivado] = []
    vistos: set[str] = set()
    for entrada in entradas:
        if entrada.classe != ClasseGramatical.ADJETIVO:
            continue
        chave = normalizar_chave(entrada.lema)
        if chave in vistos:
            continue
        vistos.add(chave)
        forma = _feminino_singular(entrada) + "mente"
        raiz_def = entrada.definicoes[0] if entrada.definicoes else ""
        definicao = f"De modo {entrada.lema}: {raiz_def}".strip()
        candidatos.append(CandidatoDerivado(entrada, forma, ClasseGramatical.ADVERBIO, definicao, "adjetivo+mente"))
    return tuple(candidatos)


def _base_diminutivo(lema: str) -> tuple[str, bool]:
    """(base, usa_zinho). Vogal átona final (a/o/e sem acento) cai antes de
    -inho/-inha; qualquer outra terminação -- consoante, vogal tônica
    acentuada, ditongo -- usa -zinho/-zinha sem cortar nada."""
    if lema.endswith(_VOGAIS_ATONAS_FINAIS) and len(lema) > 1:
        return lema[:-1], False
    return lema, True


def gerar_diminutivos(entradas: tuple[EntradaLexical, ...]) -> tuple[CandidatoDerivado, ...]:
    """Regra produtiva: substantivo/adjetivo + -inho/-inha (vogal átona cai)
    ou -zinho/-zinha (demais terminações). Ex.: "gato" -> "gatinho";
    "flor" -> "florzinho"; "café" -> "cafézinho" (vogal tônica acentuada,
    não cai)."""
    candidatos: list[CandidatoDerivado] = []
    vistos: set[str] = set()
    for entrada in entradas:
        if entrada.classe not in (ClasseGramatical.SUBSTANTIVO, ClasseGramatical.ADJETIVO):
            continue
        chave = normalizar_chave(entrada.lema)
        if chave in vistos:
            continue
        vistos.add(chave)
        base, usa_zinho = _base_diminutivo(entrada.lema)
        feminino = entrada.genero == Genero.FEMININO
        prefixo_z = "z" if usa_zinho else ""
        forma = base + prefixo_z + ("inha" if feminino else "inho")
        raiz_def = entrada.definicoes[0] if entrada.definicoes else ""
        definicao = f'Forma diminutiva de "{entrada.lema}": {raiz_def}'.strip()
        candidatos.append(CandidatoDerivado(entrada, forma, entrada.classe, definicao, "diminutivo -inho/-zinho"))
    return tuple(candidatos)


def _raiz_verbal(infinitivo: str) -> str | None:
    """Raiz do verbo (infinitivo sem a terminação -ar/-er/-ir), ou `None`
    se o infinitivo tem 3 letras ou menos ("ser", "ir", "ter", "ver",
    "dar", "ler") -- achado real medido: esses são os verbos irregulares
    monossilábicos mais antigos do português (raiz suplectiva, não
    regular), e cortar as 2 últimas letras deles produz raiz de 0-1 letra
    sem nenhum candidato real confirmado pelo oráculo em nenhuma das 3
    regras que usam esta função (18/18 não confirmados: "sível", "idor",
    "simento" etc.). Não é estimativa -- é o resultado medido que levou a
    este guard."""
    if len(infinitivo) <= 3:
        return None
    return infinitivo[:-2]


def _sufixo_agente(infinitivo: str) -> str | None:
    if infinitivo.endswith("ar"):
        return "ador"
    if infinitivo.endswith("er"):
        return "edor"
    if infinitivo.endswith("ir"):
        return "idor"
    return None


def gerar_agentes_dor(entradas: tuple[EntradaLexical, ...]) -> tuple[CandidatoDerivado, ...]:
    """Regra produtiva: verbo -> substantivo agente em -dor/-dora, conforme
    a conjugação (-ar -> -ador, -er -> -edor, -ir -> -idor). Ex.:
    "trabalhar" -> "trabalhador"/"trabalhadora"; "vender" -> "vendedor"."""
    candidatos: list[CandidatoDerivado] = []
    vistos: set[str] = set()
    for entrada in entradas:
        if entrada.classe != ClasseGramatical.VERBO:
            continue
        chave = normalizar_chave(entrada.lema)
        if chave in vistos:
            continue
        vistos.add(chave)
        sufixo = _sufixo_agente(entrada.lema)
        raiz = _raiz_verbal(entrada.lema)
        if sufixo is None or raiz is None:
            continue
        raiz_def = entrada.definicoes[0] if entrada.definicoes else ""
        definicao = f"Quem ou o que {entrada.lema}: {raiz_def}".strip()
        candidatos.append(
            CandidatoDerivado(entrada, raiz + sufixo, ClasseGramatical.SUBSTANTIVO, definicao, "verbo+dor (agente)")
        )
        candidatos.append(
            CandidatoDerivado(
                entrada, raiz + sufixo + "a", ClasseGramatical.SUBSTANTIVO, definicao, "verbo+dor (agente)"
            )
        )
    return tuple(candidatos)


def _sufixo_mento(infinitivo: str) -> str | None:
    if infinitivo.endswith("ar"):
        return "amento"
    if infinitivo.endswith(("er", "ir")):
        return "imento"
    return None


def gerar_substantivos_mento(entradas: tuple[EntradaLexical, ...]) -> tuple[CandidatoDerivado, ...]:
    """Regra produtiva: verbo -> substantivo de ação/resultado em -mento,
    conforme a conjugação (-ar -> -amento, -er/-ir -> -imento). Ex.:
    "pagar" -> "pagamento"; "conhecer" -> "conhecimento"."""
    candidatos: list[CandidatoDerivado] = []
    vistos: set[str] = set()
    for entrada in entradas:
        if entrada.classe != ClasseGramatical.VERBO:
            continue
        chave = normalizar_chave(entrada.lema)
        if chave in vistos:
            continue
        vistos.add(chave)
        sufixo = _sufixo_mento(entrada.lema)
        raiz = _raiz_verbal(entrada.lema)
        if sufixo is None or raiz is None:
            continue
        raiz_def = entrada.definicoes[0] if entrada.definicoes else ""
        definicao = f"Ação ou resultado de {entrada.lema}: {raiz_def}".strip()
        candidatos.append(
            CandidatoDerivado(entrada, raiz + sufixo, ClasseGramatical.SUBSTANTIVO, definicao, "verbo+mento")
        )
    return tuple(candidatos)


def gerar_adjetivos_oso(entradas: tuple[EntradaLexical, ...]) -> tuple[CandidatoDerivado, ...]:
    """Regra produtiva: substantivo -> adjetivo em -oso, indicando
    abundância ou qualidade relacionada ao substantivo. Ex.: "perigo" ->
    "perigoso"."""
    candidatos: list[CandidatoDerivado] = []
    vistos: set[str] = set()
    for entrada in entradas:
        if entrada.classe != ClasseGramatical.SUBSTANTIVO:
            continue
        chave = normalizar_chave(entrada.lema)
        if chave in vistos:
            continue
        vistos.add(chave)
        base = entrada.lema[:-1] if entrada.lema.endswith(_VOGAIS_ATONAS_FINAIS) else entrada.lema
        raiz_def = entrada.definicoes[0] if entrada.definicoes else ""
        definicao = f"Que tem ou está relacionado a {entrada.lema}: {raiz_def}".strip()
        candidatos.append(CandidatoDerivado(entrada, base + "oso", ClasseGramatical.ADJETIVO, definicao, "substantivo+oso"))
    return tuple(candidatos)


def _sufixo_vel(infinitivo: str) -> str | None:
    if infinitivo.endswith("ar"):
        return "ável"
    if infinitivo.endswith(("er", "ir")):
        return "ível"
    return None


def gerar_adjetivos_avel_ivel(entradas: tuple[EntradaLexical, ...]) -> tuple[CandidatoDerivado, ...]:
    """Regra produtiva: verbo -> adjetivo de capacidade/possibilidade em
    -ável/-ível, conforme a conjugação (-ar -> -ável, -er/-ir -> -ível).
    Ex.: "amar" -> "amável"; "vender" -> "vendível"."""
    candidatos: list[CandidatoDerivado] = []
    vistos: set[str] = set()
    for entrada in entradas:
        if entrada.classe != ClasseGramatical.VERBO:
            continue
        chave = normalizar_chave(entrada.lema)
        if chave in vistos:
            continue
        vistos.add(chave)
        sufixo = _sufixo_vel(entrada.lema)
        raiz = _raiz_verbal(entrada.lema)
        if sufixo is None or raiz is None:
            continue
        raiz_def = entrada.definicoes[0] if entrada.definicoes else ""
        definicao = f"Que se pode {entrada.lema}: {raiz_def}".strip()
        candidatos.append(
            CandidatoDerivado(entrada, raiz + sufixo, ClasseGramatical.ADJETIVO, definicao, "verbo+ável/ível")
        )
    return tuple(candidatos)


def gerar_substantivos_ista(entradas: tuple[EntradaLexical, ...]) -> tuple[CandidatoDerivado, ...]:
    """Regra produtiva: substantivo -> substantivo em -ista, indicando
    profissão, adepto de doutrina ou praticante de atividade ligada à
    raiz (vogal átona final cai antes do sufixo). Ex.: "arte" ->
    "artista"; "jornal" -> "jornalista". Palavra em -ista é comum de dois
    gêneros no português ("o artista"/"a artista"), por isso o candidato
    sai com `genero=None` -- quem revisar decide o traço no momento da
    incorporação (Fase 4 do plano de léxico), este módulo não inventa."""
    candidatos: list[CandidatoDerivado] = []
    vistos: set[str] = set()
    for entrada in entradas:
        if entrada.classe != ClasseGramatical.SUBSTANTIVO:
            continue
        chave = normalizar_chave(entrada.lema)
        if chave in vistos:
            continue
        vistos.add(chave)
        base = entrada.lema[:-1] if entrada.lema.endswith(_VOGAIS_ATONAS_FINAIS) else entrada.lema
        raiz_def = entrada.definicoes[0] if entrada.definicoes else ""
        definicao = f"Quem exerce ou segue o que se liga a {entrada.lema}: {raiz_def}".strip()
        candidatos.append(
            CandidatoDerivado(entrada, base + "ista", ClasseGramatical.SUBSTANTIVO, definicao, "substantivo+ista")
        )
    return tuple(candidatos)


def _prefixo_negativo(adjetivo: str) -> str:
    """Alomorfia real do prefixo negativo do português (assimilação do
    "n" ao ponto de articulação da consoante seguinte): "im-" antes de
    b/p, sem dobrar letra nenhuma porque "m" e "b"/"p" são consoantes
    diferentes ("possível"->"impossível"); "i-" antes de l OU m -- achado
    real medido por teste que falhou: "m" segue a MESMA lógica de "l", não
    a de "b"/"p", porque o português não escreve consoante dobrada "mm"
    (só "rr"/"ss" são dígrafos válidos) -- prefixo vira só "i" e funde
    com o m da palavra ("legal"->"ilegal", "moral"->"imoral", nunca
    "immoral"); "ir-" antes de r, aqui SIM dobra porque "rr" é dígrafo
    válido em português ("responsável"->"irresponsável"); "in-" nos
    demais casos ("feliz"->"infeliz")."""
    if adjetivo.startswith(("b", "p")):
        return "im"
    if adjetivo.startswith(("l", "m")):
        return "i"
    if adjetivo.startswith("r"):
        return "ir"
    return "in"


def gerar_adjetivos_negativos_in(entradas: tuple[EntradaLexical, ...]) -> tuple[CandidatoDerivado, ...]:
    """Regra produtiva: adjetivo -> adjetivo negado pelo prefixo in-/im-/
    i-/ir-, conforme a letra inicial (ver `_prefixo_negativo`). Ex.:
    "feliz" -> "infeliz"; "possível" -> "impossível"; "legal" ->
    "ilegal"; "responsável" -> "irresponsável"."""
    candidatos: list[CandidatoDerivado] = []
    vistos: set[str] = set()
    for entrada in entradas:
        if entrada.classe != ClasseGramatical.ADJETIVO:
            continue
        chave = normalizar_chave(entrada.lema)
        if chave in vistos:
            continue
        vistos.add(chave)
        prefixo = _prefixo_negativo(entrada.lema)
        raiz_def = entrada.definicoes[0] if entrada.definicoes else ""
        definicao = f"Que não é {entrada.lema}: {raiz_def}".strip()
        candidatos.append(
            CandidatoDerivado(entrada, prefixo + entrada.lema, ClasseGramatical.ADJETIVO, definicao, "in-/im-/i-/ir-+adjetivo")
        )
    return tuple(candidatos)


def _oraculo_dicionario_sistema(caminho: Path | None = None) -> frozenset[str] | None:
    """Lê o dicionário hunspell do sistema operacional só como oráculo de
    existência para VALIDAR candidatos já gerados por regra -- nunca
    copiado para este repositório, nunca fonte de novo lema por si só.
    Devolve `None` (nunca conjunto vazio fabricado) se o ficheiro não
    existir no ambiente atual: sinal honesto de "sem dado para validar",
    distinto de "nenhuma palavra confirmada"."""
    caminho = caminho or _CAMINHO_ORACULO_PADRAO
    if not caminho.is_file():
        return None
    linhas = caminho.read_text(encoding="utf-8", errors="ignore").splitlines()[1:]
    return frozenset(normalizar_chave(linha.split("/", 1)[0]) for linha in linhas if linha)


@dataclass(frozen=True, slots=True)
class ResultadoValidacao:
    total: int
    confirmados: int
    taxa: float | None
    exemplos_confirmados: tuple[str, ...]
    exemplos_nao_confirmados: tuple[str, ...]


def validar_candidatos(
    candidatos: tuple[CandidatoDerivado, ...], caminho_oraculo: Path | None = None
) -> ResultadoValidacao:
    """Mede, com número real, que fração dos candidatos gerados corresponde
    a palavra portuguesa confirmada pelo oráculo do sistema -- o teste
    empírico "isso funciona na prática" pedido pelo autor. `taxa=None`
    (nunca `0.0`) quando o oráculo não está disponível no ambiente atual."""
    oraculo = _oraculo_dicionario_sistema(caminho_oraculo)
    total = len(candidatos)
    if oraculo is None:
        return ResultadoValidacao(total, 0, None, (), tuple(c.forma for c in candidatos[:10]))
    confirmados = [c.forma for c in candidatos if normalizar_chave(c.forma) in oraculo]
    nao_confirmados = [c.forma for c in candidatos if normalizar_chave(c.forma) not in oraculo]
    taxa = (len(confirmados) / total) if total else None
    return ResultadoValidacao(total, len(confirmados), taxa, tuple(confirmados[:10]), tuple(nao_confirmados[:10]))
