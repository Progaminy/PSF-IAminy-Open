import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nucleo.sequencias_calculo_psf import (
    adicionar, multiplicar, potencia, operacao_nivel,
    sequencia_diagonal, indice_propulsional,
)


def test_operacoes_nascem_por_repeticao():
    assert adicionar(2, 3) == 5
    assert multiplicar(4, 3) == 12
    assert potencia(3, 3) == 27


def test_sequencias_diagonais_basicas():
    nivel1 = sequencia_diagonal(1, quantidade=4)
    assert [t["expressao"] for t in nivel1] == ["1 + 1", "2 + 2", "3 + 3", "4 + 4"]
    assert [t["valor"] for t in nivel1] == [2, 4, 6, 8]

    nivel2 = sequencia_diagonal(2, quantidade=4)
    assert [t["expressao"] for t in nivel2] == ["1 × 1", "2 × 2", "3 × 3", "4 × 4"]
    assert [t["valor"] for t in nivel2] == [1, 4, 9, 16]

    nivel3 = sequencia_diagonal(3, quantidade=3)
    assert [t["expressao"] for t in nivel3] == ["1 ^ 1", "2 ^ 2", "3 ^ 3"]
    assert [t["valor"] for t in nivel3] == [1, 4, 27]


def test_superpotencia_finita_com_limite():
    assert operacao_nivel(4, 2, 2, limite_valor=1000) == 4
    assert operacao_nivel(4, 3, 2, limite_valor=1000) == 27
    bloqueado = sequencia_diagonal(4, quantidade=4, limite_valor=1000)[3]
    assert bloqueado["valor"] is None
    assert bloqueado["bloqueado"] == "limite_valor ultrapassado"


def test_indice_propulsional_tem_niveis():
    indice = indice_propulsional(max_nivel=3, max_n=3, limite_valor=10000)
    assert [linha["nivel"] for linha in indice] == [1, 2, 3]
    assert indice[0]["termos"][1]["valor"] == 4
    assert indice[1]["termos"][2]["valor"] == 9
    assert indice[2]["termos"][2]["valor"] == 27
