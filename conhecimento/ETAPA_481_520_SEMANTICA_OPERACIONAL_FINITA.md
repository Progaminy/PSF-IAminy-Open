# PSF-IAminy — Etapas 481 a 520: Semântica operacional finita

**Semântica operacional** define o significado de uma expressão pelos
passos concretos que a transformam em valor — não pelo resultado final
sozinho, mas pela sequência de reduções que leva até ele (ex.: `2+3` se
reduz a `5` num passo; `(2+3)*4` primeiro reduz `2+3` a `5`, depois
`5*4` a `20`). É diferente de só "calcular o resultado": aqui cada
passo intermediário é uma afirmação verificável por si só. Este bloco
constrói essa noção de passo/redução sobre um catálogo finito de
termos, sem afirmar que toda expressão sempre termina (divergência
continua honestamente possível, não escondida).

## Exemplo

- `2+3` reduz a `5` num único passo.
- `(2+3)*4` reduz em dois passos: primeiro `2+3` vira `5`, depois `5*4` vira `20` -- cada passo intermediário é verificável por si só, não só o resultado final.

## Posição no fluxo natural

Este bloco continua a partir da etapa 480. Ele não salta para conceitos futuros: constrói apenas o próximo arco natural e mantém todos os limites declarados.

```text
conceito anterior
↓
semântica operacional finita
↓
validação finita por catálogo/teste
```

## Regra de pureza

Não usa como dependência:

- divisão nativa, resto nativo ou aritmética modular escondida;
- primalidade, fatoração ou módulos antigos de divisores;
- infinitos atuais ou equivalência universal sem fronteira;
- teoremas futuros ainda não construídos.

## Etapas registadas

| Etapa | Conceito |
|---|---|
| 481 | configuração operacional finita |
| 482 | estado, entrada, memória e saída |
| 483 | regra operacional finita |
| 484 | condição de aplicabilidade |
| 485 | ação de transição |
| 486 | passo operacional determinístico |
| 487 | traço de execução finito |
| 488 | limite de passos como fronteira |
| 489 | combustível explícito |
| 490 | terminação até limite declarado |
| 491 | linguagem de expressões finitas |
| 492 | literal natural |
| 493 | variável finita |
| 494 | adição de expressões |
| 495 | multiplicação de expressões |
| 496 | ambiente finito |
| 497 | let finito |
| 498 | avaliação por redução |
| 499 | erro por variável livre |
| 500 | limite honesto de avaliação |
| 501 | termo finito |
| 502 | regra de reescrita |
| 503 | reescrita na raiz |
| 504 | reescrita em subtermo |
| 505 | um passo de reescrita |
| 506 | forma normal finita |
| 507 | catálogo de termos |
| 508 | confluência por catálogo |
| 509 | estratégia operacional |
| 510 | determinismo declarado |
| 511 | semântica pequena etapa |
| 512 | semântica grande etapa por traço |
| 513 | programa finito mínimo |
| 514 | equivalência operacional por catálogo |
| 515 | divergência não afirmada universalmente |
| 516 | paragem por falta de regra |
| 517 | execução auditável |
| 518 | separação sintaxe/semântica |
| 519 | teste externo de avaliação |
| 520 | fechamento da semântica operacional finita |

## Forma operacional no projeto

Implementado em `nucleo/semantica_operacional_finita.py` e validado em `testes/test_semantica_operacional_finita.py`.

## Validação externa mínima

O módulo é testado contra exemplos independentes e catálogos finitos. Quando a afirmação seria universal ou infinita, o documento declara a fronteira em vez de fingir prova geral.

## Limite honesto

A etapa 520 fecha apenas este arco finito. O próximo bloco deve nascer explicitamente no fluxo, sem usar o que ainda não foi construído.
