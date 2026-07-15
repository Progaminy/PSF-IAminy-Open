"""Rastreabilidade do motor PSF-IAminy.

Fecha duas lacunas que nem a auditoria de pureza nem a execução de testes
cobrem:

1. Uma ETAPA_XX.md pode dizer "implementado em nucleo/foo.py" mesmo que
   esse ficheiro tenha sido apagado, renomeado, ou nunca existido — nada
   verificava isso. `referencias_quebradas()` confirma que todo caminho
   entre crases numa etapa aponta para um ficheiro real.

2. Um módulo pode aparecer em nucleo/ sem NENHUMA etapa o referenciar —
   quebra silenciosa da regra "nenhum conceito sem etapa registada", que
   nem `motor.fluxo` (só conta .md) nem `motor.pureza` (só audita quem já
   está registado) conseguem detetar. `modulos_orfaos()` fecha isso.

3. Um ficheiro pode continuar presente, mas importar outro módulo ou atributo
   que deixou de existir. `imports_python_quebrados()` valida estaticamente os
   imports de carregamento de `nucleo/*.py`, sem executar o código auditado.

Camada meta — só lê nomes de ficheiros e texto, não faz matemática.
"""
from __future__ import annotations

import ast
import importlib.util
import re
import sys
import symtable
from importlib.machinery import BuiltinImporter, FrozenImporter, ModuleSpec, PathFinder
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CONHECIMENTO = RAIZ / "conhecimento"
NUCLEO = RAIZ / "nucleo"
ROADMAP = RAIZ / "ROADMAP.md"
LEIAME = RAIZ / "README.md"

_PADRAO_REFERENCIA = re.compile(r"`((?:nucleo|testes)/[a-zA-Z0-9_./]+\.py)`")
# Etapas 3-19 (e algumas entre 20-60) citam o ficheiro implementado dentro
# de um bloco cercado (```text\nnucleo/x.py\n```) em vez de crase inline —
# formato mais antigo, trocado por crase inline a partir da etapa ~61.
# Sem cobrir os dois formatos, o detetor de órfãos abaixo apontaria ~15
# ficheiros genuinamente documentados como "esquecidos". Ver
# AUDITORIA_MOTOR_ETAPA_14 para o registo desta descoberta.
_PADRAO_REFERENCIA_BLOCO = re.compile(r"^((?:nucleo|testes)/[a-zA-Z0-9_./]+\.py)$", re.MULTILINE)
# ROADMAP.md usa outro formato: `modulo.NOME` ou `modulo.py`, sem prefixo
# nucleo/ — os dois sistemas de rastreio do projeto (o índice conceitual
# por etapas e o roteiro por tópicos) nunca foram unificados, e citam
# ficheiros de formas diferentes. Um detetor de órfãos que só olhasse para
# um dos dois marcaria ~34 ficheiros como "esquecidos" quando na verdade
# estão documentados — só no OUTRO sistema. Ver AUDITORIA_MOTOR_ETAPA_14.
_PADRAO_REFERENCIA_ROADMAP = re.compile(r"`([a-zA-Z_]+)\.(?:py|[A-Z][A-Za-z_0-9]*)`")

# Módulos das etapas 1-2, tratadas como implícitas desde o início do
# projeto (ver motor.fluxo.ETAPAS_IMPLICITAS) — nunca tiveram, por
# desenho, uma ETAPA_XX.md própria.
_MODULOS_ETAPAS_IMPLICITAS = {"nucleo/primitivas.py", "nucleo/logica.py", "nucleo/aritmetica.py", "nucleo/traducao.py"}

# O contrato mínimo desta auditoria é o núcleo, que é a camada coberta
# pelas regras de rastreabilidade deste módulo. Outras camadas podem ser
# pedidas explicitamente pelo argumento ``diretorios`` sem allowlists.
_DIRETORIOS_IMPORTS = ("nucleo",)


def _referencias_de_etapa(caminho_md: Path) -> set[str]:
    texto = caminho_md.read_text(encoding="utf-8")
    return set(_PADRAO_REFERENCIA.findall(texto)) | set(_PADRAO_REFERENCIA_BLOCO.findall(texto))


