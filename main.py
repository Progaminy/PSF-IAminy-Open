#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Entrada principal simples do PSF-IAminy.
Roda sem dependências pip externas.
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def responder(pergunta: str, modo: str = 'normal'):
    try:
        from psf_chat import responder as responder_chat
        vivo = responder_chat(pergunta, modo=modo)
        nivel = 'alta' if vivo.confianca >= 85 else ('média' if vivo.confianca >= 60 else 'baixa')
        return {
            'modo': modo,
            'tipo': {'principal': vivo.intencao, 'tom': vivo.tom},
            'resposta_base': vivo.texto,
            'confianca': {'score': vivo.confianca, 'nivel': nivel},
            'proximo_passo': 'resposta entregue pela entrada única psf_chat.responder',
            'auditoria': {
                'modo_cientista_aplicado': True,
                'dependencias_proibidas': [],
                'contradicoes': [],
                'faltas_cobertura': vivo.lacunas,
                'fallback_usado': vivo.fallback_usado,
                'origem': vivo.origem,
            },
        }
    except Exception as e:
        return {
            'erro': 'falha_ao_chamar_chat_vivo',
            'detalhe': str(e),
            'pergunta': pergunta,
            'resposta_base': 'O PSF recebeu a pergunta, mas o Chat Vivo não carregou. Rode verificar_integridade.py para localizar a falha.'
        }


def imprimir_humano(r):
    print('\n=== PSF-IAminy ===')
    if r.get('erro'):
        print('Erro:', r.get('erro'))
        print('Detalhe:', r.get('detalhe'))
        print(r.get('resposta_base'))
        return
    print('Tipo:', r.get('tipo', {}).get('principal'))
    print('Resposta:', r.get('resposta_base'))
    conf = r.get('confianca', {})
    print('Confiança:', conf.get('score'), conf.get('nivel'))
    print('Próximo passo:', r.get('proximo_passo'))
    aud = r.get('auditoria', {})
    if aud.get('dependencias_proibidas') or aud.get('contradicoes') or aud.get('faltas_cobertura'):
        print('Auditoria:', json.dumps(aud, ensure_ascii=False, indent=2))


def main():
    ap = argparse.ArgumentParser(description='PSF-IAminy — execução local')
    ap.add_argument('--pergunta', '-p', help='Pergunta para o cérebro único')
    ap.add_argument('--modo', default='normal', help='normal, pronta, curta, media, linha')
    ap.add_argument('--json', action='store_true', help='mostrar saída completa em JSON')
    ap.add_argument('--selftest', action='store_true', help='rodar teste rápido de importação e resposta')
    args = ap.parse_args()

    if args.selftest:
        pergunta = 'Quem é você e o que está pendente?'
    else:
        pergunta = args.pergunta

    if not pergunta:
        print('Como usar:')
        print('  python3 main.py --pergunta "Quem é você?"')
        print('  python3 main.py --selftest')
        return 0

    r = responder(pergunta, modo=args.modo)
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        imprimir_humano(r)
    return 0 if not r.get('erro') else 1

if __name__ == '__main__':
    raise SystemExit(main())
