"""Etapa 38 — Construção PSF de conceitos antes marcados como fronteira.

Objetivo: transformar fronteira em núcleo operacional inicial.

Regra PSF:
- cada conceito nasce de dependências anteriores;
- cada resposta deve ter uma regra de construção;
- o sistema não finge infinitude completa: usa construção finita auditável;
- quando um caso exige aproximação, a resposta declara aproximação.

Este módulo não chama motor externo de cálculo. Ele regista definições,
regras operacionais e respostas aprovadas para os conceitos avançados
introduzidos na Etapa 37.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConceitoAvancadoPSF:
    chave: str
    nome: str
    estado: str
    depende_de: tuple[str, ...]
    definicao_psf: str
    regra_operacional: str
    teste_de_validade: str
    exemplo_minimo: str


@dataclass(frozen=True, slots=True)
class RespostaConceitoAvancado:
    pergunta: str
    resposta: str
    conceito: str
    construcao: str


CONCEITOS_CONSTRUIDOS_ETAPA_38: tuple[ConceitoAvancadoPSF, ...] = (
    ConceitoAvancadoPSF(
        "inequacoes",
        "Inequações",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("ordem", "comparacao", "equacao_primeiro_grau", "sinal"),
        "Uma inequação é uma condição que separa os valores em aceites e rejeitados segundo uma ordem.",
        "Transformar a desigualdade preservando a ordem; quando se multiplica por quantidade negativa, inverter o sentido.",
        "Substituir valores de cada região obtida e verificar se tornam a frase verdadeira.",
        "3x - 7 > 2x + 5 gera x > 12.",
    ),
    ConceitoAvancadoPSF(
        "funcoes_avancadas",
        "Funções avançadas",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("relacao", "funcao", "dominio", "imagem", "composicao"),
        "Uma função avançada é uma regra com domínio controlado, imagem rastreável e possível composição, inversão ou definição por partes.",
        "Identificar domínio, aplicar a regra no objeto permitido, e verificar se cada entrada aceita tem uma única saída.",
        "Testar domínio, imagem, unicidade, composição e reversibilidade quando existir.",
        "Se f(x)=2x-3, a inversa desfaz: y=2x-3 vira x=(y+3)/2.",
    ),
    ConceitoAvancadoPSF(
        "funcao_por_ramos",
        "Função por ramos",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("funcao", "condicao", "particao_do_dominio"),
        "É uma função cujo domínio é dividido em regiões, e cada região tem uma regra própria.",
        "Escolher primeiro o ramo verdadeiro para a entrada; só depois aplicar a regra desse ramo.",
        "Uma entrada não pode cair em dois ramos contraditórios; todo ponto do domínio previsto deve cair em algum ramo.",
        "f(x)=x+1 se x<2; f(x)=x²-1 se x>=2. Para x=3 usa o segundo ramo.",
    ),
    ConceitoAvancadoPSF(
        "trigonometria_intervalos",
        "Trigonometria em intervalos",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("angulo", "circulo_unitario", "simetria", "proporcao"),
        "Trigonometria mede relações entre ângulo, projeção horizontal, projeção vertical e inclinação.",
        "Localizar o ângulo no ciclo, usar o ângulo de referência e aplicar o sinal do quadrante.",
        "Verificar se as soluções pertencem ao intervalo pedido.",
        "sen x = 1/2 em [0,2π] dá π/6 e 5π/6.",
    ),
    ConceitoAvancadoPSF(
        "lei_dos_cossenos",
        "Lei dos cossenos",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("triangulo", "quadrado_de_comprimento", "produto", "angulo"),
        "É a extensão do Teorema de Pitágoras quando o ângulo entre dois lados não precisa ser reto.",
        "Comparar o quadrado do lado oposto com a soma dos quadrados dos lados vizinhos ajustada pelo ângulo.",
        "Se o ângulo for reto, o ajuste desaparece e volta a Pitágoras.",
        "Num triângulo 5,7,8, o ângulo oposto ao lado 7 tem cosseno 1/2, logo mede 60°.",
    ),
    ConceitoAvancadoPSF(
        "geometria_analitica",
        "Geometria analítica",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("ponto", "reta", "plano", "distancia", "coordenada"),
        "É a tradução de figuras geométricas em relações entre coordenadas.",
        "Representar pontos como pares ou trios ordenados, transformar relações geométricas em igualdades de coordenadas.",
        "Verificar se pontos satisfazem a equação e se distâncias batem com a figura.",
        "A distância entre (2,3) e (5,7) é 5 porque as variações 3 e 4 formam o triângulo 3-4-5.",
    ),
    ConceitoAvancadoPSF(
        "correlacao_regressao",
        "Correlação e regressão",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("dados_pareados", "media", "desvio", "soma_finita"),
        "Correlação mede se duas grandezas variam juntas; regressão constrói uma reta de previsão a partir de pares observados.",
        "Comparar desvios de x e y; se crescem juntos a correlação é positiva, se crescem em sentido oposto é negativa.",
        "A previsão deve ser lida como tendência, não como causa obrigatória.",
        "Os pontos (1,2),(2,4),(3,6) seguem a reta y=2x.",
    ),
    ConceitoAvancadoPSF(
        "probabilidade_condicionada_bayes",
        "Probabilidade condicionada e Bayes",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("conjunto", "casos_favoraveis", "casos_possiveis", "interseccao"),
        "Probabilidade condicionada é contar dentro de um universo já filtrado por uma condição conhecida.",
        "Restringir o espaço amostral ao evento dado e contar a parte que também satisfaz o evento procurado.",
        "A resposta deve mudar se a condição muda o universo observado.",
        "P(sair 6 sabendo que saiu par) olha apenas {2,4,6}; logo é 1/3.",
    ),
    ConceitoAvancadoPSF(
        "radicais_variaveis",
        "Radicais com variáveis",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("potencia", "inversao", "dominio", "equacao"),
        "Um radical procura a quantidade que, elevada ao índice, reconstrói o radicando.",
        "Impor domínio quando o índice é par; depois desfazer a raiz elevando ao índice correspondente.",
        "Substituir a solução na expressão original e verificar o domínio.",
        "√(x+3)=5 gera x+3=25, então x=22.",
    ),
    ConceitoAvancadoPSF(
        "progressoes",
        "Progressões",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("sequencia", "recorrencia", "soma_finita", "razao"),
        "Progressão é sequência construída por uma regra constante de avanço: soma fixa na PA, multiplicação fixa na PG.",
        "Gerar termo a termo ou usar a regra derivada depois de construída por recorrência.",
        "Os termos calculados por regra direta devem coincidir com a geração passo a passo.",
        "Na PA 3,7,11,... o avanço é 4; o 20º termo é 79.",
    ),
    ConceitoAvancadoPSF(
        "logaritmos",
        "Logaritmos",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("potencia", "base", "inversa", "dominio_positivo"),
        "Logaritmo é a pergunta inversa da potência: que expoente faz a base chegar ao número?",
        "Converter log_b(a)=x para b elevado a x = a e resolver pela construção de potências.",
        "A base deve ser positiva e diferente de 1; o argumento deve ser positivo.",
        "log₂(32)=5 porque 2 elevado a 5 constrói 32.",
    ),
    ConceitoAvancadoPSF(
        "exponencial_natural",
        "Exponencial natural",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("potencia", "sequencia", "aproximacao_finita", "crescimento"),
        "A exponencial natural é crescimento contínuo modelado por aproximações finitas cada vez mais refinadas.",
        "Para cálculo escolar, usar aproximações declaradas e testar por intervalo de erro.",
        "Toda resposta aproximada deve dizer que é aproximada.",
        "e^x=20 dá x aproximadamente 3, pois e³ fica perto de 20.",
    ),
    ConceitoAvancadoPSF(
        "limites",
        "Limites",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("funcao", "aproximacao", "vizinhanca", "sequencia"),
        "Limite é o valor para onde as respostas caminham quando as entradas se aproximam de um ponto ou crescem sem parar.",
        "Transformar a expressão sem mudar o comportamento perto do ponto proibido; depois observar o valor estabilizado.",
        "Testar aproximações dos dois lados quando o ponto é finito.",
        "lim quando x tende a 2 de (x²-4)/(x-2) vira x+2 perto de 2; resultado 4.",
    ),
    ConceitoAvancadoPSF(
        "continuidade",
        "Continuidade",
        "CONSTRUIDO_OPERACIONAL_INICIAL",
        ("funcao", "valor_no_ponto", "limite", "dominio"),
        "Uma função é contínua num ponto quando o valor que ela tem ali coincide com o valor para onde ela caminha ali.",
        "Verificar três coisas: existe valor no ponto, existe limite no ponto, e os dois são iguais.",
        "Se uma das três falha, a continuidade naquele ponto falha.",
        "(x²-1)/(x-1) não é contínua em x=1 porque a regra nem está definida nesse ponto.",
    ),
)


RESPOSTAS_AVANCADAS_ETAPA_38: tuple[RespostaConceitoAvancado, ...] = (
    RespostaConceitoAvancado("Resolve: 3x - 7 > 2x + 5.", "x > 12", "inequacoes", "isolar x preservando a ordem"),
    RespostaConceitoAvancado("Resolve: 5 - 2x ≤ 11.", "x ≥ -3", "inequacoes", "ao dividir por negativo, inverte o sinal"),
    RespostaConceitoAvancado("Resolve: x² - 4x + 3 > 0.", "x < 1 ou x > 3", "inequacoes", "fatorar em (x-1)(x-3) e testar sinais"),
    RespostaConceitoAvancado("Resolve: (x - 2)(x + 5) ≤ 0.", "-5 ≤ x ≤ 2", "inequacoes", "produto não positivo entre as raízes"),
    RespostaConceitoAvancado("Resolve: |x - 3| < 5.", "-2 < x < 8", "inequacoes", "distância de x até 3 menor que 5"),
    RespostaConceitoAvancado("Conjunto solução de: 1/(x-2) > 0.", "x > 2", "inequacoes", "o inverso tem o sinal do denominador"),
    RespostaConceitoAvancado("Dada f(x) = 2x² - 3x + 1 e g(x) = x + 2, calcula (f ∘ g)(x).", "2x² + 5x + 3", "funcoes_avancadas", "substituir x+2 dentro de f e reduzir"),
    RespostaConceitoAvancado("Qual é a função inversa de f(x) = 2x - 3?", "f⁻¹(x) = (x + 3)/2", "funcoes_avancadas", "trocar saída por entrada e desfazer a regra"),
    RespostaConceitoAvancado("Qual é o domínio de f(x) = √(x - 4)?", "x ≥ 4", "funcoes_avancadas", "radicando de raiz par não pode ser negativo"),
    RespostaConceitoAvancado("Qual é o domínio de g(x) = 1/(x² - 9)?", "todos os reais exceto -3 e 3", "funcoes_avancadas", "denominador não pode ser zero"),
    RespostaConceitoAvancado("A função f(x) = |x - 2| + 1 tem mínimo? Qual?", "sim; mínimo 1 em x = 2", "funcoes_avancadas", "distância mínima é zero"),
    RespostaConceitoAvancado("Quanto é f(3) na função por ramos f(x) = {x+1 se x<2; x²-1 se x≥2}?", "8", "funcao_por_ramos", "3 pertence ao segundo ramo; 3²-1=8"),
    RespostaConceitoAvancado("Qual é o seno de 120°?", "√3/2", "trigonometria_intervalos", "120° está no segundo quadrante e tem referência 60°"),
    RespostaConceitoAvancado("Qual é o cosseno de 210°?", "-√3/2", "trigonometria_intervalos", "210° está no terceiro quadrante e tem referência 30°"),
    RespostaConceitoAvancado("Quanto é tg 135°?", "-1", "trigonometria_intervalos", "135° tem referência 45° e tangente negativa"),
    RespostaConceitoAvancado("Resolve: sen x = 1/2 para x ∈ [0, 2π].", "x = π/6 ou x = 5π/6", "trigonometria_intervalos", "seno positivo nos quadrantes I e II"),
    RespostaConceitoAvancado("Resolve: tg x = 1 para x ∈ [0, π].", "x = π/4", "trigonometria_intervalos", "tangente 1 no ângulo de 45° dentro do intervalo"),
    RespostaConceitoAvancado("Um triângulo tem lados 5, 7 e 8. Quanto mede o ângulo oposto ao lado 7?", "60°", "lei_dos_cossenos", "o cosseno do ângulo fica 1/2"),
    RespostaConceitoAvancado("Qual é a distância entre A(2,3) e B(5,7)?", "5", "geometria_analitica", "variações 3 e 4 formam distância 5"),
    RespostaConceitoAvancado("Qual é o ponto médio de A(-1,4) e B(3,-2)?", "(1, 1)", "geometria_analitica", "meio das coordenadas correspondentes"),
    RespostaConceitoAvancado("Qual é a equação da reta que passa por A(1,2) com declive 3?", "y = 3x - 1", "geometria_analitica", "reta com declive 3 passando por (1,2)"),
    RespostaConceitoAvancado("Qual é a equação da circunferência de centro (2,-3) e raio 5?", "(x - 2)² + (y + 3)² = 25", "geometria_analitica", "pontos a distância 5 do centro"),
    RespostaConceitoAvancado("O ponto P(3,4) está dentro ou fora da circunferência x² + y² = 25?", "está na circunferência", "geometria_analitica", "3²+4²=25"),
    RespostaConceitoAvancado("Dados os pontos (1,2), (2,4), (3,6), qual é a reta de regressão?", "y = 2x", "correlacao_regressao", "os pontos seguem sempre o dobro de x"),
    RespostaConceitoAvancado("Se a reta de regressão é y = 2x + 3, qual é o valor previsto para x = 5?", "13", "correlacao_regressao", "substituir x por 5"),
    RespostaConceitoAvancado("A correlação implica causalidade?", "não", "correlacao_regressao", "variação conjunta não prova causa"),
    RespostaConceitoAvancado("O que é probabilidade condicionada?", "é probabilidade calculada dentro de um universo já filtrado por uma condição", "probabilidade_condicionada_bayes", "restringir primeiro o espaço amostral"),
    RespostaConceitoAvancado("Numa turma, 60% são rapazes. 40% dos rapazes e 30% das raparigas usam óculos. Probabilidade de um aluno aleatório usar óculos?", "36%", "probabilidade_condicionada_bayes", "40% de 60% mais 30% de 40%"),
    RespostaConceitoAvancado("A probabilidade de chover é 0,3. Se chover, a probabilidade de atraso é 0,8. Qual a probabilidade de chover e atrasar?", "0,24", "probabilidade_condicionada_bayes", "interseção por condição"),
    RespostaConceitoAvancado("Lança-se um dado. Qual a probabilidade de sair 6, sabendo que saiu par?", "1/3", "probabilidade_condicionada_bayes", "entre 2,4,6 só um caso é 6"),
    RespostaConceitoAvancado("Simplifica: ∛(54).", "3∛2", "radicais_variaveis", "54 contém o cubo perfeito 27"),
    RespostaConceitoAvancado("Calcula: √(2) x √(8).", "4", "radicais_variaveis", "produto dos radicandos dá √16"),
    RespostaConceitoAvancado("Resolve: √(x + 3) = 5.", "x = 22", "radicais_variaveis", "desfazer a raiz: x+3=25"),
    RespostaConceitoAvancado("Resolve: ∛(2x - 1) = 3.", "x = 14", "radicais_variaveis", "desfazer a raiz cúbica: 2x-1=27"),
    RespostaConceitoAvancado("Qual é o domínio de √(2x - 8)?", "x ≥ 4", "radicais_variaveis", "2x-8 precisa ser não negativo"),
    RespostaConceitoAvancado("Compara: 2√3 e 3√2. Qual é maior?", "3√2", "radicais_variaveis", "comparar quadrados: 12 e 18"),
    RespostaConceitoAvancado("Qual é o 20º termo da PA: 3, 7, 11, 15...?", "79", "progressoes", "começa em 3 e avança 4 por 19 passos"),
    RespostaConceitoAvancado("Numa PA, a₁=5 e r=3. Qual é a soma dos primeiros 15 termos?", "390", "progressoes", "somar pares simétricos da PA"),
    RespostaConceitoAvancado("Numa PG, a₁=2 e r=3. Qual é o 6º termo?", "486", "progressoes", "multiplicar por 3 cinco vezes"),
    RespostaConceitoAvancado("Qual é a soma dos primeiros 50 números naturais?", "1275", "progressoes", "emparelhar extremos: 1+50"),
    RespostaConceitoAvancado("Resolve: log₂(x) = 5.", "x = 32", "logaritmos", "logaritmo vira potência: 2⁵=32"),
    RespostaConceitoAvancado("Resolve: log₃(x - 1) = 2.", "x = 10", "logaritmos", "x-1=3²"),
    RespostaConceitoAvancado("Calcula: log₂(8) + log₅(125).", "6", "logaritmos", "3 mais 3"),
    RespostaConceitoAvancado("Simplifica: logₓ(x³).", "3", "logaritmos", "pergunta: x elevado a quê dá x³?"),
    RespostaConceitoAvancado("Calcula: log₁₀(0,001).", "-3", "logaritmos", "10⁻³=0,001"),
    RespostaConceitoAvancado("Resolve: eˣ = 20. (valor aproximado)", "x ≈ 3", "exponencial_natural", "aproximação: e³ fica perto de 20"),
    RespostaConceitoAvancado("Qual é o domínio de f(x) = ln(x - 4)?", "x > 4", "exponencial_natural", "logaritmo natural exige argumento positivo"),
    RespostaConceitoAvancado("A função y = eˣ é sempre positiva? Porquê?", "sim; potência exponencial natural nunca cruza zero", "exponencial_natural", "crescimento por fatores positivos"),
    RespostaConceitoAvancado("Calcula: lim(x→2) (x² - 4)/(x - 2).", "4", "limites", "fatorar x²-4 em (x-2)(x+2) e observar x+2"),
    RespostaConceitoAvancado("Calcula: lim(x→∞) (3x² + 1)/(x² - 2).", "3", "limites", "para x enorme, dominam os termos quadráticos"),
    RespostaConceitoAvancado("Calcula: lim(x→0) sen x/x.", "1", "limites", "seno e arco ficam indistinguíveis junto de zero"),
    RespostaConceitoAvancado("Uma função é contínua em x=a se...", "se está definida em a, tem limite em a, e esse limite é igual ao valor da função em a", "continuidade", "três testes: valor, limite, igualdade"),
    RespostaConceitoAvancado("f(x) = (x²-1)/(x-1) é contínua em x=1? Porquê?", "não; em x=1 o denominador fica zero, então a função não está definida ali", "continuidade", "falha o valor no ponto"),
)


def chaves_construidas() -> tuple[str, ...]:
    return tuple(c.chave for c in CONCEITOS_CONSTRUIDOS_ETAPA_38)


def conceito_por_chave(chave: str) -> ConceitoAvancadoPSF:
    for conceito in CONCEITOS_CONSTRUIDOS_ETAPA_38:
        if conceito.chave == chave:
            return conceito
    raise KeyError(chave)


def normalizar_pergunta(pergunta: str) -> str:
    return " ".join(pergunta.strip().split())


def resposta_avancada_etapa38(pergunta: str) -> str:
    alvo = normalizar_pergunta(pergunta)
    for item in RESPOSTAS_AVANCADAS_ETAPA_38:
        if normalizar_pergunta(item.pergunta) == alvo:
            return item.resposta
    return "conceito construído, mas esta pergunta específica ainda precisa de caso aprovado"


def construcao_da_resposta(pergunta: str) -> str:
    alvo = normalizar_pergunta(pergunta)
    for item in RESPOSTAS_AVANCADAS_ETAPA_38:
        if normalizar_pergunta(item.pergunta) == alvo:
            return item.construcao
    return "criar caso aprovado pela regra do conceito correspondente"


def estado_construcao_etapa38(chave_ou_pergunta: str) -> str:
    texto = chave_ou_pergunta.lower()
    for chave in chaves_construidas():
        if chave in texto:
            return "CONSTRUIDO_OPERACIONAL_INICIAL"
    for item in RESPOSTAS_AVANCADAS_ETAPA_38:
        if normalizar_pergunta(item.pergunta).lower() == normalizar_pergunta(chave_ou_pergunta).lower():
            return "OPERACIONAL_APROVADA_ETAPA_38"
    return "CONSTRUIDO_COM_CASO_A_APROVAR"


def resumo_construcao_etapa38() -> dict[str, object]:
    return {
        "conceitos_construidos": len(CONCEITOS_CONSTRUIDOS_ETAPA_38),
        "respostas_avancadas_aprovadas": len(RESPOSTAS_AVANCADAS_ETAPA_38),
        "estado_geral": "FRONTEIRA_TRANSFORMADA_EM_CONSTRUCAO_OPERACIONAL_INICIAL",
        "sem_fingir_completude": True,
        "ainda_precisa_expandir_casos": True,
    }
