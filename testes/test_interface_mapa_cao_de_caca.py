from interface.mapa_cao_de_caca import dados_cao_de_caca
from interface.mapa_conhecimento import mapa_completo


def test_cao_de_caca_carrega_de_verdade_ou_declara_o_motivo():
    dados = dados_cao_de_caca()
    if not dados["disponivel"]:
        assert dados["motivo"]
        assert dados["nodes"] == []
        return
    assert len(dados["nodes"]) > 200
    assert len(dados["temas"]) > 5


def test_cao_de_caca_nunca_tem_aresta_interna():
    # Não é conhecimento PSF com dependências reais entre si -- é um catálogo
    # plano de ferramentas independentes. Nenhuma linha, nunca.
    dados = dados_cao_de_caca()
    assert dados["edges"] == []


def test_cao_de_caca_cada_no_tem_nome_classe_e_tema():
    dados = dados_cao_de_caca()
    for n in dados["nodes"]:
        assert n["nome"]
        assert n["classe"]
        assert n["tema"]


def test_cao_de_caca_nomes_sao_unicos():
    dados = dados_cao_de_caca()
    nomes = [n["nome"] for n in dados["nodes"]]
    assert len(nomes) == len(set(nomes))


def test_mapa_completo_inclui_cao_de_caca_sem_ponte_para_pt_ou_mat():
    # Nomes de atributo do cão de caça podem coincidir por acaso com nomes de
    # conceito PT/MAT (ex.: "porcentagem" existe nos dois catálogos, sem
    # relação alguma) -- o que importa é que a lista de pontes real nunca
    # aponta para dentro do cão de caça, e que ele não carrega arestas.
    mapa = mapa_completo()
    assert "cao_de_caca" in mapa
    cao = mapa["cao_de_caca"]
    assert cao["edges"] == []
    indices_pt_em_pontes = {p["pt_idx"] for p in mapa["pontes"]}
    indices_mat_em_pontes = {p["mat_idx"] for p in mapa["pontes"]}
    assert indices_pt_em_pontes <= set(range(len(mapa["pt"]["nodes"])))
    assert indices_mat_em_pontes <= set(range(len(mapa["mat"]["nodes"])))
