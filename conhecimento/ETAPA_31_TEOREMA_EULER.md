# PSF-IAminy — Etapa 31
## Teorema de Euler

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

Generalização do Pequeno Teorema de Fermat (Etapa 29): se `a` e `n` são coprimos e `n>1`, então `a^phi(n) ≡ 1 (mod n)` -- troca o expoente fixo `p-1` (só valia para módulo primo) pelo `phi(n)` (Etapa 30), que funciona para qualquer módulo maior que 1.

```text
n>1 e coprimos(a,n)  =>  a^phi(n) mod n = 1
```

## Exemplo

- `n=4`, `a=3`: `mdc(3,4)=1`, `phi(4)=2` (coprimos de 4 entre 1 e 4: `1,3`) -- `3^2 mod 4`: `9 mod 4 = 1` -- confirma `3^phi(4) ≡ 1 (mod 4)`.

## Dependências permitidas

- phi euler
- potencia modular
- congruencia igualdade restos
- mdc puro

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
