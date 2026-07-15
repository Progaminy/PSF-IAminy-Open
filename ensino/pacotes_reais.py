"""Pacotes reais: aulas derivadas direto do conhecimento puro já construído
(Português: 1139 conceitos; Matemática: 189 conceitos + primitivas), não do
currículo de pacotes antigo (`curriculos.py`, nível 0-N, escrito à mão para
pré-numeracia). Regra do autor, do zero:

    0. Sem fluxo/ligação real no grafo de dependências, não existe aula.
    1. Do zero, organizado em pacotes -- nunca por "classe" ou "nível".
    2. Um pacote é um caminho reto no grafo de dependências: anda em frente
       enquanto o nó atual tiver exatamente 1 dependência e exatamente 1
       dependente ainda não visitado. Pára exatamente no nó onde o caminho
       encontra 3 ou mais vias (contando de onde veio + para onde pode ir) --
       esse nó é o "entroncamento": o que estava vindo, mais os 2+ caminhos
       possíveis. Ali, o pacote atual termina (incluindo o próprio
       entroncamento) e um pacote novo nasce para cada caminho que sai dele.
       O comprimento do pacote nunca é escolhido -- é o que o grafo real dá:
       pode ser 1 conceito, pode ser 1000, se não houver nenhum entroncamento
       no meio.
    3. Um conceito, uma aula.
    4. Um fluxo (um trecho reto do grafo) é um pacote.
    5-7. Cada aula é gerada com o que já existe de verdade no conceito --
       `construcao` (explicação), `funcao`, `exemplos_minimos` (exemplo) --
       nunca texto pedagógico inventado à parte.
    8-9. Exercícios (e as suas correções): quando o conceito compõe de um
       primitivo formal real (`ensino/exercicio_real.py` -- soma, subtração,
       multiplicação, divisão, potência, MDC/MMC, comparação,
       divisibilidade, paridade), a pergunta PRINCIPAL é sempre "aplique a
       construção numa variação sorteada", em notação de papel, verificada
       contra o mesmo primitivo formal (Church) que calcula por dentro --
       nunca "cite uma dependência", que testaria memória do grafo, não uso
       do conceito. Para o resto (sem função executável), o exercício nasce
       do próprio grafo como antes, mas em linguagem de professor: "o que
       você precisa saber antes de aprender X" no lugar de "cite uma
       dependência de X" -- nunca um enunciado pedagógico à parte, sempre
       uma pergunta cuja resposta certa já existe no conceito.
    10. Verificação da resposta do aluno: para pergunta estruturada
       (dependência/dependente/verdadeiro-falso) a checagem é exata contra o
       grafo real. Para pergunta aberta (função/exemplo) não existe
       "verificação semântica" de verdade sem um modelo de linguagem -- e
       este projeto não usa isso como fundamento. Em vez de fingir
       compreensão, mede semelhança textual honesta (mesma técnica e mesma
       ressalva já usada em `MotorAuxiliarValidacao.comparar_portugues`:
       `difflib.SequenceMatcher`), sempre devolvendo o grau de semelhança,
       nunca só sim/não.

Isto não muda nem lê `curriculos.py` -- são sistemas paralelos, um herdado
(pré-numeracia manual) e este novo (derivado do grafo real).
"""
from __future__ import annotations

from dataclasses import dataclass
from difflib import SequenceMatcher

from interface.mapa_conhecimento import dados_matematica, dados_portugues

from .exercicio_real import (
    ExercicioReal,
    gerar_exercicio_real,
    tem_gerador_real,
    verificar_resposta_real,
)


