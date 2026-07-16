# Avaliação de qualidade matemática e linguística

Esta é uma avaliação pública pequena e executável. Ela serve como primeiro
baseline, não como certificação geral dos motores.

```bash
python3 avaliacoes/avaliar_matematica.py
python3 avaliacoes/avaliar_portugues.py
```

## Matemática

Foram avaliados sete casos de cálculo:

- precedência em `2+2*3`;
- parênteses em `(2+2)*3`;
- divisão racional exata `12:5`;
- decimal periódico truncado `1:3`;
- decimal arredondado `2:3`;
- divisão não nula por zero `12:0`;
- indeterminação `0:0`.

Cada caso verifica resultado, forma exata, estado, presença de passos,
justificativas não vazias e limite explícito quando aproximado ou indefinido.
Uma derivação por modus ponens encadeado verifica ainda o certificado no
fragmento lógico finito.

Resultado de 17 de julho de 2026:

```text
7/7 casos de cálculo aprovados
1/1 prova finita aprovada
estado: APROVADO_NO_ESCOPO_FINITO
```

Isso não prova correção para toda expressão, número, precisão nem lógica fora
do fragmento implementado. A amostra foi escolhida para capacidades públicas
centrais e casos indefinidos, não sorteada de uma população externa.

## Português

A avaliação verifica:

- `nao` inclui `não` entre as sugestões;
- `nda` inclui `nada`;
- o corretor sugere sem reescrever silenciosamente;
- `felizmente` e `incomum` são segmentadas sobre radicais confirmados;
- `desumano` e `resto` recusam cortes morfológicos falsos conhecidos;
- “interpretação” possui caminho de dependências;
- a auditoria estrutural permanece sem duplicações nem ciclos.

Esses pontos passaram. Porém, numa amostra deliberadamente pequena de oito
palavras válidas, quatro receberam sugestão ortográfica indevida:

```text
assunto, comprimento, sala, medido
4/8 falsos positivos = 50% nesta amostra
estado: PARCIAL_COM_FALSOS_POSITIVOS
```

Essa taxa não estima desempenho geral da língua: oito palavras não são corpus
representativo. Ela prova algo mais limitado e útil — o corretor atual ainda
pode tratar palavras válidas fora ou inconsistentes no léxico como erro. Por
isso, suas sugestões precisam continuar consultivas e não podem ser aplicadas
automaticamente.

## Próxima avaliação

1. criar corpus versionado com palavras/frases válidas e erros reais, separado
   por variedade e fenómeno;
2. medir precisão, revocação e falsos positivos por categoria;
3. aumentar casos matemáticos por domínio e borda, com geração independente;
4. comparar resultados com ferramentas externas em ambiente isolado;
5. registar toda divergência em `docs/VALIDACAO_EXTERNA.md`.

As avaliações executáveis falham com código de saída não zero quando as
expectativas centrais deixam de ser satisfeitas. Limitações conhecidas, como os
falsos positivos acima, aparecem no JSON e no estado em vez de serem apagadas.

