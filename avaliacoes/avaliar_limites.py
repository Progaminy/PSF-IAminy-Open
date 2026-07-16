#!/usr/bin/env python3
"""Avalia limites operacionais em subprocessos com timeout controlado."""
from __future__ import annotations

import argparse
import http.client
import json
from pathlib import Path
import subprocess
import sys
import threading
from time import perf_counter

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))


def executar_cenario(nome: str) -> dict:
    inicio = perf_counter()
    try:
        processo = subprocess.run(
            [sys.executable, __file__, "--worker", nome],
            cwd=RAIZ,
            text=True,
            capture_output=True,
            timeout=10,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {"cenario": nome, "estado": "TIMEOUT_10S", "segundos": 10.0}
    segundos = round(perf_counter() - inicio, 3)
    if processo.returncode != 0:
        return {
            "cenario": nome,
            "estado": "ERRO",
            "segundos": segundos,
            "stderr": processo.stderr[-500:],
        }
    return {
        "cenario": nome,
        "estado": "CONCLUIDO",
        "segundos": segundos,
        "resultado": json.loads(processo.stdout),
    }


def worker(nome: str) -> dict:
    if nome.startswith("matematica_"):
        from matematica import MotorMatematica

        expressoes = {
            "matematica_20_vezes_20": "20*20",
            "matematica_99_vezes_99": "99*99",
            "matematica_999_vezes_999": "999*999",
            "matematica_grande": "999999999*999999999",
            "matematica_20_termos": "+".join(["1"] * 20),
            "matematica_100_termos": "+".join(["1"] * 100),
        }
        resolucao = MotorMatematica().calcular(expressoes[nome])
        return {"estado": resolucao.estado, "resultado": resolucao.resultado}

    if nome == "portugues_texto_500_palavras":
        from lingua_portuguesa.corretor import Corretor

        texto = " ".join(["casa", "bonita"] * 250) + "."
        resultado = Corretor().corrigir_texto(texto)
        return {
            "caracteres": len(texto),
            "palavras": 500,
            "sugestoes": len(resultado.sugestoes_ortografia),
        }

    if nome == "http_100_requisicoes":
        from http.server import ThreadingHTTPServer
        from interface import servidor

        httpd = ThreadingHTTPServer(("127.0.0.1", 0), servidor.Manipulador)
        fio = threading.Thread(target=httpd.serve_forever, daemon=True)
        fio.start()
        estados = []
        try:
            porta = httpd.server_address[1]
            for _ in range(100):
                conexao = http.client.HTTPConnection("127.0.0.1", porta, timeout=5)
                conexao.request("GET", "/")
                resposta = conexao.getresponse()
                resposta.read()
                estados.append(resposta.status)
                conexao.close()
        finally:
            httpd.shutdown()
            httpd.server_close()
            fio.join(timeout=2)
        return {"requisicoes": len(estados), "todas_200": all(e == 200 for e in estados)}

    if nome == "anexo_formato_invalido":
        from ensino.leitura_documentos import ler_anexo_bytes

        try:
            ler_anexo_bytes("entrada.pdf", b"%PDF-1.4")
        except ValueError as erro:
            return {"rejeitado": True, "erro": str(erro)}
        return {"rejeitado": False}

    raise ValueError(f"cenário desconhecido: {nome}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", choices=(
        "matematica_20_vezes_20", "matematica_99_vezes_99", "matematica_999_vezes_999", "matematica_grande", "matematica_20_termos",
        "matematica_100_termos", "portugues_texto_500_palavras",
        "http_100_requisicoes", "anexo_formato_invalido",
    ))
    args = parser.parse_args()
    if args.worker:
        print(json.dumps(worker(args.worker), ensure_ascii=False))
        return 0

    cenarios = (
        "matematica_20_vezes_20", "matematica_99_vezes_99", "matematica_999_vezes_999", "matematica_grande", "matematica_20_termos",
        "matematica_100_termos", "portugues_texto_500_palavras",
        "http_100_requisicoes", "anexo_formato_invalido",
    )
    resultados = [executar_cenario(nome) for nome in cenarios]
    print(json.dumps({"timeout_segundos": 10, "resultados": resultados}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
