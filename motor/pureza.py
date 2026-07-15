"""Auditoria de pureza do motor PSF-IAminy.

Até agora, "dependências proibidas" eram só prosa nos comentários de cada
módulo — ninguém verificava se eram respeitadas de facto. Este ficheiro
fecha essa lacuna: lê os imports REAIS de cada módulo registado (via AST,
não regex sobre texto solto) e confere contra uma lista explícita do que
esse módulo não pode usar.

Camada meta, como motor/fluxo.py — inspeciona código-fonte, não faz
matemática. Pode usar `ast`/`pathlib` nativos por essa razão.

Por que um registro explícito em vez de extrair a proibição da prosa de
cada ficheiro: a prosa é inconsistente ("Dependências proibidas aqui:" em
alguns, "NÃO importa X, NÃO importa Y" noutros, nada em alguns mais
antigos) — parsear isso com regex seria frágil e daria falsos negativos
silenciosos. Um registro explícito é mais trabalho para manter, mas nunca
finge verificar algo que não verificou.
"""
from __future__ import annotations

import ast
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
NUCLEO = RAIZ / "nucleo"

# Conjuntos-base de proibição, partilhados por vários módulos abaixo — em
# vez de repetir o mesmo literal `{"aritmetica.DIV", ...}` 17 vezes (o que
# havia antes: um "conjunto igual" podia divergir por engano numa edição
# futura sem ninguém notar).
_PROIB_ARIT = {"aritmetica.DIV", "aritmetica.MOD", "aritmetica.MDC", "aritmetica.MMC"}
_PROIB_ARIT_PRIMOS = _PROIB_ARIT | {"primos"}
_PROIB_ARIT_PRIMOS_DIVISORES = _PROIB_ARIT_PRIMOS | {"divisores"}
_PROIB_DIV_MOD = {"aritmetica.DIV", "aritmetica.MOD"}
_PROIB_DIV_MOD_PRIMOS = _PROIB_DIV_MOD | {"primos"}
_PROIB_EXTERNAS_FUNDAMENTO = {"math", "numpy", "sympy", "scipy", "sklearn", "tensorflow", "torch", "qiskit", "requests", "urllib"}

# módulo -> conjunto de "modulo.NOME" ou "modulo" que ele não pode importar.
# Curado a partir da intenção declarada em cada ficheiro (ver o cabeçalho
# de cada um) — a lista abaixo é o que se torna, de facto, verificável.
REGRAS_PUREZA: dict[str, set[str]] = {
    **{nome: _PROIB_ARIT_PRIMOS_DIVISORES for nome in (
        "divisibilidade_pura", "mdc_puro", "relacoes_funcoes_naturais",
        "operacoes_algebricas_naturais", "algebra_estruturas_ii",
        "algebra_linear_inicial", "eliminacao_gaussiana_finita",
        "grafos_finitos", "grafos_ponderados_algoritmos", "grafos_emparelhamento",
        "reticulado_finito", "grafos_coloracao_arestas", "ramsey_33",
        "grafos_redes_sociais",
        "expressoes_simbolicas_finitas", "binario", "metodos_finitos",
        "categorias_finitas", "logica_predicados_finita",
        "teoria_modelos_prova_finita", "busca_prova_finita",
        "computabilidade_finita", "gramaticas_finitas",
        "semantica_operacional_finita", "automatos_finitos_naturais",
        "linguagens_regulares_naturais", "gramaticas_livres_contexto_naturais",
        "semantica_tipos_finitos", "analise_sintatica_finita",
        "semantica_denotacional_finita", "reescrita_provas_finitas",
        "automatos_pilha_finitos", "complexidade_recursos_finitos",
        "analise_discreta_finita", "topologia_finita",
        "medida_probabilidade_finita", "estatistica_finita_psf",
        "otimizacao_modelos_finitos", "sequencias_calculo_psf", "zeta_psf_finita", "aritmetica_escolar_nativa",
    )},
    **{nome: _PROIB_ARIT_PRIMOS for nome in (
        "teorema_fundamental_aritmetica", "bezout_euclides_puro", "teoria_numeros_natural",
    )},
    **{nome: _PROIB_ARIT for nome in (
        "diferenca_controlada", "euclides_subtracao_pura",
    )},
    **{nome: _PROIB_DIV_MOD for nome in (
        "divisao_euclidiana_pura", "euclides_resto_puro",
    )},
    **{nome: _PROIB_DIV_MOD_PRIMOS for nome in (
        "primalidade_pura", "fatoracao_pura",
    )},
    # Módulos meta/técnicos declarados: não são conhecimento matemático puro,
    # mas também não podem importar dependências externas como fundamento.
    **{nome: _PROIB_EXTERNAS_FUNDAMENTO for nome in (
        "cerebro_unico",
        "motor_mestre",
        "plano_mae",
        "politica_definitividade",
        "ponte_comparador_python",
    )},

}


def _imports_do_modulo(caminho: Path) -> list[tuple[str, str]]:
    """Devolve TODOS os imports de um ficheiro como pares (modulo, nome),
    cobrindo os três formatos que o Python aceita:

      - ``from .modulo import NOME``  -> (modulo, NOME)
      - ``from . import modulo``      -> (modulo, modulo) — ``ast.ImportFrom``
        com ``module=None``; cada nome importado É o próprio submódulo.
      - ``import modulo [as x]``      -> (modulo, modulo) — ``ast.Import``.

    Antes, só o primeiro formato era reconhecido: um módulo que escrevesse
    ``from . import primos`` ou ``import primos`` passava pela auditoria de
    pureza (e pela verificação de ordem, que reaproveita esta função) sem
    gerar NENHUM nome — ou seja, com zero violações reportadas mesmo
    importando algo proibido. Nenhum módulo do projeto usa hoje esses dois
    formatos, mas a auditoria não pode assumir isso silenciosamente; seria
    exatamente o "fingir que verificou" que este ficheiro existe para evitar.
    """
    arvore = ast.parse(caminho.read_text(encoding="utf-8"), filename=str(caminho))
    pares: list[tuple[str, str]] = []
    for no in ast.walk(arvore):
        if isinstance(no, ast.ImportFrom):
            if no.module:
                modulo = no.module.lstrip(".")
                for alias in no.names:
                    pares.append((modulo, alias.name))
            else:
                for alias in no.names:
                    pares.append((alias.name, alias.name))
        elif isinstance(no, ast.Import):
            for alias in no.names:
                nome = alias.name.split(".")[0]
                pares.append((nome, nome))
    return pares


def _nomes_importados(caminho: Path) -> set[str]:
    """Extrai 'modulo.NOME' e 'modulo' de todos os imports, via AST."""
    nomes: set[str] = set()
    for modulo, nome in _imports_do_modulo(caminho):
        nomes.add(modulo)
        nomes.add(f"{modulo}.{nome}")
    return nomes


def auditar_modulo(nome_modulo: str) -> list[str]:
    """Violações (nomes proibidos encontrados de facto) para um módulo registado."""
    proibidos = REGRAS_PUREZA.get(nome_modulo)
    if proibidos is None:
        return []
    caminho = NUCLEO / f"{nome_modulo}.py"
    if not caminho.exists():
        return [f"módulo registado mas ficheiro não existe: {caminho}"]
    return sorted(_nomes_importados(caminho) & proibidos)


def auditar_tudo() -> dict[str, list[str]]:
    """{nome_do_modulo: [violações]} para todo o registo. Lista vazia = limpo."""
    return {nome: auditar_modulo(nome) for nome in sorted(REGRAS_PUREZA)}
