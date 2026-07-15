"""Dados do mapa do "cão de caça" (`cao_de_caca/PSF-Calculadora`) -- catálogo de
motores de cálculo que abusam dependência externa de propósito (NumPy, SciPy,
SymPy, NetworkX, scikit-learn...), por fora da regra de construção do zero do
motor principal.

Isto NÃO é conhecimento PSF: nenhum nó daqui entra no grafo de Português ou
Matemática, nenhuma ponte é desenhada entre os dois mundos -- decisão
explícita do autor ("não ligar com outros motores"). O único papel deste
módulo é mostrar o que existe lá dentro, agrupado por assunto, para quem for
decidir se vale a pena consultar o cão de caça para um cálculo específico.

Como cão de caça vive fora do pacote principal (`cao_de_caca/PSF-Calculadora/`,
não instalado) e depende de bibliotecas científicas nem sempre presentes,
`dados_cao_de_caca()` nunca derruba o resto do mapa: se a importação falhar,
devolve uma lista vazia com o motivo declarado, nunca inventa um catálogo.
"""
from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CAMINHO_CAO_DE_CACA = RAIZ / "cao_de_caca" / "PSF-Calculadora"

_ATRIBUTOS_NAO_MOTORES = frozenset({
    "contador", "executando", "motor_problema_psf", "registro_motores",
})

_NOMES_DOMINIO_GRAFICOS = {
    "graficos": "funções e finanças básicas",
    "graficos_geometricos": "geometria plana",
    "graficos_calculo": "cálculo diferencial e integral",
    "graficos_algebra_linear": "álgebra linear",
    "graficos_probabilidade": "probabilidade e estatística",
    "graficos_grafos": "grafos",
    "graficos_calculo_vetorial": "cálculo vetorial",
    "graficos_equacoes_diferenciais": "equações diferenciais",
    "graficos_analise_avancada": "análise avançada",
    "graficos_matematica_aplicada": "matemática aplicada",
    "graficos_fundamentos": "fundamentos e lógica",
    "graficos_cultura_matematica": "cultura matemática",
    "graficos_analise_funcional": "análise funcional",
    "graficos_teoria_medida": "teoria da medida",
    "graficos_topologia": "topologia",
    "graficos_geometria_diferencial": "geometria diferencial",
}

# Segunda metade do catálogo (classes "...PSF") não tem marcador de secção
# própria -- agrupada por palavra-chave no nome do atributo.
_REGRAS_DOMINIO_PSF = (
    (("populacionais", "predador", "doencas", "difusao", "filogenetica",
      "waterman", "proteinas", "genicas", "huxley", "ecologia", "biologia"), "biologia matemática"),
    (("shannon", "informacao", "codigos", "viterbi", "ldpc", "quantica_psf",
      "compressao", "telecomunicacoes", "ecc_aplicacoes"), "teoria da informação"),
    (("fourier", "sobolev", "pseudodiferenciais", "wavelet", "tempo_frequencia",
      "processamento_sinais"), "análise harmônica e sinais"),
    (("otimizacao", "simplex", "branch", "genetico", "filas", "transporte",
      "fluxo_redes", "markov_decisao"), "otimização e pesquisa operacional"),
    (("curvas_algebricas", "bezout", "variedades_afins", "zariski", "feixes",
      "cohomologia", "curvas_elipticas", "riemann_roch", "superficies_riemann"), "geometria algébrica"),
    (("sistemas_dinamicos", "pontos_fixos", "bifurcacoes", "lyapunov",
      "atratores", "ergodica", "birkhoff", "entropia_dinamica", "fluxos_continuos"), "sistemas dinâmicos e caos"),
    (("nos_definicao", "invariantes_nos", "jones", "alexander", "khovanov",
      "heegaard", "cirurgia_dehn", "thurston", "geometrizacao", "nos_biologia"), "teoria dos nós"),
    (("pca_avancado", "agrupamentos", "discriminante", "regressao_logistica",
      "svm", "florestas", "redes_neurais", "embeddings", "bayesiana_mcmc", "causal"), "aprendizado de máquina"),
    (("poincare_computacional", "riemann_estado", "pvsnp", "navier_stokes",
      "bsd_numerico", "hodge_computacional", "yang_mills", "consciencia"), "problemas do milênio e pesquisa aberta"),
    (("provas_automaticas", "sintese_matematica", "algoritmos_complexidade",
      "ordenacao", "estruturas_dados", "equacoes_nao_lineares_numericas",
      "interpolacao", "integracao_numerica", "runge_kutta", "elementos_finitos"), "computação e análise numérica"),
    (("criptografia", "computacao_quantica"), "criptografia e computação quântica"),
    (("categorias", "funtores", "coprodutos", "colimites"), "teoria das categorias"),
    (("logica_primeira_ordem", "sistemas_dedutivos", "teoria_modelos", "turing",
      "indecidibilidade"), "lógica e computabilidade"),
    (("grupos_abstratos", "subgrupos_lagrange", "normais_quocientes",
      "homomorfismos_grupos", "aneis_abstratos", "ideais_quocientes",
      "aneis_polinomios", "corpos_extensoes", "galois"), "álgebra abstrata"),
    (("congruencias_lineares", "totiente", "euler_fermat", "primitivas_log",
      "residuos_quadraticos", "reciprocidade", "fracoes_continuas",
      "diofantinas", "algebricos_transcendentes", "fermat"), "teoria dos números avançada"),
)


