# PSF-IAminy — Etapa 21
## Propriedades da divisibilidade sobre produto

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

Se `d` divide `a`, então `d` divide `a*c` e `c*a`, para qualquer `c` natural. A prova nasce de `a=d*k` e usa apenas associatividade operacional da multiplicação já construída: `a*c = (d*k)*c = d*(k*c)`.

## Exemplo

- `d=3`, `a=6` (`3|6`), `c=5`: `a*c=30`, e de fato `3|30` (`30=3×10`).

## Dependências permitidas

- divisibilidade pura
- resto euclidiano puro
- MDC puro
- Bézout e Euclides estendido

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
