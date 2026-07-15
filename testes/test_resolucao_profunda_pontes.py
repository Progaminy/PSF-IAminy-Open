from matematica import MotorMatematica
from matematica.resolucao_pontes import resolver_dependencia


def test_raizes_aliases_e_conceitos_sao_distinguidos():
    # "igualdade" era uma raiz "implícita" até este achado: agora tem
    # documento próprio (marcador 1074, "igualdade e ordem"), então virou
    # ALIAS, não RAIZ -- "distincao" continua genuinamente sem ETAPA
    # própria, serve de exemplo de raiz de verdade.
    nomes = {"divisibilidade pura", "mdc puro"}
    assert resolver_dependencia("distincao", nomes) == ("RAIZ", "distincao")
    assert resolver_dependencia("divisibilidade", nomes) == ("ALIAS", "divisibilidade pura")
    assert resolver_dependencia("mdc puro", nomes) == ("CONCEITO", "mdc puro")


def test_auditoria_profunda_nao_confunde_campo_preenchido_com_ponte_fechada():
    profunda = MotorMatematica().auditar_pontes()["resolucao_profunda"]
    assert profunda["dependencias"] >= profunda["pontes_fechadas"]
    assert profunda["resolvidas"] == profunda["pontes_fechadas"]
