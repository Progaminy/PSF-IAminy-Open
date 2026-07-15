"""Regressão para dois bugs reais de normalização, achados numa auditoria:

1. `normalizar_texto` trocava "x²" por "x2" (perdia o expoente) em vez de
   "x**2" -- quebrava derivada, equação do 2º grau e qualquer motor que lesse
   expoente em notação unicode.
2. Motores que recebem um payload estruturado (dicionário Python, ou várias
   partes separadas por ";") passavam a `entrada` inteira por
   `normalizar_texto` antes de interpretar o payload -- isso baixava chaves
   como "A_ub"/"P"/"Q"/"R" para minúsculas (quebrando o `dict.get` que espera
   maiúscula) e apagava ";" (quebrava o separador de `fluxo maximo`).

Nenhum dos 24 testes existentes (`test_smoke.py`, `test_mapa_conhecimento.py`)
cobria isto -- os dois bugs passaram despercebidos apesar da bateria "verde".
"""
from assistente_psf import (
    MotorDerivadas,
    MotorFluxoRedesPSF,
    MotorMarkovDecisaoPSF,
    MotorOtimizacaoLinearPSF,
    PSFCalculadora,
    normalizar_texto,
)


def test_normalizar_texto_preserva_expoente_ao_quadrado():
    assert normalizar_texto("x² + 3") == "x**2 + 3"


def test_normalizar_texto_preserva_expoente_ao_cubo():
    assert normalizar_texto("x³") == "x**3"


def test_derivada_de_expressao_com_expoente_unicode_nao_e_zero():
    resultado = MotorDerivadas().calcular("derivada x²")
    assert resultado["expressao"] == "x**2"
    assert resultado["derivada"] == "2*x"


def test_otimizacao_linear_reconhece_chave_a_ub_maiuscula():
    comando = "otimizacao linear {'c': [-1, -2], 'A_ub': [[1, 1]], 'b_ub': [4]}"
    resultado = MotorOtimizacaoLinearPSF().calcular(comando)
    assert "erro" not in resultado
    primal = resultado["resultado"]["primal"]
    assert primal["sucesso"] is True
    assert primal["valor_objetivo"] == -8.0


def test_cadeia_markov_reconhece_chave_p_maiuscula():
    comando = "cadeia markov {'P': [[0.5, 0.5], [0.3, 0.7]], 'inicial': [1, 0]}"
    resultado = MotorMarkovDecisaoPSF().calcular(comando)
    assert "erro" not in resultado
    assert resultado["tipo"]


def test_fluxo_maximo_preserva_ponto_e_virgula_como_separador():
    comando = "fluxo maximo [('s','a',3),('a','t',2)] ; 's' ; 't'"
    resultado = MotorFluxoRedesPSF().calcular(comando)
    assert resultado is not None
    assert "erro" not in resultado


def test_branch_and_bound_alcancavel_pelo_terminal():
    despacho = PSFCalculadora().registro_motores.despachar(
        "branch and bound {'c': [-1, -2], 'A_ub': [[1, 1]], 'b_ub': [4]}"
    )
    assert despacho is not None
    nome, resultado, erro = despacho
    assert nome == "otimizacao_inteira"
    assert erro is None


def test_algoritmo_genetico_alcancavel_pelo_terminal():
    despacho = PSFCalculadora().registro_motores.despachar(
        "algoritmo genetico {'variaveis': 2, 'limites': [[-5, 5], [-5, 5]]}"
    )
    assert despacho is not None
    nome, resultado, erro = despacho
    assert nome == "algoritmos_geneticos"
    assert erro is None


def test_teoria_das_filas_alcancavel_pelo_terminal():
    despacho = PSFCalculadora().registro_motores.despachar("fila m m 1 2 3")
    assert despacho is not None
    nome, resultado, erro = despacho
    assert nome == "teoria_filas"
    assert erro is None
