import re

import pytest

from ensino.exercicio_real import (
    GERADORES_POR_CONCEITO,
    ExercicioReal,
    gerar_exercicio_real,
    tem_gerador_real,
    verificar_resposta_real,
)

CONCEITOS = tuple(GERADORES_POR_CONCEITO) + ("mdc mmc por fatores",)


@pytest.mark.parametrize("conceito", CONCEITOS)
def test_tem_gerador_real(conceito):
    assert tem_gerador_real(conceito)


def test_conceito_sem_funcao_real_nao_tem_gerador():
    assert not tem_gerador_real("semantica denotacional programas finitos")


@pytest.mark.parametrize("conceito", CONCEITOS)
@pytest.mark.parametrize("semente", range(30))
def test_exercicio_real_gera_e_confere_resposta_certa(conceito, semente):
    exercicio = gerar_exercicio_real(conceito, semente=semente)
    assert isinstance(exercicio, ExercicioReal)
    assert exercicio.enunciado
    assert exercicio.resposta_certa
    # a resposta certa, formatada exatamente como o exercício pede, tem que
    # ser aceita como correta -- a verificação não pode rejeitar a própria
    # resposta que ela mesma calculou.
    resultado = verificar_resposta_real(exercicio, exercicio.resposta_certa)
    assert resultado.correto is True


def test_enunciado_nunca_usa_notacao_de_chamada_de_funcao():
    """Regra 2 do autor: nunca 'SOMA(4)(7)' -- só notação de papel/prosa."""
    padrao_chamada = re.compile(r"\b[A-Z]{2,}\([^)]*\)\([^)]*\)")
    for conceito in CONCEITOS:
        for semente in range(10):
            exercicio = gerar_exercicio_real(conceito, semente=semente)
            assert not padrao_chamada.search(exercicio.enunciado), exercicio.enunciado


def test_enunciado_nunca_cita_dependencia_ou_grafo():
    """Regra 1 do autor: pergunta principal é aplicar a construção, não recall de grafo."""
    proibidas = ("depende", "dependência", "dependencia")
    for conceito in CONCEITOS:
        for semente in range(10):
            exercicio = gerar_exercicio_real(conceito, semente=semente)
            texto = exercicio.enunciado.casefold()
            assert not any(p in texto for p in proibidas), exercicio.enunciado


def test_adicao_resultado_oculto_no_enunciado():
    exercicio = gerar_exercicio_real("adicao", semente=1)
    assert "?" in exercicio.enunciado
    assert exercicio.resposta_certa not in exercicio.enunciado.split("\n")[-1]


def test_resposta_errada_numero_e_rejeitada():
    exercicio = gerar_exercicio_real("adicao", semente=2)
    errado = str(int(exercicio.resposta_certa) + 1)
    resultado = verificar_resposta_real(exercicio, errado)
    assert resultado.correto is False


def test_divisao_aceita_variacoes_de_formato_quociente_resto():
    exercicio = gerar_exercicio_real("resto e divisao euclidiana", semente=3)
    q, r = exercicio.resposta_certa.split(" resto ")
    for formato in (f"{q} resto {r}", f"{q},{r}", f"quociente {q} resto {r}"):
        assert verificar_resposta_real(exercicio, formato).correto is True


def test_divisao_resto_errado_e_rejeitado():
    exercicio = gerar_exercicio_real("resto e divisao euclidiana", semente=3)
    q, r = exercicio.resposta_certa.split(" resto ")
    resposta_errada = f"{q} resto {int(r) + 1}"
    assert verificar_resposta_real(exercicio, resposta_errada).correto is False


def test_comparador_aceita_sinal_e_palavra():
    exercicio = gerar_exercicio_real("ordem total", semente=4)
    if exercicio.resposta_certa == "<":
        assert verificar_resposta_real(exercicio, "menor").correto is True
    elif exercicio.resposta_certa == ">":
        assert verificar_resposta_real(exercicio, "maior").correto is True
    else:
        assert verificar_resposta_real(exercicio, "igual").correto is True


def test_sim_nao_aceita_variacoes_comuns():
    exercicio = gerar_exercicio_real("divisibilidade pura", semente=5)
    variacoes_sim = ("sim", "Sim", "S", "verdadeiro")
    variacoes_nao = ("nao", "não", "N", "falso")
    variacoes = variacoes_sim if exercicio.resposta_certa == "sim" else variacoes_nao
    for variacao in variacoes:
        assert verificar_resposta_real(exercicio, variacao).correto is True


def test_par_impar_aceita_acentuacao_e_sem_acento():
    exercicio = gerar_exercicio_real("paridade", semente=6)
    if exercicio.resposta_certa == "par":
        assert verificar_resposta_real(exercicio, "PAR").correto is True
    else:
        assert verificar_resposta_real(exercicio, "impar").correto is True
        assert verificar_resposta_real(exercicio, "ímpar").correto is True


def test_gerar_exercicio_real_e_deterministico_por_semente():
    a = gerar_exercicio_real("multiplicacao", semente=42)
    b = gerar_exercicio_real("multiplicacao", semente=42)
    assert a == b


def test_mdc_mmc_alterna_entre_os_dois_geradores():
    enunciados = [gerar_exercicio_real("mdc mmc por fatores", semente=s).enunciado for s in range(20)]
    tem_mdc = any("máximo divisor comum" in e for e in enunciados)
    tem_mmc = any("mínimo múltiplo comum" in e for e in enunciados)
    assert tem_mdc and tem_mmc
