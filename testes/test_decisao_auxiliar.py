import pytest

from motor.decisao_auxiliar import decidir


def test_pergunta_sem_gatilho_e_sem_assunto_nao_usa_cao_de_caca():
    decisao = decidir("quanto é 2 + 3")
    assert decisao.usar_cao_de_caca is False
    assert decisao.precisa_comparar is False
    assert decisao.precisa_valor_exato is False
    assert decisao.precisa_dependencia_externa is False


def test_pedido_de_comparacao_com_assunto_real_usa_cao_de_caca():
    decisao = decidir("quero comparar meu resultado de derivadas com outro motor")
    assert decisao.precisa_comparar is True
    assert "derivadas" in decisao.motores_candidatos
    assert decisao.usar_cao_de_caca is True


def test_pedido_de_otimizacao_reconhece_acento_diferente_do_atributo():
    # atributo real é "otimizacao_linear" (sem acento); pergunta usa "otimização".
    decisao = decidir("preciso otimizar um problema de otimização linear")
    assert decisao.precisa_valor_exato is True
    assert "otimizacao_linear" in decisao.motores_candidatos
    assert decisao.usar_cao_de_caca is True


def test_dependencia_externa_reconhece_tema_grafos():
    decisao = decidir("preciso de dependência externa para grafos grandes")
    assert decisao.precisa_dependencia_externa is True
    assert decisao.assunto == "grafos"
    assert decisao.usar_cao_de_caca is True


def test_nome_de_motor_curto_nao_casa_dentro_de_outra_palavra():
    # "pa" (Progressão Aritmética) não pode "casar" dentro de "comparar".
    decisao = decidir("quero comparar dois números quaisquer")
    assert "pa" not in decisao.motores_candidatos


def test_gatilho_sem_assunto_reconhecido_nao_usa_cao_de_caca():
    # "comparar" está presente, mas nenhum tema/motor real é citado --
    # PSF não deve fingir que sabe pra onde ir.
    decisao = decidir("quero comparar duas coisas quaisquer")
    assert decisao.precisa_comparar is True
    assert decisao.usar_cao_de_caca is False


def test_decisao_nunca_executa_o_cao_de_caca_sozinha():
    decisao = decidir("quero comparar derivadas")
    # é uma decisão, não uma execução -- não deve existir campo de resultado.
    assert not hasattr(decisao, "resultado")


@pytest.mark.parametrize("pergunta", ["", "   "])
def test_pergunta_vazia_nao_usa_cao_de_caca(pergunta):
    decisao = decidir(pergunta)
    assert decisao.usar_cao_de_caca is False
