# -*- coding: utf-8 -*-
"""Rota de correção linguística do Chat Vivo (Fase 1-C, ligada ao
orquestrador completo na Fase 6.4 do plano de corretor).

Liga ao chat o pipeline inteiro construído nas Fases 1-6:
normalização mecânica de texto corrido (Fase 1-B), whitelist ortográfica
conservadora, aviso de parônimo, e sugestão ranqueada (Fase 6.3 --
distância de edição + fonética + frequência + contexto + canal ruidoso +
proximidade semântica, nunca um único sinal isolado) via
`lingua_portuguesa.corretor.Corretor`.

Ordem de prioridade preservada (nunca correção silenciosa de significado):
1. normalização mecânica (pontuação/espaço/maiúscula/parágrafo);
2. whitelist de erros aprovados;
3. parônimo: nota consultiva, nunca troca automática;
4. palavra ausente do dicionário: sugestão ranqueada, nunca substituição.
"""
from __future__ import annotations

from functools import lru_cache

from lingua_portuguesa.corretor import Corretor
from nucleo.chat_tipos import RespostaChat


@lru_cache(maxsize=1)
def _corretor() -> Corretor:
    return Corretor()


def _responder_corrigir(texto: str, tom: str) -> RespostaChat:
    resultado = _corretor().corrigir_texto(texto)

    linhas: list[str] = []
    if resultado.normalizado != resultado.original:
        linhas.append(f"Normalizado (pontuação/espaço/maiúscula/parágrafo): {resultado.normalizado}")
    if resultado.alteracoes_whitelist:
        linhas.append(f"Ortografia (erro conhecido corrigido): {resultado.corrigido}")
        for antes, depois, motivo in resultado.alteracoes_whitelist:
            linhas.append(f"  - {antes} -> {depois} ({motivo})")
    if resultado.notas_paronimo:
        linhas.append("Parônimos possíveis (confira o sentido, não troquei sozinho):")
        linhas.extend(f"  - {nota}" for nota in resultado.notas_paronimo)
    if resultado.sugestoes_ortografia:
        linhas.append("Palavras que não reconheço no dicionário, com sugestões próximas:")
        linhas.extend(
            f'  - "{palavra}" -> talvez: {", ".join(candidatas)}'
            for palavra, candidatas in resultado.sugestoes_ortografia
        )

    if not linhas:
        corpo = f"Não encontrei nada para corrigir. Texto:\n{resultado.corrigido}"
        confianca = 70
    else:
        corpo = "\n".join(linhas) + f"\n\nTexto final sugerido: {resultado.corrigido}"
        confianca = 80

    return RespostaChat(
        corpo,
        "corrigir",
        tom,
        confianca,
        origem="lingua_portuguesa.corretor",
        conhecimento_encontrado=True,
        contexto_chat={"ultimo_titulo": "correção de texto", "ultima_origem": "lingua_portuguesa.corretor"},
    )
