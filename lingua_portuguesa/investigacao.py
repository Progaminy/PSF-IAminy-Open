"""Investigação estruturada — orquestra capacidades já reais do motor em 9 estágios.

Não inventa nenhuma capacidade nova de compreensão: cada estágio chama um
método que `MotorPortugues` já expõe de verdade (`definir_conceito_puro`,
`dependencias_conceito_puro`, `trilho_ate_conceito_puro`,
`buscar_conceitos_puros`) e organiza o resultado na sequência pedida —
o que é, o que quer, como funciona, o que fazer, o que preciso, onde
encontrar, como estruturar, como gerar, onde entregar. Quando a pergunta
não resolve a nenhum conceito conhecido (nem por nome exato, nem por
busca textual), `investigar` devolve `None` — nunca inventa um conceito
que não existe.

A "intenção" (o que quer) é reconhecida por palavras-chave explícitas na
pergunta, não por interpretação semântica real — é um classificador
transparente, honesto sobre seu próprio limite: várias perguntas caem no
caso padrão ("definição") sem que isso signifique compreensão profunda.
"""
from __future__ import annotations

from dataclasses import dataclass

from .conhecimento_puro import ConceitoPortugues
from .motor import MotorPortugues

_PALAVRAS_MECANISMO = ("como funciona", "mecanismo", "como se constrói", "como opera")
_PALAVRAS_REQUISITOS = ("de que depende", "o que precisa", "requisitos", "depende de", "precisa de")
_PALAVRAS_USO = ("quem usa", "o que usa", "ligado por", "quem depende", "o que depende de")
_PALAVRAS_LOCALIZACAO = ("onde fica", "onde encontrar", "onde está", "localizar")

_PREFIXOS_PERGUNTA = (
    "o que é o ", "o que é a ", "o que é ", "o que e o ", "o que e a ", "o que e ",
    "defina ", "definir ", "como funciona o ", "como funciona a ", "como funciona ",
    "de que depende o ", "de que depende a ", "de que depende ",
    "o que precisa o ", "o que precisa a ", "o que precisa ",
    "quem depende de ", "quem usa ", "o que usa ", "ligado por ",
    "onde fica o ", "onde fica a ", "onde fica ", "onde encontrar o ", "onde encontrar a ",
    "onde encontrar ", "onde está o ", "onde está a ", "onde está ", "localizar ",
)


@dataclass(frozen=True, slots=True)
class Investigacao:
    pergunta: str
    conceito: str
    o_que_e: str
    o_que_quer: str
    como_funciona: str
    o_que_fazer: str
    o_que_preciso: tuple[str, ...]
    quem_depende_disto: tuple[str, ...]
    onde_encontrar: tuple[str, ...]
    como_estruturar: tuple[str, ...]
    como_gerar: str
    onde_entregar: str


def _normalizar(pergunta: str) -> str:
    texto = pergunta.strip().casefold()
    if texto.endswith("?"):
        texto = texto[:-1].strip()
    return texto


def _identificar_por_nome_dentro_do_texto(texto: str, motor: MotorPortugues) -> ConceitoPortugues | None:
    """Procura o nome de conceito mais longo que aparece dentro do texto da pergunta."""
    melhor: ConceitoPortugues | None = None
    for conceito in motor.conhecimento_puro():
        nome = conceito.nome.casefold()
        if nome in texto and (melhor is None or len(nome) > len(melhor.nome)):
            melhor = conceito
    return melhor


def _identificar_conceito(pergunta: str, motor: MotorPortugues) -> ConceitoPortugues | None:
    texto = _normalizar(pergunta)
    conceito = motor.conhecimento_portugues.buscar(texto)
    if conceito is not None:
        return conceito
    for prefixo in _PREFIXOS_PERGUNTA:
        if texto.startswith(prefixo):
            resto = texto[len(prefixo):].strip()
            conceito = motor.conhecimento_portugues.buscar(resto)
            if conceito is not None:
                return conceito
    conceito = _identificar_por_nome_dentro_do_texto(texto, motor)
    if conceito is not None:
        return conceito
    candidatos = motor.buscar_conceitos_puros(pergunta)
    return candidatos[0] if candidatos else None


def _identificar_intencao(pergunta: str) -> str:
    texto = _normalizar(pergunta)
    if any(p in texto for p in _PALAVRAS_USO):
        return "uso"
    if any(p in texto for p in _PALAVRAS_REQUISITOS):
        return "requisitos"
    if any(p in texto for p in _PALAVRAS_MECANISMO):
        return "mecanismo"
    if any(p in texto for p in _PALAVRAS_LOCALIZACAO):
        return "localizacao"
    return "definicao"


_DESCRICAO_INTENCAO = {
    "uso": "a pergunta busca quem usa ou depende deste conceito",
    "requisitos": "a pergunta busca do que este conceito precisa para existir",
    "mecanismo": "a pergunta busca como o conceito é construído por dentro",
    "localizacao": "a pergunta busca onde este conceito fica na linha canônica",
    "definicao": "a pergunta busca o que o conceito é (caso padrão, sem palavra-chave mais específica)",
}

_ACAO_POR_INTENCAO = {
    "uso": "listar conceitos cujo depende_de cita este nome",
    "requisitos": "motor.dependencias_conceito_puro(nome)",
    "mecanismo": "motor.definir_conceito_puro(nome) (campo construção)",
    "localizacao": "motor.trilho_ate_conceito_puro(nome)",
    "definicao": "motor.definir_conceito_puro(nome) e motor.funcao_conceito_puro(nome)",
}


def _quem_depende_de(nome: str, motor: MotorPortugues) -> tuple[str, ...]:
    return tuple(c.nome for c in motor.conhecimento_puro() if nome in c.depende_de)


def investigar(pergunta: str, motor: MotorPortugues) -> Investigacao | None:
    """Executa os 9 estágios sobre a pergunta; None se nenhum conceito for identificado."""
    conceito = _identificar_conceito(pergunta, motor)
    if conceito is None:
        return None

    intencao = _identificar_intencao(pergunta)
    trilho = motor.trilho_ate_conceito_puro(conceito.nome)
    dependentes = _quem_depende_de(conceito.nome, motor)

    o_que_e = (
        f"'{conceito.nome}' é um conceito puro do tema '{conceito.tema_consulta}', "
        f"posição {conceito.ordem} na linha canônica do Português."
    )
    como_estruturar = (
        ("identificação", "mecanismo", "função", "dependências")
        if conceito.depende_de
        else ("identificação", "mecanismo", "função", "raiz — sem dependências")
    )
    como_gerar = (
        f"{o_que_e} {conceito.construcao} {conceito.funcao} "
        f"Depende de: {', '.join(conceito.depende_de) if conceito.depende_de else 'nada — é raiz'}. "
        f"Ligado por: {', '.join(dependentes) if dependentes else 'nada ainda depende deste conceito'}."
    )

    return Investigacao(
        pergunta=pergunta,
        conceito=conceito.nome,
        o_que_e=o_que_e,
        o_que_quer=_DESCRICAO_INTENCAO[intencao],
        como_funciona=conceito.construcao,
        o_que_fazer=_ACAO_POR_INTENCAO[intencao],
        o_que_preciso=conceito.depende_de,
        quem_depende_disto=dependentes,
        onde_encontrar=trilho,
        como_estruturar=como_estruturar,
        como_gerar=como_gerar,
        onde_entregar="objeto Investigacao devolvido pela chamada; texto pronto em como_gerar",
    )
