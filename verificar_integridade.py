#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificação local de integridade do pacote PSF-IAminy."""
from pathlib import Path
import importlib
import sys

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

OBRIGATORIOS = [
    'README.md', 'main.py', 'psf.py', 'caixa.py', 'motor_iaminy.py',
    'conhecimento', 'ensino', 'interface', 'lingua_portuguesa', 'modelos',
    'motor', 'nucleo', 'privado', 'testes', 'validacao_externa'
]

MODULOS = [
    'nucleo.cerebro_unico',
    'nucleo.motor_mestre',
    'nucleo.plano_mae',
    'nucleo.ponte_comparador_python',
    'validacao_externa.motor_calculo_python',
    'validacao_externa.motor_auxiliar',
    'matematica.divisao',
    'matematica.hipoteses',
]


def main():
    falhas = []
    for item in OBRIGATORIOS:
        if not (ROOT / item).exists():
            falhas.append(f'ausente: {item}')
    for mod in MODULOS:
        try:
            importlib.import_module(mod)
        except Exception as e:
            falhas.append(f'import falhou: {mod}: {e}')
    try:
        from nucleo.cerebro_unico import responder_com_cerebro_unico
        r = responder_com_cerebro_unico('Quem é você?')
        if not isinstance(r, dict) or 'resposta_base' not in r:
            falhas.append('cerebro_unico não devolveu resposta válida')
    except Exception as e:
        falhas.append(f'cerebro_unico falhou: {e}')

    print('=== VERIFICAÇÃO PSF-IAminy ===')
    if falhas:
        print('REPROVADO')
        for f in falhas:
            print('-', f)
        return 1
    print('APROVADO')
    print('Estrutura base restaurada, pasta privado presente, README presente, main.py executável, módulos recentes importáveis.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
