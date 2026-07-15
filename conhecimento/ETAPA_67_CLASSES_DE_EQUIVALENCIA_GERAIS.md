# PSF-IAminy — Etapa 67: Classes de equivalência gerais

## Posição no fluxo natural

Esta etapa pertence ao bloco de relações e funções, que vem depois da combinatória inicial.

## Construção pura

A classe de um elemento é o conjunto finito dos elementos que se relacionam com ele por uma equivalência. Assim nasce a ideia de agrupar por estrutura comum.

## Exemplo

- Na equivalência `{(0,0),(1,1),(2,2),(0,2),(2,0)}` sobre `{0,1,2}`, a classe de `0` é `{0,2}` (os elementos que se relacionam com `0`).

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- relação finita;
- lógica booleana já construída.

## Dependências proibidas nesta etapa

- cálculo diferencial ou integral;
- topologia;
- cardinalidade infinita;
- álgebra abstrata avançada;
- análise real;
- probabilidade;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/relacoes_funcoes_naturais.py` e validado em `testes/test_relacoes_funcoes_naturais.py`.
