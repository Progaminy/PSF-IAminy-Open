import pytest

from matematica import MotorMatematica, ResolucaoMatematica
from validacao_externa import MotorAuxiliarValidacao


def _resolucao_com_precisao(casas_decimais, modo_aproximacao):
    return ResolucaoMatematica(
        problema="1:1",
        estado="RESOLVIDO",
        resultado="1",
        passos=(),
        conhecimento_usado=(),
        casas_decimais=casas_decimais,
        modo_aproximacao=modo_aproximacao,
    )


@pytest.mark.parametrize(
    ("casas_decimais", "modo_aproximacao", "tolerancia_esperada"),
    [
        (3, "arredondar", 0.0005),
        (3, "truncar", 0.001),
        (None, None, 1e-9),
    ],
)
def test_tolerancia_reflete_a_precisao_da_resolucao(
    casas_decimais,
    modo_aproximacao,
    tolerancia_esperada,
):
    resolucao = _resolucao_com_precisao(casas_decimais, modo_aproximacao)

    tolerancia = MotorAuxiliarValidacao._tolerancia_para(resolucao)

    assert tolerancia == tolerancia_esperada


def test_arredondamento_em_tres_casas_nao_e_divergencia():
    expressao = "2:3 com 3 casas arredondado"
    resolucao = MotorMatematica().calcular(expressao)

    validacao = MotorAuxiliarValidacao().validar_matematica(expressao, resolucao)

    assert resolucao.resultado == "0,667"
    assert resolucao.casas_decimais == 3
    assert resolucao.modo_aproximacao == "arredondar"
    assert validacao.aprovado is True
    assert validacao.estado == "APROVADO_POR_COMPARAÇÃO"


def test_precisao_decimal_nao_aprova_erro_relativo_em_numero_grande():
    # O comparador genérico aprovaria 600 contra 1000 porque o erro relativo
    # 0,4 é menor que a tolerância 0,5 de zero casas. Para casas decimais,
    # porém, a margem é absoluta: 400 está muito fora de meia unidade.
    resolucao = ResolucaoMatematica(
        problema="1000",
        estado="RESOLVIDO",
        resultado="600",
        passos=(),
        conhecimento_usado=(),
        casas_decimais=0,
        modo_aproximacao="arredondar",
    )

    validacao = MotorAuxiliarValidacao().validar_matematica("1000", resolucao)

    assert validacao.aprovado is False
    assert validacao.estado == "DIVERGÊNCIA_ENCONTRADA"
