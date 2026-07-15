#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Entrada oficial do Chat Vivo PSF-IAminy."""

from nucleo.chat_vivo import RespostaChat, responder

__all__ = ["RespostaChat", "responder"]



def _main_cli(argv=None):
    """Permite rodar: python3 psf_chat.py "quem é você?"."""
    import json
    import sys
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print('Como usar:')
        print('  python3 psf_chat.py "quem é você?"')
        print('  python3 psf_chat.py --json "quem é você?"')
        print('  python3 psf_chat.py --diagnostico')
        return 0
    if args == ['--diagnostico']:
        casos = (
            'quem é você?',
            'o que é palavra?',
            'explique matemática sem fingir',
        )
        falhas = []
        for caso in casos:
            try:
                r = responder(caso, registrar=False)
                if not getattr(r, 'texto', ''):
                    falhas.append(caso)
            except Exception as erro:  # diagnóstico local, sem dependência de scripts apagados
                falhas.append(f'{caso}: {erro}')
        if falhas:
            print('DIAGNOSTICO FALHOU')
            for falha in falhas:
                print('-', falha)
            return 1
        print('DIAGNOSTICO APROVADO')
        print('Chat Vivo importável e respondendo sem depender de scripts externos.')
        return 0
    saida_json = False
    if args and args[0] == '--json':
        saida_json = True
        args = args[1:]
    if not args:
        print('Falta a pergunta depois de --json.')
        return 2
    pergunta = " ".join(args)
    r = responder(pergunta)
    if saida_json:
        print(json.dumps(r.como_dict(), ensure_ascii=False, indent=2))
        return 0
    print(r.texto)
    if getattr(r, 'origem', None):
        print(f"\nOrigem: {r.origem}")
    print(f"Confiança: {r.confianca}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main_cli())
