"""Testes de integração HTTP real do PSF-IAminy.

Os testes de `interface/` que já existiam (`test_interface_*.py`) chamam
`Roteador` diretamente, sem socket -- confirmam a lógica, mas nunca o
`http.server` real, o parsing real de query/corpo HTTP, nem os ficheiros
estáticos servidos por cima da rede. Estes testes sobem um
`ThreadingHTTPServer` de verdade numa porta livre e batem via
`http.client`, percorrendo o mesmo caminho que o navegador percorre:
chat (criar conversa, mandar mensagem, apagar), mapa, aulas e treino.

Armazém de conversas isolado em `tmp_path` -- nunca grava em
`interface/dados/conversas/` (dados reais de sessão).
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
        yield httpd.server_address[1]
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
    return resposta.status, resposta.getheader("Content-Type") or "", corpo


def _post(porta, caminho, dados):
    conexao = http.client.HTTPConnection("127.0.0.1", porta, timeout=5)
    corpo = json.dumps(dados).encode("utf-8")
    conexao.request("POST", caminho, body=corpo, headers={"Content-Type": "application/json"})
    resposta = conexao.getresponse()
    corpo_resposta = resposta.read()
    conexao.close()
    return resposta.status, json.loads(corpo_resposta.decode("utf-8"))


def _delete(porta, caminho):
    conexao = http.client.HTTPConnection("127.0.0.1", porta, timeout=5)
    conexao.request("DELETE", caminho)
    resposta = conexao.getresponse()
    resposta.read()
    conexao.close()
    return resposta.status


# ---------------------------------------------------------------------------
# Páginas estáticas servidas de verdade
# ---------------------------------------------------------------------------

def test_pagina_inicial_serve_index_html_real(porta_servidor):
    estado, tipo, corpo = _get(porta_servidor, "/")
    assert estado == 200
    assert "text/html" in tipo
    assert b"PSF-IAminy" in corpo
    assert b'<script src="/estatico/app.js">' in corpo


@pytest.mark.parametrize("pagina", ["mapa.html", "aulas.html", "treinar.html", "index.html"])
def test_paginas_estaticas_reais_tem_rotulos_acessiveis(porta_servidor, pagina):
    estado, tipo, corpo = _get(porta_servidor, "/estatico/" + pagina)
    assert estado == 200
    assert "text/html" in tipo
    texto = corpo.decode("utf-8")
    # cada página real deve ter rótulos acessíveis reais na versão servida ao
    # vivo, não só no ficheiro fonte -- aria-label em todas.
    assert "aria-label=" in texto


@pytest.mark.parametrize("pagina", ["mapa.html", "aulas.html", "treinar.html"])
def test_paginas_com_listas_dinamicas_declaram_role_real(porta_servidor, pagina):
    # estas 3 têm elementos clicáveis que nasceram sem foco/role nativo
    # (div/span) -- o corte de acessibilidade deste ficheiro deu role +
    # tabindex a eles; confirma que isso sobrevive na página servida.
    estado, tipo, corpo = _get(porta_servidor, "/estatico/" + pagina)
    assert estado == 200
    assert "role=" in corpo.decode("utf-8")


def test_index_html_usa_marcos_semanticos_nativos(porta_servidor):
    # index.html não precisa de role= explícito: já usa header/nav/main/
    # aside/footer nativos, que já carregam papel ARIA implícito -- checar
    # role= aqui seria exigir redundância, não acessibilidade real.
    estado, tipo, corpo = _get(porta_servidor, "/estatico/index.html")
    assert estado == 200
    texto = corpo.decode("utf-8")
    for marco in ("<header", "<nav", "<main", "<aside", "<footer"):
        assert marco in texto


def test_mapa_tem_alternativa_por_teclado_ao_grafo_em_canvas(porta_servidor):
    # o grafo em si (canvas, arrastar/zoom/clicar num nó) não é navegável
    # por teclado -- essa é a lacuna documentada em conversa.md/plano. O
    # que este teste confirma é que o caminho alternativo existe de verdade
    # na página servida: botão de alternância, painel de lista, listbox
    # real, e o canvas marcado como aria-hidden (não finge acessibilidade
    # que não tem).
    estado, tipo, corpo = _get(porta_servidor, "/estatico/mapa.html")
    assert estado == 200
    texto = corpo.decode("utf-8")
    assert 'id="btn-lista-view"' in texto
    assert 'id="lista-view"' in texto
    assert 'id="lista-nos"' in texto
    assert 'role="listbox"' in texto
    assert '<canvas id="tela" aria-hidden="true">' in texto


def test_app_js_e_estilo_css_servidos_reais(porta_servidor):
    estado, tipo, _ = _get(porta_servidor, "/estatico/app.js")
    assert estado == 200
    assert "javascript" in tipo
    estado, tipo, _ = _get(porta_servidor, "/estatico/estilo.css")
    assert estado == 200
    assert "css" in tipo


def test_arquivo_fora_da_pasta_estatica_fica_bloqueado(porta_servidor):
    estado, _, _ = _get(porta_servidor, "/estatico/../servidor.py")
    assert estado in (403, 404)


def test_caminho_desconhecido_devolve_404_real(porta_servidor):
    estado, _, _ = _get(porta_servidor, "/isto/nao/existe")
    assert estado == 404


# ---------------------------------------------------------------------------
# Chat -- fluxo real de ponta a ponta (criar, mandar, listar, apagar)
# ---------------------------------------------------------------------------

def test_fluxo_completo_de_chat_via_http_real(porta_servidor):
    estado, corpo = _post(porta_servidor, "/api/conversas", {})
    assert estado == 200
    id_conversa = corpo["id"]

    estado, corpo = _post(
        porta_servidor, f"/api/conversas/{id_conversa}/mensagens", {"texto": "quem é você?"}
    )
    assert estado == 200
    assert corpo["mensagens"][-1]["papel"] == "assistente"
    assert corpo["mensagens"][-1]["texto"]

    estado, tipo, corpo_bruto = _get(porta_servidor, "/api/conversas")
    assert estado == 200
    lista = json.loads(corpo_bruto)["conversas"]
    assert any(c["id"] == id_conversa for c in lista)

    estado = _delete(porta_servidor, f"/api/conversas/{id_conversa}")
    assert estado == 200

    estado, tipo, corpo_bruto = _get(porta_servidor, "/api/conversas")
    lista = json.loads(corpo_bruto)["conversas"]
    assert not any(c["id"] == id_conversa for c in lista)


def test_mensagem_para_conversa_inexistente_404_real(porta_servidor):
    estado, corpo = _post(porta_servidor, "/api/conversas/inexistente/mensagens", {"texto": "oi"})
    assert estado == 404


def test_renomear_conversa_via_http_real_persiste(porta_servidor):
    estado, corpo = _post(porta_servidor, "/api/conversas", {})
    id_conversa = corpo["id"]

    estado, corpo = _post(
        porta_servidor, f"/api/conversas/{id_conversa}/titulo", {"titulo": "  Título novo de verdade  "}
    )
    assert estado == 200
    assert corpo["titulo"] == "Título novo de verdade"

    # persistiu de verdade -- não só na resposta do POST, busca de novo confirma
    estado, tipo, corpo_bruto = _get(porta_servidor, f"/api/conversas/{id_conversa}")
    assert json.loads(corpo_bruto)["titulo"] == "Título novo de verdade"

    estado, tipo, corpo_bruto = _get(porta_servidor, "/api/conversas")
    lista = json.loads(corpo_bruto)["conversas"]
    alvo = next(c for c in lista if c["id"] == id_conversa)
    assert alvo["titulo"] == "Título novo de verdade"


def test_renomear_conversa_com_titulo_vazio_rejeitado(porta_servidor):
    estado, corpo = _post(porta_servidor, "/api/conversas", {})
    id_conversa = corpo["id"]
    estado, corpo = _post(porta_servidor, f"/api/conversas/{id_conversa}/titulo", {"titulo": "   "})
    assert estado == 400


def test_renomear_conversa_inexistente_404_real(porta_servidor):
    estado, corpo = _post(porta_servidor, "/api/conversas/inexistente/titulo", {"titulo": "x"})
    assert estado == 404


def test_apagar_conversa_e_permanente_de_verdade(porta_servidor):
    # "de verdade" = depois de apagar, a conversa não existe mais em
    # nenhuma leitura -- não é só sumir da lista, é 404 real ao buscar
    # o recurso direto, e não reaparece se a lista for pedida de novo.
    estado, corpo = _post(porta_servidor, "/api/conversas", {})
    id_conversa = corpo["id"]

    estado = _delete(porta_servidor, f"/api/conversas/{id_conversa}")
    assert estado == 200

    estado, _, _ = _get(porta_servidor, f"/api/conversas/{id_conversa}")
    assert estado == 404

    estado = _delete(porta_servidor, f"/api/conversas/{id_conversa}")
    assert estado == 404  # apagar de novo não "reencontra" nada -- já não existe


# ---------------------------------------------------------------------------
# Mapa -- rota real
# ---------------------------------------------------------------------------

def test_mapa_api_real(porta_servidor):
    estado, tipo, corpo = _get(porta_servidor, "/api/mapa")
    assert estado == 200
    assert "json" in tipo
    dados = json.loads(corpo)
    assert dados["pt"]["nodes"]
    assert dados["mat"]["nodes"]


# ---------------------------------------------------------------------------
# Aulas + treino -- fluxo real de ponta a ponta (listar, abrir, verificar)
# ---------------------------------------------------------------------------

def test_fluxo_completo_de_aula_e_verificacao_via_http_real(porta_servidor):
    estado, tipo, corpo = _get(porta_servidor, "/api/aulas/matematica")
    assert estado == 200
    pacotes = json.loads(corpo)["pacotes"]
    assert pacotes
    codigo = pacotes[0]["codigo"]

    estado, tipo, corpo = _get(porta_servidor, "/api/aulas/matematica/" + codigo)
    assert estado == 200
    dados = json.loads(corpo)
    assert dados["aulas"]
    aula = dados["aulas"][0]
    assert aula["texto"]

    if not aula["exercicios"]:
        pytest.skip("primeiro pacote real de matemática não tem exercício -- sem dependência suficiente")
    exercicio = aula["exercicios"][0]

    estado, corpo = _post(
        porta_servidor,
        "/api/aulas/verificar",
        {"area": "matematica", "conceito": aula["conceito"], "tipo": exercicio["tipo"], "resposta": "qualquer coisa"},
    )
    assert estado == 200
    assert "correto" in corpo
    assert "resposta_modelo" in corpo


def test_pacote_inexistente_404_real(porta_servidor):
    estado, _, _ = _get(porta_servidor, "/api/aulas/matematica/NAO-EXISTE")
    assert estado == 404


def test_problemas_abertos_via_http_real(porta_servidor):
    estado, tipo, corpo = _get(porta_servidor, "/api/problemas-abertos")
    assert estado == 200
    dados = json.loads(corpo)
    assert dados["total"] > 0
    assert dados["problemas"][0]["estado"]
