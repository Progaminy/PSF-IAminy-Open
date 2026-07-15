"""PSF-IAminy — Verificação diagnóstica, solidez e busca de derivação, Etapas 381 a 400.
Roda com: python3 testes/test_busca_prova_finita.py
"""
import ast
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.fluxo import relatorio_fluxo
from nucleo.traducao import para_bool
from nucleo.logica_predicados_finita import (
    ATOMICA,
    DOMINIO_FINITO,
    ESTRUTURA_FINITA,
    PARA_TODO_QUANTIFICADO,
    SUBSTITUIR_LIVRE_FINITA,
    TERMO_CONST,
    TERMO_VAR,
)
from nucleo.metodos_finitos import PROP_VAR, PROP_E, PROP_OU, PROP_IMPLICA, CONSEQUENCIA_FINITA
from nucleo.teoria_modelos_prova_finita import (
    CONCLUSAO_DE,
    CONCLUSAO_FINAL_DA_DERIVACAO,
    DERIVACAO_VALIDA,
    PASSO_DERIVACAO,
    PREMISSAS_DE,
    SEQUENTE_FINITO,
)
from nucleo.busca_prova_finita import (
    BUSCADOR_CORRETO_FINITA,
    BUSCA_CONCORDA_COM_ORACULO_FINITA,
    BUSCA_DERIVACAO_FINITA,
    BUSCA_DERIVACAO_PROFUNDIDADE_LIMITADA_FINITA,
    COMPLETUDE_HORN_FINITA,
    COMPRIMENTO_DERIVACAO_FINITA,
    CONSISTENTE_POR_BUSCA_FINITA,
    DEMONSTRACAO_PONTA_A_PONTA_FINITA,
    DIAGNOSTICO_DERIVACAO_FINITA,
    ESTADO_BUSCA_FINITO,
    FECHAMENTO_ARCO_LOGICO_341_400,
    FECHAMENTO_BUSCA_DERIVACAO_FINITA,
    GERAR_TEORIAS_HORN_FINITAS,
    LIMITE_BUSCA_FORA_DO_FRAGMENTO_FINITA,
    LIMITE_RODADAS_BUSCA_FINITA,
    MENOR_DERIVACAO_FINITA,
    PASSO_DE_BUSCA_FINITO,
    PREMISSA_INDEPENDENTE_FINITA,
    PRIMEIRO_PASSO_INVALIDO_FINITO,
    RECONSTRUIR_TESTEMUNHA_FINITA,
    REGRA_SOLIDA_FINITA,
    SOLIDEZ_REGRA_PROPOSICIONAL_FINITA,
    SOLIDEZ_REGRA_QUANTIFICADOR_FINITA,
)

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def b(valor):
    return para_bool(valor)


