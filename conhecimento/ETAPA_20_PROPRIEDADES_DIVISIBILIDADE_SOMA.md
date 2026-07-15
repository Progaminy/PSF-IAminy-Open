# PSF-IAminy — Etapa 20
## Propriedades da divisibilidade sobre soma

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

Se `d` divide `a` e `d` divide `b`, então `d` divide `a+b`. Esta etapa não cria congruência; apenas mostra que a divisibilidade é preservada pela soma quando a mesma unidade `d` constrói ambos os termos.

```text
d | a
d | b
=> d | (a+b)
```

Justificação pura: `a = d×x`, `b = d×y`, logo `a+b = d×x + d×y = d×(x+y)`.

## Exemplo

- `d=3`, `a=6`, `b=9`: `3|6` e `3|9`, e de fato `3|(6+9)=3|15` (`15=3×5`).

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
