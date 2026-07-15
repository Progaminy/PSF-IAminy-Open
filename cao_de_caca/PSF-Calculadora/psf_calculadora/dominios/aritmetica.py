"""Motores aritméticos independentes e sem dependências científicas."""

from decimal import Decimal, InvalidOperation
import re
import unicodedata

from ._legado import resolver

__all__ = [
    "MotorAdicaoSubtracao", "MotorDivisao", "MotorMultiplos",
    "MotorFracoes", "MotorPorcentagem", "MotorMMC", "MotorMDC",
]


def _normalizar(texto):
    texto = unicodedata.normalize("NFD", str(texto).lower().strip())
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = texto.replace("−", "-").replace("×", "*").replace("÷", "/")
    texto = re.sub(r"[?!;]+", " ", texto)
    return re.sub(r"\s+", " ", texto.replace(",", ".")).strip()


def _formatar(valor):
    valor = valor if isinstance(valor, Decimal) else Decimal(str(valor))
    if valor == valor.to_integral():
        return str(valor.quantize(Decimal("1")))
    return format(valor.normalize(), "f").rstrip("0").rstrip(".")


class MotorAdicaoSubtracao:
    COMANDOS = (
        "quanto e", "resultado de", "calcular", "calcule", "resolver",
        "resolva", "somar", "some", "adicionar", "adicione", "subtrair",
        "subtraia",
    )

    def calcular(self, entrada):
        expressao = _normalizar(entrada)
        for comando in self.COMANDOS:
            expressao = expressao.replace(comando, "")
        expressao = re.sub(r"\s+", "", expressao)
        if re.fullmatch(r"[+-]?\d+(?:\.\d+)?(?:[+-]\d+(?:\.\d+)?)+", expressao) is None:
            return None
        try:
            termos = [Decimal(x) for x in re.findall(r"[+-]?\d+(?:\.\d+)?", expressao)]
        except InvalidOperation:
            return None
        return {"expressao": expressao, "resultado": _formatar(sum(termos, Decimal("0")))}


class MotorMultiplos:
    QUANTIDADE_PADRAO = 10
    LIMITE_MAXIMO = 1000

    def calcular(self, entrada):
        texto = _normalizar(entrada)
        if "multiplo" not in texto:
            return None
        zero = "incluindo zero" in texto or "com zero" in texto
        padrao = re.fullmatch(
            r"(?:(\d+) )?(?:os )?multiplos(?: negativos)? de ([+-]?\d+)"
            r"(?: ate ([+-]?\d+))?(?: incluindo zero| com zero)?",
            texto,
        )
        if not padrao:
            return {"erro": "Use: 'múltiplos de 2', '5 múltiplos de -3' ou 'múltiplos de -4 até -40'."}
        quantidade, base, limite = padrao.groups()
        base = int(base)
        if "negativos" in texto:
            base = -abs(base)
        if limite is not None:
            valores = self._ate_limite(base, int(limite), zero)
            return {"descricao": f"Múltiplos de {base} até {limite}", "valores": valores}
        quantidade = int(quantidade or self.QUANTIDADE_PADRAO)
        if quantidade <= 0 or quantidade > self.LIMITE_MAXIMO:
            return {"erro": f"A quantidade deve estar entre 1 e {self.LIMITE_MAXIMO}."}
        inicio = 0 if zero else 1
        valores = [base * i for i in range(inicio, inicio + quantidade)]
        return {"descricao": f"{quantidade} múltiplos de {base}", "valores": valores}

    def _ate_limite(self, base, limite, zero):
        if base == 0:
            return [0]
        atual = 0 if zero else base
        valores = []
        comparar = (lambda x: x <= limite) if base > 0 else (lambda x: x >= limite)
        while comparar(atual) and len(valores) < self.LIMITE_MAXIMO:
            valores.append(atual)
            atual += base
        return valores


class MotorDivisao:
    def calcular(self, entrada):
        texto = _normalizar(entrada)
        numero = r"([+-]?\d+(?:\.\d+)?)"
        padroes = (
            rf"{numero}\s*(?:/|:)\s*{numero}",
            rf"(?:dividir|divida|repartir|reparta)\s+{numero}\s+por\s+{numero}",
            rf"{numero}\s+(?:dividido|dividida)\s+por\s+{numero}",
            rf"(?:agrupar|agrupe)\s+{numero}\s+(?:em\s+)?grupos?\s+de\s+{numero}",
        )
        grupos = next((m.groups() for p in padroes if (m := re.fullmatch(p, texto))), None)
        if grupos is None:
            return None
        a, b = map(Decimal, grupos)
        if b == 0:
            return {"erro": "O divisor externo não pode ser zero."}
        resultado = {"dividendo": _formatar(a), "divisor": _formatar(b), "quociente": _formatar(a / b)}
        if a == a.to_integral() and b == b.to_integral():
            ai, bi = int(a), int(b)
            qi = abs(ai) // abs(bi)
            qi = -qi if (ai < 0) != (bi < 0) else qi
            resultado.update(resto=ai - bi * qi, exata=ai - bi * qi == 0)
        return resultado


_MIGRADOS = {"MotorAdicaoSubtracao", "MotorDivisao", "MotorMultiplos"}


def __getattr__(nome):
    if nome in __all__ and nome not in _MIGRADOS:
        return resolver(nome)
    raise AttributeError(nome)
