# PSF-IAminy — Etapa 15
## MDC e MMC por fatores

## Estado atual

Já temos:

```text
divisor
MDC por definição
MDC por subtração
MDC por resto
primo
fatoração prima
```

Agora podemos construir uma nova visão:

```text
MDC e MMC como operações sobre fatores primos
```

## MDC por fatores

O MDC usa apenas os fatores comuns.

Exemplo:

```text
12 = 2 × 2 × 3
18 = 2 × 3 × 3
```

Fatores comuns:

```text
2 × 3
```

Logo:

```text
MDC(12,18) = 6
```

Forma geral:

```text
MDC = produto da interseção dos multiconjuntos de fatores
```

## MMC por fatores

O MMC usa todos os fatores necessários para cobrir os dois números.

Exemplo:

```text
12 = 2 × 2 × 3
18 = 2 × 3 × 3
```

União necessária:

```text
2 × 2 × 3 × 3
```

Logo:

```text
MMC(12,18) = 36
```

Forma geral:

```text
MMC = produto da união dos multiconjuntos de fatores
```

## Relação fundamental

Para `a > 0` e `b > 0`:

```text
MDC(a,b) × MMC(a,b) = a × b
```

No PSF-IAminy, esta relação é validada sem usar divisão como fórmula.

## Exemplo

- `12=2×2×3`, `18=2×3×3`: fatores comuns `2×3`, então `MDC(12,18)=6`.
- Mesmos números: união necessária `2×2×3×3`, então `MMC(12,18)=36`.
- Confere a relação fundamental: `MDC(12,18) × MMC(12,18) = 6×36 = 216 = 12×18`.

## No projeto

Implementado em:

```text
nucleo/teorema_fundamental_aritmetica.py
```

Funções principais:

```text
MDC_POR_FATORES_PURO
MMC_POR_FATORES_PURO
MDC_POR_FATORES_CONFERE
MDC_MMC_PRODUTO_CONFERE
```

## Validação

```text
testes/test_teorema_fundamental_aritmetica.py
```
