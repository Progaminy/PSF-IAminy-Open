# PSF-IAminy — Etapa 24
## Classes residuais

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

Uma classe residual é o agrupamento dos naturais que deixam o mesmo resto por um módulo positivo (consequência direta da congruência ser relação de equivalência, Etapa 23 -- toda relação de equivalência particiona o conjunto em classes). No núcleo, geramos a classe até um limite finito.

## Exemplo

- Classe residual de `2` módulo `5`, até o limite `20`: `{2, 7, 12, 17}` -- todos deixam resto `2` ao dividir por `5`.

## Dependências permitidas

- congruencia equivalencia
- divisibilidade pura
- resto euclidiano puro

## Conceitos proibidos nesta etapa

- operador nativo de divisão
- operador nativo de módulo/resto
- funções antigas de primos.py
- atalhos de fatoração externa

## Implementação

```text
nucleo/teoria_numeros_natural.py
```

## Validação

```text
testes/test_teoria_numeros_natural_rapida.py
```
