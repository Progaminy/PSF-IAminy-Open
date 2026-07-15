# PSF-IAminy — Marcador histórico 1055: notação científica

## Construção pura

Notação científica liga potência (usada em potência modular, ETAPA 27, e
em progressão geométrica, ETAPA 1040) e a decomposição em dígitos
(`digitos`, ETAPA 1037): decompor um número inteiro positivo em notação
científica é contar quantas casas o primeiro dígito significativo
precisa andar — o próprio comprimento da lista de dígitos menos um.

```text
contas armadas (ETAPA 1037, digitos()) + potência
→ expoente = quantidade de dígitos de n menos um
→ mantissa = n / 10^expoente (sempre entre 1 e 10, exclusive o 10)
→ conferência: mantissa × 10^expoente tem que reconstruir n exatamente
```

O expoente não é decidido por inspeção visual do número escrito: nasce
diretamente da contagem de dígitos já construída em `digitos()`, e a
mantissa é conferida reconstruindo o valor original, não aceita só por
sair da divisão.

Esta etapa cobre inteiros positivos (números grandes, o caso pedido pela
aula de origem). Números entre 0 e 1 (expoente negativo, para números
muito pequenos) continuam como próximo alvo — exigiria representar
frações decimais exatas menores que 1 como entrada, não só inteiros.

## Dependências permitidas

- contas armadas
- potência modular

## Implementação

```text
nucleo/notacao_cientifica.py
```

## Validação

```text
testes/test_notacao_cientifica.py
```

## Estado

Notação científica de inteiros positivos construída e testada, incluindo
o caso de potência exata de dez. Números menores que 1 continuam como
próximo alvo.
