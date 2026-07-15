# PSF-IAminy — Marcador histórico 1058: limite de função racional em ponto finito

## Construção pura

Liga `divisão de polinômios` (ETAPA 1056, Briot-Ruffini): a resposta legada
sem prova de `nucleo/conceitos_avancados_puros.py` ("Calcula: lim(x→2)
(x² - 4)/(x - 2). → 4, justificado por fatorar x²-4 em (x-2)(x+2)") só
tinha o resultado e a explicação em prosa — nenhuma fatoração de verdade
acontecia. Agora ela acontece: quando `a` é raiz do numerador e do
denominador ao mesmo tempo (indeterminação `0/0`), os dois se dividem
exatamente por `(x−a)` via Briot-Ruffini, e o limite é reavaliado no
quociente reduzido — não uma regra citada, uma divisão real repetida até
o denominador deixar de ter `a` como raiz.

```text
divisão de polinômios (ETAPA 1056)
→ Q(a) ≠ 0: limite = P(a)/Q(a), avaliação direta, sem indeterminação
→ Q(a) = 0 e P(a) ≠ 0: sem limite finito (a função diverge perto de a)
→ Q(a) = 0 e P(a) = 0: fatora (x−a) dos dois por Briot-Ruffini, repete
```

A repetição sempre termina: cada fatoração reduz o grau do denominador em
um, então depois de no máximo `grau(Q)` passos ou `Q(a)` deixa de ser
zero (limite encontrado) ou o polinômio se esgota (caso rejeitado como
entrada mal-formada, denominador nulo).

Esta etapa cobre só limite em ponto finito de função racional — nem
teoria geral de limites (exigiria reais completos, ETAPA 234, para
sequências arbitrárias), nem limites de funções não-racionais (seno,
exponencial). Limite no infinito e limites trigonométricos/exponenciais
continuam como próximo alvo.

## Dependências permitidas

- divisão polinômios

## Implementação

```text
nucleo/limite_racional_exato.py
```

## Validação

```text
testes/test_limite_racional_exato.py
```

## Estado

Limite de função racional em ponto finito construído e testado: os dois
exemplos clássicos de indeterminação `0/0` (`(x²-4)/(x-2)` em `x=2` dá 4;
`(x²-1)/(x-1)` em `x=1` dá 2), um caso sem indeterminação (avaliação
direta) e um caso de divergência genuína (denominador zera, numerador
não — sem limite finito, honestamente `None`, não um valor de infinito
fingido). Limite no infinito e limites de funções não-racionais
continuam como próximo alvo.
