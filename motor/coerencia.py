"""Verificador de coerência entre README, plano, relatório e regras.

Item pendente desde o início do projeto ("O que falta" do README): nada
cruzava automaticamente o que os documentos afirmam com o estado real do
motor. Consequência concreta encontrada só nesta auditoria: `interface/`
ficou quebrado (importava uma classe que já não existe) sem que nada
detectasse -- e o cabeçalho do plano citado por um teste antigo já não batia
com o texto real de `PLANO_PSF_IAMINY.md`. Este módulo não decide o que é
verdade; só compara documento com código e aponta a divergência.
"""
from __future__ import annotations

import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]

_PADRAO_ITEM_PLANO = re.compile(r"^(\d+)\.\s", re.MULTILINE)


def itens_do_plano_fora_de_ordem(caminho: "Path | None" = None) -> tuple[str, ...]:
    """`PLANO_PSF_IAMINY.md` deve ter itens 1..N estritamente sequenciais.

    Devolve uma descrição por problema encontrado (duplicado, buraco ou fora
    de ordem); tupla vazia quando a numeração está limpa. Não existe hoje
    nenhuma checagem automática disto -- foi um erro real, cometido e
    corrigido à mão, na mesma sessão que motivou este verificador.
    """
    caminho = caminho or (RAIZ / "PLANO_PSF_IAMINY.md")
    texto = caminho.read_text(encoding="utf-8")
    numeros = [int(n) for n in _PADRAO_ITEM_PLANO.findall(texto)]
    problemas: list[str] = []
    esperado = 1
    for n in numeros:
        if n != esperado:
            problemas.append(f"esperava item {esperado}, encontrado item {n}")
            esperado = n
        esperado += 1
    return tuple(problemas)


def numeros_da_auditoria_estrutural_no_readme(caminho: "Path | None" = None) -> dict[str, int | str]:
    """Extrai o bloco ```text ... conceitos: N ... raiz: X ...``` do README."""
    caminho = caminho or (RAIZ / "README.md")
    texto = caminho.read_text(encoding="utf-8")
    bloco = re.search(
        r"Auditoria estrutural atual:\s*```text\n(.*?)```",
        texto,
        re.DOTALL,
    )
    if bloco is None:
        return {}
    dados: dict[str, int | str] = {}
    for linha in bloco.group(1).strip().splitlines():
        chave, _, valor = linha.partition(":")
        chave, valor = chave.strip(), valor.strip()
        dados[chave] = int(valor) if valor.lstrip("-").isdigit() else valor
    return dados


def divergencias_readme_vs_auditoria_portugues() -> tuple[str, ...]:
    """Compara o bloco de auditoria do README com `auditar_estrutura_portugues()` ao vivo."""
    from lingua_portuguesa import MotorPortugues

    lidos = numeros_da_auditoria_estrutural_no_readme()
    if not lidos:
        return ("bloco 'Auditoria estrutural atual' não encontrado no README",)
    real = MotorPortugues().auditar_estrutura_portugues()
    esperado = {
        "conceitos": real.conceitos,
        "relações diretas": real.relacoes_diretas,
        "raiz": real.raizes[0] if len(real.raizes) == 1 else ", ".join(real.raizes),
        "duplicações": len(real.nomes_duplicados),
        "dependências ausentes": len(real.dependencias_ausentes),
        "dependências futuras": len(real.dependencias_futuras),
        "ciclos": len(real.ciclos),
        "profundidade máxima conhecida": real.profundidade_maxima,
    }
    divergencias = []
    for chave, valor_real in esperado.items():
        valor_lido = lidos.get(chave)
        if valor_lido != valor_real:
            divergencias.append(f"{chave}: README diz {valor_lido!r}, motor tem {valor_real!r}")
    return tuple(divergencias)


_PADRAO_LEXICO_NO_README = re.compile(
    r"O léxico interno reconhece \*\*(\d+) lemas, (\d+) formas e (\d+) leituras\*\*\."
)


