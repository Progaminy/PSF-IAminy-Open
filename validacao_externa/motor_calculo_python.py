
"""Etapa 59 — Motor de Cálculo Python Comparador.

Este módulo é propositalmente separado do núcleo PSF.

REGRA PRINCIPAL
---------------
O PSF puro constrói o método, a prova, a explicação e o raciocínio.
Este motor Python serve apenas como máquina de calcular, comparador,
verificador numérico, medidor de erro e auxiliar de investigação.

Permitido aqui:
- math, decimal, fractions e outras bibliotecas padrão do Python;
- fórmulas prontas como referência de comparação;
- cálculo otimizado/cache;
- teste de precisão e falsificação de valores.

Proibido aqui:
- declarar uma prova PSF;
- substituir a construção nativa;
- decidir verdade matemática profunda apenas por aproximação;
- esconder dependência como se fosse método PSF.
"""

from __future__ import annotations

import ast
import math
from dataclasses import dataclass, field
from decimal import Decimal, getcontext
from fractions import Fraction
from typing import Any, Dict, Iterable, List, Mapping, Optional, Tuple

getcontext().prec = 80

USO_PERMITIDO = (
    "comparar_valores",
    "maquina_de_calcular",
    "testar_precisao",
    "auxiliar_investigacao",
    "falsificar_resultado",
    "medir_erro",
)

USO_PROIBIDO = (
    "prova_psf",
    "metodo_fundamental",
    "fonte_do_conhecimento",
    "substituir_construcao_nativa",
    "prometer_resultado_sem_teste",
)

ESTADO_MOTOR = {
    "nome": "Motor de Cálculo Python Comparador",
    "etapa": 59,
    "tipo": "externo_auxiliar",
    "fundamento_psf": False,
    "usa_dependencias_python": True,
    "usa_dependencias_externas_pip": False,
    "pode_usar_math": True,
    "pode_usar_decimal": True,
    "pode_usar_fractions": True,
    "pode_provar_teorema": False,
    "pode_comparar": True,
    "pode_falsificar_valor": True,
    "mensagem": "Este motor calcula e compara; não cria método PSF.",
}

class ExpressaoNaoPermitida(ValueError):
    """Erro lançado quando uma expressão tenta sair do calculador seguro."""

_FUNCOES = {
    "abs": abs,
    "round": round,
    "pow": pow,
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "floor": math.floor,
    "ceil": math.ceil,
    "factorial": math.factorial,
    "gcd": math.gcd,
    "comb": math.comb,
    "perm": math.perm,
    "isclose": math.isclose,
    "degrees": math.degrees,
    "radians": math.radians,
}

_CONSTANTES = {
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "inf": math.inf,
}

_OPERADORES_BINARIOS = {
    ast.Add: lambda a, b: a + b,
    ast.Sub: lambda a, b: a - b,
    ast.Mult: lambda a, b: a * b,
    ast.Div: lambda a, b: a / b,
    ast.FloorDiv: lambda a, b: a // b,
    ast.Mod: lambda a, b: a % b,
    ast.Pow: lambda a, b: a ** b,
}

_OPERADORES_UNARIOS = {
    ast.UAdd: lambda a: +a,
    ast.USub: lambda a: -a,
}

