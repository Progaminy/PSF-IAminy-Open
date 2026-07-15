# PSF-IAminy — Etapa 65: Transitividade

## Posição no fluxo natural

Esta etapa pertence ao bloco de relações e funções, que vem depois da combinatória inicial.

## Construção pura

Uma relação é transitiva quando aRb e bRc obrigam aRc. Aqui nasce a ideia de passagem estrutural.

## Exemplo

- Na relação `{(0,0),(1,1),(2,2),(0,2),(2,0)}`: `(0,2)` e `(2,0)` estão presentes, e `(0,0)` (a passagem exigida) também está -- transitiva.

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
