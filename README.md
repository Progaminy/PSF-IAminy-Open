# PSF-IAminy

Sistema local do projeto Pensador Sem Fronteiras para conhecimento puro, investigação, organização e validação.

**Para rodar o projeto (testes, chat, interface local): veja [`COMO_RODAR.md`](COMO_RODAR.md).**

## Foco atual

O foco atual é preservar, corrigir e crescer apenas os conhecimentos principais:

```text
1. Matemática — conhecimento PSF amplo; a camada pura fica em `conhecimento/ETAPA_*.md` e módulos testados.
2. Português — conhecimento PSF vivo; agora materializado em 1141 conceitos puros na mesma linha canónica.
```

Outras áreas não são prioridade agora.

## Arquitetura atual dos motores

```text
Conhecimento de Matemática
→ MotorMatematica
→ resolução, reconstrução, prova, cálculo e monografia

Conhecimento de Português
→ MotorPortugues
→ leitura, análise, escrita, sentido e produção textual

MotorComumPSF
→ memória, dependências, auditoria, busca e rastreabilidade
```

Os motores não se sobrepõem. O motor comum presta serviços, mas não produz verdade matemática nem linguística.

O `MotorMatematica` inventaria **203 documentos conceituais matemáticos vivos**, resolve expressões racionais não negativas com precedência correta, reconstrói divisão por quociente, resto, fração e expansão decimal, executa prova formal certificada no fragmento lógico finito, distingue teste de prova universal e produz monografia como consolidação PSF.

A trigonometria natural foi ligada sem saltos internos desde diferença, unidade, medida, razão, ângulo, perpendicularidade, triângulo retângulo e semelhança até seno, cosseno, tangente, cotangente, secante, cossecante e suas identidades elementares. A implementação usa razões exatas e não chama funções trigonométricas prontas.

Todo conceito matemático inventariado precisa agora de uma ponte de entrada explícita. O motor audita os 203 documentos e bloqueia reconstrução de qualquer conceito que fique sem dependências. **Sem ponte significa sem conhecimento PSF.** Fórmulas e respostas isoladas encontradas em material antigo continuam como legado/candidatos; existência no arquivo não lhes dá autoridade de conhecimento.

Foram preservados **153 temas de material legado** como candidatos de reconstrução: 39 fórmulas, 10 monografias, 60 problemas abertos e 50 problemas aplicados, com duplicações removidas. Esses temas não entram como conhecimento pronto.


## Divisão reconstruída pelo PSF

A divisão não exata deixou de ser bloqueada. O motor preserva primeiro a forma exata e depois constrói a escrita decimal pelo transporte repetido do resto.

```text
12 : 5 → fração exata 12/5 → 2,4
12 : 5 com 3 casas → 2,400
1 : 3 com 3 casas → 0,333, mantendo 1/3 como forma exata
2 : 3 com 3 casas arredondadas → 0,667
```

Cada casa decimal mostra como o resto foi multiplicado por 10, repartido pelo divisor e convertido em novo resto. Truncamento e arredondamento são explícitos.

Divisão por zero é conhecimento matemático sólido, mas não entra como frase antecipada de autoridade. O PSF chega a esse conhecimento pelo fluxo natural: reconstrói `divisor × quociente = dividendo`; para dividendo não nulo, `0 × q` nunca o recompõe, e em `0 : 0` não há quociente único. Assim, a divisão por zero fica **não definida por construção PSF**, e não como problema aberto.

## Motor auxiliar de validação e otimização

Existe um único `MotorAuxiliarValidacao` em `validacao_externa/`, compartilhado pelos dois domínios sem os misturar.

```text
MotorMatematica → produz o cálculo e a reconstrução
MotorPortugues → produz a análise linguística
MotorAuxiliarValidacao → compara, mede, cacheia e procura divergências
```

O auxiliar pode usar recursos eficientes da biblioteca padrão, mas nunca cria conhecimento puro, prova matemática ou verdade linguística.

## Hipótese própria pendente

A técnica de Pensador Sem Fronteiras que usa divisões por níveis, restos, transporte decimal e limite relacionado à raiz quadrada foi preservada em:

