# -*- coding: utf-8 -*-
"""Rotas de auditoria, estado do projeto e perguntas operacionais."""
from __future__ import annotations

from typing import Any

from nucleo.chat_base_canonica import buscar_base_canonica, obter_registro
from nucleo.base_curiosidades_reais import procurar as procurar_curiosidade
from nucleo.chat_formatacao import _bloco_final, _fonte_publica_registro, _formatar_curiosidade, _formatar_registro
from nucleo.chat_texto import detectar_modo, detectar_tom, normalizar, tokens_de
from nucleo.chat_tipos import RegistroCanonico, RespostaChat

def _auditar_registro(registro: RegistroCanonico, texto: str) -> RespostaChat:
    """Responde perguntas do tipo 'Bhaskara tem teste?' com assunto na própria frase."""
    t = normalizar(texto)
    dados = registro.dados
    consulta_teste = "tem teste" in t
    consulta_aula = "tem aula" in t
    consulta_prova = "tem prova" in t
    consulta_lacuna = "tem lacuna" in t
    consulta_etapa = "de que etapa" in t or "de que fonte" in t or "onde esta" in t
    consulta_contradicao = "contradiz" in t
    consulta_pronto = "pronto para uso" in t
    if not any((consulta_teste, consulta_aula, consulta_prova, consulta_lacuna, consulta_etapa, consulta_contradicao, consulta_pronto)):
        return _formatar_registro(registro, detectar_modo(texto), 88)
    linhas = [
        f"Assunto: {registro.titulo}.",
        f"Fonte viva: {_fonte_publica_registro(registro)}.",
        f"Estado: {dados.get('estado', 'conhecido')}.",
        f"Tipo: {dados.get('tipo', 'conceito')}.",
    ]
    if consulta_aula or not any((consulta_teste, consulta_prova, consulta_lacuna, consulta_etapa, consulta_contradicao, consulta_pronto)):
        linhas.append(f"Tem aula: {'sim' if dados.get('aula_direta') or dados.get('aula_detalhada') else 'não'}.")
    if consulta_teste or not any((consulta_aula, consulta_prova, consulta_lacuna, consulta_etapa, consulta_contradicao, consulta_pronto)):
        linhas.append(f"Tem teste: {'sim' if dados.get('testes') else 'não'}.")
    if consulta_prova:
        linhas.append(f"Tem prova: {'sim' if dados.get('tem_prova') else 'não'}.")
    if consulta_lacuna:
        linhas.append(f"Tem lacuna: {'sim' if dados.get('tem_lacuna') else 'não'}.")
    if consulta_etapa:
        linhas.append("O chat mostra fonte viva; rastro antigo fica só para auditoria interna.")
    if consulta_contradicao:
        linhas.append("Contradição detectada nesta rota: não.")
    if consulta_pronto:
        pronto = bool(dados.get('resposta_curta') and (dados.get('testes') or dados.get('aula_direta')))
        linhas.append(f"Pronto para uso no chat: {'sim' if pronto else 'parcial'}.")
    return RespostaChat(
        "\n".join(linhas) + "\n\n" + _bloco_final(88, _fonte_publica_registro(registro), []),
        "auditoria_por_assunto",
        detectar_tom(texto),
        88,
        origem=f"base_canonica:{registro.id}",
        conhecimento_encontrado=True,
        contexto_chat={"ultimo_registro_id": registro.id, "ultima_origem": _fonte_publica_registro(registro), "ultimo_titulo": registro.titulo},
    )


def _responder_auditoria_por_assunto(texto: str) -> RespostaChat | None:
    t = normalizar(texto)
    marcadores = ("tem teste", "tem aula", "tem prova", "tem lacuna", "de que etapa", "de que fonte", "contradiz", "pronto para uso")
    if not any(m in t for m in marcadores):
        return None
    # remove palavras de auditoria para procurar só o assunto
    assunto = t
    for m in marcadores:
        assunto = assunto.replace(m, " ")
    assunto = assunto.replace("?", " ").strip()
    # Sem assunto real, isto é auditoria contextual e deve cair na rota
    # "preciso saber de qual assunto", não buscar algo aleatório como "veio".
    tokens_sem_assunto = {
        "veio", "vem", "fonte", "etapa", "teste", "aula", "prova", "lacuna",
        "esta", "está", "pronto", "uso", "algo", "anterior", "contradiz"
    }
    resto_tokens = {tok for tok in tokens_de(assunto) if tok not in tokens_sem_assunto}
    if not assunto or not resto_tokens:
        return None
    registro, score = buscar_base_canonica(assunto)
    if registro is not None and score >= 35:
        return _auditar_registro(registro, texto)
    curiosidade = procurar_curiosidade(assunto)
    if curiosidade is not None:
        linhas = [
            f"Assunto: {curiosidade.pergunta}.",
            f"Fonte viva: base de curiosidades (item {curiosidade.numero}: {curiosidade.categoria}).",
            "Tem aula: sim.",
            "Tem teste: sim.",
            "Tem lacuna: resposta curta; pode precisar expansão se o usuário pedir profundidade.",
        ]
        return RespostaChat(
            "\n".join(linhas) + "\n\n" + _bloco_final(82, f"base de curiosidades item {curiosidade.numero}", ["resposta curta"]),
            "auditoria_por_assunto",
            detectar_tom(texto),
            82,
            origem=f"curiosidade:{curiosidade.numero}",
            conhecimento_encontrado=True,
            lacunas=["resposta curta"],
            contexto_chat={"ultimo_curiosidade_numero": curiosidade.numero, "ultima_origem": f"base de curiosidades item {curiosidade.numero}", "ultimo_titulo": curiosidade.pergunta},
        )
    return None

