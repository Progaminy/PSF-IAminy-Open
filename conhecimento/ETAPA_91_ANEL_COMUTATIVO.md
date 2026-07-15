# PSF-IAminy — Etapa 91: Anel comutativo

## Posição no fluxo natural

Esta etapa pertence ao segundo bloco de estruturas algébricas, que vem depois de grupo e anel inicial (etapas 86-90).

## Construção pura

Um anel é comutativo quando, além das propriedades já exigidas pelo anel inicial (etapa 90), o produto também comuta: a×b = b×a. Nem todo anel é comutativo (matrizes, por exemplo, não comutam sob multiplicação) — mas os primeiros exemplos do PSF-IAminy, como (Z/nZ), são.

## Exemplo

- `(ℤ/5ℤ, +mod5, ×mod5)`: `3×4 mod5 = 12 mod5 = 2` e `4×3 mod5 = 12 mod5 = 2` -- o produto comuta, confirmando anel comutativo.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- anel inicial.

## Dependências proibidas nesta etapa

- corpos infinitos, extensões de corpo;
- espaços vetoriais, módulos;
- categoria, teoria de Galois;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_estruturas_ii.py` e validado em `testes/test_algebra_estruturas_ii.py`.
