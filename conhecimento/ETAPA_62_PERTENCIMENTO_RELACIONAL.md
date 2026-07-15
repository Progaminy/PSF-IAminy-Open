# PSF-IAminy — Etapa 62: Pertencimento relacional

## Posição no fluxo natural

Esta etapa pertence ao bloco de relações e funções, que vem depois da combinatória inicial.

## Construção pura

O pertencimento relacional define quando um par ordenado é reconhecido dentro de uma relação. Isto permite escrever aRb sem inventar ainda função, ordem ou conjunto avançado.

## Exemplo

- Na relação `{(0,0),(1,1),(2,2),(0,2),(2,0)}`: o par `(0,2)` pertence; o par `(1,2)` não pertence.

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
