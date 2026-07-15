# Auditoria de currículo externo de Português — 1000 aulas

Cruzamento de uma lista externa de 1000 "aulas" de Português (currículo
do alfabeto à literatura, fornecida pelo autor, 15 blocos de conteúdo)
contra os 1100 conceitos reais de `lingua_portuguesa/conhecimento_puro.py`
e os módulos operacionais (`lexico.py`, `morfologia.py`, `gramatica.py`,
`morfemas_afixais.py`). Isto não é aula nova — é inventário de cobertura.

Por pedido explícito, **os itens de exercício/atividade foram ignorados**
nesta auditoria: "revisão", "simulado", "exercícios", "produção de texto
livre", "jogo", "teste", "correção comentada", "autoavaliação", "ditado",
"leitura de X — análise" sem nomear um conceito novo, etc. Esses itens
são forma pedagógica, não conhecimento linguístico distinto — o Bloco 15
inteiro (aulas 921-1000) é essencialmente só isso, por exemplo.

Legenda: 🟢 TEM (conceito construído, com dependências e léxico
próprio) · 🟡 PARCIAL (existe por alias, por termo genérico, ou só
parte da família) · 🔵 NÃO TEM.

## Bloco 1 — Alfabeto e fonética (aulas 1-50)

🟢 quase tudo: alfabeto, vogal (com todas as variantes: aberta/fechada/
nasal/oral/tônica/átona), consoante, ditongo, tritongo, encontro
consonantal, dígrafo, sílaba (aberta/fechada/tônica), oxítona/
paroxítona/proparoxítona (com regra própria de cada uma), acento
diferencial, til, apóstrofo, nasalização, semivogal, fonema, hiato
(+ acento em hiato), sotaque, palavras homófonas (`homofonia`,
`homofonia lexical`).

🟢 **trema** — fechado (sobrevivência do sinal em nomes próprios
estrangeiros, ex.: Müller, depois do Acordo Ortográfico de 1990).

🟢 **ditongo crescente/decrescente** — fechado (dois conceitos novos,
ligados a `ditongo` e `semivogal`, distinguindo pela posição da semivogal:
"quase" crescente, "pai" decrescente).

🟢 **adaptação de estrangeirismo** — na verdade já estava fechado quando
este documento foi escrito; a leitura anterior não cruzou contra o nome
exato. `adaptação de empréstimo` (`lingua_portuguesa/conhecimento_puro.py`,
ao lado de `estrangeirismo não adaptado`) já é o processo geral de
adaptação gráfica/fonológica/morfológica de palavra recebida.

## Bloco 2 — Ortografia (aulas 51-120)

🟢 quase tudo: crase (+ regras específicas: com pronomes, com lugares),
hífen, sigla, sigla soletrada, acrônimo, abreviatura (+ convencional,
plural, ponto), toda a família de vírgula (enumeração, vocativo, aposto,
conectivo, oração adverbial/explicativa — 7 tipos nomeados), ponto e
vírgula, dois-pontos, travessão (+ de diálogo, parentético), parênteses,
aspas (+ de citação), reticências (+ de suspensão, de omissão).

🟡 parcial: os pares de confusão ortográfica específicos ("por que" x
"porque" x "por quê" x "porquê", "mas" x "mais", "onde" x "aonde" etc.)
não existem como entradas isoladas — a distinção entre classes
gramaticais que os fundamenta (preposição, conjunção, pronome
interrogativo) está construída, mas o par didático em si não é um
conceito PSF.

## Bloco 3 — Morfologia: substantivo e adjetivo (aulas 121-180)

🟢 quase completo: substantivo (comum/próprio/concreto/abstrato/
coletivo/primitivo/derivado/simples/composto/sobrecomum/epiceno/comum
de dois), gênero, número gramatical, plural (regular e casos em -ão/
-l/-m), grau aumentativo/diminutivo (sintético e analítico), adjetivo
(+ pátrio/qualificativo/relacional/uniforme), concordância nominal,
comparativo (3 tipos), superlativo (absoluto sintético/analítico,
relativo), locução adjetiva, substantivação, derivação prefixal/
sufixal/parassintética, justaposição, aglutinação, onomatopeia.

