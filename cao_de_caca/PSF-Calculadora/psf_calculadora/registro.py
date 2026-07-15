"""Registro de motores com seleção por intenção e prioridade."""

from collections import defaultdict
from dataclasses import dataclass
import re
from types import CodeType
import unicodedata

from .dependencias import DependenciaAusenteError, modulos_ausentes


def _normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    substituicoes = {"−": "-", "–": "-", "—": "-", "×": "*", "÷": "/"}
    for antigo, novo in substituicoes.items():
        texto = texto.replace(antigo, novo)
    return re.sub(r"[?!;]+", " ", texto)


ALIASES = {
    "adicao_subtracao": (
        "+", "-", "somar", "soma", "subtrair", "adicao subtracao",
    ),
    "divisao": ("/", ":", "dividir", "dividido", "divisao", "quociente"),
    "multiplos": ("multiplo", "multiplos"),
    "porcentagem": ("porcentagem", "percentagem", "%"),
    "equacoes": ("equacao", "equacoes"),
    "equacao_segundo_grau": ("equacao quadratica", "segundo grau",),
    "series_fourier": ("fourier", "serie de fourier"),
    "series_fourier_psf": ("fourier", "serie de fourier"),
    "derivadas": ("derivada", "derivadas", "derivar"),
    "integral_definida": ("integral definida", "integrar"),
    "matrizes": ("matriz", "matrizes"),
    "probabilidade": ("probabilidade",),
    "mmc": ("mmc", "minimo multiplo comum"),
    "mdc": ("mdc", "maximo divisor comum"),
    "svm": ("svm", "maquina de vetores de suporte"),
    "pa": ("pa", "progressao aritmetica"),
    "pg": ("pg", "progressao geometrica"),
    # Estes três nomes de atributo (otimizacao_inteira, algoritmos_geneticos,
    # teoria_filas) não compartilham nenhuma palavra com a frase de comando
    # que o próprio motor espera (regex interno) -- sem alias explícito, o
    # índice invertido derivava termos do NOME DO ATRIBUTO Python, nunca
    # alcançado pelo terminal. Confirmado com os três comandos reais.
    "otimizacao_inteira": ("branch and bound", "branch bound"),
    "algoritmos_geneticos": ("algoritmo genetico", "algoritmos geneticos"),
    "teoria_filas": ("fila", "filas", "teoria das filas", "teoria de filas"),
}

# Todo motor recebe uma declaração, ainda que vazia. As exceções abaixo
# documentam os recursos científicos que não pertencem à biblioteca padrão.
REQUISITOS_POR_MOTOR = {
    "series_fourier": ("sympy", "numpy", "matplotlib"),
    "series_fourier_psf": ("sympy", "numpy"),
    "derivadas": ("sympy",),
    "limites": ("sympy",),
    "integral_definida": ("sympy",),
    "integral_indefinida": ("sympy",),
    "matrizes": ("numpy",),
    "determinantes": ("numpy",),
    "sistemas_lineares": ("numpy",),
    "pca_avancado": ("numpy", "sklearn"),
    "agrupamentos": ("numpy", "sklearn"),
    "analise_discriminante": ("numpy", "sklearn"),
    "regressao_logistica": ("numpy", "sklearn"),
    "svm": ("numpy", "sklearn"),
    "arvores_florestas": ("numpy", "sklearn"),
    "redes_neurais": ("numpy", "sklearn"),
    "inferencia_bayesiana_mcmc": ("numpy", "scipy"),
    "otimizacao_linear": ("numpy", "scipy"),
    "otimizacao_nao_linear": ("numpy", "scipy"),
    "processamento_sinais": ("numpy", "scipy"),
    "transformada_fourier_r": ("numpy",),
    "transformada_fourier_rn": ("numpy",),
    "wavelets": ("numpy", "scipy"),
    "grafos": ("networkx", "matplotlib"),
}

SIMBOLOS_DEPENDENCIA = {
    "np": "numpy", "sp": "sympy", "pd": "pandas", "plt": "matplotlib",
    "matplotlib": "matplotlib", "nx": "networkx", "mp": "mpmath",
    "SklearnPCA": "sklearn", "SklearnKMeans": "sklearn",
    "AgglomerativeClustering": "sklearn",
    "LinearDiscriminantAnalysis": "sklearn", "LogisticRegression": "sklearn",
    "SVC": "sklearn", "DecisionTreeClassifier": "sklearn",
    "RandomForestClassifier": "sklearn", "MLPClassifier": "sklearn",
    "StandardScaler": "sklearn",
}

MOTORES_FALLBACK = {
    "adicao_subtracao", "divisao", "expressoes", "equacoes",
}


