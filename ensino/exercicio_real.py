"""Exercício real: aplica a construção do conceito numa variação sorteada,
não pergunta sobre o mapa de dependências.

Diretiva do autor (`conversa.md`, resposta ao achado do professor D sobre
"cite uma dependência de X" não ensinar ninguém):

1) Linguagem sempre humana, nunca nome de campo ou termo de código
   ("Qual é o resultado?", nunca "SOMA(4)(7)=?").
2) Cálculo sempre em notação de papel para o aluno -- o motor continua
   calculando por dentro com os primitivos reais de Church
   (`nucleo/aritmetica.py`: SOMA, SUB, MULT, POT, DIV, MOD, MDC, MMC,
   MENOR, MAIOR, IGUAL). O que muda é só a camada de exibição.

Cada gerador abaixo: sorteia operandos pequenos, calcula o resultado real
chamando o primitivo formal (Church, via `de_int`/`para_int`), monta o
enunciado em notação de papel com o resultado oculto, e verifica a
resposta do aluno comparando contra esse mesmo resultado -- 0.0 ou 1.0,
nunca semelhança textual (aqui sempre há uma resposta exata a conferir).

A exibição em coluna (soma/subtração/multiplicação) reaproveita
`nucleo/contas_armadas.py` (Etapa 1037, já provado contra a aritmética
escolar nativa) e depois confere o resultado dela contra o primitivo de
Church -- nunca uma segunda fonte de verdade sem conferência cruzada,
mesma disciplina já usada no resto do projeto (progressões, radicais,
contas armadas).
"""
from __future__ import annotations

import random
import re
from dataclasses import dataclass
from typing import Callable

from nucleo.aritmetica import SOMA, SUB, MULT, POT, DIV, MOD, MDC, MMC, MENOR, MAIOR, IGUAL
from nucleo.traducao import de_int, para_int, para_bool
from nucleo.contas_armadas import (
    soma_armada,
    subtracao_armada,
    multiplicacao_armada,
)


@dataclass(frozen=True, slots=True)
class ExercicioReal:
    conceito: str
    tipo: str  # "numero" | "quociente_resto" | "comparador" | "sim_nao" | "par_impar"
    enunciado: str
    resposta_certa: str


@dataclass(frozen=True, slots=True)
class ResultadoExercicioReal:
    correto: bool
    resposta_certa: str
    resposta_aluno: str


def _sorteio_pequeno(rng: random.Random, minimo: int, maximo: int) -> int:
    return rng.randint(minimo, maximo)


def _texto_coluna_oculta(a: int, b: int, operador: str) -> str:
    """Mesma moldura de `RegistroSomaArmada.texto()`, mas com o resultado
    oculto por "?" -- o aluno precisa calcular, não ler a resposta pronta."""
    largura = max(len(str(a)), len(str(b)) + 2, 3) + 2
    return "\n".join((
        f"  {a}".rjust(largura),
        f"{operador} {b}".rjust(largura),
        "-" * largura,
        "  ?".rjust(largura),
    ))


# ---------------------------------------------------------------------------
# Adição, subtração, multiplicação -- notação de coluna (conta armada)
# ---------------------------------------------------------------------------

def _exercicio_adicao(rng: random.Random) -> ExercicioReal:
    a = _sorteio_pequeno(rng, 10, 89)
    b = _sorteio_pequeno(rng, 1, 89)
    registro = soma_armada(a, b)
    esperado = para_int(SOMA(de_int(a))(de_int(b)))
    if registro.resultado != esperado:
        raise ValueError("conta armada de adição divergiu do primitivo formal (Church)")
    enunciado = "Resolva esta conta armada. Qual é o resultado?\n\n" + _texto_coluna_oculta(a, b, "+")
    return ExercicioReal("adicao", "numero", enunciado, str(esperado))


def _exercicio_subtracao(rng: random.Random) -> ExercicioReal:
    a = _sorteio_pequeno(rng, 20, 99)
    b = _sorteio_pequeno(rng, 1, a)
    registro = subtracao_armada(a, b)
    esperado = para_int(SUB(de_int(a))(de_int(b)))
    if registro.resultado != esperado:
        raise ValueError("conta armada de subtração divergiu do primitivo formal (Church)")
    enunciado = "Resolva esta conta armada. Qual é o resultado?\n\n" + _texto_coluna_oculta(a, b, "-")
    return ExercicioReal("subtracao natural", "numero", enunciado, str(esperado))


def _exercicio_multiplicacao(rng: random.Random) -> ExercicioReal:
    a = _sorteio_pequeno(rng, 2, 19)
    b = _sorteio_pequeno(rng, 2, 12)
    registro = multiplicacao_armada(a, b)
    esperado = para_int(MULT(de_int(a))(de_int(b)))
    if registro.resultado != esperado:
        raise ValueError("conta armada de multiplicação divergiu do primitivo formal (Church)")
    enunciado = "Resolva esta conta armada. Qual é o resultado?\n\n" + _texto_coluna_oculta(a, b, "x")
    return ExercicioReal("multiplicacao", "numero", enunciado, str(esperado))


