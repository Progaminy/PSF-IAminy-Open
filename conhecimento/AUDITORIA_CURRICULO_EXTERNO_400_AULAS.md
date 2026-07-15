# Auditoria de currículo externo — 1000 aulas

Cruzamento de uma lista externa de 1000 "aulas" (currículo do básico ao
avançado, fornecida pelo autor em dois lotes: 1-400 e 401-1000) contra
os 189 conceitos matemáticos reais do PSF-IAminy (auditados: construção
+ implementação + validação + ponte, 0 pendências nas três categorias em
2026-07). Isto não é conhecimento novo — é inventário de cobertura, para
orientar prioridade. O nome do arquivo preserva "400" por ser o nome
histórico já referenciado em README.md e PLANO_PSF_IAMINY.md.

Legenda: 🟢 TEM (construído, com prova, código e teste) · 🟡 PARCIAL
(existe pedaço, não o tópico inteiro) · 🔵 EM ABERTO (não construído).
Um item vira 🟢 e permanece na lista quando fecha — a marca antiga não é
apagada, só substituída, para preservar o histórico de cobertura.

## Aulas 1–10

| # | Tema | Status | Nota |
|---|---|---|---|
|1|Contar, ordem, comparar|🟢|base do núcleo inteiro|
|2|Adição|🟢||
|3|Subtração|🟢|ETAPA 5, diferença controlada|
|4|Multiplicação|🟢||
|5|Divisão|🟢|ETAPA 7-8, quociente e resto|
|6|Operações inversas|🟡|inversa relacional existe, "famílias de fatos" pedagógico não|
|7|Números grandes, QVL|🟡|posição/valor de lugar existe (ETAPA 134), não como QVL didático|
|8|Centenas|🟡|mesma base de 7|
|9|Contagem, saltos, padrões|🟢|ETAPA 48-49|
|10|Adição com reserva ("vai um")|🟢|ETAPA 1037|

## Aulas 11–20

| # | Tema | Status | Nota |
|---|---|---|---|
|11|Subtração com reserva|🟢|ETAPA 1037|
|12|Pares e ímpares|🟢|ETAPA 1049, paridade e paridade da soma conferidos contra o resto real|
|13|Multiplicação armada|🟢|ETAPA 1037|
|14|Frações|🟢|racionais exatos, base desde ETAPA 1034|
|15|Formas geométricas planas|🔵|geometria plana não construída|
|16|Perímetro|🔵|depende de 15|
|17|Área|🟡|retângulo e triângulo existem (ETAPA 1036/1038); círculo/polígono não|
|18|Medidas de comprimento (m,km,cm)|🟢|Comprimento como grandeza (1036) + conversão metro/centímetro (ETAPA 1054)|
|19|Medidas de massa|🟢|Massa como grandeza (1036) + conversão quilo/grama (ETAPA 1054)|
|20|Medidas de capacidade|🔵|não construído|

## Aulas 21–30

| # | Tema | Status | Nota |
|---|---|---|---|
|21|Medidas de tempo|🟡|Tempo como grandeza + conversão hora/minuto (ETAPA 1054); horas do relógio/calendário não|
|22|Números decimais|🟢|expansão decimal exata, transporte de resto|
|23|Porcentagem|🟢|ETAPA 1051, ponte e testes fechados (`nucleo/porcentagem.py`)|
|24|Potenciação|🟢|potência modular ETAPA 27|
|25|Raiz quadrada|🟢|ETAPA 1035 (aproxima) + ETAPA 1048 (exata quando é quadrado perfeito)|
|26|Expressões numéricas (PPMAS)|🟢|ETAPA 131-132|
|27|Equações do 1º grau|🟢|ETAPA 133|
|28|Critérios de divisibilidade|🟢|ETAPA 1053, critérios por 2,3,5,9,10 provados por construção, não decorados|
|29|Média aritmética|🟢|estatística finita, ETAPA 961-990|
|30|Regra de três simples|🟢|ETAPA 1052, direta e inversa, ligadas a proporção exata|

## Aulas 31–35

| # | Tema | Status | Nota |
|---|---|---|---|
|31|Geometria espacial (volume cubo/paralelepípedo)|🟢|`volume_paralelepipedo`, ETAPA 1036|
|32|Juros simples|🔵||
|33|Probabilidade|🟢|ETAPA 921-960|
|34|Números negativos|🟢|inteiros relativos, ETAPA 16|
|35|Ângulos (classificação)|🟡|ângulo existe dentro da trigonometria; classificação isolada não|

