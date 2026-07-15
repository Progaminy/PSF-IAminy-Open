# PSF-IAminy — Etapa 84: Elemento neutro

## Posição no fluxo natural

Esta etapa pertence ao bloco de operações algébricas, que vem depois de relações e funções (etapas 61-80).

## Construção pura

Um elemento neutro e satisfaz e∘a = a∘e = a para todo a do domínio. Nasce depois de fechamento e associatividade porque só faz sentido procurá-lo dentro de um domínio fechado.

## Exemplo

- Em `(ℤ/4ℤ, +mod4)`, `0` é neutro (`0 +mod4 a = a` para todo `a`); já `1` não é (`1 +mod4 0 = 1 ≠ 0`).

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- fechamento operação;
- associatividade.

## Dependências proibidas nesta etapa

- anéis com divisão, corpos, espaços vetoriais;
- homomorfismos, categorias;
- cardinalidade infinita;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/operacoes_algebricas_naturais.py` e validado em `testes/test_operacoes_algebricas_naturais.py`.
