"""Leitura do conhecimento matemático materializado.

Os nomes ``ETAPA_*.md`` são marcadores históricos de localização. O motor não
aceita o número como prova, verdade ou dependência. A autoridade vem do conteúdo
construído, das dependências declaradas, da implementação e dos testes reais.
"""
from __future__ import annotations

from pathlib import Path
import re

from .tipos import AuditoriaMatematica, ConceitoMatematico
from .pontes import auditar_pontes, ponte_historica
from .resolucao_pontes import auditar_resolucao_pontes

_RAIZ = Path(__file__).resolve().parents[1]
_CONHECIMENTO = _RAIZ / "conhecimento"
_PADRAO = re.compile(r"ETAPA_(\d{2,4})(?:_(\d{2,4}))?_(.+)\.md$")
_BLOCO = re.compile(r"```text\s*\n(.*?)\n```", re.S)


def _titulo_para_nome(titulo: str) -> str:
    return " ".join(titulo.replace("_", " ").strip().lower().split())


def _secao(texto: str, titulo: str) -> str:
    padrao = re.compile(
        rf"^##\s+{re.escape(titulo)}\s*$\n(.*?)(?=^##\s+|\Z)",
        re.M | re.S | re.I,
    )
    m = padrao.search(texto)
    return m.group(1).strip() if m else ""


def _itens(secao: str) -> tuple[str, ...]:
    itens = []
    for linha in secao.splitlines():
        linha = linha.strip()
        if linha.startswith("-"):
            valor = linha[1:].strip().rstrip(";")
            if valor:
                # Documentos antigos juntavam várias dependências por ponto e
                # vírgula. Cada origem precisa ser auditável separadamente.
                partes = [p.strip().rstrip(".") for p in valor.split(";") if p.strip()]
                itens.extend(partes)
    return tuple(itens)


def _referencias(secao: str) -> tuple[str, ...]:
    encontrados: list[str] = []
    for bloco in _BLOCO.findall(secao):
        for linha in bloco.splitlines():
            valor = linha.strip().strip("`")
            if valor and ("/" in valor or valor.endswith(".py")):
                encontrados.append(valor)
    return tuple(dict.fromkeys(encontrados))


_CRASE_INLINE = re.compile(r"`([^`\n]+)`")


def _referencias_ampla(secao: str) -> tuple[str, ...]:
    """Como `_referencias`, aceitando também caminho em crase dentro de frase.

    Documentos anteriores à convenção `## Implementação` às vezes escrevem
    o caminho embutido em prosa — "Implementado em `nucleo/x.py` e validado
    em `testes/test_x.py`." — em vez de bloco ```text```. Não é uma segunda
    forma de conhecimento nem um caminho novo: é o mesmo caminho de
    arquivo, só formatado de outro jeito. Sem isto, implementação e teste
    reais ficam invisíveis para a auditoria só por causa do formato do
    documento, nunca por faltar construção real.
    """
    encontrados: list[str] = list(_referencias(secao))
    for valor in _CRASE_INLINE.findall(secao):
        valor = valor.strip()
        if valor and ("/" in valor or valor.endswith(".py")):
            encontrados.append(valor)
    return tuple(dict.fromkeys(encontrados))


# Nomes de seção historicamente usados antes de "## Implementação" e
# "## Validação" existirem como convenção. Mesmo princípio de
# `ponte_historica`: cobre só formato antigo, nunca substitui a seção
# canônica quando ela existe.
_SECOES_IMPLEMENTACAO_HISTORICAS = ("Arquivo implementado", "No projeto", "Ficheiros")
_SECOES_VALIDACAO_HISTORICAS = ("Validação externa mínima", "Validação contra factos independentes")
_SECAO_COMBINADA_HISTORICA = "Forma operacional no projeto"

