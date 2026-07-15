"""Fim-a-fim, com o motor real (`Dicionario.padrao()`), não um dicionário
controlado -- prova que o pipeline completo (normalização + whitelist +
parônimo + sugestão ranqueada) funciona sobre frases reais com erro real.
"""
from lingua_portuguesa import Dicionario, Numero
from lingua_portuguesa.corretor import Corretor
from lingua_portuguesa.tipos import Pessoa


def test_normaliza_espaco_maiuscula_e_pontuacao_final():
    corretor = Corretor()
    resultado = corretor.corrigir_texto(
        "  isto e um texto sem pontuacao final e com  espacos  errados"
    )
    assert resultado.normalizado == "Isto e um texto sem pontuacao final e com espacos errados."
    assert resultado.corrigido == resultado.normalizado


def test_aplica_correcao_da_whitelist_conhecida():
    corretor = Corretor()
    resultado = corretor.corrigir_texto("a reposta esta correta.")
    assert resultado.alteracoes_whitelist == (("reposta", "resposta", "troca comum de letras"),)
    assert "resposta" in resultado.corrigido
    assert "reposta" not in resultado.corrigido


def test_avisa_paronimo_sem_trocar_sozinho():
    corretor = Corretor()
    resultado = corretor.corrigir_texto("marquei a sessão para amanhã.")
    assert len(resultado.notas_paronimo) == 1
    assert "cessão" in resultado.notas_paronimo[0]
    assert "seção" in resultado.notas_paronimo[0]
    # nunca troca sozinho -- a palavra original continua no texto corrigido.
    assert "sessão" in resultado.corrigido


def test_sugere_candidatos_ranqueados_para_palavra_fora_do_dicionario():
    corretor = Corretor()
    resultado = corretor.corrigir_texto("estudo protugues todos os dias.")
    sugestoes = dict(resultado.sugestoes_ortografia)
    assert "protugues" in sugestoes
    assert "português" in sugestoes["protugues"]


def test_forma_verbal_foi_nao_e_confundida_com_interjeicao_oi():
    resultado = Corretor().corrigir_texto("Ele foi a escola.")
    sugestoes = dict(resultado.sugestoes_ortografia)
    assert "oi" not in sugestoes.get("foi", ())


def test_preterito_perfeito_dos_onze_verbos_irregulares_tem_as_leituras_pedidas():
    primeira = Pessoa.PRIMEIRA
    terceira = Pessoa.TERCEIRA
    singular = Numero.SINGULAR
    plural = Numero.PLURAL
    esperadas = {
        ("ser", "fui"): {(primeira, singular)},
        ("ser", "foi"): {(terceira, singular)},
        ("ser", "foram"): {(terceira, plural)},
        ("estar", "estive"): {(primeira, singular)},
        ("estar", "esteve"): {(terceira, singular)},
        ("estar", "estiveram"): {(terceira, plural)},
        ("ter", "tive"): {(primeira, singular)},
        ("ter", "teve"): {(terceira, singular)},
        ("ter", "tiveram"): {(terceira, plural)},
        ("fazer", "fiz"): {(primeira, singular)},
        ("fazer", "fez"): {(terceira, singular)},
        ("fazer", "fizeram"): {(terceira, plural)},
        ("ir", "fui"): {(primeira, singular)},
        ("ir", "foi"): {(terceira, singular)},
        ("ir", "foram"): {(terceira, plural)},
        ("querer", "quis"): {(primeira, singular), (terceira, singular)},
        ("querer", "quiseram"): {(terceira, plural)},
        ("poder", "pude"): {(primeira, singular)},
        ("poder", "pôde"): {(terceira, singular)},
        ("poder", "puderam"): {(terceira, plural)},
        ("saber", "soube"): {(primeira, singular), (terceira, singular)},
        ("saber", "souberam"): {(terceira, plural)},
        ("dizer", "disse"): {(primeira, singular), (terceira, singular)},
        ("dizer", "disseram"): {(terceira, plural)},
        ("ver", "vi"): {(primeira, singular)},
        ("ver", "viu"): {(terceira, singular)},
        ("ver", "viram"): {(terceira, plural)},
        ("dar", "dei"): {(primeira, singular)},
        ("dar", "deu"): {(terceira, singular)},
        ("dar", "deram"): {(terceira, plural)},
    }
    dicionario = Dicionario.padrao()

    for (lema, forma), flexoes in esperadas.items():
        leituras = {
            (entrada.pessoa, entrada.numero)
            for entrada in dicionario.buscar(forma)
            if entrada.lema == lema
            and entrada.atributos.get("tempo") == "pretérito perfeito"
        }
        assert leituras == flexoes, (lema, forma, leituras)


def test_texto_sem_erro_conhecido_nao_aciona_whitelist():
    corretor = Corretor()
    resultado = corretor.corrigir_texto("A resposta está correta.")
    assert resultado.alteracoes_whitelist == ()
    assert resultado.corrigido == resultado.normalizado


def test_candidatos_para_expõe_pontuacao_e_ordem():
    corretor = Corretor()
    candidatos = corretor.candidatos_para("protugues")
    assert candidatos
    assert candidatos[0].forma == "português"
    # ordenado por pontuação descendente de verdade, não por acaso.
    pontuacoes = [c for c in candidatos]
    from lingua_portuguesa.corretor import pontuar

    valores = [pontuar(c) for c in pontuacoes]
    assert valores == sorted(valores, reverse=True)