## Aulas 36–45

| # | Tema | Status | Nota |
|---|---|---|---|
|36|Razão e Proporção|🟢|ETAPA 1036|
|37|Teorema de Pitágoras|🟢|relação pitagórica, base de ETAPA 1033|
|38|Semelhança de Triângulos|🟢|usado em ETAPA 1033|
|39|Números Primos e Compostos|🟢|ETAPA 10|
|40|Decomposição em Fatores Primos|🟢|ETAPA 11, 13, 14|
|41|MMC|🟢|ETAPA 15|
|42|MDC|🟢|ETAPA 4, 15|
|43|Notação Científica|🟢|ETAPA 1055|
|44|Equações do 2º Grau|🟢|ETAPA 135 (busca) + ETAPA 1048 (fórmula exata)|
|45|Funções (domínio, imagem, f(x))|🟢|ETAPA 70-71, 1047|

## Aulas 46–55

| # | Tema | Status | Nota |
|---|---|---|---|
|46|Função Afim e Gráfico|🟡|f(x)=ax+b existe (1047); "gráfico" é visual, fora de escopo|
|47|Função Quadrática (parábola)|🟡|raízes exatas (1048) e inequações do 2º grau (1057) existem; parábola/vértice visual não|
|48|Juros Compostos|🔵||
|49|Regra de Três Composta|🔵||
|50|Princípio Fundamental da Contagem|🟢|ETAPA 36-38|
|51|Permutação Simples|🟢|ETAPA 41|
|52|Combinação Simples|🟢|ETAPA 43|
|53|Probabilidade Condicional|🟢|ETAPA 1043, inclui Bayes|
|54|Moda, Mediana, Média|🟢|ETAPA 961-990|
|55|Desvio Padrão e Variância|🟢|ETAPA 1050, desvio padrão exato quando a variância é quadrado perfeito|

## Aulas 56–65

| # | Tema | Status | Nota |
|---|---|---|---|
|56|Área/Circunferência do Círculo|🔵|precisa de π|
|57|Volume Cilindro/Cone|🔵||
|58|Volume da Esfera|🔵||
|59|Trigonometria no triângulo retângulo|🟢|ETAPA 1033|
|60|Tabela trigonométrica (30°,45°,60°)|🔵|valores exigem irracionais|
|61|Ciclo trigonométrico (radianos)|🔵|círculo unitário simbólico ainda não|
|62|Lei dos Senos|🟢|ETAPA 1038|
|63|Lei dos Cossenos|🟢|ETAPA 1038|
|64|Plano Cartesiano|🟢|ETAPA 1039|
|65|Distância entre dois pontos|🟢|ETAPA 1039 (extensão), `distancia_exata_ou_none` quando o quadrado é quadrado perfeito|

## Aulas 66–75

| # | Tema | Status | Nota |
|---|---|---|---|
|66|Ponto Médio/Baricentro|🟢|ETAPA 1039 (extensão), `ponto_medio`|
|67|Equação da Reta|🟢|ETAPA 1039|
|68|Equação da Circunferência|🟢|ETAPA 1039 (extensão), construção por centro+ponto e pertencimento|
|69|Logaritmos|🟡|caso exato (1045) + domínio de composição linear (ETAPA 1060); propriedades gerais e base `e` não|
|70|Equações Exponenciais|🟡|só o caso que cai em logaritmo exato|
|71|Progressão Aritmética|🟢|ETAPA 1040|
|72|Progressão Geométrica|🟢|ETAPA 1040|
|73|Matrizes|🟢|ETAPA 104, 106|
|74|Determinantes|🟢|ETAPA 107|
|75|Sistemas Lineares|🟢|ETAPA 108, 110|

## Aulas 76–85

| # | Tema | Status | Nota |
|---|---|---|---|
|76|Números Complexos|🔵||
|77|Polinômios|🟢|ETAPA 101-102|
|78|Divisão de Polinômios (Briot-Ruffini)|🟢|ETAPA 1056|
|79|Teorema do Resto|🟢|ETAPA 1056|
|80|Inequações do 1º Grau|🟢|ETAPA 1041|
|81|Inequações do 2º Grau|🟢|ETAPA 1057|
|82|Função Exponencial|🔵||
|83|Função Logarítmica|🟡|só pontos exatos e domínio (1045, 1060)|
|84|Limites|🟡|função racional em ponto finito (ETAPA 1058); caso geral ainda depende de reais completos clássicos|
|85|Derivadas|🔵||

