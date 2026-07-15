# PSF-IAminy — Etapa 30
## Função phi de Euler

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

`phi(n)` conta quantos naturais entre `1` e `n` são coprimos de `n` (mdc igual a 1). Nasce direto de mdc/coprimalidade -- nunca de uma fórmula pronta por fatores primos.

```text
phi(n) = quantidade de k em [1,n] tais que mdc(k,n) = 1
```

## Exemplo

- `phi(9)`: coprimos de `9` entre `1` e `9` são `1,2,4,5,7,8` (excluídos `3,6,9`, múltiplos de 3) -- `phi(9) = 6`.
- `phi(6)`: coprimos de `6` entre `1` e `6` são `1,5` -- `phi(6) = 2`.

## Dependências permitidas

- mdc puro

## Conceitos proibidos nesta etapa

- operador nativo de divisão
- operador nativo de módulo/resto
- funções antigas de primos.py
- atalhos de fatoração externa
- fórmula de phi por fatoração pronta

## Implementação

```text
nucleo/teoria_numeros_natural.py
```

## Validação

```text
testes/test_teoria_numeros_natural_rapida.py
```