```text
matematica/hipoteses.py
conhecimento/HIPOTESE_DIVISAO_PRIMALIDADE_PSF.md
```

Ela está apenas guardada, sem investigação ativa. Hipóteses, teses, teorias, problemas pendentes e possível construção de axiomas serão retomados quando o motor estiver maduro. A ideia não substitui a primalidade PSF existente nem responde automaticamente a novos casos. Nos exemplos dados pelo autor, a mesma técnica é usada como teste: encontra divisores próprios em 9 e 12, concluindo que não são primos, e não encontra divisor próprio para 7 no percurso necessário, concluindo que 7 é primo.

## Regra sagrada principal

```text
Nunca fingir.
```

O PSF-IAminy não pode declarar conhecimento, prova, teste, cálculo ou conclusão que não esteja construído, materializado, validado ou marcado claramente como lacuna/hipótese.

## Conhecimento puro

O conhecimento do PSF deve ser construído por PSF, de modo fluido e natural, partindo do mínimo conhecimento possível e podendo crescer até o infinito.

Não deve usar dependências externas como fundamento.

## Monografia, pergunta, resposta, exercício e aula

Monografia, pergunta, resposta, exercício e aula são formas de apresentação, ensino, consolidação ou treino. Elas podem existir como saída futura, mas não são fundamento cego do conhecimento puro.

O PSF pode produzir monografia usando seu próprio conhecimento: ele reconstrói, desmistifica passo a passo, desmembra cálculos, fórmulas conhecidas, exercícios e argumentos, e marca o que ainda não consegue reconstruir. Resultado bonito/funcional não basta: o PSF precisa reconstruir como e porquê até a menor unidade disponível no domínio.

Quando o PSF recebe monografia pronta, a regra é: “se fosse eu, como reconstruiria isto?”. O conteúdo não entra como autoridade; entra como material a desmontar, comparar, validar ou marcar como lacuna.

Quando um ficheiro contém monografia, pergunta pronta, resposta pronta ou aula pronta, ele não deve ser tratado automaticamente como conhecimento puro. Ele deve ser removido, convertido em candidato auditável ou mantido apenas como mecanismo técnico não-fundacional quando necessário.

## Dependências

Dependências externas, quando existirem, só podem servir para:

```text
comparação
validação
medição de erro
otimização
apoio técnico
```

Elas não podem substituir a construção PSF.

## Linha única

O projeto segue regra de continuidade única:

```text
sem versões paralelas
sem etapas concorrentes
sem sobreposição
sem substituição escondida
```

Tudo entra no mesmo corpo do PSF-IAminy.

## Documentos oficiais

```text
README.md                 visão atual e coerência geral
COMO_RODAR.md             instruções mínimas de execução
REGRA_INTEGRIDADE.md      regras sagradas
REGRA_VERSAO_UNICA.md     continuidade única
PLANO_PSF_IAMINY.md       plano único crescente
RELATORIO_UNICO.md        relatório único do estado atual
```

## Estado preservado

Foi preservado:

```text
Matemática pura em conhecimento/ETAPA_*.md e nucleo/ quando testado/auditável
Português puro em lingua_portuguesa/ e conhecimento/PORTUGUES_CONHECIMENTO_PURO.md
núcleo
motor
motor de busca como mecanismo
validação externa como comparação
pasta privado/
privado/avalmath.docx
```

Foi removido da camada atual:

```text
conversas salvas
aulas prontas antigas
perguntas prontas antigas
respostas prontas antigas
baterias didáticas órfãs
relatórios temporários
auditorias e dossiês que não eram conhecimento puro
índices antigos de perguntas/respostas/problemas
monografias e resultados temporários que não eram conhecimento puro
módulos matemáticos antigos baseados em monografia/pergunta/resposta/aula pronta
log dados/auditoria_chat_vivo.jsonl
READMEs extras
conteúdo antigo de dados/base_canonica.jsonl
```

## Crescimento atual de Português

