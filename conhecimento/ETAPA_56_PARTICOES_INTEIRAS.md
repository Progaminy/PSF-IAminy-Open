# PSF-IAminy — Etapa 56: Particoes Inteiras

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Partição inteira conta decomposições aditivas de n, independente da ordem, via recorrência p(n,k).

## Exemplo

- Partições de `5`: `5`; `4+1`; `3+2`; `3+1+1`; `2+2+1`; `2+1+1+1`; `1+1+1+1+1` -- `7` decomposições diferentes, `p(5)=7`.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- recorrências;
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
