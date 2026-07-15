# PSF-IAminy — Etapa 80: Fechamento relacional-funcional inicial

## Posição no fluxo natural

Esta etapa pertence ao bloco de relações e funções, que vem depois da combinatória inicial.

## Construção pura

Este fechamento confirma o ciclo: relação binária permite propriedades; propriedades permitem equivalência e ordem; relação especial permite função.

## Exemplo

- Sobre o domínio `{0,1,2}`, o fechamento confirma de ponta a ponta: a relação de equivalência `{(0,0),(1,1),(2,2),(0,2),(2,0)}`, a ordem total "≤" e a função `f={(0,1),(1,2),(2,3)}` (com sua inversa, imagem e composição) todas passam pelas mesmas checagens já construídas nesta etapa.

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
