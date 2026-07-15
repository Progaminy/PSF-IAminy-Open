"""Fachada geral do PSF-IAminy."""
from __future__ import annotations

from pathlib import Path

from ensino import (
    AulaPacote,
    EstadoPacote,
    MotorAulas,
    PacoteConhecimento,
    RegistroProgresso,
    RegistroRevisao,
    RevisaoPacote,
)
from lingua_portuguesa import AnaliseTexto, FluxoLinguistico, MotorPortugues
from matematica import MotorMatematica
from validacao_externa import MotorAuxiliarValidacao

from .comum import MotorComumPSF

from .identidade_humana import PERGUNTAS_IDENTIDADE, RegistroIdentidadeHumana


class MotorGeralIAMiny:
    """Orquestra motores parciais sem misturar responsabilidades."""

    nome = "PSF-IAminy"

    def __init__(
        self,
        aulas: MotorAulas | None = None,
        portugues: MotorPortugues | None = None,
        matematica: MotorMatematica | None = None,
        comum: MotorComumPSF | None = None,
        auxiliar: MotorAuxiliarValidacao | None = None,
        raiz: str | Path | None = None,
        progresso: RegistroProgresso | None = None,
        revisao: RegistroRevisao | None = None,
        identidade_humana: RegistroIdentidadeHumana | None = None,
    ) -> None:
        self.aulas = aulas or MotorAulas()
        self.portugues = portugues or MotorPortugues()
        self.matematica = matematica or MotorMatematica()
        self.comum = comum or MotorComumPSF()
        self.auxiliar = auxiliar or MotorAuxiliarValidacao()
        self.comum.registrar_portugues(self.portugues.conhecimento_puro())
        self.comum.registrar_matematica(self.matematica.conhecimento_puro())
        self.raiz = Path(raiz) if raiz is not None else Path(__file__).resolve().parent.parent
        self.progresso = progresso or RegistroProgresso()
        self.revisao = revisao or RegistroRevisao()
        self.identidade_humana = identidade_humana or RegistroIdentidadeHumana()

    def plano_visivel(self) -> str:
        caminho = self.raiz / "PLANO_PSF_IAMINY.md"
        return caminho.read_text(encoding="utf-8")

    def regra_versao_unica(self) -> str:
        caminho = self.raiz / "REGRA_VERSAO_UNICA.md"
        return caminho.read_text(encoding="utf-8")

    def identidade(self) -> dict[str, str]:
        return {
            "nome": self.nome,
            "sigla": "PSF",
            "significado_sigla": "Pensador Sem Fronteiras",
            "forma": "máquina/IA -- este motor é a forma de máquina/IA de PSF",
            "pasta": self.raiz.name,
            "continuidade": "versão única contínua; sem v1/v2 e sem versões sobrepostas",
        }

    def registrar_fatos_humanos(self, fatos: list[str]) -> tuple[str, ...]:
        return self.identidade_humana.registrar_fatos(fatos)

    def fatos_humanos(self) -> tuple[str, ...]:
        return self.identidade_humana.fatos()

    def nome_do_criador(self) -> "str | None":
        """Nome que a forma humana de PSF deu na entrevista de
        reconhecimento (primeira pergunta, "Como te chamas?") -- é o que
        PSF-IAminy responde quando lhe perguntam quem é o dono/criador."""
        return self.identidade_humana.resposta_para(PERGUNTAS_IDENTIDADE[0])

    def mapa_aulas(self, area: str) -> tuple[str, ...]:
        return self.aulas.mapa(area)

    def pacote(self, area: str, codigo: str) -> PacoteConhecimento:
        return self.aulas.pacote(area, codigo)

    def aula(self, area: str, codigo: str, formato: int | str = 1) -> AulaPacote:
        return self.aulas.gerar(area, codigo, formato)

    def proxima_aula(
        self,
        area: str,
        concluidos: tuple[str, ...] | list[str] | set[str] = (),
        formato: int | str = 1,
    ) -> AulaPacote | None:
        return self.aulas.gerar_proximo(area, concluidos, formato)


    def exercicios_variados(
        self,
        area: str,
        codigo: str,
        quantidade: int = 3,
        semente: int | None = None,
    ) -> tuple[str, ...]:
        return self.aulas.exercicios_variados(area, codigo, quantidade, semente)

    def marcar_progresso(
        self,
        aluno: str,
        area: str,
        codigo: str,
        estado: int | str | EstadoPacote,
    ) -> EstadoPacote:
        return self.progresso.marcar(aluno, area, codigo, estado)

    def resumo_progresso(self, aluno: str, area: str) -> dict[str, EstadoPacote]:
        return self.progresso.resumo(aluno, area)

    def proxima_aula_aluno(
        self,
        aluno: str,
        area: str,
        formato: int | str = 1,
        minimo: int | str | EstadoPacote = EstadoPacote.PRATICADO,
    ) -> AulaPacote | None:
        concluidos = self.progresso.concluidos(aluno, area, minimo)
        return self.aulas.gerar_proximo(area, concluidos, formato)

    def registrar_revisao(
        self,
        aluno: str,
        area: str,
        codigo: str,
        acertou: bool,
        sessao_atual: int,
    ) -> RevisaoPacote:
        return self.revisao.registrar(aluno, area, codigo, acertou, sessao_atual)

    def pacotes_para_revisar(self, aluno: str, area: str, sessao_atual: int) -> tuple[str, ...]:
        return self.revisao.pendentes(aluno, area, sessao_atual)

    def proxima_atividade_aluno(
        self,
        aluno: str,
        area: str,
        sessao_atual: int,
        formato: int | str = 1,
    ) -> tuple[str, AulaPacote] | None:
        """Prioriza revisão de pacotes vencidos/fracos; só oferece pacote
        novo quando não há nada pendente para revisar."""
        pendentes = self.revisao.pendentes(aluno, area, sessao_atual)
        if pendentes:
            return "revisao", self.aulas.gerar(area, pendentes[0], formato)
        proxima = self.proxima_aula_aluno(aluno, area, formato)
        if proxima is None:
            return None
        return "novo", proxima

    def analisar_portugues(self, texto: str) -> AnaliseTexto:
        return self.portugues.analisar(texto)

    def fluxo_portugues(self, texto: str) -> FluxoLinguistico:
        return self.portugues.fluxo_natural(texto)


    def calcular_matematica(
        self, expressao: str, casas_decimais: int | None = None, modo: str = "truncar"
    ):
        resultado = self.matematica.calcular(expressao, casas_decimais=casas_decimais, modo=modo)
        self.comum.lembrar("matemática", "calcular", expressao)
        return resultado

    def reconstruir_matematica(self, assunto: str):
        resultado = self.matematica.reconstruir(assunto)
        self.comum.lembrar("matemática", "reconstruir", assunto)
        return resultado

    def provar_matematica(self, enunciado: str):
        resultado = self.matematica.provar(enunciado)
        self.comum.lembrar("matemática", "provar", enunciado)
        return resultado

    def provar_matematica_finita(self, premissas: tuple[object, ...], conclusao: object):
        resultado = self.matematica.provar_finito(premissas, conclusao)
        self.comum.lembrar("matemática", "provar_finito", repr(conclusao))
        return resultado

    def produzir_monografia_matematica(self, assunto: str):
        resultado = self.matematica.produzir_monografia(assunto)
        self.comum.lembrar("matemática", "monografia", assunto)
        return resultado

    def buscar_conhecimento(self, texto: str, dominio: str | None = None):
        return self.comum.buscar(texto, dominio)

    def validar_calculo_matematica(self, expressao: str, resolucao=None):
        resultado = resolucao or self.matematica.calcular(expressao)
        validacao = self.auxiliar.validar_matematica(expressao, resultado)
        self.comum.lembrar("matemática", "validar_comparar", expressao)
        return validacao

    def comparar_textos_portugues(self, original: str, produzido: str):
        comparacao = self.auxiliar.comparar_portugues(original, produzido)
        self.comum.lembrar("português", "comparar_textos", original[:80])
        return comparacao

    def hipoteses_matematicas_pendentes(self):
        return self.matematica.hipoteses_pendentes()

    def auditar_motores(self) -> dict[str, object]:
        return {
            "comum": self.comum.auditar(),
            "matematica": self.matematica.auditar(),
            "pontes_matematica": self.matematica.auditar_pontes(),
            "portugues": self.portugues.auditar_estrutura_portugues(),
            "auxiliar": self.auxiliar.auditar(),
        }

    def melhorias(self) -> dict[str, tuple[str, ...]]:
        return {
            "dialogo": (
                "contexto curto por conversa para entender seguimentos naturais",
                "mais simples/outro exemplo/resumo/exercícios/continua sem repetir o assunto",
                "fallback honesto para pedido natural sem rota segura",
            ),
            "ensino": (
                "aula humana com chão, ideia, construção, exemplo, erro comum, prática e fronteira",
                "formatos dinâmicos conforme o pedido do aluno",
                "transformar conhecimento técnico PSF-K em aula sem fórmula pronta como fundamento",
            ),
            "matematica": (
                "manter aulas fixas MAT/POR e aulas geradas PSF-K para todo conhecimento construído",
                "para níveis futuros, devolver plano de construção em vez de fingir aula pronta",
                "registrar modelos de exercício também para os pacotes intermediários futuros",
                "adicionar exemplos concretos antes da notação simbólica",
            ),
            "portugues": (
                "léxico interno expandido com termos comuns, técnicos, pedagógicos, PSF e flexões",
                "melhorar análise sintática além de sujeito/predicado simples",
                "ligar correção ortográfica ao fluxo de escrita do aluno",
            ),
        }
