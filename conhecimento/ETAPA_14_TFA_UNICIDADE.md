# PSF-IAminy — Etapa 14
## Teorema Fundamental da Aritmética: unicidade da decomposição prima

## Problema

A existência diz que um número pode ser decomposto em primos.

A unicidade diz algo mais forte:

```text
não existem duas decomposições primas essencialmente diferentes para o mesmo número
```

A ordem dos fatores não importa.

```text
2 × 2 × 3
```

e

```text
3 × 2 × 2
```

são a mesma decomposição como multiconjunto.

## Ideia pura

Suponha que um número `n` tem duas decomposições em primos:

```text
n = p1 × p2 × ... × pk
n = q1 × q2 × ... × qm
```

Como `p1` divide o produto dos `q`, e `p1` é primo, ele deve coincidir com algum dos fatores `q`.

Removemos esse fator comum dos dois lados.

Repetindo o processo, todos os fatores de uma decomposição são pareados com fatores da outra.

Quando tudo termina, sobra a mesma quantidade dos mesmos primos.

## Forma PSF

```text
duas listas de fatores primos
↓
mesmo produto
↓
retirar uma ocorrência comum por vez
↓
se ambas esvaziam juntas, são a mesma decomposição
```

## Cuidado honesto

A prova conceitual depende do lema:

```text
se p é primo e p divide a × b, então p divide a ou p divide b
```

Esse lema pertence ao fluxo natural imediatamente anterior à prova completa de unicidade. Nesta etapa o projeto já guarda a forma operacional da unicidade por comparação de multiconjuntos.

## No projeto

A unicidade operacional é representada por:

```text
MESMO_MULTICONJUNTO_PURO
FATORACAO_EQUIVALE_A_CANONICA
```

Isto não finge ser a prova completa do lema de Euclides; apenas fixa o comportamento estrutural que a decomposição prima deve obedecer.

## Exemplo

- `12 = 2×2×3` e também `12 = 3×2×2` -- ordens diferentes, mesmo multiconjunto `{2,2,3}`. Não existe outra lista de primos com produto `12` (ex.: `{2,6}` não vale, `6` não é primo).

## Implementação

```text
nucleo/teorema_fundamental_aritmetica.py
```

## Validação

```text
testes/test_teorema_fundamental_aritmetica.py
```
