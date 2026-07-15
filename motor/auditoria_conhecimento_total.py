"""Auditoria conjunta dos repositórios de conhecimento e material auxiliar."""
from __future__ import annotations

from lingua_portuguesa import MotorPortugues
from matematica import MotorMatematica
from nucleo.calculo_integral_avancado import auditar_pontes_calculo
from nucleo.conceitos_avancados_puros import (
    CONCEITOS_CONSTRUIDOS_ETAPA_38,
    RESPOSTAS_AVANCADAS_ETAPA_38,
)


def _auditar_avancados() -> dict[str, object]:
    conceitos = {c.chave: c for c in CONCEITOS_CONSTRUIDOS_ETAPA_38}
    conceitos_sem_origem = tuple(sorted(c.chave for c in conceitos.values() if not c.depende_de))
    respostas_sem_ponte = tuple(sorted(r.pergunta for r in RESPOSTAS_AVANCADAS_ETAPA_38 if r.conceito not in conceitos))
    return {
        "conceitos": len(conceitos),
        "respostas": len(RESPOSTAS_AVANCADAS_ETAPA_38),
        "conceitos_sem_origem": conceitos_sem_origem,
        "respostas_sem_ponte": respostas_sem_ponte,
        "sem_isolamentos": not conceitos_sem_origem and not respostas_sem_ponte,
    }


def auditar_conhecimento_total() -> dict[str, object]:
    matematica = MotorMatematica().auditar_pontes()
    portugues = MotorPortugues().auditar_estrutura_portugues()
    avancados = _auditar_avancados()
    calculo = auditar_pontes_calculo()
    isolamentos = []
    if matematica["isolados"]:
        isolamentos.append(("matematica_documental", matematica["isolados"]))
    if portugues.nomes_duplicados or portugues.dependencias_ausentes or portugues.dependencias_futuras or portugues.ciclos:
        isolamentos.append(("portugues", portugues.dependencias_ausentes + portugues.dependencias_futuras))
    if not avancados["sem_isolamentos"]:
        isolamentos.append(("conceitos_avancados", avancados))
    if not calculo["sem_isolamentos"]:
        isolamentos.append(("calculo", calculo))
    return {
        "matematica_documental": matematica,
        "portugues": {
            "conceitos": portugues.conceitos,
            "relacoes": portugues.relacoes_diretas,
            "sem_isolamentos": not (
                portugues.nomes_duplicados or portugues.dependencias_ausentes
                or portugues.dependencias_futuras or portugues.ciclos
            ),
        },
        "conceitos_avancados": avancados,
        "calculo": calculo,
        "materiais_nao_fundacionais": {
            "problemas_abertos": "guardados para depois da maturidade; não são conhecimento resolvido",
            "problemas_historicos": "referência histórica; estratégia resumida não equivale a ponte de prova PSF",
            "curiosidades_e_respostas": "apresentação/consulta; não são fundamento matemático",
            "hipoteses": "ideias guardadas; não são conhecimento provado",
        },
        "isolamentos_utilizaveis": tuple(isolamentos),
        "aprovado": not isolamentos,
    }
