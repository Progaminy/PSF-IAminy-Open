"""Corpus minúsculo e construído à mão -- todo valor esperado abaixo foi
calculado manualmente (não é fixture opaca), exatamente porque contagem +
suavização de Laplace é aritmética simples, verificável por qualquer
pessoa lendo o teste.
"""
from lingua_portuguesa.modelo_ngramas import ModeloNGrama

_TOKENS = ("o", "gato", "corre", "o", "gato", "pula")
# unigramas: o=2, gato=2, corre=1, pula=1 -- total=6, vocabulário=4
# bigramas: (o,gato)=2, (gato,corre)=1, (corre,o)=1, (gato,pula)=1


def _modelo() -> ModeloNGrama:
    return ModeloNGrama(tokens=_TOKENS, suavizacao=1.0)


def test_contagens_unigrama_e_bigrama_exatas():
    modelo = _modelo()
    assert modelo.contagem_unigrama("o") == 2
    assert modelo.contagem_unigrama("gato") == 2
    assert modelo.contagem_unigrama("corre") == 1
    assert modelo.contagem_unigrama("ausente") == 0
    assert modelo.contagem_bigrama("o", "gato") == 2
    assert modelo.contagem_bigrama("gato", "corre") == 1
    assert modelo.contagem_bigrama("gato", "ausente") == 0


def test_probabilidade_condicional_bigrama_valor_exato():
    # (contagem(o,gato) + 1) / (contagem(o) + 1*vocabulario) = (2+1)/(2+4) = 0.5
    modelo = _modelo()
    assert modelo.probabilidade_condicional("gato", "o") == 3 / 6


def test_probabilidade_condicional_unigrama_valor_exato():
    # (contagem(corre) + 1) / (total + 1*vocabulario) = (1+1)/(6+4) = 0.2
    modelo = _modelo()
    assert modelo.probabilidade_condicional("corre", anterior=None) == 2 / 10


def test_probabilidade_condicional_bigrama_nunca_visto_valor_exato():
    # (0 + 1) / (contagem(o) + 1*vocabulario) = 1/(2+4) = 1/6
    modelo = _modelo()
    assert modelo.probabilidade_condicional("inexistente", "o") == 1 / 6


def test_escolher_por_contexto_prefere_bigrama_mais_provavel():
    modelo = _modelo()
    assert modelo.escolher_por_contexto(("corre", "gato"), anterior="o") == "gato"


def test_escolher_por_contexto_sem_anterior_usa_unigrama():
    modelo = _modelo()
    # unigrama: gato(2) > corre(1) > pula(1)
    assert modelo.escolher_por_contexto(("corre", "gato"), anterior=None) == "gato"


def test_modelo_padrao_usa_corpus_interno_e_nao_e_trivial():
    modelo = ModeloNGrama()
    assert modelo.contagem_unigrama("que") > 0
