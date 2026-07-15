# PSF-IAminy — Etapas 601 a 640: Gramáticas livres de contexto naturais

Uma **gramática livre de contexto** gera strings a partir de regras de
substituição (ex.: "frase → sujeito verbo objeto"), sem que a escolha
de regra dependa do que veio antes — daí "livre de contexto". Ela
reconhece mais padrões do que um autômato finito consegue (ETAPA
521-560): consegue, por exemplo, exigir parênteses equilibrados, algo
que exige contar sem limite, impossível para uma máquina de estados
finitos. Este bloco constrói a gramática, a derivação de uma string a
partir dela, e a árvore de derivação que registra o caminho seguido.

## Exemplo

- Gramática clássica `aⁿbⁿ` (mesma quantidade de `a` seguida da mesma quantidade de `b`): gera `"ab"` e `"aabb"`, mas não `"abb"` (quantidades diferentes) -- confirmado tanto pela derivação quanto pelo reconhecedor CYK, que concordam nos dois casos.
- Árvore de derivação de `"ab"`: raiz `S`, ramifica em `A→a` e `B→b`, folhas `("a","b")`, profundidade 3.

## Posição no fluxo natural

Este bloco continua a partir da etapa 600. Ele não salta para conceitos futuros: constrói apenas o próximo arco natural e mantém todos os limites declarados.

```text
conceito anterior
↓
gramáticas livres de contexto naturais
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
| 601 | CFG finita revisitada |
| 602 | produção livre de contexto |
| 603 | derivação esquerda |
| 604 | derivação esquerda até limite |
| 605 | forma normal de Chomsky finita |
| 606 | produção terminal em CNF |
| 607 | produção binária em CNF |
| 608 | epsilon inicial em CNF |
| 609 | reconhecimento CYK finito |
| 610 | tabela triangular finita |
| 611 | base lexical da tabela |
| 612 | combinação binária da tabela |
| 613 | aceitação por símbolo inicial |
| 614 | rejeição por ausência do inicial |
| 615 | árvore sintática |
| 616 | raiz de árvore sintática |
| 617 | folhas de árvore sintática |
| 618 | profundidade de árvore sintática |
| 619 | catálogo CFG |
| 620 | concordância geração-CYK |
| 621 | parênteses como motivação anterior |
| 622 | linguagem anbn finita por CNF |
| 623 | ambiguidade como possibilidade |
| 624 | ambiguidade não decidida universalmente |
| 625 | parse como construção finita |
| 626 | limite de profundidade |
| 627 | limite de palavra |
| 628 | fronteira de catálogo |
| 629 | gramática versus reconhecedor |
| 630 | síntese de derivação e tabela |
| 631 | erro por gramática fora de CNF |
| 632 | separação terminal/não-terminal |
| 633 | não-terminal inicial preservado |
| 634 | reconhecimento sem derivar tudo |
| 635 | comparação externa de métodos |
| 636 | prova operacional limitada |
| 637 | CFL sem infinito atual |
| 638 | ponte com autômato de pilha finito |
| 639 | limite honesto CFG-PDA geral |
| 640 | fechamento CFG natural finito |

## Forma operacional no projeto

Implementado em `nucleo/gramaticas_livres_contexto_naturais.py` e validado em `testes/test_gramaticas_livres_contexto_naturais.py`.

## Validação externa mínima

O módulo é testado contra exemplos independentes e catálogos finitos. Quando a afirmação seria universal ou infinita, o documento declara a fronteira em vez de fingir prova geral.

## Limite honesto

A etapa 640 fecha apenas este arco finito. O próximo bloco deve nascer explicitamente no fluxo, sem usar o que ainda não foi construído.
