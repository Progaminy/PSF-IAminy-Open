# PSF-IAminy

Português · [English](README.en.md)

[![CI](https://github.com/Progaminy/PSF-IAminy-Open/actions/workflows/ci.yml/badge.svg)](https://github.com/Progaminy/PSF-IAminy-Open/actions/workflows/ci.yml)

Sistema local do projeto Pensador Sem Fronteiras para conhecimento puro, investigação, organização e validação.

## Em poucos minutos

**O que é.** Um sistema que constrói conhecimento de Matemática e Português a partir do mínimo possível, por construção própria (PSF = "Pensador Sem Fronteiras"), em vez de citar bibliotecas, fórmulas prontas ou respostas de terceiros como fundamento.

**Problema que tenta resolver.** Sistemas que devolvem resultado pronto sem mostrar a construção nem admitir o que ainda não sabem escondem tanto erros quanto limites reais. O PSF-IAminy tenta o oposto: todo resultado carrega o caminho até ele (a "ponte" de dependências que o gerou), e o que ainda não foi construído fica marcado como lacuna, hipótese ou limite operacional — nunca escondido ou fingido (ver [Regra sagrada principal](#regra-sagrada-principal)).

**O que já funciona, com teste automatizado.**
- Matemática: resolve expressões racionais com precedência, reconstrói divisão por quociente/resto/fração/decimal, executa prova formal no fragmento lógico finito e distingue teste de prova universal — 203 documentos conceituais auditados, todos com dependências ligadas.
- Português: 1141 conceitos puros numa linha canónica, com exemplo mínimo e 0 lacunas internas conhecidas; léxico de 1702 lemas; análise morfológica, correção ortográfica e comparação gramatical finita.
- 1106 testes automatizados passam localmente (`python3 -m pytest -q`).

**O que ainda é experimental.**
- A hipótese própria de primalidade por divisão em níveis (`matematica/hipoteses.py`) está guardada, sem investigação ativa nem integração ao motor de primalidade existente.
- Português declara 124 fronteiras abertas e 179 limites operacionais: o conceito existe, mas a operação automática ainda pode ser parcial.
- A [primeira execução pública da CI](https://github.com/Progaminy/PSF-IAminy-Open/actions/runs/29505936596), no commit `e74740e`, falhou: timeout HTTP nos quatro Pythons e uso de `ast.TryStar` no Python 3.10. A árvore local já amplia a margem do teste e compatibiliza a AST, mas a matriz só será chamada de confirmada depois de um novo push verde. Instalação via `pip install -e .` já existe (comando `psf-iaminy`), mas ainda não há release publicada.

**Como rodar uma demonstração.**
```bash
git clone https://github.com/Progaminy/PSF-IAminy-Open.git
cd PSF-IAminy-Open
python3 -m pytest -q                 # 1106 passed
python3 exemplo_publico.py           # entrada, motor, rastreabilidade, limitação -- em segundos
```
Exemplos mais profundos por domínio: [`exemplos/matematica.py`](exemplos/matematica.py), [`exemplos/portugues.py`](exemplos/portugues.py), [`exemplos/rastreabilidade.py`](exemplos/rastreabilidade.py). Instruções completas (interface local, todos os motores): [`COMO_RODAR.md`](COMO_RODAR.md).

**Auditoria da preparação pública.** [`docs/AUDITORIA_MELHORIAS_120.md`](docs/AUDITORIA_MELHORIAS_120.md) acompanha os 64 pontos sem confundir trabalho técnico com adoção externa. [`docs/QUALIDADE_CODIGO.md`](docs/QUALIDADE_CODIGO.md) mede tipagem, exceções e duplicação de produção; [`docs/ROTEIRO_VIDEO_NARRACAO.md`](docs/ROTEIRO_VIDEO_NARRACAO.md) deixa pronta uma gravação reproduzível.

**Evidência visual real.** [`docs/IMAGENS.md`](docs/IMAGENS.md) reúne a interface inicial, uma entrada e resposta reais com origem/limite explícito, o mapa de conhecimento, a área de ensino e a prévia da página estática. As capturas usam armazenamento temporário isolado e não contêm conversas persistentes do utilizador.

**Por que a abordagem é diferente.** A maioria dos sistemas de IA usa bibliotecas e modelos prontos como fundamento de verdade. O PSF-IAminy proíbe isso por regra sagrada (`REGRA_INTEGRIDADE.md`): dependências externas só podem comparar, validar ou otimizar — nunca ser fonte do conhecimento. Cada conceito matemático ou linguístico precisa de uma ponte explícita até conhecimento anterior; sem ponte, não é conhecimento PSF.

A filosofia completa, a arquitetura dos motores e o estado detalhado de cada área continuam abaixo.

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

## PSF-Calculadora (`cao_de_caca/`)

`cao_de_caca/PSF-Calculadora/` é um **subprojeto separado**, não conhecimento PSF: uma calculadora de terminal em português (própria `pyproject.toml`, próprio comando `psf-calculadora`, própria suíte de testes) que abusa de propósito de dependências científicas — NumPy, SciPy, SymPy, Pandas, Matplotlib, NetworkX, mpmath, scikit-learn — para cobrir 353 motores de cálculo em 33 assuntos (aritmética, álgebra, geometria, cálculo, estatística, otimização, sinais e outros).

O nome vem da regra que o define: é o "cão de caça" do projeto — vai buscar valor exato, otimizado ou comparação no mundo livre de bibliotecas prontas, e traz de volta, mas nunca entra como fundamento do conhecimento PSF. Por isso:

- fica **fora da coleta padrão de testes** (`pytest.ini` define `testpaths = testes`; o subprojeto roda sua própria suíte de dentro da sua pasta);
- o motor principal decide sozinho, por 4 perguntas explícitas (`motor/decisao_auxiliar.py`: preciso comparar? preciso de valor exato/otimizado? preciso de dependência externa? o assunto é reconhecido?), quando vale a pena consultá-lo;
- o mapa de conhecimento (`interface/mapa_cao_de_caca.py`) o cataloga com **zero arestas e zero pontes** para Matemática ou Português — decisão explícita do autor: é ferramenta de cálculo, não conhecimento PSF.

Ver `cao_de_caca/PSF-Calculadora/README.md` para instalação e uso próprios.

## Hipótese própria pendente

A técnica de Pensador Sem Fronteiras que usa divisões por níveis, restos, transporte decimal e limite relacionado à raiz quadrada foi preservada em:

```text
matematica/hipoteses.py
conhecimento/HIPOTESE_DIVISAO_PRIMALIDADE_PSF.md
```

Ela está apenas guardada, sem investigação ativa. Hipóteses, teses, teorias, problemas pendentes e possível construção de axiomas serão retomados quando o motor estiver maduro. A ideia não substitui a primalidade PSF existente nem responde automaticamente a novos casos. Nos exemplos dados pelo autor, a mesma técnica é usada como teste: encontra divisores próprios em 9 e 12, concluindo que não são primos, e não encontra divisor próprio para 7 no percurso necessário, concluindo que 7 é primo.

## Capacidades reais e limitações

Tabela de capacidades centrais, cada uma com teste automatizado que a sustenta. Não é a lista completa de conhecimento construído (isso está em `conhecimento/LISTA_CONHECIMENTO_MATEMATICA.md` e `conhecimento/LISTA_CONHECIMENTO_PORTUGUES.md`); é uma amostra verificável para quem chega agora ao projeto.

| Capacidade | Estado | Teste | Limitação |
| --- | --- | --- | --- |
| Resolução de expressões racionais com precedência | Implementada | `testes/test_motores_dominio_comum.py::test_motor_matematica_resolve_precedencia_sem_cortar_expressao` | Domínio racional não negativo |
| Divisão reconstruída (quociente, resto, fração, decimal) | Implementada | `testes/test_motores_dominio_comum.py::test_divisao_racional_e_decimal_sao_reconstruidas_sem_magia` e `test_divisao_periodica_preserva_fracao_e_controla_precisao` | Divisão por zero fica não definida por construção — não é erro nem problema aberto |
| Prova formal no fragmento lógico finito | Implementada | `testes/test_motores_dominio_comum.py::test_motor_matematica_prova_finita_certificada` | Restrita ao fragmento lógico finito já construído |
| Adição | Implementada | `testes/test_adicao.py` (5 testes) | Naturais/inteiros conforme o motor |
| Segmentação morfológica (prefixo+radical+sufixo) | Parcial | `testes/test_morfemas_afixais.py` (9 testes), `testes/test_morfologia_derivacional.py` (37 testes) | Só reconhece radical já existente como entrada própria no léxico; vocabulário limitado aos 1702 lemas internos |
| Correção ortográfica | Implementada | `testes/test_corretor.py`, `testes/test_corretor_integracao.py` | Léxico e candidatos internos; nenhum dicionário externo como fundamento |
| Motor auxiliar de validação e otimização | Implementado | `testes/test_motores_dominio_comum.py::test_motor_auxiliar_*` (5 testes) | Nunca decide conhecimento; só compara, mede e cacheia |
| Hipótese de primalidade por divisão em níveis | Experimental, não integrada | `testes/test_motores_dominio_comum.py::test_hipotese_do_autor_fica_pendente_e_nao_vira_primalidade_pronta` (confirma que fica pendente, não que a hipótese está provada) | Guardada sem investigação ativa; não substitui a primalidade PSF existente nem responde a novos casos automaticamente |

O projeto separa o que afirma em cinco categorias, para que nenhuma seja confundida com as outras:

- **Conhecimento implementado**: tem código, teste e ponte de dependências fechada — exemplos na tabela acima e em `conhecimento/ETAPA_*.md`.
- **Experimentos**: construções recentes ainda em ajuste, já testadas mas não necessariamente estáveis (ver entradas mais recentes de `PLANO_PSF_IAMINY.md`).
- **Hipóteses**: ideias autorais preservadas com autoria, exemplos e contraexemplos, sem entrar como conhecimento puro até prova ou falsificação — caso único hoje: `matematica/hipoteses.py` e `conhecimento/HIPOTESE_DIVISAO_PRIMALIDADE_PSF.md`, acima.
- **Problemas pendentes**: questões declaradas em aberto, sem prova fingida — `nucleo/problemas_abertos.py` fixa enunciado, dependências e plano de investigação, nunca uma solução.
- **Validação externa**: `validacao_externa/` (o `MotorAuxiliarValidacao` desta seção) compara, mede e cacheia contra outras implementações, mas nunca decide conhecimento puro nem serve de fundamento.

Limitações que o projeto reconhece abertamente:

- O motor de Matemática cobre um domínio racional finito; não afirma completude sobre os reais (ver ETAPA_1035, ainda pendente de equivalência/ordem entre leis geradoras).
- O domínio funcional não implica escala: na avaliação local, `20*20` terminou em 0,215 s, mas `99*99` excedeu 10 s devido às construções por retirada/predecessor (`docs/LIMITES_OPERACIONAIS.md`).
- Português declara **124 fronteiras abertas** (dependem de variedade, contexto, comunidade ou evidência real) e **179 limites operacionais** (o conceito existe, mas a automação ainda pode ser parcial) — nenhum dos dois é tratado como lacuna a esconder.
- A avaliação linguística pública inicial encontrou sugestões indevidas para 4 de 8 palavras válidas numa amostra pequena (50% nessa amostra, não estimativa geral); o corretor permanece consultivo e parcial. Ver `docs/AVALIACAO_QUALIDADE.md`.
- Cobertura de testes medida localmente em 63% (ver `docs/COBERTURA.md` para o detalhe por módulo). A primeira comparação externa matemática obteve 7/7 concordâncias com SymPy 1.14.0 numa amostra pequena; validação sistemática ampla e comparação linguística continuam pendentes (`docs/VALIDACAO_EXTERNA.md`).
- `dados/base_canonica.jsonl` foi esvaziado deliberadamente (ver `COMO_RODAR.md`); o chat responde de forma mais limitada até a base pura ser reconstruída por materialização PSF.

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
README.en.md              apresentação pública essencial em inglês
CONTRIBUTING.en.md        guia de contribuição em inglês
COMO_RODAR.md             instruções mínimas de execução
REGRA_INTEGRIDADE.md      regras sagradas
REGRA_VERSAO_UNICA.md     continuidade única
PLANO_PSF_IAMINY.md       plano único crescente
RELATORIO_UNICO.md        relatório único do estado atual
CHANGELOG.md              mudanças da edição pública, por versão
ROADMAP.md                prioridades públicas: agora, próximo, depois e investigação
CODE_OF_CONDUCT.md        regras de convivência e aplicação nos espaços do projeto
GOVERNANCE.md             critérios públicos de decisão, aceitação e release
AUTHORS.md                autoria, licença, conteúdo excluído e forma de citação
CITATION.cff              metadados legíveis por plataformas de citação
REFERENCIAS.md            fontes internas e protocolo para referências externas
docs/ARQUITETURA.md       diagrama e descrição de cada componente
docs/en/                  arquitetura, segurança, roadmap, demonstração e release em inglês
docs/NOTA_CIENTIFICA.md   problema, hipótese, metodologia e limitações
docs/COBERTURA.md         cobertura de testes medida, por módulo
docs/AUDITORIA_SEGURANCA.md   o que foi auditado, corrigido e o que continua como risco não testado
docs/POLITICA_DADOS.md    o que é guardado localmente, onde, por quanto tempo e como apagar
docs/RELEASE.md           notas e checklist da primeira release candidata
docs/COMPATIBILIDADE.md   versões, sistemas e estabilidade das interfaces
docs/DEPENDENCIAS.md      finalidade, separação e riscos das dependências
docs/TESTES.md            classificação reproduzível, concentração e limites da suíte
docs/DESEMPENHO.md        linha de base de tempo, inicialização e memória rastreada
docs/AVALIACAO_QUALIDADE.md   casos matemáticos/linguísticos, resultados e erros observados
docs/VALIDACAO_EXTERNA.md     comparadores, versões, concordâncias, divergências e limites
docs/REPRODUCAO.md         instalação, CLI, demonstração e suíte numa cópia limpa
docs/ANALISE_ESTATICA.md   resultados Ruff/Bandit, correções e dívida triada
docs/LIMITES_OPERACIONAIS.md   números, expressões, texto, HTTP e limites não avaliados
docs/ISSUES_PLANEJADAS.md   backlog pronto; ainda não publicado por falta de permissão de escrita
docs/IMAGENS.md           capturas reais, proveniência e limites da evidência visual
docs/CANDIDATURA.md       pacote factual para eventual atualização autorizada
docs/DIVULGACAO.md        texto técnico honesto, ainda não publicado externamente
site/                     fonte estática da página pública, ainda pendente de deploy
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
ficheiros privados não incluídos na edição pública
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
pasta privado/ (só continha um marcador estrutural, sem conteúdo pessoal real; removida por decisão do autor)
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
1106 passed na verificação local mais recente
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
