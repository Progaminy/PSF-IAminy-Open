# PSF-IAminy — Etapa 32
## Teorema Chinês dos Restos

Regra de pureza:

```text
nenhum conceito futuro é usado como fundamento
```

## Construção pura

Para módulos positivos coprimos `m` e `n`, existe (e a construção busca de verdade, entre `0` e `m*n`) um `x` que satisfaz duas congruências simultâneas: `x ≡ a (mod m)` e `x ≡ b (mod n)`.

```text
coprimos(m,n)  =>  existe x em [0, m*n) tal que x≡a (mod m) e x≡b (mod n)
```

## Exemplo

- `x ≡ 2 (mod 3)` e `x ≡ 3 (mod 5)`: buscando entre `0` e `15`, `x=8` funciona -- `resto(8,3)=2` e `resto(8,5)=3`.

## Dependências permitidas

- congruencia igualdade restos
- mdc puro
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