class CalculadoraSegura:
    """Calculadora Python segura para comparação, com cache simples.

    Não executa código arbitrário: interpreta apenas nós AST numéricos permitidos.
    """

    def __init__(self) -> None:
        self.cache: Dict[str, Any] = {}

    def calcular(self, expressao: str) -> Any:
        chave = expressao.strip()
        if chave in self.cache:
            return self.cache[chave]
        arvore = ast.parse(chave, mode="eval")
        resultado = self._avaliar(arvore.body)
        self.cache[chave] = resultado
        return resultado

    def _avaliar(self, node: ast.AST) -> Any:
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float, bool)):
                return node.value
            raise ExpressaoNaoPermitida("Constante não numérica não permitida.")

        if isinstance(node, ast.Name):
            if node.id in _CONSTANTES:
                return _CONSTANTES[node.id]
            raise ExpressaoNaoPermitida(f"Nome não permitido: {node.id}")

        if isinstance(node, ast.BinOp):
            tipo = type(node.op)
            if tipo not in _OPERADORES_BINARIOS:
                raise ExpressaoNaoPermitida("Operador binário não permitido.")
            esquerda = self._avaliar(node.left)
            direita = self._avaliar(node.right)
            if tipo is ast.Pow and isinstance(direita, (int, float)) and abs(direita) > 10000:
                raise ExpressaoNaoPermitida("Expoente demasiado grande para calculadora segura.")
            return _OPERADORES_BINARIOS[tipo](esquerda, direita)

        if isinstance(node, ast.UnaryOp):
            tipo = type(node.op)
            if tipo not in _OPERADORES_UNARIOS:
                raise ExpressaoNaoPermitida("Operador unário não permitido.")
            return _OPERADORES_UNARIOS[tipo](self._avaliar(node.operand))

        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ExpressaoNaoPermitida("Chamadas complexas não permitidas.")
            nome = node.func.id
            if nome not in _FUNCOES:
                raise ExpressaoNaoPermitida(f"Função não permitida: {nome}")
            args = [self._avaliar(arg) for arg in node.args]
            kwargs = {kw.arg: self._avaliar(kw.value) for kw in node.keywords if kw.arg is not None}
            return _FUNCOES[nome](*args, **kwargs)

        raise ExpressaoNaoPermitida(f"Expressão não permitida: {type(node).__name__}")

CALCULADORA = CalculadoraSegura()

@dataclass
class ComparacaoValor:
    valor_psf: Any
    valor_python: Any
    erro_absoluto: float
    erro_relativo: float
    tolerancia: float
    aprovado: bool
    uso: str = "comparacao_nao_metodo"
    aviso: str = "Comparação numérica não é prova PSF."

@dataclass
class RelatorioValidacao:
    pergunta: str
    expressao_python: str
    valor_psf: Any
    comparacao: ComparacaoValor
    estado: str
    passos: List[str] = field(default_factory=list)
    lacunas: List[str] = field(default_factory=list)
    proximo_passo_psf: str = "Se falhar, voltar ao método PSF puro e procurar o salto."

def _como_float(x: Any) -> float:
    if isinstance(x, bool):
        return 1.0 if x else 0.0
    if isinstance(x, Fraction):
        return float(x)
    if isinstance(x, Decimal):
        return float(x)
    return float(x)

def medir_erro(valor_psf: Any, valor_referencia: Any) -> Tuple[float, float]:
    """Mede erro absoluto e relativo entre PSF e referência Python."""
    a = _como_float(valor_psf)
    b = _como_float(valor_referencia)
    absoluto = abs(a - b)
    relativo = absoluto / max(abs(b), 1.0)
    return absoluto, relativo

def comparar_valores(valor_psf: Any, valor_python: Any, tolerancia: float = 1e-9) -> ComparacaoValor:
    absoluto, relativo = medir_erro(valor_psf, valor_python)
    aprovado = absoluto <= tolerancia or relativo <= tolerancia
    return ComparacaoValor(
        valor_psf=valor_psf,
        valor_python=valor_python,
        erro_absoluto=absoluto,
        erro_relativo=relativo,
        tolerancia=tolerancia,
        aprovado=aprovado,
    )

def calcular_expressao(expressao: str) -> Any:
    """Calcula uma expressão numérica segura para comparação."""
    return CALCULADORA.calcular(expressao)

