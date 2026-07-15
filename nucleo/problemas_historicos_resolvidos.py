# -*- coding: utf-8 -*-
"""
Etapa 49 — Problemas Históricos Famosos Resolvidos.
Regra PSF: conteúdo definitivo, sem dependências externas como fundamento.
Este módulo guarda conhecimento histórico-matemático resolvido com estado honesto.
"""

ETAPA = 49
ESTADO = "DEFINITIVO_RESOLVIDO_HISTORICO"
SEM_DEPENDENCIAS_EXTERNAS = True

PROBLEMAS_HISTORICOS_RESOLVIDOS = [
    {
        "id": "E49-H01",
        "nome": "Último Teorema de Fermat",
        "periodo": "1637–1994",
        "resolvido_por": "Andrew Wiles, com correção conjunta com Richard Taylor",
        "ano": "1994",
        "tempo_em_aberto": "357 anos",
        "area": ["Teoria dos Números", "Geometria Algébrica", "Formas Modulares"],
        "enunciado": "Para n > 2, a equação x^n + y^n = z^n não tem soluções inteiras positivas.",
        "estrategia": "Redução à modularidade de curvas elípticas semiestáveis via representação de Galois e teoria de deformações.",
        "impacto": "Unificou curvas elípticas, formas modulares, teoria de Galois e abriu caminhos ligados ao programa de Langlands.",
    },
    {
        "id": "E49-H02",
        "nome": "Conjectura de Poincaré",
        "periodo": "1904–2003",
        "resolvido_por": "Grigori Perelman, sobre o programa de Richard Hamilton",
        "ano": "2003",
        "tempo_em_aberto": "99 anos",
        "area": ["Topologia", "Geometria Diferencial", "Análise Geométrica"],
        "enunciado": "Toda 3-variedade fechada, compacta e simplesmente conexa é homeomorfa à esfera S^3.",
        "estrategia": "Fluxo de Ricci com cirurgia, funcionais de entropia, não colapso e análise de singularidades.",
        "impacto": "Resolveu a Geometrização de Thurston e transformou a análise geométrica moderna.",
    },
    {
        "id": "E49-H03",
        "nome": "Teorema das Quatro Cores",
        "periodo": "1852–1976",
        "resolvido_por": "Kenneth Appel e Wolfgang Haken",
        "ano": "1976",
        "tempo_em_aberto": "124 anos",
        "area": ["Teoria dos Grafos", "Combinatória", "Topologia"],
        "enunciado": "Todo mapa plano pode ser colorido com no máximo quatro cores de modo que regiões adjacentes tenham cores distintas.",
        "estrategia": "Redução a configurações inevitáveis e verificação computacional de redutibilidade.",
        "impacto": "Introduziu em grande escala a prova assistida por computador e levantou debates sobre verificação formal.",
    },
    {
        "id": "E49-H04",
        "nome": "Transcendência de pi",
        "periodo": "1882",
        "resolvido_por": "Ferdinand von Lindemann",
        "ano": "1882",
        "tempo_em_aberto": "aproximadamente 200 anos de suspeita moderna; quadratura do círculo vinha da Antiguidade",
        "area": ["Teoria dos Números", "Transcendência"],
        "enunciado": "pi não é raiz de nenhum polinómio não nulo com coeficientes inteiros.",
        "estrategia": "Extensão das técnicas de Hermite sobre transcendência de e e consequências para exponenciais de algébricos.",
        "impacto": "Mostrou a impossibilidade da quadratura do círculo por régua e compasso.",
    },
    {
        "id": "E49-H05",
        "nome": "Teorema Fundamental da Álgebra",
        "periodo": "1799",
        "resolvido_por": "Carl Friedrich Gauss",
        "ano": "1799",
        "tempo_em_aberto": "cerca de 200 anos de desenvolvimento informal e tentativas incompletas",
        "area": ["Álgebra", "Análise Complexa"],
        "enunciado": "Todo polinómio complexo não constante tem pelo menos uma raiz complexa.",
        "estrategia": "Analisar o mínimo de |P(z)| e mostrar que, se P(z0) != 0, pode-se diminuir localmente esse módulo.",
        "impacto": "Consolidou C como corpo algebricamente fechado fundamental para a matemática moderna.",
    },
    {
        "id": "E49-H06",
        "nome": "Independência da Hipótese do Contínuo",
        "periodo": "1878–1963",
        "resolvido_por": "Kurt Gödel e Paul Cohen",
        "ano": "1940/1963",
        "tempo_em_aberto": "85 anos",
        "area": ["Lógica", "Teoria dos Conjuntos"],
        "enunciado": "Não existe cardinal estritamente entre o dos naturais e o dos reais? A pergunta é independente de ZFC.",
        "estrategia": "Gödel construiu L onde HC vale; Cohen criou forcing para modelos onde HC falha.",
        "impacto": "Revolucionou a noção de independência, modelos e forcing em teoria dos conjuntos.",
    },
    {
        "id": "E49-H07",
        "nome": "Teorema dos Números Primos",
        "periodo": "c.1793–1896",
        "resolvido_por": "Jacques Hadamard e Charles-Jean de la Vallée Poussin",
        "ano": "1896",
        "tempo_em_aberto": "cerca de 100 anos",
        "area": ["Teoria Analítica dos Números", "Análise Complexa"],
        "enunciado": "A função contadora de primos satisfaz pi(x) ~ x/log(x).",
        "estrategia": "Estudar a função zeta de Riemann e mostrar ausência de zeros na reta Re(s)=1.",
        "impacto": "Fundou a teoria analítica moderna dos números e aprofundou a ligação entre primos e zeros da zeta.",
    },
    {
        "id": "E49-H08",
        "nome": "Classificação dos Grupos Finitos Simples",
        "periodo": "1955–2004",
        "resolvido_por": "Esforço colaborativo, incluindo Gorenstein, Aschbacher, Lyons e Solomon",
        "ano": "1955–2004",
        "tempo_em_aberto": "cerca de 150 anos desde Galois",
        "area": ["Teoria dos Grupos", "Álgebra"],
        "enunciado": "Classificar todos os grupos finitos simples.",
        "estrategia": "Divisão em famílias: cíclicos de ordem prima, alternados, grupos de tipo Lie e 26 esporádicos, com análise profunda de subgrupos locais.",
        "impacto": "Um dos maiores teoremas coletivos da matemática, com milhares de páginas de prova e aplicações em simetria.",
    },
    {
        "id": "E49-H09",
        "nome": "Teorema de Fermat-Euler sobre soma de dois quadrados",
        "periodo": "1640–1747",
        "resolvido_por": "Leonhard Euler, a partir de enunciados de Fermat",
        "ano": "1747",
        "tempo_em_aberto": "cerca de 100 anos",
        "area": ["Teoria dos Números", "Formas Quadráticas"],
        "enunciado": "Um primo ímpar p é soma de dois quadrados se e só se p ≡ 1 mod 4.",
        "estrategia": "Descida infinita e identidade multiplicativa de somas de dois quadrados.",
        "impacto": "Antecipou a teoria algébrica dos números e o estudo dos inteiros gaussianos Z[i].",
    },
    {
        "id": "E49-H10",
        "nome": "Resolução de Singularidades em característica zero",
        "periodo": "1964",
        "resolvido_por": "Heisuke Hironaka",
        "ano": "1964",
        "tempo_em_aberto": "cerca de 100 anos em forma moderna",
        "area": ["Geometria Algébrica"],
        "enunciado": "Toda variedade algébrica sobre corpo de característica zero admite resolução de singularidades.",
        "estrategia": "Sequência controlada de blow-ups em centros suaves escolhidos por invariantes que melhoram a singularidade.",
        "impacto": "Ferramenta central em geometria algébrica, birracionalidade e aplicações geométricas modernas.",
    },
]