@dataclass(frozen=True, slots=True)
class Aula:
    conceito: str
    tema: str
    explicacao: str
    funcao: str
    exemplos: tuple[str, ...]
    depende_de: tuple[str, ...]
    dependentes: tuple[str, ...] = ()

    @property
    def completa(self) -> bool:
        """Regra 7: toda aula deve ter explicação e exemplo -- nunca uma delas vazia."""
        return bool(self.explicacao) and bool(self.exemplos)

    def texto(self) -> str:
        """Formato de renderização único da aula: conceito, explicação, exemplo, ligações.

        As ligações (o que vem antes/depois no grafo) aparecem como frase de
        professor, nunca como rótulo de grafo ("Depende de: x") -- um humano
        lendo a aula não precisa saber que existe um grafo por trás.
        """
        linhas = [self.conceito.upper(), "", self.explicacao]
        if self.funcao:
            linhas += ["", "Função: " + self.funcao]
        if self.exemplos:
            linhas += ["", "Exemplo:"] + [f"  - {e}" for e in self.exemplos]
        if self.depende_de:
            linhas += ["", f"Para entender isto, você já precisa saber: {_juntar_e(self.depende_de)}."]
        else:
            linhas += ["", "Este é um ponto de partida -- não precisa de nada antes para entender."]
        if self.dependentes:
            linhas += ["", f"Aprender isto ajuda a entender depois: {_juntar_e(self.dependentes)}."]
        return "\n".join(linhas)


def _juntar_e(itens: tuple[str, ...]) -> str:
    """Lista em prosa: "a", "a e b", "a, b e c" -- nunca "a, b, c" com vírgulas cruas."""
    if len(itens) == 1:
        return itens[0]
    return ", ".join(itens[:-1]) + " e " + itens[-1]


@dataclass(frozen=True, slots=True)
class Pacote:
    codigo: str
    area: str
    aulas: tuple[Aula, ...]

    @property
    def entroncamento_final(self) -> str:
        return self.aulas[-1].conceito


def _segmentar(nodes: list[dict], edges: list[list[int]]) -> list[list[int]]:
    """Aplica a regra do entroncamento (grau total != 2) sobre o grafo real.

    Percorre por DFS com retrocesso a partir das raízes (sem pré-requisito):
    anda em frente por nós de passagem (1 dependência, 1 dependente ainda não
    visitado); pára -- incluindo o nó -- assim que o nó atual tiver 0 ou 2+
    sucessores, ou assim que o próximo nó já for outro entroncamento (2+
    pré-requisitos) ou já tiver sido visitado por outro pacote. Cada
    sucessor do ponto de parada vira o início de um pacote novo.
    """
    n = len(nodes)
    saida: list[list[int]] = [[] for _ in range(n)]
    entrada = [0] * n
    for a, b in edges:
        saida[a].append(b)
        entrada[b] += 1

    visitado = [False] * n
    pacotes: list[list[int]] = []

    def seguir(inicio: int) -> list[int]:
        pacote = [inicio]
        visitado[inicio] = True
        atual = inicio
        while True:
            sucessores = saida[atual]
            if len(sucessores) != 1:
                break
            proximo = sucessores[0]
            if visitado[proximo] or entrada[proximo] != 1:
                break
            pacote.append(proximo)
            visitado[proximo] = True
            atual = proximo
        return pacote

    def dfs(inicio: int) -> None:
        if visitado[inicio]:
            return
        pacote = seguir(inicio)
        pacotes.append(pacote)
        for proximo in saida[pacote[-1]]:
            dfs(proximo)

    raizes = [i for i in range(n) if entrada[i] == 0]
    for r in raizes:
        dfs(r)
    # nós só alcançáveis por convergência (nunca raiz, sempre visitados por
    # outro caminho primeiro) -- cobertura honesta do resto do grafo.
    for i in range(n):
        if not visitado[i]:
            dfs(i)

    return pacotes


def _dependentes_por_nome(nodes: list[dict]) -> dict[str, tuple[str, ...]]:
    """Índice reverso completo (não só intra-pacote): quem cita cada nome em depende_de."""
    mapa: dict[str, list[str]] = {n["nome"]: [] for n in nodes}
    for n in nodes:
        for dep in n.get("deps", ()):
            if dep in mapa:
                mapa[dep].append(n["nome"])
    return {nome: tuple(dependentes) for nome, dependentes in mapa.items()}


