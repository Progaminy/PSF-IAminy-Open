# PSF-IAminy — Etapa 86: Semigrupo

## Posição no fluxo natural

Esta etapa pertence ao bloco de operações algébricas, que vem depois de relações e funções (etapas 61-80).

## Construção pura

Um semigrupo é um domínio com uma operação fechada e associativa. É o primeiro nome de estrutura algébrica que o PSF-IAminy reconhece — antes dele, só existiam propriedades soltas.

## Exemplo

- `(ℤ/4ℤ, +mod4)` é semigrupo: já provado fechado (ETAPA 82) e associativo (ETAPA 83), as duas condições juntas.

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
