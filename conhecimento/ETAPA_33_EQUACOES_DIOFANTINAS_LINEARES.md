# PSF-IAminy — Etapa 33
## Equações diofantinas lineares

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

A equação `ax + by = c` (com `c` natural, `x` e `y` inteiros relativos) é solúvel exatamente quando `mdc(a,b)` divide `c`. Quando solúvel, a solução nasce multiplicando os coeficientes de Bézout de `a` e `b` pelo quociente `c/mdc(a,b)`.

```text
soluvel(a,b,c)  <=>  mdc(a,b) divide c
x = coefX_bezout(a,b) * (c / mdc(a,b))
y = coefY_bezout(a,b) * (c / mdc(a,b))
```

## Exemplo

- `6x + 9y = 3`: `mdc(6,9)=3`, e `3` divide `3` -- solúvel. Bézout de `6,9` dá coeficientes que, escalados pelo quociente `3/3=1`, resultam em `x=-1, y=1`: confere `6×(-1) + 9×1 = -6+9 = 3`.
- `6x + 9y = 4`: `mdc(6,9)=3` não divide `4` -- não solúvel.

## Dependências permitidas

- mdc puro
- divisibilidade pura
- bezout e euclides estendido
- quociente puro
- inteiros relativos puros

## Conceitos proibidos nesta etapa

- operador nativo de divisão
- operador nativo de módulo/resto
- funções antigas de primos.py
- atalhos de fatoração externa
- aritmética modular pronta de aritmetica.py

## Implementação

```text
nucleo/teoria_numeros_natural.py
```

## Validação

```text
testes/test_teoria_numeros_natural_rapida.py
```