def _aula_de_no(no: dict, dependentes: dict[str, tuple[str, ...]]) -> Aula:
    return Aula(
        conceito=no["nome"],
        tema=no["tema"],
        explicacao=no.get("construcao", ""),
        funcao=no.get("funcao", ""),
        exemplos=tuple(no.get("exemplos_minimos", ())),
        depende_de=tuple(no.get("deps", ())),
        dependentes=dependentes.get(no["nome"], ()),
    )


def pacotes_portugues() -> tuple[Pacote, ...]:
    dados = dados_portugues()
    nodes = dados["nodes"]
    dependentes = _dependentes_por_nome(nodes)
    segmentos = _segmentar(nodes, dados["edges"])
    return tuple(
        Pacote(
            codigo=f"PT-{i + 1:04d}",
            area="portugues",
            aulas=tuple(_aula_de_no(nodes[idx], dependentes) for idx in segmento),
        )
        for i, segmento in enumerate(segmentos)
    )


def pacotes_matematica() -> tuple[Pacote, ...]:
    dados = dados_matematica()
    indice_antigo_para_novo = {}
    nodes_reindexados = []
    for i, n in enumerate(dados["nodes"]):
        if n.get("tipo") != "raiz":
            indice_antigo_para_novo[i] = len(nodes_reindexados)
            nodes_reindexados.append(n)
    edges = [
        [indice_antigo_para_novo[a], indice_antigo_para_novo[b]]
        for a, b in dados["edges"]
        if a in indice_antigo_para_novo and b in indice_antigo_para_novo
    ]
    dependentes = _dependentes_por_nome(nodes_reindexados)
    segmentos = _segmentar(nodes_reindexados, edges)
    return tuple(
        Pacote(
            codigo=f"MAT-{i + 1:04d}",
            area="matematica",
            aulas=tuple(_aula_de_no(nodes_reindexados[idx], dependentes) for idx in segmento),
        )
        for i, segmento in enumerate(segmentos)
    )


# ---------------------------------------------------------------------------
# Regras 8-10: exercícios, correção, treino com verificação honesta.
# ---------------------------------------------------------------------------

_LIMIAR_SEMELHANCA = 0.5


@dataclass(frozen=True, slots=True)
class Exercicio:
    conceito: str
    pergunta: str
    tipo: str  # "dependencia" | "dependente" | "raiz" | "funcao" | "exemplo"
    respostas_aceitas: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class Correcao:
    exercicio: Exercicio
    resposta_modelo: str


@dataclass(frozen=True, slots=True)
class ResultadoVerificacao:
    correto: bool
    semelhanca: float
    resposta_modelo: str
    metodo: str


