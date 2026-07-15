# ETAPA 16 — Inteiros relativos puros

## Necessidade

Até agora o PSF-IAminy trabalha principalmente em `N`, os naturais.
Isso basta para divisibilidade, MDC, quociente, resto, primalidade e fatoração.

Mas a identidade de Bézout exige coeficientes que podem ser negativos:

```text
a*x + b*y = mdc(a,b)
```

Logo, antes de Bézout, o sistema precisa construir inteiros relativos.

## Construção

Um inteiro é representado por um par de naturais:

```text
z = (p,n)
```

com interpretação:

```text
z representa p - n
```

Exemplos:

```text
3  = (3,0)
-2 = (0,2)
0  = (0,0)
```

A mesma quantidade pode ter várias representações:

```text
3 = (3,0) = (4,1) = (5,2)
```

Por isso, a igualdade não é estrutural. É igualdade por equivalência cruzada:

```text
(p1,n1) = (p2,n2)
⇔
p1 + n2 = p2 + n1
```

## Operações

Soma:

```text
(p1,n1) + (p2,n2) = (p1+p2, n1+n2)
```

Oposto:

```text
-(p,n) = (n,p)
```

Subtração:

```text
z1 - z2 = z1 + (-z2)
```

Multiplicação:

```text
(p1-n1)(p2-n2)
= (p1p2+n1n2) - (p1n2+n1p2)
```

## Exemplo

- Temos `2` (mangas) e queremos tirar `5`: `2 - 5` não existe como diferença controlada de naturais (Etapa 5, `2 < 5`), mas como inteiro relativo é `(2,0) - (5,0) = (2,5)`, que representa `2-5 = -3` -- faltam 3.
- `3 = (3,0) = (4,1) = (5,2)`: a mesma quantidade, várias representações -- por isso a igualdade é cruzada (`p1+n2 = p2+n1`), nunca comparação estrutural direta do par.
- `-2 = (0,2)`, `0 = (0,0)`.

## Lei da etapa

Esta etapa não usa negativos nativos do Python. O sinal nasce como estrutura.

## Implementação

```text
nucleo/inteiros.py
```

## Validação

```text
testes/test_nucleo.py
```
