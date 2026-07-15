# PSF-IAminy — Etapa 49: Recorrencias

## Posição no fluxo natural

Esta etapa pertence ao primeiro bloco de **Combinatória Natural**, que vem depois de divisibilidade, primalidade, fatoração, congruência e aritmética modular.

## Construção pura

Recorrência nasce quando o próximo termo depende de termos ou estado anteriores.

## Exemplo

- Regra `próximo termo = soma dos dois anteriores`, partindo de `1,1`: `1,1,2,3,5,8,13,...` -- o sétimo termo (`13`) depende inteiramente dos dois que vieram antes dele, nunca de uma fórmula fechada direta.

## Dependências permitidas

- primitivas PSF: `V`, `F`, `ZERO`, `S`, `PAR`, `ITER`, `Y`;
- sequências finitas;
- iteração.

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
