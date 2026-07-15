# PSF-IAminy — Marcador histórico 1034: ponte dos racionais aos reais

## Construção pura

Os naturais permitem contagem; inteiros acrescentam orientação de sinal;
racionais comparam partes inteiras. Um racional isolado ainda não representa
todas as grandezas contínuas. A próxima construção conserva uma grandeza entre
dois racionais e reduz progressivamente esse intervalo.

```text
naturais → inteiros → racionais assinados
→ ordem racional → intervalo racional
→ intervalos encaixados → aproximação racional certificada
→ futura construção de equivalência e completude dos reais
```

Uma sequência finita de intervalos encaixados certifica aproximação e erro. Ela
não é chamada de número real completo: ainda faltam sequência infinita ou lei
geradora, equivalência entre representações, operações preservadas, ordem,
limites e prova de completude.

## Dependências permitidas

- inteiros relativos puros
- racionais finitos
- ordem total
- sequências finitas

## Implementação

```text
nucleo/reais_intervalos_naturais.py
```

## Validação

```text
testes/test_reais_intervalos_naturais.py
```

## Estado

Ponte operacional construída; reais completos continuam como próximo alvo.
