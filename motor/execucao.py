"""Execução controlada da bateria de testes do motor PSF-IAminy.

Regra nova da Etapa 22 do motor: ``python3 motor_iaminy.py`` NÃO pode
ficar preso por causa de testes naturalmente lentos do núcleo unário.

Antes, o modo sem argumentos tentava correr todos os ficheiros
``testes/test_*.py`` com timeout individual alto. Isso era honesto, mas
não era operacional: bastavam alguns testes pesados para o comando do motor
passar do tempo razoável.

Agora existem perfis explícitos:

- ``meta``: sem testes matemáticos; só auditorias estruturais.
- ``padrao``: bateria curta, segura, representativa; é o padrão do CLI.
- ``completo``: todos os testes, só quando pedido explicitamente.

A execução também ganhou dois travões reais:

- timeout por ficheiro;
- orçamento global da bateria.

Camada meta — invoca os testes como subprocessos, não faz matemática.
"""
from __future__ import annotations

import os
import signal
import subprocess
import sys
import time
from pathlib import Path
from typing import Iterable

RAIZ = Path(__file__).resolve().parents[1]
TESTES = RAIZ / "testes"

# Bateria curta, escolhida para cobrir o motor, pureza, fluxo recente e
# bloco mais recente e auditorias sensíveis, sem arrastar testes historicamente lentos ou verbosos.
#
# 8 nomes fantasmas (test_conversa_fluida_natural.py, test_motores_aprimorados.py,
# test_bateria_matematica_basica_100.py, test_bateria_matematica_visual_100.py,
# test_modos_resposta.py, test_modos_aula_lote.py, test_bateria_matematica_progressiva.py,
# test_ortografia_bateria.py) foram encontrados aqui sem ficheiro correspondente em
# testes/ -- `_testes_por_nomes` os descartava em silêncio, então o perfil "padrão"
# rodava menos ficheiros do que esta lista prometia, sem aviso nenhum. Removidos;
# `test_coerencia_readme_plano_relatorio_regras.py` agora trava essa classe de erro.
TESTES_PADRAO = [
    "test_motor_meta.py",
    "test_motor_execucao_controle.py",
    "test_auditoria_formulas.py",
    "test_protecao_contra_fingimento.py",
    "test_coerencia_readme_plano_relatorio_regras.py",
    "test_semantica_denotacional_finita.py",
    "test_reescrita_provas_finitas.py",
    "test_automatos_pilha_finitos.py",
    "test_complexidade_recursos_finitos.py",
    "test_analise_discreta_finita.py",
    "test_topologia_finita.py",
    "test_medida_probabilidade_finita.py",
    "test_estatistica_finita_psf.py",
    "test_otimizacao_modelos_finitos.py",
    "test_sequencias_calculo_psf.py",
    "test_zeta_psf_finita.py",
    "test_lingua_portuguesa.py",
]

# Estes testes são válidos, mas não devem rodar automaticamente no comando
# principal sem consentimento explícito. Eles exercitam partes do núcleo
# unário ou exaustivas demais para serem o caminho feliz do motor.
TESTES_PESADOS_CONHECIDOS = {
    "test_nucleo.py",
    "test_binario_posicional_finito.py",
    "test_pureza_conceitual.py",
    "test_teorema_fundamental_aritmetica.py",
    "test_bezout_euclides_lema.py",
    "test_teoria_numeros_natural_rapida.py",
    "test_computabilidade_finita.py",
    "test_busca_prova_finita.py",
    "test_teoria_modelos_prova_finita.py",
    "test_combinatoria_natural.py",
    "test_relacoes_funcoes_naturais.py",
    "test_primalidade_fatoracao_pura.py",
    "test_divisao_euclidiana_pura.py",
}


def _todos_os_testes() -> list[Path]:
    return sorted(TESTES.glob("test_*.py"))


def _testes_por_nomes(nomes: Iterable[str]) -> list[Path]:
    encontrados = {p.name: p for p in _todos_os_testes()}
    return [encontrados[n] for n in nomes if n in encontrados]


def testes_do_perfil(perfil: str = "padrao") -> list[Path]:
    """Devolve os ficheiros de teste a executar para um perfil.

    ``padrao`` é intencionalmente pequeno: o motor deve ser uma ferramenta
    de diagnóstico rápida. ``completo`` continua disponível para auditoria
    profunda.
    """
    perfil = perfil.lower().strip()
    if perfil in {"meta", "rapido", "nenhum"}:
        return []
    if perfil in {"padrao", "normal", "seguro"}:
        return _testes_por_nomes(TESTES_PADRAO)
    if perfil in {"completo", "todos", "full"}:
        return _todos_os_testes()
    raise ValueError(f"perfil de testes desconhecido: {perfil!r}")


