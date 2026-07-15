# PSF-IAminy — Marcador histórico 1049: paridade (par e ímpar)

## Construção pura

"Pares e ímpares" existia neste projeto só como caso implícito dentro de
`divisibilidade pura` (ETAPA 3: "n é par" é exatamente `2 | n`), nunca
nomeado à parte nem testado como propriedade própria. Este ramo liga a
`resto e divisão euclidiana` (ETAPA 8) e à aritmética escolar nativa
(`dividir_com_resto`, Etapa 31): resto 0 é par, resto 1 é ímpar — nenhuma
outra construção é necessária, porque o resto de dividir por dois só pode
ser 0 ou 1.

```text
resto e divisão euclidiana (ETAPA 8) + aritmética escolar nativa
→ eh_par(n): resto de n por dois é zero
→ eh_impar(n): não é par
→ paridade_da_soma(a,b): decide par+par=par, ímpar+ímpar=par,
  par+ímpar=ímpar pela regra clássica — e confere contra somar de
  verdade e checar a paridade do resultado, não aceita por decoreba
```

A regra clássica de paridade da soma não entra como fato memorizado:
`paridade_da_soma` calcula a soma de verdade (Etapa 31) e confere que a
paridade do resultado bate com o que a regra previu, levantando erro se
divergirem — mesma disciplina de conferência já usada em
`nucleo/progressoes.py` e `nucleo/contas_armadas.py`.

## Dependências permitidas

- divisibilidade pura
- resto e divisão euclidiana

## Implementação

```text
nucleo/paridade.py
```

## Validação

```text
testes/test_paridade.py
```

## Estado

Par, ímpar e a regra de paridade da soma construídos e testados, com a
regra conferida contra o cálculo direto em cada caso (par+par,
ímpar+ímpar, par+ímpar). Paridade do produto continua como próximo alvo
natural, mesma linha.