# ---------------------------------------------------------------------------
# Divisão -- quociente e resto
# ---------------------------------------------------------------------------

def _exercicio_divisao(rng: random.Random) -> ExercicioReal:
    divisor = _sorteio_pequeno(rng, 2, 12)
    quociente_real = _sorteio_pequeno(rng, 2, 15)
    resto_real = _sorteio_pequeno(rng, 0, divisor - 1)
    # dividendo construído pelos próprios primitivos de Church: divisor*quociente + resto
    produto = MULT(de_int(divisor))(de_int(quociente_real))
    dividendo_church = SOMA(produto)(de_int(resto_real))
    dividendo = para_int(dividendo_church)
    quociente_calc = para_int(DIV(dividendo_church)(de_int(divisor)))
    resto_calc = para_int(MOD(dividendo_church)(de_int(divisor)))
    if quociente_calc != quociente_real or resto_calc != resto_real:
        raise ValueError("DIV/MOD reais divergiram do dividendo montado por construção")
    enunciado = (
        f"Calcule {dividendo} ÷ {divisor}. "
        "Quanto dá o quociente, e quanto sobra de resto? "
        "(responda como \"quociente resto R\", ex.: \"5 resto 2\")"
    )
    resposta_certa = f"{quociente_calc} resto {resto_calc}"
    return ExercicioReal("resto e divisao euclidiana", "quociente_resto", enunciado, resposta_certa)


# ---------------------------------------------------------------------------
# Potenciação -- expansão por multiplicação repetida
# ---------------------------------------------------------------------------

def _exercicio_potenciacao(rng: random.Random) -> ExercicioReal:
    base = _sorteio_pequeno(rng, 2, 9)
    expoente = _sorteio_pequeno(rng, 2, 4)
    esperado = para_int(POT(de_int(base))(de_int(expoente)))
    fatores = " x ".join([str(base)] * expoente)
    enunciado = (
        f"Calcule {base}^{expoente} ({base} multiplicado por ele mesmo "
        f"{expoente} vezes: {fatores}). Qual é o resultado?"
    )
    return ExercicioReal("potenciacao por repeticao", "numero", enunciado, str(esperado))


# ---------------------------------------------------------------------------
# MDC / MMC -- passos de Euclides computados pelos primitivos reais
# ---------------------------------------------------------------------------

def _passos_euclides(a: int, b: int) -> tuple[tuple[int, int, int, int], ...]:
    """(dividendo, divisor, quociente, resto) a cada passo -- cada quociente e
    resto vem de DIV/MOD reais (Church), só traduzidos pra exibição."""
    passos: list[tuple[int, int, int, int]] = []
    x, y = a, b
    while y != 0:
        q = para_int(DIV(de_int(x))(de_int(y)))
        r = para_int(MOD(de_int(x))(de_int(y)))
        passos.append((x, y, q, r))
        x, y = y, r
    return tuple(passos)


def _exercicio_mdc(rng: random.Random) -> ExercicioReal:
    a = _sorteio_pequeno(rng, 4, 60)
    b = _sorteio_pequeno(rng, 4, 60)
    passos = _passos_euclides(a, b)
    mdc_calculado = passos[-1][1] if passos else a
    esperado = para_int(MDC(de_int(a))(de_int(b)))
    if mdc_calculado != esperado:
        raise ValueError("passos de Euclides divergiram do MDC real (Church)")
    linhas = [f"{x} = {q} x {y} + {r}" for x, y, q, r in passos]
    enunciado = (
        f"Qual é o máximo divisor comum (MDC) entre {a} e {b}? "
        "Dica -- divisões sucessivas de Euclides:\n" + "\n".join(linhas)
    )
    return ExercicioReal("mdc mmc por fatores", "numero", enunciado, str(esperado))


def _exercicio_mmc(rng: random.Random) -> ExercicioReal:
    a = _sorteio_pequeno(rng, 2, 20)
    b = _sorteio_pequeno(rng, 2, 20)
    mdc_real = para_int(MDC(de_int(a))(de_int(b)))
    produto = para_int(MULT(de_int(a))(de_int(b)))
    esperado = para_int(MMC(de_int(a))(de_int(b)))
    reconstrucao = para_int(MULT(de_int(esperado))(de_int(mdc_real)))
    if reconstrucao != produto:
        raise ValueError("MMC real (Church) não reconstrói o produto original via MDC")
    enunciado = (
        f"Qual é o mínimo múltiplo comum (MMC) entre {a} e {b}? "
        f"Dica: mmc({a},{b}) = ({a} x {b}) ÷ mdc({a},{b}) = {produto} ÷ {mdc_real}."
    )
    return ExercicioReal("mdc mmc por fatores", "numero", enunciado, str(esperado))


# ---------------------------------------------------------------------------
# Comparação, divisibilidade, paridade
# ---------------------------------------------------------------------------

