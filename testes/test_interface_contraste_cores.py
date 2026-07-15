"""Contraste de cores (WCAG 2 AA) de `interface/estatico/estilo.css`.

Lê as cores reais das variáveis `:root` (tema claro) e do bloco
`@media (prefers-color-scheme: dark)` (tema escuro) direto do ficheiro
-- nunca um retrato congelado -- e calcula a razão de contraste pela
fórmula oficial (luminância relativa, WCAG 2 §1.4.3), sem depender de
nenhuma biblioteca externa de acessibilidade. Falha se alguém trocar
uma cor e, sem perceber, deixar texto real abaixo de 4.5:1 (AA, texto
normal) -- foi assim que `--texto-suave` sobre `--bg-terciario` no
tema claro foi encontrado em 4.46:1, corrigido para 4.53:1 com uma
troca de 1 unidade de RGB, imperceptível a olho nu.
"""
from __future__ import annotations

import re
from pathlib import Path

CAMINHO_CSS = Path(__file__).resolve().parent.parent / "interface" / "estatico" / "estilo.css"

# Pares texto/fundo realmente usados na interface (não é todo par possível
# de variável -- só os que aparecem como texto sobre fundo em `estilo.css`).
PARES_TEXTO_NORMAL = [
    ("texto", "bg"),
    ("texto-suave", "bg"),
    ("texto", "bg-secundario"),
    ("texto-suave", "bg-secundario"),
    ("texto-suave", "bg-terciario"),
]
PARES_TEXTO_EM_BOTAO = [
    ("acento-texto", "acento"),
]

MINIMO_AA_TEXTO_NORMAL = 4.5
MINIMO_AA_TEXTO_GRANDE_OU_UI = 3.0


def _hex_para_rgb(hexadecimal: str) -> tuple[int, int, int]:
    h = hexadecimal.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def _luminancia_relativa(rgb: tuple[int, int, int]) -> float:
    def canal(c: int) -> float:
        c_norm = c / 255
        return c_norm / 12.92 if c_norm <= 0.03928 else ((c_norm + 0.055) / 1.055) ** 2.4

    r, g, b = (canal(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def razao_de_contraste(hex1: str, hex2: str) -> float:
    l1 = _luminancia_relativa(_hex_para_rgb(hex1))
    l2 = _luminancia_relativa(_hex_para_rgb(hex2))
    mais_clara, mais_escura = max(l1, l2), min(l1, l2)
    return (mais_clara + 0.05) / (mais_escura + 0.05)


def _variaveis_do_bloco(bloco: str) -> dict[str, str]:
    return dict(re.findall(r"--([\w-]+):\s*(#[0-9a-fA-F]{6})", bloco))


def cores_do_tema_claro() -> dict[str, str]:
    css = CAMINHO_CSS.read_text(encoding="utf-8")
    bloco = re.search(r"^:root\s*\{(.*?)\}", css, re.S | re.M)
    assert bloco, "não encontrei o bloco :root (tema claro) em estilo.css"
    return _variaveis_do_bloco(bloco.group(1))


def cores_do_tema_escuro() -> dict[str, str]:
    css = CAMINHO_CSS.read_text(encoding="utf-8")
    bloco = re.search(r"@media \(prefers-color-scheme: dark\)\s*\{\s*:root\s*\{(.*?)\}\s*\}", css, re.S)
    assert bloco, "não encontrei o bloco :root dentro de prefers-color-scheme: dark em estilo.css"
    return _variaveis_do_bloco(bloco.group(1))


def _checar_pares(cores: dict[str, str], pares, minimo: float) -> list[str]:
    falhas = []
    for texto, fundo in pares:
        razao = razao_de_contraste(cores[texto], cores[fundo])
        if razao < minimo:
            falhas.append(f"--{texto} sobre --{fundo}: {razao:.2f}:1 (mínimo {minimo}:1)")
    return falhas


def test_contraste_tema_claro_texto_normal_aa():
    falhas = _checar_pares(cores_do_tema_claro(), PARES_TEXTO_NORMAL, MINIMO_AA_TEXTO_NORMAL)
    assert not falhas, "; ".join(falhas)


def test_contraste_tema_escuro_texto_normal_aa():
    falhas = _checar_pares(cores_do_tema_escuro(), PARES_TEXTO_NORMAL, MINIMO_AA_TEXTO_NORMAL)
    assert not falhas, "; ".join(falhas)


def test_contraste_tema_claro_texto_em_botao_aa():
    falhas = _checar_pares(cores_do_tema_claro(), PARES_TEXTO_EM_BOTAO, MINIMO_AA_TEXTO_GRANDE_OU_UI)
    assert not falhas, "; ".join(falhas)


def test_contraste_tema_escuro_texto_em_botao_aa():
    falhas = _checar_pares(cores_do_tema_escuro(), PARES_TEXTO_EM_BOTAO, MINIMO_AA_TEXTO_GRANDE_OU_UI)
    assert not falhas, "; ".join(falhas)