def _responder_operacional_sem_contexto(texto: str, contexto: dict[str, Any] | None = None) -> RespostaChat | None:
    """Responde perguntas sobre o próprio estado do PSF sem procurar assunto aleatório.

    Estas perguntas costumam ser follow-up contextual ("tem teste?", "de que etapa veio?"),
    mas quando chegam sem contexto não devem cair no índice e puxar um tema errado.
    """
    t = normalizar(texto)
    contexto = contexto if isinstance(contexto, dict) else {}

    if "quantos problemas em aberto" in t or "problemas em aberto faltam" in t:
        return RespostaChat(
            "Pelos registros materializados até agora, o PSF conhece 81 entradas abertas/investigáveis com plano. Entre essas conhecidas, não há uma sem plano marcada como faltando. Isso não significa que a matemática esteja resolvida; significa apenas que o conjunto conhecido pelo projeto tem rota de investigação registrada. Novo problema trazido pelo usuário entra como novo item a materializar.",
            "estado_problemas_abertos",
            detectar_tom(texto),
            88,
            origem="motor_mestre_status",
            conhecimento_encontrado=True,
            contexto_chat={"ultimo_titulo": "Estado dos problemas em aberto", "ultima_origem": "motor_mestre_status"},
        )

    # Pedidos operacionais do produto: não devem cair no índice matemático por acidente.
    if t in {"como rodar", "como roda", "como executar", "como iniciar"} or "como rodar" in t or "como roda" in t:
        return RespostaChat(
            "Para rodar no terminal: 1) entra na pasta PSF-IAminy; 2) executa `python3 verificar_integridade.py`; 3) testa `python3 psf_chat.py 'quem é você?'`; 4) para a interface usa `python3 -m interface.servidor` e abre http://127.0.0.1:8765. Não precisa internet nem API externa.",
            "como_rodar",
            detectar_tom(texto),
            92,
            origem="README/COMO_RODAR",
            conhecimento_encontrado=True,
            contexto_chat={"ultimo_titulo": "Como rodar", "ultima_origem": "README/COMO_RODAR"},
        )

    if "como abrir interface" in t or "abrir interface" in t or "interface" in t and "como" in t:
        return RespostaChat(
            "Para abrir a interface: executa `python3 -m interface.servidor` dentro da pasta PSF-IAminy. Depois abre no navegador: http://127.0.0.1:8765. A interface deve chamar o Chat Vivo, não o fallback antigo.",
            "como_abrir_interface",
            detectar_tom(texto),
            92,
            origem="README/COMO_RODAR",
            conhecimento_encontrado=True,
            contexto_chat={"ultimo_titulo": "Interface", "ultima_origem": "README/COMO_RODAR"},
        )

    if t in {"como testar", "como testar?"} or "como testar" in t or "rodar testes" in t:
        return RespostaChat(
            "Para testar: `python3 verificar_integridade.py`, depois `python3 -m pytest testes/aceitacao -q`, e por fim `python3 -m pytest -q`. Só considera aprovado se der 0 failed e 0 errors.",
            "como_testar",
            detectar_tom(texto),
            92,
            origem="README/COMO_RODAR",
            conhecimento_encontrado=True,
            contexto_chat={"ultimo_titulo": "Como testar", "ultima_origem": "README/COMO_RODAR"},
        )

    if "o que voce sabe" in t or "o que você sabe" in t or "que sabes" in t:
        return RespostaChat(
            "Eu sei o que está materializado no projeto local: identidade do PSF, aulas básicas, fórmulas montadas/desmontadas, curiosidades matemáticas, problemas abertos com estado honesto, dossiês, testes e auditorias. O correto é perguntar um tema; eu procuro na base canônica primeiro e no índice total depois.",
            "estado_conhecimento",
            detectar_tom(texto),
            86,
            origem="motor_mestre_status",
            conhecimento_encontrado=True,
            contexto_chat={"ultimo_titulo": "Estado do conhecimento", "ultima_origem": "motor_mestre_status"},
        )

    if "o que falta melhorar" in t or "que falta melhorar" in t or "o que esta pendente" in t or "o que está pendente" in t:
        return RespostaChat(
            "No plano mãe, crescimento não é pendência. Como produto, o que ainda deve melhorar é: aumentar a bateria de conversa real, transformar mais respostas brutas do índice em entradas canônicas, melhorar follow-up contextual e reduzir respostas genéricas quando o tema existe só como trecho bruto. Isto é melhoria contínua, não falha prometida sem cobertura.",
            "estado_melhorias",
            detectar_tom(texto),
            86,
            origem="plano_mae/status_chat",
            conhecimento_encontrado=True,
            contexto_chat={"ultimo_titulo": "Melhorias do Chat Vivo", "ultima_origem": "plano_mae/status_chat"},
        )

    if "diferenca entre problema aberto e conjectura" in t or "diferença entre problema aberto e conjectura" in t:
        return RespostaChat(
            "Problema aberto é uma pergunta ainda sem solução aceita. Conjectura é uma afirmação específica que parece verdadeira, mas ainda não tem prova. Exemplo: 'P versus NP?' é problema aberto; 'Goldbach forte' é uma conjectura dentro de teoria dos números. O PSF deve separar os dois para não fingir prova.",
            "comparacao_meta_cientifica",
            detectar_tom(texto),
            92,
            origem="base_canonica:META-001/META-002",
            conhecimento_encontrado=True,
            contexto_chat={"ultimo_titulo": "Problema aberto vs conjectura", "ultima_origem": "base_canonica:META"},
        )

    if "conteudo novo" in t or "conteúdo novo" in t or "trouxer conteudo" in t or "trouxer conteúdo" in t:
        return RespostaChat(
            "Se trouxeres conteúdo novo, o caminho correto é: registrar como entrada nova, classificar o tipo, criar resposta curta, aula, teste e lacuna se existir, reindexar e só depois dizer que o PSF conhece aquilo. Não devo fingir que já estava materializado.",
            "entrada_conhecimento_novo",
            detectar_tom(texto),
            88,
            origem="regra_materializacao",
            conhecimento_encontrado=True,
            contexto_chat={"ultimo_titulo": "Conteúdo novo", "ultima_origem": "regra_materializacao"},
        )

    if "faz uma pergunta" in t or "faz pergunta" in t or "pergunta para mim" in t:
        return RespostaChat(
            "Pergunta para treinar: explica com as tuas palavras por que multiplicar por zero dá zero. Depois eu posso corrigir, simplificar ou pedir outro exemplo.",
            "gerar_pergunta_treino",
            detectar_tom(texto),
            84,
            origem="chat_vivo_treino",
            conhecimento_encontrado=True,
            contexto_chat={"ultimo_titulo": "Pergunta de treino", "ultima_origem": "chat_vivo_treino"},
        )

    perguntas_contextuais = (
        "onde esta este conhecimento",
        "de que fonte veio",
        "de que etapa veio",
        "tem teste",
        "tem aula",
        "tem prova",
        "tem lacuna",
        "contradiz algo anterior",
        "qual passo",
        "que passo",
        "passo voce usou",
        "passo você usou",
    )
    if any(p in t for p in perguntas_contextuais):
        ultimo = contexto.get("ultimo_titulo") or contexto.get("ultimo_registro_id") or contexto.get("ultimo_curiosidade_numero")
        if not ultimo:
            return RespostaChat(
                "Consigo responder isso, mas preciso saber de qual assunto estás a falar. Pergunta primeiro o tema ou escreve, por exemplo: 'Bhaskara tem teste?', 'Hipótese de Riemann tem lacuna?' ou 'de onde veio a resposta sobre padrões de Turing?'.",
                "auditoria_sem_contexto",
                detectar_tom(texto),
                78,
                origem="chat_vivo_contexto",
                conhecimento_encontrado=False,
                lacunas=["pergunta de auditoria sem assunto anterior"],
            )

    if "esta pronto para uso" in t or "pronto para uso" in t:
        return RespostaChat(
            "Como chat vivo, o PSF está pronto para uso de teste local: identidade, conversa informal, aulas básicas, curiosidades materializadas, fórmulas e problemas abertos já passam pela entrada única. Ainda deve ser tratado como projeto em melhoria contínua, não como produto final perfeito. O critério honesto é rodar verificar_integridade.py e python3 -m pytest -q antes de confiar na versão.",
            "estado_uso",
            detectar_tom(texto),
            86,
            origem="auditoria_chat_vivo",
            conhecimento_encontrado=True,
        )

    return None

