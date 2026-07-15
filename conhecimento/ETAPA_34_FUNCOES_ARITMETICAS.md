# PSF-IAminy — Etapa 34
## Funções aritméticas

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

Nomeamos três funções que já nasceram na divisibilidade pura (Etapa 3), com o vocabulário padrão da teoria dos números: `tau(n)` (quantidade de divisores de `n`), `sigma(n)` (soma dos divisores de `n`) e a soma alíquota (soma dos divisores próprios, sem contar o próprio `n`). Nenhuma fórmula nova nasce aqui -- é a mesma contagem/soma de divisores já construída, só batizada com o nome que a teoria dos números usa.

```text
tau(n)   = quantidade de divisores de n
sigma(n) = soma dos divisores de n
aliquota(n) = sigma(n) - n
```

## Exemplo

- `tau(12)`: divisores de `12` são `1,2,3,4,6,12` -- `tau(12) = 6`.
- `sigma(12)`: `1+2+3+4+6+12 = 28`.
- soma alíquota de `6`: divisores próprios `1,2,3` -- `1+2+3 = 6` (por isso `6` é número perfeito).

## Dependências permitidas

- divisibilidade pura

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
