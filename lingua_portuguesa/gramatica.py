"""Regras gramaticais pequenas, compostas e substituíveis."""
from __future__ import annotations

from typing import Protocol

from .tipos import (
    AnaliseToken,
    ClasseGramatical,
    Constituinte,
    Diagnostico,
    Genero,
    Numero,
)


class RegraGramatical(Protocol):
    def verificar(self, analises: tuple[AnaliseToken, ...]) -> tuple[Diagnostico, ...]:
        ...


def _leitura_de_classe(analise: AnaliseToken, classe: ClasseGramatical):
    return next((leitura for leitura in analise.leituras if leitura.classe == classe), None)


def _discordancias(esquerda, direita) -> list[str]:
    campos: list[str] = []
    if (
        esquerda.genero in {Genero.MASCULINO, Genero.FEMININO}
        and direita.genero in {Genero.MASCULINO, Genero.FEMININO}
        and esquerda.genero != direita.genero
    ):
        campos.append("género")
    if esquerda.numero is not None and direita.numero is not None and esquerda.numero != direita.numero:
        campos.append("número")
    return campos


class RegraConcordanciaDeterminanteNome:
    def verificar(self, analises: tuple[AnaliseToken, ...]) -> tuple[Diagnostico, ...]:
        resultados: list[Diagnostico] = []
        for esquerda, direita in zip(analises, analises[1:]):
            det = _leitura_de_classe(esquerda, ClasseGramatical.DETERMINANTE)
            nome = _leitura_de_classe(direita, ClasseGramatical.SUBSTANTIVO)
            if det is None or nome is None:
                continue
            campos = _discordancias(det, nome)
            if campos:
                resultados.append(
                    Diagnostico(
                        codigo="CONCORDANCIA_DET_NOME",
                        mensagem=f"Possível discordância de {' e '.join(campos)} entre "
                        f"“{esquerda.token.texto}” e “{direita.token.texto}”.",
                        inicio=esquerda.token.inicio,
                        fim=direita.token.fim,
                        sugestao="Faça o determinante concordar com o substantivo.",
                    )
                )
        return tuple(resultados)


def _discordancias_verbais(sujeito, verbo) -> list[str]:
    campos: list[str] = []
    if sujeito.numero is not None and verbo.numero is not None and sujeito.numero != verbo.numero:
        campos.append("número")
    if sujeito.pessoa is not None and verbo.pessoa is not None and sujeito.pessoa != verbo.pessoa:
        campos.append("pessoa")
    return campos


def _nucleo_do_sujeito(candidatos: list[AnaliseToken]):
    for item in candidatos:
        leitura = _leitura_de_classe(item, ClasseGramatical.SUBSTANTIVO)
        if leitura is None:
            leitura = _leitura_de_classe(item, ClasseGramatical.PRONOME)
        if leitura is not None:
            return leitura
    return None


class RegraConcordanciaVerboSujeito:
    """Concordância de número e pessoa entre o núcleo do sujeito e o verbo.

    Ao contrário de determinante/nome e nome/adjetivo, sujeito e verbo não
    são sempre adjacentes ("Os livros antigos chegou") -- por isso esta
    regra segmenta por frase e localiza os dois membros do par, em vez de
    comparar pares consecutivos.
    """

    def verificar(self, analises: tuple[AnaliseToken, ...]) -> tuple[Diagnostico, ...]:
        resultados: list[Diagnostico] = []
        for segmento in _segmentos_frase(analises):
            indice_verbo = next(
                (
                    i
                    for i, analise in enumerate(segmento)
                    if _leitura_de_classe(analise, ClasseGramatical.VERBO) is not None
                ),
                None,
            )
            if indice_verbo is None:
                continue
            verbo = _leitura_de_classe(segmento[indice_verbo], ClasseGramatical.VERBO)
            candidatos_sujeito = [
                item for item in segmento[:indice_verbo]
                if item.token.texto.strip() and item.token.texto not in ",;:"
            ]
            if not candidatos_sujeito:
                continue
            nucleo = _nucleo_do_sujeito(candidatos_sujeito)
            if nucleo is None:
                continue
            campos = _discordancias_verbais(nucleo, verbo)
            if campos:
                sujeito_texto = " ".join(item.token.texto for item in candidatos_sujeito)
                resultados.append(
                    Diagnostico(
                        codigo="CONCORDANCIA_VERBO_SUJEITO",
                        mensagem=f"Possível discordância de {' e '.join(campos)} entre "
                        f"“{sujeito_texto}” e “{segmento[indice_verbo].token.texto}”.",
                        inicio=candidatos_sujeito[0].token.inicio,
                        fim=segmento[indice_verbo].token.fim,
                        sugestao="Faça o verbo concordar com o núcleo do sujeito.",
                    )
                )
        return tuple(resultados)


