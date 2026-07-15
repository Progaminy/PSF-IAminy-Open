# PSF-IAminy — Etapas 441 a 480: Gramáticas formais finitas

## Posição no fluxo natural

O arco 401-440 construiu computabilidade finita: máquinas de fita limitada,
funções computáveis finitas e decidibilidade em domínio finito. O próximo
conceito natural é perguntar o que essas máquinas processam: **linguagens**.

A linguagem formal nasce sem fingimento por esta cadeia:

```text
alfabeto finito
↓
palavra finita
↓
símbolo terminal / não-terminal
↓
produção
↓
forma sentencial
↓
derivação finita
↓
linguagem gerada até profundidade declarada
↓
gramática regular e DFA equivalente no catálogo finito
↓
gramática livre de contexto e autômato de pilha finito
```

Nada aqui afirma propriedades infinitas gerais. Tudo é validado em catálogos
finitos, com profundidade, tamanho de pilha e passos declarados.

## Dependências permitidas

- primitivas fundacionais `V` e `F`;
- `DFA_FINITO` e `ACEITA_DFA_FINITO` de `nucleo/metodos_finitos.py`, já
  nascidos no bloco 136-300;
- computabilidade finita como motivação anterior, sem importar o módulo de
  máquina de fita para não misturar modelos.

## Dependências proibidas

- `DIV`, `MOD`, `MDC`, `MMC` nativos;
- módulos antigos `primos` e `divisores`;
- infinitos atuais, cardinalidade infinita e linguagem formal geral sem
  limite de derivação;
- equivalências universais sem catálogo ou fronteira declarada.

## Etapas registadas

| Etapa | Conceito |
|---|---|
| 441 | Alfabeto gramatical finito |
| 442 | Palavra gramatical finita |
| 443 | Separação terminal / não-terminal |
| 444 | Símbolo inicial |
| 445 | Produção finita |
| 446 | Gramática finita |
| 447 | Forma sentencial inicial |
| 448 | Derivação de um passo |
| 449 | Derivação até profundidade finita |
| 450 | Palavra vazia / epsilon |
| 451 | Linguagem gerada até profundidade declarada |
| 452 | Derivabilidade finita de uma palavra |
| 453 | Gramática regular linear à direita |
| 454 | Tradução de gramática regular para DFA |
| 455 | Concordância gramática-DFA em catálogo finito |
| 456 | União finita de gramáticas |
| 457 | Concatenação finita de gramáticas regulares |
| 458 | Estrela de Kleene limitada |
| 459 | Fechamento das gramáticas regulares finitas |
| 460 | Limite honesto: regularidade geral não é assumida fora do fragmento declarado |
| 461 | Produção livre de contexto finita |
| 462 | Árvore de derivação finita |
| 463 | Folhas de árvore de derivação |
| 464 | Gramática de parênteses balanceados como exemplo livre de contexto |
| 465 | Pilha finita explícita |
| 466 | Configuração de autômato de pilha finito |
| 467 | Transição com leitura opcional e topo da pilha |
| 468 | Execução não-determinística limitada |
| 469 | Aceitação por estado final em autômato de pilha finito |
| 470 | Reconhecedor de parênteses balanceados por pilha |
| 471 | Concordância gramática-pilha em catálogo finito |
| 472 | Diferença entre DFA e pilha demonstrada em exemplo finito |
| 473 | Limite de pilha como fronteira explícita |
| 474 | Limite de passos como fronteira explícita |
| 475 | Catálogo finito de palavras como oráculo externo de comparação |
| 476 | Fechamento de gramáticas livres de contexto finitas |
| 477 | Limite honesto: não há prova universal de equivalência CFG-PDA geral aqui |
| 478 | Linguagem formal finita como objeto auditável |
| 479 | Síntese do arco 441-480 |
| 480 | Fechamento do arco de gramáticas formais finitas |

## Forma operacional no projeto

Implementado em `nucleo/gramaticas_finitas.py` e validado em
`testes/test_gramaticas_finitas.py`.

## Validação contra factos independentes

1. A gramática regular `S → aS | b` gera exatamente palavras do tipo `a*b`
   dentro da profundidade declarada. O DFA traduzido aceita `aaab` e rejeita
   `aba`, usando o verificador de DFA já existente em `metodos_finitos.py`.
2. A gramática `S → ε | (S)S` gera parênteses balanceados em profundidade
   finita. O autômato de pilha finita reconhece o mesmo catálogo testado,
   aceitando `()`, `(())` e rejeitando `())`.
3. A auditoria de pureza confirma que o novo módulo não importou primalidade,
   divisores, divisão, módulo ou aritmética modular.

## Limite honesto

- `PALAVRAS_GERADAS_ATE_FINITO` depende de uma profundidade declarada. Não
  enumera linguagem infinita inteira.
- `GRAMATICA_REGULAR_PARA_DFA_FINITO` cobre apenas gramática linear à direita
  no formato `A → aB`, `A → a` ou `A → ε`.
- A equivalência gramática-DFA e gramática-pilha é conferida sobre catálogo
  finito. A equivalência geral clássica fica para uma etapa futura com prova
  própria.

## Próximo passo natural

```text
semântica operacional de linguagens formais finitas
↓
parser descendente limitado
↓
árvore sintática abstrata finita
↓
interpretação de linguagem formal simples
↓
ponte para compiladores finitos
```
