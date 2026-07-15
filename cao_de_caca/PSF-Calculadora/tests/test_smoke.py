from contextlib import redirect_stdout
from io import StringIO

import assistente_psf
from assistente_psf import PSFCalculadora
from psf_calculadora.dependencias import DependenciaAusenteError
from psf_calculadora.dominios.aritmetica import (
    MotorAdicaoSubtracao,
    MotorDivisao,
    MotorMultiplos,
)
from psf_calculadora.registro import RegistroMotores


def test_adicao_modular():
    resultado = MotorAdicaoSubtracao().calcular("calcule 2 + 3")
    assert resultado["resultado"] == "5"


def test_divisao_em_linguagem_natural():
    resultado = MotorDivisao().calcular("10 dividido por 2")
    assert resultado["quociente"] == "5"
    assert resultado["exata"] is True


def test_divisao_com_simbolo_unicode():
    resultado = MotorDivisao().calcular("10 ÷ 2")
    assert resultado["quociente"] == "5"


def test_multiplos_modular():
    resultado = MotorMultiplos().calcular("múltiplos de 3")
    assert resultado["valores"][:3] == [3, 6, 9]


def test_nomes_legados_apontam_para_classes_migradas():
    assert assistente_psf.MotorAdicaoSubtracao is MotorAdicaoSubtracao
    assert assistente_psf.MotorDivisao is MotorDivisao
    assert MotorAdicaoSubtracao.__module__.endswith("dominios.aritmetica")


def test_indice_executa_apenas_motor_candidato():
    chamadas = []

    class Motor:
        def __init__(self, nome):
            self.nome = nome

        def calcular(self, entrada):
            chamadas.append(self.nome)
            return {"resultado": self.nome}

    registro = RegistroMotores()
    registro.registrar("media", Motor("media"), intencoes=("media",))
    registro.registrar("fourier", Motor("fourier"), intencoes=("fourier",))
    nome, resultado, erro = registro.despachar("calcular media")
    assert (nome, resultado, erro) == ("media", {"resultado": "media"}, None)
    assert chamadas == ["media"]


def test_indice_remove_pontuacao_da_intencao():
    calculadora = PSFCalculadora()
    nomes = [
        item.nome
        for item in calculadora.registro_motores.candidatos("media? 1 2 3")
    ]
    assert nomes[0] == "media"


def test_intencao_explicita_vence_colisao_generica():
    calculadora = PSFCalculadora()
    nomes = [
        item.nome
        for item in calculadora.registro_motores.candidatos("derivada de x^2")
    ]
    assert nomes[0] == "derivadas"


def test_fallback_e_limitado_a_motores_declarados():
    class Nulo:
        def calcular(self, entrada):
            return None

    registro = RegistroMotores()
    registro.registrar("comum", Nulo(), intencoes=("comum",))
    registro.registrar("fallback", Nulo(), intencoes=("especial",), fallback=True)
    assert [item.nome for item in registro.candidatos("sem intencao")] == ["fallback"]


def test_dependencia_ausente_impede_execucao():
    chamadas = []

    class Cientifico:
        def calcular(self, entrada):
            chamadas.append(entrada)
            return {"resultado": 1}

    registro = RegistroMotores(verificar_dependencias=lambda deps: deps)
    registro.registrar(
        "cientifico", Cientifico(), intencoes=("cientifico",),
        dependencias=("sympy",),
    )
    nome, resultado, erro = registro.despachar("calculo cientifico")
    assert nome == "cientifico" and resultado is None
    assert isinstance(erro, DependenciaAusenteError)
    assert "pip install" in str(erro)
    assert chamadas == []


def test_fourier_tem_motores_distintos_e_requisitos():
    calculadora = PSFCalculadora()
    assert type(calculadora.series_fourier).__name__ == "MotorSeriesFourier"
    assert type(calculadora.series_fourier_psf).__name__ == "MotorSeriesFourierPSF"
    itens = calculadora.registro_motores._por_nome
    assert "sympy" in itens["series_fourier"].dependencias
    assert "numpy" in itens["series_fourier_psf"].dependencias


def test_parser_geral_esta_integrado_ao_registro():
    calculadora = PSFCalculadora()
    item = calculadora.registro_motores._por_nome["problema_psf"]
    assert item.motor is calculadora.motor_problema_psf
    assert item.dependencias == ("sympy",)


def test_candidato_especifico_executa_antes_do_parser_geral():
    calculadora = PSFCalculadora()
    calculadora.registro_motores._verificar_dependencias = lambda deps: ()
    chamadas = []
    calculadora.motor_problema_psf.calcular = lambda entrada: chamadas.append(entrada)
    despacho = calculadora.registro_motores.despachar("calcule 2 + 3")
    assert despacho[0] == "adicao_subtracao"
    assert chamadas == []


def test_parser_geral_pode_executar_com_dependencias_disponiveis():
    calculadora = PSFCalculadora()
    calculadora.registro_motores._verificar_dependencias = lambda deps: ()
    calculadora.motor_problema_psf.calcular = lambda entrada: {
        "resultado": "parser geral"
    }
    despacho = calculadora.registro_motores.despachar(
        "calcule um problema sofisticado"
    )
    assert despacho[:2] == ("problema_psf", {"resultado": "parser geral"})


def test_todos_motores_declaram_intencoes_e_dependencias():
    registro = PSFCalculadora().registro_motores
    assert all(item.intencoes for item in registro._motores)
    assert all(isinstance(item.dependencias, tuple) for item in registro._motores)


def test_integracao_terminal_basico():
    calculadora = PSFCalculadora()
    saida = StringIO()
    with redirect_stdout(saida):
        calculadora.processar_comando("10 dividido por 2")
    texto = saida.getvalue()
    assert "quociente" in texto
    assert "5" in texto


def test_integracao_terminal_com_pontuacao():
    calculadora = PSFCalculadora()
    saida = StringIO()
    with redirect_stdout(saida):
        calculadora.processar_comando("media? 1 2 3")
    assert "'media': '2'" in saida.getvalue()


def test_integracao_erro_explicito_sem_sympy():
    calculadora = PSFCalculadora()
    calculadora.motor_problema_psf.calcular = lambda entrada: None
    calculadora.registro_motores._verificar_dependencias = lambda deps: (
        tuple(d for d in deps if d == "sympy")
    )
    saida = StringIO()
    with redirect_stdout(saida):
        calculadora.processar_comando("derivada de x^2")
    texto = saida.getvalue()
    assert "requer SymPy" in texto
    assert "psf-calculadora[completo]" in texto
