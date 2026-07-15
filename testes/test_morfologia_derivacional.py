from pathlib import Path

from lingua_portuguesa.tipos import ClasseGramatical, EntradaLexical, Genero
from lingua_portuguesa.morfologia_derivacional import (
    gerar_adjetivos_avel_ivel,
    gerar_adjetivos_negativos_in,
    gerar_adjetivos_oso,
    gerar_adverbios_mente,
    gerar_agentes_dor,
    gerar_diminutivos,
    gerar_substantivos_ista,
    gerar_substantivos_mento,
    validar_candidatos,
)

_ADJ_CLARO = EntradaLexical("claro", "claro", ClasseGramatical.ADJETIVO, ("Fácil de perceber.",))
_ADJ_PERFEITO = EntradaLexical("perfeito", "perfeito", ClasseGramatical.ADJETIVO, ("Completo.",))
_NOME_GATO = EntradaLexical("gato", "gato", ClasseGramatical.SUBSTANTIVO, ("Felino doméstico.",), Genero.MASCULINO)
_NOME_FLOR = EntradaLexical("flor", "flor", ClasseGramatical.SUBSTANTIVO, ("Parte da planta.",), Genero.FEMININO)
_NOME_PERIGO = EntradaLexical("perigo", "perigo", ClasseGramatical.SUBSTANTIVO, ("Situação de risco.",), Genero.MASCULINO)
_VERBO_CORRER = EntradaLexical("correr", "correr", ClasseGramatical.VERBO, ("Deslocar-se rápido.",))
_VERBO_TRABALHAR = EntradaLexical("trabalhar", "trabalhar", ClasseGramatical.VERBO, ("Exercer atividade produtiva.",))
_VERBO_TRANSMITIR = EntradaLexical("transmitir", "transmitir", ClasseGramatical.VERBO, ("Fazer chegar de um ponto a outro.",))
_VERBO_PAGAR = EntradaLexical("pagar", "pagar", ClasseGramatical.VERBO, ("Entregar valor devido.",))
_VERBO_CONHECER = EntradaLexical("conhecer", "conhecer", ClasseGramatical.VERBO, ("Ter familiaridade com algo.",))
_VERBO_AMAR = EntradaLexical("amar", "amar", ClasseGramatical.VERBO, ("Ter amor por alguém ou algo.",))
_VERBO_VENDER = EntradaLexical("vender", "vender", ClasseGramatical.VERBO, ("Trocar algo por dinheiro.",))
_VERBO_PARTIR = EntradaLexical("partir", "partir", ClasseGramatical.VERBO, ("Dividir ou ir embora.",))
_NOME_ARTE = EntradaLexical("arte", "arte", ClasseGramatical.SUBSTANTIVO, ("Expressão criativa humana.",), Genero.FEMININO)
_NOME_JORNAL = EntradaLexical("jornal", "jornal", ClasseGramatical.SUBSTANTIVO, ("Publicação periódica de notícias.",), Genero.MASCULINO)
_ADJ_FELIZ = EntradaLexical("feliz", "feliz", ClasseGramatical.ADJETIVO, ("Que sente alegria.",))
_ADJ_POSSIVEL = EntradaLexical("possível", "possível", ClasseGramatical.ADJETIVO, ("Que pode acontecer.",))
_ADJ_LEGAL = EntradaLexical("legal", "legal", ClasseGramatical.ADJETIVO, ("Conforme a lei.",))
_ADJ_RESPONSAVEL = EntradaLexical("responsável", "responsável", ClasseGramatical.ADJETIVO, ("Que responde por algo.",))
_ADJ_MORAL = EntradaLexical("moral", "moral", ClasseGramatical.ADJETIVO, ("Relativo aos costumes e valores.",))
_VERBO_SER = EntradaLexical("ser", "ser", ClasseGramatical.VERBO, ("Existir ou apresentar característica.",))
_VERBO_IR = EntradaLexical("ir", "ir", ClasseGramatical.VERBO, ("Deslocar-se para um lugar.",))


def test_adverbio_mente_usa_feminino_singular_do_adjetivo():
    candidatos = gerar_adverbios_mente((_ADJ_CLARO,))
    assert len(candidatos) == 1
    assert candidatos[0].forma == "claramente"
    assert candidatos[0].classe == ClasseGramatical.ADVERBIO
    assert "claro" in candidatos[0].definicao