def _dominio_psf(atributo: str) -> str:
    for chaves, nome in _REGRAS_DOMINIO_PSF:
        if any(chave in atributo for chave in chaves):
            return nome
    return "avançado psf (não classificado)"


def dados_cao_de_caca() -> dict:
    """Catálogo real dos motores do cão de caça, sem nenhuma aresta -- não há
    grafo de dependências aqui (cada motor é uma ferramenta independente), e
    nenhuma ponte para Português/Matemática é criada por decisão explícita.
    """
    if not CAMINHO_CAO_DE_CACA.exists():
        return {"nodes": [], "temas": [], "disponivel": False, "motivo": "cao_de_caca não encontrado"}

    caminho_str = str(CAMINHO_CAO_DE_CACA)
    inserido = caminho_str not in sys.path
    if inserido:
        sys.path.insert(0, caminho_str)
    try:
        assistente_psf = __import__("assistente_psf")
    except Exception as erro:  # noqa: BLE001 -- dependências científicas podem faltar; nunca derruba o mapa.
        if inserido:
            sys.path.remove(caminho_str)
        return {"nodes": [], "temas": [], "disponivel": False, "motivo": f"{type(erro).__name__}: {erro}"}

    try:
        calculadora = assistente_psf.PSFCalculadora()
        atributos = [a for a in vars(calculadora) if a not in _ATRIBUTOS_NAO_MOTORES]

        nodes = []
        dominio_atual = "fundamentos e cálculo escolar"
        entrou_psf = False

        for atributo in atributos:
            motor = getattr(calculadora, atributo)
            classe = type(motor).__name__

            if classe.startswith("Graficos"):
                dominio_atual = _NOMES_DOMINIO_GRAFICOS.get(atributo, atributo)
                continue

            if classe.endswith("PSF") and not entrou_psf:
                entrou_psf = True

            dominio = _dominio_psf(atributo) if entrou_psf else dominio_atual
            nodes.append({
                "nome": atributo,
                "classe": classe,
                "tema": dominio,
                "descricao": (type(motor).__doc__ or "").strip(),
                "grau": 0,
            })

        temas = sorted({n["tema"] for n in nodes})
        return {"nodes": nodes, "edges": [], "temas": temas, "disponivel": True, "motivo": None}
    finally:
        if inserido and caminho_str in sys.path:
            sys.path.remove(caminho_str)
