"""Servidor HTTP do PSF-IAminy -- interface de chat.

Só biblioteca padrão (`http.server`) -- sem Flask/FastAPI, decisão já
tomada com o utilizador. Este ficheiro é só a casca fina que liga pedidos
HTTP ao `Roteador` (lógica pura, testada sem socket em
`testes/test_interface_servidor.py`).

Uso: python3 -m interface.servidor [porta]
Sem porta, usa 8765.
"""
from __future__ import annotations

import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

from .roteador import Roteador

_PREFIXO_CONVERSAS = "/api/conversas/"

# Sem limite, um Content-Length forjado e enorme faria o servidor tentar ler
# (e manter em memória) um corpo arbitrariamente grande antes de qualquer
# validação -- item 22/23 do plano de melhorias públicas ("payload muito
# grande"). 1 MB é generoso para texto de chat/JSON; anexos usam
# conteúdo_base64, que já cresce ~33% sobre o ficheiro original.
TAMANHO_MAXIMO_CORPO = 1_000_000

roteador = Roteador()


class CorpoMuitoGrande(Exception):
    pass


class CorpoInvalido(Exception):
    pass


class Manipulador(BaseHTTPRequestHandler):
    def _corpo_json(self) -> dict:
        try:
            tamanho = int(self.headers.get("Content-Length", 0) or 0)
        except (TypeError, ValueError) as erro:
            raise CorpoInvalido("Content-Length inválido") from erro
        if tamanho < 0:
            raise CorpoInvalido("Content-Length não pode ser negativo")
        if tamanho > TAMANHO_MAXIMO_CORPO:
            raise CorpoMuitoGrande(tamanho)
        bruto = self.rfile.read(tamanho) if tamanho else b""
        if not bruto:
            return {}
        try:
            corpo = json.loads(bruto.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as erro:
            raise CorpoInvalido("corpo não é JSON UTF-8 válido") from erro
        if not isinstance(corpo, dict):
            raise CorpoInvalido("corpo JSON deve ser um objeto")
        return corpo

    def _responder_json(self, estado: int, corpo: dict) -> None:
        dados = json.dumps(corpo, ensure_ascii=False).encode("utf-8")
        self._responder_bytes(estado, "application/json; charset=utf-8", dados)

    def _responder_bytes(self, estado: int, tipo: str, corpo: bytes) -> None:
        self.send_response(estado)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def do_GET(self) -> None:  # noqa: N802 -- nome exigido por BaseHTTPRequestHandler
        caminho = urlparse(self.path).path
        if caminho == "/":
            self._responder_bytes(*roteador.pagina_inicial())
        elif caminho.startswith("/estatico/"):
            self._responder_bytes(*roteador.arquivo_estatico(caminho[len("/estatico/"):]))
        elif caminho == "/api/conversas":
            self._responder_json(*roteador.listar_conversas())
        elif caminho.startswith(_PREFIXO_CONVERSAS):
            id_conversa = caminho[len(_PREFIXO_CONVERSAS):]
            self._responder_json(*roteador.obter_conversa(id_conversa))
        elif caminho == "/api/mapa":
            self._responder_json(*roteador.mapa_conhecimento())
        elif caminho.startswith("/api/aulas/"):
            resto = caminho[len("/api/aulas/"):].split("/", 1)
            if len(resto) == 1:
                self._responder_json(*roteador.listar_aulas(resto[0]))
            else:
                area, codigo = resto
                self._responder_json(*roteador.obter_pacote(area, codigo))
        elif caminho.startswith("/api/navegar/onde/"):
            resto = caminho[len("/api/navegar/onde/"):].split("/", 1)
            if len(resto) == 2:
                self._responder_json(*roteador.onde_estou(resto[0], unquote(resto[1])))
            else:
                self._responder_bytes(400, "text/plain; charset=utf-8", b"faltam parametros")
        elif caminho.startswith("/api/navegar/componentes/"):
            area = caminho[len("/api/navegar/componentes/"):]
            self._responder_json(*roteador.componentes(area))
        elif caminho.startswith("/api/navegar/caminho/"):
            area = caminho[len("/api/navegar/caminho/"):]
            consulta = parse_qs(urlparse(self.path).query)
            origem = consulta.get("origem", [""])[0]
            destino = consulta.get("destino", [""])[0]
            modo = consulta.get("modo", ["curto"])[0]
            self._responder_json(*roteador.navegar(area, origem, destino, modo))
        elif caminho == "/api/problemas-abertos":
            self._responder_json(*roteador.problemas_abertos())
        else:
            self._responder_bytes(404, "text/plain; charset=utf-8", b"nao encontrado")

    def do_POST(self) -> None:  # noqa: N802
        caminho = urlparse(self.path).path
        try:
            corpo = self._corpo_json()
        except CorpoMuitoGrande:
            self._responder_bytes(413, "text/plain; charset=utf-8", b"corpo do pedido excede o limite permitido")
            return
        except CorpoInvalido as erro:
            self._responder_json(400, {"erro": str(erro)})
            return
        if caminho == "/api/conversas":
            self._responder_json(*roteador.criar_conversa())
        elif caminho == "/api/aulas/verificar":
            self._responder_json(*roteador.verificar_exercicio(
                corpo.get("area", ""), corpo.get("conceito", ""),
                corpo.get("tipo", ""), corpo.get("resposta", ""),
            ))
        elif caminho.startswith(_PREFIXO_CONVERSAS) and caminho.endswith("/mensagens"):
            id_conversa = caminho[len(_PREFIXO_CONVERSAS):-len("/mensagens")]
            self._responder_json(*roteador.enviar_mensagem(id_conversa, corpo.get("texto", "")))
        elif caminho.startswith(_PREFIXO_CONVERSAS) and caminho.endswith("/anexos"):
            id_conversa = caminho[len(_PREFIXO_CONVERSAS):-len("/anexos")]
            self._responder_json(
                *roteador.enviar_anexo(id_conversa, corpo.get("nome", "anexo"), corpo.get("conteudo_base64", ""))
            )
        elif caminho.startswith(_PREFIXO_CONVERSAS) and caminho.endswith("/titulo"):
            id_conversa = caminho[len(_PREFIXO_CONVERSAS):-len("/titulo")]
            self._responder_json(*roteador.renomear_conversa(id_conversa, corpo.get("titulo", "")))
        else:
            self._responder_bytes(404, "text/plain; charset=utf-8", b"nao encontrado")

    def do_DELETE(self) -> None:  # noqa: N802
        caminho = urlparse(self.path).path
        if caminho.startswith(_PREFIXO_CONVERSAS):
            id_conversa = caminho[len(_PREFIXO_CONVERSAS):]
            self._responder_json(*roteador.remover_conversa(id_conversa))
        else:
            self._responder_bytes(404, "text/plain; charset=utf-8", b"nao encontrado")

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002 -- assinatura da base
        pass


def main(argv: "list[str] | None" = None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    porta = int(argv[0]) if argv else 8765
    servidor = ThreadingHTTPServer(("127.0.0.1", porta), Manipulador)
    print(f"PSF-IAminy a correr em http://127.0.0.1:{porta}  (Ctrl+C para parar)")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        servidor.server_close()


if __name__ == "__main__":
    main()
