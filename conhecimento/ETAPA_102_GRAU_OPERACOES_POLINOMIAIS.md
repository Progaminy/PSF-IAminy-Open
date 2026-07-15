# PSF-IAminy — Etapa 102: Grau e operações polinomiais

## Posição no fluxo natural

Esta etapa pertence ao bloco de polinómios e álgebra linear finita, que vem depois de corpo finito (etapa 94).

## Construção pura

O grau é o maior índice com coeficiente não-nulo (indefinido para o polinómio nulo). Soma: componente a componente. Produto: convolução dos coeficientes — grau(p×q)=grau(p)+grau(q) quando o anel não tem divisores de zero (domínio de integridade, etapa 93).

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- polinómios anel;
- domínio integridade.

## Dependências proibidas nesta etapa

- polinómios sobre corpos infinitos;
- espaços vetoriais de dimensão infinita;
- autovalores, autovetores, formas quadráticas;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_linear_inicial.py` e validado em `testes/test_algebra_linear_inicial.py`.
