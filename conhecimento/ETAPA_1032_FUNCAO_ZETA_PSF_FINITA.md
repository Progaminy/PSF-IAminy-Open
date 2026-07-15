# ETAPA 1032 — Função zeta PSF finita

## Regra

A função zeta não entra como fórmula pronta. Entra como reconstrução por camadas.

Não fazemos:

```text
ζ(s) = fórmula aceite, portanto usar.
```

Fazemos:

```text
número natural
↓
potência por multiplicação repetida
↓
peso inverso racional 1/(n^s)
↓
soma finita desses pesos
↓
comparação posterior com produto sobre primos
```

## Construção PSF

Para cada número positivo `n` e profundidade `s`:

```text
n^s nasce de multiplicar n por si mesmo repetidamente.
```

Depois criamos o peso:

```text
peso(n,s) = par racional (1, n^s)
```

Aqui o racional é apenas um par:

```text
(numerador, denominador)
```

Não há divisão nativa.
Não há simplificação automática por MDC.
Não há fórmula externa.

A zeta finita é:

```text
zeta_finita(s,N) = peso(1,s) + peso(2,s) + ... + peso(N,s)
```

A soma racional nasce de multiplicação cruzada construída.

## Camada de validação: produto de Euler finito

O produto de Euler não é fundamento nesta etapa. Ele entra marcado como validação estrutural posterior.

Fluxo:

```text
primalidade por retirada repetida
↓
lista finita de primos
↓
para cada primo p, construir p^s
↓
criar fator p^s/(p^s-1)
↓
comparar comportamento da soma e do produto finitos
```

Essa camada só é permitida porque já construímos:

```text
primalidade
fatoração
TFA
operações racionais finitas
```

## O que isto ainda NÃO é

Esta etapa não resolve a Hipótese de Riemann.

Ainda faltam:

```text
reais completos
complexos
séries infinitas
limites
continuação analítica
zeros complexos
espectro/operadores
```

Logo, o PSF registra a função zeta como tentativa aplicável porque ela gerou efeito real na matemática, mas só aceita a camada finita como reconstruída por agora.

## Ficheiros

```text
nucleo/zeta_psf_finita.py
testes/test_zeta_psf_finita.py
```
