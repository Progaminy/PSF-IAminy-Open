"""Motor auxiliar compartilhado de comparação, validação e otimização.

Pode usar recursos da biblioteca padrão para ganhar tempo. Nunca substitui o
MotorMatematica, o MotorPortugues ou o conhecimento puro de cada domínio.
"""
from __future__ import annotations

import unicodedata
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from difflib import SequenceMatcher
from typing import Any

from .motor_calculo_python import CALCULADORA, comparar_valores


@dataclass(frozen=True, slots=True)
class ResultadoAuxiliar:
    dominio: str
    tarefa: str
    estado: str
    aprovado: bool | None
    referencia: str | None
    detalhes: tuple[str, ...]
    aviso: str = "Motor auxiliar compara e otimiza; não cria conhecimento PSF."


class MotorAuxiliarValidacao:
    """Um único auxiliar com adaptadores independentes para os dois domínios."""

    def __init__(self) -> None:
        self._cache: dict[tuple[str, str], Any] = {}

    @staticmethod
    def _decimal_psf(texto: str | None) -> Decimal | None:
        if texto is None:
            return None
        limpo = texto.strip().replace(",", ".")
        try:
            if "/" in limpo:
                a, b = limpo.split("/", 1)
                return Decimal(a) / Decimal(b)
            return Decimal(limpo)
        except (InvalidOperation, ZeroDivisionError, ValueError):
            return None

    def validar_matematica(self, expressao: str, resolucao) -> ResultadoAuxiliar:
        if resolucao.resultado is None:
            return ResultadoAuxiliar(
                "matemática",
                "comparar cálculo",
                "SEM_RESULTADO_PSF_PARA_COMPARAR",
                None,
                None,
                tuple(resolucao.limites),
            )
        expressao_python = expressao.replace(":", "/").split(" com ", 1)[0].strip()
        try:
            referencia = CALCULADORA.calcular(expressao_python)
        except Exception as erro:  # comparador não deve derrubar o motor puro
            return ResultadoAuxiliar(
                "matemática",
                "comparar cálculo",
                "REFERÊNCIA_EXTERNA_FALHOU",
                None,
                None,
                (str(erro),),
            )
        valor_psf = self._decimal_psf(resolucao.resultado)
        if valor_psf is None:
            return ResultadoAuxiliar(
                "matemática",
                "comparar cálculo",
                "RESULTADO_PSF_NÃO_CONVERTÍVEL",
                None,
                str(referencia),
                (f"resultado PSF: {resolucao.resultado}",),
            )
        tolerancia = self._tolerancia_para(resolucao)
        comparacao = comparar_valores(valor_psf, referencia, tolerancia=tolerancia)
        # Casas decimais definem uma margem ABSOLUTA na última casa, não
        # uma percentagem do tamanho do número. O comparador genérico aceita
        # erro absoluto OU relativo; mantemos esse comportamento histórico
        # somente quando nenhuma precisão decimal foi pedida.
        aprovado = (
            comparacao.erro_absoluto <= tolerancia
            if resolucao.casas_decimais is not None
            else comparacao.aprovado
        )
        return ResultadoAuxiliar(
            "matemática",
            "comparar cálculo",
            "APROVADO_POR_COMPARAÇÃO" if aprovado else "DIVERGÊNCIA_ENCONTRADA",
            aprovado,
            str(referencia),
            (
                f"valor PSF: {resolucao.resultado}",
                f"erro absoluto: {comparacao.erro_absoluto}",
                f"erro relativo: {comparacao.erro_relativo}",
                f"tolerância usada: {tolerancia} "
                f"(casas pedidas: {resolucao.casas_decimais}, modo: {resolucao.modo_aproximacao or 'exato'})",
            ),
        )

    @staticmethod
    def _tolerancia_para(resolucao) -> float:
        """Tolerância derivada da precisão que o PSF de facto usou.

        Achado real (auditoria externa, confirmado por execução): antes,
        toda comparação usava tolerância fixa 1e-9 contra uma referência
        Python NÃO arredondada -- então "2:3 com 3 casas arredondado"
        (PSF: 0,667, correto) sempre reportava DIVERGÊNCIA_ENCONTRADA
        (erro ~0,00033 contra o 0,6666... cru), mesmo a instrução de
        arredondamento sendo lida e descartada antes da comparação. A
        informação de quantas casas e qual modo já existia estruturada em
        `resolucao.casas_decimais`/`resolucao.modo_aproximacao`
        (`matematica/tipos.py`), só nunca era lida aqui.

        Quando não há pedido de casas (`casas_decimais is None`), o
        comportamento continua exatamente 1e-9, como sempre foi.
        """
        casas = resolucao.casas_decimais
        if casas is None:
            return 1e-9
        if resolucao.modo_aproximacao == "truncar":
            # truncamento sempre arredonda para baixo (em módulo); o erro
            # máximo é quase uma unidade cheia da última casa pedida.
            return 10 ** (-casas)
        # arredondamento correto erra no máximo meia unidade da última
        # casa pedida -- é a definição matemática de arredondar.
        return 0.5 * 10 ** (-casas)

    def validar_aproximacao_irracional(
        self,
        nome: str,
        inferior: tuple[int, int],
        superior: tuple[int, int],
        referencia_python: str,
    ) -> ResultadoAuxiliar:
        """Confere um intervalo racional já construído e testado pelo PSF.

        Não decide, arredonda nem escolhe o intervalo: recebe o par
        (inferior, superior) que a lei geradora PSF (com módulo de
        convergência) já certificou como encaixado, e só usa a precisão
        otimizada da biblioteca padrão (Decimal, 80 dígitos) para conferir
        se a referência cai dentro dele e medir a largura obtida. Serve só
        para conhecimento que o PSF já tem puro, consolidado e com ponte —
        nunca para decidir um intervalo que o PSF ainda não construiu.
        """
        try:
            referencia = CALCULADORA.calcular(referencia_python)
        except Exception as erro:  # comparador não deve derrubar o motor puro
            return ResultadoAuxiliar(
                "matemática",
                "validar aproximação irracional",
                "REFERÊNCIA_EXTERNA_FALHOU",
                None,
                None,
                (str(erro),),
            )
        inf = Decimal(inferior[0]) / Decimal(inferior[1])
        sup = Decimal(superior[0]) / Decimal(superior[1])
        referencia_decimal = Decimal(str(referencia))
        contido = inf <= referencia_decimal <= sup
        return ResultadoAuxiliar(
            "matemática",
            "validar aproximação irracional",
            "REFERÊNCIA_DENTRO_DO_INTERVALO_PSF" if contido else "REFERÊNCIA_FORA_DO_INTERVALO_PSF",
            contido,
            str(referencia),
            (
                f"{nome}: intervalo PSF [{inf}, {sup}]",
                f"largura (precisão obtida): {sup - inf}",
                "Conter a referência é conferência de precisão, não prova PSF.",
            ),
        )

    @staticmethod
    def _normalizar_texto(texto: str) -> str:
        normalizado = unicodedata.normalize("NFKC", texto).casefold()
        return " ".join(normalizado.split())

    def comparar_portugues(self, original: str, produzido: str) -> ResultadoAuxiliar:
        a = self._normalizar_texto(original)
        b = self._normalizar_texto(produzido)
        semelhanca = SequenceMatcher(None, a, b).ratio()
        palavras_a = set(a.split())
        palavras_b = set(b.split())
        uniao = palavras_a | palavras_b
        intersecao = palavras_a & palavras_b
        cobertura = 1.0 if not uniao else len(intersecao) / len(uniao)
        return ResultadoAuxiliar(
            "português",
            "comparar textos",
            "COMPARAÇÃO_TEXTUAL_CONCLUÍDA",
            None,
            None,
            (
                f"semelhança de sequência: {semelhanca:.6f}",
                f"cobertura lexical: {cobertura:.6f}",
                "Semelhança não prova correção gramatical, sentido ou qualidade.",
            ),
        )

    def validar_estrutura_portugues(self, auditoria: dict[str, Any]) -> ResultadoAuxiliar:
        chaves_criticas = ("duplicacoes", "dependencias_ausentes", "dependencias_futuras", "ciclos")
        encontrados: list[str] = []
        for chave in chaves_criticas:
            valor = auditoria.get(chave, ())
            if valor:
                encontrados.append(f"{chave}: {valor}")
        aprovado = not encontrados
        return ResultadoAuxiliar(
            "português",
            "validar estrutura",
            "ESTRUTURA_APROVADA" if aprovado else "ESTRUTURA_COM_PENDÊNCIAS",
            aprovado,
            None,
            tuple(encontrados) if encontrados else ("nenhuma pendência estrutural crítica encontrada",),
        )

    def cachear(self, dominio: str, chave: str, valor: Any) -> None:
        self._cache[(dominio.lower(), chave)] = valor

    def recuperar_cache(self, dominio: str, chave: str) -> Any | None:
        return self._cache.get((dominio.lower(), chave))

    def auditar(self) -> dict[str, object]:
        return {
            "tipo": "auxiliar_externo_compartilhado",
            "fundamento_psf": False,
            "dominios": ("matemática", "português"),
            "funcoes": ("comparar", "validar", "medir", "cachear", "otimizar"),
            "itens_cache": len(self._cache),
        }
