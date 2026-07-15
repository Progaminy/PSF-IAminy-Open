# PSF-IAminy — Marcador histórico 1075: multiplicação

## Construção pura

Se adição é "contar `n` vezes a partir de `m`" (Etapa 2), multiplicação é
"somar `m` repetidamente, `n` vezes" — a mesma relação que adição tem com
sucessor, mas um andar acima.

```text
m × zero = zero                     (somar m zero vezes dá zero)
m × sucessor(n) = m + (m × n)       (multiplicar mais uma vez é somar m
                                      mais uma vez)

exemplo: 3 × 4 = 3+3+3+3
= 3 + (3 × 3)
= 3 + (3 + (3 × 2))
= 3 + (3 + (3 + (3 × 1)))
= 3 + (3 + (3 + (3 + (3 × 0))))
= 3 + (3 + (3 + (3 + 0)))
= 12
```

"O 3 que se repete 4 vezes" é exatamente a definição: multiplicação é
adição iterada, do mesmo jeito que adição é sucessor iterado.

```text
mult(m)(n) = ITER(n)(zero)(x -> soma(m)(x))
```

## Exemplo

- `3 × 4 = 3+3+3+3 = 12` (multiplicação como adição repetida, passo a passo).

## Dependências permitidas

- adição
- número natural

## Implementação

```text
nucleo/aritmetica.py
```

`MULT` ("MULTIPLICAÇÃO — m * n = ITER(n)(0)(x -> SOMA(m)(x))").

## Validação

```text
testes/test_multiplicacao.py
```

## Estado

Multiplicação construída e testada: multiplicar por zero dá zero,
comutatividade, associatividade, e a prova de que `m × n` é de fato `m`
somado `n` vezes (conferido contra soma repetida construída
independentemente no teste, não só contra a própria fórmula). Potenciação
(próxima etapa) repete o mesmo padrão mais um andar acima: multiplicação
repetida.
