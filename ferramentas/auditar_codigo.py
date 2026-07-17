#!/usr/bin/env python3
"""Auditoria estrutural reproduzível do código Python de produção.

Não altera ficheiros. Mede tipagem, docstrings, tratamento amplo de exceções e
corpos exatamente duplicados. O relatório serve para priorizar revisão humana;
não transforma métricas em prova automática de qualidade.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path

EXCLUIR_PARTES = {
    ".git",
    ".venv",
    "venv",
    "build",
    "dist",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    "cao_de_caca",
    "testes",
    "examples",
    "exemplos",
    "benchmarks",
    "avaliacoes",
    "ferramentas",
    "site",
}


@dataclass(frozen=True)
class LocalFuncao:
    ficheiro: str
    linha: int
    nome: str


@dataclass
class Resultado:
    ficheiros_python: int = 0
    erros_sintaxe: int = 0
    funcoes_metodos: int = 0
    funcoes_publicas: int = 0
    totalmente_tipadas: int = 0
    funcoes_com_retorno_tipado: int = 0
    funcoes_com_docstring: int = 0
    except_bare: int = 0
    except_exception: int = 0
    raise_exception_generico: int = 0
    grupos_duplicados_exatos: int = 0
    funcoes_em_grupos_duplicados: int = 0


def ficheiros_producao(raiz: Path) -> list[Path]:
    resultado = []
    for caminho in raiz.rglob("*.py"):
        relativo = caminho.relative_to(raiz)
        if any(parte in EXCLUIR_PARTES for parte in relativo.parts):
            continue
        resultado.append(caminho)
    return sorted(resultado)


def parametros_exigidos(no: ast.FunctionDef | ast.AsyncFunctionDef) -> list[ast.arg]:
    argumentos = [*no.args.posonlyargs, *no.args.args, *no.args.kwonlyargs]
    return [arg for arg in argumentos if arg.arg not in {"self", "cls"}]


def totalmente_tipada(no: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    return no.returns is not None and all(arg.annotation is not None for arg in parametros_exigidos(no))


def corpo_normalizado(no: ast.FunctionDef | ast.AsyncFunctionDef) -> str | None:
    corpo = list(no.body)
    if corpo and isinstance(corpo[0], ast.Expr) and isinstance(corpo[0].value, ast.Constant) and isinstance(corpo[0].value.value, str):
        corpo = corpo[1:]
    # Ignora funções triviais: duplicação de ``return None``/``pass`` não é
    # evidência útil de dívida de produção.
    nos = sum(1 for item in corpo for _ in ast.walk(item))
    if nos < 8:
        return None
    return ast.dump(ast.Module(body=corpo, type_ignores=[]), include_attributes=False)


def auditar(raiz: Path) -> tuple[Resultado, dict[str, list[LocalFuncao]], list[str]]:
    resultado = Resultado()
    duplicados: dict[str, list[LocalFuncao]] = defaultdict(list)
    erros: list[str] = []

    for caminho in ficheiros_producao(raiz):
        resultado.ficheiros_python += 1
        relativo = str(caminho.relative_to(raiz))
        try:
            arvore = ast.parse(caminho.read_text(encoding="utf-8"), filename=relativo)
        except (SyntaxError, UnicodeDecodeError) as exc:
            resultado.erros_sintaxe += 1
            erros.append(f"{relativo}: {exc}")
            continue

        for no in ast.walk(arvore):
            if isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef)):
                resultado.funcoes_metodos += 1
                if not no.name.startswith("_"):
                    resultado.funcoes_publicas += 1
                if totalmente_tipada(no):
                    resultado.totalmente_tipadas += 1
                if no.returns is not None:
                    resultado.funcoes_com_retorno_tipado += 1
                if ast.get_docstring(no):
                    resultado.funcoes_com_docstring += 1
                corpo = corpo_normalizado(no)
                if corpo is not None:
                    chave = hashlib.sha256(corpo.encode("utf-8")).hexdigest()
                    duplicados[chave].append(LocalFuncao(relativo, no.lineno, no.name))
            elif isinstance(no, ast.ExceptHandler):
                if no.type is None:
                    resultado.except_bare += 1
                elif isinstance(no.type, ast.Name) and no.type.id in {"Exception", "BaseException"}:
                    resultado.except_exception += 1
            elif isinstance(no, ast.Raise) and isinstance(no.exc, ast.Call):
                if isinstance(no.exc.func, ast.Name) and no.exc.func.id in {"Exception", "BaseException"}:
                    resultado.raise_exception_generico += 1

    grupos = {chave: locais for chave, locais in duplicados.items() if len(locais) > 1}
    resultado.grupos_duplicados_exatos = len(grupos)
    resultado.funcoes_em_grupos_duplicados = sum(len(locais) for locais in grupos.values())
    return resultado, grupos, erros


def percentagem(parte: int, total: int) -> float:
    return round((parte / total * 100) if total else 0.0, 1)


def texto_markdown(resultado: Resultado, grupos: dict[str, list[LocalFuncao]], erros: list[str]) -> str:
    linhas = [
        "# Auditoria estrutural do código de produção",
        "",
        "| Métrica | Valor |",
        "| --- | ---: |",
        f"| Ficheiros Python analisados | {resultado.ficheiros_python} |",
        f"| Funções/métodos | {resultado.funcoes_metodos} |",
        f"| Funções públicas | {resultado.funcoes_publicas} |",
        f"| Totalmente tipadas | {resultado.totalmente_tipadas} ({percentagem(resultado.totalmente_tipadas, resultado.funcoes_metodos)}%) |",
        f"| Com retorno tipado | {resultado.funcoes_com_retorno_tipado} ({percentagem(resultado.funcoes_com_retorno_tipado, resultado.funcoes_metodos)}%) |",
        f"| Com docstring própria | {resultado.funcoes_com_docstring} ({percentagem(resultado.funcoes_com_docstring, resultado.funcoes_metodos)}%) |",
        f"| `except:` sem tipo | {resultado.except_bare} |",
        f"| `except Exception/BaseException` | {resultado.except_exception} |",
        f"| `raise Exception/BaseException` genérico | {resultado.raise_exception_generico} |",
        f"| Grupos de corpos exatamente duplicados | {resultado.grupos_duplicados_exatos} |",
        f"| Funções nesses grupos | {resultado.funcoes_em_grupos_duplicados} |",
        f"| Erros de sintaxe/leitura | {resultado.erros_sintaxe} |",
    ]
    if grupos:
        linhas += ["", "## Duplicações exatas a rever"]
        for locais in sorted(grupos.values(), key=lambda x: (-len(x), x[0].ficheiro)):
            linhas.append("")
            linhas.append("- " + "; ".join(f"`{x.ficheiro}:{x.linha}` ({x.nome})" for x in locais))
    if erros:
        linhas += ["", "## Erros de análise", ""] + [f"- `{erro}`" for erro in erros]
    linhas += [
        "",
        "Estas métricas são uma linha de base, não uma sentença automática. Funções internas",
        "matemáticas e callbacks podem ter contratos claros por contexto mesmo sem anotações;",
        "duplicação exata pode ser intencional. Cada caso deve ser revisto antes de alterar código estável.",
    ]
    return "\n".join(linhas) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raiz", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--saida", type=Path)
    args = parser.parse_args()
    resultado, grupos, erros = auditar(args.raiz.resolve())
    if args.json:
        conteudo = json.dumps(
            {
                "resultado": asdict(resultado),
                "duplicados": {k: [asdict(x) for x in v] for k, v in grupos.items()},
                "erros": erros,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        ) + "\n"
    else:
        conteudo = texto_markdown(resultado, grupos, erros)
    if args.saida:
        args.saida.parent.mkdir(parents=True, exist_ok=True)
        args.saida.write_text(conteudo, encoding="utf-8")
    else:
        print(conteudo, end="")
    return 1 if erros else 0


if __name__ == "__main__":
    raise SystemExit(main())
