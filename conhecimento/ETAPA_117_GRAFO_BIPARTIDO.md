# PSF-IAminy — Etapa 117: Grafo bipartido

## Posição no fluxo natural

Esta etapa pertence ao bloco de grafos finitos, construído sobre relação binária e simetria (etapas 61-65).

## Construção pura

Os vértices dividem-se em 2 grupos onde toda aresta liga grupos diferentes — verificado por 2-coloração via busca. Testado: C4 (ciclo de 4) é bipartido; K3 (triângulo) não é.

## Dependências permitidas

- distinção; par ordenado; igualdade; domínio finito explícito;
- lógica booleana; relação binária, simetria, caminho (etapas 61-80);
- grafo relação simétrica.

## Dependências proibidas nesta etapa

- grafos infinitos; fluxo em redes; planaridade;
- teoria espectral de grafos; estruturas ainda não construídas.

## Forma operacional no projeto

Implementado em `nucleo/grafos_finitos.py` e validado em `testes/test_grafos_finitos.py`.
