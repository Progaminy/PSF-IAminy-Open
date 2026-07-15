# PSF-IAminy — Etapa 90: Anel inicial

## Posição no fluxo natural

Esta etapa pertence ao bloco de operações algébricas, que vem depois de relações e funções (etapas 61-80).

## Construção pura

Um anel nasce de duas operações sobre o mesmo domínio: a soma forma um grupo abeliano, o produto forma um semigrupo, e o produto distribui sobre a soma dos dois lados. (Z/4Z, +mod4, ×mod4) é o primeiro anel validado no projeto.

## Exemplo

- `(ℤ/4ℤ, +mod4, ×mod4)` é anel: `+mod4` já é grupo abeliano (Etapa 89), `×mod4` é semigrupo, e a distributiva confere -- `2×(1+3) mod4 = 2×0 mod4 = 0`, igual a `(2×1 + 2×3) mod4 = (2+6) mod4 = 0`.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- grupo;
- semigrupo;
- comutatividade.

## Dependências proibidas nesta etapa

- anéis com divisão, corpos, espaços vetoriais;
- homomorfismos, categorias;
- cardinalidade infinita;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/operacoes_algebricas_naturais.py` e validado em `testes/test_operacoes_algebricas_naturais.py`.
