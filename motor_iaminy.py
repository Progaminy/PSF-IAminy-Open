#!/usr/bin/env python3
"""Comando do motor meta PSF-IAminy.

Uso principal:
  python3 motor_iaminy.py              # relatório + bateria padrão curta e segura
  python3 motor_iaminy.py --rapido     # só auditorias, sem testes matemáticos
  python3 motor_iaminy.py --completo   # todos os testes, com limites de tempo

O padrão foi corrigido: o motor não deve passar do tempo por tentar correr
sempre a bateria pesada do núcleo unário. A bateria completa continua
existindo, mas agora é uma decisão explícita.
"""
from __future__ import annotations

import argparse
import sys

from motor.fluxo import relatorio_fluxo
from motor.pureza import auditar_tudo
from motor.execucao import executar_testes, resumo_execucao, testes_do_perfil
from motor.rastreabilidade import (
    candidatos_a_pureza_nao_registados,
    imports_python_quebrados,
    modulos_orfaos,
    referencias_quebradas,
)
from motor.coerencia import (
    arquivos_que_violam_regra_versao_unica,
    divergencias_lexico_no_readme,
    divergencias_readme_vs_auditoria_portugues,
    itens_do_plano_fora_de_ordem,
    modulos_da_interface_falham_ao_importar,
    nomes_de_teste_declarados_sem_ficheiro_real,
)
from motor.ordem import violacoes_de_ordem, modulos_fora_de_cobertura
from motor.desempenho import comparar_e_atualizar
from motor.formulas import resumo_auditoria_formulas
from matematica import MotorMatematica
from motor.auditoria_conhecimento_total import auditar_conhecimento_total


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Motor de fluxo natural do PSF-IAminy")
    p.add_argument("--rapido", action="store_true", help="não executa testes; só auditorias estruturais")
    p.add_argument("--completo", action="store_true", help="executa todos os testes com limite de tempo")
    p.add_argument("--timeout-teste", type=float, default=None, help="segundos máximos por ficheiro de teste")
    p.add_argument("--orcamento", type=float, default=None, help="segundos máximos para a bateria de testes")
    p.add_argument("--listar-testes", action="store_true", help="mostra que testes cada perfil executa")
    p.add_argument("--exigir-formulas-limpas", action="store_true", help="falha se houver fórmula pronta suspeita fora de legado/validação")
    return p