def listar():
    return list(PROBLEMAS_HISTORICOS_RESOLVIDOS)

def obter_por_id(pid):
    for p in PROBLEMAS_HISTORICOS_RESOLVIDOS:
        if p["id"] == pid:
            return dict(p)
    raise KeyError(pid)

def resposta_curta(pid):
    p = obter_por_id(pid)
    return f"{p['nome']} foi resolvido por {p['resolvido_por']} em {p['ano']}. Ideia central: {p['estrategia']}"

def aula(pid, modo="detalhada"):
    p = obter_por_id(pid)
    if modo == "direta":
        return f"Tema: {p['nome']}. Enunciado: {p['enunciado']} Resolução: {p['estrategia']} Impacto: {p['impacto']}"
    if modo == "passo_a_passo":
        return "\n".join([
            f"Tema: {p['nome']}",
            f"1. Problema: {p['enunciado']}",
            f"2. Área: {', '.join(p['area'])}",
            f"3. Quem resolveu: {p['resolvido_por']}",
            f"4. Estratégia: {p['estrategia']}",
            f"5. Impacto: {p['impacto']}",
            "6. Lição PSF: problema histórico resolvido deve ser tratado como teorema estabelecido, com contexto, método e limites honestos.",
        ])
    return f"{p['nome']} é um problema histórico resolvido. O núcleo da aula é ligar enunciado, método de solução e impacto matemático: {p['estrategia']}"

def validar_cobertura():
    obrig = ["id", "nome", "periodo", "resolvido_por", "ano", "tempo_em_aberto", "area", "enunciado", "estrategia", "impacto"]
    for p in PROBLEMAS_HISTORICOS_RESOLVIDOS:
        for k in obrig:
            if k not in p or p[k] in (None, ""):
                return False, p.get("id", "SEM_ID"), k
        for modo in ("direta", "detalhada", "passo_a_passo"):
            if not aula(p["id"], modo):
                return False, p["id"], modo
    return True, "OK", "OK"
