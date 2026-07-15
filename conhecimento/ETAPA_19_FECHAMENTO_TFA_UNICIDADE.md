# ETAPA 19 — Fechamento da unicidade da decomposição prima

## Situação anterior

A existência da decomposição prima já estava operacionalmente construída por busca do menor fator.
A unicidade estava registrada como operacional por comparação de multiconjuntos, mas a prova conceitual ainda apontava para uma lacuna: o lema de Euclides.

## Agora

Com o lema de Euclides disponível, a unicidade pode ser justificada conceitualmente.

Se um número possui duas decomposições em primos:

```text
n = p1*p2*...*pk
n = q1*q2*...*qm
```

Então `p1` divide o produto:

```text
q1*q2*...*qm
```

Pelo lema de Euclides, `p1` divide algum `qi`.

Como `qi` é primo, os únicos divisores positivos de `qi` são:

```text
1 e qi
```

Como `p1` também é primo, não pode ser `1`.
Logo:

```text
p1 = qi
```

Remove-se esse fator dos dois lados e repete-se o argumento.

No fim, as duas fatorações têm exatamente os mesmos primos, com as mesmas repetições, apenas talvez em ordem diferente.

## Conclusão

A decomposição prima é única até reordenação.

Esta etapa não cria algoritmo novo; ela fecha uma lacuna teórica registrada honestamente na etapa anterior.

## Exemplo

- `n=12`: se alguém propuser `12 = 2×2×3` e também `12 = 2×6`, o lema de Euclides força `2` (do lado de `2×2×3`) a coincidir com um fator de `2×6` -- e de fato `6=2×3`, então a "outra" decomposição refina para os mesmos primos `{2,2,3}`.

## Implementação

```text
nucleo/teorema_fundamental_aritmetica.py
```

## Validação

```text
testes/test_teorema_fundamental_aritmetica.py
```