Português está materializado em **1141 conceitos puros numa única linha canónica**, com **2545 relações de dependência**, **1141 conceitos com exemplo mínimo**, **0 lacunas internas conhecidas**, **124 fronteiras abertas preservadas**, **179 limites de automatização separados** e **9 equivalências terminológicas sem duplicação**.

Os 20 temas continuam apenas como índices de consulta. Eles não são etapas, versões, bases paralelas, camadas de verdade nem autoridade sobre a ordem.

```text
conhecimento/LISTA_CONHECIMENTO_PORTUGUES.md
conhecimento/PORTUGUES_CONHECIMENTO_PURO.md
lingua_portuguesa/conhecimento_puro.py
```

O crescimento alcança, na mesma linha:

```text
fundamento mínimo: diferença, som, marca, grafema e relação
fonética articulatória, fonologia, traços distintivos, sílaba e prosódia
alfabeto, ortografia, acentuação, crase, abreviaturas, números e pontuação
morfema, raiz, radical, tema, derivação, composição, flexão e conjugação
classes lexicais, pronomes, verbos, locuções e processos de formação
sintagmas, constituintes, valência, funções sintáticas, concordância e regência
orações declarativas, interrogativas, exclamativas, imperativas e subordinadas
colocação pronominal, passivas, reflexivas, causativas, controlo e elevação
semântica lexical, relações de sentido, aspecto, modalidade, escopo e referência
pragmática, atos de fala, implicaturas, cortesia, turnos e reparação
coesão, coerência, parágrafo, argumentação, falácias, narração e literatura
variação, mudança linguística, alfabetização, letramento e aprendizagem
tradução, análise contrastiva, testes linguísticos e reconstrução PSF
```

Todos os conceitos possuem definição, função, dependências anteriores e exemplo mínimo. A expressão **sem lacunas internas** não significa que o português vivo seja fechado ou que o motor automatize tudo. O projeto separa honestamente:

```text
lacuna interna = falta dentro do conhecimento declarado; estado atual: zero conhecida
fronteira aberta = depende de variedade, contexto, comunidade, história ou evidência real
limite operacional = o conceito existe, mas a operação automática ainda pode ser parcial
```

O léxico interno reconhece **1702 lemas, 4119 formas e 4565 leituras**. O motor expõe busca, dependências diretas e transitivas, temas de consulta, fronteiras abertas, limites operacionais e verificação de mestria conceitual.

## Aproveitamento interno da Matemática no Português

A Matemática já construída pelo PSF passou a servir como ferramenta interna de validação e explicação do Português, sem virar fundamento linguístico.

```text
Português puro → define e constrói o conhecimento linguístico
Matemática PSF → audita, compara, organiza e verifica a estrutura
```

Foram aproveitados: relações, grafos, busca de caminhos, gramáticas formais finitas, reescrita e otimização finita. Isso permite:

```text
auditar as 1141 unidades e as 2545 dependências
detectar duplicações, dependências ausentes, dependências futuras e ciclos
encontrar uma cadeia mínima de dependências até um conceito
identificar conceitos estruturais com muitos dependentes
comparar padrões morfológicos com uma gramática formal finita
provar a reescrita de termo alternativo para termo canónico
escolher, por critério explícito, a leitura morfológica de maior confiança
```

A gramática matemática é apenas comparadora. Quando um padrão não é reconhecido, o resultado correto é `não coberto pelo modelo finito`, nunca `português inválido`. O ficheiro `lingua_portuguesa/conhecimento_puro.py` continua sem importar o núcleo matemático. A ponte fica isolada em `lingua_portuguesa/ponte_matematica.py`.

Auditoria estrutural atual:

```text
conceitos: 1141
relações diretas: 2545
raiz: diferença
duplicações: 0
dependências ausentes: 0
dependências futuras: 0
ciclos: 0
profundidade máxima conhecida: 27
```

## Rastreabilidade técnica do núcleo

Os módulos abaixo são preservados como motor, apoio técnico, legado testado, validação interna ou componente necessário. Eles não são automaticamente conhecimento puro de Matemática ou Português:

