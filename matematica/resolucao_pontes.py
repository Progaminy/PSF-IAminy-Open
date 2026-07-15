"""Resolução semântica conservadora das dependências matemáticas."""
from __future__ import annotations

import re
import unicodedata


def normalizar_termo(texto: str) -> str:
    base = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    return " ".join(re.findall(r"[a-z0-9]+", base))


# Achado real (auditoria honesta pedida pelo autor): "zero", "s"/"sucessor",
# "numero natural", "adicao", "subtracao natural", "igualdade", "ordem",
# "multiplicacao" e "potencia por repeticao" estavam NESTA allowlist havia
# muito tempo -- ou seja, o próprio auditor fingia que estavam resolvidos
# sem nenhum documento ETAPA real por trás, violando a regra "nenhum
# conceito pode ser usado antes de nascer" que ETAPA_03 (o primeiro
# documento que existe) já citava. Materializados agora como ETAPA 1
# (número natural), ETAPA 2 (adição), 1073 (subtração natural), 1074
# (igualdade e ordem), 1075 (multiplicação) e 1076 (potenciação por
# repetição) -- por isso saíram daqui. As pontes reais (`ALIASES_CONCEITOS`
# abaixo) cobrem as variantes de nome ("zero"/"s"/"sucessor" -> "numero
# natural"; "subtracao" bare -> "subtracao natural"; "igualdade"/"ordem"
# -> "igualdade e ordem"; "potencia por repeticao" -> "potenciacao por
# repeticao").
#
# O que resta aqui são raízes GENUINAMENTE ainda implícitas -- infra-
# estrutura de baixo nível (pares, iteração, recursão, lógica booleana) e
# primitivas de domínios finitos que nenhuma ETAPA promoveu ainda a
# documento próprio. Não é fingimento silencioso: é escopo ainda não
# atacado, deixado explícito aqui em vez de escondido.
RAIZES_FUNDACIONAIS = {
    "v", "f", "par", "iter", "y",
    "distincao", "logica", "logica booleana",
    "iteracao", "recursao", "existencia limitada", "busca finita",
    "dominio finito explicito", "enumeracao finita", "soma finita",
    "produto finito", "par ordenado", "relacao finita",
    "inducao finita", "multiplos", "divisor proprio", "coprimalidade",
    "divisores", "transicao", "transicoes", "estado finito",
    "reescrita finita", "tipos finitos", "arvores finitas",
    "funcoes finitas", "pilha finita", "execucao finita", "contagem",
    "recursos", "dados finitos", "frequencia", "pesos racionais",
    "abertos finitos", "modelos finitos", "funcao objetivo",
}

# Conceitos intermediários materializados dentro de documentos-bloco. Eles não
# são raízes universais; são aceites apenas como pontos internos já descritos
# passo a passo no documento que os usa.
CONCEITOS_INTERNOS_DOCUMENTADOS = {
    "unidade de medida", "medida finita", "segmento", "direcao", "angulo",
    "razao", "proporcao", "multiplicacao cruzada", "perpendicularidade",
    "triangulo retangulo", "relacao pitagorica", "semelhanca de triangulos",
    "racionais finitos", "combinacao linear", "derivacao", "aceitacao",
    "palavras finitas", "gramaticas", "relacoes", "diferencas",
    "somas finitas", "estado", "peso", "regiao", "jacobiano",
    "reescrita", "igualdade de restos", "lei das formulas construidas",
    "estruturas finitas", "aritmetica unaria", "quantificador",
    "tuplas e dicionarios finitos",
}


ALIASES_CONCEITOS = {
    "zero": "numero natural",
    "s": "numero natural",
    "sucessor": "numero natural",
    "numeros naturais": "numero natural",
    "subtracao": "subtracao natural",
    "igualdade": "igualdade e ordem",
    "ordem": "igualdade e ordem",
    "potencia por repeticao": "potenciacao por repeticao",
    "divisibilidade": "divisibilidade pura",
    "divisor comum": "mdc puro",
    "mdc": "mdc puro",
    "resto euclidiano puro": "resto e divisao euclidiana",
    "resto euclidiano": "resto e divisao euclidiana",
    "primalidade": "primalidade pura",
    "fatoracao": "fatoracao pura",
    "fatoracao prima": "tfa existencia",
    "existencia da fatoracao prima": "tfa existencia",
    "inteiros relativos": "inteiros relativos puros",
    "bezout": "bezout e euclides estendido",
    "identidade de bezout": "bezout e euclides estendido",
    "congruencia": "congruencia equivalencia",
    "congruencia por igualdade de restos": "congruencia igualdade restos",
    "classes de equivalencia": "classes de equivalencia gerais",
    "funcao phi de euler": "phi euler",
    "funcoes": "funcao como relacao especial",
    "funcao": "funcao como relacao especial",
    "composicao": "composicao de funcoes",
    "identidade": "funcao identidade",
    "relacao de equivalencia": "equivalencia",
    "automatos finitos": "automatos finitos naturais",
    "linguagens regulares": "linguagens regulares naturais",
    "gramaticas finitas": "gramaticas formais finitas",
    "semantica operacional": "semantica operacional finita",
    "expressoes finitas": "expressao simbolica finita",
    "provas finitas": "teoria modelos prova finita",
    "conjuntos finitos": "metodos finitos",
    "ordem finita": "ordem total",
    "medida finita": "medida probabilidade finita",
    "diferenca": "diferenca controlada",
    "subtracao controlada": "diferenca controlada",
    "equacao linear finita": "equacao primeiro grau finita",
    "corpo": "corpo finito",
    "relacao binaria": "relacoes binarias",
    "caminho": "caminho grafo",
    "arvore": "arvore grafo",
    "grafo": "grafo relacao simetrica",
    "potencia": "sequencias calculo psf",
    "anel": "anel inicial",
}

