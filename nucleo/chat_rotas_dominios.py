# -*- coding: utf-8 -*-
"""Rotas de alta autoridade para os motores especializados."""
from __future__ import annotations

from functools import lru_cache
import re

from motor import MotorGeralIAMiny
from nucleo.chat_texto import detectar_tom, normalizar
from nucleo.chat_tipos import RespostaChat


LIMITE_CARACTERES_EXPRESSAO = 240
LIMITE_CASAS_DECIMAIS = 100
LIMITE_LITERAL_SIMPLES = 1_000
LIMITE_OPERANDO_CARO = 20
LIMITE_RESULTADO_POTENCIA = 400

_PADRAO_CALCULO = re.compile(
    r"^\s*(?:calcule|calcula|calcular)\s+"
    r"(?P<expressao>.+?)"
    r"(?:\s+com\s+(?P<casas>\d+)\s+casas?(?:\s+decimais?)?"
    r"(?:\s+(?P<modo>truncad[oa]s?|arredondad[oa]s?))?)?"
    r"[?.!]*\s*$",
    flags=re.IGNORECASE,
)
_NUMERAL = re.compile(r"\d+")
_POTENCIA_LITERAL = re.compile(r"(\d+)\s*\^\s*(\d+)")


@lru_cache(maxsize=1)
def _motor_geral() -> MotorGeralIAMiny:
    return MotorGeralIAMiny()


def _resposta(texto: str, intencao: str, origem: str, *, lacunas: list[str] | None = None) -> RespostaChat:
    return RespostaChat(
        texto,
        intencao,
        "pergunta",
        94,
        origem=origem,
        conhecimento_encontrado=True,
        lacunas=lacunas or [],
        contexto_chat={"ultimo_titulo": intencao, "ultima_origem": origem},
    )


def _identidade(texto: str) -> RespostaChat | None:
    t = normalizar(texto)
    if not re.search(r"\b(?:quem|o que) (?:e|es) (?:voce|tu)\b|\bquem (?:e|es) tu\b", t):
        return None
    dados = _motor_geral().identidade()
    return _resposta(
        f"Sou o {dados['nome']}, a forma de máquina/IA do Pensador Sem Fronteiras. "
        "Trabalho como uma versão única contínua e separo construção, prova, exemplo e limite.",
        "identidade_publica",
        "motor.geral:identidade",
    )


def _resposta_limite_calculo(texto: str, limite: str) -> RespostaChat:
    return RespostaChat(
        f"Não executei o cálculo pedido: {limite}",
        "calculo_fora_do_limite_operacional",
        detectar_tom(texto),
        92,
        origem="motor.matematica:limites_operacionais",
        conhecimento_encontrado=False,
        lacunas=[limite],
        deve_melhorar=False,
    )


def _limite_operacional_calculo(expressao: str) -> str | None:
    if len(expressao) > LIMITE_CARACTERES_EXPRESSAO:
        return (
            "a expressão tem mais de "
            f"{LIMITE_CARACTERES_EXPRESSAO} caracteres"
        )

    numerais = tuple(_NUMERAL.findall(expressao))
    if any(len(numeral) > 4 for numeral in numerais):
        return "cada numeral do chat deve ter no máximo 4 algarismos"
    valores = tuple(int(numeral) for numeral in numerais)
    if any(valor > LIMITE_LITERAL_SIMPLES for valor in valores):
        return (
            "o chat aceita numerais simples até "
            f"{LIMITE_LITERAL_SIMPLES}"
        )

    if any(operador in expressao for operador in ("*", "/", ":")):
        if any(valor > LIMITE_OPERANDO_CARO for valor in valores):
            return (
                "multiplicação e divisão no chat aceitam operandos até "
                f"{LIMITE_OPERANDO_CARO}; o motor puro mantém o cálculo "
                "controlado fora da interface"
            )
        if "*" in expressao:
            produto_literal = 1
            for valor in valores:
                produto_literal *= valor
            if produto_literal > LIMITE_RESULTADO_POTENCIA:
                return (
                    "o produto literal pedido ultrapassa o limite operacional "
                    f"de {LIMITE_RESULTADO_POTENCIA} para o chat"
                )

    if "^" in expressao:
        potencias = tuple(_POTENCIA_LITERAL.finditer(expressao))
        if not potencias:
            return "potências no chat devem usar base e expoente naturais literais"
        for potencia in potencias:
            base, expoente = (int(valor) for valor in potencia.groups())
            if base ** expoente > LIMITE_RESULTADO_POTENCIA:
                return (
                    "a potência pedida ultrapassa o limite operacional de "
                    f"{LIMITE_RESULTADO_POTENCIA} para o chat"
                )
    return None