# Seções inequivocamente de metadado (dependência, implementação,
# validação), nunca de derivação. Usadas só para saber onde a derivação
# termina no formato antigo — nunca para decidir se ela existe.
_SECOES_METADADOS_CORTE = (
    "Dependências permitidas",
    "Dependências proibidas",
    "Dependências proibidas nesta etapa",
    "Base permitida",
    "Implementação",
    "Validação",
    _SECAO_COMBINADA_HISTORICA,
    *_SECOES_IMPLEMENTACAO_HISTORICAS,
    *_SECOES_VALIDACAO_HISTORICAS,
)


def _construcao_por_corte(texto: str) -> str:
    """Último recurso: tudo entre o título e a primeira seção de metadado.

    Documentos anteriores à convenção "## Construção pura" registram a
    derivação sob nomes variados (Lei, Definição, Posição no fluxo
    natural, Etapas registadas, Ideia, Teorema...) em vez de um único
    cabeçalho comum. Em vez de perseguir cada nome um a um, corta no
    primeiro cabeçalho que já é reconhecidamente metadado (dependência,
    implementação, validação) e trata tudo antes disso como a derivação
    real do documento — que já existia, só não estava rotulada.
    """
    posicoes = []
    for titulo in _SECOES_METADADOS_CORTE:
        m = re.search(rf"(?m)^##\s+{re.escape(titulo)}\s*$", texto, re.I)
        if m:
            posicoes.append(m.start())
    if not posicoes:
        # Nenhuma seção de metadado encontrada: o documento inteiro é a
        # derivação, sem seção separada nenhuma (formato mais antigo).
        return texto.strip()
    return texto[: min(posicoes)].strip()


