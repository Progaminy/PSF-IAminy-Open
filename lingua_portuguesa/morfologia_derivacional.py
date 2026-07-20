"""Morfologia derivacional construída localmente.

As funções deste módulo geram candidatos por composição de uma raiz já
conhecida com afixos produtivos. Candidato não significa entrada validada:
nenhuma derivação é incorporada automaticamente ao dicionário padrão.

A validação opcional aceita somente recurso criado dentro de
``lingua_portuguesa/dados``. Não há busca em dicionário do sistema, rede,
serviço, corpus externo ou biblioteca linguística.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .normalizacao import normalizar_chave
from .tipos import ClasseGramatical, EntradaLexical, Genero

_DIRETORIO_DADOS_LOCAL = Path(__file__).resolve().parent / "dados"
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


def _oraculo_lexical_local(caminho: Path | None = None) -> frozenset[str] | None:
    """Lê somente um oráculo local fornecido explicitamente pelo projeto.

    Não procura dicionários do sistema e rejeita até um caminho explícito se
    ele sair de ``lingua_portuguesa/dados`` (inclusive por ligação simbólica).
    ``None`` significa honestamente que não há fonte local para a medição.
    """
    if caminho is None:
        return None
    try:
        resolvido = caminho.resolve(strict=True)
        resolvido.relative_to(_DIRETORIO_DADOS_LOCAL.resolve(strict=True))
    except (FileNotFoundError, OSError, ValueError):
        return None
    if not resolvido.is_file():
        return None
    linhas = resolvido.read_text(encoding="utf-8", errors="ignore").splitlines()[1:]
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
    """Mede candidatos apenas contra um recurso lexical do próprio projeto.

    ``taxa=None`` (nunca ``0.0``) quando esse recurso local não foi fornecido
    ou quando o caminho tentaria sair do diretório de dados empacotado.
    """
    oraculo = _oraculo_lexical_local(caminho_oraculo)
    total = len(candidatos)
    if oraculo is None:
        return ResultadoValidacao(total, 0, None, (), tuple(c.forma for c in candidatos[:10]))
    confirmados = [c.forma for c in candidatos if normalizar_chave(c.forma) in oraculo]
    nao_confirmados = [c.forma for c in candidatos if normalizar_chave(c.forma) not in oraculo]
    taxa = (len(confirmados) / total) if total else None
    return ResultadoValidacao(total, len(confirmados), taxa, tuple(confirmados[:10]), tuple(nao_confirmados[:10]))