def _calculo(texto: str) -> RespostaChat | None:
    correspondencia = _PADRAO_CALCULO.match(texto)
    if correspondencia is None:
        return None
    expressao = correspondencia.group("expressao").strip()
    limite = _limite_operacional_calculo(expressao)
    if limite is not None:
        return _resposta_limite_calculo(texto, limite)

    casas_texto = correspondencia.group("casas")
    if casas_texto is not None and len(casas_texto) > 4:
        return _resposta_limite_calculo(
            texto,
            f"o pedido de casas decimais excede o limite de {LIMITE_CASAS_DECIMAIS}",
        )
    casas = int(casas_texto) if casas_texto else None
    if casas is not None and casas > LIMITE_CASAS_DECIMAIS:
        return _resposta_limite_calculo(
            texto,
            f"o chat aceita no máximo {LIMITE_CASAS_DECIMAIS} casas decimais",
        )
    modo_texto = correspondencia.group("modo") or ""
    modo = "arredondar" if modo_texto.casefold().startswith("arredond") else "truncar"
    try:
        resolucao = _motor_geral().calcular_matematica(expressao, casas, modo)
    except (TypeError, ValueError) as erro:
        return RespostaChat(
            f"Não consegui interpretar o cálculo pedido: {erro}",
            "calculo_invalido",
            detectar_tom(texto),
            88,
            origem="motor.matematica",
            lacunas=["expressão fora da gramática matemática suportada"],
            deve_melhorar=False,
        )
    passos = "\n".join(f"{passo.ordem}. {passo.operacao}: {passo.saida}" for passo in resolucao.passos)
    if resolucao.resultado is None:
        partes = [f"Estado: {resolucao.estado}."]
        if passos:
            partes.append(f"Passos disponíveis:\n{passos}")
        if resolucao.limites:
            partes.append("Limites:\n" + "\n".join(f"- {limite}" for limite in resolucao.limites))
        return _resposta(
            "\n\n".join(partes),
            "calculo_nao_resolvido",
            "motor.matematica:calcular",
            lacunas=list(resolucao.limites),
        )
    exato = f" (valor exato: {resolucao.resultado_exato})" if resolucao.resultado_exato else ""
    return _resposta(
        f"Resultado: {resolucao.resultado}{exato}.\n\n{passos}",
        "calculo_matematico",
        "motor.matematica:calcular",
        lacunas=list(resolucao.limites),
    )


def _analise_portugues(texto: str) -> RespostaChat | None:
    correspondencia = re.match(r"^\s*(?:analise|analisa|analisar)\s*:\s*(.+)$", texto, flags=re.IGNORECASE)
    if correspondencia is None:
        return None
    alvo = correspondencia.group(1).strip()
    analise = _motor_geral().analisar_portugues(alvo)
    if analise.diagnosticos:
        linhas = [f"- {item.mensagem} Sugestão: {item.sugestao}" for item in analise.diagnosticos]
        corpo = "Encontrei estes diagnósticos:\n" + "\n".join(linhas)
    else:
        corpo = "Não encontrei discordâncias cobertas pelo analisador atual."
    return _resposta(corpo, "analise_portugues", "motor.portugues:analisar")


def _definicao_portugues(texto: str) -> RespostaChat | None:
    correspondencia = re.match(r"^\s*(?:o que (?:e|sao)|defina)\s+(.+?)[?.!]*\s*$", normalizar(texto))
    if correspondencia is None:
        return None
    conceito = correspondencia.group(1).strip()
    definicao = _motor_geral().portugues.definir_conceito_puro(conceito)
    if not definicao:
        return None
    return _resposta(definicao, "definicao_portugues", "motor.portugues:conhecimento_puro")


def _reconstrucao_matematica(texto: str) -> RespostaChat | None:
    t = normalizar(texto)
    bruto = texto.casefold()
    assunto = None
    if "teorema de hall" in t or re.search(r"\bhall\b", t):
        assunto = "grafos emparelhamento hall"
    elif re.search(r"r\s*\(\s*3\s*,\s*3\s*\)\s*=\s*6", bruto) or "ramsey 33" in t:
        assunto = "ramsey 33"
    if assunto is None:
        return None
    reconstrucao = _motor_geral().reconstruir_matematica(assunto)
    if reconstrucao.conceito is None:
        return None
    conceito = reconstrucao.conceito
    exemplo = f"\n\nExemplo: {conceito.exemplos_minimos[0]}." if conceito.exemplos_minimos else ""
    limite = ""
    if assunto == "grafos emparelhamento hall":
        limite = (
            "\n\nLimite: o PSF confirma o teorema em cada instância finita por duas buscas "
            "independentes; isso não substitui uma prova simbólica geral."
        )
    elif assunto == "ramsey 33":
        limite = "\n\nLimite: somente R(3,3) foi construído; Ramsey geral permanece fora do escopo."
    primeiro_paragrafo = conceito.construcao.split("\n\n", 1)[0]
    return _resposta(
        primeiro_paragrafo + exemplo + limite,
        "reconstrucao_matematica",
        f"motor.matematica:reconstruir:{conceito.nome}",
        lacunas=list(reconstrucao.limites),
    )


def responder_por_dominio(texto: str) -> RespostaChat | None:
    """Aplica autoridade por domínio antes de qualquer índice documental."""
    for rota in (_identidade, _calculo, _analise_portugues, _reconstrucao_matematica, _definicao_portugues):
        resposta = rota(texto)
        if resposta is not None:
            resposta.tom = detectar_tom(texto)
            return resposta
    return None