def divergencias_lexico_no_readme(caminho: "Path | None" = None) -> tuple[str, ...]:
    """Compara a frase de inventário lexical do README com o dicionário vivo."""
    from lingua_portuguesa.lexico import Dicionario

    caminho = caminho or (RAIZ / "README.md")
    texto = caminho.read_text(encoding="utf-8")
    encontrado = _PADRAO_LEXICO_NO_README.search(texto)
    if encontrado is None:
        return ("frase de inventário do léxico não encontrada no README",)

    documentado = tuple(int(valor) for valor in encontrado.groups())
    dicionario = Dicionario.padrao()
    real = (len(dicionario.lemas()), dicionario.total_formas(), len(dicionario))
    nomes = ("lemas", "formas", "leituras")
    return tuple(
        f"{nome}: README diz {valor_documentado}, dicionário tem {valor_real}"
        for nome, valor_documentado, valor_real in zip(nomes, documentado, real)
        if valor_documentado != valor_real
    )


# A contagem total de testes documentada não é automatizada aqui de propósito:
# obtê-la com fidelidade exigiria executar pytest num subprocesso dentro do próprio
# teste de coerência, tornando a verificação pesada, recursiva e frágil.


_PADROES_VERSAO_PROIBIDOS = (
    re.compile(r"_v\d+(?:\.|$)"),
    re.compile(r"_final(?:\.|$)"),
    re.compile(r"_nova[_-]?edicao", re.IGNORECASE),
    re.compile(r"_backup(?:\.|$)"),
    re.compile(r"_antigo(?:\.|$)"),
)

_DIRETORIOS_IGNORADOS = {".git", "__pycache__", "cao_de_caca", "privado", "node_modules"}


def nomes_de_teste_declarados_sem_ficheiro_real() -> tuple[str, ...]:
    """`TESTES_PADRAO`/`TESTES_PESADOS_CONHECIDOS` (`motor/execucao.py`) prometem
    rodar ficheiros por nome; `_testes_por_nomes` descarta em silêncio quem não
    existe. 8 nomes fantasmas viviam em `TESTES_PADRAO` até esta auditoria --
    o perfil "padrão" rodava menos do que anunciava, sem nenhum aviso.
    """
    from motor.execucao import TESTES, TESTES_PADRAO, TESTES_PESADOS_CONHECIDOS

    reais = {p.name for p in TESTES.glob("test_*.py")}
    declarados = set(TESTES_PADRAO) | TESTES_PESADOS_CONHECIDOS
    return tuple(sorted(declarados - reais))


def modulos_da_interface_falham_ao_importar() -> tuple[str, ...]:
    """`interface/roteador.py` ficou quebrado sem que nada detectasse (importava
    `ensino.dialogo.MotorDialogo`, classe que não existe mais nesta árvore) --
    `verificar_integridade.py` não cobre `interface`. Fecha esse ponto cego.
    """
    import importlib

    falhas = []
    for modulo in ("interface.servidor", "interface.roteador", "interface.conversas", "interface.mapa_conhecimento"):
        try:
            importlib.import_module(modulo)
        except Exception as erro:  # noqa: BLE001 -- qualquer falha de import é o que queremos capturar
            falhas.append(f"{modulo}: {erro}")
    return tuple(falhas)


def arquivos_que_violam_regra_versao_unica(raiz: "Path | None" = None) -> tuple[str, ...]:
    """`REGRA_VERSAO_UNICA.md` proíbe "v1", "v2", "nova edição", "edição final" internos.

    Varre nomes de ficheiro reais em busca desse padrão -- não confia só na
    regra estar escrita, confirma que ninguém violou por engano.
    """
    raiz = raiz or RAIZ
    achados = []
    for caminho in raiz.rglob("*"):
        if not caminho.is_file():
            continue
        if any(parte in _DIRETORIOS_IGNORADOS for parte in caminho.parts):
            continue
        nome = caminho.stem.lower()
        for padrao in _PADROES_VERSAO_PROIBIDOS:
            if padrao.search(nome):
                achados.append(str(caminho.relative_to(raiz)))
                break
    return tuple(achados)
