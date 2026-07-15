"""Dados do mapa/teia de conhecimento -- Português, Matemática e as pontes reais entre os dois.

Lógica pura (sem HTTP), mesmo padrão de `roteador.py`: testável direto,
sem abrir socket. Cada nó e cada ligação vem de dados que o motor já expõe
de verdade (`MotorPortugues.conhecimento_puro()`, `ConhecimentoMatematico`,
`matematica.resolucao_pontes`) -- nada aqui inventa uma ligação nova. Uma
ponte entre Português e Matemática só entra na lista se os dois nomes
existirem de facto nos dois grafos já construídos; candidatos sem par real
dos dois lados (ex.: "numeral coletivo") ficam de fora.
"""
from __future__ import annotations

from lingua_portuguesa import MotorPortugues
from matematica.conhecimento import ConhecimentoMatematico
from matematica.resolucao_pontes import normalizar_termo, resolver_dependencia

from .mapa_cao_de_caca import dados_cao_de_caca

# Pares verificados manualmente nos dois lados antes de entrar aqui -- ver
# PLANO_PSF_IAMINY.md item 312 para a lista completa e os candidatos
# descartados por falta de par real (numeral coletivo, lógica<->argumento).
_PONTES_CANDIDATAS: tuple[tuple[str, str], ...] = (
    ("algarismo arábico", "contas armadas"),
    ("numeral cardinal", "contagem finita"),
    ("numeral ordinal", "ordem total"),
    ("número por extenso", "contagem finita"),
    ("numeral multiplicativo", "principio multiplicativo"),
    ("numeral fracionário", "ponte racionais reais"),
    ("grafia de percentagem", "porcentagem"),
    ("separador decimal", "ponte racionais reais"),
    ("separador de milhares", "contas armadas"),
    ("grafia de hora", "conversao unidades"),
    ("grafia de data", "conversao unidades"),
    ("símbolo de unidade", "medidas e grandezas"),
)


def _bloco_matematico(marcador: int) -> str:
    if marcador < 100:
        return "fundamentos (1-99)"
    if marcador < 200:
        return "álgebra e grafos (100-199)"
    if marcador < 400:
        return "lógica e linguagens (200-399)"
    if marcador < 1000:
        return "provas e modelos (400-999)"
    return "reais, cálculo e avançado (1000+)"


def dados_portugues(motor: "MotorPortugues | None" = None) -> dict:
    """Grafo real do Português: um nó por conceito puro, uma aresta por depende_de resolvido."""
    motor = motor or MotorPortugues()
    conceitos = sorted(motor.conhecimento_puro(), key=lambda c: (c.tema_consulta, c.ordem))
    indice = {c.nome: i for i, c in enumerate(conceitos)}

    nodes = [
        {
            "nome": c.nome,
            "tema": c.tema_consulta,
            "ordem": c.ordem,
            "construcao": c.construcao,
            "funcao": c.funcao,
            "deps": list(c.depende_de),
            "exemplos_minimos": list(c.exemplos_minimos),
        }
        for c in conceitos
    ]
    edges = [
        [indice[dep], indice[c.nome]]
        for c in conceitos
        for dep in c.depende_de
        if dep in indice
    ]
    _marcar_graus(nodes, edges)
    temas = sorted({c.tema_consulta for c in conceitos})
    return {"nodes": nodes, "edges": edges, "temas": temas}