def test_adverbio_mente_ignora_nao_adjetivos():
    candidatos = gerar_adverbios_mente((_NOME_GATO, _VERBO_CORRER))
    assert candidatos == ()


def test_adverbio_mente_nao_duplica_lema_repetido():
    candidatos = gerar_adverbios_mente((_ADJ_CLARO, _ADJ_CLARO))
    assert len(candidatos) == 1


def test_diminutivo_vogal_atona_final_cai():
    candidatos = gerar_diminutivos((_NOME_GATO,))
    assert candidatos[0].forma == "gatinho"


def test_diminutivo_consoante_final_usa_zinho():
    candidatos = gerar_diminutivos((_NOME_FLOR,))
    assert candidatos[0].forma == "florzinha"  # género feminino do lema


def test_diminutivo_vogal_tonica_acentuada_usa_zinho():
    cafe = EntradaLexical("café", "café", ClasseGramatical.SUBSTANTIVO, ("Bebida.",), Genero.MASCULINO)
    candidatos = gerar_diminutivos((cafe,))
    assert candidatos[0].forma == "cafézinho"


def test_diminutivo_ignora_verbos():
    candidatos = gerar_diminutivos((_VERBO_CORRER,))
    assert candidatos == ()


def test_agente_dor_ar_gera_forma_masculina_e_feminina():
    candidatos = gerar_agentes_dor((_VERBO_TRABALHAR,))
    formas = {c.forma for c in candidatos}
    assert formas == {"trabalhador", "trabalhadora"}
    assert all(c.classe == ClasseGramatical.SUBSTANTIVO for c in candidatos)


def test_agente_dor_er_usa_edor():
    candidatos = gerar_agentes_dor((_VERBO_CORRER,))
    assert {c.forma for c in candidatos} == {"corredor", "corredora"}


def test_agente_dor_ir_usa_idor():
    candidatos = gerar_agentes_dor((_VERBO_TRANSMITIR,))
    assert {c.forma for c in candidatos} == {"transmitidor", "transmitidora"}


def test_agente_dor_ignora_nao_verbos():
    assert gerar_agentes_dor((_NOME_GATO,)) == ()


def test_agente_dor_ignora_verbo_de_3_letras_ou_menos():
    # achado real: "ser"/"ir" (raiz suplectiva, não regular) sem este
    # guard geravam "sedor"/"idor" -- raiz de 0-1 letra, nenhum candidato
    # real confirmado pelo oráculo. Verbo curto demais não tem raiz
    # regular suficiente pra sufixo -dor.
    assert gerar_agentes_dor((_VERBO_SER, _VERBO_IR)) == ()


def test_substantivo_mento_ar_usa_amento():
    candidatos = gerar_substantivos_mento((_VERBO_PAGAR,))
    assert len(candidatos) == 1
    assert candidatos[0].forma == "pagamento"
    assert candidatos[0].classe == ClasseGramatical.SUBSTANTIVO


def test_substantivo_mento_er_usa_imento():
    candidatos = gerar_substantivos_mento((_VERBO_CONHECER,))
    assert candidatos[0].forma == "conhecimento"


def test_substantivo_mento_ignora_nao_verbos():
    assert gerar_substantivos_mento((_NOME_GATO,)) == ()


def test_substantivo_mento_ignora_verbo_de_3_letras_ou_menos():
    assert gerar_substantivos_mento((_VERBO_SER, _VERBO_IR)) == ()


def test_adjetivo_oso_a_partir_de_substantivo():
    candidatos = gerar_adjetivos_oso((_NOME_PERIGO,))
    assert len(candidatos) == 1
    assert candidatos[0].forma == "perigoso"
    assert candidatos[0].classe == ClasseGramatical.ADJETIVO


def test_adjetivo_oso_ignora_nao_substantivos():
    assert gerar_adjetivos_oso((_VERBO_CORRER,)) == ()


def test_avel_ivel_ar_usa_avel():
    candidatos = gerar_adjetivos_avel_ivel((_VERBO_AMAR,))
    assert len(candidatos) == 1
    assert candidatos[0].forma == "amável"
    assert candidatos[0].classe == ClasseGramatical.ADJETIVO


def test_avel_ivel_er_usa_ivel():
    candidatos = gerar_adjetivos_avel_ivel((_VERBO_VENDER,))
    assert candidatos[0].forma == "vendível"


def test_avel_ivel_ir_usa_ivel():
    candidatos = gerar_adjetivos_avel_ivel((_VERBO_PARTIR,))
    assert candidatos[0].forma == "partível"


