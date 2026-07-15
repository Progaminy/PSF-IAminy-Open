# PSF-IAminy — Etapa 52: Numeros Figurados Revisitados

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Triangulares, quadrados, pentagonais e hexagonais são contagens geométricas discretas expressas por fórmulas finitas.

## Exemplo

- Triangular de `5`: `1+2+3+4+5 = 15` (pontos organizados em triângulo de lado 5).
- Quadrado de `5`: `5×5 = 25`.
- Pentagonal de `4`: `4×(3×4-1)/2 = 4×11/2 = 22`.
- Hexagonal de `4`: `4×(2×4-1) = 4×7 = 28`.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- soma finita;
- multiplicação;
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
