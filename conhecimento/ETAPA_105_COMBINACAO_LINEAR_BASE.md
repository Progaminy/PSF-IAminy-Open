# PSF-IAminy — Etapa 105: Combinação linear e base

## Posição no fluxo natural

Esta etapa pertence ao bloco de polinómios e álgebra linear finita, que vem depois de corpo finito (etapa 94).

## Construção pura

Uma combinação linear de vetores v1..vk com escalares c1..ck é Σciвi. Uma base gera o espaço quando todo vetor do espaço é alguma combinação linear dela — verificado por busca exaustiva sobre um corpo finito pequeno, não por eliminação gaussiana geral.

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
