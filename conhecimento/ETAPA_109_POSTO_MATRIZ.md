# PSF-IAminy — Etapa 109: Posto de uma matriz

## Posição no fluxo natural

Esta etapa fecha o bloco de álgebra linear finita iniciado na etapa 104.

## Construção pura

O posto é o número de linhas não-nulas depois da eliminação gaussiana — a dimensão do espaço gerado pelas linhas. Testado: identidade 3×3 tem posto 3; uma matriz com uma linha combinação linear das outras tem posto menor.

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana já construída;
- eliminação gaussiana.

## Dependências proibidas nesta etapa

- corpos infinitos; decomposição LU/QR; valores singulares;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/eliminacao_gaussiana_finita.py` e validado em `testes/test_eliminacao_gaussiana_finita.py`.