def imprimir_auditorias() -> bool:
    """Imprime auditorias estruturais. Devolve True se tudo estiver limpo."""
    tudo_limpo = True
    r = relatorio_fluxo()
    prox_num, prox_nome = r["proxima"]
    print("PSF-IAminy — Linha Única de Conhecimento")
    print("ETAPA/camada: apenas marcador histórico ou tema de consulta; não autoridade de verdade.")
    print(f"Marcador histórico máximo contabilizado: {r['maior_etapa']}")
    print(f"Total contabilizado: {r['total_contabilizado']}")
    if r["faltando_ate_maior"]:
        print("Lacunas:", r["faltando_ate_maior"])
        tudo_limpo = False
    else:
        print("Lacunas: nenhuma até a etapa máxima")
    print(f"Próximo marcador documental compatível: {prox_num} — {prox_nome}")

    auditoria_matematica = MotorMatematica().auditar()
    auditoria_pontes = MotorMatematica().auditar_pontes()
    print()
    print("--- MotorMatematica: conhecimento, referências e linha única ---")
    print(f"Conceitos matemáticos materializados: {auditoria_matematica.conceitos}")
    print(f"Nomes duplicados: {len(auditoria_matematica.nomes_duplicados)}")
    print(f"Referências de implementação ausentes: {len(auditoria_matematica.referencias_de_implementacao_ausentes)}")
    print(f"Referências de teste ausentes: {len(auditoria_matematica.referencias_de_teste_ausentes)}")
    if not auditoria_matematica.linha_unica or auditoria_matematica.referencias_de_implementacao_ausentes or auditoria_matematica.referencias_de_teste_ausentes:
        tudo_limpo = False
    print(f"Conceitos isolados sem ponte: {len(auditoria_pontes['isolados'])}")
    if auditoria_pontes["isolados"]:
        print("BLOQUEADOS sem ponte:", auditoria_pontes["isolados"])
        tudo_limpo = False
    profunda = auditoria_pontes["resolucao_profunda"]
    print(
        f"Dependências profundamente resolvidas: {profunda['resolvidas']}/{profunda['dependencias']}; "
        f"não resolvidas: {len(profunda['nao_resolvidas'])}; "
        f"agregadas/imprecisas: {len(profunda['agregadas_ou_imprecisas'])}; "
        f"futuras: {len(profunda['referencias_futuras'])}."
    )

    total = auditar_conhecimento_total()
    print("Repositórios utilizáveis isolados:", len(total["isolamentos_utilizaveis"]))
    print(
        "Pontes internas: Português",
        total["portugues"]["conceitos"],
        "conceitos; avançados",
        total["conceitos_avancados"]["respostas"],
        "respostas; Cálculo",
        total["calculo"]["respostas"],
        "respostas.",
    )
    if not total["aprovado"]:
        print("BLOQUEIOS:", total["isolamentos_utilizaveis"])
        tudo_limpo = False

    print()
    print("--- Auditoria de pureza (imports reais vs. dependências proibidas) ---")
    violacoes = auditar_tudo()
    sujos = {m: v for m, v in violacoes.items() if v}
    if sujos:
        print(f"VIOLAÇÕES em {len(sujos)}/{len(violacoes)} módulo(s) auditado(s):")
        for modulo, lista in sujos.items():
            print(f"  {modulo}: {lista}")
        tudo_limpo = False
    else:
        print(f"Limpo: {len(violacoes)}/{len(violacoes)} módulos auditados, 0 violações.")

    print()
    print("--- Rastreabilidade (documentação aponta para ficheiros reais?) ---")
    quebradas = referencias_quebradas()
    if quebradas:
        print(f"Referências quebradas em {len(quebradas)} etapa(s):", quebradas)
        tudo_limpo = False
    else:
        print("Todas as referências de todas as ETAPA_XX.md apontam para ficheiros reais.")
    orfaos = modulos_orfaos()
    if orfaos:
        print(f"Pendência de rastreabilidade — módulos sem referência documental: {orfaos}")
        tudo_limpo = False
    else:
        print("Nenhum módulo órfão — todo nucleo/*.py está documentado nalgum lugar.")
    candidatos = candidatos_a_pureza_nao_registados()
    if candidatos:
        print(f"Pendência de pureza — módulos declarados sem regra auditável: {candidatos}")
        tudo_limpo = False
    else:
        print("Nenhum módulo com pureza declarada e não registada.")
    imports_quebrados = imports_python_quebrados()
    if imports_quebrados:
        print(f"Imports Python quebrados em nucleo/*.py: {imports_quebrados}")
        tudo_limpo = False
    else:
        print("Imports Python de nucleo/*.py resolvem sem erro sintático.")

    print()
    print("--- Coerência (documentos, código, testes e interface) ---")
    verificacoes_coerencia = (
        ("Itens do plano fora de ordem", itens_do_plano_fora_de_ordem),
        ("Divergências do léxico no README", divergencias_lexico_no_readme),
        ("Divergências da estrutura de Português no README", divergencias_readme_vs_auditoria_portugues),
        ("Nomes de teste declarados sem ficheiro", nomes_de_teste_declarados_sem_ficheiro_real),
        ("Módulos da interface que falham ao importar", modulos_da_interface_falham_ao_importar),
        ("Ficheiros que violam a regra de versão única", arquivos_que_violam_regra_versao_unica),
    )
    for titulo, verificar in verificacoes_coerencia:
        problemas = verificar()
        if problemas:
            print(f"{titulo}: {problemas}")
            tudo_limpo = False
        else:
            print(f"{titulo}: nenhum.")

    print()
    print("--- Auditoria de fórmulas prontas (recriadas vs. validação/legado) ---")
    formulas = resumo_auditoria_formulas()
    print(f"Módulos com sinais de fórmula pronta/operador forte: {formulas['modulos_com_achados']}")
    print(f"  validação/legado declarado: {formulas['total_legado']}")
    print(f"  técnico não-fundamento declarado: {formulas.get('total_tecnico', 0)}")
    print(f"  suspeitos fora de classificação: {formulas['total_suspeitos']}")
    if formulas['suspeitos']:
        print("  PENDÊNCIA: há módulos PSF com sinais que exigem reconstrução/justificação.")
        for modulo, dados in sorted(formulas['suspeitos'].items()):
            exemplos = ", ".join(f"{a['valor']}@L{a['linha']}" for a in dados['achados'][:6])
            print(f"    {modulo}: {dados['total']} achado(s): {exemplos}")
        tudo_limpo = False
    else:
        print("  Nenhum suspeito fora de legado/validação/técnico não-fundamento.")
    print()
    print("--- Compatibilidade histórica dos marcadores ETAPA (não autoridade estrutural) ---")
    ordem_violacoes = violacoes_de_ordem()
    if ordem_violacoes:
        print(f"ALERTAS HISTÓRICOS em {len(ordem_violacoes)} módulo(s):", ordem_violacoes)
    else:
        print("Nenhuma inversão nos marcadores históricos conhecidos.")
    fora = modulos_fora_de_cobertura()
    if fora:
        print(f"Módulos técnicos/legados documentados fora da ordem numérica de etapas: {len(fora)} módulo(s)")
    else:
        print("Todos os módulos do núcleo estão cobertos pela verificação de ordem numérica.")
    return tudo_limpo


