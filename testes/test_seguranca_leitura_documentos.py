"""Limites de segurança para anexos ZIP/DOCX.

Os limites são reduzidos com monkeypatch para manter os casos rápidos: o
comportamento exercitado é o mesmo usado com os valores reais em produção.
"""

from __future__ import annotations

import io
import zipfile
from collections.abc import Iterable

import pytest

import ensino.leitura_documentos as leitura


_XML_MINIMO = (
    b'<?xml version="1.0"?>'
    b"<w:document><w:body><w:p><w:r><w:t>seguro</w:t>"
    b"</w:r></w:p></w:body></w:document>"
)


def _criar_zip(
    entradas: Iterable[tuple[str, bytes | str]],
    *,
    compressao: int = zipfile.ZIP_STORED,
) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=compressao) as pacote:
        for nome, dados in entradas:
            pacote.writestr(nome, dados)
    return buffer.getvalue()


def _criar_docx(
    *,
    xml: bytes = _XML_MINIMO,
    extras: Iterable[tuple[str, bytes | str]] = (),
    compressao: int = zipfile.ZIP_STORED,
) -> bytes:
    return _criar_zip(
        [("word/document.xml", xml), *extras],
        compressao=compressao,
    )


def test_zip_seguro_continua_aceitando_subdiretorios() -> None:
    dados = _criar_zip([("turma/notas.txt", "Aprovado")])

    assert leitura.ler_zip(dados) == {"turma/notas.txt": "Aprovado"}


