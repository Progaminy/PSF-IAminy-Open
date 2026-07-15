# PSF-IAminy — Etapa 89: Grupo

## Posição no fluxo natural

Esta etapa pertence ao bloco de operações algébricas, que vem depois de relações e funções (etapas 61-80).

## Construção pura

Um grupo é um monóide onde todo elemento tem inverso. Quando a operação também é comutativa, chama-se grupo abeliano. (Z/4Z, +mod4) e ((Z/5Z)\{0}, ×mod5) são os primeiros exemplos concretos validados no projeto.

## Exemplo

- `(ℤ/4ℤ, +mod4)` é grupo abeliano: monóide (ETAPA 87), todo elemento tem inverso, e a operação é comutativa. Já `(0..3, subtração truncada)` NÃO é grupo (nem toda subtração tem inverso dentro do domínio).

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- monoide;
- inverso algébrico.

## Dependências proibidas nesta etapa

- anéis com divisão, corpos, espaços vetoriais;
- homomorfismos, categorias;
- cardinalidade infinita;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/operacoes_algebricas_naturais.py` e validado em `testes/test_operacoes_algebricas_naturais.py`.