def validar_resposta_numerica(pergunta: str, valor_psf: Any, expressao_python: str, tolerancia: float = 1e-9) -> RelatorioValidacao:
    """Compara o valor produzido pelo PSF com um valor calculado por Python."""
    valor_python = calcular_expressao(expressao_python)
    comparacao = comparar_valores(valor_psf, valor_python, tolerancia)
    estado = "APROVADO_COMO_VALOR_COMPARADO" if comparacao.aprovado else "FALHOU_COMPARACAO"
    lacunas: List[str] = []
    if not comparacao.aprovado:
        lacunas.append("valor_psf_difere_do_valor_python")
    passos = [
        "receber valor produzido pelo PSF puro",
        "calcular referência no motor Python externo",
        "medir erro absoluto e relativo",
        "comparar com tolerância declarada",
        "marcar aprovado ou falha sem transformar Python em prova",
    ]
    return RelatorioValidacao(
        pergunta=pergunta,
        expressao_python=expressao_python,
        valor_psf=valor_psf,
        comparacao=comparacao,
        estado=estado,
        passos=passos,
        lacunas=lacunas,
    )

def fracao_exata(numerador: int, denominador: int) -> Fraction:
    """Cria fração exata para comparação racional."""
    return Fraction(numerador, denominador)

def decimal_preciso(valor: str) -> Decimal:
    """Cria Decimal de alta precisão a partir de texto."""
    return Decimal(valor)

def comparar_listas(valores_psf: Iterable[Any], valores_python: Iterable[Any], tolerancia: float = 1e-9) -> Dict[str, Any]:
    pares = list(zip(list(valores_psf), list(valores_python)))
    comparacoes = [comparar_valores(a, b, tolerancia) for a, b in pares]
    falhas = [c for c in comparacoes if not c.aprovado]
    maior_erro = max((c.erro_absoluto for c in comparacoes), default=0.0)
    return {
        "quantidade": len(comparacoes),
        "aprovados": len(comparacoes) - len(falhas),
        "falhas": len(falhas),
        "maior_erro_absoluto": maior_erro,
        "aprovado": len(falhas) == 0,
        "aviso": "Comparação de lista não substitui demonstração PSF.",
    }

def validar_metricas_empiricas(metricas: Mapping[str, float]) -> Dict[str, Any]:
    """Valida metas empíricas como critério de aprovação, não como promessa.

    Chaves reconhecidas: erro_maximo, auc, recall.
    """
    resultados: Dict[str, Any] = {
        "tipo": "criterio_de_aprovacao_empirica",
        "promessa": False,
        "aprovacoes": {},
        "falhas": [],
    }
    if "erro_maximo" in metricas:
        ok = metricas["erro_maximo"] <= 0.05
        resultados["aprovacoes"]["erro_maximo_ate_5_porcento"] = ok
        if not ok:
            resultados["falhas"].append("erro_maximo_maior_que_5_porcento")
    if "auc" in metricas:
        ok = metricas["auc"] > 0.95
        resultados["aprovacoes"]["auc_maior_que_0_95"] = ok
        if not ok:
            resultados["falhas"].append("auc_nao_superou_0_95")
    if "recall" in metricas:
        ok = metricas["recall"] > 0.85
        resultados["aprovacoes"]["recall_maior_que_0_85"] = ok
        if not ok:
            resultados["falhas"].append("recall_nao_superou_0_85")
    resultados["aprovado"] = len(resultados["falhas"]) == 0
    resultados["aviso"] = "Métrica empírica aprova teste observado; não garante futuro."
    return resultados

def detectar_uso_indevido(texto: str) -> List[str]:
    """Detecta frases que tentam transformar o comparador em fundamento."""
    baixo = texto.lower()
    alertas: List[str] = []
    gatilhos = {
        "python provou": "python_nao_prova_psf",
        "math provou": "math_nao_prova_psf",
        "porque o python disse": "autoridade_externa_indevida",
        "logo está demonstrado": "comparacao_nao_e_demonstracao",
        "não precisa construir": "pulou_construcao_psf",
        "garantido para sempre": "promessa_falsa_por_teste_finito",
    }
    for frase, alerta in gatilhos.items():
        if frase in baixo:
            alertas.append(alerta)
    return alertas

def politica_do_motor() -> Dict[str, Any]:
    return {
        "estado": ESTADO_MOTOR,
        "uso_permitido": USO_PERMITIDO,
        "uso_proibido": USO_PROIBIDO,
        "regra_curta": "Python calcula para comparar; PSF constrói para entender.",
    }
