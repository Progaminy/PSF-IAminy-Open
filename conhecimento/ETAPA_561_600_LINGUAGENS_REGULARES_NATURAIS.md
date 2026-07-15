# PSF-IAminy — Etapas 561 a 600: Linguagens regulares naturais

Uma **linguagem regular** é o conjunto de todas as entradas que um
autômato finito (ETAPA 521-560) aceita — é a família de padrões que
essas máquinas simples conseguem reconhecer. Este bloco estuda as
propriedades dessa família: quais operações (união, interseção,
complemento, concatenação) mantêm uma linguagem regular, e que
limites genuínos existem (padrões que nenhum autômato finito consegue
reconhecer).

## Exemplo

- Regex `a*b` (zero ou mais `a` seguidos de um `b`): contém `"aaab"` (aceita) mas não contém `"aba"` (rejeitada, `b` no meio).
- Convertida para NFA e para DFA, a regex `a*b` concorda com os dois em todo um catálogo de entradas testado -- os três modelos reconhecem exatamente a mesma linguagem.

## Posição no fluxo natural

Este bloco continua a partir da etapa 560. Ele não salta para conceitos futuros: constrói apenas o próximo arco natural e mantém todos os limites declarados.

```text
conceito anterior
↓
linguagens regulares naturais
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
| 561 | linguagem regular como expressão finita |
| 562 | expressão vazia |
| 563 | expressão epsilon |
| 564 | expressão símbolo |
| 565 | união regular |
| 566 | concatenação regular |
| 567 | estrela limitada |
| 568 | alfabeto de regex |
| 569 | enumeração limitada de regex |
| 570 | pertencimento limitado |
| 571 | catálogo regular |
| 572 | construção de Thompson finita |
| 573 | estado inicial de Thompson |
| 574 | estado final de Thompson |
| 575 | epsilon em Thompson |
| 576 | NFA de símbolo |
| 577 | NFA de união |
| 578 | NFA de concatenação |
| 579 | NFA de estrela |
| 580 | regex para NFA |
| 581 | regex para DFA por determinização |
| 582 | concordância regex-NFA |
| 583 | concordância regex-DFA |
| 584 | fechamento regular por união |
| 585 | fechamento regular por concatenação |
| 586 | fechamento regular por estrela limitada |
| 587 | linguagem vazia reconhecível |
| 588 | palavra vazia reconhecível |
| 589 | símbolo reconhecível |
| 590 | distribuição testada por catálogo |
| 591 | limite da estrela sem infinito atual |
| 592 | derivação de regex como árvore |
| 593 | normalização simples de regex |
| 594 | equivalência por catálogo |
| 595 | contraexemplo por palavra |
| 596 | fronteira de tamanho máximo |
| 597 | regularidade não assumida universalmente |
| 598 | ponte regex-autômato |
| 599 | teste externo de reconhecimento |
| 600 | fechamento das linguagens regulares naturais |

## Forma operacional no projeto

Implementado em `nucleo/linguagens_regulares_naturais.py` e validado em `testes/test_linguagens_regulares_naturais.py`.

## Validação externa mínima

O módulo é testado contra exemplos independentes e catálogos finitos. Quando a afirmação seria universal ou infinita, o documento declara a fronteira em vez de fingir prova geral.

## Limite honesto

A etapa 600 fecha apenas este arco finito. O próximo bloco deve nascer explicitamente no fluxo, sem usar o que ainda não foi construído.
