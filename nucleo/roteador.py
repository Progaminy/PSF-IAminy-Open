# -*- coding: utf-8 -*-
"""
Etapa 64 — Roteador Vivo com Índice Total.

A Etapa 63 corrigiu apenas a base real das 300 curiosidades. Esta etapa remove
o limite: toda pergunta natural passa primeiro pela base viva direta e depois,
se necessário, pelo índice total de todos os ficheiros materializados no projeto.
"""
from __future__ import annotations
from dataclasses import dataclass

from nucleo.roteador_base_curiosidades import dividir_perguntas, responder_uma as responder63_uma
from nucleo.indexador_total import responder_por_indice_total, estatisticas

@dataclass(frozen=True, slots=True)
class ResultadoRoteadorVivo64:
    reconhecido: bool
    texto: str
    intencao: str = 'roteador_vivo'


def responder_uma(entrada: str) -> ResultadoRoteadorVivo64:
    r63 = responder63_uma(entrada)
    if r63.reconhecido and r63.intencao != 'pergunta_nova':
        return ResultadoRoteadorVivo64(True, r63.texto, r63.intencao)
    achado = responder_por_indice_total(entrada)
    if achado:
        return ResultadoRoteadorVivo64(True, achado, 'indice_total_etapa64')
    return ResultadoRoteadorVivo64(
        False,
        'Não encontrei esta entrada no projeto materializado. Isto não quer dizer que nunca tenhas dito; quer dizer que ela não está em ficheiro/index local recuperável agora. Correção PSF: importar o histórico bruto da conversa ou colar novamente o bloco para virar entrada viva com resposta, aula, teste e rota.',
        'nao_materializado'
    )


def responder_texto_livre(texto: str) -> ResultadoRoteadorVivo64:
    partes = dividir_perguntas(texto)
    if not partes:
        return ResultadoRoteadorVivo64(False, '', 'vazio')
    respostas = []
    reconhecidas = 0
    for i, parte in enumerate(partes, 1):
        r = responder_uma(parte)
        if not r.reconhecido:
            if len(partes) > 1:
                respostas.append(f'{i}. {r.texto}')
            continue
        reconhecidas += 1
        prefixo = f'{i}. ' if len(partes) > 1 else ''
        respostas.append(prefixo + r.texto)
    if reconhecidas:
        return ResultadoRoteadorVivo64(True, '\n\n'.join(respostas), 'roteador_vivo')
    return ResultadoRoteadorVivo64(False, '', 'nao_materializado')


def auto_teste() -> dict:
    casos = {
        'O que são os padrões de Turing na natureza?': 'Turing',
        'Conjectura de Baum-Connes com coeficientes': 'Baum-Connes',
        'Último Teorema de Fermat': 'Fermat',
        'Fórmula de Bhaskara': 'Bhaskara',
    }
    falhas = []
    for entrada, esperado in casos.items():
        saida = responder_texto_livre(entrada).texto
        if esperado not in saida:
            falhas.append({'entrada': entrada, 'esperado': esperado, 'saida': saida[:500]})
    return {'ok': not falhas, 'falhas': falhas, 'estatisticas': estatisticas()}
