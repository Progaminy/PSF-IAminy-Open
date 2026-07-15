import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nucleo.topologia_finita import eh_topologia_finita, interior, fecho, continua_finita


def test_topologia_basica():
    U={1,2}
    T=[set(),{1},{1,2}]
    assert eh_topologia_finita(U,T)
    assert interior({1,2},T)==frozenset({1,2})
    assert fecho(U,{2},T)==frozenset({2})


def test_continuidade_finita():
    origem=[set(),{'a'},{'a','b'}]
    destino=[set(),{1},{1,2}]
    f={'a':1,'b':2}
    assert continua_finita(f, origem, destino)
