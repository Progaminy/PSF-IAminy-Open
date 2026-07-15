import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nucleo.semantica_denotacional_finita import valor_expr, denota_comando, equivalente_por_catalogo, tripla_hoare_finita, invariante_finito


def test_expr_e_comando():
    env={'x':2}
    assert valor_expr(('add',('var','x'),('const',3)), env)==5
    prog=('seq',('assign','y',('mul',('var','x'),('const',4))),('assign','z',('add',('var','y'),('const',1))))
    assert denota_comando(prog, env)['z']==9


def test_equivalencia_e_hoare():
    a=('assign','x',('add',('var','x'),('const',1)))
    b=('assign','x',('add',('const',1),('var','x')))
    assert equivalente_por_catalogo(a,b,[{'x':0},{'x':5}])
    assert tripla_hoare_finita(lambda e:e['x']>=0, a, lambda e:e['x']>0, [{'x':0},{'x':2}])


def test_invariante():
    loop=('while',('lt',('var','x'),('const',3)),('assign','x',('add',('var','x'),('const',1))))
    assert invariante_finito(lambda e:e['x']<=3, loop, {'x':0})
