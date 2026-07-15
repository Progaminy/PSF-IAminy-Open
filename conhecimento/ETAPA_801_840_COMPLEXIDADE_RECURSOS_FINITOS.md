# PSF-IAminy — Etapas 801–840
## complexidade como contagem finita de recursos, sem assintótica fingida

Regra desta faixa: nenhum conceito é usado como fórmula pronta. Quando uma expressão conhecida aparece, ela é tratada apenas como validação externa ou como forma posterior de conferir a construção PSF.

Módulo operacional: `nucleo/complexidade_recursos_finitos.py`
Teste: `testes/test_complexidade_recursos_finitos.py`

## Fluxo interno

- 801 recurso computacional
- 802 passo contado
- 803 memória contada
- 804 custo de transição
- 805 custo de algoritmo por traço
- 806 tabela de custos finita
- 807 comparação finita de custos
- 808 dominância por catálogo
- 809 crescimento observado finito
- 810 limite da extrapolação
- 811 classe finita de custo
- 812 melhor caso por catálogo
- 813 pior caso por catálogo
- 814 caso médio por catálogo
- 815 orçamento de execução
- 816 algoritmo aceitável sob orçamento
- 817 redução finita entre problemas
- 818 certificado de redução
- 819 verificação de solução
- 820 problema de decisão finito
- 821 problema de busca finito
- 822 problema de otimização finito
- 823 força bruta como baseline
- 824 poda por propriedade já provada
- 825 memoização como tabela construída
- 826 programação dinâmica finita
- 827 recorrência operacional
- 828 desdobramento de recorrência
- 829 árvore de chamadas
- 830 largura da busca
- 831 profundidade da busca
- 832 custo acumulado
- 833 regressão de desempenho do motor
- 834 perfil padrão
- 835 perfil completo
- 836 timeout honesto
- 837 orçamento global
- 838 teste pesado declarado
- 839 validação independente
- 840 fechamento de complexidade finita

## Critério de honestidade

- Os objetos são finitos, explícitos ou limitados por catálogo.
- Quando uma construção infinita clássica seria necessária, o ficheiro marca o bloqueio em vez de fingir universalidade.
- Fórmulas clássicas podem aparecer em comentários de validação, mas a construção operacional usa enumeração, transformação ou busca finita.
