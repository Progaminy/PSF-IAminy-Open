# PSF-IAminy — Etapa 134: Binário posicional finito

## Posição no fluxo natural

A etapa 133 parou corretamente antes de equação de segundo grau, porque raiz quadrada geral exigiria uma representação mais eficiente que numerais unários de Church. O primeiro passo honesto para destravar essa lacuna não é prometer reais gerais: é formalizar uma aritmética posicional finita já dentro do núcleo.

Esta etapa continua o trabalho iniciado por `nucleo/binario.py`: o vetor de 10 bits deixa de ser apenas uma conversão/registro e ganha soma binária por carry.

## Construção pura

Um bit continua sendo `V` ou `F`. Um vetor binário continua sendo uma cadeia de `PAR`, em largura fixa de 10 bits, com o bit menos significativo primeiro.

A soma nasce por soma completa de um bit:

```text
soma = a xor b xor carry
carry' = (a e b) ou (carry e (a xor b))
```

Depois o carry é propagado estruturalmente pelas 10 posições fixas. O carry final é descartado, portanto a semântica é a de um registrador finito:

```text
SOMA_BINARIA(a,b) representa (a+b) mod 1024
```

Isso ainda não resolve raiz quadrada geral. Resolve apenas o primeiro degrau que faltava: operação posicional por dígitos, sem depender de divisão, resto ou módulo.

## Domínio declarado

- largura fixa: 10 bits;
- valores representáveis diretamente: 0 a 1023;
- soma com overflow: resultado reduzido modulo 1024 pela própria queda do carry final;
- validação exaustiva: todos os pares em `[0,31] × [0,31]`;
- validação de borda: `1023+1`, `900+200` e conferências internas selecionadas.

## Dependências permitidas

- primitivas `V`, `F`, `PAR`, `ITER`;
- lógica booleana já construída (`E`, `OU`, `XOR`);
- aritmética unária apenas para ida/volta e verificação (`SOMA`, `MULT`, `POT`, `IGUAL`).

## Dependências proibidas nesta etapa

- `DIV`, `MOD`, `MDC`, `MMC`;
- primalidade, fatoração, divisores;
- operadores nativos `/`, `//`, `%` dentro do núcleo.

## Forma operacional no projeto

Implementado em `nucleo/binario.py` e validado em `testes/test_binario_posicional_finito.py`.

## Próximo limite honesto

Para substituir de verdade os naturais unários em `reais.py`, ainda faltam operações posicionais maiores: comparação, subtração com borrow, multiplicação e divisão binária. Esta etapa grava só a soma, porque é o primeiro conceito que precisa nascer.
