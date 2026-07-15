"""Fronteira honesta de conhecimento do PSF-IAminy."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RelatorioFronteira:
    topo: int
    texto: str


def relatorio_fronteira(topo: int) -> RelatorioFronteira:
    texto = "\n".join(
        (
            "Fronteira atual do PSF-IAminy",
            f"Topo construído: PSF-K{topo:04d}.",
            "O motor é aberto ao infinito, mas não finge saber o que ainda não construiu.",
            "",
            "O que melhorou nesta fronteira",
            "- conceito futuro agora não vira silêncio nem resposta genérica; vira plano de construção;",
            "- a IA pode explicar o que falta antes de ensinar;",
            "- fórmula pronta continua proibida como fundamento;",
            "- validação externa fica separada do núcleo puro.",
            "",
            "Regra para conceito futuro:",
            "1. nomear o conceito pedido;",
            "2. localizar dependências já construídas;",
            "3. construir por exemplos pequenos;",
            "4. transformar em definição provisória;",
            "5. testar contra casos simples e contra contraexemplos;",
            "6. documentar falhas e dependências;",
            "7. só depois virar aula normal.",
            "",
            "Se uma fórmula clássica existir, ela entra apenas como validação externa, não como fundamento.",
        )
    )
    return RelatorioFronteira(topo, texto)


def relatorio_infinito(topo: int) -> RelatorioFronteira:
    texto = "\n".join(
        (
            "Matemática infinita real no modo PSF",
            "Infinito aqui não significa despejar uma lista sem fim. Significa ter uma regra que pode continuar.",
            f"Hoje o conhecimento construído chega a PSF-K{topo:04d}.",
            "",
            "Motor real do infinito",
            "1. Existe um topo construído: tudo até ele pode virar aula normal.",
            "2. Existe uma próxima etapa natural: ela pode ser construída agora.",
            "3. Existe uma fronteira futura: ela pode ser planejada, mas não vendida como pronta.",
            "4. Existe validação: comparação externa pode conferir, mas não fundar o PSF.",
            "",
            "O trilho funciona assim:",
            "zero absoluto → distinção → número → operação → estrutura → modelo → validação → nova fronteira",
            "",
            "As aulas fixas ajudam o humano a começar. As aulas PSF-K ensinam tudo que o projeto já construiu.",
            "Acima do topo, o PSF responde com honestidade: ainda não construí, mas posso iniciar a construção.",
        )
    )
    return RelatorioFronteira(topo, texto)
