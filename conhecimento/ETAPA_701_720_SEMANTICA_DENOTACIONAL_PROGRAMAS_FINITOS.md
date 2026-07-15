# PSF-IAminy — Etapas 701–720
## semântica denotacional finita e verificação de comandos finitos

Regra desta faixa: nenhum conceito é usado como fórmula pronta. Quando uma expressão conhecida aparece, ela é tratada apenas como validação externa ou como forma posterior de conferir a construção PSF.

Módulo operacional: `nucleo/semantica_denotacional_finita.py`
Teste: `testes/test_semantica_denotacional_finita.py`

## Fluxo interno

- 701 semântica denotacional finita
- 702 domínio semântico finito
- 703 ambiente como catálogo variável→valor
- 704 interpretação de expressão por árvore
- 705 equivalência operacional-denotacional por catálogo
- 706 ordem semântica finita
- 707 ponto fixo finito por iteração limitada
- 708 semântica de atribuição
- 709 semântica de sequência
- 710 semântica de condicional
- 711 laço com limite explícito
- 712 traço de execução
- 713 invariante de laço finito
- 714 pré-condição
- 715 pós-condição
- 716 tripla de Hoare finita
- 717 verificação por catálogo
- 718 correção parcial finita
- 719 terminação por limite/variante declarado
- 720 fechamento semântico de programas finitos

## Critério de honestidade

- Os objetos são finitos, explícitos ou limitados por catálogo.
- Quando uma construção infinita clássica seria necessária, o ficheiro marca o bloqueio em vez de fingir universalidade.
- Fórmulas clássicas podem aparecer em comentários de validação, mas a construção operacional usa enumeração, transformação ou busca finita.
