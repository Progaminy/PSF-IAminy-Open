import pytest

from nucleo.funcao_por_ramos import FuncaoPorRamos, Ramo
from nucleo.reais_intervalos_naturais import RacionalAssinado

_ZERO = RacionalAssinado(0)


def _negativo(x: RacionalAssinado) -> bool:
    return x.numerador < 0


def _nao_negativo(x: RacionalAssinado) -> bool:
    return x.numerador >= 0


def _quadrado(x: RacionalAssinado) -> RacionalAssinado:
    return x.multiplicar(x)


def _mais_um(x: RacionalAssinado) -> RacionalAssinado:
    return x.somar(RacionalAssinado(1))


def _funcao_classica() -> FuncaoPorRamos:
    # f(x) = x² se x < 0; x+1 se x >= 0
    return FuncaoPorRamos((
        Ramo("negativo", _negativo, _quadrado),
        Ramo("nao_negativo", _nao_negativo, _mais_um),
    ))


def test_avalia_ramo_negativo():
    f = _funcao_classica()
    assert f.avaliar(RacionalAssinado(-2)) == RacionalAssinado(4)


def test_avalia_ramo_nao_negativo_no_ponto_de_transicao():
    f = _funcao_classica()
    assert f.avaliar(_ZERO) == RacionalAssinado(1)
    assert f.avaliar(RacionalAssinado(3)) == RacionalAssinado(4)


def test_rejeita_x_sem_ramo():
    # ramos cobrem só x<0 e x>0: x=0 fica sem ramo (lacuna proposital)
    f = FuncaoPorRamos((
        Ramo("negativo", lambda x: x.numerador < 0, _quadrado),
        Ramo("positivo", lambda x: x.numerador > 0, _mais_um),
    ))
    with pytest.raises(ValueError, match="não pertence a nenhum ramo"):
        f.avaliar(_ZERO)


def test_rejeita_x_em_dois_ramos():
    # ramos se sobrepõem em x=0 (ambos incluem x>=0 e x<=0)
    f = FuncaoPorRamos((
        Ramo("ate_zero", lambda x: x.numerador <= 0, _quadrado),
        Ramo("desde_zero", lambda x: x.numerador >= 0, _mais_um),
    ))
    with pytest.raises(ValueError, match="pertence a mais de um ramo"):
        f.avaliar(_ZERO)


def test_funcao_por_ramos_exige_ao_menos_um_ramo():
    with pytest.raises(ValueError, match="ao menos um ramo"):
        FuncaoPorRamos(())
