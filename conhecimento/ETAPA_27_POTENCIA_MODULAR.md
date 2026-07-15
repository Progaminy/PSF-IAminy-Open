# PSF-IAminy — Etapa 27
## Potência modular

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

A potência modular nasce por iteração de multiplicação modular (Etapa 26), nunca por exponenciação externa: elevar `a` ao expoente `e` módulo `m` é multiplicar `a` por si mesmo, módulo `m`, `e` vezes seguidas.

```text
a^e mod m = ((...((1 * a) mod m) * a) mod m) ... * a) mod m   -- e multiplicações modulares
```

## Exemplo

- `3^4 mod 5`: `3^1=3`, `(3×3) mod 5=4`, `(4×3) mod 5=2`, `(2×3) mod 5=1` -- então `3^4 mod 5 = 1`.

## Dependências permitidas

- multiplicacao modular
- potenciacao por repeticao

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