def test_avel_ivel_ignora_nao_verbos():
    assert gerar_adjetivos_avel_ivel((_NOME_GATO,)) == ()


def test_avel_ivel_ignora_verbo_de_3_letras_ou_menos():
    # achado real: "ser"->"sível" e "ir"->"ível" (raiz vazia) antes deste
    # guard -- nenhum dos dois é palavra, mesma causa raiz do agente_dor.
    assert gerar_adjetivos_avel_ivel((_VERBO_SER, _VERBO_IR)) == ()


def test_avel_ivel_nao_duplica_lema_repetido():
    candidatos = gerar_adjetivos_avel_ivel((_VERBO_AMAR, _VERBO_AMAR))
    assert len(candidatos) == 1


def test_substantivo_ista_vogal_atona_final_cai():
    candidatos = gerar_substantivos_ista((_NOME_ARTE,))
    assert len(candidatos) == 1
    assert candidatos[0].forma == "artista"
    assert candidatos[0].classe == ClasseGramatical.SUBSTANTIVO


def test_substantivo_ista_consoante_final_nao_corta():
    candidatos = gerar_substantivos_ista((_NOME_JORNAL,))
    assert candidatos[0].forma == "jornalista"


def test_substantivo_ista_ignora_nao_substantivos():
    assert gerar_substantivos_ista((_VERBO_CORRER,)) == ()


def test_substantivo_ista_nao_duplica_lema_repetido():
    candidatos = gerar_substantivos_ista((_NOME_ARTE, _NOME_ARTE))
    assert len(candidatos) == 1


def test_negativo_in_padrao():
    candidatos = gerar_adjetivos_negativos_in((_ADJ_FELIZ,))
    assert len(candidatos) == 1
    assert candidatos[0].forma == "infeliz"
    assert candidatos[0].classe == ClasseGramatical.ADJETIVO


def test_negativo_in_usa_im_antes_de_p():
    candidatos = gerar_adjetivos_negativos_in((_ADJ_POSSIVEL,))
    assert candidatos[0].forma == "impossível"


def test_negativo_in_usa_i_antes_de_l():
    candidatos = gerar_adjetivos_negativos_in((_ADJ_LEGAL,))
    assert candidatos[0].forma == "ilegal"


def test_negativo_in_usa_ir_antes_de_r():
    candidatos = gerar_adjetivos_negativos_in((_ADJ_RESPONSAVEL,))
    assert candidatos[0].forma == "irresponsável"


def test_negativo_in_usa_im_antes_de_m():
    # achado real: a assimilação bilabial cobre b/p/m, não só b/p --
    # "moral" sem esse guard virava "inmoral" (errado), correto é "imoral".
    candidatos = gerar_adjetivos_negativos_in((_ADJ_MORAL,))
    assert candidatos[0].forma == "imoral"


def test_negativo_in_ignora_nao_adjetivos():
    assert gerar_adjetivos_negativos_in((_NOME_GATO,)) == ()


def test_negativo_in_nao_duplica_lema_repetido():
    candidatos = gerar_adjetivos_negativos_in((_ADJ_FELIZ, _ADJ_FELIZ))
    assert len(candidatos) == 1


def test_validar_candidatos_sem_oraculo_devolve_taxa_none():
    candidatos = gerar_adverbios_mente((_ADJ_CLARO,))
    resultado = validar_candidatos(candidatos, caminho_oraculo=Path("/caminho/que/nao/existe.dic"))
    assert resultado.taxa is None
    assert resultado.confirmados == 0
    assert resultado.total == 1


def test_validar_candidatos_confirma_palavra_real_conhecida():
    # "perfeitamente" está listada como entrada própria no dicionário do
    # sistema (confirmado por auditoria manual) -- serve de exemplo
    # positivo real. Nota honesta: o oráculo só lê as entradas-raiz do
    # ficheiro .dic, sem aplicar as regras de afixo do .aff -- muitos
    # advérbios em -mente igualmente reais ("felizmente", "realmente")
    # não aparecem como linha própria e por isso não são confirmados por
    # este oráculo, mesmo sendo palavras corretas (limitação documentada
    # no módulo, não escondida). Se o oráculo não estiver disponível no
    # ambiente atual, o teste não falha por isso.
    resultado = validar_candidatos(gerar_adverbios_mente((_ADJ_PERFEITO,)))
    if resultado.taxa is None:
        return
    assert resultado.confirmados == 1