## Aulas 86–95

| # | Tema | Status | Nota |
|---|---|---|---|
|86|Sistema Monetário|🔵|aplicação, não construção|
|87|Números Romanos|🔵||
|88|Sistema Binário|🟢|`binario.py`, ETAPA 134|
|89|Unidades de Superfície (hectare)|🔵||
|90|Escalas e Mapas|🟡|proporção existe, "escala" não nomeada|
|91|Gráficos e Tabelas|🔵|visual|
|92|Conjuntos Numéricos (N,Z,Q,I,R)|🟡|N, Z, Q construídos; R por leis geradoras com equivalência, operações, ordem e completude de Cauchy (ETAPA 1035, 1061-1064) — não é a completude Dedekind clássica; I não construído|
|93|Diagrama de Venn|🟡|operações de conjunto existem; diagrama é visual|
|94|Lógica Matemática|🟢|ETAPA 341-360|
|95|História da Matemática|🔵|fora de escopo (não é construção)|

## Aulas 96–100

Todas 🔵 ou fora de escopo — pedagógicas/revisão (matemática no
cotidiano, estratégias de problema, revisão geral, encerramento), não
construção matemática nova.

## Aulas 101–150

- **Cálculo diferencial/integral (101-110):** 🟡 parcial — limite e
  continuidade de função racional em ponto finito (ETAPA 1058-1059),
  divisão de polinômios/Teorema do Resto (ETAPA 1056); derivadas,
  integrais e o caso geral de limites ainda dependem de reais completos
  clássicos, ainda em aberto além da base de Cauchy (ETAPA 1035, 1061-1064).
- **Álgebra Linear (111-120):** 🟡 vetores e produto escalar/vetorial
  existem (ETAPA 1038-1039); autovalores, diagonalização, espaços
  abstratos maiores 🔵.
- **Probabilidade/Estatística avançada (121-130):** 🟢 Bayes (ETAPA
  1043), 🟢 correlação/regressão e R² (ETAPA 1044) — o resto (binomial,
  normal, teorema central do limite, testes de hipótese) 🔵.
- **Matemática Discreta (131-140):** 🟢 lógica proposicional,
  quantificadores (341-360), 🟢 relações injetora/sobre/bijetora (75-77),
  🟢 recorrência (49), 🟢 grafos + Euler/Hamilton + árvores (111-130), 🟢
  combinatória com repetição (39). Indução matemática nomeada à parte:
  🟡. Teoria dos conjuntos formal: 🟡.
- **Geometria diferencial/topologia (141-150):** 🔵 tudo — exceto
  topologia finita (881-920), diferente do que a aula pede.

## Aulas 151–400

Quase inteiramente 🔵: cálculo avançado, EDOs, análise real/complexa,
física matemática, criptografia, teoria dos jogos, fractais, IA, finanças
quantitativas, história/filosofia. Dois motivos: dependem de reais
completos clássicos (a base de Cauchy já existe desde ETAPA 1064, mas
não a completude Dedekind/supremo geral), ou são áreas de pesquisa
avançada nunca visitadas por este projeto de matemática finita e
construtiva.

Exceções reais espalhadas nesse território:

- 🟢 Grupos, anéis, corpos, homomorfismos (ETAPA 89-99) — cobre boa parte
  do nível introdutório pedido nas aulas 251-259.
- 🟢 Categorias finitas (ETAPA 301) — versão finita do pedido nas aulas
  261-264.
- 🟢 Computabilidade finita (ETAPA 401) — versão finita do pedido nas
  aulas 269-270 (Turing, decidibilidade).
- 🟢 Otimização de modelos finitos (ETAPA 991) — parente finito das aulas
  331-336.
- 🟡 Hipótese de Riemann, Gödel, infinito de Cantor (aulas 184-187, 292):
  registradas em `nucleo/problemas_abertos.py` como problemas declarados
  em aberto — nem fingidas resolvidas, nem ignoradas.

## Aulas 401–1000 (segundo lote fornecido pelo autor)

Cruzamento do segundo lote (aulas 401-1000, 60 blocos de 10, tema de
pós-graduação/pesquisa e matemática aplicada) contra o código e os
documentos reais — mesmo princípio da seção anterior: nada aceito por
familiaridade do nome, só o que uma busca real no projeto confirma.
Bloco por bloco (não item por item, dado o volume):

