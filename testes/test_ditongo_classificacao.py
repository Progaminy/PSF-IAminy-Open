"""Fecha o gap pontual da auditoria de currículo de Português: `ditongo`
existia como conceito único, sem a subclassificação crescente (semivogal
antes da vogal nuclear, ex. "quase") vs. decrescente (vogal nuclear antes da
semivogal, ex. "pai") -- ver
`conhecimento/AUDITORIA_CURRICULO_PORTUGUES_1000_AULAS.md:33-34`.
"""
from lingua_portuguesa import MotorPortugues


def test_ditongo_crescente_e_decrescente_existem_como_conceitos():
    motor = MotorPortugues()
    assert "semivogal" in motor.definir_conceito_puro("ditongo crescente").casefold()
    assert "semivogal" in motor.definir_conceito_puro("ditongo decrescente").casefold()
    crescente = motor.dependencias_conceito_puro("ditongo crescente")
    decrescente = motor.dependencias_conceito_puro("ditongo decrescente")
    assert {"ditongo", "semivogal"} <= set(crescente)
    assert {"ditongo", "semivogal"} <= set(decrescente)


def test_exemplos_minimos_reais_distinguem_os_dois():
    from lingua_portuguesa.conhecimento_puro import CONCEITOS_PORTUGUES_PURO

    por_nome = {c.nome: c for c in CONCEITOS_PORTUGUES_PURO}
    crescente = por_nome["ditongo crescente"]
    decrescente = por_nome["ditongo decrescente"]
    assert "quase" in crescente.exemplos_minimos
    assert "pai" in decrescente.exemplos_minimos
    assert crescente.nao_confundir_com and decrescente.nao_confundir_com


def test_estrutura_do_portugues_continua_sem_lacuna_apos_a_adicao():
    motor = MotorPortugues()
    auditoria = motor.auditar_estrutura_portugues()
    assert auditoria.conceitos == 1141
    assert len(auditoria.nomes_duplicados) == 0
    assert len(auditoria.dependencias_ausentes) == 0
