# PSF-IAminy — Etapa 111: Grafo como relação binária sobre vértices finitos

## Posição no fluxo natural

Esta etapa pertence ao bloco de grafos finitos, construído sobre relação binária e simetria (etapas 61-65).

## Construção pura

Um grafo não-dirigido é uma relação binária SIMÉTRICA (etapa 64) sobre um conjunto finito de vértices — não uma estrutura nova. Uma aresta {a,b} é representada pelos dois pares (a,b) e (b,a), verificável com SIMETRICA_PURA já existente.

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana; relação binária, simetria, caminho (etapas 61-80);

## Dependências proibidas nesta etapa

- grafos infinitos; fluxo em redes; planaridade;
- teoria espectral de grafos; estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/grafos_finitos.py` e validado em `testes/test_grafos_finitos.py`.
