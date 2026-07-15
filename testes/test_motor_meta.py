"""Testes do motor meta (motor/) — não é matemática, é a camada
administrativa que audita o próprio projeto (pureza, ordem, fluxo).

Cobre a correção descrita em conhecimento: antes, `motor.pureza`/
`motor.ordem` só reconheciam imports no formato `from .modulo import NOME`.
`from . import modulo` e `import modulo` passavam pela auditoria sem gerar
nenhum nome — ou seja, com zero violações reportadas mesmo importando algo
proibido. Nenhum módulo do projeto usa hoje esses dois formatos, mas o
motor não pode assumir isso silenciosamente; este teste garante que os
três formatos são de facto detetados.

Roda com: python3 testes/test_motor_meta.py
"""
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from motor.pureza import _imports_do_modulo, _nomes_importados, REGRAS_PUREZA, auditar_tudo
from motor.ordem import _imports_relativos
from motor.fluxo import proxima_etapa_natural, proximos_documentados

falhas = []


def verificar(nome, obtido, esperado):
    ok = obtido == esperado
    marca = "OK" if ok else "FALHOU"
    print(f"[{marca}] {nome}: obtido={obtido!r} esperado={esperado!r}")
    if not ok:
        falhas.append(nome)


def _ficheiro_temporario(codigo: str) -> Path:
    caminho = Path(tempfile.mktemp(suffix=".py"))
    caminho.write_text(codigo, encoding="utf-8")
    return caminho


def main():
    print("PSF-IAminy — teste do motor meta (pureza, ordem, fluxo)")

    # Os três formatos de import que o Python aceita, cada um precisa
    # aparecer no resultado — é exatamente a lacuna que foi corrigida.
    caminho_from_nome = _ficheiro_temporario("from .primos import EH_PRIMO\n")
    caminho_from_modulo = _ficheiro_temporario("from . import primos\n")
    caminho_import_direto = _ficheiro_temporario("import primos\n")
    caminho_import_apelido = _ficheiro_temporario("import primos as p2\n")
    caminho_limpo = _ficheiro_temporario("from .aritmetica import SOMA\n")

    try:
        verificar(
            "from .primos import EH_PRIMO -> contém 'primos.EH_PRIMO' e 'primos'",
            {"primos", "primos.EH_PRIMO"} <= _nomes_importados(caminho_from_nome),
            True,
        )
        verificar(
            "from . import primos -> contém 'primos' (antes devolvia set() vazio)",
            "primos" in _nomes_importados(caminho_from_modulo),
            True,
        )
        verificar(
            "import primos -> contém 'primos' (antes devolvia set() vazio)",
            "primos" in _nomes_importados(caminho_import_direto),
            True,
        )
        verificar(
            "import primos as p2 -> usa o nome real 'primos', não o apelido",
            "primos" in _nomes_importados(caminho_import_apelido),
            True,
        )
        verificar(
            "módulo limpo (só aritmetica.SOMA) não contém 'primos'",
            "primos" in _nomes_importados(caminho_limpo),
            False,
        )

        # motor.ordem reaproveita a mesma extração — mesma cobertura.
        verificar(
            "motor.ordem também vê 'from . import primos'",
            "primos" in _imports_relativos(caminho_from_modulo),
            True,
        )
        verificar(
            "motor.ordem também vê 'import primos'",
            "primos" in _imports_relativos(caminho_import_direto),
            True,
        )

        # _imports_do_modulo devolve pares (modulo, nome) consistentes.
        verificar(
            "pares de 'from .primos import EH_PRIMO'",
            _imports_do_modulo(caminho_from_nome),
            [("primos", "EH_PRIMO")],
        )
        verificar(
            "pares de 'from . import primos'",
            _imports_do_modulo(caminho_from_modulo),
            [("primos", "primos")],
        )
    finally:
        for c in (caminho_from_nome, caminho_from_modulo, caminho_import_direto, caminho_import_apelido, caminho_limpo):
            c.unlink(missing_ok=True)

    # A repartição de REGRAS_PUREZA em conjuntos partilhados (_PROIB_*) não
    # pode ter mudado nenhuma regra de facto — só a forma como é escrita.
    verificar("REGRAS_PUREZA cobre todos os módulos puros registados", len(REGRAS_PUREZA), 50)
    verificar(
        "divisibilidade_pura continua com o conjunto completo (aritmética+primos+divisores)",
        REGRAS_PUREZA["divisibilidade_pura"],
        {"aritmetica.DIV", "aritmetica.MOD", "aritmetica.MDC", "aritmetica.MMC", "primos", "divisores"},
    )
    verificar(
        "divisao_euclidiana_pura continua só com DIV/MOD",
        REGRAS_PUREZA["divisao_euclidiana_pura"],
        {"aritmetica.DIV", "aritmetica.MOD"},
    )
    verificar(
        "primalidade_pura continua com DIV/MOD/primos (sem MDC/MMC/divisores)",
        REGRAS_PUREZA["primalidade_pura"],
        {"aritmetica.DIV", "aritmetica.MOD", "primos"},
    )

    verificar(
        "gramaticas_finitas entrou na auditoria de pureza",
        "gramaticas_finitas" in REGRAS_PUREZA,
        True,
    )
    verificar(
        "fluxo vivo externo contém etapa 1032",
        (1032, "funcao zeta psf finita") in proximos_documentados(),
        True,
    )
    verificar(
        "proxima_etapa_natural(1031) lê o ficheiro vivo, não o fallback genérico",
        proxima_etapa_natural(1031),
        (1032, "funcao zeta psf finita"),
    )

    # O projeto real, com a correção aplicada, continua limpo.
    violacoes = auditar_tudo()
    sujos = {m: v for m, v in violacoes.items() if v}
    verificar("auditoria real do projeto continua limpa (0 violações)", sujos, {})

    if falhas:
        print("\nFALHAS:")
        for nome in falhas:
            print(" -", nome)
        raise SystemExit(1)
    print("\nTudo passou.")


if __name__ == "__main__":
    main()
