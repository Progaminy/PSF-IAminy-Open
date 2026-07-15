# PSF-IAminy — Etapa 45: Triangulo De Pascal

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

O triângulo de Pascal nasce da recorrência C(n,k)=C(n-1,k-1)+C(n-1,k), usando apenas soma e fronteiras.

## Exemplo

- `C(5,2)` pela recorrência: `C(4,1)+C(4,2) = 4+6 = 10` -- mesmo valor de `C(5,2)` calculado direto (Etapa 43).

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- combinação simples;
- adição.

## Dependências proibidas nesta etapa

- operadores nativos `/`, `//` e `%`;
- bibliotecas matemáticas externas;
- combinatória antiga importada como autoridade;
- probabilidade, estatística, análise ou álgebra abstrata ainda não construídas neste novo fluxo.

## Implementação

A contraparte operacional está em:

```text
nucleo/combinatoria_natural.py
```

## Validação

A validação automática está em:

```text
testes/test_combinatoria_natural.py
```
