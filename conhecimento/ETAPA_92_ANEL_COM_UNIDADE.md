# PSF-IAminy — Etapa 92: Anel com unidade

## Posição no fluxo natural

Esta etapa pertence ao segundo bloco de estruturas algébricas, que vem depois de grupo e anel inicial (etapas 86-90).

## Construção pura

Um anel tem unidade quando existe elemento neutro para o produto — distinto do neutro da soma (chamado zero). Nem todo anel tem unidade (o anel dos inteiros pares, sob soma e produto usuais, não tem).

## Exemplo

- `(ℤ/5ℤ, +mod5, ×mod5)`: zero da soma é `0`; unidade do produto é `1` (`3×1 mod5 = 3` para qualquer elemento) -- os dois neutros são distintos, confirmando anel com unidade.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- anel inicial;
- elemento neutro.

## Dependências proibidas nesta etapa

- corpos infinitos, extensões de corpo;
- espaços vetoriais, módulos;
- categoria, teoria de Galois;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_estruturas_ii.py` e validado em `testes/test_algebra_estruturas_ii.py`.
