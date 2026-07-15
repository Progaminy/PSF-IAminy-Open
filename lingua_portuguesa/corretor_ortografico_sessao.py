"""Detetor ortográfico persistente do PSF — Etapa 36.

Regra permanente desta etapa:
antes de interpretar uma pergunta, o PSF deve passar a entrada por uma
camada conservadora de deteção/correção ortográfica.

A correção é conservadora porque não pode alterar a matemática:
- números ficam intactos;
- sinais como +, -, x, ÷, %, frações e horas ficam intactos;
- unidades monetárias e medidas ficam intactas;
- só palavras/frases conhecidas como erro são corrigidas.

Isto não usa internet, API, modelo externo nem biblioteca de IA. É memória
local + comparação textual simples + pares de correção aprovados.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from lingua_portuguesa.normalizacao import sem_acentos


@dataclass(frozen=True, slots=True)
class AlteracaoOrtografica:
    antes: str
    depois: str
    motivo: str = "correção aprovada"


@dataclass(frozen=True, slots=True)
class ResultadoOrtografico:
    original: str
    corrigido: str
    alteracoes: tuple[AlteracaoOrtografica, ...]

    @property
    def houve_correcao(self) -> bool:
        return bool(self.alteracoes)


# Pares aprovados. A lista deve crescer com cada sessão, mas sempre de modo
# explícito e rastreável. Não há correção automática agressiva.
CORRECOES_BASE: tuple[tuple[str, str, str], ...] = (
    ("detenção de erros", "detecção de erros", "o contexto é encontrar erros, não prender erros"),
    ("detencao de erros", "detecção de erros", "normalização sem acento do mesmo erro"),
    ("erros ortográfico", "erros ortográficos", "concordância no plural"),
    ("erros ortograficos", "erros ortográficos", "acento e plural"),
    ("em todas sessões", "em todas as sessões", "artigo necessário"),
    ("reposta média", "resposta média", "troca comum de letras"),
    ("reposta media", "resposta média", "troca comum de letras"),
    ("reposta", "resposta", "troca comum de letras"),
    ("duna si vez", "de uma só vez", "frase natural corrigida"),
    ("duma si vez", "de uma só vez", "frase natural corrigida"),
    ("duma só vez", "de uma só vez", "forma mais clara"),
    ("maus perguntas", "mais perguntas", "contexto indica quantidade adicional"),
    ("aprimure", "aprimore", "verbo correto"),
    ("detetar", "detectar", "variante preservada no padrão do projeto"),
    ("orçamento", "orçamento", "manter grafia canônica"),
)

# Memória local opcional. Se o projeto estiver em modo de escrita, pares novos
# podem ser acrescentados manualmente por ferramenta futura sem internet.
CAMINHO_MEMORIA = Path(__file__).resolve().parent / "dados" / "memoria_ortografica.tsv"


def _pares_memoria() -> tuple[tuple[str, str, str], ...]:
    if not CAMINHO_MEMORIA.exists():
        return ()
    pares: list[tuple[str, str, str]] = []
    for linha in CAMINHO_MEMORIA.read_text(encoding="utf-8").splitlines():
        if not linha.strip() or linha.lstrip().startswith("#"):
            continue
        partes = linha.split("\t")
        if len(partes) >= 2:
            motivo = partes[2] if len(partes) >= 3 else "memória local aprovada"
            pares.append((partes[0], partes[1], motivo))
    return tuple(pares)


def pares_aprovados() -> tuple[tuple[str, str, str], ...]:
    return CORRECOES_BASE + _pares_memoria()


def corrigir_ortografia(texto: str) -> ResultadoOrtografico:
    """Corrige apenas erros aprovados, sem tocar em números e símbolos.

    A implementação usa substituição de frases; isso é intencionalmente mais
    seguro que tentar adivinhar palavras desconhecidas. Quando o PSF não tem
    certeza, ele pode registrar sugestão, mas não deve alterar o pedido.
    """
    original = str(texto)
    corrigido = original
    alteracoes: list[AlteracaoOrtografica] = []

    for errado, certo, motivo in pares_aprovados():
        if errado in corrigido:
            corrigido = corrigido.replace(errado, certo)
            alteracoes.append(AlteracaoOrtografica(errado, certo, motivo))
            continue
        # Caso sem acentos: permite reconhecer a entrada normalizada quando a
        # forma original inteira coincide com o erro conhecido. Não tenta
        # reconstruir frases longas por aproximação para evitar falso positivo.
        if sem_acentos(corrigido).casefold() == sem_acentos(errado).casefold():
            corrigido = certo
            alteracoes.append(AlteracaoOrtografica(errado, certo, motivo))

    return ResultadoOrtografico(original=original, corrigido=corrigido, alteracoes=tuple(alteracoes))


def preparar_entrada_para_interpretacao(texto: str) -> str:
    """Entrada única que os motores devem chamar antes de interpretar."""
    return corrigir_ortografia(texto).corrigido


def aprender_correcao(errado: str, certo: str, motivo: str = "correção ensinada pelo utilizador") -> None:
    """Guarda um novo par de correção local.

    O PSF deve usar isto somente quando o utilizador ensina explicitamente a
    correção. Assim o motor melhora de sessão para sessão sem depender de
    dicionário externo.
    """
    CAMINHO_MEMORIA.parent.mkdir(parents=True, exist_ok=True)
    linha = f"{errado}\t{certo}\t{motivo}\n"
    existentes = CAMINHO_MEMORIA.read_text(encoding="utf-8") if CAMINHO_MEMORIA.exists() else ""
    if linha not in existentes:
        with CAMINHO_MEMORIA.open("a", encoding="utf-8") as f:
            f.write(linha)


def relatorio_correcao(texto: str) -> str:
    resultado = corrigir_ortografia(texto)
    if not resultado.houve_correcao:
        return "Ortografia: nenhuma correção aprovada necessária."
    linhas = ["Ortografia: correções aplicadas antes da interpretação:"]
    contador = 1
    for alt in resultado.alteracoes:
        linhas.append(f"{contador}. {alt.antes} -> {alt.depois} ({alt.motivo})")
        contador = contador + 1
    return "\n".join(linhas)