- **401-410 Teoria dos Jogos Avançada:** 🔵 tudo — nenhuma teoria de
  jogos formal construída (Nash, Shapley, leilões só existem como
  curiosidade em `base_curiosidades_reais.py`, não como prova).
- **411-420 Geometria Computacional:** 🔵 tudo — fecho convexo, Voronoi,
  Delaunay, nada construído.
- **421-430 Teoria dos Grafos Avançada:** 🟡 parcial — coloração de
  grafos (🟢 ETAPA 118, existência de k-coloração por busca exaustiva,
  testado com K3) e grafos Hamiltonianos (🟢 ETAPA 124) já existem.
  Planaridade e fluxo em redes são **explicitamente proibidos** no
  bloco de grafos (ETAPA 111-127 dizem isso de forma literal), então
  Teorema das Quatro Cores, Euler para planares e fluxo máximo/corte
  mínimo continuam 🔵. Emparelhamento/Hall, random graphs, expanders e
  redes complexas também 🔵.
- **431-440 Topologia Algébrica:** 🔵 tudo — homologia, cohomologia,
  K-teoria não construídas (existe "topologia finita", mas é
  combinatória de conjuntos abertos finitos, não isto).
- **441-450 Matemática dos Sons e Imagens:** 🔵 tudo — processamento de
  sinal exige números complexos, que o projeto nem constrói.
- **451-460 Estatística Espacial e Geoestatística:** 🔵 tudo.
- **461-470 Álgebra Universal e Teoria de Modelos:** 🟡 parcial —
  `nucleo/teoria_modelos_prova_finita.py` (ETAPA 361-380) já construiu
  estrutura, subestrutura, homomorfismo, isomorfismo e equivalência
  elementar sobre uma família **finita** de sentenças — cobre a aula
  464 na versão finita. Compacidade e Löwenheim-Skolem (465-466) são
  teoremas sobre estruturas infinitas, sem sentido nessa versão finita:
  🔵. Álgebras de Boole existem como raiz (lógica booleana); retículos
  gerais não.
- **471-480 Teoria dos Conjuntos Avançada:** 🔵 tudo — ordinais,
  cardinais, hipótese do contínuo, forcing. Só indução **finita**
  existe, não indução transfinita.
- **481-490 Matemática da Computação Quântica:** 🔵 tudo — sem números
  complexos no projeto, qubits/Shor/Grover não têm base para existir.
- **491-500 Encerramento da Quinta Centena:** 🔵 quase tudo, pedagógico/
  aplicado, fora de escopo de construção.
- **501-510 Teoria da Prova e Fundamentos:** 🟡 parcial — dedução
  natural e cálculo de sequentes como objeto finito verificável já
  existem (mesmo `teoria_modelos_prova_finita.py`, ETAPA 361-380:
  sequente, regra de inferência, derivação). Curry-Howard, assistentes
  de prova, lógica linear, lógicas modais: 🔵.
- **511-520 Matemática dos Materiais e Engenharia:** 🔵 tudo — aplicado/
  contínuo, fora de escopo.
- **521-530 Teoria de Representações:** 🔵 tudo — grupos/anéis/corpos
  básicos existem (ETAPA 89-99), representações propriamente ditas não.
- **531-540 Geometria Simplética e Poisson:** 🔵 tudo.
- **541-550 Análise em Variedades e EDPs Geométricas:** 🔵 tudo — exige
  reais completos clássicos e variedades diferenciáveis, nenhum dos dois
  construído além da base de Cauchy (ETAPA 1061-1064).
- **551-560 Combinatória Avançada:** 🟡 parcial — combinatória básica
  robusta já existe (princípios aditivo/multiplicativo, permutação,
  combinação, Pascal, partições, Catalan, Stirling, Bell — ETAPA 36-60).
  Ramsey, Turán, método probabilístico, designs, quadrados latinos,
  Hadamard, combinatória aditiva: 🔵, nada construído especificamente.
- **561-570 Teoria da Aprendizagem Estatística:** 🔵 quase tudo —
  regressão linear e R² existem (ETAPA 1044); SVM, redes neurais, GANs:
  🔵.
