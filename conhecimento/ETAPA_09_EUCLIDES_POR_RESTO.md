# ETAPA 09 — Euclides por resto

## Estado anterior

Já temos:

```text
MDC por definição
MDC por subtração
quociente puro
resto puro
divisão euclidiana pura
```

Agora o algoritmo de Euclides por resto pode nascer legitimamente.

## Ideia

O algoritmo por subtração remove uma cópia do menor número por vez.

O algoritmo por resto remove várias cópias de uma só vez, porque a divisão euclidiana já nos dá a sobra final.

## Regra

```text
MDC(a,0)=a
MDC(a,b)=MDC(b, resto(a,b))
```

## Interpretação PSF

O Euclides por resto não é um conceito independente.

Ele é uma compressão do Euclides por subtração.

Por isso sua validade precisa conferir com:

```text
MDC por subtração
MDC por definição pura
```

## Exemplo

- `MDC(48, 18)` por resto: `resto(48,18)=12` -> `MDC(48,18)=MDC(18,12)`; `resto(18,12)=6` -> `MDC(18,12)=MDC(12,6)`; `resto(12,6)=0` -> `MDC(12,6)=MDC(6,0)=6`. Confere com Euclides por subtração (Etapa 6): `MDC(18,12)=6`.
- Note que esse caminho (48,18)->(18,12)->(12,6)->(6,0) é bem mais curto que repetir subtrações 1 a 1 -- é exatamente essa a "compressão" que o resto traz.

## Forma operacional no projeto

`nucleo/euclides_resto_puro.py`
`testes/test_divisao_euclidiana_pura.py`
