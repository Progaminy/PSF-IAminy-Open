# PSF-IAminy — Etapa 116: Árvore como grafo especial

## Posição no fluxo natural

Esta etapa pertence ao bloco de grafos finitos, construído sobre relação binária e simetria (etapas 61-65).

## Construção pura

Uma árvore é um grafo conexo com exatamente |V|-1 arestas — a caracterização clássica, usada em vez de buscar ciclos explicitamente. Testado: uma estrela (centro + 3 folhas, 3 arestas, 4 vértices) é árvore; K4 (6 arestas) não é.

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana; relação binária, simetria, caminho (etapas 61-80);
- conectividade grafo.

## Dependências proibidas nesta etapa

- grafos infinitos; fluxo em redes; planaridade;
- teoria espectral de grafos; estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/grafos_finitos.py` e validado em `testes/test_grafos_finitos.py`.
