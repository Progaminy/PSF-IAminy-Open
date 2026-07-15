# PSF-IAminy — Etapa 43: Combinacao Simples

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Combinação remove a ordem dos arranjos dividindo por k!, depois de fatorial e quociente exato já existirem.

## Exemplo

- `C(5,2) = A(5,2)/2! = 20/2 = 10` -- escolher `2` de `5` objetos, sem se importar com a ordem.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- arranjo simples;
- fatorial natural;
- resto e divisão euclidiana.

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
