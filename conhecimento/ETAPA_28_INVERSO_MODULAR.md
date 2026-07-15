# PSF-IAminy — Etapa 28
## Inverso modular

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

O inverso modular de `a` em `m` é um `x` tal que `a*x ≡ 1 (mod m)`. Existe exatamente quando `m>1` e `a` é coprimo de `m` (mdc(a,m)=1) -- a construção busca `x` entre `1` e `m` e confere a congruência para cada candidato, parando no primeiro que funciona.

## Exemplo

- Inverso modular de `3 mod 7`: testando `x=1,2,3,4,5` -- `3×5=15`, `resto(15,7)=1` -- então o inverso é `5` (confere: `3×5 ≡ 1 mod 7`).
- `2 mod 4` não tem inverso: `mdc(2,4)=2 ≠ 1` -- `2` não é coprimo de `4`.

## Dependências permitidas

- mdc puro
- congruencia igualdade restos
- multiplicacao

## Conceitos proibidos nesta etapa

- operador nativo de divisão
- operador nativo de módulo/resto
- funções antigas de primos.py
- atalhos de fatoração externa
- aritmética modular pronta de aritmetica.py

## Implementação

```text
nucleo/teoria_numeros_natural.py
```

## Validação

```text
testes/test_teoria_numeros_natural_rapida.py
```
