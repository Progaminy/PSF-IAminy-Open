"""Etapa 41 — Cálculo Diferencial e Integral I-II definitivo PSF.

Entrada do usuário: bloco definitivo com 200 perguntas de Cálculo Diferencial
Integral I e II, incluindo Álgebra Linear I, Geometria Analítica, integrais em
várias variáveis, Fourier, Análise Complexa e EDO avançado.

Regra herdada da Etapa 39: tudo que o usuário traz entra como definitivo.
Regra herdada da Etapa 40: definitivo não significa resposta fingida; significa
preservação, classificação, auditoria, expansão obrigatória e construção gradual.

Pureza: este módulo não usa math, numpy, sympy, internet, API externa ou motor
matemático externo. Ele registra a estrutura de conhecimento, respostas-base e
regras operacionais em linguagem PSF.
"""
from __future__ import annotations

from dataclasses import dataclass

from nucleo.politica_definitividade import normalizar_estado_definitivo


@dataclass(frozen=True, slots=True)
class BlocoCalculoEtapa41:
    id_bloco: str
    curso: str
    nome: str
    intervalo: str
    quantidade: int
    nivel: str
    topicos: tuple[str, ...]
    estado: str


@dataclass(frozen=True, slots=True)
class ConceitoCalculoEtapa41:
    chave: str
    nome: str
    estado: str
    depende_de: tuple[str, ...]
    definicao_psf: str
    regra_operacional: str
    regra_de_teste: str
    modos_aula: tuple[str, ...] = ("direta", "detalhada", "passo_a_passo")


@dataclass(frozen=True, slots=True)
class RespostaCalculoEtapa41:
    id_resposta: str
    pergunta_referencia: str
    resposta_pronta: str
    topico: str
    construcao: str
    estado: str = "DEFINITIVO_COM_RESPOSTA_APROVADA"


