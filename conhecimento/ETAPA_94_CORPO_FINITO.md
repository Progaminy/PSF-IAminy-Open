# PSF-IAminy — Etapa 94: Corpo finito inicial

## Posição no fluxo natural

Esta etapa pertence ao segundo bloco de estruturas algébricas, que vem depois de grupo e anel inicial (etapas 86-90).

## Construção pura

Um corpo é um domínio de integridade onde todo elemento não-nulo tem inverso multiplicativo. (Z/5Z) é corpo porque 5 é primo; (Z/4Z) não é, porque 2 não tem inverso multiplicativo módulo 4. Este é o primeiro teorema de teoria dos números que a álgebra abstrata do PSF-IAminy confirma sozinha: Z/nZ é corpo se e somente se n é primo.

## Exemplo

- Em `(ℤ/5ℤ)`: `2×3 mod5 = 6 mod5 = 1` -- `3` é o inverso multiplicativo de `2`. Todo não-zero tem par assim -- é corpo.
- Em `(ℤ/4ℤ)`: `2×1=2`, `2×2=0`, `2×3 mod4=2` -- nenhum produto por `2` dá `1` -- `2` não tem inverso, não é corpo.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- domínio integridade;
- inverso algébrico.

## Dependências proibidas nesta etapa

- corpos infinitos, extensões de corpo;
- espaços vetoriais, módulos;
- categoria, teoria de Galois;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_estruturas_ii.py` e validado em `testes/test_algebra_estruturas_ii.py`.
