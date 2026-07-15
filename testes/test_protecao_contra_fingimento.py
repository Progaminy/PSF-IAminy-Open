"""Testes de proteção contra fingimento e contra dependência externa como fundamento.

O README lista há muito tempo, sem nunca ter sido fechado:
    criar testes explícitos contra fingimento
    criar testes explícitos contra dependência externa como fundamento

Os detectores para as duas coisas já existiam -- `motor/formulas.py` (operador
nativo suspeito, import de math/numpy/sympy/scipy/statistics/fractions/decimal
fora de módulo declarado), `motor/pureza.py` (import proibido por módulo) e
`matematica/resolucao_pontes.py` (dependência que não resolve a nenhum
conceito real). O que faltava não era o detector -- era prendê-lo ao estado
REAL do projeto como asserção que quebra a bateria, em vez de só imprimir um
relatório que ninguém é obrigado a ler. Este ficheiro não inventa nenhuma
lógica de deteção nova: só chama os auditores já existentes e trava o estado
atual (limpo) como piso permanente.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from matematica import MotorMatematica
from motor.formulas import resumo_auditoria_formulas
from motor.pureza import auditar_tudo
from motor.rastreabilidade import (
    candidatos_a_pureza_nao_registados,
    modulos_orfaos,
    referencias_quebradas,
)


def test_nenhum_modulo_nucleo_com_operador_ou_import_suspeito_nao_justificado():
    """Nenhum módulo `nucleo/*.py` pode ter `/,//,%,**` ou `math/numpy/sympy/...`
    fora dos dois grupos já explicitamente declarados e justificados
    (`MODULOS_VALIDACAO_OU_LEGADO`, `MODULOS_TECNICOS_NAO_FUNDAMENTO`).
    Um módulo novo com um atalho não registado deve fazer este teste falhar,
    não passar silenciosamente.
    """
    resumo = resumo_auditoria_formulas()
    assert resumo["suspeitos"] == {}, (
        f"módulo(s) com fórmula pronta/operador forte sem justificação registada: "
        f"{list(resumo['suspeitos'])}"
    )


def test_nenhuma_dependencia_matematica_fica_sem_resolver_ou_vaga():
    """Toda dependência declarada em `conhecimento/ETAPA_*.md` deve resolver a um
    conceito, alias, raiz, referência de módulo ou grupo real -- nunca ficar
    como frase vaga tipo "tudo o que nasceu nas etapas 1-X" (contexto não
    atômico) nem como nome que não bate com nada (não resolvida/agregada).
    """
    profunda = MotorMatematica().auditar_pontes()["resolucao_profunda"]
    assert profunda["nao_resolvidas"] == ()
    assert profunda["agregadas_ou_imprecisas"] == ()
    assert profunda["contexto_nao_atomico_ignorado"] == ()
    assert profunda["sem_lacunas"] is True


def test_nenhum_conceito_matematico_fica_isolado_sem_ponte():
    auditoria = MotorMatematica().auditar_pontes()
    assert auditoria["isolados"] == ()


def test_pureza_de_importacao_continua_limpa_no_projeto_real():
    """`motor/pureza.py` já audita imports reais contra dependências proibidas
    por módulo -- isto só prende o resultado real como piso: qualquer módulo
    puro que passe a importar algo proibido quebra a bateria."""
    violacoes = auditar_tudo()
    sujos = {modulo: v for modulo, v in violacoes.items() if v}
    assert sujos == {}


def test_nenhuma_referencia_de_documentacao_aponta_para_ficheiro_inexistente():
    assert referencias_quebradas() == {}


def test_nenhum_modulo_de_nucleo_fica_orfao_sem_documentacao():
    assert modulos_orfaos() == []


def test_nenhum_modulo_com_pureza_declarada_fica_fora_do_registo_de_regras():
    assert candidatos_a_pureza_nao_registados() == []