def verificar_pureza():
    caminho = os.path.join(os.path.dirname(__file__), "..", "nucleo", "busca_prova_finita.py")
    with open(caminho, "r", encoding="utf-8") as f:
        arvore = ast.parse(f.read(), filename=caminho)
    proibidos = {"DIV", "MOD", "MDC", "MMC", "EH_PRIMO", "DECOMPOR"}
    modulos_proibidos = {"primos", "divisores"}
    for no in ast.walk(arvore):
        if isinstance(no, ast.BinOp) and isinstance(no.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            falhas.append("operador nativo proibido em busca_prova_finita.py")
        if isinstance(no, ast.Name) and no.id in proibidos:
            falhas.append(f"nome proibido {no.id}")
        if isinstance(no, ast.ImportFrom):
            modulo = (no.module or "").split(".")[-1]
            if modulo in modulos_proibidos:
                falhas.append(f"módulo proibido {no.module}")


def main():
    print("PSF-IAminy — Verificação diagnóstica, solidez e busca de derivação, Etapas 381 a 400")
    verificar_pureza()

    r = relatorio_fluxo()
    verificar("motor contabiliza etapa máxima >= 400", r["maior_etapa"] >= 400, True)
    verificar("motor sem lacunas até a etapa máxima", r["faltando_ate_maior"], [])

    p, q, rr, s = PROP_VAR("p"), PROP_VAR("q"), PROP_VAR("r"), PROP_VAR("s")
    gamma3 = (p, PROP_IMPLICA(p, q), PROP_IMPLICA(q, rr))

    # --- Etapa 381: verificador com diagnóstico passo-a-passo ---
    passos_validos = (
        PASSO_DERIVACAO("premissa", (), SEQUENTE_FINITO(gamma3, p)),
        PASSO_DERIVACAO("premissa", (), SEQUENTE_FINITO(gamma3, PROP_IMPLICA(p, q))),
        PASSO_DERIVACAO("modus_ponens", (0, 1), SEQUENTE_FINITO(gamma3, q)),
    )
    diagnostico = DIAGNOSTICO_DERIVACAO_FINITA(passos_validos)
    verificar("diagnóstico de derivação válida marca os 3 passos como válidos", tuple(d[2] for d in diagnostico), (True, True, True))
    verificar("nenhum passo inválido numa derivação correta", PRIMEIRO_PASSO_INVALIDO_FINITO(passos_validos), None)

    passos_quebrados = passos_validos[:2] + (
        PASSO_DERIVACAO("modus_ponens", (1, 0), SEQUENTE_FINITO(gamma3, q)),
    )
    indice, nome_regra = PRIMEIRO_PASSO_INVALIDO_FINITO(passos_quebrados)
    verificar("diagnóstico aponta o passo 2 (modus ponens com entradas trocadas) como inválido", (indice, nome_regra), (2, "modus_ponens"))

    # --- Etapa 382: solidez de regra proposicional (exaustiva sobre valorações) ---
    seq_p = SEQUENTE_FINITO(gamma3, p)
    seq_pq = SEQUENTE_FINITO(gamma3, PROP_IMPLICA(p, q))
    seq_q = SEQUENTE_FINITO(gamma3, q)
    verificar("modus ponens é sólido (premissas satisfeitas implicam conclusão satisfeita, em toda valoração)",
              b(SOLIDEZ_REGRA_PROPOSICIONAL_FINITA("modus_ponens", (seq_p, seq_pq), seq_q)), True)

    seq_q_errado = SEQUENTE_FINITO(gamma3, PROP_IMPLICA(q, rr))
    verificar("um passo sintaticamente inválido é automaticamente considerado não-sólido",
              b(SOLIDEZ_REGRA_PROPOSICIONAL_FINITA("modus_ponens", (seq_p, seq_pq), seq_q_errado)), False)

    seq_e = SEQUENTE_FINITO(gamma3, PROP_E(p, q))
    verificar("∧-introdução é sólida", b(SOLIDEZ_REGRA_PROPOSICIONAL_FINITA("e_intro", (seq_p, seq_q), seq_e)), True)

    # --- Etapa 383: solidez de regra de quantificador (amostra de estruturas) ---
    x = TERMO_VAR("x")
    Dp = DOMINIO_FINITO(0, 1, 2)
    Ep = ESTRUTURA_FINITA(Dp, {"P": ((0,), (1,), (2,))}, {})
    formula_px = ATOMICA("P", x)
    universal = PARA_TODO_QUANTIFICADO("x", formula_px)
    seq_univ = SEQUENTE_FINITO((universal,), universal)
    seq_inst = SEQUENTE_FINITO((universal,), SUBSTITUIR_LIVRE_FINITA(formula_px, "x", TERMO_CONST(0)))
    verificar("∀-eliminação é sólida sobre a estrutura Ep (todo elemento satisfaz P)",
              b(SOLIDEZ_REGRA_QUANTIFICADOR_FINITA("para_todo_elim", (seq_univ,), seq_inst, TERMO_CONST(0), (Ep,))), True)

    # --- Etapa 384: validação cruzada por dispatch ---
    verificar("REGRA_SOLIDA_FINITA despacha modus_ponens para a checagem proposicional",
              b(REGRA_SOLIDA_FINITA("modus_ponens", (seq_p, seq_pq), seq_q)), True)
    verificar("REGRA_SOLIDA_FINITA despacha para_todo_elim para a checagem de quantificador",
              b(REGRA_SOLIDA_FINITA("para_todo_elim", (seq_univ,), seq_inst, TERMO_CONST(0), (Ep,))), True)

    # --- Etapas 385-387: estado de busca, passo de busca, poda/término ---
    estado0 = ESTADO_BUSCA_FINITO(gamma3, rr)
    verificar("estado inicial já contém as premissas como provadas", p in estado0["provado"] and PROP_IMPLICA(p, q) in estado0["provado"], True)
    verificar("estado inicial ainda não prova a meta", rr in estado0["provado"], False)
    estado1, mudou1 = PASSO_DE_BUSCA_FINITO(estado0)
    verificar("uma rodada de busca avança o estado (algo novo provado)", mudou1, True)
    limite = LIMITE_RODADAS_BUSCA_FINITA(estado0)
    verificar("o limite de rodadas é o tamanho do universo finito de subfórmulas", limite, len(estado0["universo"]))

    # --- Etapa 388: busca de derivação por enumeração finita ---
    encontrada = BUSCA_DERIVACAO_FINITA(gamma3, rr)
    verificar("a busca encontra sozinha uma derivação de r a partir de {p,p→q,q→r}", encontrada is not None, True)
    verificar("a derivação encontrada é validada pelo verificador independente (etapa 379)", b(DERIVACAO_VALIDA(encontrada)), True)
    verificar("a conclusão final da derivação encontrada é r", CONCLUSAO_FINAL_DA_DERIVACAO(encontrada), rr)

    sem_prova = BUSCA_DERIVACAO_FINITA(gamma3, PROP_VAR("totalmente_alheio"))
    verificar("a busca não inventa uma derivação para uma fórmula fora do alcance", sem_prova, None)

    # --- Etapa 389: testemunha construída e re-verificável ---
    testemunha = RECONSTRUIR_TESTEMUNHA_FINITA(encontrada, q)
    verificar("a testemunha para um passo intermediário (q) também é uma derivação válida", b(DERIVACAO_VALIDA(testemunha)), True)
    verificar("a testemunha intermediária conclui exatamente q", CONCLUSAO_FINAL_DA_DERIVACAO(testemunha), q)

    # --- Etapa 390 ---
    verificar("fechamento da busca de derivação (385-390)", b(FECHAMENTO_BUSCA_DERIVACAO_FINITA()), True)

    # --- Etapas 391-392: completude relativa ao fragmento de Horn (EXAUSTIVA) ---
    catalogo = (p, q, PROP_IMPLICA(p, q), PROP_IMPLICA(q, rr), PROP_IMPLICA(PROP_E(p, q), rr))
    total_teorias = sum(1 for _ in GERAR_TEORIAS_HORN_FINITAS(catalogo))
    verificar("catálogo de 5 cláusulas gera 32 teorias possíveis (2^5, exaustivo)", total_teorias, 32)
    concordou, total = COMPLETUDE_HORN_FINITA(catalogo, (p, q, rr))
    verificar("busca concorda com o oráculo semântico em TODAS as 96 combinações (32 teorias x 3 metas)", (concordou, total), (96, 96))

    # --- Etapa 393: limite honesto — contraexemplo fora do fragmento ---
    gamma_disj = (PROP_OU(p, q), PROP_IMPLICA(p, rr), PROP_IMPLICA(q, rr))
    verificar("r é consequência semântica de {p∨q, p→r, q→r} (prova por casos)", b(CONSEQUENCIA_FINITA(gamma_disj, rr)), True)
    verificar("mas a busca (sem ∨-eliminação) corretamente NÃO encontra essa derivação",
              b(LIMITE_BUSCA_FORA_DO_FRAGMENTO_FINITA(gamma_disj, rr)), True)

    # --- Etapa 394: consistência por busca ---
    gamma_transito = (PROP_VAR("verde"), PROP_IMPLICA(PROP_VAR("verde"), PROP_VAR("vermelho")))
    verificar("teoria que deriva 'verde' e 'vermelho' simultaneamente é sinalizada inconsistente (par antagônico dado)",
              b(CONSISTENTE_POR_BUSCA_FINITA(gamma_transito, ((PROP_VAR("verde"), PROP_VAR("vermelho")),))), False)
    verificar("teoria {p,p→q,q→r} é consistente para o par (q, totalmente_alheio) — alheio nunca é provado",
              b(CONSISTENTE_POR_BUSCA_FINITA(gamma3, ((q, PROP_VAR("totalmente_alheio")),))), True)

    # --- Etapa 395: independência de premissa ---
    gamma_com_irrelevante = (p, PROP_IMPLICA(p, q), PROP_IMPLICA(q, rr), PROP_VAR("irrelevante"))
    verificar("remover p→q (índice 1) derruba a consequência de r — premissa independente/necessária",
              b(PREMISSA_INDEPENDENTE_FINITA(gamma_com_irrelevante, rr, 1)), True)
    verificar("remover 'irrelevante' (índice 3) não derruba a consequência de r — não é independente/necessária",
              b(PREMISSA_INDEPENDENTE_FINITA(gamma_com_irrelevante, rr, 3)), False)

    # --- Etapa 396: comprimento e derivação mínima ---
    derivacao_padded = encontrada + (PASSO_DERIVACAO("e_intro", (0, 0), SEQUENTE_FINITO(gamma3, PROP_E(p, p))),)
    verificar("a derivação com um passo extra redundante ainda é válida", b(DERIVACAO_VALIDA(derivacao_padded)), True)
    verificar("a derivação extra é estritamente mais longa", COMPRIMENTO_DERIVACAO_FINITA(derivacao_padded) > COMPRIMENTO_DERIVACAO_FINITA(encontrada), True)
    verificar("a derivação mínima entre as duas é a encontrada pela busca (sem o passo redundante)",
              MENOR_DERIVACAO_FINITA(encontrada, derivacao_padded), encontrada)

    # --- Etapa 397: comparação de estratégias (profundidade limitada vs. até ponto fixo) ---
    gamma_cadeia = (p, PROP_IMPLICA(p, q), PROP_IMPLICA(q, rr), PROP_IMPLICA(rr, s))
    verificar("com zero rodadas, nada além das premissas é provado — s não é alcançado",
              BUSCA_DERIVACAO_PROFUNDIDADE_LIMITADA_FINITA(gamma_cadeia, s, 0), None)
    limite_total = LIMITE_RODADAS_BUSCA_FINITA(ESTADO_BUSCA_FINITO(gamma_cadeia, s))
    encontrada_cadeia = BUSCA_DERIVACAO_PROFUNDIDADE_LIMITADA_FINITA(gamma_cadeia, s, limite_total)
    verificar("com rodadas suficientes (limite do universo finito), s é alcançado", encontrada_cadeia is not None, True)
    verificar("a busca com profundidade suficiente concorda com a busca até ponto fixo", encontrada_cadeia is not None and BUSCA_DERIVACAO_FINITA(gamma_cadeia, s) is not None, True)

    # --- Etapa 398: correção do buscador ---
    verificar("o buscador é correto: tudo que devolve passa por DERIVACAO_VALIDA", b(BUSCADOR_CORRETO_FINITA(gamma3, rr)), True)
    verificar("o buscador é correto mesmo quando não encontra nada (vacuamente)", b(BUSCADOR_CORRETO_FINITA(gamma3, PROP_VAR("alheio"))), True)

    # --- Etapa 399: aplicação de ponta a ponta ---
    demonstracao = DEMONSTRACAO_PONTA_A_PONTA_FINITA(gamma_cadeia, s)
    verificar("demonstração de ponta a ponta encontra s a partir de {p,p→q,q→r,r→s} sem passos manuais", demonstracao is not None, True)
    verificar("a demonstração de ponta a ponta é válida e conclui s", b(DERIVACAO_VALIDA(demonstracao)) and CONCLUSAO_FINAL_DA_DERIVACAO(demonstracao) == s, True)

    # --- Etapa 400 ---
    verificar("fechamento do arco lógico 341-400", b(FECHAMENTO_ARCO_LOGICO_341_400()), True)

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
