# PSF-IAminy — Etapa 48: Sequencias Finitas

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Sequência finita nasce como iteração de uma regra sobre um estado inicial. Progressão aritmética (regra: somar uma razão fixa) e progressão geométrica (regra: multiplicar por uma razão fixa) são os dois primeiros exemplos concretos.

## Exemplo

- Progressão aritmética com primeiro termo `2`, razão `3`, termo de posição `4`: `2+3+3+3 = 14` (aplicar "somar 3" repetidamente, partindo de `2`, três vezes).
- Progressão geométrica com primeiro termo `2`, razão `3`, termo de posição `4`: `2×3×3×3 = 162` (aplicar "multiplicar por 3" repetidamente).

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- iteração;
- estado finito.

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
