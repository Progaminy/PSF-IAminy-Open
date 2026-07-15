"""Leitura de documentos anexados ao PSF-IAminy.

Só usa a biblioteca padrão -- sem dependências novas. Um `.docx` é, por
baixo, um `.zip` com XML (`word/document.xml`); dá para extrair o texto
sem nenhuma biblioteca de terceiros. Um `.zip` pode conter vários
ficheiros `.txt`/`.docx`; cada um é lido separadamente.

PDF fica de fora por agora -- exigiria uma dependência nova que o projeto
ainda não tem. Um anexo em formato não suportado levanta erro explícito,
não é ignorado silenciosamente.
"""
from __future__ import annotations

import io
import re
import zipfile
from pathlib import Path

_QUEBRA_LINHA = re.compile(r"<w:(?:br|cr)\s*/?>|</w:p>|</w:tr>")
_QUEBRA_TAB = re.compile(r"<w:tab\s*/?>")
_TAG = re.compile(r"<[^>]+>")
_ESPACOS = re.compile(r"[ \t]{2,}")
_LINHAS_VAZIAS = re.compile(r"\n{2,}")

EXTENSOES_SUPORTADAS: tuple[str, ...] = (".txt", ".docx", ".zip")


def _limpar_xml(xml: str) -> str:
    """Extrai o texto de um `word/document.xml`, preservando quebras de
    linha/célula (`<w:br/>`, fim de parágrafo, fim de linha de tabela) --
    sem isso, parágrafos e células de tabela adjacentes ficam colados
    num único bloco de texto, impossível de segmentar depois."""
    texto = _QUEBRA_LINHA.sub("\n", xml)
    texto = _QUEBRA_TAB.sub("\t", texto)
    texto = _TAG.sub("", texto)
    texto = _ESPACOS.sub(" ", texto)
    texto = _LINHAS_VAZIAS.sub("\n", texto)
    return texto.strip()


def ler_docx_bytes(dados: bytes) -> str:
    with zipfile.ZipFile(io.BytesIO(dados)) as pacote:
        xml = pacote.read("word/document.xml").decode("utf-8")
    return _limpar_xml(xml)


def ler_docx(caminho: "Path | str") -> str:
    return ler_docx_bytes(Path(caminho).read_bytes())


def ler_txt(caminho: "Path | str") -> str:
    return Path(caminho).read_text(encoding="utf-8", errors="replace")


def ler_zip(origem: "Path | str | bytes") -> dict[str, str]:
    """Lê todo `.txt`/`.docx` dentro de um `.zip`. Devolve {nome_interno: texto}.

    Aceita um caminho ou os bytes crus do `.zip` -- o segundo caso serve
    para um anexo recebido por upload, sem precisar de tocar em disco."""
    fonte = io.BytesIO(origem) if isinstance(origem, bytes) else origem
    conteudos: dict[str, str] = {}
    with zipfile.ZipFile(fonte) as pacote:
        for info in pacote.infolist():
            if info.is_dir():
                continue
            nome = info.filename
            sufixo = Path(nome).suffix.lower()
            dados = pacote.read(nome)
            if sufixo == ".txt":
                conteudos[nome] = dados.decode("utf-8", errors="replace")
            elif sufixo == ".docx":
                conteudos[nome] = ler_docx_bytes(dados)
    return conteudos


def ler_anexo(caminho: "Path | str") -> dict[str, str]:
    """Lê um anexo suportado. Devolve {nome: texto}: um `.txt`/`.docx`
    devolve um único par; um `.zip` devolve um par por ficheiro interno lido."""
    caminho = Path(caminho)
    sufixo = caminho.suffix.lower()
    if sufixo == ".txt":
        return {caminho.name: ler_txt(caminho)}
    if sufixo == ".docx":
        return {caminho.name: ler_docx(caminho)}
    if sufixo == ".zip":
        return ler_zip(caminho)
    raise ValueError(
        f"formato de anexo ainda não suportado: {sufixo!r} (só {EXTENSOES_SUPORTADAS})"
    )


def ler_anexo_bytes(nome: str, dados: bytes) -> dict[str, str]:
    """Variante de `ler_anexo` a partir de bytes crus + o nome (só para a
    extensão) -- para um anexo que chega por upload, sem ficheiro em disco."""
    sufixo = Path(nome).suffix.lower()
    if sufixo == ".txt":
        return {nome: dados.decode("utf-8", errors="replace")}
    if sufixo == ".docx":
        return {nome: ler_docx_bytes(dados)}
    if sufixo == ".zip":
        return ler_zip(dados)
    raise ValueError(
        f"formato de anexo ainda não suportado: {sufixo!r} (só {EXTENSOES_SUPORTADAS})"
    )
