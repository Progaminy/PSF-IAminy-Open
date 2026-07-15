# PSF-IAminy — Etapa 4
## Divisor comum e MDC puro sem divisão

Depois de construir divisor (Etapa 3), o próximo conceito natural é divisor comum: um número que divide dois números ao mesmo tempo. O maior desses divisores comuns é o MDC — construído aqui só por comparação e busca finita, sem usar `mod` nem o algoritmo de Euclides ainda (isso é a Etapa 6).

## Construção pura

### Divisor comum

`d` é divisor comum de `a` e `b` quando:

```text
d | a e d | b
```

Pela definição pura de divisibilidade (Etapa 3):

```text
∃x : d × x = a
∃y : d × y = b
```

### Maior divisor comum

`g` é MDC de `a` e `b` quando:

```text
g | a
g | b
para todo d, se d | a e d | b, então d ≤ g
```

Forma conceitual:

```text
MDC(a,b)=g ⇔ g é divisor comum de a,b e nenhum divisor comum passa de g
```

### Existência

Para `a` e `b` positivos, sempre existe pelo menos um divisor comum:

```text
1 | a
1 | b
```

Como os divisores comuns não passam de `min(a,b)`, a busca é finita — dá para testar `1, 2, 3, ..., min(a,b)` e guardar o maior que divide os dois.

### Casos especiais

```text
MDC(a,a)=a
MDC(a,1)=1
MDC(a,0)=a, se a > 0
MDC(0,b)=b, se b > 0
MDC(0,0) é indefinido
```

### Coprimalidade

`a` e `b` são coprimos quando:

```text
MDC(a,b)=1
```

### Ainda não é Euclides

Esta etapa define o MDC por propriedade e busca finita. Ainda não usamos:

```text
MDC(a,b)=MDC(b, a mod b)
```

porque `mod` ainda não nasceu legitimamente no fluxo puro (chega na Etapa 6, Euclides por subtração, e na Etapa 9, Euclides por resto).

## Exemplo

- `MDC(12, 18) = 6`: divisores comuns de 12 e 18 são `1, 2, 3, 6` -- o maior é 6.
- `MDC(9, 28) = 1`: os únicos divisores comuns são `1` -- 9 e 28 são coprimos.
- `MDC(7, 0) = 7`: caso especial, qualquer número divide 0, então o próprio 7 já é o maior divisor comum possível.

## Dependências permitidas

- divisibilidade pura
- igualdade
- ordem
- existência limitada
- busca finita

## Conceitos proibidos nesta etapa

- divisão
- resto
- módulo
- algoritmo de Euclides por módulo
- primalidade
- fatoração prima

## Implementação

```text
nucleo/mdc_puro.py
```

Este arquivo não usa DIV, MOD, primos nem fatoração.

## Validação

```text
testes/test_pureza_conceitual.py
```
