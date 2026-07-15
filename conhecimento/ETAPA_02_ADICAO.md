# PSF-IAminy — Etapa 2

## Adição: contar é aplicar sucessor repetidamente

## Construção pura

Contar `n` a partir de `m` é aplicar sucessor a `m`, `n` vezes. É exatamente
isso que a adição é — nada mais precisa ser inventado.

```text
m + zero = m                       (contar zero vezes não muda nada)
m + sucessor(n) = sucessor(m + n)  (contar mais um é aplicar sucessor mais uma vez)

exemplo: 2 + 3
= 2 + sucessor(sucessor(sucessor(zero)))
= sucessor(2 + sucessor(sucessor(zero)))
= sucessor(sucessor(2 + sucessor(zero)))
= sucessor(sucessor(sucessor(2 + zero)))
= sucessor(sucessor(sucessor(2)))
= 5
```

Usando a forma de numeral de Church (Etapa 1: `n` é a capacidade de aplicar
uma função `n` vezes), somar `m + n` é simplesmente aplicar sucessor `n`
vezes a partir de `m` — a mesma "iteração" (`ITER`) que já constrói o próprio
sucessor.

```text
soma(m)(n) = ITER(n)(m)(sucessor)
```

## Exemplo

- `2 + 3 = 5`: aplicar sucessor 3 vezes a partir de 2 (passo a passo na Construção pura acima).
- `m + 0 = m` para qualquer `m`: contar zero vezes nunca muda o ponto de partida.

## Dependências permitidas

- número natural

## Implementação

```text
nucleo/aritmetica.py
```

`SOMA`, primeira definição do ficheiro ("ADIÇÃO — m + n = ITER(n)(m)(S)").
Nenhuma função nativa de soma do Python é usada.

## Validação

```text
testes/test_adicao.py
```

## Estado

Adição construída e testada: comutatividade, associatividade e o caso base
(somar zero não muda nada), todos conferidos comparando traduções para
inteiro, nunca aceitos por definição. Multiplicação (próxima etapa) é o
passo direto seguinte: "somar `m` repetidamente, `n` vezes" é exatamente
"3+3+3+3, o 3 que se repete 4 vezes".