def _dependencias_detectadas(motor):
    """Extrai requisitos diretos dos métodos, sem importar os pacotes."""
    simbolos = set()

    def visitar_codigo(codigo):
        simbolos.update(codigo.co_names)
        for constante in codigo.co_consts:
            if isinstance(constante, CodeType):
                visitar_codigo(constante)

    for valor in vars(type(motor)).values():
        valor = getattr(valor, "__func__", valor)
        codigo = getattr(valor, "__code__", None)
        if codigo is not None:
            visitar_codigo(codigo)
    dependencias = {
        modulo for simbolo, modulo in SIMBOLOS_DEPENDENCIA.items()
        if simbolo in simbolos
    }
    if any(nome.startswith("scipy_") for nome in simbolos):
        dependencias.add("scipy")
    return tuple(sorted(dependencias))


def requisitos_do_motor(nome, motor):
    explicitas = set(REQUISITOS_POR_MOTOR.get(nome, ()))
    return tuple(sorted(explicitas | set(_dependencias_detectadas(motor))))


@dataclass(frozen=True)
class MotorRegistrado:
    nome: str
    motor: object
    prioridade: int
    intencoes: tuple
    dependencias: tuple


class RegistroMotores:
    def __init__(self, verificar_dependencias=modulos_ausentes):
        self._motores = []
        self._por_nome = {}
        self._indice = defaultdict(list)
        self._intencoes_explicitas = set()
        self._fallback = []
        self._gerais = set()
        self._verificar_dependencias = verificar_dependencias

    def registrar(
        self, nome, motor, prioridade=0, intencoes=(), dependencias=(),
        fallback=False, geral=False,
    ):
        intencoes_informadas = tuple(intencoes)
        termos = intencoes_informadas or ALIASES.get(nome, ())
        explicitas = bool(intencoes_informadas or nome in ALIASES)
        if not termos:
            termos = tuple(p for p in nome.split("_") if len(p) >= 4)
        item = MotorRegistrado(
            nome, motor, prioridade, termos, tuple(dependencias)
        )
        self._motores.append(item)
        self._por_nome[nome] = item
        for termo in termos:
            chave = _normalizar(termo).strip()
            if item not in self._indice[chave]:
                self._indice[chave].append(item)
            if explicitas:
                self._intencoes_explicitas.add((nome, chave))
        if fallback:
            self._fallback.append(item)
        if geral:
            self._gerais.add(nome)

    @staticmethod
    def _chaves_entrada(entrada):
        texto = _normalizar(entrada)
        palavras = re.findall(r"[a-z0-9_]+|[+\-*/:%]", texto)
        chaves = set(palavras)
        chaves.update(
            simbolo for simbolo in ("+", "-", "/", ":", "%")
            if simbolo in texto
        )
        for tamanho in range(2, min(4, len(palavras)) + 1):
            chaves.update(
                " ".join(palavras[i:i + tamanho])
                for i in range(len(palavras) - tamanho + 1)
            )
        return chaves

    def candidatos(self, entrada):
        """Seleciona motores pelo índice sem executar o catálogo inteiro."""
        encontrados = {}
        for chave in self._chaves_entrada(entrada):
            for item in self._indice.get(chave, ()):
                especificidade = (
                    (item.nome, chave) in self._intencoes_explicitas,
                    len(chave.split()),
                    len(chave),
                    item.prioridade,
                )
                anterior = encontrados.get(item.nome)
                if anterior is None or especificidade > anterior[1]:
                    encontrados[item.nome] = (item, especificidade)
        indexados_ordenados = [
            item for item, _ in sorted(
                encontrados.values(), key=lambda par: par[1], reverse=True
            )
        ]
        indexados = [
            item for item in indexados_ordenados if item.nome not in self._gerais
        ]
        gerais = [
            item for item in indexados_ordenados if item.nome in self._gerais
        ]
        nomes = {item.nome for item in indexados}
        fallbacks = sorted(
            (item for item in self._fallback if item.nome not in nomes),
            key=lambda item: item.prioridade,
            reverse=True,
        )
        return indexados + fallbacks + gerais

    def despachar(self, entrada):
        """Retorna ``(nome, resultado, erro)`` ou ``None``."""
        primeiro_erro = None
        for item in self.candidatos(entrada):
            ausentes = self._verificar_dependencias(item.dependencias)
            if ausentes:
                if primeiro_erro is None:
                    primeiro_erro = (
                        item.nome,
                        None,
                        DependenciaAusenteError(item.nome, ausentes),
                    )
                continue
            calcular = getattr(item.motor, "calcular", None)
            if not callable(calcular):
                continue
            try:
                resultado = calcular(entrada)
            except Exception as erro:  # isolamento entre plugins/motores
                if str(erro) and primeiro_erro is None:
                    primeiro_erro = (item.nome, None, erro)
                continue
            if resultado is not None:
                return item.nome, resultado, None
        return primeiro_erro


def criar_registro(calculadora, ordem):
    registro = RegistroMotores()
    total = len(ordem)
    vistos = set()
    for indice, nome in enumerate(ordem):
        if nome in vistos:
            continue
        vistos.add(nome)
        motor = getattr(calculadora, nome, None)
        if motor is not None:
            registro.registrar(
                nome,
                motor,
                prioridade=total - indice,
                dependencias=requisitos_do_motor(nome, motor),
                fallback=nome in MOTORES_FALLBACK,
            )
    return registro
