"""Regressão linear e coeficiente de determinação — mínimos quadrados exato.

"Correlação/regressão" existia neste projeto só como resposta legada
(`nucleo/conceitos_avancados_puros.py`), sem prova, código ou teste. Este
ramo liga a `estatística finita` (ETAPA 961-990) — reaproveita a mesma
ideia de erro quadrático de `erro_modelo`, agora para achar a reta que o
minimiza, não só medi-lo.

A reta de mínimos quadrados (inclinação e intercepto) fica exata, em
racionais — nenhuma raiz quadrada é necessária. O coeficiente de
correlação `r` clássico normaliza por um desvio-padrão (raiz quadrada,
geralmente irracional); esta etapa usa o coeficiente de determinação
`r²`, que mede a mesma ideia (quanto da variação de y a reta explica) e
fica exato.
"""
from __future__ import annotations

from dataclasses import dataclass

from .reais_intervalos_naturais import RacionalAssinado

_UM = RacionalAssinado(1)
_PASSO_TESTE = RacionalAssinado(1, 100)


@dataclass(frozen=True, slots=True)
class RetaRegressao:
    inclinacao: RacionalAssinado
    intercepto: RacionalAssinado

    def prever(self, x: RacionalAssinado) -> RacionalAssinado:
        return self.inclinacao.multiplicar(x).somar(self.intercepto)


def _erro_total(reta: RetaRegressao, dados: list[tuple[int, int]]) -> RacionalAssinado:
    total = RacionalAssinado(0)
    for x, y in dados:
        diferenca = reta.prever(RacionalAssinado(x)).subtrair(RacionalAssinado(y))
        total = total.somar(diferenca.multiplicar(diferenca))
    return total


def regressao_linear(dados: list[tuple[int, int]]) -> RetaRegressao:
    """Inclinação e intercepto por mínimos quadrados, conferidos contra vizinhos.

    inclinação = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)², intercepto = ȳ − inclinação·x̄,
    em racionais exatos. Depois de calculada, confere que nenhuma
    inclinação vizinha (levemente maior ou menor) produz erro total
    menor, reaproveitando o mesmo erro quadrático de `erro_modelo`
    (ETAPA 961-990) — a mesma prova por comparação com vizinhos já usada
    em otimização finita, não a suposição de que o cálculo é ótimo.
    """
    n = len(dados)
    if n < 2:
        raise ValueError("regressão linear exige pelo menos dois pontos")
    media_x = RacionalAssinado(sum(x for x, _ in dados), n)
    media_y = RacionalAssinado(sum(y for _, y in dados), n)

    s_xy = RacionalAssinado(0)
    s_xx = RacionalAssinado(0)
    for x, y in dados:
        dx = RacionalAssinado(x).subtrair(media_x)
        dy = RacionalAssinado(y).subtrair(media_y)
        s_xy = s_xy.somar(dx.multiplicar(dy))
        s_xx = s_xx.somar(dx.multiplicar(dx))
    if s_xx.numerador == 0:
        raise ValueError("todos os x são iguais; inclinação indefinida")

    inclinacao = s_xy.multiplicar(s_xx.reciproco())
    intercepto = media_y.subtrair(inclinacao.multiplicar(media_x))
    reta = RetaRegressao(inclinacao, intercepto)

    erro_atual = _erro_total(reta, dados)
    zero = RacionalAssinado(0)
    for delta in (_PASSO_TESTE, zero.subtrair(_PASSO_TESTE)):
        vizinha = RetaRegressao(inclinacao.somar(delta), intercepto)
        erro_vizinho = _erro_total(vizinha, dados)
        if erro_vizinho.menor_ou_igual(erro_atual) and erro_vizinho != erro_atual:
            raise ValueError("inclinação vizinha reduz o erro; mínimos quadrados não foi mínimo")
    return reta


def coeficiente_determinacao(reta: RetaRegressao, dados: list[tuple[int, int]]) -> RacionalAssinado:
    """r² = 1 − (erro residual) / (variação total de y em torno da média), exato.

    Mede quanto da variação de y a reta explica, sem raiz quadrada — ao
    contrário do coeficiente de correlação r clássico.
    """
    n = len(dados)
    media_y = RacionalAssinado(sum(y for _, y in dados), n)
    variacao_total = RacionalAssinado(0)
    for _, y in dados:
        dy = RacionalAssinado(y).subtrair(media_y)
        variacao_total = variacao_total.somar(dy.multiplicar(dy))
    if variacao_total.numerador == 0:
        raise ValueError("todos os y são iguais; coeficiente de determinação indefinido")
    erro_residual = _erro_total(reta, dados)
    return _UM.subtrair(erro_residual.multiplicar(variacao_total.reciproco()))
