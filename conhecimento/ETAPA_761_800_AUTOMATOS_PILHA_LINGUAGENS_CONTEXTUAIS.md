# PSF-IAminy — Etapas 761–800
## autômatos com pilha finita e linguagens contextuais limitadas

Regra desta faixa: nenhum conceito é usado como fórmula pronta. Quando uma expressão conhecida aparece, ela é tratada apenas como validação externa ou como forma posterior de conferir a construção PSF.

Módulo operacional: `nucleo/automatos_pilha_finitos.py`
Teste: `testes/test_automatos_pilha_finitos.py`

## Fluxo interno

- 761 memória de pilha finita
- 762 símbolo de pilha
- 763 topo de pilha
- 764 empilhar
- 765 desempilhar
- 766 transição com pilha
- 767 autômato de pilha finito limitado
- 768 aceitação por estado final
- 769 aceitação por pilha vazia
- 770 execução com profundidade limite
- 771 linguagem reconhecida por catálogo
- 772 derivação livre de contexto revisitada
- 773 árvore sintática finita
- 774 ambiguidade por catálogo
- 775 conversão gramática→autômato limitada
- 776 conversão autômato→gramática limitada
- 777 linguagem não regular por testemunho finito
- 778 limite honesto do bombeamento
- 779 parênteses balanceados finitos
- 780 expressões aninhadas finitas
- 781 pilha como histórico
- 782 chamada e retorno finitos
- 783 escopo sintático finito
- 784 ligação de nomes finita
- 785 sombra de variável
- 786 contexto de análise
- 787 gramática contextual limitada
- 788 dependência de contexto
- 789 autômato linear limitado inicial
- 790 fita limitada
- 791 configuração de máquina limitada
- 792 transição de máquina limitada
- 793 aceitação por catálogo de configurações
- 794 simulação finita
- 795 não-terminação não decidida fora do limite
- 796 certificado de aceitação
- 797 certificado de rejeição limitada
- 798 equivalência de reconhecedores por catálogo
- 799 validação externa por exemplos
- 800 fechamento das linguagens com memória limitada

## Critério de honestidade

- Os objetos são finitos, explícitos ou limitados por catálogo.
- Quando uma construção infinita clássica seria necessária, o ficheiro marca o bloqueio em vez de fingir universalidade.
- Fórmulas clássicas podem aparecer em comentários de validação, mas a construção operacional usa enumeração, transformação ou busca finita.