def _matar_processo(proc: subprocess.Popen) -> None:
    """Mata processo e grupo de processo, quando possível.

    ``subprocess.run(..., timeout=...)`` pode deixar filhos vivos em alguns
    cenários. O motor não pode depender disso. Aqui cada teste nasce em
    grupo próprio; se passar do limite, o grupo inteiro é encerrado.
    """
    try:
        os.killpg(proc.pid, signal.SIGKILL)
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


def _estilo_pytest_puro(arquivo: Path) -> bool:
    """True quando o ficheiro não tem bloco ``if __name__ == "__main__"``.

    Descoberta real ao investigar uma falha de import: ficheiros assim são
    puro estilo pytest (funções ``test_*`` soltas, sem ``main()``). Rodar
    ``python3 arquivo.py`` direto não executa nenhuma delas -- o processo só
    importa o módulo e sai com código 0, mesmo que as verificações reais
    falhassem. 14 dos 17 ficheiros de ``TESTES_PADRAO`` estavam nessa
    situação: a bateria "padrão" dava "passou" sem rodar nenhuma asserção.
    """
    return "__main__" not in arquivo.read_text(encoding="utf-8")


def _comando_para(arquivo: Path) -> list[str]:
    if _estilo_pytest_puro(arquivo):
        return [sys.executable, "-m", "pytest", str(arquivo), "-q"]
    return [sys.executable, str(arquivo)]


def _executar_um_teste(arquivo: Path, timeout_segundos: float) -> dict:
    inicio = time.monotonic()
    proc = subprocess.Popen(
        _comando_para(arquivo),
        cwd=RAIZ,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=True,
    )
    try:
        stdout, stderr = proc.communicate(timeout=timeout_segundos)
        return {
            "passou": proc.returncode == 0,
            "codigo_saida": proc.returncode,
            "erro": None if proc.returncode == 0 else (stdout[-1200:] + stderr[-1200:]),
            "segundos": round(time.monotonic() - inicio, 3),
            "timeout": False,
            "ignorado": False,
        }
    except subprocess.TimeoutExpired:
        _matar_processo(proc)
        stdout, stderr = proc.communicate()
        return {
            "passou": False,
            "codigo_saida": None,
            "erro": f"TIMEOUT do teste (> {timeout_segundos}s)\n" + (stdout[-800:] + stderr[-800:]),
            "segundos": round(time.monotonic() - inicio, 3),
            "timeout": True,
            "ignorado": False,
        }


def executar_testes(
    timeout_segundos: float = 12,
    perfil: str = "padrao",
    orcamento_global_segundos: float = 45,
) -> dict[str, dict]:
    """Corre os testes de um perfil com timeout por teste e orçamento global.

    Devolve ``{nome_ficheiro: {passou, codigo_saida, erro, segundos, ...}}``.
    Quando o orçamento global acaba, os testes restantes são marcados como
    ignorados por orçamento — o motor termina com relatório, não fica preso.
    """
    resultados: dict[str, dict] = {}
    arquivos = testes_do_perfil(perfil)
    inicio_global = time.monotonic()

    for arquivo in arquivos:
        decorrido = time.monotonic() - inicio_global
        restante = orcamento_global_segundos - decorrido
        if restante <= 0:
            resultados[arquivo.name] = {
                "passou": False,
                "codigo_saida": None,
                "erro": f"IGNORADO: orçamento global esgotado ({orcamento_global_segundos}s)",
                "segundos": 0.0,
                "timeout": False,
                "ignorado": True,
            }
            continue
        limite = max(1.0, min(timeout_segundos, restante))
        resultados[arquivo.name] = _executar_um_teste(arquivo, limite)

    return resultados


def resumo_execucao(resultados: dict[str, dict]) -> dict[str, object]:
    total = len(resultados)
    passaram = [nome for nome, r in resultados.items() if r["passou"]]
    falharam = [nome for nome, r in resultados.items() if not r["passou"] and not r.get("ignorado")]
    ignorados = [nome for nome, r in resultados.items() if r.get("ignorado")]
    timeouts = [nome for nome, r in resultados.items() if r.get("timeout")]
    return {
        "total": total,
        "passaram": len(passaram),
        "falharam_lista": falharam,
        "ignorados_lista": ignorados,
        "timeouts_lista": timeouts,
        "tudo_passou": len(falharam) == 0 and len(ignorados) == 0,
    }
