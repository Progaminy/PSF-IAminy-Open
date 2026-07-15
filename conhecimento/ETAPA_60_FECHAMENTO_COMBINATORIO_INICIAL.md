# PSF-IAminy — Etapa 60: Fechamento Combinatorio Inicial

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

O primeiro bloco combinatório fecha quando contagem, fatorial, binomial, recorrências e partições estão definidos e testados.

## Exemplo

- Fechamento conferido para `n=5`: `C(5,0)=1` e `C(5,5)=1` -- os dois casos-limite do binomial de Pascal, confirmando que o bloco fecha de forma consistente.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- contagem finita;
- fatorial natural;
- combinação simples;
- recorrências;
- partições inteiras.

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
