# PSF-IAminy — Marcador histórico 1040: progressões aritméticas e geométricas

## Construção pura

Uma **progressão** é a recorrência mais simples que existe: cada termo
nasce do anterior por uma única operação repetida — somar sempre a
mesma razão (progressão aritmética) ou multiplicar sempre pela mesma
razão (progressão geométrica). Não é conhecimento novo, é o caso mais
restrito de `recorrências` (ETAPA 49) e `sequências finitas` (ETAPA 48)
já construídas.

"Progressões" existia neste projeto só como texto de resposta legada
(`nucleo/conceitos_avancados_puros.py`): explicação e exemplo prontos, sem
prova PSF, código ou teste.

```text
recorrências (ETAPA 49) e sequências finitas (ETAPA 48)
→ progressão aritmética: a_1, a_k = a_{k-1} + razão
→ progressão geométrica: a_1, a_k = a_{k-1} × razão
→ forma fechada (a_n = a_1+(n-1)·razão ou a_1×razão^(n-1))
  conferida contra o termo calculado pela própria recorrência
→ soma dos n primeiros termos, conferida contra a soma termo a termo
```

Nenhuma fórmula fechada entra "porque é conhecida": `termo_geral` e
`soma_termos` calculam a forma fechada e comparam contra o resultado
construído pela recorrência (ou pela soma direta), levantando erro se
divergirem — mesma disciplina de conferência já usada em
`nucleo/contas_armadas.py`. Na progressão geométrica, a razão 1 é tratada
à parte (soma constante `a_1 × n`), evitando dividir por zero na fórmula
`(razão^n − 1)/(razão − 1)`.

Progressões infinitas (limite da soma quando `|razão| < 1`) dependem de
"reais completos" (ainda em aberto, ETAPA 1035) e continuam como próximo
alvo.

## Exemplo

- Aritmética: 2, 5, 8, 11, ... (razão +3) -- termo geral `2+3(n-1)`, soma dos 4 primeiros = 26.
- Geométrica: 3, 6, 12, 24, ... (razão ×2) -- termo geral `3×2^(n-1)`, soma dos 4 primeiros = 45.

## Dependências permitidas

- recorrências
- sequências finitas
- ponte racionais reais

## Implementação

```text
nucleo/progressoes.py
```

## Validação

```text
testes/test_progressoes.py
```

## Estado

Progressão aritmética e geométrica construídas e testadas: termo geral e
soma dos n primeiros termos, cada forma fechada conferida contra a
recorrência ou soma direta que a define. Soma infinita continua como
próximo alvo, depois de reais completos.
