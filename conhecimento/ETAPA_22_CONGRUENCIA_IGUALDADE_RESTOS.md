# PSF-IAminy — Etapa 22
## Congruência como igualdade de restos

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

Depois de quociente e resto (Etapas 7-8), definimos `a ≡ b (mod m)` como igualdade entre os restos puros de `a` e `b` por `m`, com `m` positivo.

```text
a ≡ b (mod m)  ⇔  resto(a,m) = resto(b,m)
```

## Exemplo

- `17 ≡ 5 (mod 12)`: `resto(17,12)=5` e `resto(5,12)=5` -- os restos coincidem.
- `17 ≢ 4 (mod 12)`: `resto(17,12)=5 ≠ 4=resto(4,12)`.

## Dependências permitidas

- divisibilidade pura
- resto euclidiano puro
- MDC puro
- Bézout e Euclides estendido

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
