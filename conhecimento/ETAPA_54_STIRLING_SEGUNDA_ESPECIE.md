# PSF-IAminy — Etapa 54: Stirling Segunda Especie

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Stirling S(n,k) conta partições de n objetos em k blocos não vazios via recorrência.

## Exemplo

- `S(5,2)=15`: há `15` jeitos diferentes de dividir `5` objetos distintos em exatamente `2` grupos, nenhum vazio.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- recorrências.

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
