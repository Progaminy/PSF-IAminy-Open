"""Testes de segurança do armazém de conversas (item 22/23 do plano de
melhorias públicas: auditar e testar caminhos controlados pelo utilizador).

Achado real desta auditoria: `id_conversa` (vindo direto da URL, ex.
`/api/conversas/{id}`) era concatenado sem validação em
`self.pasta / f"{id_conversa}.json"` (`interface/conversas.py`), ao
contrário do servidor de ficheiros estáticos, que já confere que o
caminho resolvido continua dentro da pasta permitida. Um `id_conversa`
como `"../../../algo"` conseguiria ler, apagar ou (mais restrito) escrever
fora da pasta de conversas. Corrigido validando que `id_conversa` bate
exatamente no formato produzido por `secrets.token_hex(6)` antes de montar
qualquer caminho -- qualquer outra coisa é tratada como inexistente.

Estes testes falhavam antes da correção (confirmado rodando contra o
código anterior a esta auditoria) e passam depois dela.
"""
from __future__ import annotations

import http.client
import json
import threading
from http.server import ThreadingHTTPServer

import pytest

from interface import servidor
from interface.conversas import ArmazemConversas
from interface.roteador import Roteador


@pytest.fixture()
def porta_servidor(tmp_path, monkeypatch):
    armazem_teste = ArmazemConversas(pasta=tmp_path / "conversas")
    monkeypatch.setattr(servidor, "roteador", Roteador(armazem=armazem_teste))
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Manipulador)
    fio = threading.Thread(target=httpd.serve_forever, daemon=True)
    fio.start()
    try:
        yield httpd.server_address[1], tmp_path
    finally:
        httpd.shutdown()
        httpd.server_close()
        fio.join(timeout=2)


def _get(porta, caminho):
    conexao = http.client.HTTPConnection("127.0.0.1", porta, timeout=5)
    conexao.request("GET", caminho)
    resposta = conexao.getresponse()
    corpo = resposta.read()
    conexao.close()
    return resposta.status, corpo


def _delete(porta, caminho):
    conexao = http.client.HTTPConnection("127.0.0.1", porta, timeout=5)
    conexao.request("DELETE", caminho)
    resposta = conexao.getresponse()
    resposta.read()
    conexao.close()
    return resposta.status


def _post(porta, caminho, dados):
    conexao = http.client.HTTPConnection("127.0.0.1", porta, timeout=5)
    corpo = json.dumps(dados).encode("utf-8")
    conexao.request("POST", caminho, body=corpo, headers={"Content-Type": "application/json"})
    resposta = conexao.getresponse()
    corpo_resposta = resposta.read()
    conexao.close()
    return resposta.status, corpo_resposta


_CAMINHOS_TRAVESSIA = (
    "../../../../etc/passwd",
    "..%2f..%2f..%2fetc%2fpasswd",
    "....//....//....//etc/passwd",
    "/etc/passwd",
)


@pytest.mark.parametrize("id_malicioso", _CAMINHOS_TRAVESSIA)
def test_ler_conversa_com_travessia_de_caminho_nao_expoe_ficheiro(porta_servidor, id_malicioso):
    porta, _ = porta_servidor
    estado, corpo = _get(porta, f"/api/conversas/{id_malicioso}")
    assert estado == 404
    assert b"root:" not in corpo


def test_ler_conversa_com_travessia_nao_expoe_ficheiro_irmao_real(porta_servidor):
    """Prova concreta, não coincidência de 404: com o bug (`_caminho` sem
    validação), este exato payload lia de verdade o ficheiro fora da pasta
    de conversas -- confirmado rodando contra o código anterior à correção.
    """
    porta, pasta_tmp = porta_servidor
    alvo_irmao = pasta_tmp / "arquivo_sensivel.json"
    alvo_irmao.write_text('{"segredo": true}', encoding="utf-8")

    estado, corpo = _get(porta, "/api/conversas/../arquivo_sensivel")
    assert estado == 404
    assert b"segredo" not in corpo


@pytest.mark.parametrize("id_malicioso", _CAMINHOS_TRAVESSIA)
def test_apagar_conversa_com_travessia_de_caminho_nao_apaga_nada_fora_da_pasta(porta_servidor, id_malicioso, tmp_path):
    porta, pasta_tmp = porta_servidor
    alvo_fora_da_pasta = tmp_path / "arquivo_sensivel.json"
    alvo_fora_da_pasta.write_text('{"segredo": true}', encoding="utf-8")

    estado = _delete(porta, f"/api/conversas/{id_malicioso}")
    assert estado == 404
    assert alvo_fora_da_pasta.exists()


def test_apagar_conversa_com_travessia_nao_apaga_ficheiro_irmao_real(porta_servidor):
    """Mesma prova concreta que o teste de leitura, para o `remover()`:
    com o bug, `DELETE /api/conversas/../arquivo_sensivel` apagava de
    verdade o ficheiro fora da pasta de conversas.
    """
    porta, pasta_tmp = porta_servidor
    alvo_irmao = pasta_tmp / "arquivo_sensivel.json"
    alvo_irmao.write_text('{"segredo": true}', encoding="utf-8")

    estado = _delete(porta, "/api/conversas/../arquivo_sensivel")
    assert estado == 404
    assert alvo_irmao.exists()


def test_criar_conversa_e_ler_com_id_real_continua_funcionando(porta_servidor):
    porta, _ = porta_servidor
    estado, corpo = _post(porta, "/api/conversas", {})
    assert estado == 200
    id_conversa = json.loads(corpo)["id"]

    estado, corpo = _get(porta, f"/api/conversas/{id_conversa}")
    assert estado == 200
    assert json.loads(corpo)["id"] == id_conversa


def test_armazem_recusa_id_fora_do_formato_esperado_sem_tocar_disco(tmp_path):
    armazem = ArmazemConversas(pasta=tmp_path / "conversas")
    assert armazem.carregar("../../../etc/passwd") is None
    assert armazem.remover("../../../etc/passwd") is False
    assert armazem._caminho("../../../etc/passwd") is None
    assert armazem._caminho("id-com-formato-errado") is None
