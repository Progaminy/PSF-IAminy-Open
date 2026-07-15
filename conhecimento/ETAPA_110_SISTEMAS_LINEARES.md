# PSF-IAminy — Etapa 110: Sistemas lineares finitos

## Posição no fluxo natural

Esta etapa fecha o bloco de álgebra linear finita iniciado na etapa 104.

## Construção pura

Resolve Ax=b por eliminação sobre a matriz aumentada [A|b]. Devolve a solução quando o sistema é determinado; None quando é impossível (linha 0=c≠0 aparece) ou indeterminado (posto menor que o número de incógnitas) — esta etapa não parametriza soluções infinitas, só resolve o caso determinado.

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana já construída;
- eliminação gaussiana;
- posto matriz.

## Dependências proibidas nesta etapa

- corpos infinitos; decomposição LU/QR; valores singulares;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/eliminacao_gaussiana_finita.py` e validado em `testes/test_eliminacao_gaussiana_finita.py`.
