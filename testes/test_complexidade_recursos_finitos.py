import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nucleo.complexidade_recursos_finitos import conta_passos, pior_caso_por_catalogo, melhor_caso_por_catalogo, reducao_finita


def test_conta_passos():
    r=conta_passos(lambda x:x+1,0,lambda x:x==3,limite=10)
    assert r['terminou'] and r['passos']==3


def test_casos_catalogo_e_reducao():
    custos=[{'n':1,'passos':2},{'n':2,'passos':5},{'n':3,'passos':4}]
    assert pior_caso_por_catalogo(custos)['n']==2
    assert melhor_caso_por_catalogo(custos)['n']==1
    assert reducao_finita([1,2,3], lambda x:x+1, lambda x:x%2==0, lambda y:(y-1)%2==0)
