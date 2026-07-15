from lingua_portuguesa.normalizacao_pontuacao import (
    capitalizar_inicio_de_frases,
    garantir_pontuacao_final,
    normalizar_espacos_pontuacao,
    normalizar_paragrafos,
    normalizar_texto_corrido,
)


# --- normalizar_espacos_pontuacao ---------------------------------------

def test_espacos_remove_espaco_antes_de_virgula_e_ponto():
    assert normalizar_espacos_pontuacao("Olá ,mundo .") == "Olá, mundo."


def test_espacos_texto_ja_correto_fica_igual():
    original = "Olá, mundo."
    assert normalizar_espacos_pontuacao(original) == original


def test_espacos_parenteses_ja_corretos_ficam_iguais():
    original = "texto (nota) fim"
    assert normalizar_espacos_pontuacao(original) == original


def test_espacos_corrige_parenteses_mal_espacados():
    assert normalizar_espacos_pontuacao("texto( nota )fim") == "texto (nota) fim"


def test_espacos_colapsa_espacos_duplicados_entre_palavras():
    assert normalizar_espacos_pontuacao("uma   frase   qualquer") == "uma frase qualquer"


def test_espacos_nao_mexe_em_quebra_de_linha():
    original = "linha um.\n\nlinha dois."
    assert normalizar_espacos_pontuacao(original) == original


def test_espacos_pontuacao_fechamento_consecutiva_fica_colada():
    assert normalizar_espacos_pontuacao("(nota)) fim") == "(nota)) fim"


def test_espacos_string_vazia():
    assert normalizar_espacos_pontuacao("") == ""


# --- capitalizar_inicio_de_frases ---------------------------------------

def test_capitaliza_inicio_do_texto_e_apos_pontuacao_final():
    entrada = "frase um. frase dois! frase três?"
    assert capitalizar_inicio_de_frases(entrada) == "Frase um. Frase dois! Frase três?"


def test_capitaliza_texto_ja_capitalizado_fica_igual():
    original = "Frase um. Frase dois."
    assert capitalizar_inicio_de_frases(original) == original


def test_capitaliza_ignora_espacos_e_aspas_de_abertura():
    entrada = '"frase entre aspas."'
    assert capitalizar_inicio_de_frases(entrada) == '"Frase entre aspas."'


def test_capitaliza_nao_forca_maiuscula_se_frase_comeca_com_numero():
    entrada = "3 é um número primo."
    assert capitalizar_inicio_de_frases(entrada) == entrada


def test_capitaliza_string_vazia():
    assert capitalizar_inicio_de_frases("") == ""


# --- garantir_pontuacao_final --------------------------------------------

def test_pontuacao_final_acrescenta_ponto_se_faltar():
    assert garantir_pontuacao_final("frase sem ponto final") == "frase sem ponto final."


def test_pontuacao_final_nao_mexe_se_ja_tem():
    for original in ("frase com ponto.", "frase com exclamação!", "frase com interrogação?", "frase com reticências…"):
        assert garantir_pontuacao_final(original) == original


def test_pontuacao_final_preserva_espaco_em_branco_no_fim():
    assert garantir_pontuacao_final("frase sem ponto \n") == "frase sem ponto. \n"


def test_pontuacao_final_string_vazia_ou_so_espaco():
    assert garantir_pontuacao_final("") == ""
    assert garantir_pontuacao_final("   ") == "   "


# --- normalizar_paragrafos ------------------------------------------------

def test_paragrafos_colapsa_linhas_vazias_multiplas_em_uma():
    assert normalizar_paragrafos("Para um.\n\n\n\nPara dois.") == "Para um.\n\nPara dois."


def test_paragrafos_ja_com_uma_linha_em_branco_fica_igual():
    original = "Para um.\n\nPara dois."
    assert normalizar_paragrafos(original) == original


def test_paragrafos_nao_mexe_em_quebra_de_linha_simples():
    original = "linha um\nlinha dois"
    assert normalizar_paragrafos(original) == original


def test_paragrafos_remove_espaco_sobrando_antes_da_quebra():
    assert normalizar_paragrafos("linha um   \n\nlinha dois") == "linha um\n\nlinha dois"


def test_paragrafos_normaliza_crlf():
    assert normalizar_paragrafos("linha um\r\n\r\nlinha dois") == "linha um\n\nlinha dois"


# --- normalizar_texto_corrido (pipeline completo) -------------------------

def test_pipeline_completo_corrige_texto_com_varios_problemas():
    entrada = "  isto é uma frase mal formatada ,com espaços errados  e sem ponto final"
    resultado = normalizar_texto_corrido(entrada)
    assert resultado.startswith("Isto é uma frase")
    assert ", com" in resultado
    assert resultado.rstrip().endswith(".")
    assert ",com" not in resultado


def test_pipeline_preserva_paragrafos_e_capitaliza_cada_um():
    entrada = "primeira frase sem maiúscula.\n\n\nsegunda frase, também sem maiúscula."
    resultado = normalizar_texto_corrido(entrada)
    assert resultado == "Primeira frase sem maiúscula.\n\nSegunda frase, também sem maiúscula."


def test_pipeline_texto_ja_perfeito_fica_essencialmente_igual():
    entrada = "Este texto já está correto. Não deveria mudar nada relevante."
    resultado = normalizar_texto_corrido(entrada)
    assert resultado == entrada
