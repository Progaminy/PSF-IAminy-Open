from ensino.navegacao_pacotes import (
    alcancaveis_de,
    caminho_mais_curto,
    caminho_mais_longo,
    componentes_conectados,
    onde_estou,
)


def test_onde_estou_da_raiz_portugues():
    loc = onde_estou("diferença")
    assert loc is not None
    assert loc.e_raiz is True
    assert loc.e_folha is False
    assert len(loc.dependentes) > 5


def test_onde_estou_conceito_inexistente():
    assert onde_estou("isto não existe no grafo") is None


def test_diferenca_alcanca_quase_todo_o_grafo_portugues():
    # "diferença" é a única raiz do Português -- alcança todo o resto.
    alcancaveis = alcancaveis_de("diferença")
    assert len(alcancaveis) == 1140  # 1141 conceitos menos ela própria


def test_caminho_mais_curto_e_real_e_comeca_na_origem_termina_no_destino():
    c = caminho_mais_curto("diferença", "artigo definido")
    assert c.existe is True
    assert c.conceitos[0] == "diferença"
    assert c.conceitos[-1] == "artigo definido"
    assert c.comprimento == len(c.conceitos) - 1


def test_caminho_mais_longo_nunca_e_mais_curto_que_o_caminho_mais_curto():
    curto = caminho_mais_curto("diferença", "artigo definido")
    longo = caminho_mais_longo("diferença", "artigo definido")
    assert longo.comprimento >= curto.comprimento


def test_caminho_inexistente_e_honesto_nunca_aproximado():
    # sentido contrário -- não existe caminho de um conceito quase-folha até a raiz.
    c = caminho_mais_curto("artigo definido", "diferença")
    assert c.existe is False
    assert c.conceitos == ()


def test_portugues_e_um_unico_componente_conectado():
    # achado real: o grafo (não dirigido) de Português já é uma só ilha.
    componentes = componentes_conectados("portugues")
    assert len(componentes) == 1
    assert len(componentes[0]) == 1141


def test_matematica_tem_ilhas_reais_entre_conceitos_documentados():
    # sem os nós de raiz sintéticos (primitivas), alguns conceitos só se
    # ligam a uma primitiva, nunca a outro conceito documentado -- ilha
    # real dentro deste grafo, mesmo que a ETAPA 313 já tenha mostrado que
    # a versão COM primitivas tem 0 isolados.
    componentes = componentes_conectados("matematica")
    assert len(componentes) > 1
    maior = max(componentes, key=len)
    assert len(maior) > 100
