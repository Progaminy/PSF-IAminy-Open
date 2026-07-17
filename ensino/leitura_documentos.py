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

# Limites defensivos para anexos compactados. São deliberadamente fixos para
# que todas as portas de entrada (caminho e bytes) tenham o mesmo
# comportamento e para preservar a API pública simples deste módulo.
_MAX_BYTES_COMPACTADOS = 32 * 1024 * 1024
_MAX_ENTRADAS_ZIP = 512
_MAX_BYTES_POR_ENTRADA = 16 * 1024 * 1024
_MAX_BYTES_DESCOMPRIMIDOS = 64 * 1024 * 1024
_MAX_RAZAO_COMPACTACAO = 200.0
_MIN_BYTES_PARA_VALIDAR_RAZAO = 1024 * 1024


def _formatar_bytes(quantidade: int) -> str:
    return f"{quantidade:,} bytes".replace(",", " ")


def _erro_inseguro(tipo: str, detalhe: str) -> ValueError:
    return ValueError(f"arquivo {tipo} inseguro: {detalhe}")


def _validar_tamanho_compactado(tamanho: int, tipo: str) -> None:
    if tamanho > _MAX_BYTES_COMPACTADOS:
        raise _erro_inseguro(
            tipo,
            "tamanho compactado "
            f"({_formatar_bytes(tamanho)}) excede o limite de "
            f"{_formatar_bytes(_MAX_BYTES_COMPACTADOS)}",
        )


def _validar_nome_interno(nome: str, tipo: str) -> None:
    """Rejeita nomes que seriam perigosos numa eventual extração posterior.

    Este módulo não extrai em disco, mas os nomes são devolvidos ao chamador.
    Impedir travessia e formas ambíguas aqui evita que um consumidor trate uma
    chave aparentemente inocente como caminho seguro.
    """
    if not nome:
        raise _erro_inseguro(tipo, "contém uma entrada sem nome")
    if "\\" in nome:
        raise _erro_inseguro(
            tipo,
            f"caminho interno perigoso ou ambíguo: {nome!r}",
        )
    if nome.startswith("/") or re.match(r"^[A-Za-z]:", nome):
        raise _erro_inseguro(tipo, f"caminho interno absoluto: {nome!r}")
    if ".." in nome.split("/"):
        raise _erro_inseguro(
            tipo,
            f"caminho interno com travessia de diretórios: {nome!r}",
        )


def _validar_pacote(
    pacote: zipfile.ZipFile,
    tipo: str,
) -> dict[str, zipfile.ZipInfo]:
    """Valida metadados do ZIP antes de descomprimir qualquer entrada."""
    entradas = pacote.infolist()
    if len(entradas) > _MAX_ENTRADAS_ZIP:
        raise _erro_inseguro(
            tipo,
            f"contém {len(entradas)} entradas; o limite é {_MAX_ENTRADAS_ZIP}",
        )

    total = 0
    por_nome: dict[str, zipfile.ZipInfo] = {}
    for info in entradas:
        nome = info.filename
        _validar_nome_interno(nome, tipo)
        if nome in por_nome:
            raise _erro_inseguro(tipo, f"contém entrada duplicada: {nome!r}")
        por_nome[nome] = info

        if info.file_size > _MAX_BYTES_POR_ENTRADA:
            raise _erro_inseguro(
                tipo,
                f"a entrada {nome!r} declara {_formatar_bytes(info.file_size)} "
                "descomprimidos; o limite por entrada é "
                f"{_formatar_bytes(_MAX_BYTES_POR_ENTRADA)}",
            )
        total += info.file_size
        if total > _MAX_BYTES_DESCOMPRIMIDOS:
            raise _erro_inseguro(
                tipo,
                "o tamanho total declarado após descompressão "
                f"({_formatar_bytes(total)}) excede o limite de "
                f"{_formatar_bytes(_MAX_BYTES_DESCOMPRIMIDOS)}",
            )

        if (
            info.file_size >= _MIN_BYTES_PARA_VALIDAR_RAZAO
            and info.file_size / max(info.compress_size, 1)
            > _MAX_RAZAO_COMPACTACAO
        ):
            razao = info.file_size / max(info.compress_size, 1)
            raise _erro_inseguro(
                tipo,
                f"a entrada {nome!r} tem razão de compactação {razao:.1f}:1; "
                f"o limite é {_MAX_RAZAO_COMPACTACAO:.1f}:1 "
                "(possível ZIP bomb)",
            )

    return por_nome


def _ler_entrada_limitada(
    pacote: zipfile.ZipFile,
    info: zipfile.ZipInfo,
    tipo: str,
) -> bytes:
    """Lê no máximo o limite aceito, mesmo se os metadados forem falsos."""
    with pacote.open(info) as entrada:
        dados = entrada.read(_MAX_BYTES_POR_ENTRADA + 1)
    if len(dados) > _MAX_BYTES_POR_ENTRADA:
        raise _erro_inseguro(
            tipo,
            f"a entrada {info.filename!r} ultrapassou o limite de "
            f"{_formatar_bytes(_MAX_BYTES_POR_ENTRADA)} durante a leitura",
        )
    return dados


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
    _validar_tamanho_compactado(len(dados), "DOCX")
    with zipfile.ZipFile(io.BytesIO(dados)) as pacote:
        entradas = _validar_pacote(pacote, "DOCX")
        info_documento = entradas["word/document.xml"]
        xml = _ler_entrada_limitada(pacote, info_documento, "DOCX").decode("utf-8")
    return _limpar_xml(xml)


def ler_docx(caminho: "Path | str") -> str:
    caminho = Path(caminho)
    _validar_tamanho_compactado(caminho.stat().st_size, "DOCX")
    return ler_docx_bytes(caminho.read_bytes())


def ler_txt(caminho: "Path | str") -> str:
    return Path(caminho).read_text(encoding="utf-8", errors="replace")


def ler_zip(origem: "Path | str | bytes") -> dict[str, str]:
    """Lê todo `.txt`/`.docx` dentro de um `.zip`. Devolve {nome_interno: texto}.

    Aceita um caminho ou os bytes crus do `.zip` -- o segundo caso serve
    para um anexo recebido por upload, sem precisar de tocar em disco."""
    if isinstance(origem, bytes):
        _validar_tamanho_compactado(len(origem), "ZIP")
        fonte = io.BytesIO(origem)
    else:
        caminho = Path(origem)
        _validar_tamanho_compactado(caminho.stat().st_size, "ZIP")
        fonte = caminho
    conteudos: dict[str, str] = {}
    with zipfile.ZipFile(fonte) as pacote:
        _validar_pacote(pacote, "ZIP")
        for info in pacote.infolist():
            if info.is_dir():
                continue
            nome = info.filename
            sufixo = Path(nome).suffix.lower()
            if sufixo == ".txt":
                dados = _ler_entrada_limitada(pacote, info, "ZIP")
                conteudos[nome] = dados.decode("utf-8", errors="replace")
            elif sufixo == ".docx":
                dados = _ler_entrada_limitada(pacote, info, "ZIP")
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
