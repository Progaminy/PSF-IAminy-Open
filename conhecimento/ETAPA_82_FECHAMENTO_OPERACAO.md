# PSF-IAminy — Etapa 82: Fechamento de operação

## Posição no fluxo natural

Esta etapa pertence ao bloco de operações algébricas, que vem depois de relações e funções (etapas 61-80).

## Construção pura

Uma operação é fechada sobre um domínio quando o resultado, para quaisquer dois elementos do domínio, permanece dentro do próprio domínio. Sem fechamento, não faz sentido perguntar se a operação é associativa ou se tem neutro dentro desse domínio.

## Exemplo

- `(ℤ/4ℤ, +mod4)` é fechada: somar quaisquer dois elementos de `{0,1,2,3}` módulo 4 sempre devolve outro elemento de `{0,1,2,3}`.

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