🟢 **hibridismo** — fechado (ligado a `justaposição`/`aglutinação`); único item do bloco inteiro, agora coberto.

## Bloco 4 — Artigos, numerais e pronomes (aulas 181-250)

🟢 **100% coberto**: artigo definido/indefinido, todos os 5 tipos de
numeral (cardinal/ordinal/multiplicativo/fracionário/coletivo), todos
os pronomes (reto/oblíquo/de tratamento/possessivo/demonstrativo/
indefinido/interrogativo/relativo/reflexivo/recíproco/clítico), e as
três colocações pronominais (próclise/ênclise/mesóclise).

## Bloco 5 — Verbos: conjugações e tempos (aulas 251-350)

🟢 a estrutura inteira do verbo: radical verbal, vogal temática,
desinência (modo-temporal, número-pessoal), as 3 conjugações, verbo
regular/irregular/defectivo/abundante, todos os tempos do indicativo e
subjuntivo com nome próprio (inclusive futuro do pretérito, pretérito
mais-que-perfeito), infinitivo pessoal/impessoal, gerúndio, particípio,
verbo auxiliar/de ligação/transitivo/intransitivo, voz ativa/passiva/
reflexiva, perífrase verbal, concordância verbal.

🟡 parcial: presente do indicativo e modo imperativo (os componentes
`tempo verbal`+`presente` e `modo verbal`+`imperativo` existem
separados, mas não como termo composto único); regência verbal (existe
`regência` genérica, não a lista de regências específicas por verbo:
assistir, obedecer, preferir etc. — isso é justamente o "limite
operacional" já registrado em `pessoa gramatical`: "a conjugação
completa por pessoa ainda deve crescer").

🟢 fechados: verbo pronominal, verbo reflexivo (como classe verbal,
distinto de pronome reflexivo), verbo impessoal, verbo unipessoal,
verbo anômalo, e locução verbal (ligado a `perífrase verbal`, o nome
tradicional escolar do mesmo fenômeno).

## Bloco 6 — Advérbios, preposições, conjunções, interjeições (aulas 351-420)

🟢 quase tudo: advérbio (+ modo/tempo/lugar/intensidade/afirmação/
negação), locução adverbial, preposição (+ essencial/acidental),
locução prepositiva, conjunção (+ coordenativa/subordinativa), as 5
coordenativas nomeadas (aditiva/adversativa/alternativa/conclusiva/
explicativa), 8 das 9 subordinativas adverbiais nomeadas, interjeição,
locução interjetiva.

🔵 genuíno: advérbio de dúvida (como termo próprio — existe `adjunto
adverbial de dúvida`, função sintática equivalente), oração
proporcional (existe `oração subordinada adverbial proporcional`, nome
mais completo), conjunção integrante (a função está coberta pelas
orações substantivas, o rótulo tradicional da gramática escolar não é
usado).

## Bloco 7 — Sintaxe: período simples (aulas 421-480)

🟢 **essencialmente 100%**: sujeito (simples/composto/oculto/
indeterminado), oração sem sujeito, predicado (verbal/nominal/
verbo-nominal), objeto direto/indireto/preposicionado/pleonástico,
complemento nominal, adjunto adnominal, adjunto adverbial (11
subtipos!), agente da passiva, aposto (4 subtipos), vocativo (3
posições), predicativo do sujeito/do objeto.

🟢 núcleo do sujeito — fechado como alias de `núcleo nominal` (o mesmo
conceito, agora também consultável pelo nome didático).

## Bloco 8 — Sintaxe: período composto (aulas 481-540)

🟢 **100% coberto**: período composto, coordenação (sindética/
assindética), e as 9 subordinadas substantivas + 2 adjetivas + as
reduzidas de infinitivo/gerúndio/particípio, todas nomeadas
individualmente.

## Bloco 9 — Semântica e estilística (aulas 541-620)

🟢 a base semântica inteira: sinonímia, antonímia (3 subtipos),
homonímia, paronímia, polissemia, denotação/conotação, campo semântico/
lexical, hiponímia, hiperonímia, e boa parte das figuras clássicas:
metáfora, comparação, metonímia, catacrese, personificação (=
prosopopeia), ironia, eufemismo, hipérbole, gradação, antítese,
paradoxo, elipse, anáfora, pleonasmo, ambiguidade (4 subtipos).

🟢 **fechado nesta sessão** — todo o cluster de figuras mais técnicas:
sinestesia, antonomásia, zeugma, assíndeto, polissíndeto, aliteração,
assonância, paronomásia, silepse, anacoluto (ordem 1110-1119 em
`conhecimento_puro.py`). Aliteração e assonância ganharam, além do
conceito, reconhecimento operacional real em
`lingua_portuguesa/figuras_de_som.py`: contam a consoante/vogal inicial
mais repetida numa sequência de palavras — não citam o efeito, provam
contando (testado com "o rato roeu a roupa do rei de Roma" e "Amanhã a
Ana anda apressada", ambas com repetição >= 5). Os outros oito ligam a
conceitos já existentes (metáfora, metonímia, elipse, oração coordenada
assindética/sindética, paronímia, concordância).

## Bloco 10 — Acentuação, crase e novo acordo (aulas 621-670)

🟢 sobreposição quase total com Blocos 1-2 (já cobertos ali): acento
agudo/circunflexo/grave, crase, hífen. Os casos ultra-específicos
(tem/têm, vem/vêm, pôde/pode como pares de decoreba escolar) não são
conceitos PSF separados — a regra de acentuação que os gera está
construída, o par memorizável não.

## Bloco 11 — Interpretação e compreensão textual (aulas 671-730)

🟢 quase tudo: tema, tópico frasal, coerência, coesão (9 subtipos:
referencial, sequencial, por elipse, por substituição, por colocação
lexical...), progressão temática, inferência, pressuposição (3
subtipos), intertextualidade, gênero textual, narração, descrição,
exposição, discurso direto/indireto.

🔵 genuíno: ideia principal como termo distinto de `tema` (função
coberta, rótulo didático específico não), injunção (tipologia textual
instrucional), discurso indireto livre (existe direto e indireto
separados, a forma híbrida não).

## Bloco 12 — Produção textual: redação (aulas 731-800)

🟡 a base argumentativa existe (`argumentação`, `parágrafo
argumentativo`, `cadeia argumentativa`, `garantia argumentativa`,
`argumento de autoridade documentada`, `conectivo`, `registro`,
`variedade nacional`), mas a estrutura escolar específica da redação
dissertativa-argumentativa (tese, proposta de intervenção, "dissertação"
como termo próprio, contra-argumentação nomeada) não tem entrada
dedicada — isto é modelo pedagógico de exame (ENEM/vestibular), mais
perto de gênero textual aplicado do que de conhecimento linguístico
puro construído aqui.

## Bloco 13 — Literatura: poesia e prosa (aulas 801-860)

🟢/🔵 **dividido conscientemente, não mais lacuna cega**: verso, estrofe,
métrica (com toda a família de rima e metro) e `gênero épico`/`gênero
lírico` como classificações próprias — **fechados** (ligam a `poema`,
`narração`, `gênero literário`, `gênero dramático` já existentes), mais
o conceito geral `literatura` e `método de análise literária`
(sintetiza figura de linguagem, narrador, estrutura narrativa, coesão,
coerência num roteiro de análise).

🔵 **continua fora de escopo, por decisão explícita do autor**: soneto,
novela, fábula, parábola, alegoria, mito, teatro como forma específica,
e toda a sequência de escolas literárias (Trovadorismo → Modernismo →
contemporâneo, autores, obras, biografias, datas). O autor propôs 150
aulas cobrindo isso (histórico/biográfico) e, ao ser perguntado, optou
por deixar de fora — esse conteúdo é conhecimento histórico/cultural
externo, não algo que PSF possa derivar de primitivas linguísticas sem
fingir. Mesma lógica de por que Matemática não cobre história da
matemática: a fronteira não é falta de esforço, é a natureza do
conhecimento.

## Bloco 14 — Análise linguística avançada (aulas 861-920)

🟡 parcial: fonologia como campo (a palavra em si não é conceito, mas
dezenas de termos fonológicos derivados existem: análise fonológica,
processo fonológico, assimilação fonológica, neutralização fonológica);
neologismo, arcaísmo, variação diatópica/diastrática/diacrônica (via
alias para variação regional/social/histórica), norma-padrão,
intertextualidade, falácia (5 subtipos), retórica existem.

🔵 genuíno: paródia, referenciação como termo próprio, sequência
textual como tipologia (narração/descrição/argumentação/exposição/
injunção existem soltas, não como "sequência textual" agrupadora),
modalização, polifonia.

## Bloco 15 — Revisão, simulados e "infinito" (aulas 921-1000)

Ignorado por inteiro — é 100% atividade pedagógica (revisão, simulado,
jogo, mapa mental, produção livre, autoavaliação), sem nenhum conceito
linguístico novo nomeado.

## Resumo honesto

Cobertura real, excluindo exercícios: dos 14 blocos de conteúdo (1-14),
**9 estão essencialmente completos** (Blocos 3, 4, 6, 7, 8 quase ou
totalmente 100%; Blocos 1, 2, 5, 11 com só lacunas pontuais). O Bloco 9
(semântica/estilística) está **100% coberto** depois do fecho do
cluster de figuras técnicas. O Bloco 13 (literatura) teve sua parte
**estrutural** fechada (verso, métrica, rima, gêneros lírico/épico,
literatura, método de análise) — o que restou de propósito fora de
escopo é só a parte histórico-biográfica (escolas literárias, autores,
obras, datas), por decisão explícita do autor depois de consultado:
isso é conhecimento histórico/cultural externo, não linguística
construtiva, mesma lógica de por que Matemática não cobre história da
matemática. Os dois gaps pontuais que restavam (ditongo crescente/
decrescente como classificação própria; processo geral de adaptação de
estrangeirismo) também estão fechados — o primeiro com dois conceitos
novos, o segundo por correção: já estava coberto por `adaptação de
empréstimo` quando esta auditoria foi escrita, só não tinha sido cruzado
contra esse nome exato.

**Fechados nesta sessão, 21 conceitos ao todo** (ordem 1100-1119 em
`conhecimento_puro.py`, "funcionamento" agora em 1120):
- Ordem 1100-1109: hibridismo; verbo pronominal, reflexivo, impessoal,
  unipessoal, anômalo; locução verbal; regência nominal; núcleo do
  sujeito (alias); se apassivador e se índice de indeterminação do
  sujeito (estes dois com reconhecimento operacional real em
  `lingua_portuguesa/uso_do_se.py`).
- Ordem 1110-1119: sinestesia, antonomásia, zeugma, assíndeto,
  polissíndeto, aliteração, assonância, paronomásia, silepse, anacoluto
  — aliteração e assonância com reconhecimento operacional real em
  `lingua_portuguesa/figuras_de_som.py` (contagem de consoante/vogal
  inicial repetida, não citação de memória).

## Anexo — conceitos de ligação entre blocos (segundo envio do autor)

O autor enviou um segundo material propondo "aulas de ligação" entre os
15 blocos (transições fonética→ortografia, ortografia→morfologia etc.).
Por pedido explícito, isso não foi tratado como aulas novas a somar —
foi lido como **temas/conceitos** embutidos nas pontes, e cruzado do
mesmo jeito contra o conhecimento real. A maioria já estava coberta
pelos 15 blocos originais; o que segue é só o que essa leitura por
ponte trouxe de genuinamente novo (achado ou confirmado).

🟢 **TEM**:
- Sufixos que indicam classe gramatical (-dade, -ção, -mente) — a
  ponte "ortografia→morfologia" pede exatamente isto, e é o que
  `lingua_portuguesa/morfemas_afixais.py` acabou de construir nesta
  mesma sessão (`SUFIXOS_PRODUTIVOS` já carrega `classe_resultante`).
- Concordância na tríade artigo+substantivo+adjetivo — `concordância
  nominal` existe, e `gramatica.py` já implementa as duas regras de
  verdade (`RegraConcordanciaDeterminanteNome`,
  `RegraConcordanciaNomeAdjetivo`), não só o conceito citado.
- Coesão por substituição de substantivo por pronome —
  `coesão por substituição nominal`.
- Resumo, resenha, paráfrase (a ponte "interpretação→produção") — os
  três existem como conceitos próprios.
- Ritmo (a ponte "figuras→acentuação" cita ritmo poético) — `ritmo`
  existe como conceito, mas só na acepção fonética/prosódica geral, não
  como métrica de verso (ver 🔵 abaixo).
- Relação som→grafema, a ponte "fonética→ortografia" em si — não é uma
  peça faltando: é literalmente a espinha dorsal da linha canônica
  (`diferença`→`som`→`marca`→`grafema`→`letra`), já a base de tudo.

🟢 **FECHADOS** (estavam 🟡/🔵, resolvidos nesta sessão):
- Regência nominal — ligado a `regência` genérica.
- **"Se" apassivador** (voz passiva sintética: "vendem-se casas") e
  **"se" como índice de indeterminação do sujeito** ("entende-se de
  livros") — os dois com conceito próprio E reconhecimento operacional
  real em `lingua_portuguesa/uso_do_se.py`: dado verbo+"se"+o que vem
  depois, decide entre os dois usos conferindo concordância de número
  contra o léxico (`Dicionario`), não por regra decorada. Testado com
  5 frases reais, varrido contra o léxico sem falso positivo.
- Verbo pronominal (confirma e fecha o achado do Bloco 5 pela ponte
  pronome→verbo).
- **Paródia, pastiche e sátira** — fechados (ligados a
  intertextualidade/ironia/hipérbole); `intertextualidade` já citava
  "uma paródia retoma outro texto" como exemplo antes mesmo de paródia
  existir como conceito próprio.
- **Métrica/escansão como tema de verso** — fechada a família de 11
  conceitos (métrica, escansão, verso, estrofe, decassílabo, redondilha,
  alexandrino, rima toante/consoante/rica/pobre), ligada a `sílaba` e
  `rima silábica`. Escopo honesto: só documentação — contagem automática
  de sílabas poéticas com sinalefa não construída (depende da
  tonicidade automática, já registrada como fronteira aberta).

## Anexo 2 — terceiro envio do autor: pares de confusão ortográfica

O autor enviou uma lista de 15 pares de confusão ortográfica para
completar o Bloco 2. Onze pares são reais e foram construídos em
`lingua_portuguesa/paronimos_comuns.py`, ligados ao conceito já
existente `paronímia`: comprimento/cumprimento, descrição/discrição,
estrato/extrato, flagrante/fragrante, censo/senso,
cessão/sessão/seção, concerto/conserto, emergir/imergir,
eminente/iminente, ratificar/retificar, trás/traz/atrás.

**Três pares da lista original não foram construídos, por não serem
pares reais** — sinalizado aqui em vez de aceito por confiança na
fonte (a mesma regra que vale para qualquer material externo):
"influxo x influxo" e "inerte x inerte" repetem a mesma palavra duas
vezes (parecem erro de digitação/geração da lista); "sortear x surtir"
não é uma confusão paronímica estabelecida em português — "surtir" só
existe de fato na locução "surtir efeito", não como par de confusão
com "sortear" (sortear = fazer sorteio). Nenhum dos três entrou como
conhecimento construído.

## Anexo 3 — quarto envio do autor: literatura como disciplina completa

O autor propôs remodelar o Bloco 13 com 150 aulas de história literária
(escolas, biografias, obras, datas). Antes de construir, a pergunta foi
devolvida ao autor: como tratar conteúdo histórico/biográfico, que não
é derivável de primitivas linguísticas? Resposta: **deixar de fora**,
mesma fronteira que já vale para história da matemática.

O que tinha ponte estrutural real foi fechado (4 conceitos, ordem
1135-1138): **literatura** (função estética predominante da linguagem,
ligada a gênero literário/figura de linguagem/conotação), **gênero
lírico** e **gênero épico** (completam a tríade clássica ao lado de
`gênero dramático`, que já existia — ligados a `poema` e
`narração`/`estrutura narrativa`), e **método de análise literária**
(roteiro que amarra figura de linguagem, narrador, estrutura narrativa,
coesão e coerência já existentes). Nenhuma escola literária, autor,
obra ou biografia entrou como conhecimento construído — permanecem
fora de escopo por decisão explícita, não por lacuna de esforço.
