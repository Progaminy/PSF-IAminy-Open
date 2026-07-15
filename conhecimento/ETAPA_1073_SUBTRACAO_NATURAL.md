# PSF-IAminy — Marcador histórico 1073: subtração natural (truncada)

## Construção pura

Se contar para frente é aplicar sucessor, contar para trás é desfazer um
sucessor — o predecessor. Mas nem todo número natural tem "um antes" que
funcione simetricamente: não existe natural antes do zero. Por isso a
subtração aqui é truncada — `m - n` quando `n > m` fica honestamente `zero`,
não um valor negativo fingido (números negativos exigem outra construção,
ver Etapa 16, inteiros relativos, que embrulha dois naturais num par
exatamente para representar isso sem fingir).

```text
predecessor(zero) = zero                      (não há antes do zero -- fica em zero)
predecessor(sucessor(n)) = n                   (desfaz exatamente um sucessor)

m - zero = m
m - sucessor(n) = predecessor(m - n)           (subtrair um a mais é aplicar
                                                 predecessor mais uma vez)
```

Predecessor é construído por "deslizamento" de um par `(a, b)`: começando em
`(zero, zero)` e avançando `(a, b) -> (b, sucessor(b))` a cada passo, depois
de `n` passos o primeiro elemento do par é `n - 1` (ou `zero`, se `n` já era
`zero`) — a mesma técnica de pares (Etapa 1, `PAR`) usada para carregar dois
valores através de uma iteração que só pode devolver um.

## Exemplo

- `7 - 3 = 4` (subtração normal, `n <= m`).
- `2 - 5 = 0` (trunca em zero, porque `5 > 2` -- nenhum natural fingido negativo).

## Dependências permitidas

- número natural
- adição

## Implementação

```text
nucleo/aritmetica.py
```

`PRED` (predecessor por deslizamento de pares) e `SUB` ("SUBTRAÇÃO TRUNCADA").

## Validação

```text
testes/test_subtracao_natural.py
```

## Estado

Predecessor e subtração truncada construídos e testados: `m - n = 0` quando
`n >= m`, e `(m - n) + n = m` quando `n <= m` (a prova real de que a
subtração desfaz a adição, não só "parece certo"). Igualdade e ordem
(próxima etapa) nascem diretamente disto: `m <= n` é exatamente "`m - n`
já truncou para zero".
