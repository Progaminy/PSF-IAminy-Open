"""GPS do conhecimento: navegação real sobre o mesmo grafo de dependências
que gera os pacotes/aulas (`ensino/pacotes_reais.py`). As perguntas que o
PSF se faz, pedidas pelo autor:

    onde estou? onde vou? quais são os caminhos?
    qual é a melhor via? qual é o caminho mais perto? qual é o mais longo?
    onde passo, e em cada rua passo em quê?
    a partir daqui, quais destinos são possíveis?
    a partir daqui, posso chegar a qualquer lugar?

O grafo de dependências (Português e Matemática) é um DAG (0 ciclos, já
confirmado pela auditoria estrutural em `motor/coerencia.py`) -- por isso
"caminho mais longo" é computável em tempo polinomial (programação dinâmica
sobre ordem topológica), não precisa de heurística.

Nada aqui inventa ligação: toda aresta usada já vem de `depende_de` real.
Quando não existe caminho entre dois conceitos, a resposta é honesta
(`existe=False`), nunca um caminho aproximado.
"""
from __future__ import annotations

from dataclasses import dataclass

from interface.mapa_conhecimento import dados_matematica, dados_portugues

_GERADORES = {"portugues": dados_portugues, "matematica": dados_matematica}


@dataclass(frozen=True, slots=True)
class Localizacao:
    conceito: str
    tema: str
    depende_de: tuple[str, ...]
    dependentes: tuple[str, ...]
    e_raiz: bool
    e_folha: bool


@dataclass(frozen=True, slots=True)
class Caminho:
    origem: str
    destino: str
    existe: bool
    conceitos: tuple[str, ...]
    comprimento: int


