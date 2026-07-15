# PSF-IAminy — Marcador histórico 1054: conversão entre unidades

## Construção pura

Conversão entre unidades da mesma espécie de grandeza (metro/centímetro,
quilo/grama, hora/minuto) era um item deixado explicitamente em aberto na
ETAPA 1036 (medidas e grandezas). Este ramo estende `_GrandezaEscalar`
com um fator de conversão racional entre unidades da mesma espécie.

```text
medidas e grandezas (ETAPA 1036, _GrandezaEscalar)
→ FatorConversao: quantas unidades de destino cabem numa unidade de origem
→ converter = multiplicar o valor pelo fator, preservando a espécie
  (type(self)(...) — Comprimento continua Comprimento, nunca vira Massa)
→ conferência: desfazer com o fator recíproco tem que devolver o valor original
```

`converter` não aceita o resultado só por sair da multiplicação: desfaz a
conversão com o recíproco do fator e exige que o valor original volte
exatamente — a mesma disciplina de "ida e volta" já usada em
`nucleo/funcoes_avancadas.py` para conferir inversas.

## Dependências permitidas

- medidas e grandezas
- ponte racionais reais

## Implementação

```text
nucleo/conversao_unidades.py
```

## Validação

```text
testes/test_conversao_unidades.py
```

## Estado

Conversão metro/centímetro, quilo/grama e hora/minuto construída e
testada nos dois sentidos, com conferência de ida e volta. Outras
unidades da mesma espécie (km, tonelada, segundo) usam o mesmo
`FatorConversao` sem precisar de código novo.
