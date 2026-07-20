import pytest

from lingua_portuguesa.lexico import Dicionario
from lingua_portuguesa.lexico_verbos_regulares import (
    formas_do_paradigma_regular,
    formas_verbais_regulares_locais,
    lemas_regulares_curados,
)


def test_inventario_local_e_curado_sem_inflar_com_lista_pronta():
    lemas = lemas_regulares_curados()
    assert lemas == tuple(sorted(set(lemas)))
    assert len(lemas) == 1_322
    assert all(lema.endswith("ar") for lema in lemas)
    assert all(len(formas_do_paradigma_regular(lema)) == 53 for lema in lemas)
    assert len(formas_verbais_regulares_locais()) == 70_066


def test_paradigma_ar_cobre_seis_pessoas_tempos_e_variantes_reais():
    formas = set(formas_do_paradigma_regular("falar"))
    assert len(formas) == 53
    assert {
        "falo", "falais", "falaste", "falámos", "faláveis", "faláramos",
        "faláreis", "falarei", "falaríeis", "faleis", "falássemos",
        "falardes", "falai", "falando", "falado", "faladas",
    } <= formas


def test_alternancias_ortograficas_tambem_valem_no_paradigma_completo():
    explicar = set(formas_do_paradigma_regular("explicar"))
    chegar = set(formas_do_paradigma_regular("chegar"))
    comecar = set(formas_do_paradigma_regular("começar"))
    assert {"expliquei", "expliqueis"} <= explicar
    assert {"cheguei", "chegueis"} <= chegar
    assert {"comecei", "comeceis"} <= comecar
    assert not {"explicei", "chegei", "começei"} & (explicar | chegar | comecar)


def test_padrao_so_materializa_forma_sem_inventar_leitura_semantica():
    dicionario = Dicionario.padrao()
    assert "falásseis" in dicionario
    assert dicionario.origem_ortografica("falásseis") == (
        "paradigma_verbal_regular_curado_local:falar"
    )
    assert dicionario.buscar("falásseis") == ()


@pytest.mark.parametrize(
    "lema",
    (
        "dar", "estar", "ser", "ter", "ir", "vir", "ouvir", "pedir",
        "dormir", "proibir", "criar", "construir", "distinguir", "saudar",
        "adequar", "enraizar",
    ),
)
def test_gerador_rejeita_classes_fora_do_corte_mecanico(lema):
    with pytest.raises(ValueError):
        formas_do_paradigma_regular(lema)


def test_formas_falsas_antigas_nao_sobrevivem_no_dicionario():
    dicionario = Dicionario.padrao()
    falsas_por_lema = {
        "construir": ("construe", "construimos"),
        "reconstruir": ("reconstrue", "reconstruimos"),
        "referir": ("refero", "refera"),
        "inferir": ("infero", "infera"),
        "distinguir": ("distinguo", "distingua"),
        "reger": ("rego", "rega"),
        "exigir": ("exigo", "exiga"),
        "fingir": ("fingo", "finga"),
        "corrigir": ("corrigo", "corriga"),
    }
    for lema, formas in falsas_por_lema.items():
        for forma in formas:
            assert not any(entrada.lema == lema for entrada in dicionario.buscar(forma))
    corretas_por_lema = {
        "distinguir": ("distingo", "distinga"),
        "reger": ("rejo", "reja"),
        "exigir": ("exijo", "exija"),
        "fingir": ("finjo", "finja"),
        "corrigir": ("corrijo", "corrija"),
    }
    for lema, formas in corretas_por_lema.items():
        for forma in formas:
            assert any(entrada.lema == lema for entrada in dicionario.buscar(forma))


def test_meta_real_de_dez_por_cento_usa_so_formas_atomicas():
    dicionario = Dicionario.padrao()
    assert dicionario.total_formas_atomicas() >= 60_000
    assert dicionario.cobertura_atomica() >= 10.0