class RegraCategoriaIncompativel:
    """Sinaliza quando a leitura escolhida por padrão (`AnaliseToken.principal`,
    sempre `leituras[0]`, cega a contexto) esconde um verbo real: a frase
    parece não ter nenhum verbo olhando só a leitura principal de cada
    token, mas algum token tem leitura de verbo entre as alternativas não
    escolhidas. Fatia estreita e honesta da técnica 8 (BERT/homónimos em
    contexto) -- não resolve homónimos em geral, só este caso específico e
    verificável.
    """

    def verificar(self, analises: tuple[AnaliseToken, ...]) -> tuple[Diagnostico, ...]:
        resultados: list[Diagnostico] = []
        for segmento in _segmentos_frase(analises):
            tem_verbo_principal = any(
                analise.leituras and analise.principal.classe == ClasseGramatical.VERBO
                for analise in segmento
            )
            if tem_verbo_principal:
                continue
            for analise in segmento:
                if not analise.leituras or analise.principal.classe == ClasseGramatical.VERBO:
                    continue
                leitura_verbo = _leitura_de_classe(analise, ClasseGramatical.VERBO)
                if leitura_verbo is None:
                    continue
                resultados.append(
                    Diagnostico(
                        codigo="CATEGORIA_INCOMPATIVEL",
                        mensagem=f"“{analise.token.texto}” foi lido como "
                        f"{analise.principal.classe.value}, mas também pode ser verbo -- "
                        "nenhum outro token da frase tem leitura de verbo.",
                        inicio=analise.token.inicio,
                        fim=analise.token.fim,
                        sugestao="Confira se esta palavra deveria ter sido lida como verbo.",
                    )
                )
        return tuple(resultados)


class RegraConcordanciaNomeAdjetivo:
    def verificar(self, analises: tuple[AnaliseToken, ...]) -> tuple[Diagnostico, ...]:
        resultados: list[Diagnostico] = []
        for esquerda, direita in zip(analises, analises[1:]):
            nome = _leitura_de_classe(esquerda, ClasseGramatical.SUBSTANTIVO)
            adjetivo = _leitura_de_classe(direita, ClasseGramatical.ADJETIVO)
            if nome is None or adjetivo is None:
                continue
            campos = _discordancias(nome, adjetivo)
            if campos:
                resultados.append(
                    Diagnostico(
                        codigo="CONCORDANCIA_NOME_ADJ",
                        mensagem=f"Possível discordância de {' e '.join(campos)} entre "
                        f"“{esquerda.token.texto}” e “{direita.token.texto}”.",
                        inicio=esquerda.token.inicio,
                        fim=direita.token.fim,
                        sugestao="Faça o adjetivo concordar com o substantivo.",
                    )
                )
        return tuple(resultados)


class AnalisadorGramatical:
    def __init__(self, regras: tuple[RegraGramatical, ...] | None = None) -> None:
        self.regras = regras or (
            RegraConcordanciaDeterminanteNome(),
            RegraConcordanciaNomeAdjetivo(),
            RegraConcordanciaVerboSujeito(),
            RegraCategoriaIncompativel(),
        )

    def verificar(self, analises: tuple[AnaliseToken, ...]) -> tuple[Diagnostico, ...]:
        return tuple(
            diagnostico
            for regra in self.regras
            for diagnostico in regra.verificar(analises)
        )

    def reconhecer_constituintes(
        self, analises: tuple[AnaliseToken, ...]
    ) -> tuple[Constituinte, ...]:
        constituintes: list[Constituinte] = []
        for segmento in _segmentos_frase(analises):
            indice_verbo = next(
                (
                    i
                    for i, analise in enumerate(segmento)
                    if _leitura_de_classe(analise, ClasseGramatical.VERBO) is not None
                ),
                None,
            )
            if indice_verbo is None:
                continue
            palavras_antes = [
                item for item in segmento[:indice_verbo]
                if item.token.texto.strip() and item.token.texto not in ",;:"
            ]
            do_verbo_em_diante = [
                item for item in segmento[indice_verbo:]
                if item.token.texto not in ".!?,;:"
            ]
            if palavras_antes:
                constituintes.append(
                    Constituinte(
                        "sujeito",
                        " ".join(item.token.texto for item in palavras_antes),
                        palavras_antes[0].token.inicio,
                        palavras_antes[-1].token.fim,
                    )
                )
            if do_verbo_em_diante:
                constituintes.append(
                    Constituinte(
                        "predicado",
                        " ".join(item.token.texto for item in do_verbo_em_diante),
                        do_verbo_em_diante[0].token.inicio,
                        do_verbo_em_diante[-1].token.fim,
                    )
                )
        return tuple(constituintes)


def _segmentos_frase(
    analises: tuple[AnaliseToken, ...]
) -> tuple[tuple[AnaliseToken, ...], ...]:
    segmentos: list[tuple[AnaliseToken, ...]] = []
    atual: list[AnaliseToken] = []
    for analise in analises:
        if analise.token.texto in ".!?":
            if atual:
                segmentos.append(tuple(atual))
                atual = []
            continue
        atual.append(analise)
    if atual:
        segmentos.append(tuple(atual))
    return tuple(segmentos)
