# ETAPA 08 — Resto e divisão euclidiana pura

## Nascimento do resto

Depois de construir o quociente por retiradas sucessivas, sobra um número final menor que o divisor.

Esse número é chamado de resto.

## Definição

Para `a` natural e `b` natural positivo, existem `q` e `r` tais que:

```text
a = b × q + r
r < b
```

Chamamos:

```text
q = quociente de a por b
r = resto de a por b
```

## Exemplo

- `17 = 5 × 3 + 2`, e `2 < 5` -- então `quociente(17,5)=3` e `resto(17,5)=2`.
- `20 = 4 × 5 + 0`, e `0 < 4` -- divisão exata: `quociente(20,4)=5` e `resto(20,4)=0`.

## Regra de pureza

Esta etapa não usa operador pronto de divisão, nem operador pronto de módulo.

O par `(q,r)` nasce de subtração repetida.

## Forma operacional no projeto

`nucleo/divisao_euclidiana_pura.py`
`testes/test_divisao_euclidiana_pura.py`
