# -*- coding: utf-8 -*-
"""Rotas para materialização e bloqueio honesto de fora de escopo."""
from __future__ import annotations

from nucleo.chat_texto import detectar_tom, normalizar
from nucleo.chat_tipos import RespostaChat

def _parece_comando_adicionar_conhecimento(texto: str) -> bool:
    """Detecta quando o utilizador quer registrar material novo, não buscar resposta."""
    t = normalizar(texto)
    gatilhos = (
        "adicione isso na base",
        "adiciona isso na base",
        "adicionar isso na base",
        "registre isso",
        "regista isso",
        "guarde isso",
        "guardar isso",
        "aprenda isso",
        "coloque na base",
        "põe na base",
        "poe na base",
        "materialize isso",
    )
    return any(g in t for g in gatilhos)


def _responder_comando_adicionar_conhecimento(texto: str) -> RespostaChat | None:
    if not _parece_comando_adicionar_conhecimento(texto):
        return None
    bruto = str(texto).strip()
    conteudo = bruto
    for sep in (":", "—", "-"):
        if sep in bruto:
            conteudo = bruto.split(sep, 1)[1].strip()
            break
    if not conteudo or conteudo == bruto and len(bruto.split()) < 5:
        corpo = (
            "Entendi que queres adicionar conhecimento, mas preciso do conteúdo depois do comando. "
            "Exemplo: `adicione isso na base: número triangular é um número figurado formado por pontos em triângulo`."
        )
    else:
        corpo = (
            "Recebi isto como pedido de materialização de conhecimento novo, não como pergunta para buscar no índice.\n\n"
            f"Conteúdo recebido: {conteudo}\n\n"
            "Estado: ainda não foi aprovado como conhecimento PSF.\n"
            "Próximo passo: criar uma entrada canônica com definição, resposta curta, aula, exemplo, teste e lacuna se existir. "
            "Não vou fingir que isto já estava na base."
        )
    return RespostaChat(
        corpo,
        "entrada_conhecimento_novo",
        detectar_tom(texto),
        82,
        origem="chat_vivo_materializacao",
        conhecimento_encontrado=False,
        lacunas=["entrada nova ainda não materializada"],
        deve_melhorar=True,
        contexto_chat={"ultimo_titulo": "Entrada nova de conhecimento", "ultima_origem": "chat_vivo_materializacao"},
    )


def _responder_fora_escopo_sem_inventar(texto: str) -> RespostaChat | None:
    """Bloqueia rotas que antes geravam falso positivo confiante."""
    t = normalizar(texto)
    if any(g in t for g in ("escreve um poema", "escreva um poema", "poema sobre", "me conta uma piada", "conta uma piada")):
        return RespostaChat(
            "Esse pedido é criativo/conversacional, mas esta versão do PSF está focada em estudo, matemática, investigação e auditoria local. Não encontrei rota segura para gerar isso sem misturar com conhecimento errado. Posso transformar o pedido em exercício de escrita, se quiseres.",
            "fora_escopo_criativo",
            detectar_tom(texto),
            45,
            origem="rota_segura_sem_inventar",
            conhecimento_encontrado=False,
            lacunas=["pedido criativo fora da cobertura atual"],
            fallback_usado=True,
        )
    if ("tempo hoje" in t or "achas do tempo" in t or "previsao do tempo" in t or "previsão do tempo" in t) and "matematica" not in t:
        return RespostaChat(
            "Não tenho acesso a meteorologia atual nem internet nesta versão local. Para previsão de hoje, seria preciso uma fonte externa. Posso explicar a matemática da previsão do tempo, mas não vou fingir clima atual.",
            "sem_dados_atuais",
            detectar_tom(texto),
            45,
            origem="rota_segura_sem_dados_atuais",
            conhecimento_encontrado=False,
            lacunas=["dado atual exige fonte externa"],
            fallback_usado=True,
        )
    return None

