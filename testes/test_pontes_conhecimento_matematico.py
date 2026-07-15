from matematica import MotorMatematica
from matematica.pontes import auditar_pontes


def test_todo_conceito_matematico_inventariado_tem_ponte():
    motor = MotorMatematica()
    auditoria = motor.auditar_pontes()
    assert auditoria["conceitos"] == 203
    assert auditoria["isolados"] == ()
    assert auditoria["todos_tem_ponte"] is True


def test_auditoria_rejeita_conhecimento_isolado():
    class Isolado:
        nome = "fórmula caída do céu"
        dependencias_declaradas = ()
        construcao = "resultado pronto"
        implementacoes = ("x.py",)
        testes = ("test_x.py",)

    auditoria = auditar_pontes((Isolado(),))
    assert auditoria["todos_tem_ponte"] is False
    assert auditoria["isolados"] == ("fórmula caída do céu",)
