# PSF-IAminy — Etapa 99: Classes laterais

## Posição no fluxo natural

Esta etapa pertence ao segundo bloco de estruturas algébricas, que vem depois de grupo e anel inicial (etapas 86-90).

## Construção pura

A classe lateral (à esquerda) de um elemento a em relação a um subgrupo H é {a∘h : h∈H}. As classes laterais particionam o grupo inteiro em blocos do mesmo tamanho — é a base do Teorema de Lagrange (|H| divide |G|), confirmado operacionalmente: |G|=6, |H|=3, exatamente 2 classes laterais.

## Exemplo

- `H={0,2,4}` em `(ℤ/6ℤ,+mod6)`: as classes laterais são `{0,2,4}` (a própria `H`) e `{1,3,5}` -- exatamente `2` classes, e `6/3=2` confirma o Teorema de Lagrange.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- subgrupo.

## Dependências proibidas nesta etapa

- corpos infinitos, extensões de corpo;
- espaços vetoriais, módulos;
- categoria, teoria de Galois;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_estruturas_ii.py` e validado em `testes/test_algebra_estruturas_ii.py`.
