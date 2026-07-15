# PSF-IAminy — Etapas 641 a 680: Semântica e tipos finitos

Um **sistema de tipos** classifica expressões (números, booleanos,
funções) para pegar erros ANTES de executar o programa: `2 + verdadeiro`
é rejeitado por tipagem, sem precisar rodar nada para descobrir que é
inválido. Este bloco constrói tipos finitos (`Nat`, `Bool`), as regras
que decidem se uma expressão é bem tipada, e a propriedade central de
todo sistema de tipos sério — **preservação de tipo** (se uma expressão
bem tipada dá um passo de avaliação, o resultado continua bem tipado) —
provada por catálogo finito de casos, não por indução geral sobre
programas arbitrários.

## Exemplo

- `se (1+1==2) então 3×4 senão 0`: os dois ramos do if têm tipo `Nat`, então a expressão inteira tem tipo `Nat` e avalia para `12`.
- `verdadeiro + 1`: rejeitado como mal tipado antes de qualquer execução -- adição exige `Nat` dos dois lados, e `verdadeiro` tem tipo `Bool`.

## Posição no fluxo natural

Este bloco continua a partir da etapa 640. Ele não salta para conceitos futuros: constrói apenas o próximo arco natural e mantém todos os limites declarados.

```text
conceito anterior
↓
semântica e tipos finitos
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
| 641 | tipo como classificação finita |
| 642 | tipo Nat |
| 643 | tipo Bool |
| 644 | expressão booleana |
| 645 | if finito |
| 646 | igualdade tipada |
| 647 | contexto de tipos |
| 648 | juízo de tipagem |
| 649 | variável tipada |
| 650 | literal tem tipo Nat |
| 651 | booleano tem tipo Bool |
| 652 | adição exige Nat |
| 653 | multiplicação exige Nat |
| 654 | igualdade exige tipos iguais |
| 655 | if exige Bool |
| 656 | ramos do if com mesmo tipo |
| 657 | let estende contexto |
| 658 | expressão bem tipada |
| 659 | expressão mal tipada |
| 660 | avaliação tipada |
| 661 | valor Nat |
| 662 | valor Bool |
| 663 | erro de tipo antes da execução |
| 664 | preservação de tipo |
| 665 | catálogo de ambientes |
| 666 | equivalência contextual finita |
| 667 | substituição finita por let |
| 668 | segurança semântica limitada |
| 669 | progresso não universal |
| 670 | progresso por catálogo |
| 671 | separação valor/tipo |
| 672 | semântica operacional tipada |
| 673 | prova por avaliação finita |
| 674 | contraexemplo tipado |
| 675 | fronteira de contexto |
| 676 | fronteira de linguagem |
| 677 | normalização não assumida |
| 678 | equivalência por observação |
| 679 | ponte para análise sintática |
| 680 | fechamento semântica-tipos finitos |

## Forma operacional no projeto

Implementado em `nucleo/semantica_tipos_finitos.py` e validado em `testes/test_semantica_tipos_finitos.py`.

## Validação externa mínima

O módulo é testado contra exemplos independentes e catálogos finitos. Quando a afirmação seria universal ou infinita, o documento declara a fronteira em vez de fingir prova geral.

## Limite honesto

A etapa 680 fecha apenas este arco finito. O próximo bloco deve nascer explicitamente no fluxo, sem usar o que ainda não foi construído.
