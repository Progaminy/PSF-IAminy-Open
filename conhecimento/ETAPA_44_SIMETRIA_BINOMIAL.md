# PSF-IAminy — Etapa 44: Simetria Binomial

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

C(n,k)=C(n,n-k) nasce porque escolher k elementos equivale a escolher os n-k que ficam fora.

## Exemplo

- `C(5,2)=10` e `C(5,3)=10` -- escolher `2` de `5` para participar é o mesmo que escolher `3` de `5` para ficar de fora.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- combinação simples;
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
