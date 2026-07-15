# PSF-IAminy — Etapa 95: Homomorfismo de grupos

## Posição no fluxo natural

Esta etapa pertence ao segundo bloco de estruturas algébricas, que vem depois de grupo e anel inicial (etapas 86-90).

## Construção pura

Um homomorfismo é uma função entre dois grupos que preserva a operação: f(a∘b) = f(a)∘f(b). Nasce depois de grupo (etapa 89) e de função finita (etapas 70-74) — não antes, porque precisa dos dois conceitos simultaneamente.

## Exemplo

- `f:(ℤ/6ℤ,+)→(ℤ/3ℤ,+)`, `f(x) = x mod 3`: `f(2+4 mod6) = f(0) = 0`, e `f(2)+f(4) mod3 = 2+1 mod3 = 0` -- os dois caminhos dão o mesmo resultado, confirmando que `f` preserva a operação.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- grupo;
- aplicação finita.

## Dependências proibidas nesta etapa

- corpos infinitos, extensões de corpo;
- espaços vetoriais, módulos;
- categoria, teoria de Galois;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/algebra_estruturas_ii.py` e validado em `testes/test_algebra_estruturas_ii.py`.
