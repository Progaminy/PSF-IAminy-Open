# PSF-IAminy — Etapa 46: Binomio De Newton Finito

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

O binómio finito nasce da contagem dos termos obtidos ao expandir (a+b)^n.

## Exemplo

- `(2+1)^3`: expandindo com os coeficientes de Pascal `C(3,0),C(3,1),C(3,2),C(3,3) = 1,3,3,1`: `1×2³+3×2²×1+3×2×1²+1×1³ = 8+12+6+1 = 27`, que confere com `(2+1)^3 = 3^3 = 27`.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- triângulo de Pascal;
- potência por repetição;
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
