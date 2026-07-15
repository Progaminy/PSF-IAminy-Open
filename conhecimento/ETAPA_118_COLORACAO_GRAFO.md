# PSF-IAminy — Etapa 118: Coloração de grafo finito

## Posição no fluxo natural

Esta etapa pertence ao bloco de grafos finitos, construído sobre relação binária e simetria (etapas 61-65).

## Construção pura

Existe atribuição de até k cores onde vértices adjacentes nunca compartilham cor? Busca exaustiva — o problema é NP-difícil em geral, correto aqui porque o domínio é sempre finito e pequeno. Testado: K3 precisa de exatamente 3 cores (não 2), fato clássico de teoria dos grafos.

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana; relação binária, simetria, caminho (etapas 61-80);
- grafo relação simétrica.

## Dependências proibidas nesta etapa

- grafos infinitos; fluxo em redes; planaridade;
- teoria espectral de grafos; estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/grafos_finitos.py` e validado em `testes/test_grafos_finitos.py`.
