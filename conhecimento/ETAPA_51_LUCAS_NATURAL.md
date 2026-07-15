# PSF-IAminy — Etapa 51: Lucas Natural

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Lucas usa a mesma estrutura de Fibonacci com estado inicial diferente, mostrando separação entre regra e semente.

## Exemplo

- Semente `(L(0),L(1))=(2,1)` (em vez de `(0,1)` de Fibonacci), mesma regra "somar os dois anteriores": `2,1,3,4,7,11` -- `L(5)=11`.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- fibonacci natural.

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
