# PSF-IAminy — Etapa 47: Inclusao Exclusao Basica

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Inclusão-exclusão corrige dupla contagem: |A∪B|=|A|+|B|-|A∩B|.

## Exemplo

- `|A|=5`, `|B|=7`, `|A∩B|=2`: `|A∪B| = 5+7-2 = 10` -- sem a correção, os `2` elementos comuns seriam contados duas vezes.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- adição;
- subtração;
- contagem finita.

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
