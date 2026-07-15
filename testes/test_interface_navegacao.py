from interface.roteador import Roteador


def test_onde_estou_via_roteador():
    estado, corpo = Roteador().onde_estou("portugues", "diferença")
    assert estado == 200
    assert corpo["e_raiz"] is True
    assert len(corpo["alcancaveis"]) == 1140


def test_onde_estou_conceito_inexistente_via_roteador():
    estado, corpo = Roteador().onde_estou("portugues", "isto não existe")
    assert estado == 404


def test_navegar_caminho_curto_via_roteador():
    estado, corpo = Roteador().navegar("portugues", "diferença", "fonema", "curto")
    assert estado == 200
    assert corpo["existe"] is True
    assert corpo["conceitos"][0] == "diferença"


def test_navegar_area_desconhecida():
    estado, corpo = Roteador().navegar("alemao", "a", "b", "curto")
    assert estado == 404


def test_componentes_via_roteador():
    estado, corpo = Roteador().componentes("matematica")
    assert estado == 200
    assert corpo["total_componentes"] > 1


def test_problemas_abertos_via_roteador():
    estado, corpo = Roteador().problemas_abertos()
    assert estado == 200
    assert corpo["total"] == 60
    for p in corpo["problemas"]:
        assert p["estado"]
        assert p["titulo"]
