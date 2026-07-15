# PSF-IAminy — Etapa 23
## Congruência como relação de equivalência

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

A congruência (Etapa 22) possui reflexividade, simetria e transitividade porque igualdade de restos possui essas propriedades:

```text
reflexividade:  a ≡ a (mod m)          -- resto(a,m) = resto(a,m), sempre
simetria:       a ≡ b => b ≡ a (mod m) -- igualdade de restos é simétrica
transitividade: a≡b e b≡c => a≡c       -- igualdade de restos é transitiva
```

## Exemplo

- `17 ≡ 5 (mod 12)` e `5 ≡ 29 (mod 12)` (`resto(29,12)=5` também) -- por transitividade, `17 ≡ 29 (mod 12)` (confere: `resto(17,12)=resto(29,12)=5`).

## Dependências permitidas

- congruencia igualdade restos
- divisibilidade pura
- resto euclidiano puro
- MDC puro

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