def test_zip_rejeita_tamanho_compactado_excessivo(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    dados = _criar_zip([("nota.txt", "texto")])
    monkeypatch.setattr(leitura, "_MAX_BYTES_COMPACTADOS", len(dados) - 1)

    with pytest.raises(ValueError, match=r"arquivo ZIP inseguro.*tamanho compactado"):
        leitura.ler_zip(dados)


def test_docx_por_caminho_rejeita_tamanho_antes_de_abrir_zip(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path,
) -> None:
    caminho = tmp_path / "grande.docx"
    caminho.write_bytes(b"nao e necessario abrir")
    monkeypatch.setattr(leitura, "_MAX_BYTES_COMPACTADOS", caminho.stat().st_size - 1)

    with pytest.raises(
        ValueError,
        match=r"arquivo DOCX inseguro.*tamanho compactado",
    ):
        leitura.ler_docx(caminho)


@pytest.mark.parametrize("tipo", ["ZIP", "DOCX"])
def test_rejeita_quantidade_excessiva_de_entradas(
    monkeypatch: pytest.MonkeyPatch,
    tipo: str,
) -> None:
    monkeypatch.setattr(leitura, "_MAX_ENTRADAS_ZIP", 2)
    if tipo == "ZIP":
        dados = _criar_zip(
            [("a.txt", "a"), ("b.txt", "b"), ("c.txt", "c")],
        )
        leitor = leitura.ler_zip
    else:
        dados = _criar_docx(extras=[("a.bin", b"a"), ("b.bin", b"b")])
        leitor = leitura.ler_docx_bytes

    with pytest.raises(
        ValueError,
        match=rf"arquivo {tipo} inseguro.*3 entradas.*limite é 2",
    ):
        leitor(dados)


@pytest.mark.parametrize("tipo", ["ZIP", "DOCX"])
def test_rejeita_entrada_individual_descomprimida_excessiva(
    monkeypatch: pytest.MonkeyPatch,
    tipo: str,
) -> None:
    monkeypatch.setattr(leitura, "_MAX_BYTES_POR_ENTRADA", 4)
    if tipo == "ZIP":
        dados = _criar_zip([("grande.txt", b"12345")])
        leitor = leitura.ler_zip
    else:
        dados = _criar_docx(xml=b"12345")
        leitor = leitura.ler_docx_bytes

    with pytest.raises(
        ValueError,
        match=rf"arquivo {tipo} inseguro.*limite por entrada",
    ):
        leitor(dados)


@pytest.mark.parametrize("tipo", ["ZIP", "DOCX"])
def test_rejeita_total_descomprimido_excessivo(
    monkeypatch: pytest.MonkeyPatch,
    tipo: str,
) -> None:
    monkeypatch.setattr(leitura, "_MAX_BYTES_POR_ENTRADA", 10)
    monkeypatch.setattr(leitura, "_MAX_BYTES_DESCOMPRIMIDOS", 8)
    if tipo == "ZIP":
        dados = _criar_zip([("a.txt", b"12345"), ("ignorado.bin", b"67890")])
        leitor = leitura.ler_zip
    else:
        dados = _criar_docx(xml=b"12345", extras=[("ignorado.bin", b"67890")])
        leitor = leitura.ler_docx_bytes

    with pytest.raises(
        ValueError,
        match=rf"arquivo {tipo} inseguro.*tamanho total declarado",
    ):
        leitor(dados)


@pytest.mark.parametrize("tipo", ["ZIP", "DOCX"])
def test_rejeita_razao_de_compactacao_de_zip_bomb(
    monkeypatch: pytest.MonkeyPatch,
    tipo: str,
) -> None:
    monkeypatch.setattr(leitura, "_MIN_BYTES_PARA_VALIDAR_RAZAO", 1)
    monkeypatch.setattr(leitura, "_MAX_RAZAO_COMPACTACAO", 2.0)
    if tipo == "ZIP":
        dados = _criar_zip(
            [("repetido.txt", b"A" * 2048)],
            compressao=zipfile.ZIP_DEFLATED,
        )
        leitor = leitura.ler_zip
    else:
        dados = _criar_docx(
            xml=b"A" * 2048,
            compressao=zipfile.ZIP_DEFLATED,
        )
        leitor = leitura.ler_docx_bytes

    with pytest.raises(
        ValueError,
        match=rf"arquivo {tipo} inseguro.*possível ZIP bomb",
    ):
        leitor(dados)


@pytest.mark.parametrize(
    "nome",
    [
        pytest.param("../segredo.txt", id="travessia"),
        pytest.param("/segredo.txt", id="absoluto-posix"),
        pytest.param("C:/segredo.txt", id="absoluto-windows"),
        pytest.param(r"pasta\segredo.txt", id="separador-windows"),
    ],
)
def test_zip_rejeita_caminho_interno_perigoso(nome: str) -> None:
    dados = _criar_zip([(nome, "segredo")])

    with pytest.raises(ValueError, match=r"arquivo ZIP inseguro.*caminho interno"):
        leitura.ler_zip(dados)


def test_docx_rejeita_caminho_perigoso_mesmo_em_entrada_nao_lida() -> None:
    dados = _criar_docx(extras=[("../segredo.bin", b"segredo")])

    with pytest.raises(ValueError, match=r"arquivo DOCX inseguro.*travessia"):
        leitura.ler_docx_bytes(dados)


def test_zip_rejeita_nomes_duplicados() -> None:
    with pytest.warns(UserWarning, match="Duplicate name"):
        dados = _criar_zip([("nota.txt", "primeira"), ("nota.txt", "segunda")])

    with pytest.raises(ValueError, match=r"arquivo ZIP inseguro.*entrada duplicada"):
        leitura.ler_zip(dados)


def test_zip_externo_aplica_limites_ao_docx_interno(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(leitura, "_MIN_BYTES_PARA_VALIDAR_RAZAO", 1)
    monkeypatch.setattr(leitura, "_MAX_RAZAO_COMPACTACAO", 5.0)
    docx_bomba = _criar_docx(
        xml=b"A" * 4096,
        compressao=zipfile.ZIP_DEFLATED,
    )
    dados = _criar_zip([("interno.docx", docx_bomba)])

    with pytest.raises(
        ValueError,
        match=r"arquivo DOCX inseguro.*possível ZIP bomb",
    ):
        leitura.ler_zip(dados)
