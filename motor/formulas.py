"""Auditoria de fórmulas prontas no PSF-IAminy.

Objetivo: não provar que tudo está puro; o objetivo é NÃO fingir.
O motor separa três estados:

1. `recriado_psf`: módulo cuja faixa já foi reconstruída por conceitos PSF;
2. `validacao_ou_legado`: módulo antigo/eficiente que pode conter fórmulas
   clássicas para validação, comparação ou dívida técnica declarada;
3. `suspeito`: uso de operador/função com cara de fórmula pronta fora de
   um módulo marcado.

Esta auditoria é deliberadamente conservadora: ela aponta riscos. O relatório
humano decide se aquilo é dívida técnica, validação externa ou construção já
justificada.
"""
from __future__ import annotations

import ast
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
NUCLEO = RAIZ / "nucleo"

# Módulos antigos/eficientes que podem conter fórmulas clássicas em comentário
# ou implementação. Eles NÃO contam como conceitos PSF recriados; ficam como
# validação, história ou dívida técnica até serem substituídos por módulos
# puros/documentados.
MODULOS_VALIDACAO_OU_LEGADO = {
    "modelo_eficiente",
    "aritmetica", "primos", "divisores", "racionais", "reais",
    "probabilidade", "proporcionalidade", "porcentagem", "harmonicos",
    "numeros_figurados", "combinatoria", "catalan_stirling", "geometria",
    "binario", "inversa_potencia", "calculo_discreto",
    # `reais_intervalos_naturais` é majoritariamente construção PSF genuína
    # (intervalos racionais, Newton para raiz quadrada); só o `%` do seu MDC
    # interno segue exatamente o mesmo motivo já registrado em `reais.py`
    # (custo O(valor) por subtração fica inviável quando os dígitos dobram
    # a cada passo de Newton -- resto é O(dígitos), justificado em comentário
    # no próprio ficheiro).
    "reais_intervalos_naturais",
    # `espaco_combinatorio_palavras` é camada de TRADUÇÃO/ENDEREÇAMENTO, papel
    # já reservado a `nucleo/traducao.py` -- localizar/reconstruir uma
    # sequência dentro de um total já provado (Etapa 39,
    # ESCOLHAS_ORDENADAS_COM_REPETICAO_PURO em combinatoria_natural.py), não
    # provar aritmética nova. Tentativa real de fazer isso pela camada
    # "escolar nativa" foi testada e mediu-se que trava: `predecessor` busca
    # por sucessão a partir de zero a cada chamada (mesma armadilha já
    # registada em `contas_armadas.py`, "decompor 9801 assim passa de um
    # minuto") -- a posição de uma palavra de só 3 letras já reproduziu o
    # travamento. `**`/`divmod` nativos aqui têm o mesmo estatuto que `+1`
    # em `traducao.py`: bookkeeping, não fundamento.
    "espaco_combinatorio_palavras",
}

# Módulos de interface, busca e chat podem conter operadores técnicos de
# pontuação, proporção de confiança, pontuação de busca ou limpeza textual.
# Isso não é conhecimento matemático puro nem fórmula como fundamento.
MODULOS_TECNICOS_NAO_FUNDAMENTO = {
    "base_curiosidades_reais",
    "chat_auditoria",
    "chat_base_canonica",
    "indexador_total",
}

# Módulos cujo objetivo é reconstrução operacional finita por fluxo natural.
# Neles, operadores de divisão/módulo, chamadas math/sympy/numpy, etc., são
# suspeitos e devem ser justificados ou removidos.
MODULOS_RECRIADOS_PSF = {
    p.stem for p in NUCLEO.glob("*.py")
    if p.stem not in MODULOS_VALIDACAO_OU_LEGADO and p.stem != "__init__"
}

OPERADORES_SUSPEITOS = {
    ast.Div: "/",
    ast.FloorDiv: "//",
    ast.Mod: "%",
    ast.Pow: "**",
}
FUNCOES_PRONTAS_SUSPEITAS = {
    "sqrt", "factorial", "comb", "perm", "gcd", "lcm", "mean", "median",
    "variance", "stdev", "solve", "integrate", "diff", "sin", "cos", "log",
}
MODULOS_EXTERNOS_SUSPEITOS = {"math", "statistics", "fractions", "decimal", "numpy", "sympy", "scipy"}


def _nome_chamada(no: ast.AST) -> str | None:
    if isinstance(no, ast.Name):
        return no.id
    if isinstance(no, ast.Attribute):
        base = _nome_chamada(no.value)
        return f"{base}.{no.attr}" if base else no.attr
    return None


def achados_modulo(caminho: Path) -> list[dict[str, object]]:
    arv = ast.parse(caminho.read_text(encoding="utf-8"), filename=str(caminho))
    achados: list[dict[str, object]] = []
    for no in ast.walk(arv):
        if isinstance(no, ast.BinOp):
            for classe, simbolo in OPERADORES_SUSPEITOS.items():
                if isinstance(no.op, classe):
                    achados.append({"linha": getattr(no, "lineno", 0), "tipo": "operador", "valor": simbolo})
        elif isinstance(no, ast.Call):
            nome = _nome_chamada(no.func)
            if nome:
                curto = nome.split(".")[-1]
                raiz = nome.split(".")[0]
                if curto in FUNCOES_PRONTAS_SUSPEITAS or raiz in MODULOS_EXTERNOS_SUSPEITOS:
                    achados.append({"linha": getattr(no, "lineno", 0), "tipo": "chamada", "valor": nome})
        elif isinstance(no, ast.Import):
            for a in no.names:
                raiz = a.name.split(".")[0]
                if raiz in MODULOS_EXTERNOS_SUSPEITOS:
                    achados.append({"linha": getattr(no, "lineno", 0), "tipo": "import", "valor": a.name})
        elif isinstance(no, ast.ImportFrom):
            raiz = (no.module or "").split(".")[0]
            if raiz in MODULOS_EXTERNOS_SUSPEITOS:
                achados.append({"linha": getattr(no, "lineno", 0), "tipo": "import", "valor": no.module})
    return achados


def auditar_formulas() -> dict[str, dict[str, object]]:
    saida: dict[str, dict[str, object]] = {}
    for caminho in sorted(NUCLEO.glob("*.py")):
        if caminho.stem == "__init__":
            continue
        achados = achados_modulo(caminho)
        if not achados:
            continue
        if caminho.stem in MODULOS_VALIDACAO_OU_LEGADO:
            estado = "validacao_ou_legado"
        elif caminho.stem in MODULOS_TECNICOS_NAO_FUNDAMENTO:
            estado = "tecnico_nao_fundamento"
        else:
            estado = "suspeito"
        saida[caminho.stem] = {"estado": estado, "achados": achados[:40], "total": len(achados)}
    return saida


def resumo_auditoria_formulas() -> dict[str, object]:
    dados = auditar_formulas()
    suspeitos = {m: d for m, d in dados.items() if d["estado"] == "suspeito"}
    legado = {m: d for m, d in dados.items() if d["estado"] == "validacao_ou_legado"}
    tecnico = {m: d for m, d in dados.items() if d["estado"] == "tecnico_nao_fundamento"}
    return {
        "modulos_com_achados": len(dados),
        "suspeitos": suspeitos,
        "validacao_ou_legado": legado,
        "tecnico_nao_fundamento": tecnico,
        "total_suspeitos": len(suspeitos),
        "total_legado": len(legado),
        "total_tecnico": len(tecnico),
    }
