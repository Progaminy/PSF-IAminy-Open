# PSF-IAminy — Marcador histórico 1048: equação quadrática exata (fórmula resolvente)

## Construção pura

A "equação quadrática finita" já existente (ETAPA 135,
`RESOLVER_QUADRATICA_FINITA_PURA`) testa cada valor de um domínio finito
dado — busca, não fórmula. Esta etapa constrói a fórmula resolvente de
verdade: `x = (−b ± √(b²−4ac)) / 2a`, mas só aceita o resultado quando o
discriminante é quadrado perfeito de um racional. Quando não é (a maioria
dos casos — as raízes seriam irracionais), a construção declara isso
honestamente, sem aproximar: esse caso mais geral depende de reais
completos (ETAPA 1035, próximo alvo).

```text
ponte racionais reais (ETAPA 1034/1035)
→ discriminante = b² − 4ac
→ √discriminante exato: só quando numerador e denominador (já reduzidos)
  forem quadrados perfeitos de inteiro — busca direta, sem raiz nativa
→ se não for quadrado perfeito: None, honestamente, não aproximação
→ se for: x1, x2 pela fórmula, cada um conferido substituindo de volta
  em a·x²+b·x+c
```

`raiz_quadrada_exata_ou_none` não é a lei geradora de raiz quadrada
(ETAPA 1035) — aquela aproxima qualquer raiz, inclusive irracional; esta
só aceita quando a raiz é exatamente racional, e devolve `None` em vez de
aproximar quando não é. São dois problemas diferentes: um aproxima, o
outro decide se uma aproximação é sequer necessária.

Testado com raízes inteiras distintas, raiz dupla (discriminante zero) e
o caso honestamente sem resposta exata (`x²−2=0`, discriminante 8, não é
quadrado perfeito).

## Dependências permitidas

- equação quadrática finita
- fatoração pura
- ponte racionais reais

## Implementação

```text
nucleo/equacao_quadratica_exata.py
```

## Validação

```text
testes/test_equacao_quadratica_exata.py
```

## Estado

Raiz quadrada exata de racional e fórmula resolvente construídas e
testadas, com raízes conferidas por substituição. Discriminante não
quadrado perfeito continua honestamente sem solução exata, como próximo
alvo depois de reais completos.
