# PSF-IAminy — Etapa 106: Matriz como aplicação linear finita

## Posição no fluxo natural

Esta etapa pertence ao bloco de polinómios e álgebra linear finita, que vem depois de corpo finito (etapa 94).

## Construção pura

Uma matriz é uma tupla de tuplas (linhas); aplicá-la a um vetor é o produto matriz-vetor usual, calculado só com soma e produto do corpo subjacente.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- espaço vetorial finito.

## Dependências proibidas nesta etapa

- polinómios sobre corpos infinitos;
- espaços vetoriais de dimensão infinita;
- autovalores, autovetores, formas quadráticas;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_linear_inicial.py` e validado em `testes/test_algebra_linear_inicial.py`.
