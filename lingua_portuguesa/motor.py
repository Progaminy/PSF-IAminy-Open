"""Fachada do motor de língua portuguesa."""
from __future__ import annotations

from .fluxo import ConstrutorFluxoNatural
from .gramatica import AnalisadorGramatical
from .conhecimento_puro import ConceitoPortugues, ConstrutorConhecimentoPortugues
from .lexico import Dicionario
from .morfologia import AnalisadorMorfologico
from .normalizacao import normalizar_texto
from .ponte_matematica import (
    AuditoriaMatematicaPortugues,
    ComparacaoGramaticalFinita,
    PonteMatematicaPortugues,
    ProvaReescritaTerminologica,
)
from .tipos import AnaliseTexto, FluxoLinguistico
from .tokenizacao import Tokenizador


class MotorPortugues:
    """Orquestra o pipeline sem acoplar as suas etapas.

    Componentes podem ser injetados, permitindo trocar léxico, tokenizador ou
    regras gramaticais sem alterar a API de quem consome o motor.
    """

    def __init__(
        self,
        dicionario: Dicionario | None = None,
        tokenizador: Tokenizador | None = None,
        gramatica: AnalisadorGramatical | None = None,
    ) -> None:
        self.dicionario = dicionario or Dicionario.padrao()
        self.tokenizador = tokenizador or Tokenizador()
        self.morfologia = AnalisadorMorfologico(self.dicionario)
        self.gramatica = gramatica or AnalisadorGramatical()
        self.construtor_fluxo = ConstrutorFluxoNatural()
        self.conhecimento_portugues = ConstrutorConhecimentoPortugues()
        self.ponte_matematica = PonteMatematicaPortugues(self.conhecimento_portugues)

    def analisar(self, texto: str) -> AnaliseTexto:
        tokens = self.tokenizador.tokenizar(texto)
        morfologia = self.morfologia.analisar(tokens)
        diagnosticos = self.gramatica.verificar(morfologia)
        constituintes = self.gramatica.reconhecer_constituintes(morfologia)
        fluxo = self.construtor_fluxo.construir(
            texto, tokens, morfologia, diagnosticos, constituintes
        )
        return AnaliseTexto(
            texto=texto,
            texto_normalizado=normalizar_texto(texto),
            tokens=tokens,
            morfologia=morfologia,
            diagnosticos=diagnosticos,
            constituintes=constituintes,
            fluxo=fluxo,
        )

    def ler(self, texto: str) -> AnaliseTexto:
        """Leitura operacional: conserva o texto e devolve análise auditável."""
        return self.analisar(texto)

    def interpretar_sentido(self, texto: str) -> dict[str, object]:
        """Interpretação interna limitada ao léxico e à gramática materializados."""
        analise = self.analisar(texto)
        lemas = tuple(
            item.leituras[0].lema
            for item in analise.morfologia
            if item.leituras
        )
        return {
            "texto": texto,
            "lemas_reconhecidos": lemas,
            "diagnosticos": tuple(d.mensagem for d in analise.diagnosticos),
            "limite": "Não inventa contexto externo nem intenção não sustentada pelo texto.",
        }

    def revisar_escrita(self, texto: str) -> dict[str, object]:
        """Revisa sem apagar o original e sem aplicar correção silenciosa."""
        analise = self.analisar(texto)
        return {
            "original": texto,
            "normalizado_para_analise": analise.texto_normalizado,
            "diagnosticos": tuple(d.mensagem for d in analise.diagnosticos),
            "estado": "REVISÃO_ASSISTIDA; nenhuma alteração automática foi imposta",
        }

    def produzir_texto(self, unidades: tuple[str, ...] | list[str]) -> str:
        """Compõe unidades fornecidas; não inventa factos ou conteúdo ausente."""
        partes: list[str] = []
        for unidade in unidades:
            trecho = " ".join(str(unidade).strip().split())
            if not trecho:
                continue
            if trecho[-1] not in ".!?":
                trecho += "."
            partes.append(trecho)
        return " ".join(partes)

    def escrever(self, unidades: tuple[str, ...] | list[str]) -> str:
        """Alias explícito de produção textual controlada."""
        return self.produzir_texto(unidades)

    def fluxo_natural(self, texto: str) -> FluxoLinguistico:
        """Devolve a escada som → letra → palavra → significado → texto."""
        fluxo = self.analisar(texto).fluxo
        assert fluxo is not None
        return fluxo

    def explicar_fluxo(self, texto: str) -> tuple[str, ...]:
        fluxo = self.fluxo_natural(texto)
        return tuple(
            f"{estagio.ordem}. {estagio.nome}: {estagio.descricao} "
            f"({estagio.quantidade})"
            for estagio in fluxo.estagios
        )


    def conhecimento_puro(self) -> tuple[ConceitoPortugues, ...]:
        """Devolve os conceitos puros de Português construídos no PSF."""
        return self.conhecimento_portugues.todos()

    def caminho_conhecimento_portugues(self) -> tuple[str, ...]:
        """Caminho natural: diferença → som → grafema → palavra → texto."""
        return self.conhecimento_portugues.caminho_natural()

    def funcionamento_portugues(self) -> tuple[str, ...]:
        """Funcionamento objetivo do conhecimento de Português no motor."""
        return self.conhecimento_portugues.funcionamento()

    def definir_conceito_puro(self, nome: str) -> str | None:
        conceito = self.conhecimento_portugues.buscar(nome)
        if conceito is None:
            return None
        return conceito.construcao

    def funcao_conceito_puro(self, nome: str) -> str | None:
        conceito = self.conhecimento_portugues.buscar(nome)
        if conceito is None:
            return None
        return conceito.funcao

    def dependencias_conceito_puro(self, nome: str) -> tuple[str, ...]:
        return self.conhecimento_portugues.dependencias_de(nome)

    def trilho_ate_conceito_puro(self, nome: str) -> tuple[str, ...]:
        return self.conhecimento_portugues.trilho_ate(nome)

    def lacunas_conhecimento_portugues(self) -> tuple[str, ...]:
        return self.conhecimento_portugues.lacunas()

    def fronteiras_abertas_portugues(self) -> dict[str, str]:
        """Fronteiras do português vivo que dependem de contexto ou dados reais."""
        return self.conhecimento_portugues.fronteiras_abertas()

    def limites_operacionais_portugues(self) -> dict[str, str]:
        """Conceitos construídos cuja automatização ainda pode ser parcial."""
        return self.conhecimento_portugues.limites_operacionais()

    def mestria_conceitual_portugues(self) -> bool:
        """Confirma domínio interno sem lacunas, sem prometer mundo fechado."""
        return self.conhecimento_portugues.mestria_conceitual()

    def dependencias_transitivas_conceito_puro(self, nome: str) -> tuple[str, ...]:
        """Devolve todas as dependências anteriores necessárias ao conceito."""
        return self.conhecimento_portugues.dependencias_transitivas_de(nome)

    def temas_consulta_conhecimento_portugues(self) -> tuple[str, ...]:
        """Lista índices temáticos sem lhes dar autoridade estrutural."""
        return self.conhecimento_portugues.temas_consulta()

    def conceitos_por_tema(self, tema: str) -> tuple[ConceitoPortugues, ...]:
        """Consulta por tema; a linha real continua definida por ordem e dependências."""
        return self.conhecimento_portugues.por_tema(tema)

    def camadas_conhecimento_portugues(self) -> tuple[str, ...]:
        """Compatibilidade legada. As antigas camadas são apenas temas de consulta."""
        return self.temas_consulta_conhecimento_portugues()

    def conceitos_por_camada(self, camada: str) -> tuple[ConceitoPortugues, ...]:
        """Compatibilidade legada. Use :meth:`conceitos_por_tema`."""
        return self.conceitos_por_tema(camada)

    def buscar_conceitos_puros(self, trecho: str) -> tuple[ConceitoPortugues, ...]:
        """Busca por nome, construção ou função dentro do conhecimento puro."""
        return self.conhecimento_portugues.buscar_texto(trecho)

    def estatisticas_conhecimento_portugues(self) -> dict[str, int]:
        """Mede o conhecimento materializado sem fingir completude."""
        return self.conhecimento_portugues.estatisticas()

    def aliases_conhecimento_portugues(self) -> dict[str, str]:
        """Termos equivalentes que apontam para um conceito canónico único."""
        return self.conhecimento_portugues.aliases()

    def auditar_estrutura_portugues(self) -> AuditoriaMatematicaPortugues:
        """Usa relações e grafos como validação, nunca como fonte linguística."""
        return self.ponte_matematica.auditar_dependencias()

    def caminho_minimo_conceito_puro(self, nome: str) -> tuple[str, ...]:
        """Menor caminho real de dependências até um conceito."""
        return self.ponte_matematica.caminho_minimo_ate(nome)

    def conceitos_estruturais_portugues(self, limite: int = 10) -> tuple[tuple[str, int], ...]:
        """Conceitos que sustentam mais dependentes diretos."""
        return self.ponte_matematica.conceitos_estruturais(limite)

    def comparar_padrao_gramatical_finito(
        self, texto: str, limite_passos: int = 12
    ) -> ComparacaoGramaticalFinita:
        """Compara, sem declarar completude, o padrão morfológico do texto."""
        return self.ponte_matematica.comparar_gramatica_finita(
            self.analisar(texto), limite_passos
        )

    def provar_equivalencia_terminologica(
        self, termo: str
    ) -> ProvaReescritaTerminologica:
        """Mostra a reescrita auditável de alias para conceito canónico."""
        return self.ponte_matematica.provar_alias(termo)

    def definir(self, palavra: str) -> tuple[str, ...]:
        return self.dicionario.definir(palavra)

    def sugerir(self, palavra: str, limite: int = 5) -> tuple[str, ...]:
        return self.dicionario.sugerir(palavra, limite)

    def estatisticas_lexico(self) -> dict[str, int]:
        """Resumo do dicionário interno, útil para auditoria do português amplo."""
        return {
            "lemas": len(self.dicionario.lemas()),
            "formas": self.dicionario.total_formas(),
            "leituras": len(self.dicionario),
        }
