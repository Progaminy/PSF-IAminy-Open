from interface.roteador import Roteador


def test_listar_aulas_area_desconhecida():
    estado, corpo = Roteador().listar_aulas("alemao")
    assert estado == 404
    assert "erro" in corpo


def test_listar_aulas_portugues_cobre_todos_os_pacotes():
    estado, corpo = Roteador().listar_aulas("portugues")
    assert estado == 200
    assert len(corpo["pacotes"]) > 1000


def test_obter_pacote_inexistente():
    estado, corpo = Roteador().obter_pacote("portugues", "PT-9999")
    assert estado == 404


def test_obter_pacote_real_tem_aula_completa_com_exercicios_e_corrigidos():
    roteador = Roteador()
    codigo = roteador.listar_aulas("portugues")[1]["pacotes"][0]["codigo"]
    estado, corpo = roteador.obter_pacote("portugues", codigo)
    assert estado == 200
    aula = corpo["aulas"][0]
    assert aula["texto"]
    assert len(aula["exercicios"]) == len(aula["corrigidos"])
    for corrigido in aula["corrigidos"]:
        assert corrigido["pergunta"]
        assert corrigido["resposta"]


def test_verificar_exercicio_estruturado_correto_e_incorreto():
    roteador = Roteador()
    estado, ok = roteador.verificar_exercicio("portugues", "diferença", "raiz", "sim")
    assert estado == 200
    assert ok["correto"] is True
    estado, errado = roteador.verificar_exercicio("portugues", "diferença", "raiz", "não")
    assert errado["correto"] is False


def test_verificar_exercicio_conceito_inexistente():
    estado, corpo = Roteador().verificar_exercicio("portugues", "isto não existe", "raiz", "sim")
    assert estado == 404