```text
nucleo/aprofundamento_provas.py
nucleo/autoidentidade_confianca.py
nucleo/base_curiosidades_reais.py
nucleo/calculo_discreto.py
nucleo/calculo_integral_avancado.py
nucleo/catalan_stirling.py
nucleo/cerebro_unico.py
nucleo/chat_auditoria.py
nucleo/chat_base_canonica.py
nucleo/chat_formatacao.py
nucleo/chat_rotas.py
nucleo/chat_rotas_auditoria.py
nucleo/chat_rotas_basicas.py
nucleo/chat_rotas_corretor.py
nucleo/chat_rotas_materializacao.py
nucleo/chat_rotas_resolvedores.py
nucleo/chat_texto.py
nucleo/chat_tipos.py
nucleo/chat_vivo.py
nucleo/cobertura_total_abertos.py
nucleo/combinadores.py
nucleo/combinatoria.py
nucleo/conceitos_avancados_puros.py
nucleo/divisores.py
nucleo/espaco_combinatorio_palavras.py
nucleo/geometria.py
nucleo/harmonicos.py
nucleo/indexador_total.py
nucleo/inteiros.py
nucleo/inversa_potencia.py
nucleo/laboratorio_cientifico.py
nucleo/modo_cientista.py
nucleo/motor_mestre.py
nucleo/numeros_figurados.py
nucleo/ordenacao_finita.py
nucleo/plano_mae.py
nucleo/politica_cobertura_total.py
nucleo/politica_definitividade.py
nucleo/ponte_comparador_python.py
nucleo/porcentagem.py
nucleo/predicados.py
nucleo/primos.py
nucleo/probabilidade.py
nucleo/problemas_abertos.py
nucleo/problemas_historicos_resolvidos.py
nucleo/proporcionalidade.py
nucleo/racionais.py
nucleo/reais.py
nucleo/roteador.py
nucleo/roteador_base_curiosidades.py
```

## Listas de conhecimento

```text
conhecimento/LISTA_CONHECIMENTO_PORTUGUES.md
conhecimento/LISTA_CONHECIMENTO_MATEMATICA.md
conhecimento/AUDITORIA_CURRICULO_EXTERNO_400_AULAS.md
conhecimento/AUDITORIA_CURRICULO_PORTUGUES_1000_AULAS.md
```

Essas listas são inventário do conhecimento materializado; não são aula pronta nem resposta pronta. As auditorias de currículo externo cruzam listas fornecidas pelo autor (Matemática: 1000 aulas em dois lotes, 1-400 e 401-1000; Português: 1000 aulas em 15 blocos) contra os conceitos reais do projeto — também não são aula pronta, é mapa de cobertura para orientar prioridade (ver `PLANO_PSF_IAMINY.md`, itens 262-274 e 303 para Matemática, item 305 para Português).

## Como verificar

```bash
cd PSF-IAminy
python3 verificar_integridade.py
python3 -m pytest -q
python3 motor_iaminy.py --rapido
```

Resultado atual esperado:

```text
660 passed
```

```text
verificar_integridade.py → APROVADO
pytest → todos os testes passam, incluindo a ponte Matemática–Português
motor_iaminy.py --rapido → sem pendências fatais
```

## Como rodar

```bash
python3 psf.py --pergunta "texto para analisar"
python3 psf_chat.py "texto para conversar"
```

Para abrir interface local:

```bash
python3 -m interface.servidor
```

Depois abrir:

```text
http://127.0.0.1:8765/
```

## O que falta

```text
aprofundar inventários fonéticos e variação de pronúncia sem fingir universalidade
construir famílias completas de ortografia, acentuação, hífen e divisão silábica
materializar paradigmas regulares e irregulares de flexão e conjugação
aprofundar sintaxe de clíticos, coordenação, subordinação e ordem dos constituintes
aprofundar semântica, pragmática e interpretação com evidência textual explícita
construir operações reais de revisão, leitura e produção textual sobre os conceitos puros
continuar limpeza fina da Matemática sem apagar conhecimento puro
```

## Regra curta

> O PSF-IAminy só cresce se continuar verdadeiro, puro, integrado e coerente.
