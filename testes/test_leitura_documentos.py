"""Teste de ensino/leitura_documentos.py.

Usa ficheiros sintéticos (não depende de privado/avalmath.docx existir)
para provar txt/docx/zip, por caminho e por bytes.

Roda com: python3 testes/test_leitura_documentos.py
"""
import io
import os
import sys
import tempfile
import zipfile
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ensino.leitura_documentos import ler_anexo, ler_anexo_bytes, ler_docx_bytes, ler_txt, ler_zip

falhas = []


def ok(nome, obtido, esperado):
    passou = obtido == esperado
    print(("[OK]" if passou else "[FALHOU]"), nome, obtido, esperado)
    if not passou:
        falhas.append(nome)


def _docx_sintetico(texto1: str, texto2: str) -> bytes:
    """Constrói um .docx mínimo, válido o suficiente para ler_docx_bytes:
    dois parágrafos separados por <w:br/>, exatamente como o Word grava."""
    xml = (
        '<?xml version="1.0"?>'
        "<w:document><w:body><w:p><w:r><w:t>"
        f"{texto1}</w:t><w:br/><w:t>{texto2}"
        "</w:t></w:r></w:p></w:body></w:document>"
    )
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as pacote:
        pacote.writestr("word/document.xml", xml)
    return buffer.getvalue()


def main():
    print("PSF-IAminy — teste de leitura de documentos")

    # .txt, por caminho
    caminho_txt = Path(tempfile.mktemp(suffix=".txt"))
    caminho_txt.write_text("Olá PSF-IAminy", encoding="utf-8")
    try:
        ok("ler_txt", ler_txt(caminho_txt), "Olá PSF-IAminy")
        ok("ler_anexo .txt", ler_anexo(caminho_txt), {caminho_txt.name: "Olá PSF-IAminy"})
    finally:
        caminho_txt.unlink()

    # .docx sintético, por bytes e por caminho
    dados_docx = _docx_sintetico("Primeira linha", "Segunda linha")
    ok("ler_docx_bytes preserva a quebra do <w:br/>", ler_docx_bytes(dados_docx), "Primeira linha\nSegunda linha")

    caminho_docx = Path(tempfile.mktemp(suffix=".docx"))
    caminho_docx.write_bytes(dados_docx)
    try:
        ok("ler_anexo .docx", ler_anexo(caminho_docx), {caminho_docx.name: "Primeira linha\nSegunda linha"})
    finally:
        caminho_docx.unlink()

    ok(
        "ler_anexo_bytes .docx",
        ler_anexo_bytes("anexo.docx", dados_docx),
        {"anexo.docx": "Primeira linha\nSegunda linha"},
    )
    ok("ler_anexo_bytes .txt", ler_anexo_bytes("nota.txt", "olá".encode("utf-8")), {"nota.txt": "olá"})

    # .zip com um .txt e um .docx sintético dentro
    buffer_zip = io.BytesIO()
    with zipfile.ZipFile(buffer_zip, "w") as pacote:
        pacote.writestr("nota.txt", "conteúdo simples")
        pacote.writestr("sub/relatorio.docx", dados_docx)
    dados_zip = buffer_zip.getvalue()

    lido_de_bytes = ler_zip(dados_zip)
    ok("ler_zip (bytes) contém os dois ficheiros", set(lido_de_bytes), {"nota.txt", "sub/relatorio.docx"})
    ok("ler_zip (bytes) txt", lido_de_bytes["nota.txt"], "conteúdo simples")
    ok("ler_zip (bytes) docx interno", lido_de_bytes["sub/relatorio.docx"], "Primeira linha\nSegunda linha")

    caminho_zip = Path(tempfile.mktemp(suffix=".zip"))
    caminho_zip.write_bytes(dados_zip)
    try:
        ok("ler_anexo .zip == ler_zip por caminho", ler_anexo(caminho_zip), lido_de_bytes)
    finally:
        caminho_zip.unlink()

    ok("ler_anexo_bytes .zip", ler_anexo_bytes("pacote.zip", dados_zip), lido_de_bytes)

    # extensão não suportada: erro explícito, não silêncio.
    try:
        ler_anexo_bytes("prova.pdf", b"%PDF-1.4")
        ok("pdf deveria levantar ValueError", "não levantou", "ValueError")
    except ValueError as erro:
        ok("pdf levanta ValueError explicando a lacuna", ".pdf" in str(erro), True)

    if falhas:
        print("FALHAS", falhas)
        raise SystemExit(1)
    print("Tudo passou.")


if __name__ == "__main__":
    main()
