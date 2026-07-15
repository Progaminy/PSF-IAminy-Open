# PSF-IAminy — Etapa 108: Eliminação gaussiana finita

## Posição no fluxo natural

Esta etapa fecha o bloco de álgebra linear finita iniciado na etapa 104.

## Construção pura

Reduz uma matriz à forma escalonada: para cada coluna, acha um pivô não-nulo, normaliza-o para a unidade (usando o inverso multiplicativo do corpo, etapa 94) e elimina essa coluna das outras linhas. Funciona por cópia — nunca modifica a matriz de entrada.

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana já construída;
- matriz aplicação linear;
- corpo finito.

## Dependências proibidas nesta etapa

- corpos infinitos; decomposição LU/QR; valores singulares;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/eliminacao_gaussiana_finita.py` e validado em `testes/test_eliminacao_gaussiana_finita.py`.