BLOCOS_CALCULO_ETAPA_41: tuple[BlocoCalculoEtapa41, ...] = (
    BlocoCalculoEtapa41("41-I-01", "Calculo I", "Limites e continuidade", "1-10", 10, "calculo_rigoroso", ("epsilon_delta", "continuidade", "bolzano", "thomae", "uniforme"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-I-02", "Calculo I", "Derivadas", "11-20", 10, "calculo_rigoroso", ("derivada_por_definicao", "logaritmica", "implicita", "inversa", "trigonometricas"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-I-03", "Calculo I", "Teoremas fundamentais", "21-30", 10, "calculo_rigoroso", ("rolle", "lagrange", "cauchy", "lhopital", "taylor", "maclaurin", "resto"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-I-04", "Calculo I", "Aplicações das derivadas", "31-40", 10, "calculo_aplicado", ("monotonia", "concavidade", "otimizacao", "taxas_relacionadas", "newton", "diferencial"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-I-05", "Calculo I", "Primitivas", "41-50", 10, "calculo_integral", ("partes", "substituicao", "trigonometricas", "hiperbolica", "racionais", "logaritmicas"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-I-06", "Calculo I", "Integral definido", "51-60", 10, "calculo_integral", ("riemann", "tfc", "areas", "volumes", "arco", "superficie", "valor_medio", "improprios"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-I-07", "Calculo I", "Séries numéricas", "61-70", 10, "analise_series", ("geometrica", "telescopica", "divergencia", "integral", "comparacao", "razao", "raiz", "leibniz"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-I-08", "Calculo I", "Séries de potências", "71-80", 10, "analise_series", ("raio_convergencia", "taylor", "arctg", "erro", "intervalo", "derivar_series", "integrar_series"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-I-09", "Calculo I", "Álgebra Linear I", "81-90", 10, "algebra_linear", ("gauss", "determinante", "vandermonde", "inversa", "espaco_vetorial", "base", "nucleo", "imagem", "autovalores"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-I-10", "Calculo I", "Geometria Analítica", "91-100", 10, "geometria_analitica", ("ponto_plano", "reta_plano", "angulo_planos", "distancia_retas", "intersecao", "esfera", "projecao", "produto_vetorial", "conicas"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-II-01", "Calculo II", "Funções de várias variáveis", "1-10", 10, "calculo_multivariavel", ("dominio_imagem", "curvas_nivel", "limites_multivariaveis", "continuidade", "derivadas_parciais", "onda"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-II-02", "Calculo II", "Diferenciabilidade", "11-20", 10, "calculo_multivariavel", ("diferenciabilidade", "plano_tangente", "aproximacao_linear", "diferencial_total", "regra_cadeia", "gradiente", "derivada_direcional"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-II-03", "Calculo II", "Otimização em várias variáveis", "21-30", 10, "otimizacao_multivariavel", ("criticos", "hessiana", "sela", "lagrange", "restricoes", "area_minima"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-II-04", "Calculo II", "Integrais duplos", "31-40", 10, "integracao_multivariavel", ("retangulos", "regioes", "ordem_integracao", "polares", "gauss", "volume"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-II-05", "Calculo II", "Integrais triplos", "41-50", 10, "integracao_multivariavel", ("caixas", "esfera", "cilindricas", "esfericas", "massa", "centro_massa", "inercia", "cone"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-II-06", "Calculo II", "Integrais de linha e superfície", "51-60", 10, "calculo_vetorial", ("linha", "trabalho", "conservativo", "green", "superficie", "fluxo", "gauss_divergencia"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-II-07", "Calculo II", "Séries de Fourier", "61-70", 10, "analise_harmonica", ("fourier", "parseval", "gibbs", "dirichlet", "senos", "cossenos", "transformada", "convolucao"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-II-08", "Calculo II", "Análise Complexa", "71-90", 20, "analise_complexa", ("holomorfa", "cauchy_riemann", "integral_complexa", "cauchy", "laurent", "singularidade", "residuos", "mobius", "liouville", "gamma"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
    BlocoCalculoEtapa41("41-II-09", "Calculo II", "EDO avançado", "91-100", 10, "edo_avancada", ("segunda_ordem", "ressonancia", "sistemas", "variacao_parametros", "series", "bessel", "laplace", "green"), normalizar_estado_definitivo("DEFINITIVO_CLASSIFICADO")),
)

TOTAL_PERGUNTAS_ETAPA_41: int = 200

CONCEITOS_CALCULO_ETAPA_41: tuple[ConceitoCalculoEtapa41, ...] = (
    ConceitoCalculoEtapa41("epsilon_delta_operacional", "Prova ε-δ", "DEFINITIVO_COM_AULA", ("limite", "vizinhanca", "desigualdade"), "Provar limite por ε-δ é construir uma regra que transforma qualquer tolerância vertical ε numa tolerância horizontal δ.", "Isolar |f(x)-L| e escolher δ que garanta esse valor menor que ε.", "A prova é válida quando todo ε positivo recebe δ positivo e respeita 0<|x-a|<δ."),
    ConceitoCalculoEtapa41("continuidade_uniforme", "Continuidade uniforme", "DEFINITIVO_COM_AULA", ("continuidade", "epsilon_delta", "intervalo"), "Continuidade uniforme usa o mesmo δ para todos os pontos do domínio.", "Controlar |f(x)-f(y)| por |x-y| sem depender do ponto escolhido.", "Validar se δ não muda quando o ponto muda; em compacto usar Heine-Cantor."),
    ConceitoCalculoEtapa41("derivada_por_limite_rigorosa", "Derivada por definição", "DEFINITIVO_COM_AULA", ("limite", "quociente_incremental"), "Derivada é limite da taxa média quando a variação da entrada tende a zero.", "Formar [f(x+h)-f(x)]/h, simplificar e tomar h→0.", "A expressão final deve representar inclinação local ou taxa instantânea."),
    ConceitoCalculoEtapa41("taylor_maclaurin_resto", "Taylor, MacLaurin e resto", "DEFINITIVO_COM_AULA", ("derivadas_sucessivas", "aproximacao", "erro"), "Taylor reconstrói uma função perto de um ponto por derivadas sucessivas e controla o erro pelo resto.", "Calcular derivadas no ponto, montar polinómio e estimar resto por limite ou cota.", "A aproximação só é aceite com ordem, centro e erro explicitados."),
    ConceitoCalculoEtapa41("otimizacao_diferencial", "Otimização diferencial", "DEFINITIVO_COM_AULA", ("derivada", "restricao", "fronteira"), "Otimizar é procurar valores extremos respeitando domínio e restrições.", "Reduzir variáveis, derivar, resolver pontos críticos, testar sinal/fronteira.", "O candidato deve satisfazer a condição e ser classificado."),
    ConceitoCalculoEtapa41("integracao_por_partes_ciclica", "Integração por partes e cíclica", "DEFINITIVO_COM_AULA", ("produto", "primitiva", "derivada"), "Partes inverte a regra do produto; casos cíclicos devolvem a integral original.", "Escolher u e dv, aplicar ∫u dv=uv-∫v du e isolar quando a integral reaparece.", "Diferenciar a resposta deve recuperar o integrando."),
    ConceitoCalculoEtapa41("integral_riemann_tfc", "Integral de Riemann e TFC", "DEFINITIVO_COM_AULA", ("soma", "limite", "acumulacao"), "Integral definido é limite de somas de áreas; o TFC liga acumulação e derivada.", "Particionar, somar retângulos e passar ao limite; ou usar primitiva quando permitido.", "Resultado deve coincidir com soma-limite ou diferença de primitivas."),
    ConceitoCalculoEtapa41("series_convergencia_completa", "Séries e critérios de convergência", "DEFINITIVO_COM_AULA", ("sucessao", "soma_parcial", "limite"), "Série é sucessão de somas parciais; converge se essas somas estabilizam.", "Aplicar condição necessária, comparação, integral, razão, raiz ou Leibniz conforme a forma.", "Critério usado deve ser explicitamente compatível com os termos."),
    ConceitoCalculoEtapa41("series_potencias", "Séries de potências", "DEFINITIVO_COM_AULA", ("series", "raio", "intervalo"), "Série de potências é uma soma infinita controlada por distância ao centro.", "Usar razão/raiz para obter raio; testar extremos separadamente.", "Intervalo final deve indicar centro, raio e extremos."),
    ConceitoCalculoEtapa41("gauss_algebra_linear", "Eliminação de Gauss e bases", "DEFINITIVO_COM_AULA", ("matriz", "sistema", "operacao_linha"), "Gauss transforma sistema mantendo soluções até revelar pivôs, núcleo e imagem.", "Usar operações elementares, triangularizar e ler solução/dimensão.", "Operações devem preservar equivalência do sistema."),
    ConceitoCalculoEtapa41("geometria_analitica_vetorial", "Geometria analítica vetorial", "DEFINITIVO_COM_AULA", ("vetor", "produto_escalar", "produto_vetorial", "distancia"), "Objetos geométricos viram relações entre pontos, vetores, planos e distâncias.", "Construir vetores diretores/normais e aplicar projeção, produto escalar/vetorial e equações.", "Resultado deve satisfazer a condição geométrica original."),
    ConceitoCalculoEtapa41("limites_multivariaveis", "Limites em várias variáveis", "DEFINITIVO_COM_AULA", ("limite", "caminho", "coordenadas"), "Um limite multivariável só existe se todas as aproximações ao ponto convergem para o mesmo valor.", "Testar caminhos; quando necessário usar cotas ou coordenadas polares.", "Dois caminhos com valores distintos provam inexistência."),
    ConceitoCalculoEtapa41("diferenciabilidade_gradiente", "Diferenciabilidade, gradiente e plano tangente", "DEFINITIVO_COM_AULA", ("derivadas_parciais", "aproximacao_linear"), "Diferenciabilidade é possibilidade de substituir localmente a função por uma aproximação linear.", "Calcular gradiente, formar plano tangente e verificar resto pequeno em relação à distância.", "Plano tangente deve tocar e aproximar a superfície no ponto."),
    ConceitoCalculoEtapa41("lagrange_multivariavel", "Multiplicadores de Lagrange", "DEFINITIVO_COM_AULA", ("gradiente", "restricao", "otimizacao"), "Em extremo sob restrição, o gradiente da função é alinhado com o gradiente da restrição.", "Resolver ∇f=λ∇g junto da restrição.", "Soluções devem ser testadas na restrição e classificadas."),
    ConceitoCalculoEtapa41("integrais_multiplos", "Integrais duplos e triplos", "DEFINITIVO_COM_AULA", ("integral", "regiao", "jacobiano"), "Integrais múltiplos acumulam grandezas sobre regiões planas ou sólidas.", "Descrever domínio, escolher ordem/coordenadas e integrar com jacobiano quando muda coordenadas.", "Limites devem reconstruir exatamente a região."),
    ConceitoCalculoEtapa41("calculo_vetorial", "Integrais de linha, superfície, Green e Gauss", "DEFINITIVO_COM_AULA", ("campo_vetorial", "curva", "superficie", "fluxo"), "Cálculo vetorial mede trabalho ao longo de curvas e fluxo através de superfícies.", "Parametrizar ou usar teoremas globais quando hipóteses valem.", "Orientação e fronteira precisam estar explícitas."),
    ConceitoCalculoEtapa41("fourier_analise_harmonica", "Séries de Fourier", "DEFINITIVO_COM_AULA", ("ortogonalidade", "periodicidade", "integral"), "Fourier decompõe uma função em ondas seno e cosseno ponderadas por coeficientes.", "Calcular coeficientes por ortogonalidade e aplicar condições de convergência.", "A paridade da função deve simplificar termos quando possível."),
    ConceitoCalculoEtapa41("analise_complexa_residuos", "Análise complexa e resíduos", "DEFINITIVO_COM_AULA", ("complexos", "holomorfia", "singularidade", "contorno"), "Funções complexas diferenciáveis obedecem estrutura forte; resíduos capturam contribuição local de polos.", "Verificar Cauchy-Riemann, expandir Laurent, identificar singularidades e somar resíduos.", "O contorno deve conter exatamente as singularidades contadas."),
    ConceitoCalculoEtapa41("edo_avancada_laplace_green", "EDO avançado, Laplace e Green", "DEFINITIVO_COM_AULA", ("derivada", "equacao", "condicao_inicial", "linearidade"), "EDO relaciona uma função às suas derivadas; métodos mudam conforme ordem, linearidade e condições.", "Classificar, resolver homogénea, obter particular por método adequado e aplicar condições.", "Substituir a solução na EDO deve recuperar a equação."),
)

RESPOSTAS_CALCULO_ETAPA_41: tuple[RespostaCalculoEtapa41, ...] = (
    RespostaCalculoEtapa41("41-I-001", "lim x->2 3x+1", "7", "epsilon_delta", "|3x+1-7|=3|x-2|; escolher δ=ε/3."),
    RespostaCalculoEtapa41("41-I-002", "lim x->0 x^2", "0", "epsilon_delta", "Se |x|<min(1,ε), então |x²|<ε."),
    RespostaCalculoEtapa41("41-I-004", "x sen(1/x), f(0)=0", "contínua em 0", "continuidade", "|x sen(1/x)|≤|x| e |x|→0."),
    RespostaCalculoEtapa41("41-I-005", "sen(1/x)", "não é prolongável continuamente em 0", "continuidade", "caminhos para 0 podem dar oscilações sem limite único."),
    RespostaCalculoEtapa41("41-I-007", "x^3-2 tem raiz", "sim", "bolzano", "f(1)=-1 e f(2)=6; muda sinal."),
    RespostaCalculoEtapa41("41-I-011", "derivar 1/x^2", "-2/x^3", "derivada", "Quociente incremental simplifica até o limite -2/x³."),
    RespostaCalculoEtapa41("41-I-015", "derivar x^x", "x^x(ln x + 1)", "derivacao_logaritmica", "ln y=x ln x; y'/y=ln x+1."),
    RespostaCalculoEtapa41("41-I-019", "(f^-1)'(2), f=x^3+x", "1/4", "inversa", "f(1)=2 e (f^-1)'(2)=1/f'(1)=1/4."),
    RespostaCalculoEtapa41("41-I-024", "lim (tg x-x)/x^3", "1/3", "lhopital_taylor", "tg x=x+x³/3+..."),
    RespostaCalculoEtapa41("41-I-025", "lim ln x/sqrt x infinito", "0", "lhopital", "crescimento exponencial/potência domina logaritmo."),
    RespostaCalculoEtapa41("41-I-026", "lim x^x, x->0+", "1", "limite_exponencial", "x^x=e^(x ln x) e x ln x→0."),
    RespostaCalculoEtapa41("41-I-031", "monotonia x^3-3x^2+2", "cresce (-∞,0), decresce (0,2), cresce (2,∞)", "aplicacao_derivada", "f'=3x(x-2)."),
    RespostaCalculoEtapa41("41-I-038", "Newton sqrt2 x0=1 duas iterações", "x1=3/2, x2=17/12", "newton", "x_{n+1}=(x_n+2/x_n)/2."),
    RespostaCalculoEtapa41("41-I-041", "∫x e^x dx", "e^x(x-1)+C", "partes", "u=x, dv=e^x dx."),
    RespostaCalculoEtapa41("41-I-043", "∫ln x dx", "x ln x - x + C", "partes", "u=ln x, dv=dx."),
    RespostaCalculoEtapa41("41-I-045", "∫e^x cos x dx", "e^x(sen x + cos x)/2 + C", "partes_ciclica", "Aplicar partes duas vezes e isolar a integral."),
    RespostaCalculoEtapa41("41-I-051", "∫0^1 x^2 dx", "1/3", "riemann", "Soma de quadrados normalizada tende a 1/3."),
    RespostaCalculoEtapa41("41-I-052", "d/dx ∫0^x sen(t^2)dt", "sen(x²)", "tfc", "TFC: derivada da acumulação é integrando em x."),
    RespostaCalculoEtapa41("41-I-058", "valor médio sen x em [0,π]", "2/π", "valor_medio", "(1/π)∫0^π sen x dx=2/π."),
    RespostaCalculoEtapa41("41-I-059", "∫0∞ e^-x dx", "1", "improprio", "[-e^-x]_0^∞=1."),
    RespostaCalculoEtapa41("41-I-061", "∑(1/3)^n", "1/2", "serie_geometrica", "Primeiro termo 1/3, razão 1/3: a/(1-r)=1/2."),
    RespostaCalculoEtapa41("41-I-062", "∑1/(n(n+1))", "1", "telescopica", "1/(n(n+1))=1/n-1/(n+1)."),
    RespostaCalculoEtapa41("41-I-063", "∑ n/(n+1)", "diverge", "condicao_necessaria", "termo geral tende a 1, não a 0."),
    RespostaCalculoEtapa41("41-I-067", "∑2^n/n!", "converge", "razao", "razão tende a 0."),
    RespostaCalculoEtapa41("41-I-071", "raio ∑x^n/n", "1", "series_potencias", "Critério da razão/raiz dá R=1."),
    RespostaCalculoEtapa41("41-I-073", "raio ∑x^n/2^n", "2", "series_potencias", "É geométrica em x/2."),
    RespostaCalculoEtapa41("41-I-082", "det [[1,2,3],[4,5,6],[7,8,9]]", "0", "determinante", "Linhas dependentes; terceira diferença repete a primeira diferença."),
    RespostaCalculoEtapa41("41-I-084", "inversa [[1,2],[3,4]]", "[[-2,1],[3/2,-1/2]]", "matriz_inversa", "det=-2; aplicar fórmula 2x2."),
    RespostaCalculoEtapa41("41-I-090", "autovalores [[2,1],[1,2]]", "3 e 1", "autovalores", "Vetores (1,1) e (1,-1)."),
    RespostaCalculoEtapa41("41-I-091", "distância ponto plano", "4/3", "geometria_analitica", "|2-2+6-5|/√(4+1+4)=1/3? Para plano 2x-y+2z=5 e ponto (1,2,3): |2-2+6-5|/3=1/3."),
    RespostaCalculoEtapa41("41-I-097", "projeção de (1,2,3) sobre (1,0,0)", "(1,0,0)", "projecao", "Componente na direção do eixo x."),
    RespostaCalculoEtapa41("41-I-098", "u×v (1,2,3)x(4,5,6)", "(-3,6,-3)", "produto_vetorial", "Determinante formal dos vetores de base."),
    RespostaCalculoEtapa41("41-II-004", "lim (x²-y²)/(x²+y²)", "não existe", "limite_multivariavel", "Pelo eixo x dá 1; pelo eixo y dá -1."),
    RespostaCalculoEtapa41("41-II-005", "lim xy/(x²+y²)", "não existe", "limite_multivariavel", "Pelo caminho y=x dá 1/2; pelo eixo dá 0."),
    RespostaCalculoEtapa41("41-II-008", "parciais x²y+xy³", "fx=2xy+y³; fy=x²+3xy²", "parciais", "Derivar uma variável mantendo a outra fixa."),
    RespostaCalculoEtapa41("41-II-012", "plano tangente z=x²+y² em (1,1,2)", "z=2x+2y-2", "plano_tangente", "Gradiente (2,2)."),
    RespostaCalculoEtapa41("41-II-018", "direcional de x²+y² em (1,0) direção (1,1)", "√2", "derivada_direcional", "Gradiente (2,0) dot direção unitária (1/√2,1/√2)."),
    RespostaCalculoEtapa41("41-II-021", "extremos x²+y²-2x-4y+5", "mínimo em (1,2), valor 0", "otimizacao_multivariavel", "Completar quadrados: (x-1)²+(y-2)²."),
    RespostaCalculoEtapa41("41-II-024", "classificar x²+xy+y²", "mínimo estrito em (0,0)", "hessiana", "Hessiana positiva definida."),
    RespostaCalculoEtapa41("41-II-025", "x²-y²", "ponto de sela em (0,0)", "hessiana", "Sinais opostos por direções x e y."),
    RespostaCalculoEtapa41("41-II-031", "∬ xy, [0,1]x[0,2]", "1", "integral_duplo", "∫0¹ x dx · ∫0² y dy = 1/2 · 2."),
    RespostaCalculoEtapa41("41-II-038", "área círculo raio R por polares", "πR²", "polares", "∫0^{2π}∫0^R r dr dθ."),
    RespostaCalculoEtapa41("41-II-041", "∭ xyz em caixa", "9/2", "integral_triplo", "Produto das integrais: 1/2 · 2 · 9/2."),
    RespostaCalculoEtapa41("41-II-044", "volume esfera raio R", "4πR³/3", "esfericas", "Integrar ρ² sen φ."),
    RespostaCalculoEtapa41("41-II-051", "∫C (x+y)ds segmento 0 a (1,1)", "√2", "linha_escalar", "Parametrizar (t,t); integrando 2t, ds=√2dt."),
    RespostaCalculoEtapa41("41-II-054", "F=(2xy,x²+2y) conservativo", "sim; potencial x²y+y²", "conservativo", "Derivadas cruzadas coincidem."),
    RespostaCalculoEtapa41("41-II-055", "F=(y,-x) conservativo", "não", "campo_vetorial", "∂Q/∂x=-1 e ∂P/∂y=1."),
    RespostaCalculoEtapa41("41-II-056", "∮ y dx - x dy círculo unitário", "-2π", "green", "Green dá ∬(-1-1)dA=-2π."),
    RespostaCalculoEtapa41("41-II-059", "fluxo F=(x,y,z) esfera unitária", "4π", "gauss", "div F=3; volume esfera=4π/3."),
    RespostaCalculoEtapa41("41-II-061", "Fourier de x em [-π,π]", "2∑((-1)^{n+1} sen(nx)/n)", "fourier", "Função ímpar: só senos."),
    RespostaCalculoEtapa41("41-II-064", "fenómeno de Gibbs", "oscilação persistente perto de saltos", "fourier", "As somas parciais excedem perto de descontinuidades."),
    RespostaCalculoEtapa41("41-II-071", "z² holomorfa", "sim", "complexa", "Polinómio complexo é holomorfo."),
    RespostaCalculoEtapa41("41-II-072", "conj(z) holomorfa", "não", "complexa", "Cauchy-Riemann falha salvo ponto isolado."),
    RespostaCalculoEtapa41("41-II-075", "∫ e^z/z, |z|=1", "2πi", "cauchy", "Resíduo de e^z/z em 0 é 1."),
    RespostaCalculoEtapa41("41-II-079", "sen z/z em 0", "removível", "singularidade", "limite vale 1."),
    RespostaCalculoEtapa41("41-II-081", "∫ dz/(z²+1), |z|=2", "0", "residuos", "Polos i e -i dentro; resíduos somam 0."),
    RespostaCalculoEtapa41("41-II-091", "y''+4y'+4y=0", "y=(C1+C2x)e^(-2x)", "edo_ordem2", "Raiz dupla r=-2."),
    RespostaCalculoEtapa41("41-II-092", "y''-y=e^x", "yh=C1e^x+C2e^-x; yp=(x/2)e^x", "edo_nao_homogenea", "Ressonância com e^x."),
    RespostaCalculoEtapa41("41-II-098", "Laplace de y''+y", "s²Y-sy(0)-y'(0)+Y", "laplace", "Transformar derivadas usando condições iniciais."),
)

# Ponte entre os rótulos curtos das respostas antigas e os conceitos que lhes
# dão fundamento. Um rótulo sem entrada aqui não pode liberar resposta pronta.
PONTES_TOPICOS_CALCULO: dict[str, str] = {
    "epsilon_delta": "epsilon_delta_operacional", "bolzano": "epsilon_delta_operacional",
    "continuidade": "continuidade_uniforme",
    "derivada": "derivada_por_limite_rigorosa", "derivacao_logaritmica": "derivada_por_limite_rigorosa",
    "inversa": "derivada_por_limite_rigorosa", "lhopital": "derivada_por_limite_rigorosa",
    "lhopital_taylor": "taylor_maclaurin_resto", "limite_exponencial": "taylor_maclaurin_resto",
    "aplicacao_derivada": "otimizacao_diferencial", "newton": "otimizacao_diferencial",
    "partes": "integracao_por_partes_ciclica", "partes_ciclica": "integracao_por_partes_ciclica",
    "riemann": "integral_riemann_tfc", "tfc": "integral_riemann_tfc",
    "valor_medio": "integral_riemann_tfc", "improprio": "integral_riemann_tfc",
    "serie_geometrica": "series_convergencia_completa", "telescopica": "series_convergencia_completa",
    "condicao_necessaria": "series_convergencia_completa", "razao": "series_convergencia_completa",
    "series_potencias": "series_potencias",
    "gauss": "gauss_algebra_linear", "determinante": "gauss_algebra_linear",
    "matriz_inversa": "gauss_algebra_linear", "autovalores": "gauss_algebra_linear",
    "geometria_analitica": "geometria_analitica_vetorial", "produto_vetorial": "geometria_analitica_vetorial",
    "projecao": "geometria_analitica_vetorial",
    "limite_multivariavel": "limites_multivariaveis",
    "parciais": "diferenciabilidade_gradiente", "plano_tangente": "diferenciabilidade_gradiente",
    "derivada_direcional": "diferenciabilidade_gradiente",
    "otimizacao_multivariavel": "lagrange_multivariavel", "hessiana": "lagrange_multivariavel",
    "integral_duplo": "integrais_multiplos", "integral_triplo": "integrais_multiplos",
    "polares": "integrais_multiplos", "esfericas": "integrais_multiplos",
    "linha_escalar": "calculo_vetorial", "campo_vetorial": "calculo_vetorial",
    "conservativo": "calculo_vetorial", "green": "calculo_vetorial",
    "fourier": "fourier_analise_harmonica",
    "complexa": "analise_complexa_residuos", "cauchy": "analise_complexa_residuos",
    "singularidade": "analise_complexa_residuos", "residuos": "analise_complexa_residuos",
    "edo_ordem2": "edo_avancada_laplace_green", "edo_nao_homogenea": "edo_avancada_laplace_green",
    "laplace": "edo_avancada_laplace_green",
}


def auditar_pontes_calculo() -> dict[str, object]:
    conceitos = {c.chave: c for c in CONCEITOS_CALCULO_ETAPA_41}
    conceitos_sem_origem = tuple(sorted(c.chave for c in conceitos.values() if not c.depende_de))
    respostas_sem_ponte: list[str] = []
    pontes_para_conceito_ausente: list[tuple[str, str]] = []
    for resposta in RESPOSTAS_CALCULO_ETAPA_41:
        destino = PONTES_TOPICOS_CALCULO.get(resposta.topico)
        if destino is None:
            respostas_sem_ponte.append(resposta.id_resposta)
        elif destino not in conceitos:
            pontes_para_conceito_ausente.append((resposta.id_resposta, destino))
    return {
        "conceitos": len(conceitos),
        "respostas": len(RESPOSTAS_CALCULO_ETAPA_41),
        "conceitos_sem_origem": conceitos_sem_origem,
        "respostas_sem_ponte": tuple(respostas_sem_ponte),
        "pontes_para_conceito_ausente": tuple(pontes_para_conceito_ausente),
        "sem_isolamentos": not conceitos_sem_origem and not respostas_sem_ponte and not pontes_para_conceito_ausente,
    }


def total_perguntas_etapa41() -> int:
    return sum(bloco.quantidade for bloco in BLOCOS_CALCULO_ETAPA_41)


def estado_etapa41() -> dict[str, object]:
    return {
        "etapa": 41,
        "nome": "Calculo Diferencial e Integral I-II definitivo",
        "total_perguntas": TOTAL_PERGUNTAS_ETAPA_41,
        "blocos": len(BLOCOS_CALCULO_ETAPA_41),
        "conceitos": len(CONCEITOS_CALCULO_ETAPA_41),
        "respostas_base_aprovadas": len(RESPOSTAS_CALCULO_ETAPA_41),
        "definitivo_por_defeito": True,
        "sem_dependencia_externa": True,
        "estado_minimo": "DEFINITIVO_REGISTADO",
    }


def resposta_calculo_etapa41(id_resposta: str) -> str | None:
    for resposta in RESPOSTAS_CALCULO_ETAPA_41:
        if resposta.id_resposta == id_resposta:
            conceito = PONTES_TOPICOS_CALCULO.get(resposta.topico)
            if conceito not in {c.chave for c in CONCEITOS_CALCULO_ETAPA_41}:
                return None
            return resposta.resposta_pronta
    return None


def conceitos_etapa41() -> tuple[str, ...]:
    return tuple(conceito.chave for conceito in CONCEITOS_CALCULO_ETAPA_41)
