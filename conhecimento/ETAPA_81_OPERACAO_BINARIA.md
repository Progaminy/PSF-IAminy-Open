# PSF-IAminy — Etapa 81: Operação binária

## Posição no fluxo natural

Esta etapa pertence ao bloco de operações algébricas, que vem depois de relações e funções (etapas 61-80).

## Construção pura

Uma operação binária sobre um domínio nasce quando dois elementos do domínio produzem, por uma regra fixa, um terceiro valor. É o mesmo padrão já usado por SOMA e MULT — nome próprio para o tópico ficar rastreável, não uma estrutura nova.

## Exemplo

- Adição módulo 4 sobre `{0,1,2,3}`: `2 +mod4 3 = 1` (porque `5 mod 4 = 1`) -- dois elementos do domínio produzem um terceiro pela regra fixa.

## Dependências permitidas

- distinção;
- par ordenado;
- igualdade;
- domínio finito explícito;
- lógica booleana já construída;

## Dependências proibidas nesta etapa

- anéis com divisão, corpos, espaços vetoriais;
- homomorfismos, categorias;
- cardinalidade infinita;
- análise real, cálculo diferencial ou integral;
- estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/operacoes_algebricas_naturais.py` e validado em `testes/test_operacoes_algebricas_naturais.py`.