def referencias_quebradas() -> dict[str, list[str]]:
    """{ficheiro_etapa: [caminhos citados que não existem]}. Vazio = tudo bate."""
    quebradas: dict[str, list[str]] = {}
    for arquivo in sorted(CONHECIMENTO.glob("ETAPA_*.md")):
        faltando = [r for r in _referencias_de_etapa(arquivo) if not (RAIZ / r).exists()]
        if faltando:
            quebradas[arquivo.name] = sorted(faltando)
    return quebradas


def modulos_nucleo_referenciados() -> set[str]:
    """Módulos nucleo/ referenciados pelo sistema de etapas (conhecimento/)."""
    referenciados: set[str] = set()
    for arquivo in sorted(CONHECIMENTO.glob("ETAPA_*.md")):
        referenciados |= {r for r in _referencias_de_etapa(arquivo) if r.startswith("nucleo/")}
    return referenciados


def modulos_nucleo_referenciados_no_roadmap() -> set[str]:
    """Módulos nucleo/ referenciados pelo sistema de tópicos (ROADMAP.md),
    convertidos para o formato nucleo/X.py para comparação uniforme."""
    if not ROADMAP.exists():
        return set()
    texto = ROADMAP.read_text(encoding="utf-8")
    nomes_modulo = {m.group(1) for m in _PADRAO_REFERENCIA_ROADMAP.finditer(texto)}
    existentes = {p.stem for p in NUCLEO.glob("*.py")}
    return {f"nucleo/{nome}.py" for nome in nomes_modulo if nome in existentes}


def modulos_nucleo_referenciados_no_readme() -> set[str]:
    """Módulos nucleo/ mencionados no README.md (cobre infraestrutura
    partilhada — combinadores.py, inversa_potencia.py — que não é um
    "tópico" numerado em nenhum dos dois sistemas acima, mas está
    genuinamente documentada, só que noutro lugar)."""
    if not LEIAME.exists():
        return set()
    texto = LEIAME.read_text(encoding="utf-8")
    existentes = {p.stem for p in NUCLEO.glob("*.py")}
    return {f"nucleo/{nome}.py" for nome in existentes if f"{nome}.py" in texto}


def modulos_orfaos() -> list[str]:
    """nucleo/*.py que NENHUM dos três lugares de documentação (ETAPA_XX.md,
    ROADMAP.md, README.md) referencia, e que também não é etapa implícita."""
    todos = {f"nucleo/{p.name}" for p in NUCLEO.glob("*.py") if p.name != "__init__.py"}
    rastreados = (
        modulos_nucleo_referenciados()
        | modulos_nucleo_referenciados_no_roadmap()
        | modulos_nucleo_referenciados_no_readme()
        | _MODULOS_ETAPAS_IMPLICITAS
    )
    return sorted(todos - rastreados)


def candidatos_a_pureza_nao_registados() -> list[str]:
    """Módulos cujo cabeçalho PARECE declarar dependências proibidas
    (menciona "proibid" ou "NÃO importa") mas não estão em
    motor.pureza.REGRAS_PUREZA — sinal de registo esquecido, não prova
    definitiva (por isso é uma sugestão a rever, não uma falha automática)."""
    from .pureza import REGRAS_PUREZA

    candidatos = []
    for caminho in sorted(NUCLEO.glob("*.py")):
        if caminho.stem == "__init__":
            continue
        cabecalho = caminho.read_text(encoding="utf-8")[:2500]
        cabecalho_lower = cabecalho.lower()
        parece_declarar = "proibid" in cabecalho_lower or "não importa" in cabecalho_lower
        if parece_declarar and caminho.stem not in REGRAS_PUREZA:
            candidatos.append(caminho.stem)
    return candidatos


def _localizar_modulo_sem_executar(nome: str, raiz: Path) -> ModuleSpec | None:
    """Localiza ``nome`` com os finders do importlib, sem chamar loader.exec_module."""
    partes = nome.split(".")
    if not partes or any(not parte for parte in partes):
        return None

    completo = partes[0]
    especificacao = (
        BuiltinImporter.find_spec(completo)
        or FrozenImporter.find_spec(completo)
        or PathFinder.find_spec(completo, [str(raiz), *sys.path])
    )
    for parte in partes[1:]:
        if especificacao is None or especificacao.submodule_search_locations is None:
            return None
        completo = f"{completo}.{parte}"
        especificacao = PathFinder.find_spec(completo, list(especificacao.submodule_search_locations))
    return especificacao


