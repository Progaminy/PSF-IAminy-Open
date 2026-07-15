from lingua_portuguesa import ClasseGramatical, Dicionario, EntradaLexical, Genero, MotorPortugues, Numero
from lingua_portuguesa.desambiguacao import escolher_leitura
from lingua_portuguesa.tipos import Pessoa


def _dicionario_com_palavra_ambigua() -> Dicionario:
    dicionario = Dicionario()
    dicionario.adicionar(
        EntradaLexical("eu", "eu", ClasseGramatical.PRONOME, pessoa=Pessoa.PRIMEIRA, numero=Numero.SINGULAR)
    )
    dicionario.adicionar(
        EntradaLexical(
            "banco", "banco", ClasseGramatical.SUBSTANTIVO,
            ("Assento comprido.",), genero=Genero.MASCULINO, numero=Numero.SINGULAR,
        )
    )
    dicionario.adicionar(
        EntradaLexical(
            "bancar", "banco", ClasseGramatical.VERBO,
            ("Sustentar financeiramente.",), pessoa=Pessoa.PRIMEIRA, numero=Numero.SINGULAR,
        )
    )
    dicionario.adicionar(
        EntradaLexical("gostar", "gosto", ClasseGramatical.VERBO, pessoa=Pessoa.PRIMEIRA, numero=Numero.SINGULAR)
    )
    dicionario.adicionar(EntradaLexical("de", "de", ClasseGramatical.PREPOSICAO))
    return dicionario


def test_escolhe_leitura_de_verbo_quando_frase_parece_sem_verbo():
    motor = MotorPortugues(dicionario=_dicionario_com_palavra_ambigua())
    analise = motor.analisar("Eu banco.")
    indice_banco = next(i for i, a in enumerate(analise.morfologia) if a.token.texto == "banco")
    alvo = analise.morfologia[indice_banco]
    assert len(alvo.leituras) == 2  # confirma que a ambiguidade existe de verdade
    vizinhanca = analise.morfologia[:indice_banco] + analise.morfologia[indice_banco + 1:]
    escolhida = escolher_leitura(alvo, vizinhanca)
    assert escolhida.classe == ClasseGramatical.VERBO


def test_escolhe_leitura_de_substantivo_quando_ja_ha_verbo_real_na_frase():
    motor = MotorPortugues(dicionario=_dicionario_com_palavra_ambigua())
    analise = motor.analisar("Eu gosto de banco.")
    indice_banco = next(i for i, a in enumerate(analise.morfologia) if a.token.texto == "banco")
    alvo = analise.morfologia[indice_banco]
    vizinhanca = analise.morfologia[:indice_banco] + analise.morfologia[indice_banco + 1:]
    escolhida = escolher_leitura(alvo, vizinhanca)
    assert escolhida.classe == ClasseGramatical.SUBSTANTIVO


def test_palavra_nao_ambigua_devolve_principal_sem_olhar_vizinhanca():
    motor = MotorPortugues(dicionario=_dicionario_com_palavra_ambigua())
    analise = motor.analisar("Eu gosto.")
    indice_gosto = next(i for i, a in enumerate(analise.morfologia) if a.token.texto == "gosto")
    alvo = analise.morfologia[indice_gosto]
    assert len(alvo.leituras) == 1
    escolhida = escolher_leitura(alvo, ())
    assert escolhida is alvo.principal
