# PSF-IAminy — Etapa 83: Associatividade

## Posição no fluxo natural

Esta etapa pertence ao bloco de operações algébricas, que vem depois de relações e funções (etapas 61-80).

## Construção pura

Uma operação é associativa quando o agrupamento de três elementos não altera o resultado: (a∘b)∘c = a∘(b∘c). É a propriedade que permite escrever a∘b∘c sem ambiguidade.

## Exemplo

- `(ℤ/4ℤ, +mod4)` é associativa: `(1 +mod4 2) +mod4 3` e `1 +mod4 (2 +mod4 3)` dão o mesmo resultado, `2`, para qualquer agrupamento testado.

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
