import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nucleo.medida_probabilidade_finita import medida, aditividade_disjunta, probabilidade_como_par, condicional_como_par, independentes_por_produto_cruzado, distribuicao_variavel


def test_medida_probabilidade():
    U={1,2,3,4}
    pesos={x:1 for x in U}
    assert medida({1,2},pesos)==2
    assert aditividade_disjunta({1},{2,3},pesos)
    assert probabilidade_como_par({1,2},U,pesos)==(2,4)
    assert condicional_como_par({1,2},{2,3},U,pesos)==(1,2)


def test_independencia_e_distribuicao():
    U={(0,0),(0,1),(1,0),(1,1)}
    A={x for x in U if x[0]==1}
    B={x for x in U if x[1]==1}
    assert independentes_por_produto_cruzado(A,B,U)
    assert distribuicao_variavel(U, lambda x:x[0]) == {0:2,1:2}
