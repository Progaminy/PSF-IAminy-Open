"""Resolvedor de exercícios do PSF-IAminy -- "modo cientista".

Para cada pergunta, o motor procura entre o que já sabe (nucleo/, ensino/,
modelos/) um padrão reconhecível, deriva a resposta com os seus próprios
métodos -- nunca com uma fórmula externa nem um LLM -- e explica o
raciocínio em três passos: o que sabe, o que aplicou, a resposta.

Quando nenhum padrão reconhece a pergunta, o motor diz isso com honestidade
e regista a pergunta em `padroes_nao_reconhecidos.json`. Esse ficheiro é o
mecanismo de crescimento: perguntas não resolvidas acumulam ali para se
tornarem padrões novos depois -- "detectar limite -> corrigir -> integrar"
(ver PLANO_PSF_IAMINY.md), nunca uma resposta inventada.

Um padrão também pode ser RECONHECIDO mas ainda assim não ter resposta
segura (ex.: uma hipotenusa cujo resultado não é um quadrado perfeito) --
nesse caso não é "padrão desconhecido" (não vai para o log de descoberta),
é uma lacuna de capacidade já identificada e explicada.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from psf_iaminy.recursos import caminho_dado_mutavel

from lingua_portuguesa.normalizacao import normalizar_texto
from modelos.eficiente import (
    divisores_int,
    porcentagem_de_int,
    potencia_racional_int,
    raiz_quadrada_exata_int,
    regra_de_tres_direta_int,
    simplificar_fracao_int,
)
from nucleo.ordenacao_finita import ordenar_crescente, ordenar_decrescente
from nucleo.sequencias_calculo_psf import adicionar, multiplicar, potencia, subtrair_controlado

CAMINHO_NAO_RECONHECIDOS = caminho_dado_mutavel("ensino", "padroes_nao_reconhecidos.json")


@dataclass(frozen=True, slots=True)
class Resolucao:
    pergunta: str
    resolvida: bool
    padrao: "str | None"
    resposta: "str | None"
    raciocinio: str


def _extrair_inteiros(texto: str) -> list[int]:
    return [int(pedaco) for pedaco in re.findall(r"-?\d+", texto)]


def _numero_sem_espacos(bruto: str) -> int:
    return int(re.sub(r"\s+", "", bruto))


def _fracao_ou_inteiro(numerador: int, denominador: int) -> str:
    num, den = simplificar_fracao_int(numerador, denominador)
    return str(num) if den == 1 else f"{num}/{den}"


# --------------------------------------------------------------------------
# Cada função devolve (resolvida, resposta, raciocínio). `resposta` só
# importa quando resolvida=True -- ver `resolver()`.
# --------------------------------------------------------------------------


def _resolver_soma_contextual(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    a, b = int(m.group(1)), int(m.group(2))
    total = adicionar(a, b)
    raciocinio = (
        f"Sei que juntar é reunir dois grupos e contar o total (pacote MAT-006). "
        f"Apliquei a soma que já tenho pronta: adicionar({a}, {b})."
    )
    return True, f"{total}", raciocinio


def _resolver_calculo_direto(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    a, b = _numero_sem_espacos(m.group(1)), _numero_sem_espacos(m.group(3))
    operador = m.group(2)
    if operador == "+":
        resultado, explicacao = adicionar(a, b), "juntar (pacote MAT-006)"
    elif operador == "-":
        resultado, explicacao = subtrair_controlado(a, b), "retirar (pacote MAT-007)"
    else:  # ÷
        resultado = _fracao_ou_inteiro(a, b) if b != 0 else None
        explicacao = "dividir em partes iguais"
        if resultado is None:
            return False, None, "Divisão por zero não tem resultado -- não invento um."
    raciocinio = f"Sei fazer {explicacao}. Apliquei: {a} {operador} {b}."
    return True, f"{resultado}", raciocinio


_NOMES_OPERADOR = {
    "mais": "juntar (pacote MAT-006)",
    "+": "juntar (pacote MAT-006)",
    "menos": "retirar (pacote MAT-007)",
    "-": "retirar (pacote MAT-007)",
    "vezes": "multiplicar (somar grupos iguais repetidamente)",
    "*": "multiplicar (somar grupos iguais repetidamente)",
    "x": "multiplicar (somar grupos iguais repetidamente)",
    "×": "multiplicar (somar grupos iguais repetidamente)",
    "dividido": "dividir em partes iguais",
    "/": "dividir em partes iguais",
    "÷": "dividir em partes iguais",
}
_SOMAR = {"mais", "+"}
_SUBTRAIR = {"menos", "-"}
_MULTIPLICAR = {"vezes", "*", "x", "×"}


def _resolver_conversacional(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    a, operador, b = int(m.group(1)), m.group(2), int(m.group(3))
    if operador in _SOMAR:
        resultado = f"{adicionar(a, b)}"
    elif operador in _SUBTRAIR:
        resultado = f"{subtrair_controlado(a, b)}"
    elif operador in _MULTIPLICAR:
        resultado = f"{multiplicar(a, b)}"
    else:  # dividido, /, ÷
        if b == 0:
            return False, None, "Divisão por zero não tem resultado -- não invento um."
        resultado = _fracao_ou_inteiro(a, b)
    raciocinio = f"Sei fazer {_NOMES_OPERADOR[operador]}. Apliquei: {a} {operador} {b}."
    return True, resultado, raciocinio


def _resolver_multiplicacao_caixas(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    a, b = int(m.group(1)), int(m.group(2))
    total = multiplicar(a, b)
    raciocinio = (
        f"Sei que multiplicar é somar grupos iguais repetidamente. "
        f"Apliquei: multiplicar({a}, {b})."
    )
    return True, f"{total}", raciocinio


def _resolver_area_retangulo(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    a, b = int(m.group(1)), int(m.group(2))
    total = multiplicar(a, b)
    raciocinio = f"Sei que a área de um retângulo é base vezes altura. Apliquei: multiplicar({a}, {b})."
    return True, f"{total} m²", raciocinio


def _resolver_percentagem(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    p, n = int(m.group(1)), int(m.group(2))
    num, den = porcentagem_de_int(p, n)
    raciocinio = (
        f"Sei que p% de n é uma fração exata p*n/100. "
        f"Apliquei: porcentagem_de_int({p}, {n}) = {num}/{den}."
    )
    return True, (str(num) if den == 1 else f"{num}/{den}"), raciocinio


def _resolver_fracao_comparar(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    a, b, c, d = (int(g) for g in m.groups())
    esquerda, direita = a * d, c * b
    if esquerda > direita:
        maior = f"{a}/{b}"
    elif direita > esquerda:
        maior = f"{c}/{d}"
    else:
        maior = "iguais"
    raciocinio = (
        f"Sei comparar frações multiplicando em cruz: {a}/{b} vs {c}/{d} -> "
        f"{a}×{d}={esquerda} vs {c}×{b}={direita}."
    )
    return True, maior, raciocinio


def _resolver_fracao_somar(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    a, b, c, d = (int(g) for g in m.groups())
    num, den = a * d + c * b, b * d
    resposta = _fracao_ou_inteiro(num, den)
    raciocinio = (
        f"Sei somar frações: a/b + c/d = (ad+cb)/(bd). "
        f"Apliquei: ({a}×{d}+{c}×{b})/({b}×{d}) = {num}/{den}."
    )
    return True, resposta, raciocinio


def _resolver_decimal_para_fracao(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    inteiro, decimal = m.group(1), m.group(2)
    casas = len(decimal)
    num, den = int(inteiro) * (10**casas) + int(decimal), 10**casas
    resposta = _fracao_ou_inteiro(num, den)
    raciocinio = (
        f"Sei que um decimal é uma fração com denominador potência de 10. "
        f"Apliquei: {inteiro},{decimal} = {num}/{den}."
    )
    return True, resposta, raciocinio


def _resolver_media(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    numeros = _extrair_inteiros(m.group(1))
    total = 0
    for x in numeros:
        total = adicionar(total, x)
    resposta = _fracao_ou_inteiro(total, len(numeros))
    raciocinio = f"Sei que a média é a soma dividida pela quantidade. Apliquei: soma{numeros}={total}, ÷{len(numeros)}."
    return True, resposta, raciocinio


def _resolver_maior_da_lista(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    numeros = _extrair_inteiros(m.group(1))
    maior = ordenar_crescente(numeros)[-1]
    raciocinio = (
        f"Sei ordenar e comparar quantidades (pacotes MAT-005/MAT-008). "
        f"Apliquei: ordenar {numeros} e tomar o último."
    )
    return True, f"{maior}", raciocinio


def _resolver_razao_receita(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    a, b, c = int(m.group(1)), int(m.group(2)), int(m.group(3))
    num, den = regra_de_tres_direta_int(a, b, c)
    raciocinio = (
        f"Sei que numa razão a:b, se a quantidade do lado a é c, a do lado b é x=b*c/a "
        f"(regra de três simples). Apliquei: regra_de_tres_direta_int({a},{b},{c})."
    )
    return True, (str(num) if den == 1 else f"{num}/{den}"), raciocinio


def _resolver_razao_semelhanca(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    a, b, c = int(m.group(1)), int(m.group(2)), int(m.group(3))
    num, den = regra_de_tres_direta_int(a, b, c)
    raciocinio = (
        f"Sei que figuras semelhantes mantêm a mesma razão entre lados correspondentes. "
        f"Apliquei: regra_de_tres_direta_int({a},{b},{c})."
    )
    return True, (str(num) if den == 1 else f"{num}/{den}"), raciocinio


def _resolver_hipotenusa(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    a, b = int(m.group(1)), int(m.group(2))
    soma_quadrados = adicionar(multiplicar(a, a), multiplicar(b, b))
    raiz = raiz_quadrada_exata_int(soma_quadrados)
    if raiz is None:
        return (
            False,
            None,
            f"Sei o teorema de Pitágoras: hipotenusa² = {a}² + {b}² = {soma_quadrados}. "
            f"Mas {soma_quadrados} não é um quadrado perfeito, e ainda não tenho raiz real "
            f"de propósito geral -- não invento um valor aproximado aqui.",
        )
    raciocinio = (
        f"Sei o teorema de Pitágoras e sei reconhecer quadrados perfeitos. "
        f"Apliquei: {a}²+{b}²={soma_quadrados}=  {raiz}²."
    )
    return True, f"{raiz}", raciocinio


def _resolver_fatorar_quadratica(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    b, c = int(m.group(1)), int(m.group(2))
    for r in divisores_int(c):
        s = c // r
        if r + s == b:
            raciocinio = (
                f"Sei procurar dois números cujo produto é {c} e cuja soma é {b}, testando "
                f"os divisores de {c}. Apliquei: {r} e {s} servem ({r}×{s}={c}, {r}+{s}={b})."
            )
            return True, f"(x + {r})(x + {s})", raciocinio
    return (
        False,
        None,
        f"Procurei entre os divisores inteiros positivos de {c} dois que somem {b} e não "
        f"achei -- as raízes podem não ser inteiras, e ainda não factorizo esse caso.",
    )


def _resolver_velocidade_media(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    distancia, tempo = int(m.group(1)), int(m.group(2))
    resposta = _fracao_ou_inteiro(distancia, tempo)
    raciocinio = (
        f"Sei que velocidade média é distância dividida pelo tempo. "
        f"Apliquei: {distancia} ÷ {tempo}."
    )
    return True, f"{resposta} km/h", raciocinio


def _resolver_equacao_linear_simples(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    a, b, c = int(m.group(1)), int(m.group(2)), int(m.group(3))
    resposta = _fracao_ou_inteiro(c - b, a)
    raciocinio = (
        f"Sei isolar x numa equação ax+b=c: x=(c-b)/a. Apliquei: ({c}-{b})/{a}."
    )
    return True, resposta, raciocinio


def _resolver_distancia_pontos(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    x1, y1, x2, y2 = (int(g) for g in m.groups())
    dx, dy = x2 - x1, y2 - y1
    soma_quadrados = adicionar(multiplicar(dx, dx), multiplicar(dy, dy))
    raiz = raiz_quadrada_exata_int(soma_quadrados)
    if raiz is None:
        return (
            False,
            None,
            f"Sei a fórmula da distância: dist² = ({dx})² + ({dy})² = {soma_quadrados}. "
            f"Mas {soma_quadrados} não é um quadrado perfeito, e ainda não tenho raiz real "
            f"de propósito geral -- não invento um valor aproximado aqui.",
        )
    raciocinio = (
        f"Sei a fórmula da distância entre dois pontos e sei reconhecer quadrados perfeitos. "
        f"Apliquei: ({dx})²+({dy})²={soma_quadrados}={raiz}²."
    )
    return True, f"{raiz}", raciocinio


def _resolver_planos_iguais(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    alfa, beta, gamma, delta = (int(g) for g in m.groups())
    numerador, denominador = alfa - gamma, delta - beta
    if denominador == 0:
        return False, None, "Os dois planos crescem igual (mesmo coeficiente de x) -- não há um único x onde se igualam."
    resposta = _fracao_ou_inteiro(numerador, denominador)
    raciocinio = (
        f"Sei reorganizar {alfa}+{beta}x = {gamma}+{delta}x isolando x: "
        f"x=({alfa}-{gamma})/({delta}-{beta})={numerador}/{denominador}."
    )
    return True, resposta, raciocinio


def _resolver_ordenar(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    direcao = m.group(1).lower()
    numeros = _extrair_inteiros(m.group(2))
    resultado = ordenar_crescente(numeros) if direcao == "crescente" else ordenar_decrescente(numeros)
    raciocinio = (
        f"Sei comparar quantidades e organizar uma sequência em ordem "
        f"(pacotes MAT-005/MAT-008). Apliquei a ordenação {direcao} sobre {numeros}."
    )
    return True, ", ".join(str(v) for v in resultado), raciocinio


def _resolver_pa_soma(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    n = int(m.group(1))
    numeros = _extrair_inteiros(m.group(2))
    primeiro, razao = numeros[0], numeros[1] - numeros[0]
    termo = primeiro
    total = 0
    termos = []
    for _ in range(n):
        termos.append(termo)
        total = adicionar(total, termo)
        termo = adicionar(termo, razao)
    raciocinio = (
        f"Sei que uma progressão aritmética soma sempre a mesma razão ao termo anterior, "
        f"e sei somar (pacote MAT-006). Apliquei: primeiro termo {primeiro}, razão {razao}, "
        f"gerei {n} termos ({', '.join(str(t) for t in termos)}) e somei-os um a um."
    )
    return True, f"{total}", raciocinio


def _resolver_log(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    base, k = int(m.group(1)), int(m.group(2))
    x = potencia(base, k)
    raciocinio = (
        f"Sei que log_b(x)=k é outra forma de escrever x=b^k -- não preciso calcular "
        f"logaritmo nenhum, só reorganizar o que já sei sobre potências. "
        f"Apliquei: potencia({base}, {k})."
    )
    return True, f"{x}", raciocinio


def _resolver_crescimento(m: "re.Match[str]") -> tuple[bool, "str | None", str]:
    base = int(m.group(1))
    inteiro, decimais, t = int(m.group(2)), m.group(3), int(m.group(4))
    casas = len(decimais)
    numerador_taxa = inteiro * (10**casas) + int(decimais)
    denominador_taxa = 10**casas
    num_pot, den_pot = potencia_racional_int(numerador_taxa, denominador_taxa, t)
    num_total, den_total = simplificar_fracao_int(base * num_pot, den_pot)
    aproximado = round(num_total / den_total, 3)
    raciocinio = (
        f"Sei que uma taxa decimal é uma fração exata "
        f"({m.group(2)},{decimais} = {numerador_taxa}/{denominador_taxa}), e sei elevar "
        f"frações a um expoente inteiro sem precisar de números reais aproximados. "
        f"Apliquei: {base} × ({numerador_taxa}/{denominador_taxa})^{t} = {num_total}/{den_total}."
    )
    return True, f"{num_total}/{den_total} (aproximadamente {aproximado})", raciocinio


@dataclass(frozen=True, slots=True)
class Padrao:
    nome: str
    regex: "re.Pattern[str]"
    derivar: Callable[["re.Match[str]"], tuple[bool, "str | None", str]]

    def tentar(self, texto: str) -> "tuple[bool, str | None, str] | None":
        m = self.regex.search(texto)
        return self.derivar(m) if m else None


PADROES: tuple[Padrao, ...] = (
    Padrao(
        "conversacional_aritmetica",
        re.compile(
            # aceita tanto por extenso ("18 mais 18") como por símbolo
            # ("18+18", "18 x 18", "calcula 7*8", "resolver 2+2").
            r"(?:quanto\s+(?:e|é|d[áa])|calcula|calcular|resolve|resolver|resultado\s+de)\s+(\d+)\s*(\+|-|x|×|\*|÷|/|mais|menos|vezes|dividido)(?:\s+por)?\s*(\d+)",
            re.IGNORECASE,
        ),
        _resolver_conversacional,
    ),
    Padrao(
        "soma_contextual",
        re.compile(r"conta\s+(\d+)\s+\S+\s+e\s+mais\s+(\d+)\s+\S+.*?quantos", re.IGNORECASE | re.DOTALL),
        _resolver_soma_contextual,
    ),
    Padrao(
        "soma_contextual_ao_todo",
        re.compile(r"há\s+(\d+)\s+\S+.*?e\s+(\d+)\s+\S+.*?ao todo", re.IGNORECASE | re.DOTALL),
        _resolver_soma_contextual,
    ),
    Padrao(
        "crescimento_exponencial_racional",
        re.compile(
            r"p\(t\)\s*=\s*(\d+)\s*\(\s*(\d+),(\d+)\s*\)\s*\^\s*t.*?calcula\s+p\(\s*(\d+)\s*\)",
            re.IGNORECASE | re.DOTALL,
        ),
        _resolver_crescimento,
    ),
    Padrao(
        "logaritmo_como_potencia",
        re.compile(r"log\s*(\d+)\s*\(\s*x\s*\)\s*=\s*(\d+)", re.IGNORECASE),
        _resolver_log,
    ),
    Padrao(
        "progressao_aritmetica_soma",
        re.compile(r"soma\s+dos\s+(\d+)\s+primeiros\s+termos\s+da\s+pa\s+([\d,\s]+)\.\.\.", re.IGNORECASE),
        _resolver_pa_soma,
    ),
    Padrao(
        "fracao_comparar",
        re.compile(r"compara:?\s*(\d+)/(\d+)\s*e\s*(\d+)/(\d+).*?maior", re.IGNORECASE),
        _resolver_fracao_comparar,
    ),
    Padrao(
        "fracao_somar",
        re.compile(r"calcula:?\s*(\d+)/(\d+)\s*\+\s*(\d+)/(\d+)", re.IGNORECASE),
        _resolver_fracao_somar,
    ),
    Padrao(
        "decimal_para_fracao",
        re.compile(r"escreve\s+(\d+),(\d+)\s+como\s+fra", re.IGNORECASE),
        _resolver_decimal_para_fracao,
    ),
    Padrao(
        "percentagem",
        re.compile(r"calcula\s+(\d+)%\s+de\s+(\d+)", re.IGNORECASE),
        _resolver_percentagem,
    ),
    Padrao(
        "media_de_lista",
        re.compile(r"média\s+de\s+(.+?)\s+é\s+quanto", re.IGNORECASE),
        _resolver_media,
    ),
    Padrao(
        "maior_valor_lista",
        re.compile(r"valores\s+(.+?):\s*qual\s+é\s+o\s+maior", re.IGNORECASE),
        _resolver_maior_da_lista,
    ),
    Padrao(
        "razao_receita",
        re.compile(r"razão\s+(\d+):(\d+)\s+de\s+\S+\s+e\s+\S+.*?há\s+(\d+)\s+copos", re.IGNORECASE | re.DOTALL),
        _resolver_razao_receita,
    ),
    Padrao(
        "razao_semelhanca",
        re.compile(r"razão\s+(\d+):(\d+).*?pequeno\s+mede\s+(\d+).*?maior", re.IGNORECASE | re.DOTALL),
        _resolver_razao_semelhanca,
    ),
    Padrao(
        "hipotenusa_pitagoras",
        re.compile(r"catetos\s+(\d+)\s+e\s+(\d+).*?hipotenusa", re.IGNORECASE | re.DOTALL),
        _resolver_hipotenusa,
    ),
    Padrao(
        "fatorar_quadratica",
        re.compile(r"fatora:?\s*x[²2]\s*\+\s*(\d+)x\s*\+\s*(\d+)", re.IGNORECASE),
        _resolver_fatorar_quadratica,
    ),
    Padrao(
        "planos_lineares_iguais",
        re.compile(r"a\s*=\s*(\d+)\s*\+\s*(\d+)x\s+e\s+b\s*=\s*(\d+)\s*\+\s*(\d+)x", re.IGNORECASE),
        _resolver_planos_iguais,
    ),
    Padrao(
        "equacao_linear_simples",
        re.compile(r"resolve\s+(\d+)x\s*\+\s*(\d+)\s*=\s*(\d+)", re.IGNORECASE),
        _resolver_equacao_linear_simples,
    ),
    Padrao(
        "velocidade_media",
        re.compile(r"percorre\s+(\d+)\s*km\s+em\s+(\d+)\s*h.*?velocidade\s+média", re.IGNORECASE | re.DOTALL),
        _resolver_velocidade_media,
    ),
    Padrao(
        "distancia_entre_pontos",
        re.compile(
            r"distância\s+entre\s+a\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)\s+e\s+b\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)",
            re.IGNORECASE,
        ),
        _resolver_distancia_pontos,
    ),
    Padrao(
        "multiplicacao_caixas",
        re.compile(r"(\d+)\s+\S+\s+com\s+(\d+)\s+\S+\s+cada", re.IGNORECASE),
        _resolver_multiplicacao_caixas,
    ),
    Padrao(
        "area_retangulo",
        re.compile(r"mede\s+(\d+)\s*m\s*por\s*(\d+)\s*m", re.IGNORECASE),
        _resolver_area_retangulo,
    ),
    Padrao(
        "calculo_direto",
        re.compile(r"calcula:?\s*([\d\s]+?)\s*([+\-÷])\s*([\d\s]+?)\s*\.", re.IGNORECASE),
        _resolver_calculo_direto,
    ),
    Padrao(
        "ordenar_lista",
        re.compile(r"em\s+ordem\s+(crescente|decrescente)\s*:?\s*([\d,\s]+)", re.IGNORECASE),
        _resolver_ordenar,
    ),
)


def _registrar_nao_reconhecido(pergunta: str, caminho: Path) -> None:
    existentes: list[str] = []
    if caminho.exists():
        existentes = json.loads(caminho.read_text(encoding="utf-8"))
    if pergunta not in existentes:
        existentes.append(pergunta)
        caminho.write_text(json.dumps(existentes, indent=2, ensure_ascii=False), encoding="utf-8")


def resolver(pergunta: str, caminho_nao_reconhecidos: "Path | str | None" = None) -> Resolucao:
    texto = normalizar_texto(pergunta)
    for padrao in PADROES:
        resultado = padrao.tentar(texto)
        if resultado is not None:
            resolvida, resposta, raciocinio = resultado
            return Resolucao(
                pergunta=pergunta,
                resolvida=resolvida,
                padrao=padrao.nome,
                resposta=resposta if resolvida else None,
                raciocinio=raciocinio,
            )
    caminho = Path(caminho_nao_reconhecidos) if caminho_nao_reconhecidos is not None else CAMINHO_NAO_RECONHECIDOS
    _registrar_nao_reconhecido(pergunta, caminho)
    return Resolucao(
        pergunta=pergunta,
        resolvida=False,
        padrao=None,
        resposta=None,
        raciocinio="Ainda não reconheço este padrão de pergunta -- fica registado para virar um padrão novo depois.",
    )
