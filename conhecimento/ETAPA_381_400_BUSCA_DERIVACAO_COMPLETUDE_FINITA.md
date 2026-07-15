# PSF-IAminy — Etapas 381 a 400: Verificação diagnóstica, solidez, busca de derivação por enumeração finita e completude relativa

## Posição no fluxo natural

A etapa 361-380 fechou prova de primeira ordem como objeto finito verificável
(sequente, regra como transição, derivação) mas deixou três dívidas
explícitas no seu "Próximo passo natural": um verificador com diagnóstico
por passo, confirmação de que as regras registadas são SÓLIDAS (preservam
satisfação, não só sintaticamente bem-formadas) e busca de derivação por
enumeração finita — a etapa 386 prometida lá. Esta etapa fecha essas três
dívidas e, com elas, o arco lógico 341-400.

```text
prova de primeira ordem como objeto finito (361-380)
↓
verificador com diagnóstico passo-a-passo
↓
solidez (soundness) de cada regra sobre uma amostra semântica
↓
estado de busca / passo de busca / poda
↓
busca de derivação por enumeração finita, profundidade limitada
↓
completude relativa a um fragmento decidível
↓
limite honesto de completude fora do fragmento
↓
consistência, independência, comprimento, comparação de estratégias
↓
fechamento do arco lógico 341-400
```

## Dependências permitidas

- `nucleo/teoria_modelos_prova_finita.py` inteiro (etapas 361-380):
  `SEQUENTE_FINITO`, `PREMISSAS_DE`, `CONCLUSAO_DE`, `PASSO_DERIVACAO`,
  `PASSO_VALIDO`, `DERIVACAO_VALIDA`, `CONCLUSAO_FINAL_DA_DERIVACAO`.
- `nucleo/logica_predicados_finita.py` (etapas 341-360): `ESTRUTURA_FINITA`,
  `SATISFAZ_FINITA`, `ATOMICA`.
- `nucleo/metodos_finitos.py` (etapa 275, lógica proposicional finita):
  `PROP_VAR`, `PROP_E`, `PROP_OU`, `PROP_IMPLICA`, `AVALIAR_PROP_FINITA`,
  `VALORACOES_PROP_FINITA`, `VARIAVEIS_PROP_FINITA`, `CONSEQUENCIA_FINITA`
  — usado como ORÁCULO semântico independente para validar a busca, exatamente
  como já foi usado na etapa 376.

## Dependências proibidas

- nenhum SAT-solver, motor de unificação ou provador automático importado;
- `DIV`, `MOD`, `MDC`, `MMC` nativos, módulos antigos `primos`/`divisores`;
- busca irrestrita sobre fórmulas arbitrárias — toda busca aqui é limitada a
  um conjunto FINITO e explícito de subfórmulas (ver "fragmento" abaixo).

## O fragmento pesquisado (decisão de escopo, declarada, não escondida)

`BUSCA_DERIVACAO_FINITA` só encadeia `premissa`, `modus_ponens`, `e_intro`,
`e_elim_esq`, `e_elim_dir` e `ou_intro` — as regras cuja aplicabilidade pode
ser decidida sem abrir uma sub-derivação hipotética. `implica_intro`,
`ou_elim`, `para_todo_intro`, `para_todo_elim`, `existe_intro`,
`existe_elim` continuam apenas VERIFICÁVEIS (etapa 373-378), não
pesquisadas automaticamente aqui — buscá-las exigiria sub-derivações sob
hipótese, adiado para além da etapa 400. Isto restringe a busca ao
fragmento positivo (∧, ∨-introdução, → só por modus ponens, sem
negação) — o mesmo fragmento por trás de encadeamento progressivo
("forward chaining") sobre cláusulas de Horn proposicionais, um
procedimento de decisão clássico e completo para esse fragmento
(consequência de cláusulas de Horn é decidível em tempo linear pelo
algoritmo de marcação — facto padrão de lógica computacional).

## Etapas registadas

