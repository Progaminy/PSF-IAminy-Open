import pytest

from lingua_portuguesa import MotorPortugues
from lingua_portuguesa.investigacao import Investigacao, investigar


@pytest.fixture(scope="module")
def motor():
    return MotorPortugues()


def test_pergunta_e_so_o_nome_do_conceito(motor):
    inv = investigar("morfema", motor)
    assert inv is not None
    assert inv.conceito == "morfema"
    assert inv.o_que_preciso == ("palavra", "lema")
    assert inv.onde_encontrar[-1] == "morfema"
    assert "palavra" in inv.onde_encontrar


def test_pergunta_o_que_e_com_prefixo_natural(motor):
    inv = investigar("o que é morfema?", motor)
    assert inv is not None
    assert inv.conceito == "morfema"
    assert "busca o que o conceito é" in inv.o_que_quer


def test_pergunta_como_funciona_identifica_intencao_mecanismo(motor):
    inv = investigar("como funciona a concordância?", motor)
    assert inv is not None
    assert inv.conceito == "concordância"
    assert inv.o_que_fazer == "motor.definir_conceito_puro(nome) (campo construção)"
    assert "construído por dentro" in inv.o_que_quer
    assert inv.como_funciona == motor.definir_conceito_puro("concordância")


def test_pergunta_de_que_depende_identifica_intencao_requisitos(motor):
    inv = investigar("de que depende o morfema?", motor)
    assert inv is not None
    assert inv.conceito == "morfema"
    assert "precisa para existir" in inv.o_que_quer


def test_pergunta_quem_depende_devolve_dependentes_reais(motor):
    inv = investigar("quem depende de morfema?", motor)
    assert inv is not None
    assert inv.conceito == "morfema"
    assert "radical" in inv.quem_depende_disto
    assert "prefixo" in inv.quem_depende_disto
    assert "sufixo" in inv.quem_depende_disto


def test_pergunta_onde_fica_identifica_intencao_localizacao(motor):
    inv = investigar("onde fica sintaxe?", motor)
    assert inv is not None
    assert inv.conceito == "sintaxe"
    assert "linha canônica" in inv.o_que_quer
    assert inv.onde_encontrar[0] == "diferença"
    assert inv.onde_encontrar[-1] == "sintaxe"


def test_pergunta_desconhecida_devolve_none_honesto(motor):
    assert investigar("isto não é nada conhecido xyz123", motor) is None


def test_conceito_raiz_declara_ausencia_de_dependencias(motor):
    inv = investigar("diferença", motor)
    assert inv is not None
    assert inv.o_que_preciso == ()
    assert "raiz — sem dependências" in inv.como_estruturar
    assert "é raiz" in inv.como_gerar


def test_investigacao_e_dataclass_imutavel(motor):
    inv = investigar("morfema", motor)
    with pytest.raises(AttributeError):
        inv.conceito = "outro"


def test_como_gerar_produz_texto_nao_vazio_com_conceito_e_ligacoes(motor):
    inv = investigar("morfema", motor)
    assert inv.conceito in inv.como_gerar
    assert "Ligado por" in inv.como_gerar
    assert "Depende de" in inv.como_gerar
