# PSF-IAminy — Etapa 3
## Divisibilidade pura sem divisão

Lei permanente:

> Nenhum conceito pode ser usado antes de nascer.

Por isso, divisibilidade não pode ser definida por divisão. A definição correta nasce de multiplicação e existência: perguntar "`a` divide `b`?" é perguntar "existe algum `k` que, multiplicado por `a`, reconstrói `b`?" — nada mais.

## Construção pura

### Definição bruta

`a` divide-bruto `b` quando existe `k` natural tal que:

```text
a × k = b
```

Isto permite o caso degenerado `0 | 0`, porque `0 × k = 0` para qualquer `k`.

### Definição estável

`a` divide `b` quando:

```text
a ≠ 0 e existe k natural tal que a × k = b
```

Forma:

```text
a | b ⇔ a ≠ 0 ∧ ∃k∈N : a × k = b
```

### Múltiplo

`b` é múltiplo de `a` quando:

```text
a | b
```

Ou seja:

```text
b = a × k
```

### Fator

`a` é fator de `b` quando `a` aparece numa construção multiplicativa de `b`:

```text
a | b
```

### Divisor próprio

`d` é divisor próprio de `n` quando:

```text
d | n e d < n
```

### Soma dos divisores próprios

```text
soma_divisores_proprios(n) = soma de todos os d tais que d | n e d < n
```

### Número perfeito, abundante e deficiente

Comparando essa soma com o próprio `n`:

```text
perfeito:   soma_divisores_proprios(n) = n
abundante:  soma_divisores_proprios(n) > n
deficiente: soma_divisores_proprios(n) < n
```

## Exemplo

- `6` é perfeito: divisores próprios `1, 2, 3` -- soma `1+2+3 = 6`.
- `28` é perfeito: divisores próprios `1, 2, 4, 7, 14` -- soma `1+2+4+7+14 = 28`.
- `12` é abundante: divisores próprios `1, 2, 3, 4, 6` -- soma `16 > 12`.
- `8` é deficiente: divisores próprios `1, 2, 4` -- soma `7 < 8`.

## Conceitos proibidos nesta etapa

- divisão
- resto
- módulo
- primo
- fatoração
- MDC por Euclides
- congruência

## Dependências permitidas

- ZERO
- S
- igualdade
- ordem
- adição
- multiplicação
- existência limitada

## Implementação

```text
nucleo/divisibilidade_pura.py
```

Este arquivo não usa DIV, MOD, primos nem fatoração.

## Validação

```text
testes/test_pureza_conceitual.py
```
