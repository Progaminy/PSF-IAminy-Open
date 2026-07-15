# PSF-IAminy — Etapa 38: Contagem Finita

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

A contagem finita estabiliza a passagem de coleções para números naturais sem recorrer a medida, probabilidade ou análise: é o mesmo princípio aditivo (Etapa 36) e multiplicativo (Etapa 37), agora batizados como a operação de contar uma coleção (união disjunta ou produto cartesiano), não uma peça nova.

## Exemplo

- União disjunta de uma coleção de `3` itens com outra de `4`: contagem total `3+4 = 7` (mesmo caso da Etapa 36, agora como "contar uma coleção").
- Produto cartesiano de uma coleção de `3` itens com outra de `4`: contagem total `3×4 = 12` (mesmo caso da Etapa 37).

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- contagem;
- número natural.

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
