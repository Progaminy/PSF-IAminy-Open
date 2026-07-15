# PSF-IAminy — Etapas 681 a 700: Análise sintática finita

**Análise sintática** (parsing) é o processo inverso da geração: dada
uma string e uma gramática (ETAPA 601-640), decidir se a string
pertence à linguagem da gramática e, se sim, reconstruir a árvore de
derivação que a gera. É o que transforma texto solto em estrutura
verificável — a mesma ideia por trás de "essa expressão matemática está
bem formada?" ou "essa frase segue a gramática da língua?". Este bloco
constrói esse processo sobre gramáticas finitas, sem ambiguidade
escondida.

## Exemplo

- `"2+3*4"` é analisada respeitando precedência: a árvore fica `2 + (3×4)`, não `(2+3)×4` -- avaliada dá `14`, não `20`.
- `"(())()"` tem parênteses balanceados (aceito); `"(()"` tem parênteses desbalanceados (rejeitado).

## Posição no fluxo natural

Este bloco continua a partir da etapa 680. Ele não salta para conceitos futuros: constrói apenas o próximo arco natural e mantém todos os limites declarados.

```text
conceito anterior
↓
análise sintática finita
↓
validação finita por catálogo/teste
```

## Regra de pureza

Não usa como dependência:

- divisão nativa, resto nativo ou aritmética modular escondida;
- primalidade, fatoração ou módulos antigos de divisores;
- infinitos atuais ou equivalência universal sem fronteira;
- teoremas futuros ainda não construídos.

## Etapas registadas

| Etapa | Conceito |
|---|---|
| 681 | tokenização finita |
| 682 | token de número |
| 683 | token de operador |
| 684 | token de parêntese |
| 685 | fim de entrada |
| 686 | lexer aritmético finito |
| 687 | parser descendente |
| 688 | expressão |
| 689 | termo |
| 690 | fator |
| 691 | precedência multiplicativa |
| 692 | associatividade à esquerda |
| 693 | AST aritmética |
| 694 | parse de texto |
| 695 | verificação de parênteses |
| 696 | erro sintático |
| 697 | tabela LL(1) mínima |
| 698 | pipeline léxico-sintático |
| 699 | pipeline sintaxe-tipo-valor |
| 700 | fechamento do arco 481-700 |

## Forma operacional no projeto

Implementado em `nucleo/analise_sintatica_finita.py` e validado em `testes/test_analise_sintatica_finita.py`.

## Validação externa mínima

O módulo é testado contra exemplos independentes e catálogos finitos. Quando a afirmação seria universal ou infinita, o documento declara a fronteira em vez de fingir prova geral.

## Limite honesto

A etapa 700 fecha apenas este arco finito. O próximo bloco deve nascer explicitamente no fluxo, sem usar o que ainda não foi construído.
