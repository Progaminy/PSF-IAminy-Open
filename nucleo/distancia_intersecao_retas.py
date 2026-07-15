"""Distância de ponto a reta e interseção de retas — próximo alvo já
documentado por ETAPA 1039 (`geometria_analitica.py`), não um recomeço.

Os dois produtos vetoriais/escalares que já provam paralelismo e
perpendicularidade em ETAPA 1039 bastam de novo aqui: a distância de um
ponto a uma reta nasce do mesmo produto vetorial que mede área (ETAPA
1038, lei dos senos); a interseção de duas retas nasce da mesma equação
geral `a·x + b·y = c` cujo determinante já decide paralelismo
(`retas_paralelas`). Nenhuma peça nova de álgebra linear é inventada: o
sistema de duas equações é resolvido por Cramer com a aritmética exata
já provada de `RacionalAssinado`, e o resultado é sempre conferido contra
a própria definição de pertencimento (`pertence_a_reta`), nunca aceito só
por sair da fórmula.
"""
from __future__ import annotations

from .equacao_quadratica_exata import raiz_quadrada_exata_ou_none
from .geometria_analitica import Reta, pertence_a_reta, retas_paralelas
from .reais_intervalos_naturais import RacionalAssinado
from .trigonometria_plana import Ponto, Vetor

_ZERO = RacionalAssinado(0)


def distancia_ao_quadrado_ponto_reta(ponto: Ponto, reta: Reta) -> RacionalAssinado:
    """Quadrado da distância de um ponto a uma reta, exato, sem raiz quadrada.

    O produto vetorial entre (ponto − p1) e a direção da reta carrega
    "comprimento da direção × distância" (o dobro da área do triângulo
    formado pelos dois pontos da reta e o ponto — mesma leitura usada em
    ETAPA 1038 para a lei dos senos); dividir o quadrado disso pelo
    quadrado do comprimento da direção isola o quadrado da distância.
    """
    v = Vetor.entre(reta.p1, ponto)
    cruzado = v.produto_vetorial(reta.direcao())
    return cruzado.multiplicar(cruzado).multiplicar(reta.direcao().norma_ao_quadrado().reciproco())


def distancia_ponto_reta_exata_ou_none(ponto: Ponto, reta: Reta) -> RacionalAssinado | None:
    """Distância de ponto a reta, exata, só quando o quadrado é quadrado perfeito.

    Mesmo padrão de `distancia_exata_ou_none` (ETAPA 1039): liga
    `distancia_ao_quadrado_ponto_reta` a `raiz_quadrada_exata_ou_none`
    (ETAPA 1048); quando não é quadrado perfeito racional, devolve `None`
    em vez de aproximar.
    """
    return raiz_quadrada_exata_ou_none(distancia_ao_quadrado_ponto_reta(ponto, reta))


def _equacao_geral(reta: Reta) -> tuple[RacionalAssinado, RacionalAssinado, RacionalAssinado]:
    """(a, b, c) de `a·x + b·y = c`, a partir de um ponto e da direção da reta."""
    direcao = reta.direcao()
    a, b = direcao.dy, _ZERO.subtrair(direcao.dx)
    c = a.multiplicar(reta.p1.x).somar(b.multiplicar(reta.p1.y))
    return a, b, c


def intersecao_de_retas(r1: Reta, r2: Reta) -> Ponto | None:
    """Ponto de interseção de duas retas, ou `None` quando são paralelas.

    Monta a equação geral de cada reta e resolve o sistema 2x2 pela regra
    de Cramer: o determinante `a1·b2 − a2·b1` é a mesma expressão que
    `retas_paralelas` já usa (produto vetorial das direções) — paralelas
    dá determinante zero e por isso `None`, honesto, nunca uma divisão
    por zero disfarçada. O ponto resultante é conferido pertencendo às
    duas retas de verdade (`pertence_a_reta`), não só aceito por sair da
    fórmula.
    """
    if retas_paralelas(r1, r2):
        return None
    a1, b1, c1 = _equacao_geral(r1)
    a2, b2, c2 = _equacao_geral(r2)
    det = a1.multiplicar(b2).subtrair(a2.multiplicar(b1))
    inverso_det = det.reciproco()
    x = c1.multiplicar(b2).subtrair(c2.multiplicar(b1)).multiplicar(inverso_det)
    y = a1.multiplicar(c2).subtrair(a2.multiplicar(c1)).multiplicar(inverso_det)
    ponto = Ponto(x, y)
    if not (pertence_a_reta(ponto, r1) and pertence_a_reta(ponto, r2)):
        raise ValueError("interseção calculada não pertence às duas retas de origem")
    return ponto
