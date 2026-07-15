# PSF-IAminy — Etapa 104: Espaço vetorial finito inicial

## Posição no fluxo natural

Esta etapa pertence ao bloco de polinómios e álgebra linear finita, que vem depois de corpo finito (etapa 94).

## Construção pura

Um vetor é uma tupla de escalares de um corpo já validado (etapa 94). A soma de vetores e o produto escalar×vetor nascem diretamente das operações do corpo — os oito axiomas de espaço vetorial seguem das propriedades de corpo já confirmadas, não precisam de nova prova.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- corpo finito.

## Dependências proibidas nesta etapa

- polinómios sobre corpos infinitos;
- espaços vetoriais de dimensão infinita;
- autovalores, autovetores, formas quadráticas;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_linear_inicial.py` e validado em `testes/test_algebra_linear_inicial.py`.
