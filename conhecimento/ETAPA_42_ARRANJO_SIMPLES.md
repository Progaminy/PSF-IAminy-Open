# PSF-IAminy — Etapa 42: Arranjo Simples

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Arranjo escolhe k posições ordenadas a partir de n objetos sem repetição; nasce de n!/(n-k)! usando quociente euclidiano já construído.

## Exemplo

- `A(5,2) = 5!/(5-2)! = 120/6 = 20` -- escolher e ordenar `2` de `5` objetos distintos.
- `A(2,5)` (escolher mais objetos do que existem): sentinela `0`, honesto, nunca inventa arranjo impossível.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- fatorial natural;
- resto e divisão euclidiana;
- subtração.

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