def gerar_exercicios(aula: Aula, semente: "int | None" = None) -> tuple[Exercicio, ...]:
    """Um exercício por fato real já contido na aula -- nunca um enunciado
    pedagógico inventado à parte. Sem dependência real, sem dependente real,
    sem função ou sem exemplo, simplesmente não nasce aquele exercício
    (honesto: melhor ter menos do que fingir que existe).

    Quando o conceito compõe de um primitivo formal real (soma, subtração,
    multiplicação, divisão, potência, MDC/MMC, comparação, divisibilidade,
    paridade -- ver `exercicio_real.py`), o PRIMEIRO exercício é sempre
    "aplique a construção" numa variação sorteada, em notação de papel,
    verificada contra o mesmo primitivo formal que calcula por dentro. As
    perguntas sobre o grafo (o que vem antes/depois) continuam existindo,
    mas como secundárias, nunca como a primeira pergunta."""
    exercicios: list[Exercicio] = []
    c = aula.conceito
    if tem_gerador_real(c):
        real = gerar_exercicio_real(c, semente=semente)
        exercicios.append(Exercicio(c, real.enunciado, f"conta_real:{real.tipo}", (real.resposta_certa,)))
    if aula.depende_de:
        exercicios.append(Exercicio(c, f'O que você precisa saber antes de aprender "{c}"?', "dependencia", aula.depende_de))
        exercicios.append(Exercicio(
            c, f'Para entender "{c}", é preciso já saber "{aula.depende_de[0]}"? (sim/não)', "verdadeiro_falso", ("sim",)
        ))
    else:
        exercicios.append(Exercicio(c, f'"{c}" é um ponto de partida -- não precisa de nada antes? (sim/não)', "raiz", ("sim",)))
    if aula.dependentes:
        exercicios.append(Exercicio(c, f'O que fica mais fácil de entender depois que você aprende "{c}"?', "dependente", aula.dependentes))
    if aula.funcao:
        exercicios.append(Exercicio(c, f'Qual é a função de "{c}"?', "funcao", (aula.funcao,)))
    if aula.exemplos:
        exercicios.append(Exercicio(c, f'Dê um exemplo de "{c}".', "exemplo", aula.exemplos))
    return tuple(exercicios)


def gerar_corrigidos(aula: Aula, semente: "int | None" = None) -> tuple[Correcao, ...]:
    """Regra 9: exercício e correção juntos, mesma estrutura da aula."""
    return tuple(
        Correcao(exercicio=ex, resposta_modelo=ex.respostas_aceitas[0])
        for ex in gerar_exercicios(aula, semente=semente)
    )


def verificar_resposta(exercicio: Exercicio, resposta_aluno: str) -> ResultadoVerificacao:
    """Regra 10. Estruturado (dependência/dependente/verdadeiro-falso/raiz):
    checagem exata contra o grafo real -- 0.0 ou 1.0, nunca "quase". Aberto
    (função/exemplo): sem modelo de linguagem como fundamento, não existe
    verificação semântica de verdade -- mede semelhança textual honesta
    (mesma técnica de `MotorAuxiliarValidacao.comparar_portugues`) e devolve
    o grau, nunca só um sim/não fingindo compreensão.
    """
    if exercicio.tipo.startswith("conta_real:"):
        tipo_real = exercicio.tipo.split(":", 1)[1]
        resultado_real = verificar_resposta_real(
            ExercicioReal(exercicio.conceito, tipo_real, exercicio.pergunta, exercicio.respostas_aceitas[0]),
            resposta_aluno,
        )
        return ResultadoVerificacao(
            resultado_real.correto,
            1.0 if resultado_real.correto else 0.0,
            resultado_real.resposta_certa,
            "exato (conferido contra o primitivo formal de Church)",
        )
    resposta = resposta_aluno.strip().casefold()
    if exercicio.tipo in ("dependencia", "dependente"):
        certo = any(resposta == r.casefold() for r in exercicio.respostas_aceitas)
        return ResultadoVerificacao(certo, 1.0 if certo else 0.0, exercicio.respostas_aceitas[0], "exato")
    if exercicio.tipo in ("verdadeiro_falso", "raiz"):
        afirmativas = {"sim", "s", "verdadeiro", "certo"}
        negativas = {"nao", "não", "n", "falso", "errado"}
        esperado_sim = exercicio.respostas_aceitas[0] == "sim"
        certo = (resposta in afirmativas) if esperado_sim else (resposta in negativas)
        return ResultadoVerificacao(certo, 1.0 if certo else 0.0, exercicio.respostas_aceitas[0], "exato")
    semelhanca = max(
        SequenceMatcher(None, resposta, r.casefold()).ratio()
        for r in exercicio.respostas_aceitas
    )
    return ResultadoVerificacao(
        semelhanca >= _LIMIAR_SEMELHANCA,
        round(semelhanca, 3),
        exercicio.respostas_aceitas[0],
        "semelhança textual (não prova compreensão -- ver MotorAuxiliarValidacao)",
    )
