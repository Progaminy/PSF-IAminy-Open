import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nucleo.estatistica_finita_psf import frequencias, media_par, mediana_finita, moda_finita, amplitude_finita, variancia_par, erro_modelo


def test_estatistica_descritiva():
    dados=[1,2,2,5]
    assert frequencias(dados)=={1:1,2:2,5:1}
    assert media_par(dados)==(10,4)
    assert mediana_finita(dados)==(4,2)
    assert moda_finita(dados)==[2]
    assert amplitude_finita(dados)==4
    assert variancia_par([1,2,3])[1]==27


def test_erro_modelo():
    assert erro_modelo([(1,2),(2,4)], lambda x:2*x)==0
