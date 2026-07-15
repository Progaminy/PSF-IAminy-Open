# PSF-IAminy — Etapa 39: Escolha Ordenada Com Repeticao

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Uma sequência de k posições com n opções em cada posição nasce como potência n^k, pois multiplica n por si mesmo k vezes.

## Exemplo

- `4` posições, `3` opções em cada: `3^4 = 3×3×3×3 = 81` sequências possíveis (repetição permitida em cada posição).

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- potência por repetição.

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