- **571-580 Teoria dos Números Computacional:** 🟡 parcial — segurança
  de RSA/fatoração de inteiros grandes e criptografia pós-quântica
  baseada em reticulados já estão **registradas como problemas abertos
  declarados** em `nucleo/problemas_abertos.py` (não fingidas resolvidas,
  não ignoradas). Testes de primalidade reais (Miller-Rabin, AKS),
  curvas elípticas, provas de conhecimento zero: 🔵.
- **581-590 Física-Matemática Avançada:** 🔵 tudo — totalmente fora de
  escopo.
- **591-600 Encerramento da Sexta Centena:** 🔵 quase tudo, filosófico/
  pedagógico.
- **601-610 Matemática dos Riscos e Seguros (Atuária):** 🔵 tudo.
- **611-620 Matemática da Genética e Evolução:** 🔵 tudo.
- **621-630 Teoria da Complexidade Computacional:** 🟡 parcial — "P
  versus NP" já está **registrado como problema aberto declarado**
  (`nucleo/problemas_abertos.py`, inclusive citado como Problema do
  Milênio); as etapas de grafos (coloração, Hamiltoniano) já observam
  na própria construção que o problema é NP-difícil em geral e correto
  apenas por o domínio ser finito. Classes formais (P, NP, PSPACE, BQP),
  Cook-Levin, hierarquia polinomial como teoria construída: 🔵.
- **631-640 Matemática das Decisões e Votação:** 🔵 tudo — Arrow,
  Gibbard-Satterthwaite, Gale-Shapley não construídos.
- **641-650 Geometria da Informação:** 🔵 tudo.
- **651-660 Teoria de Ondas e Solitons:** 🔵 tudo.
- **661-670 Matemática das Redes Sociais:** 🟡 muito parcial — grafos
  reais existem (grau, conectividade, caminho, ciclo, ETAPA 111-127);
  métricas específicas de rede social (centralidade, agrupamento,
  modularidade, homofilia): 🔵.
- **671-680 Matemática da Energia e Sustentabilidade:** 🔵 tudo.
- **681-690 Tópicos de Geometria Enumerativa:** 🔵 tudo.
- **691-700 Encerramento da Sétima Centena:** 🔵 quase tudo, pedagógico.
- **701-710 Matemática da Astronomia e Cosmologia:** 🔵 tudo.
- **711-720 Teoria dos Conjuntos Fuzzy e Lógica Difusa:** 🔵 tudo —
  lógica booleana clássica existe como raiz; lógica de valores contínuos
  não.
- **721-730 Séries Temporais e Previsão:** 🔵 tudo — exige reais
  completos clássicos e estatística contínua.
- **731-740 Teoria da Informação Quântica Avançada:** 🔵 tudo.
- **741-750 Matemática do Aprendizado Profundo:** 🟡 muito parcial —
  "limites fundamentais de generalização de redes neuronais profundas"
  já **registrado como problema aberto declarado**
  (`nucleo/problemas_abertos.py`). Backpropagation, transformers, LLMs:
  🔵, nada construído.
- **751-760 Programação Matemática e Otimização Discreta:** 🟡 muito
  parcial — otimização de modelos finitos existe (ETAPA 991); MIP,
  planos de corte, VRP, meta-heurísticas específicas: 🔵.
- **761-770 Matemática da Medicina e Imagens Médicas:** 🔵 tudo.
- **771-780 Matemática da Música e Acústica:** 🔵 quase tudo — só razão/
  proporção (ETAPA 1036) toca de leve em afinação; acústica/escalas
  propriamente ditas não construídas.
- **781-790 Teoria de Singularidades e Catástrofes:** 🔵 tudo.
- **791-800 Encerramento da Oitava Centena:** 🔵 quase tudo, cultural/
  pedagógico.
- **801-810 Teoria de Processos Estocásticos:** 🔵 tudo — só menção em
  `base_curiosidades_reais.py` (curiosidade, não construção); nenhuma
  cadeia de Markov, martingale ou movimento browniano real construído.
  Probabilidade finita (ETAPA 921-960) é a base mais próxima que existe.
- **811-820 Topologia de Dimensões Baixas:** 🔵 tudo.
- **821-830 Análise Numérica de EDPs:** 🔵 tudo.
- **831-840 Teoria dos Números Analítica:** 🟡 muito parcial — Hipótese
  de Riemann já **registrada como problema aberto declarado**
  (`nucleo/problemas_abertos.py`, também como Problema do Milênio);
  teoria dos números elementar robusta existe (primos, MDC/MMC,
  congruência, ETAPA 1-20-ish); funções L, formas modulares, Langlands:
  🔵.
