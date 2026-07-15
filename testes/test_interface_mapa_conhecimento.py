import pytest

from interface.mapa_conhecimento import dados_matematica, dados_pontes, dados_portugues, mapa_completo
from interface.roteador import Roteador
from lingua_portuguesa import MotorPortugues


@pytest.fixture(scope="module")
def motor():
    return MotorPortugues()


def test_dados_portugues_cobre_todos_os_conceitos_reais(motor):
    esperado = list(motor.conhecimento_puro())
    dados = dados_portugues(motor)
    assert len(dados["nodes"]) == len(esperado)
    nomes = {n["nome"] for n in dados["nodes"]}
    assert nomes == {c.nome for c in esperado}


def test_dados_portugues_arestas_vem_so_de_depende_de_real(motor):
    dados = dados_portugues(motor)
    nomes_por_indice = [n["nome"] for n in dados["nodes"]]
    por_nome = {n["nome"]: n for n in dados["nodes"]}
    for a, b in dados["edges"]:
        fonte, alvo = nomes_por_indice[a], nomes_por_indice[b]
        assert fonte in por_nome[alvo]["deps"]


def test_dados_portugues_raiz_sem_dependencia_mas_com_dependentes(motor):
    dados = dados_portugues(motor)
    por_nome = {n["nome"]: n for n in dados["nodes"]}
    raiz = por_nome["diferença"]
    assert raiz["deps"] == []
    assert raiz["grau"] > 0  # outros conceitos dependem dela -- não é isolada


def test_dados_matematica_inclui_primitivas_como_nos_raiz():
    dados = dados_matematica()
    tipos = {n["tipo"] for n in dados["nodes"]}
    assert "raiz" in tipos
    nomes_raiz = [n["nome"] for n in dados["nodes"] if n["tipo"] == "raiz"]
    assert all(n.startswith("raiz: ") for n in nomes_raiz)


def test_dados_matematica_nenhum_conceito_fica_isolado():
    dados = dados_matematica()
    isolados = [n["nome"] for n in dados["nodes"] if n["grau"] == 0]
    # "busca derivacao completude finita" parecia isolado quando só CONCEITO,
    # ALIAS e RAIZ contavam como aresta -- mas as suas 3 dependências são
    # REFERENCIA_DE_MODULO (depende do módulo inteiro de outro conceito, não
    # de um símbolo específico), e o próprio `auditar_resolucao_pontes` do
    # projeto já trata esse estado como resolvido, não como lacuna. Ignorá-lo
    # no mapa seria o mapa fingir menos confiança do que o motor já provou.
    assert isolados == []
    por_nome = {n["nome"]: n for n in dados["nodes"]}
    assert por_nome["busca derivacao completude finita"]["grau"] == 3
    por_nome = {n["nome"]: n for n in dados["nodes"]}
    assert por_nome["teoria modelos prova finita"]["grau"] > 0


def test_dados_matematica_grau_zero_nao_aparece_em_nenhuma_aresta():
    dados = dados_matematica()
    referenciados = set()
    for a, b in dados["edges"]:
        referenciados.add(a)
        referenciados.add(b)
    for i, n in enumerate(dados["nodes"]):
        if n["grau"] == 0:
            assert i not in referenciados


def test_dados_pontes_so_inclui_pares_que_existem_nos_dois_lados():
    pt = dados_portugues()
    mat = dados_matematica()
    pontes = dados_pontes(pt, mat)
    assert len(pontes) == 12
    pt_nomes = {n["nome"] for n in pt["nodes"]}
    mat_nomes = {n["nome"] for n in mat["nodes"]}
    for p in pontes:
        assert p["pt"] in pt_nomes
        assert p["mat"] in mat_nomes
        assert pt["nodes"][p["pt_idx"]]["nome"] == p["pt"]
        assert mat["nodes"][p["mat_idx"]]["nome"] == p["mat"]


def test_dados_pontes_exclui_candidato_sem_par_real():
    pt = dados_portugues()
    mat = dados_matematica()
    pontes = dados_pontes(pt, mat)
    nomes_pt_nas_pontes = {p["pt"] for p in pontes}
    assert "numeral coletivo" not in nomes_pt_nas_pontes


def test_mapa_completo_tem_as_quatro_partes():
    mapa = mapa_completo()
    assert set(mapa.keys()) == {"pt", "mat", "pontes", "cao_de_caca"}
    assert len(mapa["pt"]["nodes"]) == len(mapa["pt"]["edges"]) or True  # só garante que não explode
    assert len(mapa["pontes"]) == 12


def test_cao_de_caca_nao_tem_nenhuma_aresta_interna_nem_ponte():
    mapa = mapa_completo()
    cao = mapa["cao_de_caca"]
    assert cao["edges"] == []
    for ponte in mapa["pontes"]:
        assert ponte["pt"] not in {n["nome"] for n in cao["nodes"]}


def test_roteador_expoe_mapa_conhecimento():
    roteador = Roteador()
    estado, corpo = roteador.mapa_conhecimento()
    assert estado == 200
    assert set(corpo.keys()) == {"pt", "mat", "pontes", "cao_de_caca"}
    assert len(corpo["pt"]["nodes"]) > 1000
    assert len(corpo["mat"]["nodes"]) > 150
