# PSF-IAminy — Etapa 5: Diferença controlada

## Lei da etapa

A diferença `a-b` só pode existir como número natural quando `a >= b`.

A subtração truncada já existia como mecanismo operacional de Peano, mas o PSF-IAminy agora separa claramente:

- operação operacional: `SUB(a,b)`;
- validade conceitual: `a >= b`;
- diferença controlada: `a-b` apenas quando definida.

## Definição

```text
diferenca_definida(a,b) ⇔ a >= b
```

```text
diferenca_controlada(a,b) = a-b, se a >= b
```

Se `a < b`, o sistema pode devolver `ZERO` como sentinela operacional, mas isso não deve ser lido como diferença matemática verdadeira.

## Teorema de reconstituição

Se `a >= b`, então:

```text
(a-b)+b = a
```

Este teorema impede que a diferença seja apenas truque computacional.
Ela precisa reconstruir o valor original.

## Teorema de preservação dos divisores comuns

Se:

```text
d | a
d | b
a >= b
```

então:

```text
d | (a-b)
```

Justificação pura:

```text
a = d×x
b = d×y
a-b = d×x - d×y = d×(x-y)
```

No núcleo computacional, não dependemos de fatoração nem de divisão; apenas testamos a propriedade pela definição de divisibilidade:

```text
d | n ⇔ existe k tal que d×k = n
```

## Teorema inverso

Se:

```text
d | b
d | (a-b)
a >= b
```

então:

```text
d | a
```

porque:

```text
a = (a-b)+b
```

## Conclusão

Agora já podemos justificar o passo central de Euclides por subtração:

```text
MDC(a,b) = MDC(a-b,b), quando a >= b
```

mas ainda não usamos resto, módulo nem divisão.

## Exemplo

- `7 - 3 = 4` está definida (`7 >= 3`), e reconstitui: `4 + 3 = 7`.
- `3 - 7` NÃO está definida como diferença controlada (`3 < 7`) -- o sistema pode devolver `ZERO` como sentinela, mas isso não é "a resposta é zero", é "esta pergunta não tem diferença natural aqui".
- Preservação de divisor comum: `6 | 18` e `6 | 12`, `18 >= 12`, então `6 | (18-12) = 6 | 6` -- confere.

## Forma operacional no projeto

`nucleo/diferenca_controlada.py`
`testes/test_fluxo_natural_sem_dependencias.py`