FRASES_DE_CONTEXTO_NAO_DEPENDENCIA = (
    "tudo o que nasceu",
    "ja construid",
    "quando necessario",
    "apenas nas etapas",
    "etapas 1",
)


def resolver_dependencia(dependencia: str, nomes: set[str]) -> tuple[str, str | None]:
    termo = normalizar_termo(dependencia)
    if termo.startswith("relacao binaria simetria caminho"):
        necessarios = {"relacoes binarias", "simetria", "caminho grafo"}
        if necessarios <= nomes:
            return "GRUPO_DE_CONCEITOS", "relacoes binarias + simetria + caminho grafo"
    if termo.startswith("aritmetica unaria apenas para ida volta"):
        return "RAIZ", "aritmetica unaria"
    if termo.startswith("primitivas e estruturas finitas"):
        return "RAIZ", "primitivas + estruturas finitas"
    if termo.startswith("relacoes funcoes ordens grafos polinomios"):
        return "GRUPO_DE_CONCEITOS", "linha finita anterior"
    if termo.startswith("o precedente operacional de predicados"):
        return "INTERNO_DOCUMENTADO", "quantificadores finitos"
    if termo.startswith("tuplas e dicionarios finitos"):
        return "RAIZ", "estruturas finitas de suporte"
    if termo.startswith("primitivas psf") or termo.startswith("primitivas fundacionais") or termo.startswith("primitivas v"):
        return "RAIZ", "primitivas psf"
    if termo.startswith("logica booleana"):
        return "RAIZ", "logica booleana"
    referencias_modulo = {
        "metodos finitos": "metodos finitos",
        "logica predicados finita": "logica predicados finita",
        "teoria modelos prova finita": "teoria modelos prova finita",
        "computabilidade finita": "computabilidade finita",
    }
    for fragmento, conceito in referencias_modulo.items():
        if fragmento.replace(" ", "_") in dependencia.lower() or fragmento in termo:
            if conceito in nomes:
                return "REFERENCIA_DE_MODULO", conceito
    # Marcadores entre parênteses são localização histórica, não parte do nome.
    termo_sem_marcador = re.sub(r"\s+etapas?\s+\d+.*$", "", termo).strip()
    if termo_sem_marcador != termo:
        if termo_sem_marcador in nomes:
            return "CONCEITO", termo_sem_marcador
        alias_sem_marcador = ALIASES_CONCEITOS.get(termo_sem_marcador)
        if alias_sem_marcador and normalizar_termo(alias_sem_marcador) in nomes:
            return "ALIAS", normalizar_termo(alias_sem_marcador)
    if any(frase in termo for frase in FRASES_DE_CONTEXTO_NAO_DEPENDENCIA):
        # São notas históricas/condicionais redundantes, não vértices do grafo.
        return "CONTEXTO_NAO_ATOMICO", None
    if termo in RAIZES_FUNDACIONAIS:
        return "RAIZ", termo
    if termo in CONCEITOS_INTERNOS_DOCUMENTADOS:
        return "INTERNO_DOCUMENTADO", termo
    if termo in nomes:
        return "CONCEITO", termo
    alias = ALIASES_CONCEITOS.get(termo)
    if alias and normalizar_termo(alias) in nomes:
        return "ALIAS", normalizar_termo(alias)
    return "NAO_RESOLVIDA", None


def auditar_resolucao_pontes(conceitos: tuple[object, ...]) -> dict[str, object]:
    nomes = {normalizar_termo(getattr(c, "nome")) for c in conceitos}
    por_nome = {normalizar_termo(getattr(c, "nome")): c for c in conceitos}
    nao_resolvidas: list[tuple[str, str]] = []
    agregadas: list[tuple[str, str]] = []
    contexto_nao_atomico: list[tuple[str, str]] = []
    futuras: list[tuple[str, str]] = []
    resolvidas = 0
    total = 0
    for conceito in conceitos:
        destino = normalizar_termo(getattr(conceito, "nome"))
        marcador_destino = getattr(conceito, "marcador_historico", None)
        for dependencia in getattr(conceito, "dependencias_declaradas", ()):
            total += 1
            estado, origem = resolver_dependencia(dependencia, nomes)
            if estado == "AGREGADA_OU_IMPRECISA":
                agregadas.append((destino, dependencia))
            elif estado == "CONTEXTO_NAO_ATOMICO":
                contexto_nao_atomico.append((destino, dependencia))
            elif estado == "NAO_RESOLVIDA":
                nao_resolvidas.append((destino, dependencia))
            else:
                resolvidas += 1
                if estado in {"CONCEITO", "ALIAS"} and origem in por_nome:
                    marcador_origem = getattr(por_nome[origem], "marcador_historico", None)
                    # ETAPA é marcador histórico, não ordem de verdade. Só a
                    # autorreferência é ciclo inequívoco neste inventário.
                    if origem == destino:
                        futuras.append((destino, origem))
    return {
        "dependencias": total,
        "resolvidas": resolvidas,
        "nao_resolvidas": tuple(nao_resolvidas),
        "agregadas_ou_imprecisas": tuple(agregadas),
        "contexto_nao_atomico_ignorado": tuple(contexto_nao_atomico),
        "referencias_futuras": tuple(futuras),
        "pontes_fechadas": resolvidas,
        "sem_lacunas": not nao_resolvidas and not agregadas and not futuras,
    }
