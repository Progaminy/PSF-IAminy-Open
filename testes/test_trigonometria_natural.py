import pytest

from nucleo.trigonometria_natural import (
    FLUXO_TRIGONOMETRICO_NATURAL,
    TrianguloRetangulo,
    auditar_fluxo_trigonometrico,
    cossecante,
    cosseno,
    cotangente,
    identidade_fundamental_confere,
    identidades_de_quociente_conferem,
    identidades_reciprocas_conferem,
    secante,
    seno,
    tangente,
)


def test_fluxo_natural_chega_as_seis_razoes_sem_lacunas():
    auditoria = auditar_fluxo_trigonometrico()
    assert auditoria["sem_lacunas_internas"] is True
    assert auditoria["dependencias_ausentes_ou_futuras"] == ()
    nomes = tuple(p.nome for p in FLUXO_TRIGONOMETRICO_NATURAL)
    for nome in ("seno", "cosseno", "tangente", "cotangente", "secante", "cossecante"):
        assert nome in nomes


def test_triangulo_3_4_5_constroi_razoes_exatas():
    t = TrianguloRetangulo(cateto_adjacente=4, cateto_oposto=3, hipotenusa=5)
    assert seno(t).texto() == "3/5"
    assert cosseno(t).texto() == "4/5"
    assert tangente(t).texto() == "3/4"
    assert cotangente(t).texto() == "4/3"
    assert secante(t).texto() == "5/4"
    assert cossecante(t).texto() == "5/3"


def test_semelhanca_conserva_todas_as_razoes():
    pequeno = TrianguloRetangulo(4, 3, 5)
    grande = pequeno.ampliar(7)
    funcoes = (seno, cosseno, tangente, cotangente, secante, cossecante)
    assert all(funcao(pequeno).igual(funcao(grande)) for funcao in funcoes)


def test_identidades_nascem_das_razoes_e_de_pitagoras():
    t = TrianguloRetangulo(12, 5, 13)
    assert identidade_fundamental_confere(t)
    assert identidades_de_quociente_conferem(t)
    assert identidades_reciprocas_conferem(t)


def test_nao_aceita_lados_que_fingem_triangulo_retangulo():
    with pytest.raises(ValueError, match="não formam"):
        TrianguloRetangulo(2, 3, 4)