class ConhecimentoMatematico:
    """Inventário vivo da matemática já materializada."""

    def __init__(self, base: Path | None = None) -> None:
        self.base = base or _CONHECIMENTO
        self._conceitos = self._carregar()
        self._por_nome = {c.nome: c for c in self._conceitos}

    def _carregar(self) -> tuple[ConceitoMatematico, ...]:
        saida: list[ConceitoMatematico] = []
        for arquivo in sorted(self.base.glob("ETAPA_*.md")):
            m = _PADRAO.match(arquivo.name)
            if not m:
                continue
            inicio = int(m.group(1))
            fim = int(m.group(2)) if m.group(2) else None
            nome = _titulo_para_nome(m.group(3))
            texto = arquivo.read_text(encoding="utf-8")
            construcao = _secao(texto, "Construção pura")
            if not construcao:
                construcao = _secao(texto, "Construção")
            if not construcao:
                construcao = _construcao_por_corte(texto)
            dependencias = _itens(_secao(texto, "Dependências permitidas"))
            if not dependencias:
                dependencias = _itens(_secao(texto, "Base permitida"))
            if not dependencias:
                ponte = ponte_historica(str(arquivo.relative_to(_RAIZ)), nome)
                if ponte is not None:
                    dependencias = ponte.origens
            exemplos_minimos = _itens(_secao(texto, "Exemplo"))
            if not exemplos_minimos:
                exemplos_minimos = _itens(_secao(texto, "Exemplos"))
            implementacoes = _referencias_ampla(_secao(texto, "Implementação"))
            testes = _referencias_ampla(_secao(texto, "Validação"))
            if not implementacoes or not testes:
                # "Forma operacional no projeto" é uma frase estruturada e
                # limpa ("Implementado em X e validado em Y") — mais
                # confiável que seções de discussão que só mencionam outro
                # arquivo de passagem. Por isso vem antes dos sinônimos
                # soltos abaixo, não depois.
                combinada = _referencias_ampla(_secao(texto, _SECAO_COMBINADA_HISTORICA))
                if not implementacoes:
                    implementacoes = tuple(p for p in combinada if p.startswith("nucleo/"))
                if not testes:
                    testes = tuple(p for p in combinada if p.startswith("testes/"))
            for titulo in _SECOES_IMPLEMENTACAO_HISTORICAS:
                if implementacoes:
                    break
                implementacoes = _referencias_ampla(_secao(texto, titulo))
            for titulo in _SECOES_VALIDACAO_HISTORICAS:
                if testes:
                    break
                testes = _referencias_ampla(_secao(texto, titulo))
            if not implementacoes or not testes:
                # Último recurso: alguns documentos citam "Módulo operacional:"
                # e "Teste:" fora de qualquer seção "##" (logo após o título).
                # Em vez de perseguir mais um nome de cabeçalho, procura o
                # caminho no documento inteiro — só aceita o que já é um
                # caminho real de nucleo/ ou testes/, nunca inventa um novo.
                documento_inteiro = _referencias_ampla(texto)
                if not implementacoes:
                    implementacoes = tuple(p for p in documento_inteiro if p.startswith("nucleo/"))
                if not testes:
                    testes = tuple(p for p in documento_inteiro if p.startswith("testes/"))
            marcador = inicio if fim is None else inicio
            saida.append(
                ConceitoMatematico(
                    nome=nome,
                    construcao=construcao or "Construção ainda não extraída do documento.",
                    dependencias_declaradas=dependencias,
                    implementacoes=implementacoes,
                    testes=testes,
                    arquivo=str(arquivo.relative_to(_RAIZ)),
                    marcador_historico=marcador,
                    exemplos_minimos=exemplos_minimos,
                )
            )
        return tuple(saida)

    def todos(self) -> tuple[ConceitoMatematico, ...]:
        return self._conceitos

    def buscar(self, nome: str) -> ConceitoMatematico | None:
        chave = " ".join(nome.lower().strip().split())
        if chave in self._por_nome:
            return self._por_nome[chave]
        candidatos = [c for c in self._conceitos if chave in c.nome or c.nome in chave]
        return candidatos[0] if len(candidatos) == 1 else None

    def buscar_texto(self, trecho: str) -> tuple[ConceitoMatematico, ...]:
        tokens = {t for t in re.findall(r"[\wáéíóúâêôãõç]+", trecho.lower()) if len(t) > 2}
        pontuados: list[tuple[int, ConceitoMatematico]] = []
        for conceito in self._conceitos:
            alvo = " ".join((conceito.nome, conceito.construcao)).lower()
            pontos = sum(1 for token in tokens if token in alvo)
            if pontos:
                pontuados.append((pontos, conceito))
        pontuados.sort(key=lambda item: (-item[0], item[1].nome))
        return tuple(c for _, c in pontuados)

    def auditar(self) -> AuditoriaMatematica:
        nomes: dict[str, int] = {}
        marcadores: dict[int, int] = {}
        impl_ausentes: list[str] = []
        testes_ausentes: list[str] = []
        for c in self._conceitos:
            nomes[c.nome] = nomes.get(c.nome, 0) + 1
            if c.marcador_historico is not None:
                marcadores[c.marcador_historico] = marcadores.get(c.marcador_historico, 0) + 1
            for ref in c.implementacoes:
                if not (_RAIZ / ref).exists():
                    impl_ausentes.append(f"{c.nome}: {ref}")
            for ref in c.testes:
                if not (_RAIZ / ref).exists():
                    testes_ausentes.append(f"{c.nome}: {ref}")
        duplicados = tuple(sorted(nome for nome, n in nomes.items() if n > 1))
        repetidos = tuple(sorted(numero for numero, n in marcadores.items() if n > 1))
        observacoes = (
            "ETAPA é marcador histórico de localização, não camada de verdade.",
            "A linha matemática é única; validade depende de construção, referências reais e testes.",
            "O grafo semântico completo de dependências ainda não está materializado em formato canónico.",
        )
        return AuditoriaMatematica(
            conceitos=len(self._conceitos),
            nomes_duplicados=duplicados,
            referencias_de_implementacao_ausentes=tuple(sorted(set(impl_ausentes))),
            referencias_de_teste_ausentes=tuple(sorted(set(testes_ausentes))),
            marcadores_historicos_repetidos=repetidos,
            linha_unica=not duplicados,
            observacoes=observacoes,
        )

    def auditar_pontes(self) -> dict[str, object]:
        """Confirma que nenhum conceito inventariado ficou isolado."""
        basica = auditar_pontes(self._conceitos)
        basica["resolucao_profunda"] = auditar_resolucao_pontes(self._conceitos)
        return basica
