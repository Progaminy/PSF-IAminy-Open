import pytest

from nucleo.funcoes_avancadas import FuncaoLinear, composicao
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _r(n: int, d: int = 1) -> RacionalAssinado:
    return RacionalAssinado(n, d)


def test_imagem_rastreada_e_injetividade():
    # f(x) = 2x - 3, domínio {1,2,3}
    f = FuncaoLinear(_r(2), _r(-3), (_r(1), _r(2), _r(3)))
    assert f.imagem() == (_r(-1), _r(1), _r(3))
    assert f.eh_injetora() is True


def test_funcao_constante_nao_e_injetora():
    f = FuncaoLinear(_r(0), _r(5), (_r(1), _r(2), _r(3)))
    assert f.eh_injetora() is False


def test_inversa_do_exemplo_classico():
    # f(x) = 2x-3 -> f⁻¹(y) = (y+3)/2, ou seja coeficiente 1/2, constante 3/2
    f = FuncaoLinear(_r(2), _r(-3), (_r(1), _r(2), _r(3)))
    inv = f.inversa()
    assert inv.coeficiente == _r(1, 2)
    assert inv.constante == _r(3, 2)
    # desfaz f em cada ponto do domínio original
    for x in f.dominio:
        assert inv.aplicar(f.aplicar(x)) == x


def test_funcao_constante_nao_tem_inversa():
    f = FuncaoLinear(_r(0), _r(5), (_r(1), _r(2)))
    with pytest.raises(ValueError, match="não tem inversa"):
        f.inversa()


def test_aplicar_rejeita_x_fora_do_dominio():
    f = FuncaoLinear(_r(1), _r(0), (_r(1), _r(2)))
    with pytest.raises(ValueError, match="não pertence ao domínio"):
        f.aplicar(_r(99))


def test_composicao_de_duas_funcoes_lineares():
    # f(x)=2x-3 domínio {1,2,3}; g(x)=x+1 domínio {0,1,2} (imagem de g cai em domínio de f)
    f = FuncaoLinear(_r(2), _r(-3), (_r(1), _r(2), _r(3)))
    g = FuncaoLinear(_r(1), _r(1), (_r(0), _r(1), _r(2)))
    fg = composicao(f, g)
    assert fg.coeficiente == _r(2)
    assert fg.constante == _r(-1)
    for x in g.dominio:
        assert fg.aplicar(x) == f.aplicar(g.aplicar(x))


def test_composicao_rejeita_saida_fora_do_dominio_de_f():
    f = FuncaoLinear(_r(2), _r(-3), (_r(1), _r(2)))  # domínio pequeno
    g = FuncaoLinear(_r(1), _r(1), (_r(0), _r(1), _r(2)))  # g(2)=3, fora do domínio de f
    with pytest.raises(ValueError, match="composição indefinida"):
        composicao(f, g)


def test_funcao_linear_rejeita_dominio_vazio():
    with pytest.raises(ValueError, match="domínio não vazio"):
        FuncaoLinear(_r(1), _r(0), ())
