# PSF-IAminy — Etapa 101: Polinómios sobre um anel

## Posição no fluxo natural

Esta etapa pertence ao bloco de polinómios e álgebra linear finita, que vem depois de corpo finito (etapa 94).

## Construção pura

Um polinómio sobre um anel é uma tupla finita de coeficientes (a0,a1,...,an), representando a0+a1x+...+anxⁿ. Nasce depois de anel (etapa 90) porque precisa de soma e produto já definidos para combinar os coeficientes.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- anel inicial.

## Dependências proibidas nesta etapa

- polinómios sobre corpos infinitos;
- espaços vetoriais de dimensão infinita;
- autovalores, autovetores, formas quadráticas;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_linear_inicial.py` e validado em `testes/test_algebra_linear_inicial.py`.
