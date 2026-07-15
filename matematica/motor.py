"""Fachada única do conhecimento matemático PSF."""
from __future__ import annotations

from .candidatos import todos_candidatos
from .conhecimento import ConhecimentoMatematico
from .expressao import resolver_expressao
from .tipos import MonografiaPSF, ProvaFinita, ReconstrucaoMatematica, ResolucaoMatematica


class MotorMatematica:
    """Usa o conhecimento matemático para reconstruir, calcular, provar e consolidar.

    O motor não declara que um catálogo antigo é conhecimento. Material legado
    entra somente como candidato de reconstrução.
    """

    def __init__(self, conhecimento: ConhecimentoMatematico | None = None) -> None:
        self.conhecimento = conhecimento or ConhecimentoMatematico()

    def conhecimento_puro(self):
        return self.conhecimento.todos()

    def buscar(self, trecho: str):
        return self.conhecimento.buscar_texto(trecho)

    def auditar(self):
        return self.conhecimento.auditar()

    def auditar_pontes(self):
        return self.conhecimento.auditar_pontes()

    def calcular(
        self,
        expressao: str,
        casas_decimais: int | None = None,
        modo: str = "truncar",
    ) -> ResolucaoMatematica:
        return resolver_expressao(expressao, casas_decimais=casas_decimais, modo=modo)

    def reconstruir(self, assunto: str) -> ReconstrucaoMatematica:
        conceito = self.conhecimento.buscar(assunto)
        if conceito is None:
            termos = {t for t in assunto.lower().split() if len(t) > 2}
            candidatos = []
            for item in self.conhecimento.todos():
                nome_termos = {t for t in item.nome.lower().split() if len(t) > 2}
                comuns = termos & nome_termos
                if comuns and len(comuns) >= max(1, (len(termos) + 1) // 2):
                    candidatos.append((len(comuns), item))
            candidatos.sort(key=lambda par: (-par[0], par[1].nome))
            if len(candidatos) == 1 or (len(candidatos) > 1 and candidatos[0][0] > candidatos[1][0]):
                conceito = candidatos[0][1]
        if conceito is None:
            return ReconstrucaoMatematica(
                conceito=None,
                estado="NÃO_MATERIALIZADO",
                trilho_documental=(),
                explicacao=(
                    "O assunto ainda não foi localizado como conceito matemático puro.",
                    "Ele pode entrar como candidato, mas não como resposta pronta.",
                ),
                limites=("É necessário reconstruir dependências e testes antes de declarar conhecimento.",),
            )
        if not conceito.eh_conhecimento_psf:
            return ReconstrucaoMatematica(
                conceito=conceito,
                estado="BLOQUEADO_SEM_PONTE_DE_CONHECIMENTO",
                trilho_documental=(),
                explicacao=(
                    f"O conceito {conceito.nome} existe no inventário, mas não possui ponte de entrada.",
                    "Nenhuma fórmula ou conclusão isolada pode ser usada como conhecimento PSF.",
                ),
                limites=("Construir e validar dependências anteriores antes de liberar o conceito.",),
            )
        explicacao = (
            f"Conceito: {conceito.nome}.",
            f"Construção: {conceito.construcao}",
            "O marcador histórico serve apenas para localizar o documento.",
        )
        return ReconstrucaoMatematica(
            conceito=conceito,
            estado="RECONSTRUÇÃO_MATERIALIZADA",
            trilho_documental=conceito.dependencias_declaradas,
            explicacao=explicacao,
            limites=(() if conceito.implementacoes and conceito.testes else ("Implementação ou teste não foi extraído completamente.",)),
        )

    def provar(self, enunciado: str) -> ReconstrucaoMatematica:
        """Primeira prova auditável: localizar construção e seus suportes.

        Provas formais específicas continuam nos módulos de lógica, reescrita e
        busca finita. Esta fachada nunca transforma simples localização em prova.
        """
        r = self.reconstruir(enunciado)
        if r.conceito is None:
            return r
        if not r.conceito.testes:
            return ReconstrucaoMatematica(
                conceito=r.conceito,
                estado="CONSTRUÍDO_MAS_PROVA_NÃO_CERTIFICADA",
                trilho_documental=r.trilho_documental,
                explicacao=r.explicacao,
                limites=("Nenhum teste/prova documental foi extraído para este conceito.",),
            )
        return ReconstrucaoMatematica(
            conceito=r.conceito,
            estado="CONSTRUÇÃO_COM_CERTIFICADO_DE_TESTE",
            trilho_documental=r.trilho_documental,
            explicacao=r.explicacao + tuple(f"Teste: {t}" for t in r.conceito.testes),
            limites=("Teste executável não equivale automaticamente a prova universal.",),
        )

    def provar_finito(self, premissas: tuple[object, ...], conclusao: object) -> ProvaFinita:
        """Busca e verifica uma derivação no fragmento lógico finito suportado.

        Esta é prova formal real dentro do fragmento implementado; não é uma
        promessa de provar qualquer enunciado matemático.
        """
        from nucleo.busca_prova_finita import BUSCA_DERIVACAO_FINITA
        from nucleo.teoria_modelos_prova_finita import DERIVACAO_VALIDA

        passos = BUSCA_DERIVACAO_FINITA(tuple(premissas), conclusao)
        if passos is None:
            return ProvaFinita(
                estado="NÃO_DERIVADO_NO_FRAGMENTO_FINITO",
                premissas=tuple(premissas),
                conclusao=conclusao,
                passos=(),
                valida=False,
                limite="Falha da busca finita não prova que o enunciado é falso ou impossível fora do fragmento.",
            )
        valor = DERIVACAO_VALIDA(passos)
        valida = bool(valor(True)(False))
        return ProvaFinita(
            estado="PROVA_FINITA_CERTIFICADA" if valida else "DERIVAÇÃO_ENCONTRADA_MAS_INVÁLIDA",
            premissas=tuple(premissas),
            conclusao=conclusao,
            passos=tuple(passos),
            valida=valida,
            limite="Certificado válido apenas no fragmento lógico finito implementado.",
        )

    def produzir_monografia(self, assunto: str) -> MonografiaPSF:
        r = self.reconstruir(assunto)
        if r.conceito is None:
            texto = (
                f"# {assunto}\n\n"
                "## Estado\n\nNão materializado como conhecimento puro.\n\n"
                "## Plano de reconstrução\n\n"
                "1. Identificar objetos mínimos.\n2. Construir dependências.\n"
                "3. Recriar cálculos e fórmulas.\n4. Comparar.\n5. Testar.\n"
            )
            return MonografiaPSF(assunto, "PLANO_DE_RECONSTRUÇÃO", texto, (), r.limites)
        c = r.conceito
        deps = "\n".join(f"- {d}" for d in c.dependencias_declaradas) or "- Nenhuma dependência extraída."
        impl = "\n".join(f"- {i}" for i in c.implementacoes) or "- Não extraída."
        testes = "\n".join(f"- {t}" for t in c.testes) or "- Não extraído."
        texto = f"""# {c.nome.title()}

## Estado PSF

Reconstrução baseada em conhecimento materializado; não é cópia de monografia pronta.

## Construção

{c.construcao}

## Dependências declaradas

{deps}

## Implementação

{impl}

## Testes e prova disponível

{testes}

## Limites

- O número do antigo ficheiro ETAPA é apenas localização histórica.
- Fórmulas conhecidas devem ser desmontadas e reconstruídas antes de serem usadas como fundamento.
"""
        return MonografiaPSF(c.nome, "CONSOLIDAÇÃO_PSF", texto, (c.nome,), r.limites)

    def candidatos_de_reconstrucao(self) -> tuple[str, ...]:
        return todos_candidatos()

    def hipoteses_pendentes(self):
        from .hipoteses import hipoteses_pendentes

        return hipoteses_pendentes()

    def estudar_hipotese(self, identificador: str):
        from .hipoteses import obter_hipotese

        return obter_hipotese(identificador)
