"""Teste de segurança do servidor HTTP (item 22/23 do plano de melhorias
públicas: payload muito grande).

Achado real desta auditoria: `Manipulador._corpo_json()` lia
`self.rfile.read(tamanho)` usando o `Content-Length` declarado pelo
cliente, sem nenhum limite -- um cliente poderia declarar um
Content-Length enorme e forçar o servidor a tentar ler (e manter em
memória) um corpo arbitrariamente grande antes de qualquer validação.
Corrigido com `TAMANHO_MAXIMO_CORPO` (1 MB): um Content-Length maior
devolve 413 sem tocar em `rfile.read`.
"""
from __future__ import annotations

import http.client
import threading
from http.server import ThreadingHTTPServer

import pytest

from interface import servidor


@pytest.fixture()
def porta_servidor():
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Manipulador)
    fio = threading.Thread(target=httpd.serve_forever, daemon=True)
    fio.start()
    try:
        yield httpd.server_address[1]
    finally:
        httpd.shutdown()
        httpd.server_close()
        fio.join(timeout=2)


def test_content_length_acima_do_limite_e_rejeitado_sem_ler_o_corpo(porta_servidor):
    conexao = http.client.HTTPConnection("127.0.0.1", porta_servidor, timeout=5)
    conexao.request(
        "POST",
        "/api/conversas",
        body=b"",
        headers={
            "Content-Length": str(servidor.TAMANHO_MAXIMO_CORPO + 1),
            "Content-Type": "application/json",
        },
    )
    resposta = conexao.getresponse()
    corpo = resposta.read()
    conexao.close()
    assert resposta.status == 413
    assert corpo


def test_content_length_dentro_do_limite_continua_funcionando(porta_servidor):
    conexao = http.client.HTTPConnection("127.0.0.1", porta_servidor, timeout=5)
    conexao.request("POST", "/api/conversas", body=b"{}", headers={"Content-Type": "application/json"})
    resposta = conexao.getresponse()
    resposta.read()
    conexao.close()
    assert resposta.status == 200


@pytest.mark.parametrize("corpo", (b"{", b"\xff", b"[]"))
def test_corpo_malformado_devolve_400_sem_encerrar_conexao(porta_servidor, corpo):
    conexao = http.client.HTTPConnection("127.0.0.1", porta_servidor, timeout=5)
    conexao.request(
        "POST",
        "/api/conversas",
        body=corpo,
        headers={"Content-Type": "application/json"},
    )
    resposta = conexao.getresponse()
    resposta_json = resposta.read().decode("utf-8")
    conexao.close()
    assert resposta.status == 400
    assert '"erro"' in resposta_json
