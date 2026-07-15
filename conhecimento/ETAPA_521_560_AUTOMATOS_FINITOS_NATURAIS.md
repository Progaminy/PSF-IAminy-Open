# PSF-IAminy — Etapas 521 a 560: Autômatos finitos naturais

Um **autômato finito** é uma máquina de estados: começa num estado
inicial, lê símbolos um a um, muda de estado seguindo regras fixas, e
aceita ou rejeita a entrada dependendo de onde parou. É o modelo mais
simples de "reconhecer um padrão" — sem memória além do estado atual,
sem fita, sem pilha. Este bloco constrói autômatos determinísticos e
não-determinísticos, e a prova de que os dois reconhecem exatamente as
mesmas linguagens (equivalência), em domínio finito.

## Exemplo

- DFA que reconhece "número par de `a`": lendo `"a","b","a"` o traço de estados é `(par, ímpar, ímpar, par)` -- termina em `par`, então aceita.
- O complemento desse DFA rejeita exatamente onde o original aceita; a interseção com um segundo DFA ("termina em `b`") exige as duas condições ao mesmo tempo.

## Posição no fluxo natural

Este bloco continua a partir da etapa 520. Ele não salta para conceitos futuros: constrói apenas o próximo arco natural e mantém todos os limites declarados.

```text
conceito anterior
↓
autômatos finitos naturais
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
| 521 | máquina finita como transição |
| 522 | estado finito |
| 523 | alfabeto de entrada |
| 524 | transição total determinística |
| 525 | estado inicial |
| 526 | estado final |
| 527 | passo de DFA |
| 528 | execução de DFA |
| 529 | aceitação por estado final |
| 530 | rejeição por estado não-final |
| 531 | complemento de DFA |
| 532 | produto de autômatos |
| 533 | união de DFA |
| 534 | interseção de DFA |
| 535 | catálogo de palavras |
| 536 | equivalência por catálogo |
| 537 | não-determinismo finito |
| 538 | transição epsilon |
| 539 | fecho epsilon |
| 540 | movimento de NFA |
| 541 | execução de NFA |
| 542 | aceitação de NFA |
| 543 | conjunto de estados atuais |
| 544 | construção por subconjuntos |
| 545 | tradução NFA para DFA |
| 546 | concordância NFA-DFA por catálogo |
| 547 | linguagem reconhecida finitamente |
| 548 | fronteira de alfabeto |
| 549 | erro por símbolo externo |
| 550 | máquina total versus parcial |
| 551 | estado lixo explícito |
| 552 | determinização finita |
| 553 | fechamento por complemento |
| 554 | fechamento por união |
| 555 | fechamento por interseção |
| 556 | diferença por interseção com complemento |
| 557 | equivalência operacional finita |
| 558 | prova por teste de catálogo |
| 559 | limite honesto de equivalência geral |
| 560 | fechamento dos autômatos finitos naturais |

## Forma operacional no projeto

Implementado em `nucleo/automatos_finitos_naturais.py` e validado em `testes/test_automatos_finitos_naturais.py`.

## Validação externa mínima

O módulo é testado contra exemplos independentes e catálogos finitos. Quando a afirmação seria universal ou infinita, o documento declara a fronteira em vez de fingir prova geral.

## Limite honesto

A etapa 560 fecha apenas este arco finito. O próximo bloco deve nascer explicitamente no fluxo, sem usar o que ainda não foi construído.
