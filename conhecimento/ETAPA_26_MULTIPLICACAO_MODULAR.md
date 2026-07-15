# PSF-IAminy — Etapa 26
## Multiplicação modular

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

A multiplicação modular nasce como multiplicação comum (natural) seguida de representante canônico pelo resto puro -- mesma estrutura da adição modular (Etapa 25), trocando soma por produto:

```text
(a * b) mod m = resto(a*b, m)
```

## Exemplo

- `(4 × 5) mod 7`: `4×5=20`, `resto(20,7)=6` -- então `(4×5) mod 7 = 6`.

## Dependências permitidas

- multiplicacao
- congruencia igualdade restos
- resto euclidiano puro

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
