# PSF-IAminy — Etapa 85: Comutatividade

## Posição no fluxo natural

Esta etapa pertence ao bloco de operações algébricas, que vem depois de relações e funções (etapas 61-80).

## Construção pura

Uma operação é comutativa quando a ordem dos elementos não importa: a∘b = b∘a. Independente de associatividade — existem operações associativas não comutativas, e vice-versa (embora esta última seja rara em domínios finitos pequenos).

## Exemplo

- `+mod4` é comutativa (`a +mod4 b = b +mod4 a` sempre). Já a subtração truncada sobre `{0,1,2,3}` NÃO é comutativa: `3 − 1 = 2`, mas `1 − 3 = 0` (truncada, não `-2`).

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;
- operação binária.

## Dependências proibidas nesta etapa

- anéis com divisão, corpos, espaços vetoriais;
- homomorfismos, categorias;
- cardinalidade infinita;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/operacoes_algebricas_naturais.py` e validado em `testes/test_operacoes_algebricas_naturais.py`.
