# PSF-IAminy — Etapa 70: Função como relação especial

## Posição no fluxo natural

Esta etapa pertence ao bloco de relações e funções, que vem depois da combinatória inicial.

## Construção pura

Função não é primitiva. É uma relação em que cada entrada do domínio possui exatamente uma saída. Esta etapa impede fingir função antes de relação.

## Exemplo

- `f = {(0,1),(1,2),(2,3)}` sobre o domínio `{0,1,2}` é funcional (cada entrada tem exatamente uma saída) e total no domínio -- é função. Já `{(0,1),(0,2)}` (duas saídas para a entrada `0`) não é funcional.

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
