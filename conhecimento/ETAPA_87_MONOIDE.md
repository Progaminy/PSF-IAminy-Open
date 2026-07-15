# PSF-IAminy — Etapa 87: Monóide

## Posição no fluxo natural

Esta etapa pertence ao bloco de operações algébricas, que vem depois de relações e funções (etapas 61-80).

## Construção pura

Um monóide é um semigrupo onde além disso existe um elemento neutro. Todo monóide é semigrupo; nem todo semigrupo é monóide (a soma de naturais positivos, sem o zero, é semigrupo mas não monóide).

## Exemplo

- `(ℤ/4ℤ, +mod4)` é monóide: semigrupo (ETAPA 86) mais o neutro `0` (ETAPA 84) que ele já tinha.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- semigrupo;
- elemento neutro.

## Dependências proibidas nesta etapa

- anéis com divisão, corpos, espaços vetoriais;
- homomorfismos, categorias;
- cardinalidade infinita;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/operacoes_algebricas_naturais.py` e validado em `testes/test_operacoes_algebricas_naturais.py`.
