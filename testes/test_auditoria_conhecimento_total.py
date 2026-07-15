from motor.auditoria_conhecimento_total import auditar_conhecimento_total
from nucleo.calculo_integral_avancado import auditar_pontes_calculo, resposta_calculo_etapa41


def test_todos_os_repositorios_utilizaveis_tem_pontes():
    auditoria = auditar_conhecimento_total()
    assert auditoria["aprovado"] is True
    assert auditoria["isolamentos_utilizaveis"] == ()
    assert auditoria["matematica_documental"]["conceitos"] == 203
    assert auditoria["portugues"]["conceitos"] == 1141


def test_as_59_respostas_de_calculo_chegam_a_conceitos():
    auditoria = auditar_pontes_calculo()
    assert auditoria["respostas"] == 59
    assert auditoria["respostas_sem_ponte"] == ()
    assert auditoria["sem_isolamentos"] is True
    assert resposta_calculo_etapa41("41-II-061") is not None
