import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nucleo.otimizacao_modelos_finitos import minimo_global, maximo_global, minimo_local, busca_gulosa, perda_quadratica_catalogo, treinar_por_busca, comparar_modelos


def test_minmax_e_local():
    assert minimo_global([3,1,2], lambda x:x*x)==(1,1)
    assert maximo_global([3,1,2], lambda x:x)==(3,3)
    assert minimo_local(0, lambda x:[x-1,x+1], lambda y:y*y)


def test_treino_finito():
    dados=[(1,2),(2,4),(3,6)]
    fabrica=lambda p: (lambda x:p*x)
    assert perda_quadratica_catalogo(fabrica(2), dados)==0
    assert treinar_por_busca([1,2,3], fabrica, dados)==2
    modelo, erro=comparar_modelos([fabrica(1),fabrica(2)], dados)
    assert erro==0 and modelo(4)==8


def test_gulosa():
    assert busca_gulosa(5, lambda x:[x-1] if x>0 else [], lambda x:x)==0
