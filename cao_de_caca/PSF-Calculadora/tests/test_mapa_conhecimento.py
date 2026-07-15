import json
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
GRAFO = json.loads(
    (RAIZ / "docs" / "mapa_conhecimento_361_1000.json").read_text(
        encoding="utf-8"
    )
)


def test_preserva_todas_as_aulas_sem_lacunas():
    numeros = [aula["aula"] for aula in GRAFO["aulas"]]
    assert numeros == list(range(361, 1001))


def test_arestas_sao_validas_e_unicas():
    ids = {no["id"] for no in GRAFO["nos"]}
    arestas = {
        (aresta["origem"], aresta["destino"], aresta["tipo"])
        for aresta in GRAFO["arestas"]
    }
    assert len(arestas) == len(GRAFO["arestas"])
    assert all(origem in ids and destino in ids for origem, destino, _ in arestas)


def test_toda_aula_tem_ligacao_estrutural():
    pertencimentos = {
        aresta["origem"]
        for aresta in GRAFO["arestas"]
        if aresta["tipo"] == "pertence_a"
    }
    assert pertencimentos == {f"aula:{numero}" for numero in range(361, 1001)}


def test_toda_aula_tem_estado_documentado():
    estados = {"TEMOS", "PARCIAL", "NAO_TEMOS"}
    assert all(aula["status"] in estados for aula in GRAFO["aulas"])


def test_aulas_biologicas_possuem_motores_especificos():
    esperados = {
        361: "modelos_populacionais_novo",
        362: "presa_predador_novo",
        363: "propagacao_doencas",
        364: "reacao_difusao",
        365: "filogenetica",
        366: "smith_waterman",
        367: "dobramento_proteinas",
        368: "redes_genicas_booleanas",
        369: "hodgkin_huxley",
        370: "l_systems",
    }
    por_numero = {aula["aula"]: aula for aula in GRAFO["aulas"]}
    for numero, motor in esperados.items():
        assert por_numero[numero]["status"] == "TEMOS"
        assert motor in por_numero[numero]["evidencias"]


def test_motores_sem_relacao_ficam_documentados():
    ligados = {
        aresta["destino"].removeprefix("motor:")
        for aresta in GRAFO["arestas"]
        if aresta["destino"].startswith("motor:")
    }
    documentados = set(GRAFO["metadata"]["motores_sem_ligacao"])
    todos = {no["id"].removeprefix("motor:") for no in GRAFO["nos"] if no["tipo"] == "motor"}
    assert documentados == todos - ligados