class _Grafo:
    """Índice reaproveitável -- monta uma vez, responde várias perguntas."""

    def __init__(self, area: str) -> None:
        gerador = _GERADORES.get(area)
        if gerador is None:
            raise ValueError(f"área desconhecida: {area!r}")
        dados = gerador()
        self.nomes = [n["nome"] for n in dados["nodes"] if n.get("tipo") != "raiz"]
        self._indice = {nome: i for i, nome in enumerate(self.nomes)}
        self._nodes = [n for n in dados["nodes"] if n.get("tipo") != "raiz"]
        n = len(self.nomes)
        self.saida: list[list[int]] = [[] for _ in range(n)]
        self.entrada: list[list[int]] = [[] for _ in range(n)]
        for a, b in dados["edges"]:
            nome_a, nome_b = dados["nodes"][a]["nome"], dados["nodes"][b]["nome"]
            if nome_a in self._indice and nome_b in self._indice:
                ia, ib = self._indice[nome_a], self._indice[nome_b]
                self.saida[ia].append(ib)
                self.entrada[ib].append(ia)

    def indice(self, nome: str) -> "int | None":
        return self._indice.get(nome)

    def localizar(self, nome: str) -> "Localizacao | None":
        i = self.indice(nome)
        if i is None:
            return None
        no = self._nodes[i]
        deps = tuple(self.nomes[p] for p in self.entrada[i])
        dependentes = tuple(self.nomes[s] for s in self.saida[i])
        return Localizacao(
            conceito=nome, tema=no["tema"], depende_de=deps, dependentes=dependentes,
            e_raiz=not deps, e_folha=not dependentes,
        )

    def alcancaveis_de(self, nome: str) -> tuple[str, ...]:
        """Todo destino possível a partir daqui, seguindo só arestas reais para a frente."""
        i = self.indice(nome)
        if i is None:
            return ()
        vistos = set()
        pilha = list(self.saida[i])
        while pilha:
            atual = pilha.pop()
            if atual in vistos:
                continue
            vistos.add(atual)
            pilha.extend(self.saida[atual])
        return tuple(sorted(self.nomes[i] for i in vistos))

    def caminho_mais_curto(self, origem: str, destino: str) -> Caminho:
        i, j = self.indice(origem), self.indice(destino)
        if i is None or j is None:
            return Caminho(origem, destino, False, (), 0)
        anterior = {i: None}
        fila = [i]
        cabeca = 0
        while cabeca < len(fila):
            atual = fila[cabeca]
            cabeca += 1
            if atual == j:
                break
            for prox in self.saida[atual]:
                if prox not in anterior:
                    anterior[prox] = atual
                    fila.append(prox)
        if j not in anterior:
            return Caminho(origem, destino, False, (), 0)
        sequencia = []
        no = j
        while no is not None:
            sequencia.append(self.nomes[no])
            no = anterior[no]
        sequencia.reverse()
        return Caminho(origem, destino, True, tuple(sequencia), len(sequencia) - 1)

    def caminho_mais_longo(self, origem: str, destino: str) -> Caminho:
        """DAG -> programação dinâmica sobre ordem topológica, sem heurística."""
        i, j = self.indice(origem), self.indice(destino)
        if i is None or j is None:
            return Caminho(origem, destino, False, (), 0)
        ordem = self._ordem_topologica()
        posicao_na_ordem = {no: p for p, no in enumerate(ordem)}
        melhor_comprimento = {i: 0}
        melhor_anterior: dict[int, "int | None"] = {i: None}
        for no in ordem[posicao_na_ordem[i]:]:
            if no not in melhor_comprimento:
                continue
            for prox in self.saida[no]:
                candidato = melhor_comprimento[no] + 1
                if candidato > melhor_comprimento.get(prox, -1):
                    melhor_comprimento[prox] = candidato
                    melhor_anterior[prox] = no
        if j not in melhor_comprimento:
            return Caminho(origem, destino, False, (), 0)
        sequencia = []
        no = j
        while no is not None:
            sequencia.append(self.nomes[no])
            no = melhor_anterior[no]
        sequencia.reverse()
        return Caminho(origem, destino, True, tuple(sequencia), len(sequencia) - 1)

    def _ordem_topologica(self) -> list[int]:
        n = len(self.nomes)
        grau_entrada = [len(self.entrada[i]) for i in range(n)]
        fila = [i for i in range(n) if grau_entrada[i] == 0]
        ordem = []
        cabeca = 0
        while cabeca < len(fila):
            atual = fila[cabeca]
            cabeca += 1
            ordem.append(atual)
            for prox in self.saida[atual]:
                grau_entrada[prox] -= 1
                if grau_entrada[prox] == 0:
                    fila.append(prox)
        return ordem

    def componentes_conectados(self) -> tuple[tuple[str, ...], ...]:
        """Ignora direção -- só quer saber quem consegue chegar a quem, de algum
        jeito. Cada componente é uma "ilha": nada de uma liga a nada de outra.
        Honesto sobre fragmentação real -- não finge um grafo mais unido do
        que é.
        """
        n = len(self.nomes)
        nao_dirigido: list[list[int]] = [[] for _ in range(n)]
        for a in range(n):
            for b in self.saida[a]:
                nao_dirigido[a].append(b)
                nao_dirigido[b].append(a)
        visitado = [False] * n
        componentes = []
        for inicio in range(n):
            if visitado[inicio]:
                continue
            pilha = [inicio]
            visitado[inicio] = True
            componente = []
            while pilha:
                atual = pilha.pop()
                componente.append(atual)
                for viz in nao_dirigido[atual]:
                    if not visitado[viz]:
                        visitado[viz] = True
                        pilha.append(viz)
            componentes.append(tuple(sorted(self.nomes[i] for i in componente)))
        return tuple(sorted(componentes, key=len, reverse=True))


_CACHE: dict[str, _Grafo] = {}


def _grafo(area: str) -> _Grafo:
    if area not in _CACHE:
        _CACHE[area] = _Grafo(area)
    return _CACHE[area]


def onde_estou(conceito: str, area: str = "portugues") -> "Localizacao | None":
    return _grafo(area).localizar(conceito)


def alcancaveis_de(conceito: str, area: str = "portugues") -> tuple[str, ...]:
    return _grafo(area).alcancaveis_de(conceito)


def caminho_mais_curto(origem: str, destino: str, area: str = "portugues") -> Caminho:
    return _grafo(area).caminho_mais_curto(origem, destino)


def caminho_mais_longo(origem: str, destino: str, area: str = "portugues") -> Caminho:
    return _grafo(area).caminho_mais_longo(origem, destino)


def componentes_conectados(area: str = "portugues") -> tuple[tuple[str, ...], ...]:
    """Regra 4.1, parte honesta: em vez de fingir "tudo é um círculo só",
    devolve as ilhas reais. Se houver mais de uma, o grafo NÃO está todo
    ligado -- e isto é o que decide o que "isolar" na regra 5.
    """
    return _grafo(area).componentes_conectados()
