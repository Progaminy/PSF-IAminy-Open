"""Interface de decisão: antes de responder sozinho, o motor principal se
pergunta se deve consultar uma ferramenta auxiliar externa (`cao_de_caca`).

Perguntas, na ordem pedida pelo autor:
    1. Preciso comparar um resultado?
    2. Preciso de um valor exato ou otimizado?
    3. Preciso usar dependência externa?
    4. Qual é o assunto -- o cão de caça tem esse assunto?

Se (1), (2) ou (3) forem verdadeiras e o cão de caça tiver o assunto (4), a
decisão aponta para lá. Não é IA nem heurística estatística -- é um
classificador honesto por palavra-chave, no mesmo espírito de
`lingua_portuguesa/investigacao.py`: transparente sobre o próprio limite,
nunca finge entender mais do que realmente decide. O catálogo consultado é
sempre o real, ao vivo (`interface.mapa_cao_de_caca.dados_cao_de_caca`) --
nunca uma lista congelada que possa ficar desatualizada.

Isto nunca produz conhecimento PSF nem substitui `MotorMatematica`/
`MotorPortugues`: é só um roteador, o mesmo papel que `MotorAuxiliarValidacao`
já cumpre para comparação/validação, agora formalizado e estendido ao
catálogo inteiro do cão de caça.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

from interface.mapa_cao_de_caca import dados_cao_de_caca


def _dobrar(texto: str) -> str:
    """Minúsculas sem acento -- só para casar texto, nunca para exibir."""
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return sem_acento.casefold()

_PALAVRAS_COMPARAR = (
    "comparar", "compare", "conferir", "confirma", "confere",
    "bate com", "validar", "verificar contra",
)
_PALAVRAS_VALOR_EXATO = (
    "exato", "exata", "otimizado", "otimizada", "otimizar",
    "maximizar", "minimizar", "precisão", "casas decimais",
)
_PALAVRAS_DEPENDENCIA_EXTERNA = (
    "numpy", "scipy", "sympy", "matplotlib", "networkx", "scikit-learn",
    "gráfico", "grafico", "plot", "dependência externa", "dependencia externa",
)


@dataclass(frozen=True, slots=True)
class DecisaoAuxiliar:
    pergunta: str
    precisa_comparar: bool
    precisa_valor_exato: bool
    precisa_dependencia_externa: bool
    assunto: str | None
    cao_de_caca_tem_assunto: bool
    cao_de_caca_disponivel: bool
    usar_cao_de_caca: bool
    motores_candidatos: tuple[str, ...]


_TAMANHO_MINIMO_CANDIDATO = 4


def _assunto_no_cao_de_caca(pergunta: str, catalogo: dict) -> tuple[str | None, tuple[str, ...]]:
    """Procura, no catálogo REAL (ao vivo), um tema ou nome de motor citado na pergunta.

    Casamento por fronteira de palavra (nunca substring solto -- "pa" não
    pode casar dentro de "comparar") e sem distinguir acento (para aceitar
    "otimização" batendo com o atributo "otimizacao"). Nomes de motor com
    menos de 4 letras (ex.: "pa", "pg") são ignorados como assunto -- curtos
    demais para significar algo fora de um comando explícito do cão de caça.
    """
    texto = _dobrar(pergunta)
    tema_encontrado: str | None = None
    candidatos: list[str] = []
    for no in catalogo.get("nodes", ()):
        tema_dobrado = _dobrar(no["tema"])
        if tema_encontrado is None and re.search(r"\b" + re.escape(tema_dobrado) + r"\b", texto):
            tema_encontrado = no["tema"]
        nome_legivel = _dobrar(no["nome"].replace("_", " "))
        if len(no["nome"]) >= _TAMANHO_MINIMO_CANDIDATO and re.search(r"\b" + re.escape(nome_legivel) + r"\b", texto):
            candidatos.append(no["nome"])
    return tema_encontrado, tuple(candidatos)


def decidir(pergunta: str) -> DecisaoAuxiliar:
    """Executa as 4 perguntas e devolve a decisão -- nunca executa o cão de caça sozinho."""
    texto = pergunta.casefold()
    precisa_comparar = any(p in texto for p in _PALAVRAS_COMPARAR)
    precisa_valor_exato = any(p in texto for p in _PALAVRAS_VALOR_EXATO)
    precisa_dependencia = any(p in texto for p in _PALAVRAS_DEPENDENCIA_EXTERNA)

    catalogo = dados_cao_de_caca()
    disponivel = bool(catalogo.get("disponivel", False))
    assunto, candidatos = _assunto_no_cao_de_caca(pergunta, catalogo) if disponivel else (None, ())
    tem_assunto = disponivel and (assunto is not None or bool(candidatos))

    precisa_algo = precisa_comparar or precisa_valor_exato or precisa_dependencia
    usar = precisa_algo and tem_assunto

    return DecisaoAuxiliar(
        pergunta=pergunta,
        precisa_comparar=precisa_comparar,
        precisa_valor_exato=precisa_valor_exato,
        precisa_dependencia_externa=precisa_dependencia,
        assunto=assunto,
        cao_de_caca_tem_assunto=tem_assunto,
        cao_de_caca_disponivel=disponivel,
        usar_cao_de_caca=usar,
        motores_candidatos=candidatos,
    )
