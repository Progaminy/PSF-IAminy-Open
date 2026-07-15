# PSF-IAminy — Etapa 79: Imagem e pré-imagem

## Posição no fluxo natural

Esta etapa pertence ao bloco de relações e funções, que vem depois da combinatória inicial.

## Construção pura

Imagem é o conjunto finito das saídas atingidas; pré-imagem é o conjunto finito das entradas que atingem uma saída.

## Exemplo

- Para `f = {(0,1),(1,2),(2,3)}`: a imagem de `f` é `{1,2,3}`; a pré-imagem de `2` é `{1}` (só `1` mapeia para `2`).

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
