# PSF-IAminy — Marcador histórico 1041: inequações lineares

## Construção pura

Resolver uma **inequação** é isolar x do mesmo jeito que numa equação
(ETAPA 133), com uma diferença crítica: multiplicar ou dividir os dois
lados por uma quantidade negativa inverte o sentido da comparação
(`<` vira `>`). Este ramo liga `ordem total` (ETAPA 69) a `equação de
primeiro grau` (ETAPA 133), sem introduzir nenhuma regra nova além
dessa inversão.

"Inequações" existia neste projeto só como texto de resposta legada
(`nucleo/conceitos_avancados_puros.py`): explicação e exemplo prontos, sem
prova PSF, código ou teste.

```text
ordem total (ETAPA 69) + equação primeiro grau finita (ETAPA 133)
→ a·x + b ⋈ c: subtrai b dos dois lados, divide por a
→ se a > 0: comparador mantém sentido
→ se a < 0: comparador inverte (multiplicar/dividir por negativo troca a ordem)
→ conferência: testar um valor de cada lado do limite na inequação original
```

A regra de inversão não é aceita "porque é conhecida": `resolver_inequacao_linear`
testa `limite+1` e `limite-1` diretamente na inequação original (antes de
isolar x) e levanta erro se a solução apontar para o lado errado. Isso
cobre os quatro comparadores (`>`, `>=`, `<`, `<=`) e os dois casos de
sinal do coeficiente.

Sistemas de inequações (interseção de soluções) e inequações quadráticas
continuam como próximo alvo desta mesma linha.

## Exemplo

- `2x + 3 > 7` -> `x > 2` (coeficiente positivo, sentido mantido).
- `-2x + 3 > 7` -> `x < -2` (coeficiente negativo, sentido invertido ao dividir por -2).

## Dependências permitidas

- ordem total
- equação primeiro grau finita
- ponte racionais reais

## Implementação

```text
nucleo/inequacoes.py
```

## Validação

```text
testes/test_inequacoes.py
```

## Estado

Inequação linear com um coeficiente construída e testada para os quatro
comparadores, com e sem inversão de sinal, cada solução conferida contra
a inequação original em dois pontos de teste. Sistemas de inequações e
inequações quadráticas continuam como próximo alvo.
