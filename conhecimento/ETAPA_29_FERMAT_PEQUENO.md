# PSF-IAminy — Etapa 29
## Pequeno Teorema de Fermat

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

Se `p` é primo e `a` é coprimo de `p`, então `a^(p-1) ≡ 1 (mod p)`. O projeto registra a proposição como implicação (hipótese → congruência) e confere em casos concretos usando a potência modular já construída, nunca aceitando o teorema sem checagem.

```text
primo(p) e coprimos(a,p)  =>  a^(p-1) mod p = 1
```

## Exemplo

- `p=5`, `a=2`: `5` é primo, `mdc(2,5)=1` -- `2^4 mod 5`: `2^1=2,2^2 mod5=4,2^3 mod5=3,2^4 mod5=1` -- confirma `2^4 ≡ 1 (mod 5)`.

## Dependências permitidas

- primalidade pura
- mdc puro
- potencia modular
- congruencia igualdade restos

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
