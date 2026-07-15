# PSF-IAminy — Etapa 25
## Adição modular

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

A soma modular nasce como soma comum (Etapa 2) seguida de representante canônico pelo resto puro (Etapa 8):

```text
(a + b) mod m = resto(a+b, m)
```

## Exemplo

- `(8 + 9) mod 5`: `8+9=17`, `resto(17,5)=2` -- então `(8+9) mod 5 = 2`.

## Dependências permitidas

- adição
- congruencia igualdade restos
- resto euclidiano puro

## Conceitos proibidos nesta etapa

- operador nativo de divisão
- operador nativo de módulo/resto
- funções antigas de primos.py
- atalhos de fatoração externa

## Implementação

```text
nucleo/teoria_numeros_natural.py
```

## Validação

```text
testes/test_teoria_numeros_natural_rapida.py
```
