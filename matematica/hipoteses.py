"""Hipóteses matemáticas ainda não provadas.

Uma hipótese preservada aqui não entra automaticamente como conhecimento puro,
algoritmo confiável ou resultado. Ela permanece disponível para formalização,
prova, comparação e falsificação.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HipoteseMatematica:
    identificador: str
    titulo: str
    autor: str
    estado: str
    intuicao: tuple[str, ...]
    exemplos_originais: tuple[str, ...]
    ambiguidades: tuple[str, ...]
    plano_de_estudo: tuple[str, ...]
    criterio_de_falsificacao: tuple[str, ...]
    arquivo: str


HIPOTESE_DIVISAO_REVELA_PRIMALIDADE = HipoteseMatematica(
    identificador="divisao_revela_primalidade_psf",
    titulo="Divisão por níveis como possível reveladora de divisibilidade e primalidade",
    autor="Pensador Sem Fronteiras",
    estado="IDEIA_GUARDADA_ATÉ_O_MOTOR_ESTAR_MADURO",
    intuicao=(
        "Começar obrigatoriamente pela divisão por 2.",
        "Representar quociente e resto por distribuições repetidas em níveis.",
        "Manter o mesmo nível ao transportar restos e casas decimais.",
        "Observar padrões que possam indicar por quais números o dividendo se revela divisível.",
        "Usar a raiz quadrada do número como limite provisório da procura de divisores.",
        "Para números grandes, usar os padrões como polos de aproximação antes da verificação completa.",
    ),
    exemplos_originais=(
        "12 é caso de teste de primalidade: a técnica encontra divisor próprio e conclui que 12 não é primo.",
        "9 é caso de teste de primalidade: a técnica encontra o divisor próprio 3 e conclui que 9 não é primo.",
        "7 é caso de teste de primalidade: a técnica não encontra divisor próprio no percurso necessário e conclui que 7 é primo.",
        "As anotações de repartição, níveis, restos e transporte decimal pertencem à mesma técnica guardada.",
    ),
    ambiguidades=(
        "Formalizar exatamente o significado de 'manter o nível'.",
        "Formalizar quando e por que aparece a transformação '-1'.",
        "Formalizar o significado de 'já temos 2', 'já temos 3' ou 'já temos 5'.",
        "Definir qual padrão final classifica um número como primo, composto ou apenas candidato.",
        "Definir como o limite da raiz quadrada entra na sequência sem usar a regra pronta como fundamento.",
    ),
    plano_de_estudo=(
        "Esperar o motor atingir maturidade antes de iniciar investigação, formalização ou execução da hipótese.",
        "Transcrever então a técnica completa, inclusive o PDF futuro, sem alterar silenciosamente a intenção do autor.",
        "Definir estado, entrada, transformação, saída e condição de paragem de cada movimento.",
        "Executar manualmente os casos 2 a 30 e preservar todas as sequências.",
        "Comparar depois com a primalidade PSF já construída, apenas como validador.",
        "Procurar o primeiro contraexemplo e estudar por que o padrão falhou.",
        "Verificar se a técnica é um algoritmo de divisão, um detector de fatores, um crivo, uma representação binária ou uma combinação dessas ideias.",
        "Medir custo e investigar se os polos realmente reduzem a procura em números grandes.",
    ),
    criterio_de_falsificacao=(
        "Se dois números com classificações diferentes produzirem o mesmo certificado final, o certificado é insuficiente.",
        "Se um composto for certificado como primo ou um primo como composto sob regras formalizadas, a versão testada é falsificada.",
        "Se a técnica depender de conhecer previamente o divisor ou a primalidade, ela não funciona como descoberta independente.",
        "Se ultrapassar a raiz sem justificativa e ainda exigir todos os divisores, não oferece a redução proposta.",
    ),
    arquivo="conhecimento/HIPOTESE_DIVISAO_PRIMALIDADE_PSF.md",
)


def hipoteses_pendentes() -> tuple[HipoteseMatematica, ...]:
    return (HIPOTESE_DIVISAO_REVELA_PRIMALIDADE,)


def obter_hipotese(identificador: str) -> HipoteseMatematica | None:
    chave = identificador.strip().lower()
    for hipotese in hipoteses_pendentes():
        if chave in {hipotese.identificador.lower(), hipotese.titulo.lower()}:
            return hipotese
    return None
