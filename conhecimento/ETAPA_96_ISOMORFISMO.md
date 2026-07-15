# PSF-IAminy — Etapa 96: Isomorfismo

## Posição no fluxo natural

Esta etapa pertence ao segundo bloco de estruturas algébricas, que vem depois de grupo e anel inicial (etapas 86-90).

## Construção pura

Um isomorfismo é um homomorfismo bijetor — reaproveita BIJETORA_PURA da etapa 77 sem redefinir nada. Dois grupos isomorfos são "a mesma estrutura", só com nomes diferentes para os elementos.

## Exemplo

- A identidade `f(x)=x` de `(ℤ/5ℤ,+)` para `(ℤ/5ℤ,+)` é isomorfismo: preserva a soma (é homomorfismo) e é bijetora (cada elemento vai para si mesmo, sem colisão) -- caso trivial, mas verificado de verdade, não assumido.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- homomorfismo grupos;
- bijetividade.

## Dependências proibidas nesta etapa

- corpos infinitos, extensões de corpo;
- espaços vetoriais, módulos;
- categoria, teoria de Galois;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_estruturas_ii.py` e validado em `testes/test_algebra_estruturas_ii.py`.