def main(argv: list[str] | None = None) -> None:
    args = _parser().parse_args(argv)

    if args.listar_testes:
        for perfil in ("padrao", "completo"):
            print(f"{perfil}:")
            for t in testes_do_perfil(perfil):
                print(" -", t.name)
        return

    auditorias_limpas = imprimir_auditorias()
    if args.exigir_formulas_limpas and resumo_auditoria_formulas()["suspeitos"]:
        sys.exit(1)

    if args.rapido:
        print("\n(modo --rapido: testes não executados)")
        if not auditorias_limpas:
            sys.exit(1)
        return

    perfil = "completo" if args.completo else "padrao"
    timeout = args.timeout_teste if args.timeout_teste is not None else (20.0 if args.completo else 10.0)
    orcamento = args.orcamento if args.orcamento is not None else (180.0 if args.completo else 30.0)

    print()
    print(f"--- Execução real da bateria de testes ({perfil}) ---")
    print(f"Limites: {timeout:g}s por teste; {orcamento:g}s no total.")
    resultados = executar_testes(timeout_segundos=timeout, perfil=perfil, orcamento_global_segundos=orcamento)
    resumo = resumo_execucao(resultados)

    for nome, r in resultados.items():
        estado = "OK" if r["passou"] else ("IGNORADO" if r.get("ignorado") else "FALHOU")
        print(f"  [{estado}] {nome} — {r['segundos']}s")

    if resumo["tudo_passou"]:
        print(f"Todos os {resumo['total']} ficheiros da bateria {perfil} passaram.")
    else:
        print(f"{resumo['passaram']}/{resumo['total']} passaram.")
        if resumo["timeouts_lista"]:
            print("Timeouts:", resumo["timeouts_lista"])
        if resumo["ignorados_lista"]:
            print("Ignorados por orçamento:", resumo["ignorados_lista"])
        if resumo["falharam_lista"]:
            print("Falharam:", resumo["falharam_lista"])
            for nome in resumo["falharam_lista"]:
                print(f"\n--- erro em {nome} ---")
                print(resultados[nome]["erro"])
        sys.exit(1)

    desempenho = comparar_e_atualizar(resultados)
    if desempenho["regressoes"]:
        print(f"\nAVISO — regressão de desempenho em {len(desempenho['regressoes'])} ficheiro(s):")
        for linha in desempenho["regressoes"]:
            print(f"  {linha}")
    elif desempenho["novos"]:
        print(f"({len(desempenho['novos'])} ficheiro(s) de teste registados agora pela primeira vez na linha de base de desempenho)")

    if not auditorias_limpas:
        sys.exit(1)


if __name__ == "__main__":
    main()
