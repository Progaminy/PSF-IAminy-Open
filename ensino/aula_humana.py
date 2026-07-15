"""Transformação de conhecimento técnico em aula humana.

O motor não cria conhecimento do nada. Ele reorganiza conhecimento existente em
forma de professor: começa no chão, mostra a ideia, constrói, dá exemplo,
previne erro comum, propõe prática e mostra a fronteira. O pedido do aluno pode
mudar o foco: simples, exemplo, exercícios, resumo ou desmontagem.
"""
from __future__ import annotations

from ensino.tipos import AulaPacote
from ensino.aulas_infinitas import AulaConhecimento
from ensino.conversa_fluida import normalizar_pedido


def _modo(pedido: str) -> str:
    normal = normalizar_pedido(pedido)
    if any(chave in normal for chave in ("mais simples", "nao entendi", "nao percebi", "sem formula", "como criança", "do zero")):
        return "simples"
    if any(chave in normal for chave in ("outro exemplo", "exemplo", "caso concreto", "pratico")):
        return "exemplo"
    if any(chave in normal for chave in ("exercicio", "atividade", "praticar", "treino")):
        return "exercicios"
    if any(chave in normal for chave in ("resumo", "curto", "poucas palavras", "so a ideia")):
        return "resumo"
    if any(chave in normal for chave in ("desmonta", "passo a passo", "por partes", "construir do zero", "reconstruir")):
        return "desmontada"
    return "completa"


def humanizar_pacote(aula: AulaPacote, pedido: str = "") -> str:
    p = aula.pacote
    modo = _modo(pedido)
    exemplo = p.exemplos[0] if p.exemplos else "Constrói um exemplo pequeno com objetos reais."
    exercicio = p.exercicios[0] if p.exercicios else "Refaz a ideia com outro número ou outra palavra."
    passos = "\n".join(f"{i}. {passo}" for i, passo in enumerate(p.passos, 1))
    desmontagem = "\n".join(f"- {linha}" for linha in p.desmontagem[:5])
    pre = ", ".join(p.pre_requisitos) if p.pre_requisitos else "nenhum; começa do chão"

    if modo == "resumo":
        return "\n".join((f"{p.codigo} — {p.titulo}", "Resumo humano", p.objetivo, f"Ideia: {p.explicacao}", f"Exemplo mínimo: {exemplo}"))

    if modo == "exemplo":
        exemplos = p.exemplos or (exemplo,)
        return "\n".join((
            f"{p.codigo} — {p.titulo}",
            "Vamos ver por exemplos, sem pressa.",
            "Ideia antes do exemplo",
            p.explicacao,
            "",
            "Exemplos guiados",
            *[f"{i}. {item}" for i, item in enumerate(exemplos, 1)],
            "",
            "Agora tenta",
            exercicio,
        ))

    if modo == "exercicios":
        exercicios = p.exercicios or (exercicio,)
        return "\n".join((
            f"{p.codigo} — {p.titulo}",
            "Treino humano: primeiro faço um, depois tu fazes.",
            f"Modelo: {exemplo}",
            "",
            "Exercícios",
            *[f"{i}. {item}" for i, item in enumerate(exercicios, 1)],
            "",
            "Como corrigir",
            "Confere se cada passo respeita a ideia central e não pula a construção.",
        ))

    abertura = "Vou explicar pelo modo PSF: primeiro o conceito, depois o símbolo."
    if modo == "simples":
        abertura = "Vou simplificar: uma ideia de cada vez, sem fórmula pronta."
    elif modo == "desmontada":
        abertura = "Vou desmontar: chão, peças, montagem, teste e uso."

    return "\n".join(
        (
            f"{p.codigo} — {p.titulo}",
            abertura,
            f"Pré-requisitos: {pre}.",
            "",
            "1. Chão humano",
            "Antes de qualquer símbolo, olha para a situação concreta: que coisa existe e que ação queremos fazer com ela?",
            "",
            "2. Ideia central",
            p.objetivo,
            "",
            "3. Construção do zero",
            p.explicacao,
            "",
            "4. Passos falados",
            passos,
            "",
            "5. Exemplo pequeno",
            exemplo,
            "",
            "6. Desmontagem PSF",
            desmontagem,
            "",
            "7. Erro comum",
            "Decorar o resultado sem saber de onde ele veio. No PSF, o símbolo vem depois da construção.",
            "",
            "8. Exercício para fixar",
            exercicio,
            "",
            "Quando quiseres, podes dizer: 'mais simples', 'dá outro exemplo', 'exercícios', 'resumo' ou 'continua'.",
        )
    )


def humanizar_conhecimento(aula: AulaConhecimento, pedido: str = "") -> str:
    modo = _modo(pedido)
    if not aula.construida:
        return aula.texto + "\n\nModo honesto: isto ainda é fronteira. Primeiro construímos, depois ensinamos."

    linhas = [l.strip() for l in aula.texto.splitlines() if l.strip()]
    ideias = [l for l in linhas if l.startswith("- ")][:10]
    if not ideias:
        ideias = ["- Ler o documento de origem e extrair o primeiro conceito estável."]

    if modo == "resumo":
        return "\n".join((
            f"{aula.codigo} — {aula.titulo}",
            "Resumo humano do conhecimento PSF construído.",
            f"Origem: {aula.origem}.",
            *ideias[:4],
        ))

    if modo == "exemplo":
        return "\n".join((
            f"{aula.codigo} — {aula.titulo}",
            "Exemplo PSF mínimo",
            "1. Escolhe o menor caso em que o conceito aparece.",
            "2. Nomeia os objetos anteriores que ele usa.",
            "3. Aplica a construção uma peça de cada vez.",
            "4. Só no fim compara com a forma clássica, se existir.",
            "",
            "Ideias usadas nesta etapa",
            *ideias[:6],
        ))

    if modo == "exercicios":
        return "\n".join((
            f"{aula.codigo} — {aula.titulo}",
            "Exercícios PSF",
            "1. Explica esta etapa com palavras próprias, sem fórmula pronta.",
            "2. Diz quais conceitos anteriores ela usa.",
            "3. Cria um exemplo mínimo e testa se a construção funciona.",
            "4. Escreve uma pergunta que ainda fica na fronteira.",
        ))

    abertura = "Aula humana gerada do conhecimento PSF construído."
    if modo == "simples":
        abertura = "Vou simplificar esta etapa PSF: chão primeiro, símbolo depois."
    elif modo == "desmontada":
        abertura = "Vou desmontar esta etapa PSF por construção."

    return "\n".join(
        (
            f"{aula.codigo} — {aula.titulo}",
            abertura,
            f"Origem: {aula.origem}.",
            "",
            "1. Chão da aula",
            "Não começo por fórmula pronta. Começo por perguntar: que objeto existe, que relação aparece e que operação nasce daí?",
            "",
            "2. Ideia reconstruída",
            *ideias,
            "",
            "3. Como aplicar",
            "1. Escolhe um caso pequeno.",
            "2. Reconstrói usando os conceitos anteriores.",
            "3. Testa contra um exemplo clássico só no fim.",
            "4. Se o teste falhar, o conceito volta para revisão.",
            "",
            "4. Erro comum",
            "Usar uma fórmula conhecida antes de o PSF ter reconstruído a razão dela existir.",
            "",
            "5. Exercício PSF",
            "Explica esta etapa com um exemplo mínimo e diz quais conceitos anteriores ela usa.",
            "",
            "Podes responder com: 'mais simples', 'outro exemplo', 'exercícios', 'resumo' ou 'continua'.",
        )
    )
