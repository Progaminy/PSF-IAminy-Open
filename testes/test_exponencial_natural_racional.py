from nucleo.equivalencia_leis_geradoras import sao_consistentes_ate_epsilon
from nucleo.exponencial_natural_racional import (
    exponencial_natural_racional,
    soma_parcial_exponencial,
)
from nucleo.operacoes_leis_geradoras import lei_geradora_constante, lei_geradora_produto
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _r(n: int, d: int = 1) -> RacionalAssinado:
    return RacionalAssinado(n, d)


def test_soma_parcial_e_exata_e_cresce_para_x_positivo():
    x = _r(1)
    s0 = soma_parcial_exponencial(x, 0)
    s1 = soma_parcial_exponencial(x, 1)
    s2 = soma_parcial_exponencial(x, 2)
    assert s0 == _r(1)
    assert s1 == _r(2)
    assert s2 == _r(5, 2)  # 1 + 1 + 1/2


def test_exponencial_de_zero_e_exatamente_um():
    # Único caso onde a série tem valor fechado trivial: todo termo além
    # de k=0 é zero, então o limite é exato, não só consistente até epsilon.
    limite = exponencial_natural_racional(_r(0))
    um = lei_geradora_constante(_r(1))
    assert sao_consistentes_ate_epsilon(limite, um, _r(1, 1_000_000)) is True


def test_e_vezes_e_menos_um_e_consistente_com_um():
    # eˣ · e⁻ˣ = 1 é identidade pura, verificada com o produto de leis já
    # construído (ETAPA 1062) -- nenhuma referência decimal externa usada.
    e1 = exponencial_natural_racional(_r(1))
    e_menos_1 = exponencial_natural_racional(_r(-1))
    produto = lei_geradora_produto(e1, e_menos_1)
    assert sao_consistentes_ate_epsilon(produto, lei_geradora_constante(_r(1)), _r(1, 100)) is True


def test_e_ao_quadrado_e_consistente_com_e_vezes_e():
    # e¹ · e¹ = e² -- mesma identidade de potência, também sem referência externa.
    e1 = exponencial_natural_racional(_r(1))
    e2 = exponencial_natural_racional(_r(2))
    produto = lei_geradora_produto(e1, e1)
    assert sao_consistentes_ate_epsilon(produto, e2, _r(1, 100)) is True


def test_exponencial_de_negativo_fica_entre_zero_e_um():
    # e⁻¹ ∈ (0, 1): construído aqui só com as próprias somas parciais
    # (série alternada), sem constante externa.
    limite = exponencial_natural_racional(_r(-1))
    n = 12
    intervalo = limite.passo(n)
    zero = lei_geradora_constante(_r(0))
    um = lei_geradora_constante(_r(1))
    assert intervalo.inferior.numerador > 0
    assert sao_consistentes_ate_epsilon(limite, zero, _r(1, 10)) is False
    assert sao_consistentes_ate_epsilon(limite, um, _r(1, 10)) is False


def test_lei_do_limite_produz_prefixo_encaixado():
    limite = exponencial_natural_racional(_r(1))
    aproximacao = limite.prefixo(6)
    certificado = aproximacao.certificado_finito()
    assert certificado["encaixados"] is True
