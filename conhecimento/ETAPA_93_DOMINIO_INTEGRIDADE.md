# PSF-IAminy — Etapa 93: Domínio de integridade

## Posição no fluxo natural

Esta etapa pertence ao segundo bloco de estruturas algébricas, que vem depois de grupo e anel inicial (etapas 86-90).

## Construção pura

Um domínio de integridade é um anel comutativo com unidade, sem divisores de zero (a×b=0 só quando a=0 ou b=0), com zero diferente da unidade. (Z/4Z) falha aqui: 2×2=0 mod 4, mas nem 2 é zero — 2 é um divisor de zero.

## Exemplo

- `(ℤ/5ℤ)` é domínio de integridade (`5` é primo, nenhum produto de não-zeros dá zero mod 5).
- `(ℤ/4ℤ)` NÃO é: `2×2 mod4 = 4 mod4 = 0`, mas `2 ≠ 0` -- `2` é divisor de zero.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- anel comutativo;
- anel com unidade.

## Dependências proibidas nesta etapa

- corpos infinitos, extensões de corpo;
- espaços vetoriais, módulos;
- categoria, teoria de Galois;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_estruturas_ii.py` e validado em `testes/test_algebra_estruturas_ii.py`.
