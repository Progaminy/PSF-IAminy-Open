# PSF-IAminy — Marcador histórico 1074: igualdade e ordem

## Construção pura

"Menor ou igual" nasce direto da subtração truncada (Etapa 1073): `m <= n`
é exatamente a afirmação de que `m - n` já truncou para zero (não sobrou
nada para tirar). Igualdade e as outras comparações vêm todas da mesma
peça, sem precisar de nenhuma ideia nova.

```text
m <= n  <=>  (m - n) é zero

m < n   <=>  (m <= n) e não (n <= m)     -- menor estrito
m = n   <=>  (m <= n) e (n <= m)         -- as duas cotas ao mesmo tempo
m > n   <=>  n < m
m >= n  <=>  n <= m
```

Esta é a mesma peça, "é zero", que a Etapa 3 (divisibilidade) já citava
como "igualdade" e "ordem" sem que nenhuma das duas tivesse nascido —
dívida fechada aqui.

## Exemplo

- `2 < 5` (verdadeiro) e `5 < 2` (falso); `3 <= 3` e `3 >= 3` (as duas verdadeiras -- igualdade pelas duas cotas).
- Tricotomia: para `m=4, n=4`, exatamente uma de `4<4`, `4=4`, `4>4` é verdadeira (`4=4`).

## Dependências permitidas

- subtração natural

## Implementação

```text
nucleo/aritmetica.py
```

`IS_ZERO`, `MENOR_OU_IGUAL`, `IGUAL`, `MENOR`, `MAIOR`, `MAIOR_OU_IGUAL`.

## Validação

```text
testes/test_igualdade_e_ordem.py
```

## Estado

Igualdade e as quatro comparações de ordem construídas e testadas:
reflexividade da igualdade, antissimetria e transitividade da ordem,
tricotomia (para todo par `m,n`, exatamente uma de `m<n`, `m=n`, `m>n` é
verdadeira). Multiplicação (próxima etapa) reaproveita adição do mesmo
jeito que subtração reaproveitou sucessor.