def _localizar_modulo_auditavel(nome: str, raiz: Path) -> ModuleSpec | None:
    """Localiza precisamente código local e conservadoramente pacote externo.

    Pacotes externos podem materializar submódulos durante a execução do seu
    ``__init__`` (``collections.abc`` é um exemplo da stdlib). Como esta
    auditoria não executa módulos, para eles confirma apenas a raiz importável.
    Módulos que pertencem à árvore local são sempre resolvidos por inteiro.
    """
    especificacao = _localizar_modulo_sem_executar(nome, raiz)
    if especificacao is not None or "." not in nome:
        return especificacao
    raiz_do_nome = nome.partition(".")[0]
    e_local = (raiz / raiz_do_nome).is_dir() or (raiz / f"{raiz_do_nome}.py").is_file()
    if e_local:
        return None
    return _localizar_modulo_sem_executar(raiz_do_nome, raiz)


def _caminho_python_local(especificacao: ModuleSpec, raiz: Path) -> Path | None:
    origem = especificacao.origin
    if not origem or not origem.endswith(".py"):
        return None
    caminho = Path(origem).resolve()
    try:
        caminho.relative_to(raiz.resolve())
    except ValueError:
        return None
    return caminho


def _valor_constante_de_type_checking(no: ast.expr) -> bool | None:
    """Valor conhecido de testes ``TYPE_CHECKING``; ``None`` se for outro if."""
    if isinstance(no, ast.Name) and no.id == "TYPE_CHECKING":
        return False
    if isinstance(no, ast.Attribute) and no.attr == "TYPE_CHECKING":
        return False
    if isinstance(no, ast.UnaryOp) and isinstance(no.op, ast.Not):
        valor = _valor_constante_de_type_checking(no.operand)
        return None if valor is None else not valor
    return None


