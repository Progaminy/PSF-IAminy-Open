from lingua_portuguesa.corretor import PESOS_PADRAO, pontuar, ranquear
from lingua_portuguesa.tipos_corretor import Candidato


def test_pontuar_soma_ponderada_valor_exato():
    candidato = Candidato(
        forma="x",
        distancia_edicao=1,
        similaridade_fonetica=1.0,
        frequencia=0.1,
        probabilidade_contexto=0.5,
        proximidade_semantica=0.2,
        peso_erro=0.3,
        compatibilidade_gramatical=True,
    )
    # 0.30*(1/2) + 0.20*1 + 0.15*0.5 + 0.15*1 + 0.10*0.3 + 0.05*0.1 + 0.05*0.2
    esperado = (
        PESOS_PADRAO["distancia_edicao"] * 0.5
        + PESOS_PADRAO["compatibilidade_gramatical"] * 1.0
        + PESOS_PADRAO["probabilidade_contexto"] * 0.5
        + PESOS_PADRAO["similaridade_fonetica"] * 1.0
        + PESOS_PADRAO["peso_erro"] * 0.3
        + PESOS_PADRAO["frequencia"] * 0.1
        + PESOS_PADRAO["proximidade_semantica"] * 0.2
    )
    assert abs(pontuar(candidato) - esperado) < 1e-9
    assert abs(pontuar(candidato) - 0.620) < 1e-9


def test_pontuar_sinal_ausente_contribui_zero():
    so_distancia = Candidato(forma="x", distancia_edicao=0)
    assert abs(pontuar(so_distancia) - PESOS_PADRAO["distancia_edicao"]) < 1e-9

    nenhum_sinal = Candidato(forma="x")
    assert pontuar(nenhum_sinal) == 0.0


def test_ranquear_ordena_por_pontuacao_descendente():
    forte = Candidato(forma="forte", distancia_edicao=0)
    fraco = Candidato(forma="fraco", distancia_edicao=5)
    vazio = Candidato(forma="vazio")
    resultado = ranquear((fraco, vazio, forte))
    assert tuple(c.forma for c in resultado) == ("forte", "fraco", "vazio")


def test_ranquear_desempate_por_forma_quando_pontuacao_e_frequencia_empatam():
    zebra = Candidato(forma="zebra", similaridade_fonetica=1.0)
    abacate = Candidato(forma="abacate", probabilidade_contexto=1.0)
    # ambos pontuam 0.15 (mesmo peso: similaridade_fonetica == probabilidade_contexto)
    assert abs(pontuar(zebra) - pontuar(abacate)) < 1e-9
    resultado = ranquear((zebra, abacate))
    assert tuple(c.forma for c in resultado) == ("abacate", "zebra")


def test_ranquear_desempate_por_frequencia_antes_do_alfabeto():
    pesos_sem_frequencia = {**PESOS_PADRAO, "frequencia": 0.0}
    populares = Candidato(forma="zzzz", similaridade_fonetica=1.0, frequencia=0.9)
    rara = Candidato(forma="aaaa", similaridade_fonetica=1.0, frequencia=0.1)
    assert abs(pontuar(populares, pesos_sem_frequencia) - pontuar(rara, pesos_sem_frequencia)) < 1e-9
    resultado = ranquear((populares, rara), pesos_sem_frequencia)
    assert tuple(c.forma for c in resultado) == ("zzzz", "aaaa")
