# PSF-IAminy — Etapa 98: Subgrupo

## Posição no fluxo natural

Esta etapa pertence ao segundo bloco de estruturas algébricas, que vem depois de grupo e anel inicial (etapas 86-90).

## Construção pura

Um subconjunto H de um grupo G é subgrupo quando H, com a mesma operação restrita, também forma um grupo: contém o neutro, é fechado, e cada elemento tem inverso dentro de H. Testado com H={0,2,4} dentro de (Z/6Z,+).

## Exemplo

- `H={0,2,4}` dentro de `(ℤ/6ℤ,+mod6)`: contém o `0`, é fechado (`2+4 mod6=0∈H`, `4+4 mod6=2∈H`), e cada elemento tem inverso dentro de `H` -- é subgrupo.
- `H'={0,1}` NÃO é subgrupo: `1+1 mod6=2`, que não está em `H'` -- não é fechado.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- grupo.

## Dependências proibidas nesta etapa

- corpos infinitos, extensões de corpo;
- espaços vetoriais, módulos;
- categoria, teoria de Galois;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_estruturas_ii.py` e validado em `testes/test_algebra_estruturas_ii.py`.
