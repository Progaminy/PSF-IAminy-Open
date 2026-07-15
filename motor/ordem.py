"""Verificação de compatibilidade dos marcadores históricos.

Esta auditoria não decide verdade nem dependência matemática. Ela apenas deteta
inversões suspeitas no arquivo histórico ETAPA enquanto a migração para
dependências canónicas não está completa.

Verificação de ordem do motor PSF-IAminy.

A Lei PSF-IAminy ("nada se usa antes de nascer") até agora só era respeitada
por convenção — cada módulo *diz*, em comentário, o que não pode importar,
mas nada confirmava que o número da etapa de quem importa é sempre maior
que o número da etapa de quem é importado. Este ficheiro fecha isso onde
for possível.

COBERTURA HONESTA (não assumida): a verificação só funciona para módulos
cuja etapa é conhecida — e isso depende de as ETAPA_XX.md declararem o
ficheiro implementado de forma reconhecível (ver motor.rastreabilidade).
Testado: as etapas 6-19 (exceto 3, 4 e 15) são exposição matemática pura,
sem essa declaração — os módulos correspondentes
(diferenca_controlada.py, euclides_subtracao_pura.py,
divisao_euclidiana_pura.py, euclides_resto_puro.py, primalidade_pura.py,
fatoracao_pura.py, bezout_euclides_puro.py) ficam FORA desta verificação
específica até essa lacuna de documentação ser fechada — não porque
violem a ordem, mas porque não há como confirmar automaticamente. Isto é
reportado explicitamente, não escondido.
"""
from __future__ import annotations

import re
from pathlib import Path

from .pureza import _imports_do_modulo
from .rastreabilidade import _referencias_de_etapa

RAIZ = Path(__file__).resolve().parents[1]
CONHECIMENTO = RAIZ / "conhecimento"
NUCLEO = RAIZ / "nucleo"

# Etapas implícitas do núcleo inicial (ver motor.fluxo.ETAPAS_IMPLICITAS).
# Sem esta semente, a verificação de ordem tratava módulos fundacionais como
# "fora de cobertura", embora o próprio motor já os conte nas etapas 1-2.
ETAPAS_IMPLÍCITAS_POR_MODULO = {
    "primitivas": 1,
    "logica": 1,
    "aritmetica": 1,
    "traducao": 1,
}

_PADRAO_NUMERO_ETAPA = re.compile(r"ETAPA_(\d+)_")


def modulo_para_etapas() -> dict[str, list[int]]:
    """{nome_do_modulo: [números de etapa que o documentam]}."""
    mapa: dict[str, list[int]] = {}
    for nome, numero in ETAPAS_IMPLÍCITAS_POR_MODULO.items():
        mapa.setdefault(nome, []).append(numero)
    for arquivo in sorted(CONHECIMENTO.glob("ETAPA_*.md")):
        m = _PADRAO_NUMERO_ETAPA.match(arquivo.name)
        if not m:
            continue
        numero = int(m.group(1))
        for ref in _referencias_de_etapa(arquivo):
            if ref.startswith("nucleo/"):
                mapa.setdefault(Path(ref).stem, []).append(numero)
    return mapa


def _etapa_minima(nome_modulo: str, mapa: dict[str, list[int]]) -> int | None:
    """Módulos que cobrem várias etapas (ex.: teoria_numeros_natural.py
    cobre 20-35) usam a MENOR — é a etapa em que o módulo "nasceu"."""
    etapas = mapa.get(nome_modulo)
    return min(etapas) if etapas else None


def _imports_relativos(caminho: Path) -> set[str]:
    """Nomes de módulo importados por `caminho` (todos os formatos — ver
    `motor.pureza._imports_do_modulo`, reaproveitada aqui para não duplicar
    a mesma extração de AST em dois lugares que podiam divergir)."""
    return {modulo for modulo, _ in _imports_do_modulo(caminho)}


def modulos_fora_de_cobertura() -> list[str]:
    """nucleo/*.py sem etapa conhecida — não podem ser verificados."""
    mapa = modulo_para_etapas()
    return sorted(
        p.stem for p in NUCLEO.glob("*.py")
        if p.stem != "__init__" and _etapa_minima(p.stem, mapa) is None
    )


def violacoes_de_ordem() -> dict[str, list[str]]:
    """Nome legado: devolve alertas de marcador histórico, não violações de verdade.

    {modulo: [\"importado (etapa X > etapa própria Y)\", ...]}.
    Só considera módulos com etapa conhecida dos dois lados — ver
    `modulos_fora_de_cobertura()` para o que fica de fora."""
    mapa = modulo_para_etapas()
    violacoes: dict[str, list[str]] = {}
    for caminho in sorted(NUCLEO.glob("*.py")):
        nome = caminho.stem
        if nome == "__init__":
            continue
        minha_etapa = _etapa_minima(nome, mapa)
        if minha_etapa is None:
            continue
        problemas = []
        for importado in _imports_relativos(caminho):
            etapa_importado = _etapa_minima(importado, mapa)
            if etapa_importado is not None and etapa_importado > minha_etapa:
                problemas.append(f"{importado} (etapa {etapa_importado} > {minha_etapa})")
        if problemas:
            violacoes[nome] = problemas
    return violacoes
