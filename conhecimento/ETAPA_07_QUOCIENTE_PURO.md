# ETAPA 07 — Quociente puro

## Construção pura

O quociente não nasce como operação pronta. Ele nasce como contagem de quantas retiradas iguais cabem em um número natural.

Para naturais `a` e `b`, com `b` diferente de zero:

```text
quociente(a,b) = quantidade de vezes que b pode ser retirado de a antes de sobrar algo menor que b
```

Ainda não usamos operador de divisão. O quociente é construído por repetição de subtrações (Etapa 5).

## Exemplo

- `quociente(17, 5) = 3`: `17 -> 12 -> 7 -> 2` -- três retiradas de 5, sobrando 2 (menor que 5, então paramos).
- `quociente(10, 5) = 2`: `10 -> 5 -> 0` -- duas retiradas exatas, sobrando 0.

## Dependências permitidas

- número natural
- ordem
- igualdade
- subtração controlada
- iteração
- recursão

## Implementação

```text
nucleo/divisao_euclidiana_pura.py
```

## Validação

```text
testes/test_divisao_euclidiana_pura.py
```
