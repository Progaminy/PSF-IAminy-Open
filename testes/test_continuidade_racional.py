from nucleo.continuidade_racional import analisar_continuidade_racional
from nucleo.reais_intervalos_naturais import RacionalAssinado


def _r(n: int) -> RacionalAssinado:
    return RacionalAssinado(n)


def _p(*coeficientes: int) -> tuple[RacionalAssinado, ...]:
    return tuple(_r(c) for c in coeficientes)


def test_descontinuidade_removivel_tem_limite_mas_nao_e_continua():
    # f(x) = (x²-1)/(x-1) em x=1: limite existe (2), mas f(1) não está
    # definida no denominador zero da expressão original.
    analise = analisar_continuidade_racional(_p(1, 0, -1), _p(1, -1), _r(1))
    assert analise.definida_no_ponto is False
    assert analise.valor_no_ponto is None
    assert analise.limite_no_ponto == _r(2)
    assert analise.continua is False


def test_funcao_racional_continua_no_ponto_do_dominio():
    # f(x) = (x+5)/(x-1) em x=3: sem indeterminação, definida e contínua.
    analise = analisar_continuidade_racional(_p(1, 5), _p(1, -1), _r(3))
    assert analise.definida_no_ponto is True
    assert analise.valor_no_ponto == _r(4)
    assert analise.limite_no_ponto == _r(4)
    assert analise.continua is True


def test_divergencia_genuina_nao_definida_nem_continua():
    # f(x) = 1/(x-3) em x=3: nem valor nem limite finito existem.
    analise = analisar_continuidade_racional(_p(1), _p(1, -3), _r(3))
    assert analise.definida_no_ponto is False
    assert analise.valor_no_ponto is None
    assert analise.limite_no_ponto is None
    assert analise.continua is False


def test_outro_exemplo_classico_de_descontinuidade_removivel():
    # f(x) = (x²-4)/(x-2) em x=2: mesmo padrão do primeiro teste.
    analise = analisar_continuidade_racional(_p(1, 0, -4), _p(1, -2), _r(2))
    assert analise.definida_no_ponto is False
    assert analise.limite_no_ponto == _r(4)
    assert analise.continua is False