| Etapa | Conceito |
|---|---|
| 381 | Verificador de derivação com diagnóstico passo-a-passo (não só V/F agregado) |
| 382 | Solidez (soundness) de regra proposicional sobre amostra exaustiva de valorações |
| 383 | Solidez (soundness) de regra de quantificador sobre amostra de estruturas finitas |
| 384 | Validação cruzada: toda regra registada em `PASSO_VALIDO` é sólida |
| 385 | Estado de busca finito (hipóteses, conjunto-alvo fechado sob subfórmula, provados, passos) |
| 386 | Passo de busca: uma rodada de encadeamento progressivo sobre o estado |
| 387 | Poda: nunca reprocessar uma fórmula já provada (fecho finito garante término) |
| 388 | Busca de derivação por enumeração finita (`BUSCA_DERIVACAO_FINITA`) |
| 389 | Testemunha construída: a derivação devolvida é reconstruída e re-verificável, não uma afirmação de existência |
| 390 | Fechamento da busca de derivação (385-390) |
| 391 | Completude relativa: comparação exaustiva busca vs. oráculo semântico sobre teorias de Horn geradas por um catálogo finito de cláusulas |
| 392 | Completude do fragmento de Horn proposicional (mesma comparação, expressa como taxa de acerto 1/1) |
| 393 | Limite honesto: contraexemplo real fora do fragmento (∨-eliminação necessária) onde a busca falha e o oráculo confirma que a fórmula era mesmo consequência |
| 394 | Consistência de uma teoria finita: ausência de derivação de contradição dentro do fecho de busca |
| 395 | Independência de premissa: remover uma premissa necessária derruba a consequência semântica |
| 396 | Comprimento de derivação e derivação mínima entre alternativas |
| 397 | Comparação de estratégias: profundidade limitada vs. busca até ponto fixo |
| 398 | Correção do buscador: toda derivação que ele devolve passa por `DERIVACAO_VALIDA` |
| 399 | Aplicação de ponta a ponta: consequência de {p,p→q,q→r,q→s} encontrada sem passos manuais |
| 400 | Fechamento do arco lógico 341-400 |

## Forma operacional no projeto

Implementado em `nucleo/busca_prova_finita.py` e validado em
`testes/test_busca_prova_finita.py`.

## Validação contra factos independentes

1. **Algoritmo de marcação para cláusulas de Horn é decidível e completo**
   (facto padrão de lógica computacional/ciência da computação — a base do
   Datalog e da resolução SLD restrita a Horn). Testado exaustivamente: um
   catálogo fixo de 5 cláusulas candidatas (`p`, `q`,
   `p→q`, `q→r`, `(p∧q)→r`) gera 2⁵ = 32 teorias possíveis; cruzadas com 3
   metas possíveis (`p`,`q`,`r`), são 96 combinações — em TODAS,
   `BUSCA_DERIVACAO_FINITA` concorda com `CONSEQUENCIA_FINITA` (o oráculo já
   validado na etapa 275).
2. **Contraexemplo real de incompletude fora do fragmento**: de
   `{p∨q, p→r, q→r}` segue `r` semanticamente (prova por casos / eliminação
   do ∨) — `CONSEQUENCIA_FINITA` confirma. `BUSCA_DERIVACAO_FINITA`, que não
   pesquisa `ou_elim` automaticamente, corretamente NÃO encontra uma
   derivação — o limite é do buscador, não da lógica.
3. **Toda derivação devolvida pela busca é re-verificada por
   `DERIVACAO_VALIDA`** (a mesma função de verificação da etapa 379,
   escrita independentemente do algoritmo de busca) — solidez do buscador
   confirmada por um verificador que não compartilha código com ele.

## Limite honesto

- A busca cobre só o fragmento positivo (∧, ∨-introdução, →-eliminação);
  `implica_intro`, `ou_elim` e as regras de quantificador continuam só
  verificáveis manualmente (etapas 373-378), não pesquisadas.
- "Profundidade limitada" aqui é o fecho de um conjunto FINITO e explícito
  de subfórmulas de `gamma ∪ {chi}` — não uma busca sobre todas as fórmulas
  possíveis (que seria infinita). Fórmulas fora desse fecho nunca são
  consideradas, mesmo que ajudassem.
- A solidez (etapas 382-383) é testada sobre amostras — exaustiva quando o
  domínio é pequeno (valorações proposicionais), amostral quando envolve
  estruturas de primeira ordem (mesma fronteira honesta já registada em
  `EQUIVALENCIA_ELEMENTAR_FINITA`, etapa 368).

## Próximo passo natural

```text
verificação de passos que abrem hipótese (implica_intro, ou_elim) dentro da busca
↓
máquina de estados finita com memória limitada (fita/registador explícito)
↓
função computável finita e decidibilidade de propriedades finitas
↓
gramáticas formais finitas e a hierarquia de Chomsky revisitada
```
