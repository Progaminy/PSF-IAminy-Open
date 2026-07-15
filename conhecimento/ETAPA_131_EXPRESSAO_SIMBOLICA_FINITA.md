# PSF-IAminy — Etapa 131: Expressão simbólica finita

## Posição no fluxo natural

Esta etapa começa o bloco de expressões simbólicas, construído sobre corpo finito (etapa 94).

## Construção pura

Uma expressão é uma tupla aninhada com construtores CONST, VAR, SOMA_EXPR, SUB_EXPR, MULT_EXPR, POT_EXPR — uma árvore de sintaxe mínima, uma variável só, sobre um domínio já validado (naturais, ou um corpo finito como Z/5Z).

## Dependências permitidas

- distinção; igualdade; domínio finito explícito; corpo (etapas 91-94);
- corpo finito.

## Dependências proibidas nesta etapa

- múltiplas variáveis; equações de grau >= 2; raízes gerais;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/expressoes_simbolicas_finitas.py` e validado em `testes/test_expressoes_simbolicas_finitas.py`.
