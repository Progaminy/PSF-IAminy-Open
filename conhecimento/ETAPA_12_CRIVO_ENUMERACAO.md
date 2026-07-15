# ETAPA 12 — CRIVO COMO ENUMERAÇÃO

## Lei

Antes de um crivo otimizado, nasce uma enumeração honesta:

```text
percorrer os números de 2 até limite
manter apenas os que satisfazem PRIMO_PURO
```

Isto ainda não é o Crivo de Eratóstenes otimizado. É o primeiro nascimento do
conceito de lista de primos.

## Definição

```text
CRIVO_ENUMERACAO_PURO(limite) = lista de n em [2, limite] tais que n é primo
```

## Importância

Esta etapa cria a ponte natural para:

```text
crivo por remoção de múltiplos
teorema fundamental da aritmética
funções aritméticas
congruência
aritmética modular
```

## Exemplo

- `CRIVO_ENUMERACAO_PURO(10) = [2, 3, 5, 7]`: percorre `2` a `10`, testando `PRIMO_PURO` em cada um -- `4, 6, 8, 9, 10` são compostos, ficam de fora.

## Implementação

```text
nucleo/primalidade_pura.py
```

## Validação

```text
testes/test_primalidade_fatoracao_pura.py
```
