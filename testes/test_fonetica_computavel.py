from lingua_portuguesa.conhecimento_puro import CONCEITOS_PORTUGUES_PURO
from lingua_portuguesa.fonetica_computavel import TRACOS_GRAFEMA, codigo_fonetico


def test_coerencia_tracos_correspondem_a_conceitos_reais():
    """Nenhum rótulo de traço usado em TRACOS_GRAFEMA pode ser inventado --
    tem que ser o nome exato de um ConceitoPortugues real do tema
    fonetica_fonologia. Teste machine-checked, não confiança de leitura."""
    nomes_reais = {c.nome for c in CONCEITOS_PORTUGUES_PURO if c.camada == "fonetica_fonologia"}
    assert nomes_reais, "tema fonetica_fonologia deveria ter conceitos reais"
    for grafema, tracos in TRACOS_GRAFEMA.items():
        for dimensao, rotulo in tracos.items():
            assert rotulo in nomes_reais, (
                f"grafema {grafema!r}, dimensão {dimensao!r}: rótulo {rotulo!r} "
                "não corresponde a nenhum conceito real de fonetica_fonologia"
            )


def test_pares_sonoros_surdos_colapsam_no_mesmo_codigo():
    # a confusão sonora/surda (s/z, c/ç) é a fonte mais comum de erro real
    # de ortografia -- ambas devem cair na mesma classe de agrupamento.
    assert codigo_fonetico("caça") == codigo_fonetico("cassa")
    assert codigo_fonetico("casa") == codigo_fonetico("caza")


def test_palavras_com_consoantes_de_classes_diferentes_nao_colapsam():
    assert codigo_fonetico("casa") != codigo_fonetico("cama")
    assert codigo_fonetico("pato") != codigo_fonetico("mato")


def test_codigo_mantem_primeiro_grafema_intacto():
    assert codigo_fonetico("chuva").startswith("ch")
    assert codigo_fonetico("xuva").startswith("x")
    # por isso "chuva" e "xuva" não colapsam, apesar do resto ser igual --
    # propriedade real do Soundex clássico, não uma falha.
    assert codigo_fonetico("chuva") != codigo_fonetico("xuva")


def test_codigo_colapsa_consoantes_repetidas_da_mesma_classe():
    assert codigo_fonetico("carro") == codigo_fonetico("caro")


def test_codigo_ignora_vogais_diferentes_entre_consoantes_iguais():
    assert codigo_fonetico("bala") == codigo_fonetico("bola")


def test_string_vazia():
    assert codigo_fonetico("") == ""


def test_digrafo_nh_e_reconhecido_como_unidade_palatal_distinta_de_n():
    # "nh" (palatal) não pode virar "n"(alveolar)+"h"(sem traço) -- isso
    # mudaria a classe de agrupamento e coincidiria por acaso com "n" puro.
    assert TRACOS_GRAFEMA["nh"]["ponto"] == "palatal"
    assert codigo_fonetico("sono") != codigo_fonetico("sonho")
