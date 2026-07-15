# PSF-IAminy — Etapa 69: Ordem total

## Posição no fluxo natural

Esta etapa pertence ao bloco de relações e funções, que vem depois da combinatória inicial.

## Construção pura

Ordem total é ordem parcial com comparabilidade completa: para todo par de elementos, um se relaciona ao outro em alguma direção.

## Exemplo

- A relação "menor ou igual" `{(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)}` sobre `{0,1,2}` é ordem total: todo par de `0,1,2` está comparado em alguma direção.

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
