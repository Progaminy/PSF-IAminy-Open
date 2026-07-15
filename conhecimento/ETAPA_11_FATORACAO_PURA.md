# ETAPA 11 — FATORAÇÃO PURA POR BUSCA

## Lei

Fatoração nasce depois de:

```text
divisibilidade
quociente
resto
divisão euclidiana
primo
composto
```

A fatoração pura não é uma definição de primo. Ela é uma decomposição obtida por
busca do menor fator.

## Construção

Para `n > 1`:

```text
1. procura o menor d >= 2 tal que d | n
2. coloca d na lista de fatores
3. calcula q tal que n = d × q
4. repete o processo sobre q
```

O quociente usado no passo 3 vem da divisão euclidiana pura, construída antes por
subtrações repetidas.

## Exemplo

- `12 → 2, 2, 3`: menor fator `2` (`12=2×6`), depois `2` de novo (`6=2×3`), depois `3` (primo, para).
- `29 → 29`: nenhum `d` de `2` a `28` divide `29` -- é primo, a "fatoração" é ele mesmo.

## Dependências proibidas

Esta etapa não pode depender de:

```text
MOD nativo
DIV nativo
operador /
operador //
operador %
fatoração pronta antiga
```

## Forma operacional no projeto

`nucleo/fatoracao_pura.py`
`testes/test_primalidade_fatoracao_pura.py`
