"""Agrupamento dos motores por domínio, sem importar dependências pesadas."""

DOMINIOS = {
    "aritmetica": {"adicao_subtracao", "divisao", "multiplos", "fracoes", "porcentagem", "mdc", "mmc"},
    "algebra": {"equacoes", "equacao_segundo_grau", "polinomios", "matrizes", "sistemas_lineares"},
    "geometria": {"formas", "perimetro", "area", "pitagoras", "geometria_espacial"},
    "calculo": {"limites", "derivadas", "integral_definida", "integral_indefinida", "series_fourier"},
    "estatistica": {"media", "dispersao", "probabilidade", "estatistica_central"},
    "computacao": {"algoritmos_ordenacao", "estruturas_dados", "computacao_quantica"},
    "aplicada": {"financeira_avancada", "otimizacao_linear", "processamento_sinais", "modelos_populacionais_novo"},
}


def dominio_do_motor(nome):
    for dominio, motores in DOMINIOS.items():
        if nome in motores:
            return dominio
    return "avancada"
