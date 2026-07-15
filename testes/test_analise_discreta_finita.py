import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nucleo.analise_discreta_finita import diferencas, diferenca_ordem, soma_acumulada, media_como_par, converge_por_janela, integral_discreta, monotona_crescente_finita


def test_diferencas_somas():
    assert diferencas([1,3,6,10]) == [2,3,4]
    assert diferenca_ordem([1,4,9,16],2) == [2,2]
    assert soma_acumulada([1,2,3]) == [1,3,6]
    assert media_como_par([2,4,6]) == (12,3)


def test_convergencia_finita():
    assert converge_por_janela([10,8,7,7,7],0,3)
    assert integral_discreta([2,3,4]) == 9
    assert monotona_crescente_finita([1,2,2,5])
