# PSF-IAminy — Etapa 74: Composição de funções

## Posição no fluxo natural

Esta etapa pertence ao bloco de relações e funções, que vem depois da combinatória inicial.

## Construção pura

Compor funções é aplicar uma depois da outra. A composição só nasce quando função e aplicação já existem.

## Exemplo

- `f = {(0,1),(1,2),(2,3)}` e `g = {(1,2),(2,3),(3,4)}`: a composta `g∘f` aplicada em `1` calcula `f(1)=2`, depois `g(2)=3` -- resultado `3`.

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
