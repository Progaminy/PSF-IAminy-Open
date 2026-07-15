# PSF-IAminy — Etapa 88: Inverso algébrico

## Posição no fluxo natural

Esta etapa pertence ao bloco de operações algébricas, que vem depois de relações e funções (etapas 61-80).

## Construção pura

Dado um neutro e, um elemento a tem inverso b quando a∘b = b∘a = e. A definição depende de um neutro já identificado — por isso vem depois da etapa 84, não antes.

## Exemplo

- Em `(ℤ/4ℤ, +mod4)` com neutro `0`: `2` é o próprio inverso de si mesmo (`2 +mod4 2 = 4 mod 4 = 0`).

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- elemento neutro.

## Dependências proibidas nesta etapa

- anéis com divisão, corpos, espaços vetoriais;
- homomorfismos, categorias;
- cardinalidade infinita;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/operacoes_algebricas_naturais.py` e validado em `testes/test_operacoes_algebricas_naturais.py`.
