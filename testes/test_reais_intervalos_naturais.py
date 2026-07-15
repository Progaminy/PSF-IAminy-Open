import pytest

from nucleo.reais_intervalos_naturais import AproximacaoReal, IntervaloRacional, RacionalAssinado


def test_racional_assinado_normaliza_e_compara():
    assert RacionalAssinado(-2, 4) == RacionalAssinado(-1, 2)
    assert RacionalAssinado(-1, 2).menor_ou_igual(RacionalAssinado(1, 3))


def test_intervalos_encaixados_criam_certificado_finito():
    aproximacao = AproximacaoReal((
        IntervaloRacional(RacionalAssinado(1), RacionalAssinado(2)),
        IntervaloRacional(RacionalAssinado(7, 5), RacionalAssinado(3, 2)),
        IntervaloRacional(RacionalAssinado(141, 100), RacionalAssinado(142, 100)),
    ))
    certificado = aproximacao.certificado_finito()
    assert certificado["encaixados"] is True
    assert certificado["largura_final"] == RacionalAssinado(1, 100)
    assert "NÃO É COMPLETUDE" in certificado["estado"]


def test_rejeita_intervalo_invertido_ou_nao_encaixado():
    with pytest.raises(ValueError):
        IntervaloRacional(RacionalAssinado(2), RacionalAssinado(1))
    with pytest.raises(ValueError, match="encaixados"):
        AproximacaoReal((
            IntervaloRacional(RacionalAssinado(0), RacionalAssinado(1)),
            IntervaloRacional(RacionalAssinado(2), RacionalAssinado(3)),
        ))


def test_racional_assinado_soma_multiplica_e_reciproco():
    assert RacionalAssinado(1, 2).somar(RacionalAssinado(1, 3)) == RacionalAssinado(5, 6)
    assert RacionalAssinado(2, 3).multiplicar(RacionalAssinado(3, 4)) == RacionalAssinado(1, 2)
    assert RacionalAssinado(-3, 4).reciproco() == RacionalAssinado(-4, 3)
    with pytest.raises(ValueError, match="recíproco"):
        RacionalAssinado(0, 5).reciproco()
