import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nucleo.reescrita_provas_finitas import forma_normal_limitada, equivalente_por_reescrita, derivacao_valida, grafo_reescrita


def test_normalizacao():
    regras=[(('add',0,'x'),'x'), (('mul',1,'x'),'x')]
    assert forma_normal_limitada(('add',0,'x'), regras)=='x'
    assert equivalente_por_reescrita(('mul',1,'x'),'x',regras)


def test_derivacao_e_grafo():
    regras=[('a','b'),('b','c')]
    assert derivacao_valida('a','c',regras,['b','c'])
    assert grafo_reescrita(['a','b','c'],regras)=={'a':'b','b':'c','c':'c'}
