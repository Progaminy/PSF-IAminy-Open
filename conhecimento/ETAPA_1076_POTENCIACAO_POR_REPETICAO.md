# PSF-IAminy — Marcador histórico 1076: potenciação por repetição

## Construção pura

O mesmo padrão de "repetir a operação anterior" sobe mais um andar:
potenciação é multiplicação repetida, do mesmo jeito que multiplicação é
adição repetida (Etapa 1075) e adição é sucessor repetido (Etapa 2).

```text
m ^ zero = um                        (multiplicar zero vezes dá o elemento
                                       neutro da multiplicação, não zero)
m ^ sucessor(n) = m × (m ^ n)        (potenciar mais uma vez é multiplicar
                                       por m mais uma vez)

exemplo: 2 ^ 4
= 2 × (2 ^ 3) = 2 × (2 × (2 ^ 2)) = 2 × (2 × (2 × (2 ^ 1)))
= 2 × (2 × (2 × (2 × (2 ^ 0)))) = 2 × (2 × (2 × (2 × 1))) = 16
```

Raiz e logaritmo (residual do item 300, ainda não construído nesta linha)
são os dois "outros lados da mesma caixa" que potenciação fecha: assim como
`2+3=5` permite perguntar "que número somado a 3 dá 5?" (a própria
subtração, Etapa 1073), `2^3=8` permite perguntar "que base elevada a 3 dá
8?" (raiz) ou "a que expoente elevo 2 para dar 8?" (logaritmo) — a mesma
pergunta de "encontrar o lado que falta", uma vez para cada operação.

## Dependências permitidas

- multiplicação

## Implementação

```text
nucleo/aritmetica.py
```

`POT` ("POTENCIAÇÃO — m^n = ITER(n)(1)(x -> MULT(m)(x))").

## Validação

```text
testes/test_potenciacao_por_repeticao.py
```

## Estado

Potenciação construída e testada: `m^0 = 1` (elemento neutro, não zero),
`m^1 = m`, e a prova de que `m^n` é de fato `m` multiplicado por si mesmo
`n` vezes (conferido contra multiplicação repetida construída
independentemente, não só aceito por sair da fórmula). Com isto, a
sequência que Etapa 1 abriu (contar -> sucessor -> adição -> subtração ->
igualdade/ordem -> multiplicação -> potenciação) fecha um fluxo único, sem
nenhum entroncamento no meio -- exatamente o pedido de que todo esse trecho
formasse um só pacote de aula, não vários pedaços soltos. Raiz exata já
existe (Etapa 1048); raiz geral, logaritmo geral e divisão continuam
etapas próprias já construídas em outros ramos (Etapa 7, divisão
euclidiana; Etapa 1045, logaritmos).
