# PSF-IAminy — Etapa 36: Principio Aditivo

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

A contagem de alternativas disjuntas nasce como soma: se uma escolha tem a possibilidades e outra, sem sobreposição, tem b possibilidades, o total é a+b.

## Exemplo

- Uma escolha tem `3` alternativas e outra, disjunta (nenhuma em comum com a primeira), tem `4` -- total de alternativas possíveis: `3+4 = 7`.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
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
