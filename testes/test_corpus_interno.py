from lingua_portuguesa.conhecimento_puro import CONCEITOS_PORTUGUES_PURO
from lingua_portuguesa.corpus_interno import (
    frases_da_prosa_autoral_ampla,
    frases_do_conhecimento_puro,
    tokens_do_corpus,
    tokens_do_corpus_amplo,
)


def test_frases_nao_e_trivial_e_reflete_a_quantidade_de_conceitos():
    frases = frases_do_conhecimento_puro()
    # cada conceito contribui pelo menos construção+função -- o corpus
    # tem que crescer com o conhecimento real, nunca ser um número fixo.
    assert len(frases) >= 2 * len(CONCEITOS_PORTUGUES_PURO)


def test_tokens_nao_e_trivial():
    tokens = tokens_do_corpus()
    assert len(tokens) > 5000


def test_bigrama_real_do_primeiro_conceito_aparece_no_corpus():
    # concept 1 "diferença": construção real conhecida, palavra por
    # palavra -- prova que o corpus vem de texto real, não sintético.
    tokens = tokens_do_corpus()
    indice = next(i for i, t in enumerate(tokens) if t == "perceber")
    assert tokens[indice] == "perceber"
    assert tokens[indice + 1] == "que"


def test_tokens_sao_so_palavras_sem_pontuacao():
    tokens = tokens_do_corpus()
    assert "." not in tokens
    assert "," not in tokens


def test_frases_de_um_conceito_conhecido_estao_presentes():
    frases = frases_do_conhecimento_puro()
    assert "O primeiro conhecimento é perceber que uma ocorrência pode ser separada de outra." in frases


def test_prosa_autoral_ampla_le_documentos_reais_fora_de_conhecimento_puro():
    frases = frases_da_prosa_autoral_ampla()
    # README + RELATORIO_UNICO + PLANO + COMO_RODAR + conhecimento/*.md
    # (203 ETAPAs + auditorias) -- bem mais que os documentos únicos
    # centrais, prova que a leitura varreu o diretório inteiro.
    assert len(frases) > 200


def test_prosa_autoral_ampla_nao_traz_identificador_de_codigo():
    texto_completo = " ".join(frases_da_prosa_autoral_ampla())
    # `SOMA`/`MULT`/`ITER` só aparecem em trechos de código (crase) nos
    # documentos -- se aparecerem aqui, o filtro de código falhou.
    assert "`SOMA`" not in texto_completo
    assert "`MULT`" not in texto_completo


def test_tokens_do_corpus_amplo_e_maior_que_o_corpus_estreito():
    estreito = tokens_do_corpus()
    amplo = tokens_do_corpus_amplo()
    assert len(set(amplo)) > len(set(estreito))
    # o corpus estreito continua inteiramente contido no amplo -- é adição
    # pura, nunca substituição.
    assert set(estreito) <= set(amplo)


def test_tokens_do_corpus_amplo_descarta_tokens_curtos_demais():
    amplo = tokens_do_corpus_amplo()
    estreito = set(tokens_do_corpus())
    assert not any(len(t) < 3 for t in amplo if t not in estreito)