def dados_matematica(conhecimento: "ConhecimentoMatematico | None" = None) -> dict:
    """Grafo real da Matemática, incluindo primitivas fundacionais ("raiz: nome") citadas
    como dependência real mas sem etapa própria -- sem elas, a maioria dos conceitos
    apareceria falsamente isolada, já que suas dependências apontam para primitivas
    (adição, lógica booleana, ...) e não para outros conceitos documentados.
    """
    ck = conhecimento or ConhecimentoMatematico()
    conceitos = sorted(ck.todos(), key=lambda c: c.marcador_historico)
    nomes = {normalizar_termo(c.nome) for c in conceitos}
    por_norm = {normalizar_termo(c.nome): c.nome for c in conceitos}

    nodes: list[dict] = []
    indice: dict[str, int] = {}

    def adicionar(
        nome: str, tema: str, tipo: str, construcao: str = "", deps: "list[str] | None" = None,
        exemplos_minimos: "tuple[str, ...]" = (),
    ) -> None:
        indice[nome] = len(nodes)
        nodes.append({
            "nome": nome, "tema": tema, "tipo": tipo, "construcao": construcao,
            "deps": deps or [], "exemplos_minimos": list(exemplos_minimos),
        })

    for c in conceitos:
        adicionar(
            c.nome, _bloco_matematico(c.marcador_historico), "conceito", c.construcao,
            list(c.dependencias_declaradas), c.exemplos_minimos,
        )

    edges: list[list[int]] = []
    for c in conceitos:
        alvo = indice[c.nome]
        for dep in c.dependencias_declaradas:
            estado, origem = resolver_dependencia(dep, nomes)
            if estado in ("CONCEITO", "ALIAS", "REFERENCIA_DE_MODULO") and origem in por_norm:
                # REFERENCIA_DE_MODULO ("depende do módulo inteiro X") é tratada
                # como dependência resolvida pelo próprio `auditar_resolucao_pontes`
                # do projeto (não é lacuna) -- teria que ganhar uma linha aqui
                # também, senão o mapa fica mais desconfiado da ligação do que o
                # motor que a validou.
                fonte_nome = por_norm[origem]
                if fonte_nome in indice:
                    edges.append([indice[fonte_nome], alvo])
            elif estado == "RAIZ":
                raiz_nome = f"raiz: {origem}"
                if raiz_nome not in indice:
                    adicionar(raiz_nome, "primitivas", "raiz")
                edges.append([indice[raiz_nome], alvo])
            elif estado == "GRUPO_DE_CONCEITOS" and origem:
                # origem é uma string composta "a + b + c" -- só desenha uma
                # linha para cada parte que já é de facto um nó real; partes
                # sem par real ficam de fora, mesma regra de sempre.
                for parte in origem.split(" + "):
                    fonte_nome = por_norm.get(parte)
                    if fonte_nome is not None and fonte_nome in indice:
                        edges.append([indice[fonte_nome], alvo])

    _marcar_graus(nodes, edges)
    temas = sorted({n["tema"] for n in nodes})
    return {"nodes": nodes, "edges": edges, "temas": temas}


def dados_pontes(pt: dict, mat: dict) -> list[dict]:
    """Só entra ponte cujos dois nomes existem de facto nos dois grafos já construídos."""
    pt_indice = {n["nome"]: i for i, n in enumerate(pt["nodes"])}
    mat_indice = {n["nome"]: i for i, n in enumerate(mat["nodes"])}
    mat_por_norm = {normalizar_termo(n["nome"]): n["nome"] for n in mat["nodes"]}

    pontes = []
    for nome_pt, busca_mat in _PONTES_CANDIDATAS:
        nome_mat = mat_por_norm.get(normalizar_termo(busca_mat))
        if nome_pt in pt_indice and nome_mat is not None and nome_mat in mat_indice:
            pontes.append({
                "pt": nome_pt, "pt_idx": pt_indice[nome_pt],
                "mat": nome_mat, "mat_idx": mat_indice[nome_mat],
            })
    return pontes


def _marcar_graus(nodes: list[dict], edges: list[list[int]]) -> None:
    graus = [0] * len(nodes)
    for a, b in edges:
        graus[a] += 1
        graus[b] += 1
    for i, g in enumerate(graus):
        nodes[i]["grau"] = g


def mapa_completo() -> dict:
    """Payload único servido por /api/mapa: os dois grafos reais e as pontes reais entre eles,
    mais o catálogo do cão de caça -- deliberadamente sem nenhuma ponte para os outros dois,
    porque não é conhecimento PSF, é ferramenta de cálculo com dependência externa.
    """
    pt = dados_portugues()
    mat = dados_matematica()
    pontes = dados_pontes(pt, mat)
    cao_de_caca = dados_cao_de_caca()
    return {"pt": pt, "mat": mat, "pontes": pontes, "cao_de_caca": cao_de_caca}
