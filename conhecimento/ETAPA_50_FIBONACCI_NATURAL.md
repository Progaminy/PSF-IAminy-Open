# PSF-IAminy — Etapa 50: Fibonacci Natural

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Fibonacci nasce como recorrência de par de estado: (F(n),F(n+1)) avança para (F(n+1),F(n)+F(n+1)).

## Exemplo

- Estado inicial `(F(0),F(1))=(0,1)`: avançando `7` vezes -- `(1,1)→(1,2)→(2,3)→(3,5)→(5,8)→(8,13)→(13,21)` -- o primeiro elemento do estado final é `F(7)=13`.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- recorrências;
- adição;
- par ordenado.

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