- **841-850 Matemática dos Sistemas Complexos:** 🔵 tudo.
- **851-860 Álgebra Homológica:** 🔵 tudo — grupos/anéis/corpos básicos
  existem (ETAPA 89-99), homologia/funtores derivados/categorias
  derivadas não.
- **861-870 Teoria da Informação e Aprendizado:** 🔵 quase tudo — só o
  mesmo registro de problema aberto de generalização (741-750) toca de
  leve; entropia, informação mútua, MDL não construídos.
- **871-880 Matemática do Universo Digital:** 🟡 muito parcial — RSA,
  criptografia pós-quântica, consenso blockchain e provas de
  conhecimento zero já **registrados como problemas abertos
  declarados** (`nucleo/problemas_abertos.py`); PageRank, hashing,
  Reed-Solomon: 🔵.
- **881-890 Modelagem Matemática Multidisciplinar:** 🔵 tudo, aplicado.
- **891-900 Encerramento da Nona Centena:** 🔵 quase tudo, filosófico.
- **901-910 Teoria de Controle e Sistemas Dinâmicos:** 🔵 tudo.
- **911-920 Geometria dos Números e Retículos:** 🟡 muito parcial —
  criptografia baseada em reticulados (LWE, NTRU) já **registrada como
  problema aberto declarado** (`nucleo/problemas_abertos.py`); Minkowski,
  LLL, empacotamento de esferas: 🔵.
- **921-930 Matemática da Percepção e Visão:** 🔵 tudo.
- **931-940 Teoria das Probabilidades Avançada:** 🟡 muito parcial —
  probabilidade finita robusta existe (condicional, Bayes, ETAPA
  921-960); grandes desvios, matrizes aleatórias, percolação: 🔵.
- **941-950 Matemática da Robótica:** 🔵 tudo.
- **951-960 Teoria de Singularidades em EDPs:** 🔵 tudo.
- **961-970 Matemática do Envelhecimento e Longevidade:** 🔵 tudo,
  atuarial/aplicado.
- **971-980 Geometria Algébrica Computacional:** 🔵 tudo — bases de
  Gröbner e software (Macaulay2 etc.) não construídos.
- **981-990 Matemática da Consciência e Cognição:** 🔵 tudo, natureza
  filosófica/especulativa, fora de escopo de construção matemática.
- **991-1000 O Grande Final:** 🟡 — os Problemas do Milênio citados
  (P vs NP, Hipótese de Riemann, Conjectura de Hodge, Yang-Mills,
  Navier-Stokes, Birch-Swinnerton-Dyer) **já estão todos registrados**
  em `nucleo/problemas_abertos.py` com estado explícito
  `PROBLEMA_ABERTO_DECLARADO` e plano de investigação nativo — nem
  fingidos resolvidos, nem ignorados. O resto (pedagógico/filosófico)
  fora de escopo de construção.

Resumo honesto deste segundo lote: dos 60 blocos, **14 têm algum
🟡 parcial** (421-430, 461-470, 501-510, 551-560, 561-570, 571-580,
621-630, 661-670, 741-750, 751-760, 831-840, 861-870, 871-880, 911-920,
931-940 — a maioria porque um problema difícil citado já está
genuinamente registrado como aberto em `nucleo/problemas_abertos.py`,
não porque o projeto o resolveu; só 421-430, 461-470, 501-510 e 551-560
têm construção real por trás, não apenas registro de problema aberto).
Os outros 46 blocos são inteiramente 🔵: exigem infraestrutura que o
projeto genuinamente não tem ainda (números complexos, reais completos
clássicos, variedades diferenciáveis, processos estocásticos contínuos,
física, ou são aplicações de domínio específico fora do escopo de
matemática construtiva finita). Nenhum desses blocos tem ponte de um
passo só — diferente do primeiro lote (263-274), aqui não há candidatos
de "próximo alvo imediato" do mesmo tamanho.

## Candidatos com ligação próxima (próximos alvos prováveis)

Ver `PLANO_PSF_IAMINY.md`, itens 262+, para a lista priorizada original
dos 🟡/🔵 que já tinham ponte direta para código existente — todos os 12
candidatos originais (itens 263-274) estão fechados. Os 🟡/🔵 que
restam nesta auditoria (limites gerais, funções não-racionais,
trigonometria em intervalos, geometria plana/espacial, cálculo) exigem
construções maiores, sem ponte de um passo só.
