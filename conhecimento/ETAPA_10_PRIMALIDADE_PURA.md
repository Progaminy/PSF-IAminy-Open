# ETAPA 10 — PRIMALIDADE PURA

## Lei

Primo não pode ser definido por fatoração, porque fatoração ainda não nasceu.
Primo também não nasce de divisão nativa, módulo nativo ou tabela pronta.

Depois de nascer o resto euclidiano puro, podemos testar divisibilidade de modo operacional:

```text
d | n ⇔ RESTO_PURO(n,d) = 0
```

Isto não é módulo nativo; é o resto já construído por subtrações repetidas.

A definição pura é:

```text
n é primo ⇔ n > 1 e não existe d tal que 1 < d < n e d | n
```

Na origem conceitual, `d | n` continua significando:

```text
existe k natural tal que d × k = n
```

Logo, primalidade nasce de:

```text
número natural
ordem
divisibilidade
negação existencial
busca finita
```

## Composto

```text
n é composto ⇔ n > 1 e existe divisor interno de n
```

Um divisor interno é qualquer divisor entre `2` e `n-1`.

## Casos básicos

```text
0 não é primo
1 não é primo
2 é primo
3 é primo
4 é composto
5 é primo
6 é composto
```

## Exemplo

- `5` é primo: nenhum `d` com `1 < d < 5` divide `5` (testa `2, 3, 4` -- nenhum funciona).
- `6` é composto: `2 | 6` e `1 < 2 < 6` -- `2` é um divisor interno.

## Honestidade PSF

Esta etapa ainda não usa fatoração para justificar primalidade. A fatoração só
pode aparecer depois, como consequência da existência de fatores.

## Forma operacional no projeto

`nucleo/primalidade_pura.py`
`testes/test_primalidade_fatoracao_pura.py`
