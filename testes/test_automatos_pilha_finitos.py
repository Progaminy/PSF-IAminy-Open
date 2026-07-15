import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from nucleo.automatos_pilha_finitos import aceita_pilha, parenteses_balanceados_finito


def test_parenteses_funcao_direta():
    assert parenteses_balanceados_finito('(())')
    assert not parenteses_balanceados_finito('(()')


def test_automato_pilha_simples_an_bn():
    # reconhece a^n b^n para catálogo pequeno
    trans={
        ('q','a','$'):[('q',('$','A'))],
        ('q','a','A'):[('q',('A','A'))],
        ('q','b','A'):[('p',())],
        ('p','b','A'):[('p',())],
        ('p',None,'$'):[('f',('$',))],
    }
    assert aceita_pilha('aabb','q',{'f'},('$',),trans,limite=50)
    assert not aceita_pilha('aaab','q',{'f'},('$',),trans,limite=50)
