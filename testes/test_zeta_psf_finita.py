import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nucleo.zeta_psf_finita import (
    peso_zeta,
    zeta_finita_por_soma,
    produto_euler_finito_validacao,
    racional_igual,
    primos_ate_por_retirada,
    reconstrucao_zeta_finita,
)


def test_peso_zeta_nasce_de_potencia_repetida():
    assert peso_zeta(3, 2) == (1, 9)
    assert peso_zeta(4, 3) == (1, 64)


def test_zeta_finita_por_soma_sem_divisao():
    # 1 + 1/4 + 1/9 = 49/36
    assert racional_igual(zeta_finita_por_soma(2, 3), (49, 36))


def test_primos_por_retirada_para_validacao_euler():
    assert primos_ate_por_retirada(10) == [2, 3, 5, 7]


def test_produto_euler_finito_e_validacao_nao_fundamento():
    # p=2: 4/3; p=3: 9/8; produto = 36/24 = 3/2
    assert racional_igual(produto_euler_finito_validacao(2, 3), (3, 2))


def test_reconstrucao_declara_bloqueios_para_rh():
    r = reconstrucao_zeta_finita(2, 3, 3)
    assert r["estado"] == "camada finita; não é continuação analítica; não é RH"
    assert r["validacao_euler_finita"]["papel"] == "comparação estrutural posterior, não fundamento"
    assert "números complexos" in r["bloqueios_para_RH"]
