# ETAPA 17 — Identidade de Bézout e Euclides estendido

## Ponto de partida

Já temos:

```text
MDC por definição
Euclides por subtração
quociente
resto
Euclides por resto
inteiros relativos
```

Agora podemos construir combinações lineares.

## Combinação linear

Para naturais `a,b` e inteiros `x,y`, uma combinação linear é:

```text
a*x + b*y
```

O resultado é um inteiro.

## Identidade de Bézout

A identidade de Bézout diz:

```text
existem inteiros x,y tais que:
a*x + b*y = mdc(a,b)
```

No PSF-IAminy, isto não é introduzido como fórmula mágica.
Ele nasce do algoritmo de Euclides estendido.

## Reconstituição pelo Euclides estendido

Se:

```text
a = b*q + r
```

e já sabemos que:

```text
g = b*x1 + r*y1
```

então, como:

```text
r = a - b*q
```

substituímos:

```text
g = b*x1 + (a - b*q)*y1
```

logo:

```text
g = a*y1 + b*(x1 - q*y1)
```

Portanto os novos coeficientes são:

```text
x = y1
y = x1 - q*y1
```

## Exemplo

- `a=12, b=18`: `MDC(12,18)=6` (Etapa 15). Coeficientes de Bézout: `x=-1, y=1` -- confere `12×(-1) + 18×1 = -12+18 = 6`.

## Lei da etapa

O Euclides estendido só aparece depois de quociente e resto já terem sido construídos.
Ele não usa módulo nativo, divisão nativa, congruência nem aritmética modular.

## Forma operacional no projeto

`nucleo/bezout_euclides_puro.py`
`testes/test_bezout_euclides_lema.py`
