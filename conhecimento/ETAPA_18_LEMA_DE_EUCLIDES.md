# ETAPA 18 — Lema de Euclides

## Enunciado

Se `p` é primo e `p` divide `a*b`, então:

```text
p divide a ou p divide b
```

Forma simbólica:

```text
p primo ∧ p | ab  ⇒  p | a ∨ p | b
```

## Por que este lema é necessário?

Na etapa anterior, a unicidade do Teorema Fundamental da Aritmética ainda não podia ser fechada honestamente.
A unicidade exige saber que um primo que divide um produto precisa dividir algum fator.

Logo, o lema de Euclides é a ponte entre:

```text
primo
produto
fatoração única
```

## Prova conceitual usando Bézout

Suponha:

```text
p é primo
p | a*b
```

Se `p | a`, acabou.

Se `p` não divide `a`, então, como `p` é primo, o único divisor comum possível de `p` e `a` é `1`.
Logo:

```text
mdc(p,a)=1
```

Por Bézout, existem inteiros `x,y` tais que:

```text
p*x + a*y = 1
```

Multiplicando por `b`:

```text
p*x*b + a*y*b = b
```

O primeiro termo é divisível por `p`.
O segundo termo também é divisível por `p`, porque assumimos que `p | a*b`.

Então a soma é divisível por `p`.
Logo:

```text
p | b
```

Portanto:

```text
p | a ou p | b
```

## Exemplo

- `p=7`, `a*b=21` (`a=3, b=7`): `7 | 21`. `7` não divide `3`, então (pelo lema) `7` deve dividir `7` -- e de fato divide.

## Observação de honestidade

A prova usa propriedades algébricas da divisibilidade sobre soma e produto.
Essas propriedades já são coerentes com as definições anteriores, mas devem continuar a ser registradas como lemas auxiliares no fluxo seguinte.

## Implementação

```text
nucleo/bezout_euclides_puro.py
```

## Validação

```text
testes/test_bezout_euclides_lema.py
```
