"""Tabela de traços fonéticos computável -- Soundex/Metaphone-equivalente
para português (Fase 4.1 do plano de corretor, técnica 4 do pedido
original: candidatos foneticamente parecidos).

Cada rótulo de traço usado em `TRACOS_GRAFEMA` é o `nome` de um conceito
REAL já documentado no tema `fonetica_fonologia` de `conhecimento_puro.py`
(ponto de articulação, modo de articulação, vozeamento) -- nunca uma
categoria inventada sem lastro. `test_fonetica_computavel.py` confirma isto
mecanicamente: nenhum rótulo usado aqui escapa ao conjunto de nomes reais
daquele tema.

Soundex e Metaphone são algoritmos determinísticos clássicos (mapeamento
fixo + colapso de repetição), não modelos estatísticos ou treinados -- a
regra do projeto que proíbe atalho pré-treinado (Word2Vec/BERT/XGBoost)
não os alcança; a tabela e a redução abaixo são construídas do zero,
PSF-próprias.

**Simplificação assumida e declarada, não escondida**: esta primeira
versão classifica cada grafema/dígrafo por UMA classe fixa, ignorando
grafemas sensíveis a contexto (ex.: "c"/"g" antes de "e"/"i" mudam de som
em português real -- "cela" vs "cama", "gelo" vs "gato"). Modelar essa
sensibilidade a contexto fica como extensão futura, não fingida aqui.
"""
from __future__ import annotations

# ponto/modo/vozeamento de cada grafema/dígrafo -- cada valor usado é o
# nome exato de um ConceitoPortugues real do tema fonetica_fonologia.
TRACOS_GRAFEMA: dict[str, dict[str, str]] = {
    "b": {"ponto": "bilabial", "modo": "oclusiva", "vozeamento": "consoante sonora"},
    "p": {"ponto": "bilabial", "modo": "oclusiva", "vozeamento": "consoante surda"},
    "d": {"ponto": "dental", "modo": "oclusiva", "vozeamento": "consoante sonora"},
    "t": {"ponto": "dental", "modo": "oclusiva", "vozeamento": "consoante surda"},
    "g": {"ponto": "velar", "modo": "oclusiva", "vozeamento": "consoante sonora"},
    "c": {"ponto": "velar", "modo": "oclusiva", "vozeamento": "consoante surda"},
    "k": {"ponto": "velar", "modo": "oclusiva", "vozeamento": "consoante surda"},
    "q": {"ponto": "velar", "modo": "oclusiva", "vozeamento": "consoante surda"},
    "qu": {"ponto": "velar", "modo": "oclusiva", "vozeamento": "consoante surda"},
    "gu": {"ponto": "velar", "modo": "oclusiva", "vozeamento": "consoante sonora"},
    "f": {"ponto": "labiodental", "modo": "fricativa", "vozeamento": "consoante surda"},
    "v": {"ponto": "labiodental", "modo": "fricativa", "vozeamento": "consoante sonora"},
    "s": {"ponto": "alveolar", "modo": "fricativa", "vozeamento": "consoante surda"},
    "z": {"ponto": "alveolar", "modo": "fricativa", "vozeamento": "consoante sonora"},
    "ç": {"ponto": "alveolar", "modo": "fricativa", "vozeamento": "consoante surda"},
    "x": {"ponto": "palatal", "modo": "fricativa", "vozeamento": "consoante surda"},
    "ch": {"ponto": "palatal", "modo": "fricativa", "vozeamento": "consoante surda"},
    "j": {"ponto": "palatal", "modo": "fricativa", "vozeamento": "consoante sonora"},
    "l": {"ponto": "alveolar", "modo": "lateral"},
    "lh": {"ponto": "palatal", "modo": "lateral"},
    "r": {"ponto": "alveolar", "modo": "vibrante"},
    "rr": {"ponto": "alveolar", "modo": "vibrante"},
    "m": {"ponto": "bilabial", "modo": "nasal consonantal"},
    "n": {"ponto": "alveolar", "modo": "nasal consonantal"},
    "nh": {"ponto": "palatal", "modo": "nasal consonantal"},
}

_DIGRAFOS: tuple[str, ...] = ("ch", "lh", "nh", "rr", "qu", "gu")

# O CÓDIGO de agrupamento (usado por `codigo_fonetico`) usa só ponto+modo,
# ignorando vozeamento de propósito: é exatamente a distinção sonora/surda
# (s/z, c/g, f/v...) que mais gera erro real de ortografia em português --
# juntar esses pares na mesma classe é o que torna a redução útil para
# achar candidatos foneticamente parecidos, igual ao Soundex clássico
# juntar b/f/p/v e c/g/j/k/q/s/x/z.
_CHAVES_AGRUPAMENTO: tuple[tuple[str, str], ...] = tuple(
    sorted({(tracos["ponto"], tracos["modo"]) for tracos in TRACOS_GRAFEMA.values()})
)
_CODIGO_POR_CHAVE: dict[tuple[str, str], str] = {
    chave: str(indice + 1) for indice, chave in enumerate(_CHAVES_AGRUPAMENTO)
}


def _grafemas(palavra: str) -> list[str]:
    """Quebra a palavra em grafemas, tratando dígrafos como uma unidade."""
    minuscula = palavra.casefold()
    unidades: list[str] = []
    indice = 0
    while indice < len(minuscula):
        par = minuscula[indice : indice + 2]
        if par in _DIGRAFOS:
            unidades.append(par)
            indice += 2
        else:
            unidades.append(minuscula[indice])
            indice += 1
    return unidades


def _codigo_de(grafema: str) -> str | None:
    tracos = TRACOS_GRAFEMA.get(grafema)
    if tracos is None:
        return None
    return _CODIGO_POR_CHAVE[(tracos["ponto"], tracos["modo"])]


def mesma_classe_fonetica(a: str, b: str) -> bool:
    """True se os grafemas `a` e `b` pertencerem à mesma classe de
    ponto+modo de articulação. Ao contrário de `codigo_fonetico` (que
    compara a palavra inteira e mantém o primeiro grafema literal), esta
    função compara diretamente dois grafemas quaisquer -- útil para
    avaliar uma substituição pontual em qualquer posição da palavra."""
    tracos_a = TRACOS_GRAFEMA.get(a.casefold())
    tracos_b = TRACOS_GRAFEMA.get(b.casefold())
    if tracos_a is None or tracos_b is None:
        return False
    return (tracos_a["ponto"], tracos_a["modo"]) == (tracos_b["ponto"], tracos_b["modo"])


def codigo_fonetico(palavra: str) -> str:
    """Reduz `palavra` a um código fonético (Soundex/Metaphone-equivalente
    para PT): mantém o primeiro grafema tal como está, reduz os grafemas
    seguintes ao código da sua classe ponto+modo, ignora vogais e outros
    caracteres sem traço conhecido, e colapsa códigos repetidos
    consecutivos (mesma ideia central de Soundex)."""
    grafemas = _grafemas(palavra)
    if not grafemas:
        return ""
    primeiro = grafemas[0]
    codigos: list[str] = []
    anterior: str | None = None
    for grafema in grafemas[1:]:
        codigo = _codigo_de(grafema)
        if codigo is None:
            anterior = None
            continue
        if codigo != anterior:
            codigos.append(codigo)
        anterior = codigo
    return (primeiro + "".join(codigos)).casefold()
