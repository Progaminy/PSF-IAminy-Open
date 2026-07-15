# PSF-IAminy — Marcador histórico 1051: porcentagem

## Construção pura

**Porcentagem** é uma razão com denominador fixo em 100: "20%" é
literalmente `20/100`, e calcular "20% de 50" é multiplicar `50` pela
fração `20/100`, sempre mantida exata (nunca decimal aproximado). Isto
já estava construído em `nucleo/porcentagem.py` e já tinha teste real
em `testes/test_nucleo.py` e `testes/test_modelo_eficiente.py` — só
nunca tinha ganhado documento de etapa nem ponte própria auditada.
Esta etapa não constrói nada novo: registra o que já existia.

```text
igualdade + adição + multiplicação (primitivas, já construídas)
→ racionais finitos (RAC)
→ p% de n = p·n/100 (PORCENTAGEM_DE)
→ aumentar n em p% = n·(100+p)/100 (AUMENTAR_PERCENTUAL)
→ diminuir n em p% = n·(100−p)/100 (DIMINUIR_PERCENTUAL)
```

Porcentagem não é conhecimento novo: é racional com denominador 100,
construído sobre a mesma base de racionais finitos já provada. `100` em
si nasce por soma repetida de `2` cinco vezes dobrada (`10×10`), sem
importar nenhum literal numérico pronto.

`DIMINUIR_PERCENTUAL` usa subtração truncada (`SUB`), documentada no
próprio módulo: para `p > 100` (diminuir mais que 100%) o resultado
trunca em `0/100` em vez de ficar negativo — correto para o uso comum
(`p` entre 0 e 100), mas uma fronteira honesta, não escondida.

## Exemplo

- `25% de 80 = 20` (fração exata `2000/100`, reduzida).
- `80` aumentado em `25% = 100`; `80` diminuído em `25% = 60`.

## Dependências permitidas

- igualdade
- adição
- multiplicação
- racionais finitos

## Implementação

```text
nucleo/porcentagem.py
```

## Validação

```text
testes/test_nucleo.py
testes/test_modelo_eficiente.py
```

## Estado

Porcentagem de um valor, aumento e diminuição percentual construídos e
testados (já existiam; esta etapa fecha a ponte). Diminuir mais que 100%
com resultado negativo exigiria racionais assinados, e continua como
próximo alvo.
