#!/usr/bin/env python3
"""Avaliação pública pequena, incluindo erros conhecidos do Português."""
from __future__ import annotations

import json
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

from lingua_portuguesa import MotorPortugues
from lingua_portuguesa.corretor import Corretor
from lingua_portuguesa.lexico import Dicionario
from lingua_portuguesa.morfemas_afixais import segmentar_morfemas


def main() -> int:
    corretor = Corretor()
    erros = corretor.corrigir_texto("Ela nao sabia nda.")
    sugestoes = {palavra.casefold(): tuple(s.casefold() for s in candidatos) for palavra, candidatos in erros.sugestoes_ortografia}
    typos = {
        "nao_inclui_não": "não" in sugestoes.get("nao", ()),
        "nda_inclui_nada": "nada" in sugestoes.get("nda", ()),
        "não_reescreve_automaticamente": erros.corrigido == erros.original,
    }

    validas = ("casa", "bonita", "assunto", "comprimento", "sala", "medido", "menina", "feliz")
    texto_validas = " ".join(validas) + "."
    resultado_validas = corretor.corrigir_texto(texto_validas)
    falsos_positivos = tuple(palavra.casefold() for palavra, _ in resultado_validas.sugestoes_ortografia)

    dicionario = Dicionario.padrao()
    felizmente = segmentar_morfemas("felizmente", dicionario)
    incomum = segmentar_morfemas("incomum", dicionario)
    morfologia = {
        "felizmente": felizmente is not None and felizmente.radical == "feliz" and felizmente.sufixo is not None,
        "incomum": incomum is not None and incomum.radical == "comum" and incomum.prefixo is not None,
        "desumano_recusa_corte_falso": segmentar_morfemas("desumano", dicionario) is None,
        "resto_recusa_corte_falso": segmentar_morfemas("resto", dicionario) is None,
    }

    motor = MotorPortugues()
    caminho = motor.caminho_minimo_conceito_puro("interpretação")
    rastreabilidade = bool(caminho) and caminho[-1] == "interpretação"
    audit = motor.auditar_estrutura_portugues()

    resultado = {
        "deteccao_erros_alvo": typos,
        "morfologia": morfologia,
        "rastreabilidade_interpretacao": rastreabilidade,
        "auditoria": {
            "conceitos": audit.conceitos,
            "duplicacoes": len(audit.nomes_duplicados),
            "ciclos": len(audit.ciclos),
        },
        "palavras_validas_avaliadas": len(validas),
        "falsos_positivos": falsos_positivos,
        "taxa_falso_positivo_amostra": len(falsos_positivos) / len(validas),
    }
    base_ok = all(typos.values()) and all(morfologia.values()) and rastreabilidade
    resultado["estado"] = "PARCIAL_COM_FALSOS_POSITIVOS" if base_ok and falsos_positivos else ("APROVADO_NA_AMOSTRA" if base_ok else "DIVERGENCIA")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 0 if base_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

