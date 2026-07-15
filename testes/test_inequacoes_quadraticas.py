import pytest

from nucleo.inequacoes import Comparador
from nucleo.inequacoes_quadraticas import resolver_inequacao_quadratica
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _r(n: int, d: int = 1) -> RacionalAssinado:
    return RacionalAssinado(n, d)


def test_fora_das_raizes_parabola_para_cima():
    # x² - 5x + 6 > 0 (raízes 2 e 3, a>0): fora das raízes
    solucao = resolver_inequacao_quadratica(_r(1), _r(-5), _r(6), Comparador.MAIOR)
    assert solucao.raizes == (_r(2), _r(3))
    assert solucao.classificacao == "fora_das_raizes"
    assert solucao.satisfaz(_r(1)) is True
    assert solucao.satisfaz(_r(5)) is True
    assert solucao.satisfaz(_r(5, 2)) is False  # 2,5 está entre as raízes


def test_entre_raizes_parabola_para_baixo():
    # -x² + 5x - 6 > 0 (mesmas raízes 2 e 3, a<0): entre as raízes
    solucao = resolver_inequacao_quadratica(_r(-1), _r(5), _r(-6), Comparador.MAIOR)
    assert solucao.raizes == (_r(2), _r(3))
    assert solucao.classificacao == "entre_raizes"
    assert solucao.satisfaz(_r(5, 2)) is True
    assert solucao.satisfaz(_r(1)) is False
    assert solucao.satisfaz(_r(4)) is False


def test_sem_raizes_reais_sinal_constante_positivo():
    # x² + x + 1 > 0: discriminante negativo, sempre positivo
    solucao = resolver_inequacao_quadratica(_r(1), _r(1), _r(1), Comparador.MAIOR)
    assert solucao.raizes == ()
    assert solucao.classificacao == "todos_os_reais"
    assert solucao.satisfaz(_r(-100)) is True
    assert solucao.satisfaz(_r(100)) is True


def test_raiz_dupla_todos_exceto_um_ponto():
    # (x-2)² > 0: positivo em todo lugar, exceto exatamente em x=2
    solucao = resolver_inequacao_quadratica(_r(1), _r(-4), _r(4), Comparador.MAIOR)
    assert solucao.raizes == (_r(2),)
    assert solucao.classificacao == "todos_exceto_um_ponto"
    assert solucao.satisfaz(_r(2)) is False
    assert solucao.satisfaz(_r(3)) is True


def test_raiz_dupla_maior_ou_igual_e_todos_os_reais():
    # (x-2)² >= 0: verdadeiro para todo x, inclusive x=2
    solucao = resolver_inequacao_quadratica(_r(1), _r(-4), _r(4), Comparador.MAIOR_OU_IGUAL)
    assert solucao.classificacao == "todos_os_reais"
    assert solucao.satisfaz(_r(2)) is True


def test_rejeita_a_igual_a_zero():
    with pytest.raises(ValueError, match="não é uma inequação do 2º grau"):
        resolver_inequacao_quadratica(_r(0), _r(1), _r(1), Comparador.MAIOR)


def test_rejeita_discriminante_nao_quadrado_perfeito():
    with pytest.raises(ValueError, match="não é quadrado perfeito"):
        resolver_inequacao_quadratica(_r(1), _r(0), _r(-2), Comparador.MAIOR)