def _imports_fora_de_type_checking(corpo: list[ast.stmt]):
    """Percorre imports de todos os escopos, exceto ramos ``TYPE_CHECKING``."""
    for no in corpo:
        if isinstance(no, (ast.Import, ast.ImportFrom)):
            yield no
        elif isinstance(no, ast.If):
            valor_type_checking = _valor_constante_de_type_checking(no.test)
            if valor_type_checking is True:
                yield from _imports_fora_de_type_checking(no.body)
            elif valor_type_checking is False:
                yield from _imports_fora_de_type_checking(no.orelse)
            else:
                yield from _imports_fora_de_type_checking(no.body)
                yield from _imports_fora_de_type_checking(no.orelse)
        elif isinstance(no, (ast.For, ast.AsyncFor, ast.While)):
            yield from _imports_fora_de_type_checking(no.body)
            yield from _imports_fora_de_type_checking(no.orelse)
        elif isinstance(no, (ast.With, ast.AsyncWith)):
            yield from _imports_fora_de_type_checking(no.body)
        elif isinstance(no, (ast.Try, ast.TryStar)):
            yield from _imports_fora_de_type_checking(no.body)
            for tratador in no.handlers:
                yield from _imports_fora_de_type_checking(tratador.body)
            yield from _imports_fora_de_type_checking(no.orelse)
            yield from _imports_fora_de_type_checking(no.finalbody)
        elif isinstance(no, ast.Match):
            for caso in no.cases:
                yield from _imports_fora_de_type_checking(caso.body)
        elif isinstance(no, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            yield from _imports_fora_de_type_checking(no.body)


def _modulo_e_pacote(especificacao: ModuleSpec) -> bool:
    return especificacao.submodule_search_locations is not None


def _nome_e_pacote_da_origem(caminho: Path, raiz: Path) -> tuple[str, str]:
    relativo = caminho.relative_to(raiz).with_suffix("")
    partes = list(relativo.parts)
    e_pacote = partes[-1] == "__init__"
    if e_pacote:
        partes.pop()
    nome = ".".join(partes)
    pacote = nome if e_pacote else nome.rpartition(".")[0]
    return nome, pacote


def imports_python_quebrados(
    raiz: "Path | None" = None,
    diretorios: tuple[str, ...] = _DIRETORIOS_IMPORTS,
) -> list[str]:
    """Deteta imports de carregamento quebrados sem importar o código auditado.

    Por omissão percorre ``nucleo/*.py``; camadas adicionais são opt-in pelo
    argumento ``diretorios``. A AST encontra erros sintáticos e imports em
    qualquer escopo. ``importlib`` localiza módulos sem executar os respetivos
    loaders; para módulos Python locais, a tabela de símbolos confirma ainda os
    atributos de ``from modulo import atributo``. Só imports de anotação sob
    ``TYPE_CHECKING``, que nunca rodam, ficam fora desta auditoria.
    """
    raiz = (raiz or RAIZ).resolve()
    fontes = sorted(
        caminho
        for diretorio in diretorios
        for caminho in (raiz / diretorio).glob("*.py")
        if caminho.is_file()
    )
    arvores: dict[Path, ast.Module] = {}
    erros_sintaxe: dict[Path, SyntaxError] = {}
    falhas: list[str] = []

    def arvore_de(caminho: Path) -> ast.Module | None:
        caminho = caminho.resolve()
        if caminho in arvores:
            return arvores[caminho]
        if caminho in erros_sintaxe:
            return None
        try:
            texto = caminho.read_text(encoding="utf-8")
            arvore = ast.parse(texto, filename=str(caminho))
            # ``ast.parse`` aceita alguns programas que o compilador rejeita
            # (por exemplo, ``return`` fora de função). Compilar a AST não a
            # executa e fecha também esses erros sintáticos/contextuais.
            compile(arvore, str(caminho), "exec")
        except (OSError, UnicodeError) as erro:
            falhas.append(f"{caminho}: não foi possível ler: {erro}")
            return None
        except SyntaxError as erro:
            erros_sintaxe[caminho] = erro
            return None
        arvores[caminho] = arvore
        return arvore

    for fonte in fontes:
        arvore_de(fonte)
    for caminho, erro in sorted(erros_sintaxe.items()):
        relativo = caminho.relative_to(raiz)
        falhas.append(f"{relativo}: erro de sintaxe na linha {erro.lineno}: {erro.msg}")

    nomes_por_caminho: dict[Path, set[str]] = {}

    def nomes_definidos(caminho: Path) -> set[str] | None:
        caminho = caminho.resolve()
        if caminho in nomes_por_caminho:
            return nomes_por_caminho[caminho]
        arvore = arvore_de(caminho)
        if arvore is None:
            return None
        tabela = symtable.symtable(caminho.read_text(encoding="utf-8"), str(caminho), "exec")
        nomes = {
            identificador
            for identificador in tabela.get_identifiers()
            if (
                (simbolo := tabela.lookup(identificador)).is_assigned()
                or simbolo.is_imported()
                or simbolo.is_namespace()
            )
        }
        nomes_por_caminho[caminho] = nomes
        return nomes

    for fonte in fontes:
        arvore = arvores.get(fonte.resolve())
        if arvore is None:
            continue
        _, pacote = _nome_e_pacote_da_origem(fonte, raiz)
        relativo = fonte.relative_to(raiz)
        for no in _imports_fora_de_type_checking(arvore.body):
            if isinstance(no, ast.Import):
                for apelido in no.names:
                    if _localizar_modulo_auditavel(apelido.name, raiz) is None:
                        falhas.append(f"{relativo}:{no.lineno}: módulo '{apelido.name}' inexistente")
                continue

            if no.level:
                referencia = "." * no.level + (no.module or "")
                try:
                    modulo = importlib.util.resolve_name(referencia, pacote)
                except (ImportError, ValueError):
                    falhas.append(f"{relativo}:{no.lineno}: import relativo '{referencia}' inválido")
                    continue
            else:
                modulo = no.module or ""

            especificacao = _localizar_modulo_auditavel(modulo, raiz)
            if especificacao is None:
                falhas.append(f"{relativo}:{no.lineno}: módulo '{modulo}' inexistente")
                continue

            caminho_alvo = _caminho_python_local(especificacao, raiz)
            if caminho_alvo is None:
                # Atributos de stdlib/extensões não podem ser inspecionados
                # estaticamente com segurança; a existência do módulo já foi
                # confirmada sem o executar.
                continue
            nomes = nomes_definidos(caminho_alvo)
            if nomes is None or "__getattr__" in nomes:
                continue
            for apelido in no.names:
                if apelido.name == "*" or apelido.name in nomes:
                    continue
                submodulo = f"{modulo}.{apelido.name}"
                if _modulo_e_pacote(especificacao) and _localizar_modulo_sem_executar(submodulo, raiz):
                    continue
                falhas.append(
                    f"{relativo}:{no.lineno}: atributo '{apelido.name}' inexistente em '{modulo}'"
                )

    return sorted(set(falhas))