def _exercicio_comparacao(rng: random.Random) -> ExercicioReal:
    a = _sorteio_pequeno(rng, 1, 99)
    b = _sorteio_pequeno(rng, 1, 99)
    if para_bool(MENOR(de_int(a))(de_int(b))):
        certo = "<"
    elif para_bool(MAIOR(de_int(a))(de_int(b))):
        certo = ">"
    else:
        if not para_bool(IGUAL(de_int(a))(de_int(b))):
            raise ValueError("MENOR/MAIOR/IGUAL reais não cobrem o par sorteado")
        certo = "="
    enunciado = f"Qual sinal fica entre {a} e {b}: <, > ou =?"
    return ExercicioReal("ordem total", "comparador", enunciado, certo)


def _exercicio_divisibilidade(rng: random.Random) -> ExercicioReal:
    divisor = _sorteio_pequeno(rng, 2, 12)
    n = _sorteio_pequeno(rng, 2, 100)
    divisivel = para_int(MOD(de_int(n))(de_int(divisor))) == 0
    enunciado = f"{n} é divisível por {divisor}? Responda sim ou não."
    return ExercicioReal("divisibilidade pura", "sim_nao", enunciado, "sim" if divisivel else "não")


def _exercicio_paridade(rng: random.Random) -> ExercicioReal:
    n = _sorteio_pequeno(rng, 1, 200)
    par = para_int(MOD(de_int(n))(de_int(2))) == 0
    enunciado = f"{n} é par ou ímpar?"
    return ExercicioReal("paridade", "par_impar", enunciado, "par" if par else "ímpar")


GERADORES_POR_CONCEITO: dict[str, Callable[[random.Random], ExercicioReal]] = {
    "adicao": _exercicio_adicao,
    "subtracao natural": _exercicio_subtracao,
    "multiplicacao": _exercicio_multiplicacao,
    "resto e divisao euclidiana": _exercicio_divisao,
    "potenciacao por repeticao": _exercicio_potenciacao,
    "ordem total": _exercicio_comparacao,
    "divisibilidade pura": _exercicio_divisibilidade,
    "paridade": _exercicio_paridade,
}

# "mdc mmc por fatores" tem dois geradores possíveis (MDC ou MMC) -- entra à
# parte porque não é 1 conceito = 1 gerador, é 1 conceito = 2 perguntas.
_GERADORES_MDC_MMC = (_exercicio_mdc, _exercicio_mmc)


def tem_gerador_real(conceito: str) -> bool:
    return conceito in GERADORES_POR_CONCEITO or conceito == "mdc mmc por fatores"


def gerar_exercicio_real(conceito: str, semente: "int | None" = None) -> ExercicioReal:
    """Sorteia uma variação nova do conceito e devolve o exercício real
    (enunciado em notação de papel/linguagem humana, resposta certa vinda do
    primitivo formal). Levanta KeyError se o conceito não tiver gerador --
    honesto: nunca inventa exercício de conta para conceito sem função real."""
    rng = random.Random(semente)
    if conceito == "mdc mmc por fatores":
        gerador = rng.choice(_GERADORES_MDC_MMC)
        return gerador(rng)
    gerador = GERADORES_POR_CONCEITO[conceito]
    return gerador(rng)


_PADRAO_INTEIROS = re.compile(r"-?\d+")


def verificar_resposta_real(exercicio: ExercicioReal, resposta_aluno: str) -> ResultadoExercicioReal:
    """Verificação exata (0.0/1.0) contra a resposta certa -- aqui sempre há
    um valor exato a conferir (nunca semelhança textual)."""
    bruta = resposta_aluno.strip()
    resposta = bruta.casefold()
    if exercicio.tipo == "numero":
        numeros = _PADRAO_INTEIROS.findall(bruta)
        correto = len(numeros) == 1 and numeros[0] == exercicio.resposta_certa
    elif exercicio.tipo == "quociente_resto":
        numeros = _PADRAO_INTEIROS.findall(bruta)
        esperado_q, esperado_r = exercicio.resposta_certa.split(" resto ")
        correto = len(numeros) >= 2 and numeros[0] == esperado_q and numeros[1] == esperado_r
    elif exercicio.tipo == "comparador":
        mapa = {"<": "<", "menor": "<", ">": ">", "maior": ">", "=": "=", "igual": "="}
        correto = mapa.get(resposta) == exercicio.resposta_certa
    elif exercicio.tipo == "sim_nao":
        afirmativas = {"sim", "s", "verdadeiro", "certo"}
        negativas = {"nao", "não", "n", "falso", "errado"}
        esperado_sim = exercicio.resposta_certa == "sim"
        correto = (resposta in afirmativas) if esperado_sim else (resposta in negativas)
    elif exercicio.tipo == "par_impar":
        pares = {"par"}
        impares = {"impar", "ímpar"}
        esperado_par = exercicio.resposta_certa == "par"
        correto = (resposta in pares) if esperado_par else (resposta in impares)
    else:
        raise ValueError(f"tipo de exercício real desconhecido: {exercicio.tipo}")
    return ResultadoExercicioReal(correto, exercicio.resposta_certa, bruta)
