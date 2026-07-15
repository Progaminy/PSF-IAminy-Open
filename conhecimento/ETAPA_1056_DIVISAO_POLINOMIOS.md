# PSF-IAminy — Marcador histórico 1056: divisão de polinômios e Teorema do Resto

## Construção pura

Liga `polinômios anel` (ETAPA 101) e `grau operações polinomiais`
(ETAPA 102), que trabalhavam sobre um anel finito, ao domínio dos
racionais exatos (`ponte racionais reais`, ETAPA 1034): dividir um
polinômio por `(x−a)` é o algoritmo de Briot-Ruffini, e o resto dessa
divisão é exatamente `P(a)` — o Teorema do Resto não é aceito como fato
citado, é conferido calculando os dois caminhos de forma independente.

```text
polinômios anel (ETAPA 101) + racionais exatos (ETAPA 1034)
→ Briot-Ruffini: parciais[0] = c_n; parciais[i] = c_i + a·parciais[i-1]
→ quociente = parciais menos o último; resto = último parcial
→ conferência: resto tem que ser igual a P(a) por avaliação direta (Horner)
```

Um polinômio é representado como tupla de coeficientes do maior grau para
o menor — a mesma convenção de `digitos()` (ETAPA 1037), do mais
significativo primeiro. `avaliar_polinomio` usa o método de Horner (só
soma e produto, sem potência repetida, mesmo princípio de `raízes de
polinômios`, ETAPA 103). `dividir_por_x_menos_a` calcula o resto por
Briot-Ruffini e imediatamente confere contra a avaliação direta de `P(a)`;
se os dois caminhos divergirem, levanta erro em vez de silenciar a
divergência. `teorema_do_resto` e `eh_raiz` são consequências diretas
dessa conferência, não regras à parte.

Esta etapa cobre divisão apenas por `(x−a)` (grau 1). Divisão por
polinômios de grau maior continua como próximo alvo.

## Dependências permitidas

- polinômios anel
- grau operações polinomiais
- ponte racionais reais

## Implementação

```text
nucleo/divisao_polinomios.py
```

## Validação

```text
testes/test_divisao_polinomios.py
```

## Estado

Avaliação por Horner, divisão de Briot-Ruffini por `(x−a)` e Teorema do
Resto construídos e testados com o polinômio clássico
`x³-6x²+11x-6=(x-1)(x-2)(x-3)`, incluindo divisão por raiz conhecida
(resto zero) e por valor que não é raiz (resto igual a `P(a)`). Divisão
por polinômios de grau maior que 1 continua como próximo alvo.
