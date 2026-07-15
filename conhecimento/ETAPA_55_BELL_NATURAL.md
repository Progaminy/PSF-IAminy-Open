# PSF-IAminy — Etapa 55: Bell Natural

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Bell nasce como soma de todos os Stirling S(n,k), contando todas as partições de um conjunto finito.

## Exemplo

- Bell de `4`: soma de `S(4,1)+S(4,2)+S(4,3)+S(4,4) = 1+7+6+1 = 15` -- todas as formas de particionar um conjunto de `4` objetos, em qualquer quantidade de grupos não vazios.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- stirling segunda espécie;
- soma finita.

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
