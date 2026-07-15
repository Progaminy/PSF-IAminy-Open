# PSF-IAminy — Marcador histórico 1059: continuidade de função racional num ponto

## Construção pura

Liga `limite de função racional` (ETAPA 1058) e `divisão de polinômios`
(ETAPA 1056): a resposta legada de `nucleo/conceitos_avancados_puros.py`
("uma função é contínua em x=a se está definida em a, tem limite em a, e
esse limite é igual ao valor da função em a") tinha as três condições em
prosa, sem checar nenhuma delas. Aqui as três nascem dos mesmos cálculos
já provados, e são comparadas, não assumidas.

```text
limite de função racional (ETAPA 1058) + divisão de polinômios (ETAPA 1056)
→ definida_no_ponto: Q(a) ≠ 0 na expressão original (denominador não zera)
→ valor_no_ponto: P(a)/Q(a), só quando definida
→ limite_no_ponto: limite_racional_em_ponto (fatora (x−a) se precisar)
→ continua: definida E limite existe E os dois são iguais
```

O segundo exemplo legado ("f(x) = (x²-1)/(x-1) é contínua em x=1?" →
"não; o denominador fica zero, então a função não está definida ali")
mostra a distinção central desta etapa: o limite existe ali (2, por
fatoração de `(x-1)` via Briot-Ruffini), mas a função, na sua expressão
original, não está definida em `x=1` — dividir por zero não produz valor,
mesmo que o buraco seja "preenchível" no limite. Ter limite não é o
mesmo que ser contínua; essa é uma descontinuidade removível, não uma
ausência de comportamento. Quando `Q(a) ≠ 0`, as três condições sempre
batem por construção (o próprio `limite_racional_em_ponto` devolve
`P(a)/Q(a)` direto nesse caso) — mas a igualdade é conferida de verdade
a cada chamada, não hardcoded como suposição.

Esta etapa cobre só função racional (razão de polinômios). Continuidade
de funções não-racionais (trigonométricas, exponenciais) continua como
próximo alvo, dependendo de círculo unitário simbólico ou reais completos.

## Dependências permitidas

- limite racional exato
- divisão polinômios

## Implementação

```text
nucleo/continuidade_racional.py
```

## Validação

```text
testes/test_continuidade_racional.py
```

## Estado

Continuidade de função racional num ponto construída e testada: os dois
exemplos clássicos de descontinuidade removível (`(x²-1)/(x-1)` em
`x=1` e `(x²-4)/(x-2)` em `x=2`, ambos com limite mas sem valor definido
na expressão original), um caso contínuo (sem indeterminação) e um caso
de divergência genuína (nem valor nem limite finito). Continuidade de
funções não-racionais continua como próximo alvo.
